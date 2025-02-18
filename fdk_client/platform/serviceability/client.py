"""Serviceability Platform Client"""
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..PlatformConfig import PlatformConfig

from .validator import ServiceabilityValidator

class Serviceability:
    def __init__(self, config: PlatformConfig):
        self._conf = config

    
    async def createCourierPartnerAccount(self, body="", request_headers:Dict={}):
        """Retrieves a list of courier partner accounts.
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.createCourierPartnerAccount()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CourierAccountDetailsBody
        schema = CourierAccountDetailsBody()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/account", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/account", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CourierAccountDetailsBody
            schema = CourierAccountDetailsBody()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createCourierPartnerAccount")
                print(e)

        return response
    
    async def getCourierPartnerAccounts(self, page_no=None, page_size=None, stage=None, payment_mode=None, transport_type=None, account_ids=None, self_ship=None, own_account=None, q=None, request_headers:Dict={}):
        """Retrieves a list of courier partner accounts.
        :param page_no : The current page number for paginated results. : type integer
        :param page_size : Determines the items to be displayed in a page : type integer
        :param stage : Stage of the account. : type string
        :param payment_mode : Filters dp accounts based on payment mode : type string
        :param transport_type : Filters dp accounts based on transport_type : type string
        :param account_ids : Filters dp accounts based on their ids : type array
        :param self_ship : To filter self ship/non self ship dp accounts : type boolean
        :param own_account : Filters seller owned or Fynd Managed dp accounts : type boolean
        :param q : Filters dp accounts based on case sensitive partial account name : type string
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if stage is not None:
            payload["stage"] = stage
        if payment_mode is not None:
            payload["payment_mode"] = payment_mode
        if transport_type is not None:
            payload["transport_type"] = transport_type
        if account_ids is not None:
            payload["account_ids"] = account_ids
        if self_ship is not None:
            payload["self_ship"] = self_ship
        if own_account is not None:
            payload["own_account"] = own_account
        if q is not None:
            payload["q"] = q

        # Parameter validation
        schema = ServiceabilityValidator.getCourierPartnerAccounts()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/account", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"The current page number for paginated results.","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"Determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"stage","description":"Stage of the account.","schema":{"type":"string","enum":["enabled","disabled"]}},{"in":"query","name":"payment_mode","description":"Filters dp accounts based on payment mode","schema":{"type":"string"}},{"in":"query","name":"transport_type","description":"Filters dp accounts based on transport_type","schema":{"type":"string","enum":["surface","air","waterways"]}},{"in":"query","name":"account_ids","description":"Filters dp accounts based on their ids","schema":{"type":"array","items":{"type":"string"}}},{"in":"query","name":"self_ship","description":"To filter self ship/non self ship dp accounts","schema":{"type":"boolean"}},{"in":"query","name":"own_account","description":"Filters seller owned or Fynd Managed dp accounts","schema":{"type":"boolean"}},{"in":"query","name":"q","description":"Filters dp accounts based on case sensitive partial account name","schema":{"type":"string"}}],"query":[{"in":"query","name":"page_no","description":"The current page number for paginated results.","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"Determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"stage","description":"Stage of the account.","schema":{"type":"string","enum":["enabled","disabled"]}},{"in":"query","name":"payment_mode","description":"Filters dp accounts based on payment mode","schema":{"type":"string"}},{"in":"query","name":"transport_type","description":"Filters dp accounts based on transport_type","schema":{"type":"string","enum":["surface","air","waterways"]}},{"in":"query","name":"account_ids","description":"Filters dp accounts based on their ids","schema":{"type":"array","items":{"type":"string"}}},{"in":"query","name":"self_ship","description":"To filter self ship/non self ship dp accounts","schema":{"type":"boolean"}},{"in":"query","name":"own_account","description":"Filters seller owned or Fynd Managed dp accounts","schema":{"type":"boolean"}},{"in":"query","name":"q","description":"Filters dp accounts based on case sensitive partial account name","schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}]}""", serverType="platform", page_no=page_no, page_size=page_size, stage=stage, payment_mode=payment_mode, transport_type=transport_type, account_ids=account_ids, self_ship=self_ship, own_account=own_account, q=q)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, stage=stage, payment_mode=payment_mode, transport_type=transport_type, account_ids=account_ids, self_ship=self_ship, own_account=own_account, q=q)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/account", page_no=page_no, page_size=page_size, stage=stage, payment_mode=payment_mode, transport_type=transport_type, account_ids=account_ids, self_ship=self_ship, own_account=own_account, q=q), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CompanyCourierPartnerAccountListResult
            schema = CompanyCourierPartnerAccountListResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCourierPartnerAccounts")
                print(e)

        return response
    
    async def updateCourierPartnerAccount(self, account_id=None, body="", request_headers:Dict={}):
        """Updates an existing courier partner account.
        :param account_id : Unique ID of courier account : type string
        """
        payload = {}
        
        if account_id is not None:
            payload["account_id"] = account_id

        # Parameter validation
        schema = ServiceabilityValidator.updateCourierPartnerAccount()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CourierAccountDetailsBody
        schema = CourierAccountDetailsBody()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/account/{account_id}", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"account_id","description":"Unique ID of courier account","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"account_id","description":"Unique ID of courier account","schema":{"type":"string"},"required":true}]}""", serverType="platform", account_id=account_id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/account/{account_id}", account_id=account_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CourierAccountDetailsBody
            schema = CourierAccountDetailsBody()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateCourierPartnerAccount")
                print(e)

        return response
    
    async def getCourierPartnerAccount(self, account_id=None, request_headers:Dict={}):
        """Retrieves a single courier partner account.
        :param account_id : Unique ID of courier account : type string
        """
        payload = {}
        
        if account_id is not None:
            payload["account_id"] = account_id

        # Parameter validation
        schema = ServiceabilityValidator.getCourierPartnerAccount()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/account/{account_id}", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"account_id","description":"Unique ID of courier account","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"account_id","description":"Unique ID of courier account","schema":{"type":"string"},"required":true}]}""", serverType="platform", account_id=account_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/account/{account_id}", account_id=account_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CourierAccountResult
            schema = CourierAccountResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCourierPartnerAccount")
                print(e)

        return response
    
    async def updateCompanyConfiguration(self, body="", request_headers:Dict={}):
        """Updates an existing delivery setup for a company, including the ability to adjust self-shipping preferences.
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.updateCompanyConfiguration()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CompanyConfigurationSchema
        schema = CompanyConfigurationSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/configuration", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/configuration", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CompanyConfig
            schema = CompanyConfig()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateCompanyConfiguration")
                print(e)

        return response
    
    async def getCompanyConfiguration(self, request_headers:Dict={}):
        """Retrieves information about the delivery setup for a company
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.getCompanyConfiguration()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/configuration", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/configuration", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CompanyConfig
            schema = CompanyConfig()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCompanyConfiguration")
                print(e)

        return response
    
    async def bulkTat(self, extension_id=None, scheme_id=None, body="", request_headers:Dict={}):
        """Updates locality wise TAT(Turn Around Time) for particular courier scheme using CSV file.
