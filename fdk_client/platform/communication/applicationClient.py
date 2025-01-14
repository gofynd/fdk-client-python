"""Communication Platform Client"""
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..PlatformConfig import PlatformConfig

from .applicationValidator import CommunicationValidator

class Communication:
    def __init__(self, config: PlatformConfig, applicationId: str):
        self._conf = config
        self.applicationId = applicationId

    
    async def getAppProviders(self, request_headers:Dict={}):
        """Retrieve a list of providers associated with the sales channel.
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.getAppProviders()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/app-provider/get-provider", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/app-provider/get-provider", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AppProvider
            schema = AppProvider()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAppProviders")
                print(e)

        return response
    
    async def updateAppProviders(self, body="", request_headers:Dict={}):
        """Modify provider configuration using provider object id .
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.updateAppProviders()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AppProviderReq
        schema = AppProviderReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/app-provider/update-provider", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/app-provider/update-provider", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AppProvider
            schema = AppProvider()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateAppProviders")
                print(e)

        return response
    
    async def getGlobalProviders(self, request_headers:Dict={}):
        """Retrieve a list of global communication providers associated with the sales channel..
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.getGlobalProviders()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/app-provider/global-providers", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/app-provider/global-providers", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GlobalProviders
            schema = GlobalProviders()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getGlobalProviders")
                print(e)

        return response
    
    async def getEmailProviders(self, page_no=None, page_size=None, sort=None, query=None, request_headers:Dict={}):
        """Retrieves a list of all email communication providers associated with the sales channel..
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        :param sort : To sort based on created_at : type object
        :param query : To search based on plain text : type object
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if sort is not None:
            payload["sort"] = sort
        if query is not None:
            payload["query"] = query

        # Parameter validation
        schema = CommunicationValidator.getEmailProviders()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/providers", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}],"optional":[{"in":"query","name":"page_no","description":"Current page no","required":false,"schema":{"type":"integer","minimum":1,"exclusiveMinimum":false,"example":1}},{"in":"query","name":"page_size","description":"Current request items count","required":false,"schema":{"type":"integer","example":10}},{"in":"query","name":"sort","description":"To sort based on created_at","required":false,"schema":{"type":"object","example":{"created_at":-1}}},{"in":"query","name":"query","description":"To search based on plain text","required":false,"schema":{"type":"object","example":{"$or":[{"name":{"$regex":"mk","$options":"i"}},{"tags":{"$regex":"mk","$options":"i"}}]}}}],"query":[{"in":"query","name":"page_no","description":"Current page no","required":false,"schema":{"type":"integer","minimum":1,"exclusiveMinimum":false,"example":1}},{"in":"query","name":"page_size","description":"Current request items count","required":false,"schema":{"type":"integer","example":10}},{"in":"query","name":"sort","description":"To sort based on created_at","required":false,"schema":{"type":"object","example":{"created_at":-1}}},{"in":"query","name":"query","description":"To search based on plain text","required":false,"schema":{"type":"object","example":{"$or":[{"name":{"$regex":"mk","$options":"i"}},{"tags":{"$regex":"mk","$options":"i"}}]}}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}]}""", serverType="platform", page_no=page_no, page_size=page_size, sort=sort, query=query)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, sort=sort, query=query)
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/providers", page_no=page_no, page_size=page_size, sort=sort, query=query), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import EmailProviders
            schema = EmailProviders()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getEmailProviders")
                print(e)

        return response
    
    async def createEmailProvider(self, body="", request_headers:Dict={}):
        """Creates a new email communication provider.
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.createEmailProvider()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import EmailProviderReq
        schema = EmailProviderReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/providers", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/providers", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import EmailProvider
            schema = EmailProvider()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createEmailProvider")
                print(e)

        return response
    
    async def getEmailProviderById(self, id=None, request_headers:Dict={}):
        """Retrieves detailed information about a specific email communication provider.
        :param id : Email provider id : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CommunicationValidator.getEmailProviderById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/providers/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}},{"in":"path","name":"id","description":"Email provider id","required":true,"schema":{"type":"string","example":"5fd9fd44c474a7e3d5d376d6"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}},{"in":"path","name":"id","description":"Email provider id","required":true,"schema":{"type":"string","example":"5fd9fd44c474a7e3d5d376d6"}}]}""", serverType="platform", id=id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/providers/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import EmailProvider
            schema = EmailProvider()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getEmailProviderById")
                print(e)

        return response
    
    async def updateEmailProviderById(self, id=None, body="", request_headers:Dict={}):
        """Modifys the configurations of a specific email communication provider.
        :param id : Email provider id : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CommunicationValidator.updateEmailProviderById()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import EmailProviderReq
        schema = EmailProviderReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/providers/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}},{"in":"path","name":"id","description":"Email provider id","required":true,"schema":{"type":"string","example":"5fd9fd44c474a7e3d5d376d6"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}},{"in":"path","name":"id","description":"Email provider id","required":true,"schema":{"type":"string","example":"5fd9fd44c474a7e3d5d376d6"}}]}""", serverType="platform", id=id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/providers/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import EmailProvider
            schema = EmailProvider()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateEmailProviderById")
                print(e)

        return response
    
    async def deleteEmailProviderById(self, id=None, request_headers:Dict={}):
        """Removes a specific email communication provider from the platform permenantly.
        :param id : Email provider id : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CommunicationValidator.deleteEmailProviderById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/providers/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}},{"in":"path","name":"id","description":"Email provider id","required":true,"schema":{"type":"string","example":"5fd9fd44c474a7e3d5d376d6"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}},{"in":"path","name":"id","description":"Email provider id","required":true,"schema":{"type":"string","example":"5fd9fd44c474a7e3d5d376d6"}}]}""", serverType="platform", id=id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/providers/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GenericDelete
            schema = GenericDelete()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteEmailProviderById")
                print(e)

        return response
    
    async def getSmsProviders(self, page_no=None, page_size=None, sort=None, query=None, request_headers:Dict={}):
        """Retrieves a list of SMS communication providers.
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        :param sort : To sort based on created_at : type object
        :param query : To search based on plain text : type object
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if sort is not None:
            payload["sort"] = sort
        if query is not None:
            payload["query"] = query

        # Parameter validation
        schema = CommunicationValidator.getSmsProviders()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/providers", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}],"optional":[{"in":"query","name":"page_no","description":"Current page no","required":false,"schema":{"type":"integer","minimum":1,"exclusiveMinimum":false,"example":1}},{"in":"query","name":"page_size","description":"Current request items count","required":false,"schema":{"type":"integer","example":10}},{"in":"query","name":"sort","description":"To sort based on created_at","required":false,"schema":{"type":"object","example":{"created_at":-1}}},{"in":"query","name":"query","description":"To search based on plain text","required":false,"schema":{"type":"object","example":{"$or":[{"name":{"$regex":"mk","$options":"i"}},{"tags":{"$regex":"mk","$options":"i"}}]}}}],"query":[{"in":"query","name":"page_no","description":"Current page no","required":false,"schema":{"type":"integer","minimum":1,"exclusiveMinimum":false,"example":1}},{"in":"query","name":"page_size","description":"Current request items count","required":false,"schema":{"type":"integer","example":10}},{"in":"query","name":"sort","description":"To sort based on created_at","required":false,"schema":{"type":"object","example":{"created_at":-1}}},{"in":"query","name":"query","description":"To search based on plain text","required":false,"schema":{"type":"object","example":{"$or":[{"name":{"$regex":"mk","$options":"i"}},{"tags":{"$regex":"mk","$options":"i"}}]}}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}]}""", serverType="platform", page_no=page_no, page_size=page_size, sort=sort, query=query)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, sort=sort, query=query)
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/providers", page_no=page_no, page_size=page_size, sort=sort, query=query), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        return response
    
    async def createSmsProvider(self, body="", request_headers:Dict={}):
        """Creates a new SMS communication provider.
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.createSmsProvider()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SmsProviderReq
        schema = SmsProviderReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/providers", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/providers", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        return response
    
    async def getDefaultSmsProviders(self, request_headers:Dict={}):
        """Retrieve all the default SMS communication providers.
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.getDefaultSmsProviders()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/default-providers", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/default-providers", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        return response
    
    async def getSmsProviderById(self, id=None, request_headers:Dict={}):
        """Retrieve detailed information about a specific SMS communication provider.
        :param id : Sms provider id : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CommunicationValidator.getSmsProviderById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/providers/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}},{"in":"path","name":"id","description":"Sms provider id","required":true,"schema":{"type":"string","example":"5fd9fd07c474a7710dd376d5"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}},{"in":"path","name":"id","description":"Sms provider id","required":true,"schema":{"type":"string","example":"5fd9fd07c474a7710dd376d5"}}]}""", serverType="platform", id=id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/providers/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        return response
    
    async def updateSmsProviderById(self, id=None, body="", request_headers:Dict={}):
        """Modifys the configurations of a specific SMS communication provider.
        :param id : Sms provider id : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CommunicationValidator.updateSmsProviderById()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SmsProviderReq
        schema = SmsProviderReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/providers/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}},{"in":"path","name":"id","description":"Sms provider id","required":true,"schema":{"type":"string","example":"5fd9fd07c474a7710dd376d5"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}},{"in":"path","name":"id","description":"Sms provider id","required":true,"schema":{"type":"string","example":"5fd9fd07c474a7710dd376d5"}}]}""", serverType="platform", id=id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/providers/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        return response
    
    async def deleteSmsProviderById(self, id=None, request_headers:Dict={}):
        """Removes a specific SMS communication provider from the platform permenantly.
        :param id : Sms provider id : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CommunicationValidator.deleteSmsProviderById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/providers/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}},{"in":"path","name":"id","description":"Sms provider id","required":true,"schema":{"type":"string","example":"5fd9fd07c474a7710dd376d5"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}},{"in":"path","name":"id","description":"Sms provider id","required":true,"schema":{"type":"string","example":"5fd9fd07c474a7710dd376d5"}}]}""", serverType="platform", id=id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/providers/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GenericDelete
            schema = GenericDelete()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteSmsProviderById")
                print(e)

        return response
    
    async def getCampaigns(self, query=None, page_no=None, page_size=None, sort=None, request_headers:Dict={}):
        """Retrieves a list of communication campaigns.
        :param query : To search based on plain text : type object
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        :param sort : To sort based on created_at : type object
        """
        payload = {}
        
        if query is not None:
            payload["query"] = query
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if sort is not None:
            payload["sort"] = sort

        # Parameter validation
        schema = CommunicationValidator.getCampaigns()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/campaigns/campaigns", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}],"optional":[{"in":"query","name":"query","description":"To search based on plain text","required":false,"schema":{"type":"object","example":{"$or":[{"name":{"$regex":"mk","$options":"i"}},{"tags":{"$regex":"mk","$options":"i"}}]}}},{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"query":[{"in":"query","name":"query","description":"To search based on plain text","required":false,"schema":{"type":"object","example":{"$or":[{"name":{"$regex":"mk","$options":"i"}},{"tags":{"$regex":"mk","$options":"i"}}]}}},{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}]}""", serverType="platform", query=query, page_no=page_no, page_size=page_size, sort=sort)
        query_string = await create_query_string(query=query, page_no=page_no, page_size=page_size, sort=sort)
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/campaigns/campaigns", query=query, page_no=page_no, page_size=page_size, sort=sort), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import Campaigns
            schema = Campaigns()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCampaigns")
                print(e)

        return response
    
    async def createCampaign(self, body="", request_headers:Dict={}):
        """Creates a new communication campaign.
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.createCampaign()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CampaignReq
        schema = CampaignReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/campaigns/campaigns", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/campaigns/campaigns", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import Campaign
            schema = Campaign()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createCampaign")
                print(e)

        return response
    
    async def getCampaignById(self, id=None, request_headers:Dict={}):
        """Retrieves detailed information about a specific communication campaign.
        :param id : Campaign id : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CommunicationValidator.getCampaignById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/campaigns/campaigns/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}},{"in":"path","name":"id","description":"Campaign id","required":true,"schema":{"type":"string","example":"6009a1ea1f6a61d88e80a867"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}},{"in":"path","name":"id","description":"Campaign id","required":true,"schema":{"type":"string","example":"6009a1ea1f6a61d88e80a867"}}]}""", serverType="platform", id=id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/campaigns/campaigns/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import Campaign
            schema = Campaign()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCampaignById")
                print(e)

        return response
    
    async def updateCampaignById(self, id=None, body="", request_headers:Dict={}):
        """Modify the configuration of a specific communication campaign.
        :param id : Campaign id : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CommunicationValidator.updateCampaignById()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CampaignReq
        schema = CampaignReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/campaigns/campaigns/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}},{"in":"path","name":"id","description":"Campaign id","required":true,"schema":{"type":"string","example":"6009a1ea1f6a61d88e80a867"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}},{"in":"path","name":"id","description":"Campaign id","required":true,"schema":{"type":"string","example":"6009a1ea1f6a61d88e80a867"}}]}""", serverType="platform", id=id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/campaigns/campaigns/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import Campaign
            schema = Campaign()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateCampaignById")
                print(e)

        return response
    
    async def getStatsOfCampaignById(self, id=None, request_headers:Dict={}):
        """Retrieves statistical data for a specific a communication campaign.
        :param id : Campaign id : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CommunicationValidator.getStatsOfCampaignById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/campaigns/get-stats/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}},{"in":"path","name":"id","description":"Campaign id","required":true,"schema":{"type":"string","example":"6009a1ea1f6a61d88e80a867"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}},{"in":"path","name":"id","description":"Campaign id","required":true,"schema":{"type":"string","example":"6009a1ea1f6a61d88e80a867"}}]}""", serverType="platform", id=id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/campaigns/get-stats/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetStats
            schema = GetStats()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getStatsOfCampaignById")
                print(e)

        return response
    
    async def getBigQueryRowCountById(self, id=None, request_headers:Dict={}):
        """Retrieves big query row count by id
        :param id : Audience id : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CommunicationValidator.getBigQueryRowCountById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/bigquery-row-count/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}},{"in":"path","name":"id","description":"Audience id","required":true,"schema":{"type":"string","example":"5fb6675c09fd901023917a5f"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}},{"in":"path","name":"id","description":"Audience id","required":true,"schema":{"type":"string","example":"5fb6675c09fd901023917a5f"}}]}""", serverType="platform", id=id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/bigquery-row-count/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        return response
    
    async def createBigQueryRowCount(self, request_headers:Dict={}):
        """Creates big query row count
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.createBigQueryRowCount()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/bigquery-row-count", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/bigquery-row-count", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        return response
    
    async def getBigQueryHeadersById(self, id=None, request_headers:Dict={}):
        """Retrieves header information from BigQuery.
        :param id : Audience id : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CommunicationValidator.getBigQueryHeadersById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/bigquery-headers/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}},{"in":"path","name":"id","description":"Audience id","required":true,"schema":{"type":"string","example":"5fb6675c09fd901023917a5f"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}},{"in":"path","name":"id","description":"Audience id","required":true,"schema":{"type":"string","example":"5fb6675c09fd901023917a5f"}}]}""", serverType="platform", id=id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/bigquery-headers/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        return response
    
    async def createBigQueryNCount(self, request_headers:Dict={}):
        """Creates big query n count
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.createBigQueryNCount()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/bigquery-n-records", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/bigquery-n-records", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        return response
    
    async def createBigQueryHeaders(self, request_headers:Dict={}):
        """Create BigQuery headers
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.createBigQueryHeaders()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/bigquery-headers", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/bigquery-headers", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        return response
    
    async def getSystemAudiences(self, request_headers:Dict={}):
        """Retrieves a list of  system-defined audiences for communication.
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.getSystemAudiences()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/system-datasources", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/system-datasources", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        return response
    
    async def getAudiences(self, page_no=None, page_size=None, sort=None, query=None, request_headers:Dict={}):
        """Retrieves a list of all the audiences.
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        :param sort : To sort based on created_at : type object
        :param query : To search based on plain text : type object
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if sort is not None:
            payload["sort"] = sort
        if query is not None:
            payload["query"] = query

        # Parameter validation
        schema = CommunicationValidator.getAudiences()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/datasources", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}],"optional":[{"in":"query","name":"page_no","description":"Current page no","required":false,"schema":{"type":"integer","minimum":1,"exclusiveMinimum":false,"example":1}},{"in":"query","name":"page_size","description":"Current request items count","required":false,"schema":{"type":"integer","example":10}},{"in":"query","name":"sort","description":"To sort based on created_at","required":false,"schema":{"type":"object","example":{"created_at":-1}}},{"in":"query","name":"query","description":"To search based on plain text","required":false,"schema":{"type":"object","example":{"$or":[{"name":{"$regex":"mk","$options":"i"}},{"tags":{"$regex":"mk","$options":"i"}}]}}}],"query":[{"in":"query","name":"page_no","description":"Current page no","required":false,"schema":{"type":"integer","minimum":1,"exclusiveMinimum":false,"example":1}},{"in":"query","name":"page_size","description":"Current request items count","required":false,"schema":{"type":"integer","example":10}},{"in":"query","name":"sort","description":"To sort based on created_at","required":false,"schema":{"type":"object","example":{"created_at":-1}}},{"in":"query","name":"query","description":"To search based on plain text","required":false,"schema":{"type":"object","example":{"$or":[{"name":{"$regex":"mk","$options":"i"}},{"tags":{"$regex":"mk","$options":"i"}}]}}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}]}""", serverType="platform", page_no=page_no, page_size=page_size, sort=sort, query=query)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, sort=sort, query=query)
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/datasources", page_no=page_no, page_size=page_size, sort=sort, query=query), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import Audiences
            schema = Audiences()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAudiences")
                print(e)

        return response
    
    async def createAudience(self, body="", request_headers:Dict={}):
        """Creates a new email audience.
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.createAudience()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AudienceReq
        schema = AudienceReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/datasources", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/datasources", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import Audience
            schema = Audience()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createAudience")
                print(e)

        return response
    
    async def getAudienceById(self, id=None, request_headers:Dict={}):
        """Retrieves detailed information about an specific audience.
        :param id : Audience id : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CommunicationValidator.getAudienceById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/datasources/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}},{"in":"path","name":"id","description":"Audience id","required":true,"schema":{"type":"string","example":"5fb6675c09fd901023917a5f"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}},{"in":"path","name":"id","description":"Audience id","required":true,"schema":{"type":"string","example":"5fb6675c09fd901023917a5f"}}]}""", serverType="platform", id=id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/datasources/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import Audience
            schema = Audience()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAudienceById")
                print(e)

        return response
    
    async def updateAudienceById(self, id=None, body="", request_headers:Dict={}):
        """Modify the configuration of a specific audience.
        :param id : Audience id : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CommunicationValidator.updateAudienceById()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AudienceReq
        schema = AudienceReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/datasources/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}},{"in":"path","name":"id","description":"Audience id","required":true,"schema":{"type":"string","example":"5fb6675c09fd901023917a5f"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}},{"in":"path","name":"id","description":"Audience id","required":true,"schema":{"type":"string","example":"5fb6675c09fd901023917a5f"}}]}""", serverType="platform", id=id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/datasources/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import Audience
            schema = Audience()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateAudienceById")
                print(e)

        return response
    
    async def deleteAudienceById(self, id=None, body="", request_headers:Dict={}):
        """Remove a specific audience permenantly.
        :param id : Audience id : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CommunicationValidator.deleteAudienceById()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AudienceReq
        schema = AudienceReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/datasources/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}},{"in":"path","name":"id","description":"Audience id","required":true,"schema":{"type":"string","example":"5fb6675c09fd901023917a5f"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}},{"in":"path","name":"id","description":"Audience id","required":true,"schema":{"type":"string","example":"5fb6675c09fd901023917a5f"}}]}""", serverType="platform", id=id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/datasources/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import Audience
            schema = Audience()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteAudienceById")
                print(e)

        return response
    
    async def getDummyDatasources(self, request_headers:Dict={}):
        """Retrieve a list of dummy data sources.
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.getDummyDatasources()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/datasources/dummy-data-sources", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/datasources/dummy-data-sources", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        return response
    
    async def getDummyDatasourcesMeta(self, id=None, request_headers:Dict={}):
        """Retrieve metadata information about dummy data sources.
        :param id : Dummy datasources meta ID : type integer
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CommunicationValidator.getDummyDatasourcesMeta()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/datasources/dummy-data-sources-meta/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}},{"in":"path","name":"id","description":"Dummy datasources meta ID","required":true,"schema":{"type":"integer","format":"int32","example":2}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}},{"in":"path","name":"id","description":"Dummy datasources meta ID","required":true,"schema":{"type":"integer","format":"int32","example":2}}]}""", serverType="platform", id=id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/datasources/dummy-data-sources-meta/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import DummyDatasourcesMeta
            schema = DummyDatasourcesMeta()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getDummyDatasourcesMeta")
                print(e)

        return response
    
    async def getNSampleRecordsFromCsvByGet(self, request_headers:Dict={}):
        """Retrieve a specified number of sample records from a CSV data source.
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.getNSampleRecordsFromCsvByGet()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/get-n-records", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/get-n-records", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetNRecordsCsvRes
            schema = GetNRecordsCsvRes()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getNSampleRecordsFromCsvByGet")
                print(e)

        return response
    
    async def getNSampleRecordsFromCsv(self, body="", request_headers:Dict={}):
        """Retrieve a specified number of sample records from a CSV data source.
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.getNSampleRecordsFromCsv()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import GetNRecordsCsvReq
        schema = GetNRecordsCsvReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/get-n-records", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/get-n-records", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetNRecordsCsvRes
            schema = GetNRecordsCsvRes()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getNSampleRecordsFromCsv")
                print(e)

        return response
    
    async def getEmailTemplates(self, page_no=None, page_size=None, sort=None, query=None, request_headers:Dict={}):
        """Retrieves a list of available email communication templates.
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        :param sort : To sort based on created_at : type object
        :param query : To search based on plain text : type object
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if sort is not None:
            payload["sort"] = sort
        if query is not None:
            payload["query"] = query

        # Parameter validation
        schema = CommunicationValidator.getEmailTemplates()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/templates", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}],"optional":[{"in":"query","name":"page_no","description":"Current page no","required":false,"schema":{"type":"integer","minimum":1,"exclusiveMinimum":false,"example":1}},{"in":"query","name":"page_size","description":"Current request items count","required":false,"schema":{"type":"integer","example":10}},{"in":"query","name":"sort","description":"To sort based on created_at","required":false,"schema":{"type":"object","example":{"created_at":-1}}},{"in":"query","name":"query","description":"To search based on plain text","required":false,"schema":{"type":"object","example":{"$or":[{"name":{"$regex":"mk","$options":"i"}},{"tags":{"$regex":"mk","$options":"i"}}]}}}],"query":[{"in":"query","name":"page_no","description":"Current page no","required":false,"schema":{"type":"integer","minimum":1,"exclusiveMinimum":false,"example":1}},{"in":"query","name":"page_size","description":"Current request items count","required":false,"schema":{"type":"integer","example":10}},{"in":"query","name":"sort","description":"To sort based on created_at","required":false,"schema":{"type":"object","example":{"created_at":-1}}},{"in":"query","name":"query","description":"To search based on plain text","required":false,"schema":{"type":"object","example":{"$or":[{"name":{"$regex":"mk","$options":"i"}},{"tags":{"$regex":"mk","$options":"i"}}]}}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}]}""", serverType="platform", page_no=page_no, page_size=page_size, sort=sort, query=query)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, sort=sort, query=query)
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/templates", page_no=page_no, page_size=page_size, sort=sort, query=query), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import EmailTemplates
            schema = EmailTemplates()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getEmailTemplates")
                print(e)

        return response
    
    async def createEmailTemplate(self, body="", request_headers:Dict={}):
        """Creates a new email communication template.
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.createEmailTemplate()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import EmailTemplateReq
        schema = EmailTemplateReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/templates", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/templates", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import EmailTemplate
            schema = EmailTemplate()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createEmailTemplate")
                print(e)

        return response
    
    async def getSystemEmailTemplates(self, request_headers:Dict={}):
        """Retrieves system-defined email communication templates.
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.getSystemEmailTemplates()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/system-templates", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/system-templates", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SystemEmailTemplates
            schema = SystemEmailTemplates()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getSystemEmailTemplates")
                print(e)

        return response
    
    async def getEmailTemplateById(self, id=None, request_headers:Dict={}):
        """Retrieves detailed information about a specific email communication template.
        :param id : Email template id : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CommunicationValidator.getEmailTemplateById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/templates/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}},{"in":"path","name":"id","description":"Email template id","required":true,"schema":{"type":"string","example":"5ef42a49c8b67d279c27a980"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}},{"in":"path","name":"id","description":"Email template id","required":true,"schema":{"type":"string","example":"5ef42a49c8b67d279c27a980"}}]}""", serverType="platform", id=id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/templates/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import EmailTemplate
            schema = EmailTemplate()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getEmailTemplateById")
                print(e)

        return response
    
    async def updateEmailTemplateById(self, id=None, body="", request_headers:Dict={}):
        """Modifys the content and settings of a specific email communication template.
        :param id : Email template id : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CommunicationValidator.updateEmailTemplateById()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import EmailTemplateReq
        schema = EmailTemplateReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/templates/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}},{"in":"path","name":"id","description":"Email template id","required":true,"schema":{"type":"string","example":"5ef42a49c8b67d279c27a980"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}},{"in":"path","name":"id","description":"Email template id","required":true,"schema":{"type":"string","example":"5ef42a49c8b67d279c27a980"}}]}""", serverType="platform", id=id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/templates/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import EmailTemplate
            schema = EmailTemplate()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateEmailTemplateById")
                print(e)

        return response
    
    async def deleteEmailTemplateById(self, id=None, request_headers:Dict={}):
        """Removes a specific email communication template from the platform permenantly.
        :param id : Email template id : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CommunicationValidator.deleteEmailTemplateById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/templates/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}},{"in":"path","name":"id","description":"Email template id","required":true,"schema":{"type":"string","example":"5ef42a49c8b67d279c27a980"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}},{"in":"path","name":"id","description":"Email template id","required":true,"schema":{"type":"string","example":"5ef42a49c8b67d279c27a980"}}]}""", serverType="platform", id=id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/templates/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GenericDelete
            schema = GenericDelete()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteEmailTemplateById")
                print(e)

        return response
    
    async def getSubscribedEmailTemplates(self, page_no=None, page_size=None, query=None, request_headers:Dict={}):
        """Retrieves a list of email communication templates that are subscribed to an event.
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        :param query : To search based on plain text : type object
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if query is not None:
            payload["query"] = query

        # Parameter validation
        schema = CommunicationValidator.getSubscribedEmailTemplates()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/subscribedTemplates", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}],"optional":[{"in":"query","name":"page_no","description":"Current page no","required":false,"schema":{"type":"integer","minimum":1,"exclusiveMinimum":false,"example":1}},{"in":"query","name":"page_size","description":"Current request items count","required":false,"schema":{"type":"integer","example":10}},{"in":"query","name":"query","description":"To search based on plain text","required":false,"schema":{"type":"object","example":{"$or":[{"name":{"$regex":"mk","$options":"i"}},{"tags":{"$regex":"mk","$options":"i"}}]}}}],"query":[{"in":"query","name":"page_no","description":"Current page no","required":false,"schema":{"type":"integer","minimum":1,"exclusiveMinimum":false,"example":1}},{"in":"query","name":"page_size","description":"Current request items count","required":false,"schema":{"type":"integer","example":10}},{"in":"query","name":"query","description":"To search based on plain text","required":false,"schema":{"type":"object","example":{"$or":[{"name":{"$regex":"mk","$options":"i"}},{"tags":{"$regex":"mk","$options":"i"}}]}}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}]}""", serverType="platform", page_no=page_no, page_size=page_size, query=query)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, query=query)
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/subscribedTemplates", page_no=page_no, page_size=page_size, query=query), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import EmailTemplates
            schema = EmailTemplates()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getSubscribedEmailTemplates")
                print(e)

        return response
    
    async def getSmsTemplates(self, page_no=None, page_size=None, sort=None, query=None, request_headers:Dict={}):
        """Retrieve a list of all SMS communication templates.
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        :param sort : To sort based on created_at : type object
        :param query : To search based on plain text : type object
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if sort is not None:
            payload["sort"] = sort
        if query is not None:
            payload["query"] = query

        # Parameter validation
        schema = CommunicationValidator.getSmsTemplates()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/templates", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}],"optional":[{"in":"query","name":"page_no","description":"Current page no","required":false,"schema":{"type":"integer","minimum":1,"exclusiveMinimum":false,"example":1}},{"in":"query","name":"page_size","description":"Current request items count","required":false,"schema":{"type":"integer","example":10}},{"in":"query","name":"sort","description":"To sort based on created_at","required":false,"schema":{"type":"object","example":{"created_at":-1}}},{"in":"query","name":"query","description":"To search based on plain text","required":false,"schema":{"type":"object","example":{"$or":[{"name":{"$regex":"mk","$options":"i"}},{"tags":{"$regex":"mk","$options":"i"}}]}}}],"query":[{"in":"query","name":"page_no","description":"Current page no","required":false,"schema":{"type":"integer","minimum":1,"exclusiveMinimum":false,"example":1}},{"in":"query","name":"page_size","description":"Current request items count","required":false,"schema":{"type":"integer","example":10}},{"in":"query","name":"sort","description":"To sort based on created_at","required":false,"schema":{"type":"object","example":{"created_at":-1}}},{"in":"query","name":"query","description":"To search based on plain text","required":false,"schema":{"type":"object","example":{"$or":[{"name":{"$regex":"mk","$options":"i"}},{"tags":{"$regex":"mk","$options":"i"}}]}}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}]}""", serverType="platform", page_no=page_no, page_size=page_size, sort=sort, query=query)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, sort=sort, query=query)
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/templates", page_no=page_no, page_size=page_size, sort=sort, query=query), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SmsTemplates
            schema = SmsTemplates()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getSmsTemplates")
                print(e)

        return response
    
    async def createSmsTemplate(self, body="", request_headers:Dict={}):
        """Creates a new SMS communication template.
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.createSmsTemplate()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SmsTemplateReq
        schema = SmsTemplateReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/templates", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/templates", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SmsTemplate
            schema = SmsTemplate()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createSmsTemplate")
                print(e)

        return response
    
    async def getSystemSmsTemplates(self, request_headers:Dict={}):
        """Retrieves system-defined SMS communication templates.
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.getSystemSmsTemplates()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/system-templates", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/system-templates", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        return response
    
    async def getSmsTemplateById(self, id=None, request_headers:Dict={}):
        """Retrieves detailed information about a specific SMS communication template.
        :param id : Sms template id : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CommunicationValidator.getSmsTemplateById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/templates/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}},{"in":"path","name":"id","description":"Sms template id","required":true,"schema":{"type":"string","example":"5ef42a49c8b67d279c27a980"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}},{"in":"path","name":"id","description":"Sms template id","required":true,"schema":{"type":"string","example":"5ef42a49c8b67d279c27a980"}}]}""", serverType="platform", id=id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/templates/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SmsTemplate
            schema = SmsTemplate()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getSmsTemplateById")
                print(e)

        return response
    
    async def updateSmsTemplateById(self, id=None, body="", request_headers:Dict={}):
        """Modifys the content and settings of a specific SMS communication template.
        :param id : Sms template id : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CommunicationValidator.updateSmsTemplateById()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SmsTemplateReq
        schema = SmsTemplateReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/templates/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}},{"in":"path","name":"id","description":"Sms template id","required":true,"schema":{"type":"string","example":"5ef42a49c8b67d279c27a980"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}},{"in":"path","name":"id","description":"Sms template id","required":true,"schema":{"type":"string","example":"5ef42a49c8b67d279c27a980"}}]}""", serverType="platform", id=id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/templates/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SmsTemplate
            schema = SmsTemplate()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateSmsTemplateById")
                print(e)

        return response
    
    async def deleteSmsTemplateById(self, id=None, request_headers:Dict={}):
        """Removes a specific SMS communication template from the platform permenantly.
        :param id : Sms template id : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CommunicationValidator.deleteSmsTemplateById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/templates/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}},{"in":"path","name":"id","description":"Sms template id","required":true,"schema":{"type":"string","example":"5ef42a49c8b67d279c27a980"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}},{"in":"path","name":"id","description":"Sms template id","required":true,"schema":{"type":"string","example":"5ef42a49c8b67d279c27a980"}}]}""", serverType="platform", id=id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/templates/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GenericDelete
            schema = GenericDelete()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteSmsTemplateById")
                print(e)

        return response
    
    async def getSubscribedSmsTemplates(self, page_no=None, page_size=None, query=None, request_headers:Dict={}):
        """Retrieve a list of SMS communication templates that are subscribed to an event.
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        :param query : To search based on plain text : type object
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if query is not None:
            payload["query"] = query

        # Parameter validation
        schema = CommunicationValidator.getSubscribedSmsTemplates()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/subscribedTemplates", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}],"optional":[{"in":"query","name":"page_no","description":"Current page no","required":false,"schema":{"type":"integer","minimum":1,"exclusiveMinimum":false,"example":1}},{"in":"query","name":"page_size","description":"Current request items count","required":false,"schema":{"type":"integer","example":10}},{"in":"query","name":"query","description":"To search based on plain text","required":false,"schema":{"type":"object","example":{"$or":[{"name":{"$regex":"mk","$options":"i"}},{"tags":{"$regex":"mk","$options":"i"}}]}}}],"query":[{"in":"query","name":"page_no","description":"Current page no","required":false,"schema":{"type":"integer","minimum":1,"exclusiveMinimum":false,"example":1}},{"in":"query","name":"page_size","description":"Current request items count","required":false,"schema":{"type":"integer","example":10}},{"in":"query","name":"query","description":"To search based on plain text","required":false,"schema":{"type":"object","example":{"$or":[{"name":{"$regex":"mk","$options":"i"}},{"tags":{"$regex":"mk","$options":"i"}}]}}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}]}""", serverType="platform", page_no=page_no, page_size=page_size, query=query)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, query=query)
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/subscribedTemplates", page_no=page_no, page_size=page_size, query=query), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SmsTemplates
            schema = SmsTemplates()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getSubscribedSmsTemplates")
                print(e)

        return response
    
    async def sendCommunicationSynchronously(self, body="", request_headers:Dict={}):
        """Sends real-time communications to sellers with immediate delivery.
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.sendCommunicationSynchronously()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import EngineRequest
        schema = EngineRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/engine/send-instant", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/engine/send-instant", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import EngineResponse
            schema = EngineResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for sendCommunicationSynchronously")
                print(e)

        return response
    
    async def sendCommunicationAsynchronously(self, body="", request_headers:Dict={}):
        """Sends communications to sellers with deffered delivery.
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.sendCommunicationAsynchronously()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import EngineRequest
        schema = EngineRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/engine/send-async", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/engine/send-async", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import EngineResponse
            schema = EngineResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for sendCommunicationAsynchronously")
                print(e)

        return response
    
    async def getEventSubscriptions(self, page_no=None, page_size=None, populate=None, request_headers:Dict={}):
        """Retrieves a list of all event subscriptions.
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        :param populate : Populate Fields : type string
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if populate is not None:
            payload["populate"] = populate

        # Parameter validation
        schema = CommunicationValidator.getEventSubscriptions()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/event/event-subscriptions", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}],"optional":[{"in":"query","name":"page_no","description":"Current page no","required":false,"schema":{"type":"integer","minimum":1,"exclusiveMinimum":false,"example":1}},{"in":"query","name":"page_size","description":"Current request items count","required":false,"schema":{"type":"integer","example":10}},{"in":"query","name":"populate","description":"Populate Fields","required":false,"schema":{"type":"string","example":"template.sms.template"}}],"query":[{"in":"query","name":"page_no","description":"Current page no","required":false,"schema":{"type":"integer","minimum":1,"exclusiveMinimum":false,"example":1}},{"in":"query","name":"page_size","description":"Current request items count","required":false,"schema":{"type":"integer","example":10}},{"in":"query","name":"populate","description":"Populate Fields","required":false,"schema":{"type":"string","example":"template.sms.template"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}]}""", serverType="platform", page_no=page_no, page_size=page_size, populate=populate)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, populate=populate)
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/event/event-subscriptions", page_no=page_no, page_size=page_size, populate=populate), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import EventSubscriptions
            schema = EventSubscriptions()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getEventSubscriptions")
                print(e)

        return response
    
    async def createEventSubscriptions(self, body="", request_headers:Dict={}):
        """Creates a new event subscription.
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.createEventSubscriptions()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SubscriptionsObject
        schema = SubscriptionsObject()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/event/event-subscriptions", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/event/event-subscriptions", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import EventSubscriptionsBulkUpdateResponse
            schema = EventSubscriptionsBulkUpdateResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createEventSubscriptions")
                print(e)

        return response
    
    async def getEventSubscriptionsById(self, id=None, populate=None, request_headers:Dict={}):
        """Retrieves detailed information about a specific event subscription.
        :param id : Event subscription id : type string
        :param populate : Populate Fields : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        if populate is not None:
            payload["populate"] = populate

        # Parameter validation
        schema = CommunicationValidator.getEventSubscriptionsById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/event/event-subscriptions/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}},{"in":"path","name":"id","description":"Event subscription id","required":true,"schema":{"type":"string","example":"5fd9fd44c474a7e3d5d376d6"}}],"optional":[{"in":"query","name":"populate","description":"Populate Fields","required":false,"schema":{"type":"string","example":"template.sms.template"}}],"query":[{"in":"query","name":"populate","description":"Populate Fields","required":false,"schema":{"type":"string","example":"template.sms.template"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}},{"in":"path","name":"id","description":"Event subscription id","required":true,"schema":{"type":"string","example":"5fd9fd44c474a7e3d5d376d6"}}]}""", serverType="platform", id=id, populate=populate)
        query_string = await create_query_string(populate=populate)
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/event/event-subscriptions/{id}", id=id, populate=populate), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import EventSubscription
            schema = EventSubscription()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getEventSubscriptionsById")
                print(e)

        return response
    
    async def editEventSubscriptions(self, id=None, body="", request_headers:Dict={}):
        """Modifys the configuration and settings of a specific event subscription.
        :param id : Event subscription id : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CommunicationValidator.editEventSubscriptions()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SubscriptionsObject
        schema = SubscriptionsObject()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/event/event-subscriptions/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}},{"in":"path","name":"id","description":"Event subscription id","required":true,"schema":{"type":"string","example":"5fd9fd44c474a7e3d5d376d6"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}},{"in":"path","name":"id","description":"Event subscription id","required":true,"schema":{"type":"string","example":"5fd9fd44c474a7e3d5d376d6"}}]}""", serverType="platform", id=id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/event/event-subscriptions/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import EventSubscriptionsBulkUpdateResponse
            schema = EventSubscriptionsBulkUpdateResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for editEventSubscriptions")
                print(e)

        return response
    
    async def deleteEventSubscriptionsById(self, id=None, request_headers:Dict={}):
        """Removes a specific event subscription from the platform permenantly.
        :param id : Event subscription id : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CommunicationValidator.deleteEventSubscriptionsById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/event/event-subscriptions/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}},{"in":"path","name":"id","description":"Event subscription id","required":true,"schema":{"type":"string","example":"5fd9fd44c474a7e3d5d376d6"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}},{"in":"path","name":"id","description":"Event subscription id","required":true,"schema":{"type":"string","example":"5fd9fd44c474a7e3d5d376d6"}}]}""", serverType="platform", id=id)
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/event/event-subscriptions/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GenericDelete
            schema = GenericDelete()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteEventSubscriptionsById")
                print(e)

        return response
    
    async def createEventSubscriptionsByBulk(self, body="", request_headers:Dict={}):
        """Creates a new event subscription in bulk.
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.createEventSubscriptionsByBulk()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import EventSubscriptionsBulkUpdateRequest
        schema = EventSubscriptionsBulkUpdateRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/event/event-subscriptions/bulkUpdate", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/event/event-subscriptions/bulkUpdate", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        return response
    
    async def getGlobalVariables(self, request_headers:Dict={}):
        """Retrieves a list of communication global variables.
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.getGlobalVariables()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/global-variables", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/global-variables", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GlobalVariablesGetResponse
            schema = GlobalVariablesGetResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getGlobalVariables")
                print(e)

        return response
    
    async def postGlobalVariables(self, body="", request_headers:Dict={}):
        """Updates and creates communication global variables.
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.postGlobalVariables()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import GlobalVariablesReq
        schema = GlobalVariablesReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/global-variables", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/global-variables", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GlobalVariablesPostResponse
            schema = GlobalVariablesPostResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for postGlobalVariables")
                print(e)

        return response
    
    async def getJobs(self, page_no=None, page_size=None, sort=None, query=None, request_headers:Dict={}):
        """Retrieves a list of campaign jobs.
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        :param sort : To sort based on created_at : type object
        :param query : To search based on plain text : type object
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if sort is not None:
            payload["sort"] = sort
        if query is not None:
            payload["query"] = query

        # Parameter validation
        schema = CommunicationValidator.getJobs()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/jobs/jobs", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}],"optional":[{"in":"query","name":"page_no","description":"Current page no","required":false,"schema":{"type":"integer","minimum":1,"exclusiveMinimum":false,"example":1}},{"in":"query","name":"page_size","description":"Current request items count","required":false,"schema":{"type":"integer","example":10}},{"in":"query","name":"sort","description":"To sort based on created_at","required":false,"schema":{"type":"object","example":{"created_at":-1}}},{"in":"query","name":"query","description":"To search based on plain text","required":false,"schema":{"type":"object","example":{"$or":[{"name":{"$regex":"mk","$options":"i"}},{"tags":{"$regex":"mk","$options":"i"}}]}}}],"query":[{"in":"query","name":"page_no","description":"Current page no","required":false,"schema":{"type":"integer","minimum":1,"exclusiveMinimum":false,"example":1}},{"in":"query","name":"page_size","description":"Current request items count","required":false,"schema":{"type":"integer","example":10}},{"in":"query","name":"sort","description":"To sort based on created_at","required":false,"schema":{"type":"object","example":{"created_at":-1}}},{"in":"query","name":"query","description":"To search based on plain text","required":false,"schema":{"type":"object","example":{"$or":[{"name":{"$regex":"mk","$options":"i"}},{"tags":{"$regex":"mk","$options":"i"}}]}}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}]}""", serverType="platform", page_no=page_no, page_size=page_size, sort=sort, query=query)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, sort=sort, query=query)
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/jobs/jobs", page_no=page_no, page_size=page_size, sort=sort, query=query), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import Jobs
            schema = Jobs()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getJobs")
                print(e)

        return response
    
    async def createJobs(self, body="", request_headers:Dict={}):
        """Creates a new campaign  job.
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.createJobs()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateJobsReq
        schema = CreateJobsReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/jobs/jobs", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/jobs/jobs", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CreateJobsRes
            schema = CreateJobsRes()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createJobs")
                print(e)

        return response
    
    async def triggerCampaignJob(self, body="", request_headers:Dict={}):
        """Initiates a job to execute a communication campaign.
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.triggerCampaignJob()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import TriggerJobRequest
        schema = TriggerJobRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/jobs/trigger-job", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/jobs/trigger-job", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import TriggerJobResponse
            schema = TriggerJobResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for triggerCampaignJob")
                print(e)

        return response
    
    async def getJobLogs(self, page_no=None, page_size=None, sort=None, query=None, request_headers:Dict={}):
        """Retrieve logs and details related to campaign jobs.
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        :param sort : To sort based on created_at : type object
        :param query : To search based on plain text : type object
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if sort is not None:
            payload["sort"] = sort
        if query is not None:
            payload["query"] = query

        # Parameter validation
        schema = CommunicationValidator.getJobLogs()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/jobs/logs", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}],"optional":[{"in":"query","name":"page_no","description":"Current page no","required":false,"schema":{"type":"integer","minimum":1,"exclusiveMinimum":false,"example":1}},{"in":"query","name":"page_size","description":"Current request items count","required":false,"schema":{"type":"integer","example":10}},{"in":"query","name":"sort","description":"To sort based on created_at","required":false,"schema":{"type":"object","example":{"created_at":-1}}},{"in":"query","name":"query","description":"To search based on plain text","required":false,"schema":{"type":"object","example":{"$or":[{"name":{"$regex":"mk","$options":"i"}},{"tags":{"$regex":"mk","$options":"i"}}]}}}],"query":[{"in":"query","name":"page_no","description":"Current page no","required":false,"schema":{"type":"integer","minimum":1,"exclusiveMinimum":false,"example":1}},{"in":"query","name":"page_size","description":"Current request items count","required":false,"schema":{"type":"integer","example":10}},{"in":"query","name":"sort","description":"To sort based on created_at","required":false,"schema":{"type":"object","example":{"created_at":-1}}},{"in":"query","name":"query","description":"To search based on plain text","required":false,"schema":{"type":"object","example":{"$or":[{"name":{"$regex":"mk","$options":"i"}},{"tags":{"$regex":"mk","$options":"i"}}]}}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}]}""", serverType="platform", page_no=page_no, page_size=page_size, sort=sort, query=query)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, sort=sort, query=query)
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/jobs/logs", page_no=page_no, page_size=page_size, sort=sort, query=query), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import JobLogs
            schema = JobLogs()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getJobLogs")
                print(e)

        return response
    
    async def getCommunicationLogs(self, page_id=None, page_size=None, sort=None, query=None, request_headers:Dict={}):
        """Retrieve a lsit of logs and records of communication activities.
        :param page_id : Current page no : type string
        :param page_size : Current request items count : type integer
        :param sort : To sort based on _id : type object
        :param query :  : type object
        """
        payload = {}
        
        if page_id is not None:
            payload["page_id"] = page_id
        if page_size is not None:
            payload["page_size"] = page_size
        if sort is not None:
            payload["sort"] = sort
        if query is not None:
            payload["query"] = query

        # Parameter validation
        schema = CommunicationValidator.getCommunicationLogs()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/log", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}],"optional":[{"name":"page_id","in":"query","schema":{"type":"string"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"_id":{"type":"integer"}}},"description":"To sort based on _id"},{"name":"query","in":"query","schema":{"type":"object"}}],"query":[{"name":"page_id","in":"query","schema":{"type":"string"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"_id":{"type":"integer"}}},"description":"To sort based on _id"},{"name":"query","in":"query","schema":{"type":"object"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}]}""", serverType="platform", page_id=page_id, page_size=page_size, sort=sort, query=query)
        query_string = await create_query_string(page_id=page_id, page_size=page_size, sort=sort, query=query)
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/log", page_id=page_id, page_size=page_size, sort=sort, query=query), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import Logs
            schema = Logs()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCommunicationLogs")
                print(e)

        return response
    
    async def sendOtp(self, body="", request_headers:Dict={}):
        """Sends a one-time password (OTP) for authentication or verification.
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.sendOtp()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SendOtpCommsReq
        schema = SendOtpCommsReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/otp/send-otp-comms", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/otp/send-otp-comms", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SendOtpCommsRes
            schema = SendOtpCommsRes()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for sendOtp")
                print(e)

        return response
    
    async def verfiyOtp(self, body="", request_headers:Dict={}):
        """Verifies the one-time password (OTP) for authentication or verification.
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.verfiyOtp()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import VerifyOtpCommsReq
        schema = VerifyOtpCommsReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/otp/verify-otp-comms", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/otp/verify-otp-comms", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import VerifyOtpCommsSuccessRes
            schema = VerifyOtpCommsSuccessRes()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for verfiyOtp")
                print(e)

        return response
    
    async def getOtpConfiguration(self, request_headers:Dict={}):
        """Retrieves all configurations related to OTP.
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.getOtpConfiguration()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/otp/otp-configuration", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/otp/otp-configuration", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import OtpConfiguration
            schema = OtpConfiguration()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getOtpConfiguration")
                print(e)

        return response
    
    async def updateOtpConfiguration(self, request_headers:Dict={}):
        """Updates all configurations related to OTP.
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.updateOtpConfiguration()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/otp/otp-configuration", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"13741"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"637b6355dc65337da9b5c951"}}]}""", serverType="platform", )
        query_string = await create_query_string()
        if query_string:
            url_with_params += "?" + query_string

        headers = {}
        headers["Authorization"] = f"Bearer {await self._conf.getAccessToken()}"
        for h in self._conf.extraHeaders:
            headers.update(h)
        if request_headers != {}:
            headers.update(request_headers)

        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/otp/otp-configuration", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import OtpConfiguration
            schema = OtpConfiguration()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateOtpConfiguration")
                print(e)

        return response
    