

"""User Application Client"""

import base64
import ujson
from urllib.parse import urlparse

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .validator import UserValidator

class User:
    def __init__(self, config):
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
            "forgotPassword": "/service/application/user/authentication/v1.0/login/password/reset/forgot",
            "sendResetToken": "/service/application/user/authentication/v1.0/login/password/reset/token",
            "loginWithToken": "/service/application/user/authentication/v1.0/login/token",
            "registerWithForm": "/service/application/user/authentication/v1.0/register/form",
            "verifyEmail": "/service/application/user/authentication/v1.0/verify/email",
            "verifyMobile": "/service/application/user/authentication/v1.0/verify/mobile",
            "hasPassword": "/service/application/user/authentication/v1.0/has-password",
            "updatePassword": "/service/application/user/authentication/v1.0/password",
            "deleteUser": "/service/application/user/authentication/v1.0/delete",
            "logout": "/service/application/user/authentication/v1.0/logout",
            "sendOTPOnMobile": "/service/application/user/authentication/v1.0/otp/mobile/send",
            "verifyMobileOTP": "/service/application/user/authentication/v1.0/otp/mobile/verify",
            "sendOTPOnEmail": "/service/application/user/authentication/v1.0/otp/email/send",
            "verifyEmailOTP": "/service/application/user/authentication/v1.0/otp/email/verify",
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
            "sendVerificationLinkToEmail": "/service/application/user/profile/v1.0/email/link/send"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def loginWithFacebook(self, platform=None, body=""):
        """Use this API to login or register using Facebook credentials.
        :param platform : ID of the application : type string
        """
        payload = {}
        
        if platform:
            payload["platform"] = platform
        
        # Parameter validation
        schema = UserValidator.loginWithFacebook()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import OAuthRequestSchema
        schema = OAuthRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["loginWithFacebook"], proccessed_params="""{"required":[],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"headers":[],"path":[]}""", platform=platform)
        query_string = await create_query_string(platform=platform)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["loginWithFacebook"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/login/facebook-token", platform=platform), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def loginWithGoogle(self, platform=None, body=""):
        """Use this API to login or register using Google Account credentials.
        :param platform : ID of the application : type string
        """
        payload = {}
        
        if platform:
            payload["platform"] = platform
        
        # Parameter validation
        schema = UserValidator.loginWithGoogle()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import OAuthRequestSchema
        schema = OAuthRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["loginWithGoogle"], proccessed_params="""{"required":[],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"headers":[],"path":[]}""", platform=platform)
        query_string = await create_query_string(platform=platform)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["loginWithGoogle"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/login/google-token", platform=platform), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def loginWithGoogleAndroid(self, platform=None, body=""):
        """Use this API to login or register in Android app using Google Account credentials.
        :param platform : ID of the application : type string
        """
        payload = {}
        
        if platform:
            payload["platform"] = platform
        
        # Parameter validation
        schema = UserValidator.loginWithGoogleAndroid()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import OAuthRequestSchema
        schema = OAuthRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["loginWithGoogleAndroid"], proccessed_params="""{"required":[],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"headers":[],"path":[]}""", platform=platform)
        query_string = await create_query_string(platform=platform)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["loginWithGoogleAndroid"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/login/google-android", platform=platform), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def loginWithGoogleIOS(self, platform=None, body=""):
        """Use this API to login or register in iOS app using Google Account credentials.
        :param platform : ID of the application : type string
        """
        payload = {}
        
        if platform:
            payload["platform"] = platform
        
        # Parameter validation
        schema = UserValidator.loginWithGoogleIOS()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import OAuthRequestSchema
        schema = OAuthRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["loginWithGoogleIOS"], proccessed_params="""{"required":[],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"headers":[],"path":[]}""", platform=platform)
        query_string = await create_query_string(platform=platform)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["loginWithGoogleIOS"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/login/google-ios", platform=platform), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def loginWithAppleIOS(self, platform=None, body=""):
        """Use this API to login or register in iOS app using Apple Account credentials.
        :param platform : ID of the application : type string
        """
        payload = {}
        
        if platform:
            payload["platform"] = platform
        
        # Parameter validation
        schema = UserValidator.loginWithAppleIOS()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import OAuthRequestAppleSchema
        schema = OAuthRequestAppleSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["loginWithAppleIOS"], proccessed_params="""{"required":[],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"headers":[],"path":[]}""", platform=platform)
        query_string = await create_query_string(platform=platform)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["loginWithAppleIOS"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/login/apple-ios", platform=platform), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def loginWithOTP(self, platform=None, body=""):
        """Use this API to login or register with a One-time Password (OTP) sent via Email or SMS.
        :param platform : ID of the application : type string
        """
        payload = {}
        
        if platform:
            payload["platform"] = platform
        
        # Parameter validation
        schema = UserValidator.loginWithOTP()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SendOtpRequestSchema
        schema = SendOtpRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["loginWithOTP"], proccessed_params="""{"required":[],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"headers":[],"path":[]}""", platform=platform)
        query_string = await create_query_string(platform=platform)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["loginWithOTP"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/login/otp", platform=platform), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def loginWithEmailAndPassword(self, body=""):
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
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["loginWithEmailAndPassword"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/login/password", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def sendResetPasswordEmail(self, platform=None, body=""):
        """Use this API to reset a password using the link sent on email.
        :param platform : ID of the application : type string
        """
        payload = {}
        
        if platform:
            payload["platform"] = platform
        
        # Parameter validation
        schema = UserValidator.sendResetPasswordEmail()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SendResetPasswordEmailRequestSchema
        schema = SendResetPasswordEmailRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["sendResetPasswordEmail"], proccessed_params="""{"required":[],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"headers":[],"path":[]}""", platform=platform)
        query_string = await create_query_string(platform=platform)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["sendResetPasswordEmail"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/login/password/reset", platform=platform), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def sendResetPasswordMobile(self, platform=None, body=""):
        """Use this API to reset a password using the link sent on mobile.
        :param platform : ID of the application : type string
        """
        payload = {}
        
        if platform:
            payload["platform"] = platform
        
        # Parameter validation
        schema = UserValidator.sendResetPasswordMobile()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SendResetPasswordMobileRequestSchema
        schema = SendResetPasswordMobileRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["sendResetPasswordMobile"], proccessed_params="""{"required":[],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"headers":[],"path":[]}""", platform=platform)
        query_string = await create_query_string(platform=platform)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["sendResetPasswordMobile"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/login/password/mobile/reset", platform=platform), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def forgotPassword(self, body=""):
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
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["forgotPassword"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/login/password/reset/forgot", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def sendResetToken(self, body=""):
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
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["sendResetToken"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/login/password/reset/token", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def loginWithToken(self, body=""):
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
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["loginWithToken"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/login/token", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def registerWithForm(self, platform=None, body=""):
        """Use this API to perform user registration by sending form data in the request body.
        :param platform : ID of the application : type string
        """
        payload = {}
        
        if platform:
            payload["platform"] = platform
        
        # Parameter validation
        schema = UserValidator.registerWithForm()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import FormRegisterRequestSchema
        schema = FormRegisterRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["registerWithForm"], proccessed_params="""{"required":[],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"headers":[],"path":[]}""", platform=platform)
        query_string = await create_query_string(platform=platform)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["registerWithForm"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/register/form", platform=platform), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def verifyEmail(self, body=""):
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
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["verifyEmail"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/verify/email", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def verifyMobile(self, body=""):
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
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["verifyMobile"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/verify/mobile", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def hasPassword(self, body=""):
        """Use this API to check if user has created a password for login.
        """
        payload = {}
        
        # Parameter validation
        schema = UserValidator.hasPassword()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["hasPassword"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["hasPassword"]).netloc, "get", await create_url_without_domain("/service/application/user/authentication/v1.0/has-password", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def updatePassword(self, body=""):
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
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["updatePassword"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/password", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def deleteUser(self, body=""):
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
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["deleteUser"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/delete", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def logout(self, body=""):
        """Use this API to check to logout a user from the app.
        """
        payload = {}
        
        # Parameter validation
        schema = UserValidator.logout()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["logout"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["logout"]).netloc, "get", await create_url_without_domain("/service/application/user/authentication/v1.0/logout", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def sendOTPOnMobile(self, platform=None, body=""):
        """Use this API to send an OTP to a mobile number.
        :param platform : ID of the application : type string
        """
        payload = {}
        
        if platform:
            payload["platform"] = platform
        
        # Parameter validation
        schema = UserValidator.sendOTPOnMobile()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SendMobileOtpRequestSchema
        schema = SendMobileOtpRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["sendOTPOnMobile"], proccessed_params="""{"required":[],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"headers":[],"path":[]}""", platform=platform)
        query_string = await create_query_string(platform=platform)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["sendOTPOnMobile"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/otp/mobile/send", platform=platform), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def verifyMobileOTP(self, platform=None, body=""):
        """Use this API to verify the OTP received on a mobile number.
        :param platform : ID of the application : type string
        """
        payload = {}
        
        if platform:
            payload["platform"] = platform
        
        # Parameter validation
        schema = UserValidator.verifyMobileOTP()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import VerifyOtpRequestSchema
        schema = VerifyOtpRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["verifyMobileOTP"], proccessed_params="""{"required":[],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"headers":[],"path":[]}""", platform=platform)
        query_string = await create_query_string(platform=platform)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["verifyMobileOTP"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/otp/mobile/verify", platform=platform), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def sendOTPOnEmail(self, platform=None, body=""):
        """Use this API to send an OTP to an email ID.
        :param platform : ID of the application : type string
        """
        payload = {}
        
        if platform:
            payload["platform"] = platform
        
        # Parameter validation
        schema = UserValidator.sendOTPOnEmail()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SendEmailOtpRequestSchema
        schema = SendEmailOtpRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["sendOTPOnEmail"], proccessed_params="""{"required":[],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"headers":[],"path":[]}""", platform=platform)
        query_string = await create_query_string(platform=platform)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["sendOTPOnEmail"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/otp/email/send", platform=platform), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def verifyEmailOTP(self, platform=None, body=""):
        """Use this API to verify the OTP received on an email ID.
        :param platform : ID of the application : type string
        """
        payload = {}
        
        if platform:
            payload["platform"] = platform
        
        # Parameter validation
        schema = UserValidator.verifyEmailOTP()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import VerifyEmailOtpRequestSchema
        schema = VerifyEmailOtpRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["verifyEmailOTP"], proccessed_params="""{"required":[],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"headers":[],"path":[]}""", platform=platform)
        query_string = await create_query_string(platform=platform)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["verifyEmailOTP"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/otp/email/verify", platform=platform), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getLoggedInUser(self, body=""):
        """Use this API  to get the details of a logged in user.
        """
        payload = {}
        
        # Parameter validation
        schema = UserValidator.getLoggedInUser()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getLoggedInUser"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getLoggedInUser"]).netloc, "get", await create_url_without_domain("/service/application/user/authentication/v1.0/session", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getListOfActiveSessions(self, body=""):
        """Use this API to retrieve all active sessions of a user.
        """
        payload = {}
        
        # Parameter validation
        schema = UserValidator.getListOfActiveSessions()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getListOfActiveSessions"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getListOfActiveSessions"]).netloc, "get", await create_url_without_domain("/service/application/user/authentication/v1.0/sessions", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getPlatformConfig(self, name=None, body=""):
        """Use this API to get all the platform configurations such as mobile image, desktop image, social logins, and all other text.
        :param name : Name of the application, e.g. Fynd : type string
        """
        payload = {}
        
        if name:
            payload["name"] = name
        
        # Parameter validation
        schema = UserValidator.getPlatformConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getPlatformConfig"], proccessed_params="""{"required":[],"optional":[{"name":"name","in":"query","description":"Name of the application, e.g. Fynd","schema":{"type":"string"}}],"query":[{"name":"name","in":"query","description":"Name of the application, e.g. Fynd","schema":{"type":"string"}}],"headers":[],"path":[]}""", name=name)
        query_string = await create_query_string(name=name)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["getPlatformConfig"]).netloc, "get", await create_url_without_domain("/service/application/user/platform/v1.0/config", name=name), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def updateProfile(self, platform=None, body=""):
        """Use this API to update details in the user profile. Details can be first name, last name, gender, email, phone number, or profile picture.
        :param platform : ID of the application : type string
        """
        payload = {}
        
        if platform:
            payload["platform"] = platform
        
        # Parameter validation
        schema = UserValidator.updateProfile()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import EditProfileRequestSchema
        schema = EditProfileRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["updateProfile"], proccessed_params="""{"required":[],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"headers":[],"path":[]}""", platform=platform)
        query_string = await create_query_string(platform=platform)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["updateProfile"]).netloc, "post", await create_url_without_domain("/service/application/user/profile/v1.0/detail", platform=platform), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def addMobileNumber(self, platform=None, body=""):
        """Use this API to add a new mobile number to a profile.
        :param platform : ID of the application : type string
        """
        payload = {}
        
        if platform:
            payload["platform"] = platform
        
        # Parameter validation
        schema = UserValidator.addMobileNumber()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import EditMobileRequestSchema
        schema = EditMobileRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["addMobileNumber"], proccessed_params="""{"required":[],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"headers":[],"path":[]}""", platform=platform)
        query_string = await create_query_string(platform=platform)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["addMobileNumber"]).netloc, "put", await create_url_without_domain("/service/application/user/profile/v1.0/mobile", platform=platform), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def deleteMobileNumber(self, platform=None, active=None, primary=None, verified=None, country_code=None, phone=None, body=""):
        """Use this API to delete a mobile number from a profile.
        :param platform : ID of the application : type string
        :param active : This is a boolean value to check if mobile number is active 1.True - Number is active 2. False - Number is inactive : type boolean
        :param primary : This is a boolean value to check if mobile number is primary number (main number) 1. True - Number is primary 2. False - Number is not primary : type boolean
        :param verified : This is a boolean value to check if mobile number is verified 1. True - Number is verified 2.False - Number is not verified yet : type boolean
        :param country_code : Country code of the phone number, e.g. 91 : type string
        :param phone : Phone number : type string
        """
        payload = {}
        
        if platform:
            payload["platform"] = platform
        
        if active:
            payload["active"] = active
        
        if primary:
            payload["primary"] = primary
        
        if verified:
            payload["verified"] = verified
        
        if country_code:
            payload["country_code"] = country_code
        
        if phone:
            payload["phone"] = phone
        
        # Parameter validation
        schema = UserValidator.deleteMobileNumber()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["deleteMobileNumber"], proccessed_params="""{"required":[{"name":"active","in":"query","required":true,"description":"This is a boolean value to check if mobile number is active 1.True - Number is active 2. False - Number is inactive","schema":{"type":"boolean"}},{"name":"primary","in":"query","description":"This is a boolean value to check if mobile number is primary number (main number) 1. True - Number is primary 2. False - Number is not primary","required":true,"schema":{"type":"boolean"}},{"name":"verified","in":"query","description":"This is a boolean value to check if mobile number is verified 1. True - Number is verified 2.False - Number is not verified yet","required":true,"schema":{"type":"boolean"}},{"name":"country_code","in":"query","description":"Country code of the phone number, e.g. 91","required":true,"schema":{"type":"string"}},{"name":"phone","in":"query","description":"Phone number","required":true,"schema":{"type":"string"}}],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}},{"name":"active","in":"query","required":true,"description":"This is a boolean value to check if mobile number is active 1.True - Number is active 2. False - Number is inactive","schema":{"type":"boolean"}},{"name":"primary","in":"query","description":"This is a boolean value to check if mobile number is primary number (main number) 1. True - Number is primary 2. False - Number is not primary","required":true,"schema":{"type":"boolean"}},{"name":"verified","in":"query","description":"This is a boolean value to check if mobile number is verified 1. True - Number is verified 2.False - Number is not verified yet","required":true,"schema":{"type":"boolean"}},{"name":"country_code","in":"query","description":"Country code of the phone number, e.g. 91","required":true,"schema":{"type":"string"}},{"name":"phone","in":"query","description":"Phone number","required":true,"schema":{"type":"string"}}],"headers":[],"path":[]}""", platform=platform, active=active, primary=primary, verified=verified, country_code=country_code, phone=phone)
        query_string = await create_query_string(platform=platform, active=active, primary=primary, verified=verified, country_code=country_code, phone=phone)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["deleteMobileNumber"]).netloc, "delete", await create_url_without_domain("/service/application/user/profile/v1.0/mobile", platform=platform, active=active, primary=primary, verified=verified, country_code=country_code, phone=phone), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def setMobileNumberAsPrimary(self, body=""):
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
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["setMobileNumberAsPrimary"]).netloc, "post", await create_url_without_domain("/service/application/user/profile/v1.0/mobile/primary", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def sendVerificationLinkToMobile(self, platform=None, body=""):
        """Use this API to send a verification link to a mobile number
        :param platform : ID of the application : type string
        """
        payload = {}
        
        if platform:
            payload["platform"] = platform
        
        # Parameter validation
        schema = UserValidator.sendVerificationLinkToMobile()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SendVerificationLinkMobileRequestSchema
        schema = SendVerificationLinkMobileRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["sendVerificationLinkToMobile"], proccessed_params="""{"required":[],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"headers":[],"path":[]}""", platform=platform)
        query_string = await create_query_string(platform=platform)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["sendVerificationLinkToMobile"]).netloc, "post", await create_url_without_domain("/service/application/user/profile/v1.0/mobile/link/send", platform=platform), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def addEmail(self, platform=None, body=""):
        """Use this API to add a new email address to a profile
        :param platform : ID of the application : type string
        """
        payload = {}
        
        if platform:
            payload["platform"] = platform
        
        # Parameter validation
        schema = UserValidator.addEmail()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import EditEmailRequestSchema
        schema = EditEmailRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["addEmail"], proccessed_params="""{"required":[],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"headers":[],"path":[]}""", platform=platform)
        query_string = await create_query_string(platform=platform)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["addEmail"]).netloc, "put", await create_url_without_domain("/service/application/user/profile/v1.0/email", platform=platform), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def deleteEmail(self, platform=None, active=None, primary=None, verified=None, email=None, body=""):
        """Use this API to delete an email address from a profile
        :param platform : ID of the application : type string
        :param active : This is a boolean value to check if email ID is active 1. True - Email ID is active 2.False - Email ID is inactive : type boolean
        :param primary : This is a boolean value to check if email ID is primary (main email ID) 1. True - Email ID is primary 2.False - Email ID is not primary : type boolean
        :param verified : This is a boolean value to check if email ID is verified 1. True - Email ID is verified 2.False - Email ID is not verified yet : type boolean
        :param email : The email ID to delete : type string
        """
        payload = {}
        
        if platform:
            payload["platform"] = platform
        
        if active:
            payload["active"] = active
        
        if primary:
            payload["primary"] = primary
        
        if verified:
            payload["verified"] = verified
        
        if email:
            payload["email"] = email
        
        # Parameter validation
        schema = UserValidator.deleteEmail()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["deleteEmail"], proccessed_params="""{"required":[{"name":"active","in":"query","description":"This is a boolean value to check if email ID is active 1. True - Email ID is active 2.False - Email ID is inactive","required":true,"schema":{"type":"boolean"}},{"name":"primary","in":"query","description":"This is a boolean value to check if email ID is primary (main email ID) 1. True - Email ID is primary 2.False - Email ID is not primary","required":true,"schema":{"type":"boolean"}},{"name":"verified","in":"query","description":"This is a boolean value to check if email ID is verified 1. True - Email ID is verified 2.False - Email ID is not verified yet","required":true,"schema":{"type":"boolean"}},{"name":"email","in":"query","description":"The email ID to delete","required":true,"schema":{"type":"string"}}],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}},{"name":"active","in":"query","description":"This is a boolean value to check if email ID is active 1. True - Email ID is active 2.False - Email ID is inactive","required":true,"schema":{"type":"boolean"}},{"name":"primary","in":"query","description":"This is a boolean value to check if email ID is primary (main email ID) 1. True - Email ID is primary 2.False - Email ID is not primary","required":true,"schema":{"type":"boolean"}},{"name":"verified","in":"query","description":"This is a boolean value to check if email ID is verified 1. True - Email ID is verified 2.False - Email ID is not verified yet","required":true,"schema":{"type":"boolean"}},{"name":"email","in":"query","description":"The email ID to delete","required":true,"schema":{"type":"string"}}],"headers":[],"path":[]}""", platform=platform, active=active, primary=primary, verified=verified, email=email)
        query_string = await create_query_string(platform=platform, active=active, primary=primary, verified=verified, email=email)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["deleteEmail"]).netloc, "delete", await create_url_without_domain("/service/application/user/profile/v1.0/email", platform=platform, active=active, primary=primary, verified=verified, email=email), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def setEmailAsPrimary(self, body=""):
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
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["setEmailAsPrimary"]).netloc, "post", await create_url_without_domain("/service/application/user/profile/v1.0/email/primary", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def sendVerificationLinkToEmail(self, platform=None, body=""):
        """Use this API to send verification link to an email address.
        :param platform : ID of the application : type string
        """
        payload = {}
        
        if platform:
            payload["platform"] = platform
        
        # Parameter validation
        schema = UserValidator.sendVerificationLinkToEmail()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import EditEmailRequestSchema
        schema = EditEmailRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["sendVerificationLinkToEmail"], proccessed_params="""{"required":[],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"headers":[],"path":[]}""", platform=platform)
        query_string = await create_query_string(platform=platform)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(urlparse(self._urls["sendVerificationLinkToEmail"]).netloc, "post", await create_url_without_domain("/service/application/user/profile/v1.0/email/link/send", platform=platform), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    