Export locality wise CSV files.
        :param extension_id : Unique Identifier of courier partner extension. : type string
        :param scheme_id : Unique identifier for the scheme, used to fetch or modify scheme details. : type string
        """
        payload = {}
        
        if extension_id is not None:
            payload["extension_id"] = extension_id
        if scheme_id is not None:
            payload["scheme_id"] = scheme_id

        # Parameter validation
        schema = ServiceabilityValidator.bulkTat()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import BulkRegionJobDetails
        schema = BulkRegionJobDetails()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/courier-partner/{extension_id}/scheme/{scheme_id}/tat", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"extension_id","description":"Unique Identifier of courier partner extension.","schema":{"type":"string"},"required":true},{"in":"path","name":"scheme_id","description":"Unique identifier for the scheme, used to fetch or modify scheme details.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"extension_id","description":"Unique Identifier of courier partner extension.","schema":{"type":"string"},"required":true},{"in":"path","name":"scheme_id","description":"Unique identifier for the scheme, used to fetch or modify scheme details.","schema":{"type":"string"},"required":true}]}""", serverType="platform", extension_id=extension_id, scheme_id=scheme_id)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/courier-partner/{extension_id}/scheme/{scheme_id}/tat", extension_id=extension_id, scheme_id=scheme_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BulkRegionResultItemData
            schema = BulkRegionResultItemData()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for bulkTat")
                print(e)

        return response
    
    async def getBulkTat(self, extension_id=None, scheme_id=None, page_no=None, page_size=None, batch_id=None, action=None, status=None, country=None, region=None, start_date=None, end_date=None, request_headers:Dict={}):
        """Retrieves the history of changes made to TAT(Turn Around Time) for scheme.
        :param extension_id : Unique Identifier of courier partner extension. : type string
        :param scheme_id : Unique identifier for the scheme, used to fetch or modify scheme details. : type string
        :param page_no : The current page number for paginated results. : type integer
        :param page_size : Determines the items to be displayed in a page : type integer
        :param batch_id : Unique identifier of bulk job : type string
        :param action : Import or export bulk type : type string
        :param status : Status of the bulk actions : type string
        :param country : Country for which bulk job is initiated : type string
        :param region : Region for which bulk job is initiated : type string
        :param start_date : Fetch job history after a particule date : type string
        :param end_date : Fetch job history before a particule date : type string
        """
        payload = {}
        
        if extension_id is not None:
            payload["extension_id"] = extension_id
        if scheme_id is not None:
            payload["scheme_id"] = scheme_id
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if batch_id is not None:
            payload["batch_id"] = batch_id
        if action is not None:
            payload["action"] = action
        if status is not None:
            payload["status"] = status
        if country is not None:
            payload["country"] = country
        if region is not None:
            payload["region"] = region
        if start_date is not None:
            payload["start_date"] = start_date
        if end_date is not None:
            payload["end_date"] = end_date

        # Parameter validation
        schema = ServiceabilityValidator.getBulkTat()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/courier-partner/{extension_id}/scheme/{scheme_id}/tat", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"extension_id","description":"Unique Identifier of courier partner extension.","schema":{"type":"string"},"required":true},{"in":"path","name":"scheme_id","description":"Unique identifier for the scheme, used to fetch or modify scheme details.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"The current page number for paginated results.","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"Determines the items to be displayed in a page","schema":{"type":"integer","default":12,"minimum":1}},{"in":"query","name":"batch_id","description":"Unique identifier of bulk job","schema":{"type":"string"}},{"in":"query","name":"action","description":"Import or export bulk type","schema":{"type":"string","enum":["import","export"]}},{"in":"query","name":"status","description":"Status of the bulk actions","schema":{"type":"string","enum":["processing","failed","partial","completed"]}},{"in":"query","name":"country","description":"Country for which bulk job is initiated","schema":{"type":"string"}},{"in":"query","name":"region","description":"Region for which bulk job is initiated","schema":{"type":"string"}},{"in":"query","name":"start_date","description":"Fetch job history after a particule date","schema":{"type":"string","format":"date-time"}},{"in":"query","name":"end_date","description":"Fetch job history before a particule date","schema":{"type":"string","format":"date-time"}}],"query":[{"in":"query","name":"page_no","description":"The current page number for paginated results.","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"Determines the items to be displayed in a page","schema":{"type":"integer","default":12,"minimum":1}},{"in":"query","name":"batch_id","description":"Unique identifier of bulk job","schema":{"type":"string"}},{"in":"query","name":"action","description":"Import or export bulk type","schema":{"type":"string","enum":["import","export"]}},{"in":"query","name":"status","description":"Status of the bulk actions","schema":{"type":"string","enum":["processing","failed","partial","completed"]}},{"in":"query","name":"country","description":"Country for which bulk job is initiated","schema":{"type":"string"}},{"in":"query","name":"region","description":"Region for which bulk job is initiated","schema":{"type":"string"}},{"in":"query","name":"start_date","description":"Fetch job history after a particule date","schema":{"type":"string","format":"date-time"}},{"in":"query","name":"end_date","description":"Fetch job history before a particule date","schema":{"type":"string","format":"date-time"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"extension_id","description":"Unique Identifier of courier partner extension.","schema":{"type":"string"},"required":true},{"in":"path","name":"scheme_id","description":"Unique identifier for the scheme, used to fetch or modify scheme details.","schema":{"type":"string"},"required":true}]}""", serverType="platform", extension_id=extension_id, scheme_id=scheme_id, page_no=page_no, page_size=page_size, batch_id=batch_id, action=action, status=status, country=country, region=region, start_date=start_date, end_date=end_date)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, batch_id=batch_id, action=action, status=status, country=country, region=region, start_date=start_date, end_date=end_date)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/courier-partner/{extension_id}/scheme/{scheme_id}/tat", extension_id=extension_id, scheme_id=scheme_id, page_no=page_no, page_size=page_size, batch_id=batch_id, action=action, status=status, country=country, region=region, start_date=start_date, end_date=end_date), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BulkRegionResult
            schema = BulkRegionResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getBulkTat")
                print(e)

        return response
    
    async def bulkServiceability(self, extension_id=None, scheme_id=None, body="", request_headers:Dict={}):
        """Bulk operations involve either new serviceability settings or updating existing ones in large quantities.
        :param extension_id : Unique Identifier of courier partner extension. : type string
        :param scheme_id : Unique identifier for the scheme, used to fetch or modify scheme details. : type string
        """
        payload = {}
        
        if extension_id is not None:
            payload["extension_id"] = extension_id
        if scheme_id is not None:
            payload["scheme_id"] = scheme_id

        # Parameter validation
        schema = ServiceabilityValidator.bulkServiceability()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import BulkRegionJobDetails
        schema = BulkRegionJobDetails()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/courier-partner/{extension_id}/scheme/{scheme_id}/serviceability/bulk", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"extension_id","description":"Unique Identifier of courier partner extension.","schema":{"type":"string"},"required":true},{"in":"path","name":"scheme_id","description":"Unique identifier for the scheme, used to fetch or modify scheme details.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"extension_id","description":"Unique Identifier of courier partner extension.","schema":{"type":"string"},"required":true},{"in":"path","name":"scheme_id","description":"Unique identifier for the scheme, used to fetch or modify scheme details.","schema":{"type":"string"},"required":true}]}""", serverType="platform", extension_id=extension_id, scheme_id=scheme_id)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/courier-partner/{extension_id}/scheme/{scheme_id}/serviceability/bulk", extension_id=extension_id, scheme_id=scheme_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BulkRegionResultItemData
            schema = BulkRegionResultItemData()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for bulkServiceability")
                print(e)

        return response
    
    async def getBulkServiceability(self, extension_id=None, scheme_id=None, page_no=None, page_size=None, batch_id=None, action=None, status=None, country=None, region=None, start_date=None, end_date=None, request_headers:Dict={}):
        """Retrieves the history of changes made to serviceability settings for a scheme.
        :param extension_id : Unique Identifier of courier partner extension. : type string
        :param scheme_id : Unique identifier for the scheme, used to fetch or modify scheme details. : type string
        :param page_no : The current page number for paginated results. : type integer
        :param page_size : Determines the items to be displayed in a page : type integer
        :param batch_id : Unique identifier of bulk job : type string
        :param action : Import or export bulk type : type string
        :param status : Status of the bulk actions : type string
        :param country : Country for which bulk job is initiated : type string
        :param region : Region for which bulk job is initiated : type string
        :param start_date : Fetch job history after a particule date : type string
        :param end_date : Fetch job history before a particule date : type string
        """
        payload = {}
        
        if extension_id is not None:
            payload["extension_id"] = extension_id
        if scheme_id is not None:
            payload["scheme_id"] = scheme_id
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if batch_id is not None:
            payload["batch_id"] = batch_id
        if action is not None:
            payload["action"] = action
        if status is not None:
            payload["status"] = status
        if country is not None:
            payload["country"] = country
        if region is not None:
            payload["region"] = region
        if start_date is not None:
            payload["start_date"] = start_date
        if end_date is not None:
            payload["end_date"] = end_date

        # Parameter validation
        schema = ServiceabilityValidator.getBulkServiceability()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/courier-partner/{extension_id}/scheme/{scheme_id}/serviceability/bulk", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"extension_id","description":"Unique Identifier of courier partner extension.","schema":{"type":"string"},"required":true},{"in":"path","name":"scheme_id","description":"Unique identifier for the scheme, used to fetch or modify scheme details.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"The current page number for paginated results.","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"Determines the items to be displayed in a page","schema":{"type":"integer","default":12,"minimum":1}},{"in":"query","name":"batch_id","description":"Unique identifier of bulk job","schema":{"type":"string"}},{"in":"query","name":"action","description":"Import or export bulk type","schema":{"type":"string","enum":["import","export"]}},{"in":"query","name":"status","description":"Status of the bulk actions","schema":{"type":"string","enum":["completed","failed","partial","processing"]}},{"in":"query","name":"country","description":"Country for which bulk job is initiated","schema":{"type":"string"}},{"in":"query","name":"region","description":"Region for which bulk job is initiated","schema":{"type":"string"}},{"in":"query","name":"start_date","description":"Fetch job history after a particule date","schema":{"type":"string","format":"date-time"}},{"in":"query","name":"end_date","description":"Fetch job history before a particule date","schema":{"type":"string","format":"date-time"}}],"query":[{"in":"query","name":"page_no","description":"The current page number for paginated results.","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"Determines the items to be displayed in a page","schema":{"type":"integer","default":12,"minimum":1}},{"in":"query","name":"batch_id","description":"Unique identifier of bulk job","schema":{"type":"string"}},{"in":"query","name":"action","description":"Import or export bulk type","schema":{"type":"string","enum":["import","export"]}},{"in":"query","name":"status","description":"Status of the bulk actions","schema":{"type":"string","enum":["completed","failed","partial","processing"]}},{"in":"query","name":"country","description":"Country for which bulk job is initiated","schema":{"type":"string"}},{"in":"query","name":"region","description":"Region for which bulk job is initiated","schema":{"type":"string"}},{"in":"query","name":"start_date","description":"Fetch job history after a particule date","schema":{"type":"string","format":"date-time"}},{"in":"query","name":"end_date","description":"Fetch job history before a particule date","schema":{"type":"string","format":"date-time"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier of the company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"extension_id","description":"Unique Identifier of courier partner extension.","schema":{"type":"string"},"required":true},{"in":"path","name":"scheme_id","description":"Unique identifier for the scheme, used to fetch or modify scheme details.","schema":{"type":"string"},"required":true}]}""", serverType="platform", extension_id=extension_id, scheme_id=scheme_id, page_no=page_no, page_size=page_size, batch_id=batch_id, action=action, status=status, country=country, region=region, start_date=start_date, end_date=end_date)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, batch_id=batch_id, action=action, status=status, country=country, region=region, start_date=start_date, end_date=end_date)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/courier-partner/{extension_id}/scheme/{scheme_id}/serviceability/bulk", extension_id=extension_id, scheme_id=scheme_id, page_no=page_no, page_size=page_size, batch_id=batch_id, action=action, status=status, country=country, region=region, start_date=start_date, end_date=end_date), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BulkRegionResult
            schema = BulkRegionResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getBulkServiceability")
                print(e)

        return response
    
    async def createPackageMaterial(self, page_no=None, body="", request_headers:Dict={}):
        """Creates a packaging material
        :param page_no : The current page number for paginated results. : type integer
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no

        # Parameter validation
        schema = ServiceabilityValidator.createPackageMaterial()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PackageMaterial
        schema = PackageMaterial()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/packaging-materials", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller.","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"The current page number for paginated results.","schema":{"type":"integer"},"required":false}],"query":[{"in":"query","name":"page_no","description":"The current page number for paginated results.","schema":{"type":"integer"},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller.","schema":{"type":"integer"},"required":true}]}""", serverType="platform", page_no=page_no)
        query_string = await create_query_string(page_no=page_no)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/packaging-materials", page_no=page_no), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PackageMaterialResult
            schema = PackageMaterialResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createPackageMaterial")
                print(e)

        return response
    
    async def getPackageMaterialList(self, page_no=None, page_size=None, q=None, size=None, package_type=None, request_headers:Dict={}):
        """Retrieves a list of packaging materials
        :param page_no : The current page number for paginated results. : type integer
        :param page_size : Determines the items to be displayed in a page : type integer
        :param q : Used to search for matching results based on the provided input. : type string
        :param size : Filters items based on given size : type string
        :param package_type : Filters items based on given package_type : type string
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if q is not None:
            payload["q"] = q
        if size is not None:
            payload["size"] = size
        if package_type is not None:
            payload["package_type"] = package_type

        # Parameter validation
        schema = ServiceabilityValidator.getPackageMaterialList()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/packaging-materials", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"The current page number for paginated results.","schema":{"type":"integer","default":1}},{"in":"query","name":"page_size","description":"Determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"q","description":"Used to search for matching results based on the provided input.","schema":{"type":"string"}},{"in":"query","name":"size","description":"Filters items based on given size","schema":{"type":"string"}},{"in":"query","name":"package_type","description":"Filters items based on given package_type","schema":{"type":"string","enum":["Corrugated Box","Wooden Box","Box","Paper Bag"]}}],"query":[{"in":"query","name":"page_no","description":"The current page number for paginated results.","schema":{"type":"integer","default":1}},{"in":"query","name":"page_size","description":"Determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"q","description":"Used to search for matching results based on the provided input.","schema":{"type":"string"}},{"in":"query","name":"size","description":"Filters items based on given size","schema":{"type":"string"}},{"in":"query","name":"package_type","description":"Filters items based on given package_type","schema":{"type":"string","enum":["Corrugated Box","Wooden Box","Box","Paper Bag"]}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}]}""", serverType="platform", page_no=page_no, page_size=page_size, q=q, size=size, package_type=package_type)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, q=q, size=size, package_type=package_type)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/packaging-materials", page_no=page_no, page_size=page_size, q=q, size=size, package_type=package_type), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PackagesListResult
            schema = PackagesListResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPackageMaterialList")
                print(e)

        return response
    
    async def createPackageMaterialRule(self, body="", request_headers:Dict={}):
        """Creates a packaging rule
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.createPackageMaterialRule()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PackageRule
        schema = PackageRule()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/packaging-material/rules", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller.","schema":{"type":"integer"},"required":true}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/packaging-material/rules", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PackageRuleResult
            schema = PackageRuleResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createPackageMaterialRule")
                print(e)

        return response
    
    async def getPackageMaterialRule(self, rule_id=None, request_headers:Dict={}):
        """Retrieve packaging rule details.
        :param rule_id : A `package_material_rule_id` is a unique identifier for a Package Material Rule : type string
        """
        payload = {}
        
        if rule_id is not None:
            payload["rule_id"] = rule_id

        # Parameter validation
        schema = ServiceabilityValidator.getPackageMaterialRule()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/packaging-material/rules/{rule_id}", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller.","schema":{"type":"integer"},"required":true},{"in":"path","name":"rule_id","description":"A `package_material_rule_id` is a unique identifier for a Package Material Rule","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller.","schema":{"type":"integer"},"required":true},{"in":"path","name":"rule_id","description":"A `package_material_rule_id` is a unique identifier for a Package Material Rule","schema":{"type":"string"},"required":true}]}""", serverType="platform", rule_id=rule_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/packaging-material/rules/{rule_id}", rule_id=rule_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PackageRuleResult
            schema = PackageRuleResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPackageMaterialRule")
                print(e)

        return response
    
    async def updatePackageMaterialRule(self, rule_id=None, body="", request_headers:Dict={}):
        """Update an existing packaging rule
        :param rule_id : A `package_material_rule_id` is a unique identifier for a Package Material Rule : type string
        """
        payload = {}
        
        if rule_id is not None:
            payload["rule_id"] = rule_id

        # Parameter validation
        schema = ServiceabilityValidator.updatePackageMaterialRule()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PackageRule
        schema = PackageRule()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/packaging-material/rules/{rule_id}", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller.","schema":{"type":"integer"},"required":true},{"in":"path","name":"rule_id","description":"A `package_material_rule_id` is a unique identifier for a Package Material Rule","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller.","schema":{"type":"integer"},"required":true},{"in":"path","name":"rule_id","description":"A `package_material_rule_id` is a unique identifier for a Package Material Rule","schema":{"type":"string"},"required":true}]}""", serverType="platform", rule_id=rule_id)
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

        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/packaging-material/rules/{rule_id}", rule_id=rule_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PackageRuleResult
            schema = PackageRuleResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updatePackageMaterialRule")
                print(e)

        return response
    
    async def updatePackageMaterials(self, package_material_id=None, body="", request_headers:Dict={}):
        """Update an existing packaging material
        :param package_material_id : A `package_material_id` is a unique identifier for a Package Material : type string
        """
        payload = {}
        
        if package_material_id is not None:
            payload["package_material_id"] = package_material_id

        # Parameter validation
        schema = ServiceabilityValidator.updatePackageMaterials()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PackageMaterial
        schema = PackageMaterial()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/packaging-material/{package_material_id}", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller.","schema":{"type":"integer"},"required":true},{"in":"path","name":"package_material_id","description":"A `package_material_id` is a unique identifier for a Package Material","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller.","schema":{"type":"integer"},"required":true},{"in":"path","name":"package_material_id","description":"A `package_material_id` is a unique identifier for a Package Material","schema":{"type":"string"},"required":true}]}""", serverType="platform", package_material_id=package_material_id)
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

        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/packaging-material/{package_material_id}", package_material_id=package_material_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PackageMaterialResult
            schema = PackageMaterialResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updatePackageMaterials")
                print(e)

        return response
    
    async def getPackageMaterials(self, package_material_id=None, request_headers:Dict={}):
        """Retrieve a single packaging material
        :param package_material_id : A `package_material_id` is a unique identifier for a Package Material : type string
        """
        payload = {}
        
        if package_material_id is not None:
            payload["package_material_id"] = package_material_id

        # Parameter validation
        schema = ServiceabilityValidator.getPackageMaterials()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/packaging-material/{package_material_id}", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"package_material_id","description":"A `package_material_id` is a unique identifier for a Package Material","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"package_material_id","description":"A `package_material_id` is a unique identifier for a Package Material","schema":{"type":"string"},"required":true}]}""", serverType="platform", package_material_id=package_material_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/packaging-material/{package_material_id}", package_material_id=package_material_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PackageItem
            schema = PackageItem()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPackageMaterials")
                print(e)

        return response
    
    async def getOptimalLocations(self, body="", request_headers:Dict={}):
        """Retrieves a list selling locations which are best suited to fullfil an order for a customer.
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.getOptimalLocations()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import OptimlLocationsRequestSchema
        schema = OptimlLocationsRequestSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/optimal-locations", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/optimal-locations", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import OptimalLocationsResult
            schema = OptimalLocationsResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getOptimalLocations")
                print(e)

        return response
    
    async def createCourierPartnerScheme(self, body="", request_headers:Dict={}):
        """Create Scheme for courier partner extension
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.createCourierPartnerScheme()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CourierPartnerSchemeDetailsModel
        schema = CourierPartnerSchemeDetailsModel()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/courier-partner/scheme", """{"required":[{"in":"path","name":"company_id","description":"The unique identifier of the company.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"The unique identifier of the company.","schema":{"type":"integer"},"required":true}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/courier-partner/scheme", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CourierPartnerSchemeModelSchema
            schema = CourierPartnerSchemeModelSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createCourierPartnerScheme")
                print(e)

        return response
    
    async def getCourierPartnerSchemes(self, scheme_type=None, payment_mode=None, capabilities=None, scheme_ids=None, request_headers:Dict={}):
        """Get created Schemes for courier partner
        :param scheme_type : Indicates whether a scheme is created by an admin for global purposes or customized for a specific company. : type string
        :param payment_mode : Indicates payment mode for a scheme. : type string
        :param capabilities : Indicates whether the scheme possesses certain capabilities. : type array
        :param scheme_ids : List of scheme ids which need to be returned in the response. : type array
        """
        payload = {}
        
        if scheme_type is not None:
            payload["scheme_type"] = scheme_type
        if payment_mode is not None:
            payload["payment_mode"] = payment_mode
        if capabilities is not None:
            payload["capabilities"] = capabilities
        if scheme_ids is not None:
            payload["scheme_ids"] = scheme_ids

        # Parameter validation
        schema = ServiceabilityValidator.getCourierPartnerSchemes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/courier-partner/scheme", """{"required":[{"in":"path","name":"company_id","description":"The unique identifier of the company.","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"scheme_type","description":"Indicates whether a scheme is created by an admin for global purposes or customized for a specific company.","schema":{"type":"string","enum":["global","custom"]},"required":false},{"in":"query","name":"payment_mode","description":"Indicates payment mode for a scheme.","schema":{"type":"string","enum":["COD","PREPAID"]},"required":false},{"in":"query","name":"capabilities","description":"Indicates whether the scheme possesses certain capabilities.","schema":{"type":"array","items":{"type":"string"}},"required":false},{"in":"query","name":"scheme_ids","description":"List of scheme ids which need to be returned in the response.","schema":{"type":"array","items":{"type":"string"}},"required":false}],"query":[{"in":"query","name":"scheme_type","description":"Indicates whether a scheme is created by an admin for global purposes or customized for a specific company.","schema":{"type":"string","enum":["global","custom"]},"required":false},{"in":"query","name":"payment_mode","description":"Indicates payment mode for a scheme.","schema":{"type":"string","enum":["COD","PREPAID"]},"required":false},{"in":"query","name":"capabilities","description":"Indicates whether the scheme possesses certain capabilities.","schema":{"type":"array","items":{"type":"string"}},"required":false},{"in":"query","name":"scheme_ids","description":"List of scheme ids which need to be returned in the response.","schema":{"type":"array","items":{"type":"string"}},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"The unique identifier of the company.","schema":{"type":"integer"},"required":true}]}""", serverType="platform", scheme_type=scheme_type, payment_mode=payment_mode, capabilities=capabilities, scheme_ids=scheme_ids)
        query_string = await create_query_string(scheme_type=scheme_type, payment_mode=payment_mode, capabilities=capabilities, scheme_ids=scheme_ids)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/courier-partner/scheme", scheme_type=scheme_type, payment_mode=payment_mode, capabilities=capabilities, scheme_ids=scheme_ids), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CourierPartnerSchemeList
            schema = CourierPartnerSchemeList()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCourierPartnerSchemes")
                print(e)

        return response
    
    async def updateCourierPartnerScheme(self, scheme_id=None, body="", request_headers:Dict={}):
        """Update Scheme for courier partner extension
        :param scheme_id : Unique identifier for the scheme, used to fetch or modify scheme details. : type string
        """
        payload = {}
        
        if scheme_id is not None:
            payload["scheme_id"] = scheme_id

        # Parameter validation
        schema = ServiceabilityValidator.updateCourierPartnerScheme()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CourierPartnerSchemeUpdateDetailsSchema
        schema = CourierPartnerSchemeUpdateDetailsSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/courier-partner/scheme/{scheme_id}", """{"required":[{"in":"path","name":"scheme_id","description":"Unique identifier for the scheme, used to fetch or modify scheme details.","schema":{"type":"string"},"required":true},{"in":"path","name":"company_id","description":"The unique identifier of the company.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"scheme_id","description":"Unique identifier for the scheme, used to fetch or modify scheme details.","schema":{"type":"string"},"required":true},{"in":"path","name":"company_id","description":"The unique identifier of the company.","schema":{"type":"integer"},"required":true}]}""", serverType="platform", scheme_id=scheme_id, )
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/courier-partner/scheme/{scheme_id}", scheme_id=scheme_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CourierPartnerSchemeModelSchema
            schema = CourierPartnerSchemeModelSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateCourierPartnerScheme")
                print(e)

        return response
    
    async def getCourierPartnerScheme(self, scheme_id=None, request_headers:Dict={}):
        """Update Scheme for courier partner extension by Id
        :param scheme_id : Unique identifier for the scheme, used to fetch or modify scheme details. : type string
        """
        payload = {}
        
        if scheme_id is not None:
            payload["scheme_id"] = scheme_id

        # Parameter validation
        schema = ServiceabilityValidator.getCourierPartnerScheme()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/courier-partner/scheme/{scheme_id}", """{"required":[{"in":"path","name":"scheme_id","description":"Unique identifier for the scheme, used to fetch or modify scheme details.","schema":{"type":"string"},"required":true},{"in":"path","name":"company_id","description":"The unique identifier of the company.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"scheme_id","description":"Unique identifier for the scheme, used to fetch or modify scheme details.","schema":{"type":"string"},"required":true},{"in":"path","name":"company_id","description":"The unique identifier of the company.","schema":{"type":"integer"},"required":true}]}""", serverType="platform", scheme_id=scheme_id, )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/courier-partner/scheme/{scheme_id}", scheme_id=scheme_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CourierPartnerSchemeModelSchema
            schema = CourierPartnerSchemeModelSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCourierPartnerScheme")
                print(e)

        return response
    
    async def sampleFileServiceability(self, body="", request_headers:Dict={}):
        """Sample File Download
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.sampleFileServiceability()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import BulkRegionServiceabilityTatDetails
        schema = BulkRegionServiceabilityTatDetails()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/localities/bulk-sample", """{"required":[{"in":"path","name":"company_id","description":"The unique identifier of the company.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"The unique identifier of the company.","schema":{"type":"integer"},"required":true}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/localities/bulk-sample", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BulkRegionServiceabilityTatResultItemData
            schema = BulkRegionServiceabilityTatResultItemData()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for sampleFileServiceability")
                print(e)

        return response
    
    async def getSampleFileServiceabilityStatus(self, page_no=None, page_size=None, batch_id=None, request_headers:Dict={}):
        """Get Serviceability TAT sample file generator status
        :param page_no : The current page number for paginated results. : type integer
        :param page_size : Determines the items to be displayed in a page : type integer
        :param batch_id : Batch id of the execution : type string
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if batch_id is not None:
            payload["batch_id"] = batch_id

        # Parameter validation
        schema = ServiceabilityValidator.getSampleFileServiceabilityStatus()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/localities/bulk-sample", """{"required":[{"in":"path","name":"company_id","description":"The unique identifier of the company.","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"The current page number for paginated results.","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"Determines the items to be displayed in a page","schema":{"type":"integer","default":12,"minimum":1}},{"in":"query","name":"batch_id","description":"Batch id of the execution","schema":{"type":"string"}}],"query":[{"in":"query","name":"page_no","description":"The current page number for paginated results.","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"Determines the items to be displayed in a page","schema":{"type":"integer","default":12,"minimum":1}},{"in":"query","name":"batch_id","description":"Batch id of the execution","schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"The unique identifier of the company.","schema":{"type":"integer"},"required":true}]}""", serverType="platform", page_no=page_no, page_size=page_size, batch_id=batch_id, )
        query_string = await create_query_string(page_no=page_no, page_size=page_size, batch_id=batch_id, )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/localities/bulk-sample", page_no=page_no, page_size=page_size, batch_id=batch_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BulkRegionServiceabilityTatResult
            schema = BulkRegionServiceabilityTatResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getSampleFileServiceabilityStatus")
                print(e)

        return response
    
    async def getCountries(self, onboard=None, page_no=None, page_size=None, q=None, hierarchy=None, request_headers:Dict={}):
        """Retrieve a list of countries for logistical purposes.
        :param onboard : Only fetch countries which allowed for onboard on Platform. : type boolean
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 12 : type integer
        :param q : The search string to search in the list of countries by name. : type string
        :param hierarchy : The search filter to filter countries based on their available hierarchy. : type string
        """
        payload = {}
        
        if onboard is not None:
            payload["onboard"] = onboard
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if q is not None:
            payload["q"] = q
        if hierarchy is not None:
            payload["hierarchy"] = hierarchy

        # Parameter validation
        schema = ServiceabilityValidator.getCountries()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/countries", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"onboard","description":"Only fetch countries which allowed for onboard on Platform.","schema":{"type":"boolean"},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results. Default value is 1.","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"The number of items to retrieve in each page. Default value is 12","schema":{"type":"integer","default":12,"maximum":300},"required":false},{"in":"query","name":"q","description":"The search string to search in the list of countries by name.","schema":{"type":"string"},"required":false},{"in":"query","name":"hierarchy","description":"The search filter to filter countries based on their available hierarchy.","schema":{"type":"string","enum":["state","city","pincode","sector"]},"required":false}],"query":[{"in":"query","name":"onboard","description":"Only fetch countries which allowed for onboard on Platform.","schema":{"type":"boolean"},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results. Default value is 1.","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"The number of items to retrieve in each page. Default value is 12","schema":{"type":"integer","default":12,"maximum":300},"required":false},{"in":"query","name":"q","description":"The search string to search in the list of countries by name.","schema":{"type":"string"},"required":false},{"in":"query","name":"hierarchy","description":"The search filter to filter countries based on their available hierarchy.","schema":{"type":"string","enum":["state","city","pincode","sector"]},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}]}""", serverType="platform", onboard=onboard, page_no=page_no, page_size=page_size, q=q, hierarchy=hierarchy)
        query_string = await create_query_string(onboard=onboard, page_no=page_no, page_size=page_size, q=q, hierarchy=hierarchy)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/countries", onboard=onboard, page_no=page_no, page_size=page_size, q=q, hierarchy=hierarchy), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetCountries
            schema = GetCountries()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCountries")
                print(e)

        return response
    
    async def getInstalledCourierPartnerExtensions(self, page_no=None, page_size=None, is_installed=None, request_headers:Dict={}):
        """This API returns response of Package Materials Rules from mongo database.
        :param page_no : The current page number for paginated results. : type integer
        :param page_size : Determines the items to be displayed in a page : type integer
        :param is_installed : Filter to get installed extensions only : type string
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if is_installed is not None:
            payload["is_installed"] = is_installed

        # Parameter validation
        schema = ServiceabilityValidator.getInstalledCourierPartnerExtensions()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/list", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"The current page number for paginated results.","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"Determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"is_installed","description":"Filter to get installed extensions only","schema":{"type":"string","enum":["true","false"]}}],"query":[{"in":"query","name":"page_no","description":"The current page number for paginated results.","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"Determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"is_installed","description":"Filter to get installed extensions only","schema":{"type":"string","enum":["true","false"]}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}]}""", serverType="platform", page_no=page_no, page_size=page_size, is_installed=is_installed)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, is_installed=is_installed)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/list", page_no=page_no, page_size=page_size, is_installed=is_installed), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import InstallCourierPartnerResponseSchema
            schema = InstallCourierPartnerResponseSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getInstalledCourierPartnerExtensions")
                print(e)

        return response
    
    async def getSelfShipDetails(self, request_headers:Dict={}):
        """Get the self-ship details such as TAT, activation status, and unit for a specified company.
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.getSelfShipDetails()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/selfship", """{"required":[{"name":"company_id","in":"path","description":"Unique identifier of the company","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Unique identifier of the company","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/selfship", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SelfshipSchema
            schema = SelfshipSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getSelfShipDetails")
                print(e)

        return response
    
    async def updateSelfShipDetails(self, body="", request_headers:Dict={}):
        """Updates the self-ship details such as TAT, activation status, and unit for a specified company.
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.updateSelfShipDetails()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SelfshipSchema
        schema = SelfshipSchema()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/selfship", """{"required":[{"name":"company_id","in":"path","description":"Unique identifier of the company","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Unique identifier of the company","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/selfship", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SelfshipSchema
            schema = SelfshipSchema()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateSelfShipDetails")
                print(e)

        return response
    