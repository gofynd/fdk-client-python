# FDK Python

![GitHub requirements.txt version](https://img.shields.io/github/package-json/v/gofynd/fdk-client-python?style=plastic)
![GitHub Workflow Status](https://img.shields.io/github/workflow/status/gofynd/fdk-client-python?style=plastic)
![GitHub](https://img.shields.io/github/license/gofynd/fdk-client-python?style=plastic)
[![Coverage Status](https://coveralls.io/repos/github/gofynd/fdk-client-python/badge.svg)](https://coveralls.io/github/gofynd/fdk-client-python)

FDK client for python

## Getting Started

Get started with the python Development SDK for Fynd Platform

### Usage

```bash
pip install "git+https://github.com/gofynd/fdk-client-python.git@3.17.1#egg=fdk_client"
```

Using this method, you can `import` fdk-client-python like so:

```python
from fdk_client.application.ApplicationClient import ApplicationClient
```

---

### Log Curl

To print the curl command in the console for all network calls made using `applicationClient` or `platformClient`, set the logger level to `"DEBUG"`.

```python

applicationClient = ApplicationClient({
    "applicationID": "YOUR_APPLICATION_ID",
    "applicationToken": "YOUR_APPLICATION_TOKEN",
    "logLevel": "DEBUG"
})

async def apiCall():
    try:
        response = await applicationClient.user.loginWithEmailAndPassword(body = {
              "password": "value",
              "username": "value"
            })
        print(response)
    except Exception as e:
        print(e)

apiCall()
```

The above code will log the curl command in the console

```bash
curl --request POST 'https://api.fynd.com/service/application/user/authentication/v1.0/login/password' --header 'x-fp-date: 20240308T171355Z' --header 'x-fp-signature: v1.1:aad5df1ad58fc87e74b040f5b0394be6cdd2d687ec7681b200bb3e20d48a458a' --header 'Authorization: Bearer <authorization-token>' --header 'Content-Type: application/json' --data-raw '{"password": "value", "username": "value"}'
```

---

### Sample Usage - ApplicationClient

```python

applicationClient = ApplicationClient({
    "applicationID": "YOUR_APPLICATION_ID",
    "applicationToken": "YOUR_APPLICATION_TOKEN",
    "domain": "YOUR_DOMAIN",
    "locationDetails": "LOCATION_DETAILS_OBJECT"
})
applicationClient.setLocationDetails(
    { 
        "pincode":"385001",
        "country": "India",
        "city":  "Ahmedabad",
        "location": {
            "longitude": "72.585022", 
            "latitude": "23.033863"
        }
    }
)

async def getProductDetails():
    try:
        product = await applicationClient.catalog.getProductDetailBySlug(slug="product-slug")
        print(product)
    except Exception as e:
        print(e)

getProductDetails()
```

---

#### Persisting cookies across requests

Some APIs require a login to proceed ahead. For this, we have several login options mentioned in these [User methods](/documentation/application/USER.md).
Using any of these methods, you can get a cookie. All you need to do is store the cookie in application config. Consider an example with mobile OTP:

```python
send_otp_response = applicationClient.user.loginWithOTP(
    platform=YOUR_APPLICATION_ID,
    body={
        "countryCode": "<your country code without the + sign>",
        "captchaCode": "<your captcha code>",
        "mobile": "<your mobile number>"
    }
)

login_response = applicationClient.user.verifyMobileOTP(
    platform=YOUR_APPLICATION_ID,
    body={
        "requestId": send_otp_response["json"]["request_id"],
        "otp": <your OTP>
    }
)

applicationClient.config.cookies = login_response["cookies"]
```

This will make sure the cookies are passed in all subsequent API calls.

---

### Sample Usage - PlatformClient

```python
from fdk_client.common.aiohttp_helper import AiohttpHelper
from fdk_client.platform.PlatformConfig import PlatformConfig
from fdk_client.platform.PlatformClient import PlatformClient
from fdk_client.common.utils import create_url_without_domain, get_headers_with_signature


async def setAccessToken(platformConfig, cookies):
    reqData = {
        "grant_type": "client_credentials",
        "client_id": platformConfig.apiKey,
        "client_secret": platformConfig.apiSecret
    }
    url = f"{platformConfig.domain}/service/panel/authentication/v1.0/company/{platformConfig.companyId}/oauth/token"
    url_without_domain = await create_url_without_domain(f"/service/panel/authentication/v1.0/company/{platformConfig.companyId}/oauth/token")
    headers = get_headers_with_signature(platformConfig.domain, "post", url_without_domain, "", {}, reqData)
    res = await AiohttpHelper().aiohttp_request("POST", url, reqData, headers, cookies=cookies)
    return res["json"]

async def loginUser(platformConfig):
    skywarpURL = f"{platformConfig.domain}/service/panel/authentication/v1.0/auth/login/password"
    userData = {
        "username": "YOUR_USERNAME",
        "password": "YOUR_PASSWORD",
        "g-recaptcha-response": "_skip_"
    }
    url_without_domain = "/service/panel/authentication/v1.0/auth/login/password"
    headers = get_headers_with_signature(platformConfig.domain, "post", url_without_domain, "", {}, userData)
    res = await AiohttpHelper().aiohttp_request("POST", skywarpURL, userData, headers)
    return res

try:
    platformConfig = PlatformConfig({
        "companyId": "YOUR_COMPANY_ID",
        "domain": "YOUR_DOMAIN",
        "apiKey": "YOUR_APIKEY",
        "apiSecret": "YOUR_APISECRET"
    })
    loginResponse = await loginUser(platformConfig)
    # print(loginResponse)
    tokenResponse = await setAccessToken(platformConfig, loginResponse["cookies"])
    # print(tokenResponse)
    await platformConfig.oauthClient.setToken(tokenResponse)
    platformClient = PlatformClient({
        "companyId": "YOUR_COMPANY_ID",
        "domain": "YOUR_DOMAIN",
        "apiKey": "YOUR_APIKEY",
        "apiSecret": "YOUR_APISECRET"
    })
    token = await platformClient.getAccesstokenObj(grant_type='client_credentials')
    platformClient.setToken(token)
    
    res = await platformClient.lead.getTicket(id="YOUR_TICKET_ID")
    # use res
except Exception as e:
    print(e)
```

---

### Sample Usage - request function

The request function allows you to make custom API requests with ease. It is available on both `platform` and `application` client.

#### Method Signature

```python
async def request(self, method, url, query={}, body={}, headers={}):
```

#### Parameters

-   `method`: A `str` representing the HTTP method (e.g., `'GET'`, `'POST'`, `'PUT'`,`'PATCH'`,`'DELETE'`).
-   `url`: A `str` representing the target URL for the HTTP request.
-   `query`: An optional `dict` containing key-value pairs for the URL's query parameters. Defaults to an empty dictionary.
-   `body`: An optional `dict` representing the body of the request, typically used in `POST`, `PUT`, or `PATCH` requests. Defaults to an empty dictionary.
-   `headers`: An optional `dict` representing any HTTP headers to include with the request. Defaults to an empty dictionary.

#### Return Value

-   The method returns HTTP response object 

#### Example

```python
url = '/service/platform/catalog/v1.0/company/1/products/'
method = 'GET'
query = {
    "company_id": "1",
    "page_no": 1,
    "page_size": 10,
    "name": "Jeans"
}
response = await platformClient.request(method, url, query=query)

url_post = '/service/platform/logistics/v1.0/company/1/packaging-materials'
method_post = 'POST'
body_post = {
    "name": "Pack Big",
    "width": "24",
    "height": "24",
    "length": "24",
    "package_type": "box",
    "weight": 100
}
response = await platformClient.request(method_post, url_post, body = body_post)

```

---

### Headers

When calling method, custom request headers can be included by passing a dictionary of headers as the `request_headers` argument in the method signature

```python
request_headers = {
    "x-api-version": "1.0"
}

response = await platform_client.application("<APPLICATION_ID>").theme.getAllPages(
    theme_id="<THEME_ID>",
    request_headers=request_headers
)
```



