"""User Application Client"""

import base64
import ujson
from urllib.parse import urlparse
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..ApplicationConfig import ApplicationConfig

from .validator import UserValidator

class User:
    def __init__(self, config: ApplicationConfig):
        self._conf = config
        self._relativeUrls = {
            "loginWithFacebook": "/service/application/user/authentication/v1.0/login/facebook-token",
            "loginWithGoogle": "/service/application/user/authentication/v1.0/login/google-token",
            "loginWithGoogleAndroid": "/service/application/user/authentication/v1.0/login/google-android",
            "loginWithGoogleIOS": "/service/application/user/authentication/v1.0/login/google-ios",
            "loginWithAppleIOS": "/service/application/user/authentication/v1.0/login/apple-ios",
            "loginWithOTP": "/service/application/user/authentication/v1.0/login/otp",
            "loginWithEmailAndPassword": "/service/application/user/authentication/v1.0/login/password",
            "sendResetPasswordEmail": "/service/application/user/authentication/v1.0/login/password/reset",
            "sendResetPasswordMobile": "/service/application/user/authentication/v1.0/login/password/mobile/reset",
            "sendResetToken": "/service/application/user/authentication/v1.0/login/password/reset/token",
            "forgotPassword": "/service/application/user/authentication/v1.0/login/password/reset/forgot",
            "resetForgotPassword": "/service/application/user/authentication/v1.0/login/password/forgot",
            "loginWithToken": "/service/application/user/authentication/v1.0/login/token",
            "registerWithForm": "/service/application/user/authentication/v1.0/register/form",
            "verifyEmail": "/service/application/user/authentication/v1.0/verify/email",
            "verifyMobile": "/service/application/user/authentication/v1.0/verify/mobile",
            "hasPassword": "/service/application/user/authentication/v1.0/has-password",
            "updatePassword": "/service/application/user/authentication/v1.0/password",
            "sendOTPOnMobile": "/service/application/user/authentication/v1.0/otp/mobile/send",
            "sendForgotOTPOnMobile": "/service/application/user/authentication/v1.0/otp/forgot/mobile/send",
            "verifyMobileOTP": "/service/application/user/authentication/v1.0/otp/mobile/verify",
            "verifyMobileForgotOTP": "/service/application/user/authentication/v1.0/otp/forgot/mobile/verify",
            "sendOTPOnEmail": "/service/application/user/authentication/v1.0/otp/email/send",
            "sendForgotOTPOnEmail": "/service/application/user/authentication/v1.0/otp/forgot/email/send",
            "verifyEmailOTP": "/service/application/user/authentication/v1.0/otp/email/verify",
            "verifyEmailForgotOTP": "/service/application/user/authentication/v1.0/otp/forgot/email/verify",
            "getLoggedInUser": "/service/application/user/authentication/v1.0/session",
            "getListOfActiveSessions": "/service/application/user/authentication/v1.0/sessions",
            "getPlatformConfig": "/service/application/user/platform/v1.0/config",
            "updateProfile": "/service/application/user/profile/v1.0/detail",
            "addMobileNumber": "/service/application/user/profile/v1.0/mobile",
            "deleteMobileNumber": "/service/application/user/profile/v1.0/mobile",
            "setMobileNumberAsPrimary": "/service/application/user/profile/v1.0/mobile/primary",
            "sendVerificationLinkToMobile": "/service/application/user/profile/v1.0/mobile/link/send",
            "addEmail": "/service/application/user/profile/v1.0/email",
            "deleteEmail": "/service/application/user/profile/v1.0/email",
            "setEmailAsPrimary": "/service/application/user/profile/v1.0/email/primary",
            "sendVerificationLinkToEmail": "/service/application/user/profile/v1.0/email/link/send",
            "userExists": "/service/application/user/authentication/v1.0/user-exists",
            "deleteUser": "/service/application/user/authentication/v1.0/delete",
            "logout": "/service/application/user/authentication/v1.0/logout",
            "getUserAttributes": "/service/application/user/profile/v1.0/user-attributes",
            "updateUserAttributes": "/service/application/user/profile/v1.0/user-attributes"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def loginWithFacebook(self, platform=None, body="", request_headers:Dict={}):
        """Use this API to login or register using Facebook credentials.
        :param platform : ID of the application : type string
        """
        payload = {}
        
        if platform is not None:
            payload["platform"] = platform

        # Parameter validation
        schema = UserValidator.loginWithFacebook()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import OAuthRequestSchema
        schema = OAuthRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["loginWithFacebook"], proccessed_params="""{"required":[],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"},"examples":{"facebook token login success":{"value":"5eda528b97457fe43a733ace"},"facebook token login failure":{"value":""}}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"},"examples":{"facebook token login success":{"value":"5eda528b97457fe43a733ace"},"facebook token login failure":{"value":""}}}],"headers":[],"path":[]}""", platform=platform)
        query_string = await create_query_string(platform=platform)

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["loginWithFacebook"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/login/facebook-token", platform=platform), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import AuthSuccess
            schema = AuthSuccess()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for loginWithFacebook")
                print(e)

        return response
    
    async def loginWithGoogle(self, platform=None, body="", request_headers:Dict={}):
        """Use this API to login or register using Google Account credentials.
        :param platform : ID of the application : type string
        """
        payload = {}
        
        if platform is not None:
            payload["platform"] = platform

        # Parameter validation
        schema = UserValidator.loginWithGoogle()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import OAuthRequestSchema
        schema = OAuthRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["loginWithGoogle"], proccessed_params="""{"required":[],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"},"examples":{"google token login success":{"value":"5eda528b97457fe43a733ace"}}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"},"examples":{"google token login success":{"value":"5eda528b97457fe43a733ace"}}}],"headers":[],"path":[]}""", platform=platform)
        query_string = await create_query_string(platform=platform)

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["loginWithGoogle"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/login/google-token", platform=platform), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import AuthSuccess
            schema = AuthSuccess()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for loginWithGoogle")
                print(e)

        return response
    
    async def loginWithGoogleAndroid(self, platform=None, body="", request_headers:Dict={}):
        """Use this API to login or register in Android app using Google Account credentials.
        :param platform : ID of the application : type string
        """
        payload = {}
        
        if platform is not None:
            payload["platform"] = platform

        # Parameter validation
        schema = UserValidator.loginWithGoogleAndroid()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import OAuthRequestSchema
        schema = OAuthRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["loginWithGoogleAndroid"], proccessed_params="""{"required":[],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"},"examples":{"google android token login success":{"value":"5eda528b97457fe43a733ace"}}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"},"examples":{"google android token login success":{"value":"5eda528b97457fe43a733ace"}}}],"headers":[],"path":[]}""", platform=platform)
        query_string = await create_query_string(platform=platform)

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["loginWithGoogleAndroid"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/login/google-android", platform=platform), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import AuthSuccess
            schema = AuthSuccess()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for loginWithGoogleAndroid")
                print(e)

        return response
    
    async def loginWithGoogleIOS(self, platform=None, body="", request_headers:Dict={}):
        """Use this API to login or register in iOS app using Google Account credentials.
        :param platform : ID of the application : type string
        """
        payload = {}
        
        if platform is not None:
            payload["platform"] = platform

        # Parameter validation
        schema = UserValidator.loginWithGoogleIOS()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import OAuthRequestSchema
        schema = OAuthRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["loginWithGoogleIOS"], proccessed_params="""{"required":[],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"},"examples":{"google android token login success":{"value":"5eda528b97457fe43a733ace"}}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"},"examples":{"google android token login success":{"value":"5eda528b97457fe43a733ace"}}}],"headers":[],"path":[]}""", platform=platform)
        query_string = await create_query_string(platform=platform)

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["loginWithGoogleIOS"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/login/google-ios", platform=platform), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import AuthSuccess
            schema = AuthSuccess()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for loginWithGoogleIOS")
                print(e)

        return response
    
    async def loginWithAppleIOS(self, platform=None, body="", request_headers:Dict={}):
        """Use this API to login or register in iOS app using Apple Account credentials.
        :param platform : ID of the application : type string
        """
        payload = {}
        
        if platform is not None:
            payload["platform"] = platform

        # Parameter validation
        schema = UserValidator.loginWithAppleIOS()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import OAuthRequestAppleSchema
        schema = OAuthRequestAppleSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["loginWithAppleIOS"], proccessed_params="""{"required":[],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"},"examples":{"apple ios login success":{"value":"5eda528b97457fe43a733ace"}}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"},"examples":{"apple ios login success":{"value":"5eda528b97457fe43a733ace"}}}],"headers":[],"path":[]}""", platform=platform)
        query_string = await create_query_string(platform=platform)

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["loginWithAppleIOS"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/login/apple-ios", platform=platform), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import AuthSuccess
            schema = AuthSuccess()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for loginWithAppleIOS")
                print(e)

        return response
    
    async def loginWithOTP(self, platform=None, body="", request_headers:Dict={}):
        """Use this API to login or register with a One-time Password (OTP) sent via Email or SMS.
        :param platform : ID of the application : type string
        """
        payload = {}
        
        if platform is not None:
            payload["platform"] = platform

        # Parameter validation
        schema = UserValidator.loginWithOTP()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SendOtpRequestSchema
        schema = SendOtpRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["loginWithOTP"], proccessed_params="""{"required":[],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"},"examples":{"login otp success":{"value":"5eda528b97457fe43a733ace"},"login otp failure":{"value":""}}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"},"examples":{"login otp success":{"value":"5eda528b97457fe43a733ace"},"login otp failure":{"value":""}}}],"headers":[],"path":[]}""", platform=platform)
        query_string = await create_query_string(platform=platform)

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["loginWithOTP"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/login/otp", platform=platform), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import SendOtpResponse
            schema = SendOtpResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for loginWithOTP")
                print(e)

        return response
    
    async def loginWithEmailAndPassword(self, body="", request_headers:Dict={}):
        """Use this API to login or register using an email address and password.
        """
        payload = {}
        

        # Parameter validation
        schema = UserValidator.loginWithEmailAndPassword()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PasswordLoginRequestSchema
        schema = PasswordLoginRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["loginWithEmailAndPassword"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["loginWithEmailAndPassword"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/login/password", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import LoginSuccess
            schema = LoginSuccess()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for loginWithEmailAndPassword")
                print(e)

        return response
    
    async def sendResetPasswordEmail(self, platform=None, body="", request_headers:Dict={}):
        """Use this API to reset a password using the link sent on email.
        :param platform : ID of the application : type string
        """
        payload = {}
        
        if platform is not None:
            payload["platform"] = platform

        # Parameter validation
        schema = UserValidator.sendResetPasswordEmail()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SendResetPasswordEmailRequestSchema
        schema = SendResetPasswordEmailRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["sendResetPasswordEmail"], proccessed_params="""{"required":[],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"},"examples":{"reset password success":{"value":"5eda528b97457fe43a733ace"},"reset password failure":{"value":""}}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"},"examples":{"reset password success":{"value":"5eda528b97457fe43a733ace"},"reset password failure":{"value":""}}}],"headers":[],"path":[]}""", platform=platform)
        query_string = await create_query_string(platform=platform)

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["sendResetPasswordEmail"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/login/password/reset", platform=platform), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import ResetPasswordSuccess
            schema = ResetPasswordSuccess()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for sendResetPasswordEmail")
                print(e)

        return response
    
    async def sendResetPasswordMobile(self, platform=None, body="", request_headers:Dict={}):
        """Use this API to reset a password using the link sent on mobile.
        :param platform : ID of the application : type string
        """
        payload = {}
        
        if platform is not None:
            payload["platform"] = platform

        # Parameter validation
        schema = UserValidator.sendResetPasswordMobile()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SendResetPasswordMobileRequestSchema
        schema = SendResetPasswordMobileRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["sendResetPasswordMobile"], proccessed_params="""{"required":[],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"},"examples":{"reset password mobile failure":{"value":""}}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"},"examples":{"reset password mobile failure":{"value":""}}}],"headers":[],"path":[]}""", platform=platform)
        query_string = await create_query_string(platform=platform)

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["sendResetPasswordMobile"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/login/password/mobile/reset", platform=platform), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import ResetPasswordSuccess
            schema = ResetPasswordSuccess()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for sendResetPasswordMobile")
                print(e)

        return response
    
    async def sendResetToken(self, body="", request_headers:Dict={}):
        """Use this API to send code to reset password.
        """
        payload = {}
        

        # Parameter validation
        schema = UserValidator.sendResetToken()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CodeRequestBodySchema
        schema = CodeRequestBodySchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["sendResetToken"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["sendResetToken"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/login/password/reset/token", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import ResetPasswordSuccess
            schema = ResetPasswordSuccess()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for sendResetToken")
                print(e)

        return response
    
    async def forgotPassword(self, body="", request_headers:Dict={}):
        """Use this API to reset a password using the code sent on email or SMS.
        """
        payload = {}
        

        # Parameter validation
        schema = UserValidator.forgotPassword()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ForgotPasswordRequestSchema
        schema = ForgotPasswordRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["forgotPassword"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["forgotPassword"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/login/password/reset/forgot", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import LoginSuccess
            schema = LoginSuccess()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for forgotPassword")
                print(e)

        return response
    
    async def resetForgotPassword(self, body="", request_headers:Dict={}):
        """Use this API to reset a password using the code sent on email or SMS.
        """
        payload = {}
        

        # Parameter validation
        schema = UserValidator.resetForgotPassword()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ForgotPasswordRequestSchema
        schema = ForgotPasswordRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["resetForgotPassword"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["resetForgotPassword"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/login/password/forgot", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import ResetForgotPasswordSuccess
            schema = ResetForgotPasswordSuccess()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for resetForgotPassword")
                print(e)

        return response
    
    async def loginWithToken(self, body="", request_headers:Dict={}):
        """Use this API to login or register using a token for authentication.
        """
        payload = {}
        

        # Parameter validation
        schema = UserValidator.loginWithToken()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import TokenRequestBodySchema
        schema = TokenRequestBodySchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["loginWithToken"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["loginWithToken"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/login/token", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import LoginSuccess
            schema = LoginSuccess()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for loginWithToken")
                print(e)

        return response
    
    async def registerWithForm(self, platform=None, body="", request_headers:Dict={}):
        """Use this API to perform user registration by sending form data in the request body.
        :param platform : ID of the application : type string
        """
        payload = {}
        
        if platform is not None:
            payload["platform"] = platform

        # Parameter validation
        schema = UserValidator.registerWithForm()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import FormRegisterRequestSchema
        schema = FormRegisterRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["registerWithForm"], proccessed_params="""{"required":[],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"},"examples":{"register form success":{"value":"5eda528b97457fe43a733ace"},"register form failure":{"value":""}}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"},"examples":{"register form success":{"value":"5eda528b97457fe43a733ace"},"register form failure":{"value":""}}}],"headers":[],"path":[]}""", platform=platform)
        query_string = await create_query_string(platform=platform)

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["registerWithForm"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/register/form", platform=platform), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import RegisterFormSuccess
            schema = RegisterFormSuccess()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for registerWithForm")
                print(e)

        return response
    
    async def verifyEmail(self, body="", request_headers:Dict={}):
        """Use this API to send a verification code to verify an email.
        """
        payload = {}
        

        # Parameter validation
        schema = UserValidator.verifyEmail()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CodeRequestBodySchema
        schema = CodeRequestBodySchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["verifyEmail"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["verifyEmail"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/verify/email", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import VerifyEmailSuccess
            schema = VerifyEmailSuccess()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for verifyEmail")
                print(e)

        return response
    
    async def verifyMobile(self, body="", request_headers:Dict={}):
        """Use this API to send a verification code to verify a mobile number.
        """
        payload = {}
        

        # Parameter validation
        schema = UserValidator.verifyMobile()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CodeRequestBodySchema
        schema = CodeRequestBodySchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["verifyMobile"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["verifyMobile"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/verify/mobile", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import VerifyEmailSuccess
            schema = VerifyEmailSuccess()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for verifyMobile")
                print(e)

        return response
    
    async def hasPassword(self, body="", request_headers:Dict={}):
        """Use this API to check if user has created a password for login.
        """
        payload = {}
        

        # Parameter validation
        schema = UserValidator.hasPassword()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["hasPassword"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["hasPassword"]).netloc, "get", await create_url_without_domain("/service/application/user/authentication/v1.0/has-password", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import HasPasswordSuccess
            schema = HasPasswordSuccess()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for hasPassword")
                print(e)

        return response
    
    async def updatePassword(self, body="", request_headers:Dict={}):
        """Use this API to update the password.
        """
        payload = {}
        

        # Parameter validation
        schema = UserValidator.updatePassword()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UpdatePasswordRequestSchema
        schema = UpdatePasswordRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["updatePassword"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["updatePassword"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/password", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import VerifyEmailSuccess
            schema = VerifyEmailSuccess()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updatePassword")
                print(e)

        return response
    
    async def sendOTPOnMobile(self, platform=None, body="", request_headers:Dict={}):
        """Use this API to send an OTP to a mobile number.
        :param platform : ID of the application : type string
        """
        payload = {}
        
        if platform is not None:
            payload["platform"] = platform

        # Parameter validation
        schema = UserValidator.sendOTPOnMobile()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SendMobileOtpRequestSchema
        schema = SendMobileOtpRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["sendOTPOnMobile"], proccessed_params="""{"required":[],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"},"examples":{"send mobile otp success":{"value":"5eda528b97457fe43a733ace"},"send mobile otp failure":{"value":""}}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"},"examples":{"send mobile otp success":{"value":"5eda528b97457fe43a733ace"},"send mobile otp failure":{"value":""}}}],"headers":[],"path":[]}""", platform=platform)
        query_string = await create_query_string(platform=platform)

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["sendOTPOnMobile"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/otp/mobile/send", platform=platform), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import OtpSuccess
            schema = OtpSuccess()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for sendOTPOnMobile")
                print(e)

        return response
    
    async def sendForgotOTPOnMobile(self, platform=None, body="", request_headers:Dict={}):
        """Use this API to send an Forgot OTP to a mobile number.
        :param platform : ID of the application : type string
        """
        payload = {}
        
        if platform is not None:
            payload["platform"] = platform

        # Parameter validation
        schema = UserValidator.sendForgotOTPOnMobile()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SendMobileForgotOtpRequestSchema
        schema = SendMobileForgotOtpRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["sendForgotOTPOnMobile"], proccessed_params="""{"required":[],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"},"examples":{"send forgot otp on mobile success":{"value":"5eda528b97457fe43a733ace"},"send forgot otp on mobile failure":{"value":""}}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"},"examples":{"send forgot otp on mobile success":{"value":"5eda528b97457fe43a733ace"},"send forgot otp on mobile failure":{"value":""}}}],"headers":[],"path":[]}""", platform=platform)
        query_string = await create_query_string(platform=platform)

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["sendForgotOTPOnMobile"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/otp/forgot/mobile/send", platform=platform), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import OtpSuccess
            schema = OtpSuccess()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for sendForgotOTPOnMobile")
                print(e)

        return response
    
    async def verifyMobileOTP(self, platform=None, body="", request_headers:Dict={}):
        """Use this API to verify the OTP received on a mobile number.
        :param platform : ID of the application : type string
        """
        payload = {}
        
        if platform is not None:
            payload["platform"] = platform

        # Parameter validation
        schema = UserValidator.verifyMobileOTP()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import VerifyOtpRequestSchema
        schema = VerifyOtpRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["verifyMobileOTP"], proccessed_params="""{"required":[],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"},"examples":{"verify mobile otp success":{"value":"5eda528b97457fe43a733ace"},"verify mobile otp failure":{"value":""}}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"},"examples":{"verify mobile otp success":{"value":"5eda528b97457fe43a733ace"},"verify mobile otp failure":{"value":""}}}],"headers":[],"path":[]}""", platform=platform)
        query_string = await create_query_string(platform=platform)

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["verifyMobileOTP"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/otp/mobile/verify", platform=platform), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import VerifyOtpSuccess
            schema = VerifyOtpSuccess()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for verifyMobileOTP")
                print(e)

        return response
    
    async def verifyMobileForgotOTP(self, platform=None, body="", request_headers:Dict={}):
        """Use this API to verify the Forgot OTP received on a mobile number.
        :param platform : ID of the application : type string
        """
        payload = {}
        
        if platform is not None:
            payload["platform"] = platform

        # Parameter validation
        schema = UserValidator.verifyMobileForgotOTP()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import VerifyMobileForgotOtpRequestSchema
        schema = VerifyMobileForgotOtpRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["verifyMobileForgotOTP"], proccessed_params="""{"required":[],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"},"examples":{"verify forgot otp on mobile success":{"value":"5eda528b97457fe43a733ace"},"verify forgot otp on mobile failure":{"value":""}}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"},"examples":{"verify forgot otp on mobile success":{"value":"5eda528b97457fe43a733ace"},"verify forgot otp on mobile failure":{"value":""}}}],"headers":[],"path":[]}""", platform=platform)
        query_string = await create_query_string(platform=platform)

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["verifyMobileForgotOTP"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/otp/forgot/mobile/verify", platform=platform), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import VerifyForgotOtpSuccess
            schema = VerifyForgotOtpSuccess()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for verifyMobileForgotOTP")
                print(e)

        return response
    
    async def sendOTPOnEmail(self, platform=None, body="", request_headers:Dict={}):
        """Use this API to send an OTP to an email ID.
        :param platform : ID of the application : type string
        """
        payload = {}
        
        if platform is not None:
            payload["platform"] = platform

        # Parameter validation
        schema = UserValidator.sendOTPOnEmail()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SendEmailOtpRequestSchema
        schema = SendEmailOtpRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["sendOTPOnEmail"], proccessed_params="""{"required":[],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"},"examples":{"send email otp success":{"value":"5eda528b97457fe43a733ace"},"send email otp failure":{"value":""}}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"},"examples":{"send email otp success":{"value":"5eda528b97457fe43a733ace"},"send email otp failure":{"value":""}}}],"headers":[],"path":[]}""", platform=platform)
        query_string = await create_query_string(platform=platform)

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["sendOTPOnEmail"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/otp/email/send", platform=platform), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import EmailOtpSuccess
            schema = EmailOtpSuccess()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for sendOTPOnEmail")
                print(e)

        return response
    
    async def sendForgotOTPOnEmail(self, platform=None, body="", request_headers:Dict={}):
        """Use this API to send an Forgot OTP to an email ID.
        :param platform : ID of the application : type string
        """
        payload = {}
        
        if platform is not None:
            payload["platform"] = platform

        # Parameter validation
        schema = UserValidator.sendForgotOTPOnEmail()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SendEmailForgotOtpRequestSchema
        schema = SendEmailForgotOtpRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["sendForgotOTPOnEmail"], proccessed_params="""{"required":[],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"},"examples":{"send forgot otp on email success":{"value":"5eda528b97457fe43a733ace"},"send forgot otp on email failure":{"value":""}}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"},"examples":{"send forgot otp on email success":{"value":"5eda528b97457fe43a733ace"},"send forgot otp on email failure":{"value":""}}}],"headers":[],"path":[]}""", platform=platform)
        query_string = await create_query_string(platform=platform)

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["sendForgotOTPOnEmail"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/otp/forgot/email/send", platform=platform), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import EmailOtpSuccess
            schema = EmailOtpSuccess()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for sendForgotOTPOnEmail")
                print(e)

        return response
    
    async def verifyEmailOTP(self, platform=None, body="", request_headers:Dict={}):
        """Use this API to verify the OTP received on an email ID.
        :param platform : ID of the application : type string
        """
        payload = {}
        
        if platform is not None:
            payload["platform"] = platform

        # Parameter validation
        schema = UserValidator.verifyEmailOTP()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import VerifyEmailOtpRequestSchema
        schema = VerifyEmailOtpRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["verifyEmailOTP"], proccessed_params="""{"required":[],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"},"examples":{"verify email otp success":{"value":"5eda528b97457fe43a733ace"},"verify email otp failure":{"value":""}}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"},"examples":{"verify email otp success":{"value":"5eda528b97457fe43a733ace"},"verify email otp failure":{"value":""}}}],"headers":[],"path":[]}""", platform=platform)
        query_string = await create_query_string(platform=platform)

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["verifyEmailOTP"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/otp/email/verify", platform=platform), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import VerifyOtpSuccess
            schema = VerifyOtpSuccess()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for verifyEmailOTP")
                print(e)

        return response
    
    async def verifyEmailForgotOTP(self, platform=None, body="", request_headers:Dict={}):
        """Use this API to verify the Forgot OTP received on an email ID.
        :param platform : ID of the application : type string
        """
        payload = {}
        
        if platform is not None:
            payload["platform"] = platform

        # Parameter validation
        schema = UserValidator.verifyEmailForgotOTP()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import VerifyEmailForgotOtpRequestSchema
        schema = VerifyEmailForgotOtpRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["verifyEmailForgotOTP"], proccessed_params="""{"required":[],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"},"examples":{"verify forgot otp on email success":{"value":"5eda528b97457fe43a733ace"},"verify forgot otp on email failure":{"value":""}}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"},"examples":{"verify forgot otp on email success":{"value":"5eda528b97457fe43a733ace"},"verify forgot otp on email failure":{"value":""}}}],"headers":[],"path":[]}""", platform=platform)
        query_string = await create_query_string(platform=platform)

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["verifyEmailForgotOTP"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/otp/forgot/email/verify", platform=platform), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import VerifyForgotOtpSuccess
            schema = VerifyForgotOtpSuccess()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for verifyEmailForgotOTP")
                print(e)

        return response
    
    async def getLoggedInUser(self, body="", request_headers:Dict={}):
        """Use this API  to get the details of a logged in user.
        """
        payload = {}
        

        # Parameter validation
        schema = UserValidator.getLoggedInUser()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getLoggedInUser"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getLoggedInUser"]).netloc, "get", await create_url_without_domain("/service/application/user/authentication/v1.0/session", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import UserObjectSchema
            schema = UserObjectSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getLoggedInUser")
                print(e)

        return response
    
    async def getListOfActiveSessions(self, body="", request_headers:Dict={}):
        """Use this API to retrieve all active sessions of a user.
        """
        payload = {}
        

        # Parameter validation
        schema = UserValidator.getListOfActiveSessions()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getListOfActiveSessions"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getListOfActiveSessions"]).netloc, "get", await create_url_without_domain("/service/application/user/authentication/v1.0/sessions", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import SessionListSuccess
            schema = SessionListSuccess()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getListOfActiveSessions")
                print(e)

        return response
    
    async def getPlatformConfig(self, name=None, body="", request_headers:Dict={}):
        """Use this API to get all the platform configurations such as mobile image, desktop image, social logins, and all other text.
        :param name : Name of the application, e.g. Fynd : type string
        """
        payload = {}
        
        if name is not None:
            payload["name"] = name

        # Parameter validation
        schema = UserValidator.getPlatformConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getPlatformConfig"], proccessed_params="""{"required":[],"optional":[{"name":"name","in":"query","description":"Name of the application, e.g. Fynd","schema":{"type":"string"},"examples":{"get platform config success":{"value":"5eda528b97457fe43a733ace"}}}],"query":[{"name":"name","in":"query","description":"Name of the application, e.g. Fynd","schema":{"type":"string"},"examples":{"get platform config success":{"value":"5eda528b97457fe43a733ace"}}}],"headers":[],"path":[]}""", name=name)
        query_string = await create_query_string(name=name)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getPlatformConfig"]).netloc, "get", await create_url_without_domain("/service/application/user/platform/v1.0/config", name=name), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import PlatformSchema
            schema = PlatformSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPlatformConfig")
                print(e)

        return response
    
    async def updateProfile(self, platform=None, body="", request_headers:Dict={}):
        """Use this API to update details in the user profile. Details can be first name, last name, gender, email, phone number, or profile picture.
        :param platform : ID of the application : type string
        """
        payload = {}
        
        if platform is not None:
            payload["platform"] = platform

        # Parameter validation
        schema = UserValidator.updateProfile()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import EditProfileRequestSchema
        schema = EditProfileRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["updateProfile"], proccessed_params="""{"required":[],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"},"examples":{"edit profile success":{"value":"5eda528b97457fe43a733ace"},"edit profile failure":{"value":""}}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"},"examples":{"edit profile success":{"value":"5eda528b97457fe43a733ace"},"edit profile failure":{"value":""}}}],"headers":[],"path":[]}""", platform=platform)
        query_string = await create_query_string(platform=platform)

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["updateProfile"]).netloc, "post", await create_url_without_domain("/service/application/user/profile/v1.0/detail", platform=platform), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import ProfileEditSuccess
            schema = ProfileEditSuccess()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateProfile")
                print(e)

        return response
    
    async def addMobileNumber(self, platform=None, body="", request_headers:Dict={}):
        """Use this API to add a new mobile number to a profile.
        :param platform : ID of the application : type string
        """
        payload = {}
        
        if platform is not None:
            payload["platform"] = platform

        # Parameter validation
        schema = UserValidator.addMobileNumber()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import EditMobileRequestSchema
        schema = EditMobileRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["addMobileNumber"], proccessed_params="""{"required":[],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"},"examples":{"add mobile number to profile success":{"value":"5eda528b97457fe43a733ace"},"add mobile number to profile failure":{"value":""}}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"},"examples":{"add mobile number to profile success":{"value":"5eda528b97457fe43a733ace"},"add mobile number to profile failure":{"value":""}}}],"headers":[],"path":[]}""", platform=platform)
        query_string = await create_query_string(platform=platform)

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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["addMobileNumber"]).netloc, "put", await create_url_without_domain("/service/application/user/profile/v1.0/mobile", platform=platform), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import VerifyMobileOTPSuccess
            schema = VerifyMobileOTPSuccess()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for addMobileNumber")
                print(e)

        return response
    
    async def deleteMobileNumber(self, platform=None, active=None, primary=None, verified=None, country_code=None, phone=None, body="", request_headers:Dict={}):
        """Use this API to delete a mobile number from a profile.
        :param platform : ID of the application : type string
        :param active : This is a boolean value to check if mobile number is active 1.True - Number is active 2. False - Number is inactive : type boolean
        :param primary : This is a boolean value to check if mobile number is primary number (main number) 1. True - Number is primary 2. False - Number is not primary : type boolean
        :param verified : This is a boolean value to check if mobile number is verified 1. True - Number is verified 2.False - Number is not verified yet : type boolean
        :param country_code : Country code of the phone number, e.g. 91 : type string
        :param phone : Phone number : type string
        """
        payload = {}
        
        if platform is not None:
            payload["platform"] = platform
        if active is not None:
            payload["active"] = active
        if primary is not None:
            payload["primary"] = primary
        if verified is not None:
            payload["verified"] = verified
        if country_code is not None:
            payload["country_code"] = country_code
        if phone is not None:
            payload["phone"] = phone

        # Parameter validation
        schema = UserValidator.deleteMobileNumber()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["deleteMobileNumber"], proccessed_params="""{"required":[{"name":"active","in":"query","required":true,"description":"This is a boolean value to check if mobile number is active 1.True - Number is active 2. False - Number is inactive","schema":{"type":"boolean"},"examples":{"Delete mobile number from profile success":{"value":true},"Delete mobile number from profile failure":{"value":false}}},{"name":"primary","in":"query","description":"This is a boolean value to check if mobile number is primary number (main number) 1. True - Number is primary 2. False - Number is not primary","required":true,"schema":{"type":"boolean"},"examples":{"Delete mobile number from profile success":{"value":true},"Delete mobile number from profile failure":{"value":false}}},{"name":"verified","in":"query","description":"This is a boolean value to check if mobile number is verified 1. True - Number is verified 2.False - Number is not verified yet","required":true,"schema":{"type":"boolean"},"examples":{"Delete mobile number from profile success":{"value":true},"Delete mobile number from profile failure":{"value":false}}},{"name":"country_code","in":"query","description":"Country code of the phone number, e.g. 91","required":true,"schema":{"type":"string"},"examples":{"Delete mobile number from profile success":{"value":"91"},"Delete mobile number from profile failure":{"value":""}}},{"name":"phone","in":"query","description":"Phone number","required":true,"schema":{"type":"string"},"examples":{"Delete mobile number from profile success":{"value":"9987568530"},"Delete mobile number from profile failure":{"value":""}}}],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"},"examples":{"Delete mobile number from profile success":{"value":"5eda528b97457fe43a733ace"},"Delete mobile number from profile failure":{"value":""}}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"},"examples":{"Delete mobile number from profile success":{"value":"5eda528b97457fe43a733ace"},"Delete mobile number from profile failure":{"value":""}}},{"name":"active","in":"query","required":true,"description":"This is a boolean value to check if mobile number is active 1.True - Number is active 2. False - Number is inactive","schema":{"type":"boolean"},"examples":{"Delete mobile number from profile success":{"value":true},"Delete mobile number from profile failure":{"value":false}}},{"name":"primary","in":"query","description":"This is a boolean value to check if mobile number is primary number (main number) 1. True - Number is primary 2. False - Number is not primary","required":true,"schema":{"type":"boolean"},"examples":{"Delete mobile number from profile success":{"value":true},"Delete mobile number from profile failure":{"value":false}}},{"name":"verified","in":"query","description":"This is a boolean value to check if mobile number is verified 1. True - Number is verified 2.False - Number is not verified yet","required":true,"schema":{"type":"boolean"},"examples":{"Delete mobile number from profile success":{"value":true},"Delete mobile number from profile failure":{"value":false}}},{"name":"country_code","in":"query","description":"Country code of the phone number, e.g. 91","required":true,"schema":{"type":"string"},"examples":{"Delete mobile number from profile success":{"value":"91"},"Delete mobile number from profile failure":{"value":""}}},{"name":"phone","in":"query","description":"Phone number","required":true,"schema":{"type":"string"},"examples":{"Delete mobile number from profile success":{"value":"9987568530"},"Delete mobile number from profile failure":{"value":""}}}],"headers":[],"path":[]}""", platform=platform, active=active, primary=primary, verified=verified, country_code=country_code, phone=phone)
        query_string = await create_query_string(platform=platform, active=active, primary=primary, verified=verified, country_code=country_code, phone=phone)

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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["deleteMobileNumber"]).netloc, "delete", await create_url_without_domain("/service/application/user/profile/v1.0/mobile", platform=platform, active=active, primary=primary, verified=verified, country_code=country_code, phone=phone), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import LoginSuccess
            schema = LoginSuccess()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteMobileNumber")
                print(e)

        return response
    
    async def setMobileNumberAsPrimary(self, body="", request_headers:Dict={}):
        """Use this API to set a mobile number as primary. Primary number is a verified number used for all future communications.
        """
        payload = {}
        

        # Parameter validation
        schema = UserValidator.setMobileNumberAsPrimary()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SendVerificationLinkMobileRequestSchema
        schema = SendVerificationLinkMobileRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["setMobileNumberAsPrimary"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["setMobileNumberAsPrimary"]).netloc, "post", await create_url_without_domain("/service/application/user/profile/v1.0/mobile/primary", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import LoginSuccess
            schema = LoginSuccess()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for setMobileNumberAsPrimary")
                print(e)

        return response
    
    async def sendVerificationLinkToMobile(self, platform=None, body="", request_headers:Dict={}):
        """Use this API to send a verification link to a mobile number
        :param platform : ID of the application : type string
        """
        payload = {}
        
        if platform is not None:
            payload["platform"] = platform

        # Parameter validation
        schema = UserValidator.sendVerificationLinkToMobile()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SendVerificationLinkMobileRequestSchema
        schema = SendVerificationLinkMobileRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["sendVerificationLinkToMobile"], proccessed_params="""{"required":[],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"},"examples":{"send verification link to mobile success":{"value":"5eda528b97457fe43a733ace"},"send verification link to mobile failure":{"value":""}}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"},"examples":{"send verification link to mobile success":{"value":"5eda528b97457fe43a733ace"},"send verification link to mobile failure":{"value":""}}}],"headers":[],"path":[]}""", platform=platform)
        query_string = await create_query_string(platform=platform)

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["sendVerificationLinkToMobile"]).netloc, "post", await create_url_without_domain("/service/application/user/profile/v1.0/mobile/link/send", platform=platform), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import SendMobileVerifyLinkSuccess
            schema = SendMobileVerifyLinkSuccess()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for sendVerificationLinkToMobile")
                print(e)

        return response
    
    async def addEmail(self, platform=None, body="", request_headers:Dict={}):
        """Use this API to add a new email address to a profile
        :param platform : ID of the application : type string
        """
        payload = {}
        
        if platform is not None:
            payload["platform"] = platform

        # Parameter validation
        schema = UserValidator.addEmail()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import EditEmailRequestSchema
        schema = EditEmailRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["addEmail"], proccessed_params="""{"required":[],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"},"examples":{"add email to profile success":{"value":"5eda528b97457fe43a733ace"},"add email to profile failure":{"value":""}}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"},"examples":{"add email to profile success":{"value":"5eda528b97457fe43a733ace"},"add email to profile failure":{"value":""}}}],"headers":[],"path":[]}""", platform=platform)
        query_string = await create_query_string(platform=platform)

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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["addEmail"]).netloc, "put", await create_url_without_domain("/service/application/user/profile/v1.0/email", platform=platform), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import VerifyEmailOTPSuccess
            schema = VerifyEmailOTPSuccess()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for addEmail")
                print(e)

        return response
    
    async def deleteEmail(self, platform=None, active=None, primary=None, verified=None, email=None, body="", request_headers:Dict={}):
        """Use this API to delete an email address from a profile
        :param platform : ID of the application : type string
        :param active : This is a boolean value to check if email ID is active 1. True - Email ID is active 2.False - Email ID is inactive : type boolean
        :param primary : This is a boolean value to check if email ID is primary (main email ID) 1. True - Email ID is primary 2.False - Email ID is not primary : type boolean
        :param verified : This is a boolean value to check if email ID is verified 1. True - Email ID is verified 2.False - Email ID is not verified yet : type boolean
        :param email : The email ID to delete : type string
        """
        payload = {}
        
        if platform is not None:
            payload["platform"] = platform
        if active is not None:
            payload["active"] = active
        if primary is not None:
            payload["primary"] = primary
        if verified is not None:
            payload["verified"] = verified
        if email is not None:
            payload["email"] = email

        # Parameter validation
        schema = UserValidator.deleteEmail()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["deleteEmail"], proccessed_params="""{"required":[{"name":"active","in":"query","description":"This is a boolean value to check if email ID is active 1. True - Email ID is active 2.False - Email ID is inactive","required":true,"schema":{"type":"boolean"},"examples":{"Delete email from profile success":{"value":true},"Delete email from profile failure":{"value":false}}},{"name":"primary","in":"query","description":"This is a boolean value to check if email ID is primary (main email ID) 1. True - Email ID is primary 2.False - Email ID is not primary","required":true,"schema":{"type":"boolean"},"examples":{"Delete email from profile success":{"value":true},"Delete email from profile failure":{"value":false}}},{"name":"verified","in":"query","description":"This is a boolean value to check if email ID is verified 1. True - Email ID is verified 2.False - Email ID is not verified yet","required":true,"schema":{"type":"boolean"},"examples":{"Delete email from profile success":{"value":true},"Delete email from profile failure":{"value":false}}},{"name":"email","in":"query","description":"The email ID to delete","required":true,"schema":{"type":"string"},"examples":{"Delete email from profile success":{"value":"vinit.mav12345@gofynd.com"},"Delete email from profile failure":{"value":""}}}],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"},"examples":{"Delete email from profile success":{"value":"5eda528b97457fe43a733ace"},"Delete email from profile failure":{"value":""}}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"},"examples":{"Delete email from profile success":{"value":"5eda528b97457fe43a733ace"},"Delete email from profile failure":{"value":""}}},{"name":"active","in":"query","description":"This is a boolean value to check if email ID is active 1. True - Email ID is active 2.False - Email ID is inactive","required":true,"schema":{"type":"boolean"},"examples":{"Delete email from profile success":{"value":true},"Delete email from profile failure":{"value":false}}},{"name":"primary","in":"query","description":"This is a boolean value to check if email ID is primary (main email ID) 1. True - Email ID is primary 2.False - Email ID is not primary","required":true,"schema":{"type":"boolean"},"examples":{"Delete email from profile success":{"value":true},"Delete email from profile failure":{"value":false}}},{"name":"verified","in":"query","description":"This is a boolean value to check if email ID is verified 1. True - Email ID is verified 2.False - Email ID is not verified yet","required":true,"schema":{"type":"boolean"},"examples":{"Delete email from profile success":{"value":true},"Delete email from profile failure":{"value":false}}},{"name":"email","in":"query","description":"The email ID to delete","required":true,"schema":{"type":"string"},"examples":{"Delete email from profile success":{"value":"vinit.mav12345@gofynd.com"},"Delete email from profile failure":{"value":""}}}],"headers":[],"path":[]}""", platform=platform, active=active, primary=primary, verified=verified, email=email)
        query_string = await create_query_string(platform=platform, active=active, primary=primary, verified=verified, email=email)

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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["deleteEmail"]).netloc, "delete", await create_url_without_domain("/service/application/user/profile/v1.0/email", platform=platform, active=active, primary=primary, verified=verified, email=email), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import LoginSuccess
            schema = LoginSuccess()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteEmail")
                print(e)

        return response
    
    async def setEmailAsPrimary(self, body="", request_headers:Dict={}):
        """Use this API to set an email address as primary. Primary email ID is a email address used for all future communications.
        """
        payload = {}
        

        # Parameter validation
        schema = UserValidator.setEmailAsPrimary()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import EditEmailRequestSchema
        schema = EditEmailRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["setEmailAsPrimary"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["setEmailAsPrimary"]).netloc, "post", await create_url_without_domain("/service/application/user/profile/v1.0/email/primary", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import LoginSuccess
            schema = LoginSuccess()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for setEmailAsPrimary")
                print(e)

        return response
    
    async def sendVerificationLinkToEmail(self, platform=None, body="", request_headers:Dict={}):
        """Use this API to send verification link to an email address.
        :param platform : ID of the application : type string
        """
        payload = {}
        
        if platform is not None:
            payload["platform"] = platform

        # Parameter validation
        schema = UserValidator.sendVerificationLinkToEmail()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import EditEmailRequestSchema
        schema = EditEmailRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["sendVerificationLinkToEmail"], proccessed_params="""{"required":[],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"},"examples":{"send verification link to email success":{"value":"5eda528b97457fe43a733ace"},"send verification link to email failure":{"value":""}}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"},"examples":{"send verification link to email success":{"value":"5eda528b97457fe43a733ace"},"send verification link to email failure":{"value":""}}}],"headers":[],"path":[]}""", platform=platform)
        query_string = await create_query_string(platform=platform)

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["sendVerificationLinkToEmail"]).netloc, "post", await create_url_without_domain("/service/application/user/profile/v1.0/email/link/send", platform=platform), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import SendEmailVerifyLinkSuccess
            schema = SendEmailVerifyLinkSuccess()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for sendVerificationLinkToEmail")
                print(e)

        return response
    
    async def userExists(self, q=None, body="", request_headers:Dict={}):
        """Use this API to check whether user is already registered or not to the sales channel.
        :param q : email id or phone number of user : type string
        """
        payload = {}
        
        if q is not None:
            payload["q"] = q

        # Parameter validation
        schema = UserValidator.userExists()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["userExists"], proccessed_params="""{"required":[{"in":"query","name":"q","description":"email id or phone number of user","schema":{"type":"string"},"required":true,"examples":{"user exists success":{"value":"vinit.mav12@gofynd.com"},"user exists failure":{"value":""}}}],"optional":[],"query":[{"in":"query","name":"q","description":"email id or phone number of user","schema":{"type":"string"},"required":true,"examples":{"user exists success":{"value":"vinit.mav12@gofynd.com"},"user exists failure":{"value":""}}}],"headers":[],"path":[]}""", q=q)
        query_string = await create_query_string(q=q)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["userExists"]).netloc, "get", await create_url_without_domain("/service/application/user/authentication/v1.0/user-exists", q=q), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import UserExistsResponse
            schema = UserExistsResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for userExists")
                print(e)

        return response
    
    async def deleteUser(self, body="", request_headers:Dict={}):
        """verify otp and delete user
        """
        payload = {}
        

        # Parameter validation
        schema = UserValidator.deleteUser()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import DeleteApplicationUserRequestSchema
        schema = DeleteApplicationUserRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["deleteUser"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["deleteUser"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/delete", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import DeleteUserSuccess
            schema = DeleteUserSuccess()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteUser")
                print(e)

        return response
    
    async def logout(self, body="", request_headers:Dict={}):
        """Use this API to check to logout a user from the app.
        """
        payload = {}
        

        # Parameter validation
        schema = UserValidator.logout()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["logout"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["logout"]).netloc, "get", await create_url_without_domain("/service/application/user/authentication/v1.0/logout", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import LogoutSuccess
            schema = LogoutSuccess()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for logout")
                print(e)

        return response
    
    async def getUserAttributes(self, slug=None, body="", request_headers:Dict={}):
        """Use this API to get the list of user attributes
        :param slug : Filter by attribute slug. : type string
        """
        payload = {}
        
        if slug is not None:
            payload["slug"] = slug

        # Parameter validation
        schema = UserValidator.getUserAttributes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getUserAttributes"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"slug","schema":{"type":"string"},"description":"Filter by attribute slug."}],"query":[{"in":"query","name":"slug","schema":{"type":"string"},"description":"Filter by attribute slug."}],"headers":[],"path":[]}""", slug=slug)
        query_string = await create_query_string(slug=slug)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getUserAttributes"]).netloc, "get", await create_url_without_domain("/service/application/user/profile/v1.0/user-attributes", slug=slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import UserAttributes
            schema = UserAttributes()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getUserAttributes")
                print(e)

        return response
    
    async def updateUserAttributes(self, body="", request_headers:Dict={}):
        """Use this API to update user attributes
        """
        payload = {}
        

        # Parameter validation
        schema = UserValidator.updateUserAttributes()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UpdateUserAttributesRequest
        schema = UpdateUserAttributesRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(api_url=self._urls["updateUserAttributes"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
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

        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["updateUserAttributes"]).netloc, "patch", await create_url_without_domain("/service/application/user/profile/v1.0/user-attributes", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)

        if 200 <= int(response['status_code']) < 300:
            from .models import UserAttributes
            schema = UserAttributes()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateUserAttributes")
                print(e)

        return response
    