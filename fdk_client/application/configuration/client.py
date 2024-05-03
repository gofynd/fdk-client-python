"""Configuration Application Client"""

import base64
import ujson
from urllib.parse import urlparse
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..ApplicationConfig import ApplicationConfig

from .validator import ConfigurationValidator

class Configuration:
    def __init__(self, config: ApplicationConfig):
        self._conf = config
        self._relativeUrls = {
            "getApplication": "/service/application/configuration/v1.0/application",
            "getOwnerInfo": "/service/application/configuration/v1.0/about",
            "getBasicDetails": "/service/application/configuration/v1.0/detail",
            "getIntegrationTokens": "/service/application/configuration/v1.0/token",
            "getOrderingStores": "/service/application/configuration/v1.0/ordering-store/stores",
            "getStoreDetailById": "/service/application/configuration/v1.0/ordering-store/stores/{store_id}",
            "getFeatures": "/service/application/configuration/v1.0/feature",
            "getContactInfo": "/service/application/configuration/v1.0/information",
            "getCurrencies": "/service/application/configuration/v1.0/currencies",
            "getCurrencyById": "/service/application/configuration/v1.0/currency/{id}",
            "getAppCurrencies": "/service/application/configuration/v1.0/currency",
            "getLanguages": "/service/application/configuration/v1.0/languages",
            "getOrderingStoreCookie": "/service/application/configuration/v1.0/ordering-store/select",
            "removeOrderingStoreCookie": "/service/application/configuration/v1.0/ordering-store/select",
            "getAppStaffList": "/service/application/configuration/v1.0/staff/list",
            "getAppStaffs": "/service/application/configuration/v1.0/staff"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def getApplication(self, body="", request_headers:Dict={}):
        """Retrieve details of the current sales channel.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.getApplication()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getApplication"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
        query_string = await create_query_string()

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getApplication"]).netloc, "get", await create_url_without_domain("/service/application/configuration/v1.0/application", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import Application
            schema = Application()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getApplication")
                print(e)

        return response
    
    async def getOwnerInfo(self, body="", request_headers:Dict={}):
        """Retrieve details of the sales channel owner.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.getOwnerInfo()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getOwnerInfo"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
        query_string = await create_query_string()

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getOwnerInfo"]).netloc, "get", await create_url_without_domain("/service/application/configuration/v1.0/about", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ApplicationAboutResponse
            schema = ApplicationAboutResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getOwnerInfo")
                print(e)

        return response
    
    async def getBasicDetails(self, body="", request_headers:Dict={}):
        """Retrieve basic details of the sales channel.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.getBasicDetails()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getBasicDetails"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
        query_string = await create_query_string()

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getBasicDetails"]).netloc, "get", await create_url_without_domain("/service/application/configuration/v1.0/detail", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ApplicationDetail
            schema = ApplicationDetail()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getBasicDetails")
                print(e)

        return response
    
    async def getIntegrationTokens(self, body="", request_headers:Dict={}):
        """Retrieve tools integration token of the sales channel. For ex- Firebase, MoEngage, Segment, GTM, Freshchat, Safetynet, Google Map and Facebook.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.getIntegrationTokens()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getIntegrationTokens"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
        query_string = await create_query_string()

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getIntegrationTokens"]).netloc, "get", await create_url_without_domain("/service/application/configuration/v1.0/token", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AppTokenResponse
            schema = AppTokenResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getIntegrationTokens")
                print(e)

        return response
    
    async def getOrderingStores(self, page_no=None, page_size=None, q=None, body="", request_headers:Dict={}):
        """Retrieve details of all the deployment store locations where the sales channel will be used for order placement.
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
        :param q : Store code or name of the ordering store. : type string
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if q is not None:
            payload["q"] = q

        # Parameter validation
        schema = ConfigurationValidator.getOrderingStores()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getOrderingStores"], proccessed_params="""{"required":[],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"The page number to navigate through the given set of results. Default value is 1."},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"The number of items to retrieve in each page. Default value is 10."},{"name":"q","in":"query","schema":{"type":"string"},"description":"Store code or name of the ordering store.","examples":{"success":{"value":"MRVLB01"}}}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"The page number to navigate through the given set of results. Default value is 1."},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"The number of items to retrieve in each page. Default value is 10."},{"name":"q","in":"query","schema":{"type":"string"},"description":"Store code or name of the ordering store.","examples":{"success":{"value":"MRVLB01"}}}],"headers":[],"path":[]}""", serverType="application", page_no=page_no, page_size=page_size, q=q)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, q=q)

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getOrderingStores"]).netloc, "get", await create_url_without_domain("/service/application/configuration/v1.0/ordering-store/stores", page_no=page_no, page_size=page_size, q=q), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import OrderingStores
            schema = OrderingStores()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getOrderingStores")
                print(e)

        return response
    
    async def getStoreDetailById(self, store_id=None, body="", request_headers:Dict={}):
        """Retrieve detail of a selling location (store) by it's Id.
        :param store_id : Store uid : type integer
        """
        payload = {}
        
        if store_id is not None:
            payload["store_id"] = store_id

        # Parameter validation
        schema = ConfigurationValidator.getStoreDetailById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getStoreDetailById"], proccessed_params="""{"required":[{"name":"store_id","in":"path","required":true,"description":"Store uid","schema":{"type":"integer"},"examples":{"404":{"value":990},"success":{"value":1}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"store_id","in":"path","required":true,"description":"Store uid","schema":{"type":"integer"},"examples":{"404":{"value":990},"success":{"value":1}}}]}""", serverType="application", store_id=store_id)
        query_string = await create_query_string(store_id=store_id)

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getStoreDetailById"]).netloc, "get", await create_url_without_domain("/service/application/configuration/v1.0/ordering-store/stores/{store_id}", store_id=store_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import OrderingStore
            schema = OrderingStore()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getStoreDetailById")
                print(e)

        return response
    
    async def getFeatures(self, body="", request_headers:Dict={}):
        """Retrieve configuration of the features of the sales channel.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.getFeatures()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getFeatures"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
        query_string = await create_query_string()

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getFeatures"]).netloc, "get", await create_url_without_domain("/service/application/configuration/v1.0/feature", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AppFeatureResponse
            schema = AppFeatureResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getFeatures")
                print(e)

        return response
    
    async def getContactInfo(self, body="", request_headers:Dict={}):
        """Retrieve contact details of the sales channel.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.getContactInfo()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getContactInfo"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
        query_string = await create_query_string()

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getContactInfo"]).netloc, "get", await create_url_without_domain("/service/application/configuration/v1.0/information", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ApplicationInformation
            schema = ApplicationInformation()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getContactInfo")
                print(e)

        return response
    
    async def getCurrencies(self, body="", request_headers:Dict={}):
        """Retrieve a list of available currencies.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.getCurrencies()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCurrencies"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
        query_string = await create_query_string()

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getCurrencies"]).netloc, "get", await create_url_without_domain("/service/application/configuration/v1.0/currencies", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CurrenciesResponse
            schema = CurrenciesResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCurrencies")
                print(e)

        return response
    
    async def getCurrencyById(self, id=None, body="", request_headers:Dict={}):
        """Retrieve details of the currency.
        :param id : Object ID assigned to the currency : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = ConfigurationValidator.getCurrencyById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCurrencyById"], proccessed_params="""{"required":[{"name":"id","in":"path","required":true,"description":"Object ID assigned to the currency","schema":{"type":"string"},"examples":{"success":{"value":"5bc8a62e21d33c25ebbfd6d3"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"id","in":"path","required":true,"description":"Object ID assigned to the currency","schema":{"type":"string"},"examples":{"success":{"value":"5bc8a62e21d33c25ebbfd6d3"}}}]}""", serverType="application", id=id)
        query_string = await create_query_string(id=id)

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getCurrencyById"]).netloc, "get", await create_url_without_domain("/service/application/configuration/v1.0/currency/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import Currency
            schema = Currency()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCurrencyById")
                print(e)

        return response
    
    async def getAppCurrencies(self, body="", request_headers:Dict={}):
        """Retrieve currency configuration of the sales channel.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.getAppCurrencies()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getAppCurrencies"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
        query_string = await create_query_string()

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getAppCurrencies"]).netloc, "get", await create_url_without_domain("/service/application/configuration/v1.0/currency", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AppCurrencyResponse
            schema = AppCurrencyResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAppCurrencies")
                print(e)

        return response
    
    async def getLanguages(self, body="", request_headers:Dict={}):
        """Retrieve a list of available languages.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.getLanguages()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getLanguages"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
        query_string = await create_query_string()

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getLanguages"]).netloc, "get", await create_url_without_domain("/service/application/configuration/v1.0/languages", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import LanguageResponse
            schema = LanguageResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getLanguages")
                print(e)

        return response
    
    async def getOrderingStoreCookie(self, body="", request_headers:Dict={}):
        """Reset cookie of ordering store.
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.getOrderingStoreCookie()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import OrderingStoreSelectRequest
        schema = OrderingStoreSelectRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["getOrderingStoreCookie"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
        query_string = await create_query_string()

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getOrderingStoreCookie"]).netloc, "post", await create_url_without_domain("/service/application/configuration/v1.0/ordering-store/select", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SuccessMessageResponse
            schema = SuccessMessageResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getOrderingStoreCookie")
                print(e)

        return response
    
    async def removeOrderingStoreCookie(self, body="", request_headers:Dict={}):
        """Remove store cookie
        """
        payload = {}
        

        # Parameter validation
        schema = ConfigurationValidator.removeOrderingStoreCookie()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["removeOrderingStoreCookie"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", serverType="application" )
        query_string = await create_query_string()

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["removeOrderingStoreCookie"]).netloc, "delete", await create_url_without_domain("/service/application/configuration/v1.0/ordering-store/select", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SuccessMessageResponse
            schema = SuccessMessageResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for removeOrderingStoreCookie")
                print(e)

        return response
    
    async def getAppStaffList(self, page_no=None, page_size=None, order_incent=None, ordering_store=None, user=None, user_name=None, body="", request_headers:Dict={}):
        """Retrieve a list of all staff members of the sales channel.
        :param page_no :  : type integer
        :param page_size :  : type integer
        :param order_incent : This is a boolean value. Select `true` to retrieve the staff members eligible for getting incentives on orders. : type boolean
        :param ordering_store : ID of the ordering store. Helps in retrieving staff members working at a particular ordering store. : type integer
        :param user : Mongo ID of the staff. Helps in retrieving the details of a particular staff member. : type string
        :param user_name : user name of the member : type string
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if order_incent is not None:
            payload["order_incent"] = order_incent
        if ordering_store is not None:
            payload["ordering_store"] = ordering_store
        if user is not None:
            payload["user"] = user
        if user_name is not None:
            payload["user_name"] = user_name

        # Parameter validation
        schema = ConfigurationValidator.getAppStaffList()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getAppStaffList"], proccessed_params="""{"required":[],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"}},{"name":"page_size","in":"query","schema":{"type":"integer"}},{"name":"order_incent","in":"query","description":"This is a boolean value. Select `true` to retrieve the staff members eligible for getting incentives on orders.","required":false,"schema":{"type":"boolean","example":true}},{"name":"ordering_store","in":"query","description":"ID of the ordering store. Helps in retrieving staff members working at a particular ordering store.","required":false,"schema":{"type":"integer","example":12},"examples":{"400":{"value":1},"success":{"value":1}}},{"name":"user","in":"query","description":"Mongo ID of the staff. Helps in retrieving the details of a particular staff member.","required":false,"schema":{"type":"string","example":"5e6b6ae7d450b1219ffdf3b2"},"examples":{"400":{"value":"test"},"success":{"value":"000000000000000016841367"}}},{"name":"user_name","in":"query","description":"user name of the member","schema":{"type":"string"},"examples":{"400":{"value":"Fynd"},"success":{"value":"Fynd"}}}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"}},{"name":"page_size","in":"query","schema":{"type":"integer"}},{"name":"order_incent","in":"query","description":"This is a boolean value. Select `true` to retrieve the staff members eligible for getting incentives on orders.","required":false,"schema":{"type":"boolean","example":true}},{"name":"ordering_store","in":"query","description":"ID of the ordering store. Helps in retrieving staff members working at a particular ordering store.","required":false,"schema":{"type":"integer","example":12},"examples":{"400":{"value":1},"success":{"value":1}}},{"name":"user","in":"query","description":"Mongo ID of the staff. Helps in retrieving the details of a particular staff member.","required":false,"schema":{"type":"string","example":"5e6b6ae7d450b1219ffdf3b2"},"examples":{"400":{"value":"test"},"success":{"value":"000000000000000016841367"}}},{"name":"user_name","in":"query","description":"user name of the member","schema":{"type":"string"},"examples":{"400":{"value":"Fynd"},"success":{"value":"Fynd"}}}],"headers":[],"path":[]}""", serverType="application", page_no=page_no, page_size=page_size, order_incent=order_incent, ordering_store=ordering_store, user=user, user_name=user_name)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, order_incent=order_incent, ordering_store=ordering_store, user=user, user_name=user_name)

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getAppStaffList"]).netloc, "get", await create_url_without_domain("/service/application/configuration/v1.0/staff/list", page_no=page_no, page_size=page_size, order_incent=order_incent, ordering_store=ordering_store, user=user, user_name=user_name), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AppStaffListResponse
            schema = AppStaffListResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAppStaffList")
                print(e)

        return response
    
    async def getAppStaffs(self, order_incent=None, ordering_store=None, user=None, body="", request_headers:Dict={}):
        """Retrieve a staff user including the names, employee code, incentive status, assigned ordering stores, and title of each staff added to the sales channel.
        :param order_incent : This is a boolean value. Select `true` to retrieve the staff members eligible for getting incentives on orders. : type boolean
        :param ordering_store : ID of the ordering store. Helps in retrieving staff members working at a particular ordering store. : type integer
        :param user : Mongo ID of the staff. Helps in retrieving the details of a particular staff member. : type string
        """
        payload = {}
        
        if order_incent is not None:
            payload["order_incent"] = order_incent
        if ordering_store is not None:
            payload["ordering_store"] = ordering_store
        if user is not None:
            payload["user"] = user

        # Parameter validation
        schema = ConfigurationValidator.getAppStaffs()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getAppStaffs"], proccessed_params="""{"required":[],"optional":[{"name":"order_incent","in":"query","description":"This is a boolean value. Select `true` to retrieve the staff members eligible for getting incentives on orders.","required":false,"schema":{"type":"boolean","example":true}},{"name":"ordering_store","in":"query","description":"ID of the ordering store. Helps in retrieving staff members working at a particular ordering store.","required":false,"schema":{"type":"integer","example":12},"examples":{"400":{"value":1},"success":{"value":1}}},{"name":"user","in":"query","description":"Mongo ID of the staff. Helps in retrieving the details of a particular staff member.","required":false,"schema":{"type":"string","example":"5e6b6ae7d450b1219ffdf3b2"},"examples":{"400":{"value":"test"},"success":{"value":"000000000000000016841367"}}}],"query":[{"name":"order_incent","in":"query","description":"This is a boolean value. Select `true` to retrieve the staff members eligible for getting incentives on orders.","required":false,"schema":{"type":"boolean","example":true}},{"name":"ordering_store","in":"query","description":"ID of the ordering store. Helps in retrieving staff members working at a particular ordering store.","required":false,"schema":{"type":"integer","example":12},"examples":{"400":{"value":1},"success":{"value":1}}},{"name":"user","in":"query","description":"Mongo ID of the staff. Helps in retrieving the details of a particular staff member.","required":false,"schema":{"type":"string","example":"5e6b6ae7d450b1219ffdf3b2"},"examples":{"400":{"value":"test"},"success":{"value":"000000000000000016841367"}}}],"headers":[],"path":[]}""", serverType="application", order_incent=order_incent, ordering_store=ordering_store, user=user)
        query_string = await create_query_string(order_incent=order_incent, ordering_store=ordering_store, user=user)

        headers={}
        headers["Authorization"] = f'Bearer {base64.b64encode(f"{self._conf.applicationID}:{self._conf.applicationToken}".encode()).decode()}'
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getAppStaffs"]).netloc, "get", await create_url_without_domain("/service/application/configuration/v1.0/staff", order_incent=order_incent, ordering_store=ordering_store, user=user), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AppStaffResponse
            schema = AppStaffResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAppStaffs")
                print(e)

        return response
    