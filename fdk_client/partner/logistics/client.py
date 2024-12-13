"""Logistics Partner Client"""
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..PartnerConfig import PartnerConfig

from .validator import LogisticsValidator

class Logistics:
    def __init__(self, config: PartnerConfig):
        self._conf = config

    
    async def sampleFileServiceability(self, body="", request_headers:Dict={}):
        """Sample File Download
        """
        payload = {}
        

        # Parameter validation
        schema = LogisticsValidator.sampleFileServiceability()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import BulkRegionServiceabilityTatRequest
        schema = BulkRegionServiceabilityTatRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/logistics/v1.0/organization/{self._conf.organizationId}/localities/bulk-sample", """{"required":[{"in":"path","name":"organization_id","description":"Unique Identifier of Organization","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"organization_id","description":"Unique Identifier of Organization","schema":{"type":"string"},"required":true}]}""", serverType="partner", )
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/partner/logistics/v1.0/organization/{self._conf.organizationId}/localities/bulk-sample", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BulkRegionServiceabilityTatResponseItemData
            schema = BulkRegionServiceabilityTatResponseItemData()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for sampleFileServiceability")
                print(e)

        return response
    
    async def getSampleFileServiceabilityStatus(self, page_no=None, page_size=None, batch_id=None, request_headers:Dict={}):
        """Get Serviceability TAT sample file generator status
        :param page_no : index of the item to start returning with : type integer
        :param page_size : determines the items to be displayed in a page : type integer
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
        schema = LogisticsValidator.getSampleFileServiceabilityStatus()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/logistics/v1.0/organization/{self._conf.organizationId}/localities/bulk-sample", """{"required":[{"in":"path","name":"organization_id","description":"Unique Identifier of Organization","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"determines the items to be displayed in a page","schema":{"type":"integer","default":12,"minimum":1}},{"in":"query","name":"batch_id","description":"Batch id of the execution","schema":{"type":"string"}}],"query":[{"in":"query","name":"page_no","description":"index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"determines the items to be displayed in a page","schema":{"type":"integer","default":12,"minimum":1}},{"in":"query","name":"batch_id","description":"Batch id of the execution","schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"organization_id","description":"Unique Identifier of Organization","schema":{"type":"string"},"required":true}]}""", serverType="partner", page_no=page_no, page_size=page_size, batch_id=batch_id)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, batch_id=batch_id)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/partner/logistics/v1.0/organization/{self._conf.organizationId}/localities/bulk-sample", page_no=page_no, page_size=page_size, batch_id=batch_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BulkRegionServiceabilityTatResponse
            schema = BulkRegionServiceabilityTatResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getSampleFileServiceabilityStatus")
                print(e)

        return response
    
    async def bulkTat(self, extension_id=None, scheme_id=None, body="", request_headers:Dict={}):
        """Region TAT Import or Export
        :param extension_id : Unique Identifier of CP Extension : type string
        :param scheme_id : Unique identifier of a scheme : type string
        """
        payload = {}
        
        if extension_id is not None:
            payload["extension_id"] = extension_id
        if scheme_id is not None:
            payload["scheme_id"] = scheme_id

        # Parameter validation
        schema = LogisticsValidator.bulkTat()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import BulkRegionJobSerializer
        schema = BulkRegionJobSerializer()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/logistics/v1.0/organization/{self._conf.organizationId}/courier-partner/{extension_id}/scheme/{scheme_id}/tat", """{"required":[{"in":"path","name":"organization_id","description":"Unique Identifier of Organization","schema":{"type":"string"},"required":true},{"in":"path","name":"extension_id","description":"Unique Identifier of CP Extension","schema":{"type":"string"},"required":true},{"in":"path","name":"scheme_id","description":"Unique identifier of a scheme","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"organization_id","description":"Unique Identifier of Organization","schema":{"type":"string"},"required":true},{"in":"path","name":"extension_id","description":"Unique Identifier of CP Extension","schema":{"type":"string"},"required":true},{"in":"path","name":"scheme_id","description":"Unique identifier of a scheme","schema":{"type":"string"},"required":true}]}""", serverType="partner", extension_id=extension_id, scheme_id=scheme_id)
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/partner/logistics/v1.0/organization/{self._conf.organizationId}/courier-partner/{extension_id}/scheme/{scheme_id}/tat", extension_id=extension_id, scheme_id=scheme_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BulkRegionResponseItemData
            schema = BulkRegionResponseItemData()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for bulkTat")
                print(e)

        return response
    
    async def getBulkTat(self, extension_id=None, scheme_id=None, page_no=None, page_size=None, batch_id=None, action=None, status=None, country=None, region=None, start_date=None, end_date=None, request_headers:Dict={}):
        """Get region tat bulk history
        :param extension_id : Unique Identifier of CP Extension : type string
        :param scheme_id : Unique identifier of a scheme : type string
        :param page_no : index of the item to start returning with : type integer
        :param page_size : determines the items to be displayed in a page : type integer
        :param batch_id : Unique identifier of bulk job : type string
        :param action : import or export bulk type : type string
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
        schema = LogisticsValidator.getBulkTat()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/logistics/v1.0/organization/{self._conf.organizationId}/courier-partner/{extension_id}/scheme/{scheme_id}/tat", """{"required":[{"in":"path","name":"organization_id","description":"Unique Identifier of Organization","schema":{"type":"string"},"required":true},{"in":"path","name":"extension_id","description":"Unique Identifier of CP Extension","schema":{"type":"string"},"required":true},{"in":"path","name":"scheme_id","description":"Unique identifier of a scheme","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"determines the items to be displayed in a page","schema":{"type":"integer","default":12,"minimum":1}},{"in":"query","name":"batch_id","description":"Unique identifier of bulk job","schema":{"type":"string"}},{"in":"query","name":"action","description":"import or export bulk type","schema":{"type":"string"}},{"in":"query","name":"status","description":"Status of the bulk actions","schema":{"type":"string"}},{"in":"query","name":"country","description":"Country for which bulk job is initiated","schema":{"type":"string"}},{"in":"query","name":"region","description":"Region for which bulk job is initiated","schema":{"type":"string"}},{"in":"query","name":"start_date","description":"Fetch job history after a particule date","example":"2023-08-03T00:00:00.000Z","schema":{"type":"string"}},{"in":"query","name":"end_date","description":"Fetch job history before a particule date","example":"2023-08-03T00:00:00.000Z","schema":{"type":"string"}}],"query":[{"in":"query","name":"page_no","description":"index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"determines the items to be displayed in a page","schema":{"type":"integer","default":12,"minimum":1}},{"in":"query","name":"batch_id","description":"Unique identifier of bulk job","schema":{"type":"string"}},{"in":"query","name":"action","description":"import or export bulk type","schema":{"type":"string"}},{"in":"query","name":"status","description":"Status of the bulk actions","schema":{"type":"string"}},{"in":"query","name":"country","description":"Country for which bulk job is initiated","schema":{"type":"string"}},{"in":"query","name":"region","description":"Region for which bulk job is initiated","schema":{"type":"string"}},{"in":"query","name":"start_date","description":"Fetch job history after a particule date","example":"2023-08-03T00:00:00.000Z","schema":{"type":"string"}},{"in":"query","name":"end_date","description":"Fetch job history before a particule date","example":"2023-08-03T00:00:00.000Z","schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"organization_id","description":"Unique Identifier of Organization","schema":{"type":"string"},"required":true},{"in":"path","name":"extension_id","description":"Unique Identifier of CP Extension","schema":{"type":"string"},"required":true},{"in":"path","name":"scheme_id","description":"Unique identifier of a scheme","schema":{"type":"string"},"required":true}]}""", serverType="partner", extension_id=extension_id, scheme_id=scheme_id, page_no=page_no, page_size=page_size, batch_id=batch_id, action=action, status=status, country=country, region=region, start_date=start_date, end_date=end_date)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, batch_id=batch_id, action=action, status=status, country=country, region=region, start_date=start_date, end_date=end_date)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/partner/logistics/v1.0/organization/{self._conf.organizationId}/courier-partner/{extension_id}/scheme/{scheme_id}/tat", extension_id=extension_id, scheme_id=scheme_id, page_no=page_no, page_size=page_size, batch_id=batch_id, action=action, status=status, country=country, region=region, start_date=start_date, end_date=end_date), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BulkRegionResponse
            schema = BulkRegionResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getBulkTat")
                print(e)

        return response
    
    async def bulkServiceability(self, extension_id=None, scheme_id=None, body="", request_headers:Dict={}):
        """Serviceability Import or Export
        :param extension_id : Unique Identifier of CP Extension : type string
        :param scheme_id : Unique identifier of a scheme : type string
        """
        payload = {}
        
        if extension_id is not None:
            payload["extension_id"] = extension_id
        if scheme_id is not None:
            payload["scheme_id"] = scheme_id

        # Parameter validation
        schema = LogisticsValidator.bulkServiceability()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import BulkRegionJobSerializer
        schema = BulkRegionJobSerializer()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/logistics/v1.0/organization/{self._conf.organizationId}/courier-partner/{extension_id}/scheme/{scheme_id}/serviceability/bulk", """{"required":[{"in":"path","name":"organization_id","description":"Unique Identifier of Organization","schema":{"type":"string"},"required":true},{"in":"path","name":"extension_id","description":"Unique Identifier of CP Extension","schema":{"type":"string"},"required":true},{"in":"path","name":"scheme_id","description":"Unique identifier of a scheme","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"organization_id","description":"Unique Identifier of Organization","schema":{"type":"string"},"required":true},{"in":"path","name":"extension_id","description":"Unique Identifier of CP Extension","schema":{"type":"string"},"required":true},{"in":"path","name":"scheme_id","description":"Unique identifier of a scheme","schema":{"type":"string"},"required":true}]}""", serverType="partner", extension_id=extension_id, scheme_id=scheme_id)
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/partner/logistics/v1.0/organization/{self._conf.organizationId}/courier-partner/{extension_id}/scheme/{scheme_id}/serviceability/bulk", extension_id=extension_id, scheme_id=scheme_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BulkRegionResponseItemData
            schema = BulkRegionResponseItemData()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for bulkServiceability")
                print(e)

        return response
    
    async def getBulkServiceability(self, extension_id=None, scheme_id=None, page_no=None, page_size=None, batch_id=None, action=None, status=None, country=None, region=None, start_date=None, end_date=None, request_headers:Dict={}):
        """Get Region Serviceability Bulk History
        :param extension_id : Unique Identifier of CP Extension : type string
        :param scheme_id : Unique identifier of a scheme : type string
        :param page_no : index of the item to start returning with : type integer
        :param page_size : determines the items to be displayed in a page : type integer
        :param batch_id : Unique identifier of bulk job : type string
        :param action : import or export bulk type : type string
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
        schema = LogisticsValidator.getBulkServiceability()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/logistics/v1.0/organization/{self._conf.organizationId}/courier-partner/{extension_id}/scheme/{scheme_id}/serviceability/bulk", """{"required":[{"in":"path","name":"organization_id","description":"Unique Identifier of Organization","schema":{"type":"string"},"required":true},{"in":"path","name":"extension_id","description":"Unique Identifier of CP Extension","schema":{"type":"string"},"required":true},{"in":"path","name":"scheme_id","description":"Unique identifier of a scheme","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"determines the items to be displayed in a page","schema":{"type":"integer","default":12,"minimum":1}},{"in":"query","name":"batch_id","description":"Unique identifier of bulk job","schema":{"type":"string"}},{"in":"query","name":"action","description":"import or export bulk type","schema":{"type":"string"}},{"in":"query","name":"status","description":"Status of the bulk actions","schema":{"type":"string"}},{"in":"query","name":"country","description":"Country for which bulk job is initiated","schema":{"type":"string"}},{"in":"query","name":"region","description":"Region for which bulk job is initiated","schema":{"type":"string"}},{"in":"query","name":"start_date","description":"Fetch job history after a particule date","example":"2023-08-01T00:00:00.000Z","schema":{"type":"string"}},{"in":"query","name":"end_date","description":"Fetch job history before a particule date","example":"2023-08-03T00:00:00.000Z","schema":{"type":"string"}}],"query":[{"in":"query","name":"page_no","description":"index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"determines the items to be displayed in a page","schema":{"type":"integer","default":12,"minimum":1}},{"in":"query","name":"batch_id","description":"Unique identifier of bulk job","schema":{"type":"string"}},{"in":"query","name":"action","description":"import or export bulk type","schema":{"type":"string"}},{"in":"query","name":"status","description":"Status of the bulk actions","schema":{"type":"string"}},{"in":"query","name":"country","description":"Country for which bulk job is initiated","schema":{"type":"string"}},{"in":"query","name":"region","description":"Region for which bulk job is initiated","schema":{"type":"string"}},{"in":"query","name":"start_date","description":"Fetch job history after a particule date","example":"2023-08-01T00:00:00.000Z","schema":{"type":"string"}},{"in":"query","name":"end_date","description":"Fetch job history before a particule date","example":"2023-08-03T00:00:00.000Z","schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"organization_id","description":"Unique Identifier of Organization","schema":{"type":"string"},"required":true},{"in":"path","name":"extension_id","description":"Unique Identifier of CP Extension","schema":{"type":"string"},"required":true},{"in":"path","name":"scheme_id","description":"Unique identifier of a scheme","schema":{"type":"string"},"required":true}]}""", serverType="partner", extension_id=extension_id, scheme_id=scheme_id, page_no=page_no, page_size=page_size, batch_id=batch_id, action=action, status=status, country=country, region=region, start_date=start_date, end_date=end_date)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, batch_id=batch_id, action=action, status=status, country=country, region=region, start_date=start_date, end_date=end_date)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/partner/logistics/v1.0/organization/{self._conf.organizationId}/courier-partner/{extension_id}/scheme/{scheme_id}/serviceability/bulk", extension_id=extension_id, scheme_id=scheme_id, page_no=page_no, page_size=page_size, batch_id=batch_id, action=action, status=status, country=country, region=region, start_date=start_date, end_date=end_date), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BulkRegionResponse
            schema = BulkRegionResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getBulkServiceability")
                print(e)

        return response
    
    async def createCourierPartnerAccount(self, company_id=None, body="", request_headers:Dict={}):
        """This API Creates a new Courier Account
        :param company_id : A `company_id` is a unique identifier for a particular sale channel. : type integer
        """
        payload = {}
        
        if company_id is not None:
            payload["company_id"] = company_id

        # Parameter validation
        schema = LogisticsValidator.createCourierPartnerAccount()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CourierAccountRequestBody
        schema = CourierAccountRequestBody()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/logistics/v1.0/organization/{self._conf.organizationId}/company/{company_id}/courier-partner/account", """{"required":[{"in":"path","name":"organization_id","description":"Unique Identifier of Organization","schema":{"type":"string"},"required":true},{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"organization_id","description":"Unique Identifier of Organization","schema":{"type":"string"},"required":true},{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}]}""", serverType="partner", company_id=company_id)
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/partner/logistics/v1.0/organization/{self._conf.organizationId}/company/{company_id}/courier-partner/account", company_id=company_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CourierAccount
            schema = CourierAccount()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createCourierPartnerAccount")
                print(e)

        return response
    
    async def getCourierPartnerAccounts(self, company_id=None, page_no=None, page_size=None, stage=None, payment_mode=None, transport_type=None, request_headers:Dict={}):
        """This API returns Courier Account of a company.
        :param company_id : A `company_id` is a unique identifier for a particular sale channel. : type integer
        :param page_no : index of the item to start returning with : type integer
        :param page_size : determines the items to be displayed in a page : type integer
        :param stage : stage of the account. enabled/disabled : type string
        :param payment_mode : Filters dp accounts based on payment mode : type string
        :param transport_type : Filters dp accounts based on transport_type : type string
        """
        payload = {}
        
        if company_id is not None:
            payload["company_id"] = company_id
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

        # Parameter validation
        schema = LogisticsValidator.getCourierPartnerAccounts()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/logistics/v1.0/organization/{self._conf.organizationId}/company/{company_id}/courier-partner/account", """{"required":[{"in":"path","name":"organization_id","description":"Unique Identifier of Organization","schema":{"type":"string"},"required":true},{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"stage","description":"stage of the account. enabled/disabled","schema":{"type":"string"}},{"in":"query","name":"payment_mode","description":"Filters dp accounts based on payment mode","schema":{"type":"string"}},{"in":"query","name":"transport_type","description":"Filters dp accounts based on transport_type","schema":{"type":"string"}}],"query":[{"in":"query","name":"page_no","description":"index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"stage","description":"stage of the account. enabled/disabled","schema":{"type":"string"}},{"in":"query","name":"payment_mode","description":"Filters dp accounts based on payment mode","schema":{"type":"string"}},{"in":"query","name":"transport_type","description":"Filters dp accounts based on transport_type","schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"organization_id","description":"Unique Identifier of Organization","schema":{"type":"string"},"required":true},{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}]}""", serverType="partner", company_id=company_id, page_no=page_no, page_size=page_size, stage=stage, payment_mode=payment_mode, transport_type=transport_type)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, stage=stage, payment_mode=payment_mode, transport_type=transport_type)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/partner/logistics/v1.0/organization/{self._conf.organizationId}/company/{company_id}/courier-partner/account", company_id=company_id, page_no=page_no, page_size=page_size, stage=stage, payment_mode=payment_mode, transport_type=transport_type), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CompanyCourierPartnerAccountListResponse
            schema = CompanyCourierPartnerAccountListResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCourierPartnerAccounts")
                print(e)

        return response
    
    async def updateCourierPartnerAccount(self, company_id=None, account_id=None, body="", request_headers:Dict={}):
        """Updates Courier Account
        :param company_id : A `company_id` is a unique identifier for a particular sale channel. : type integer
        :param account_id : Unique ID of courier account : type string
        """
        payload = {}
        
        if company_id is not None:
            payload["company_id"] = company_id
        if account_id is not None:
            payload["account_id"] = account_id

        # Parameter validation
        schema = LogisticsValidator.updateCourierPartnerAccount()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CourierAccount
        schema = CourierAccount()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/logistics/v1.0/organization/{self._conf.organizationId}/company/{company_id}/courier-partner/account/{account_id}", """{"required":[{"in":"path","name":"organization_id","description":"Unique Identifier of Organization","schema":{"type":"string"},"required":true},{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"account_id","description":"Unique ID of courier account","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"organization_id","description":"Unique Identifier of Organization","schema":{"type":"string"},"required":true},{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"account_id","description":"Unique ID of courier account","schema":{"type":"string"},"required":true}]}""", serverType="partner", company_id=company_id, account_id=account_id)
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/partner/logistics/v1.0/organization/{self._conf.organizationId}/company/{company_id}/courier-partner/account/{account_id}", company_id=company_id, account_id=account_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CourierAccountResponse
            schema = CourierAccountResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateCourierPartnerAccount")
                print(e)

        return response
    
    async def getCourierPartnerAccount(self, company_id=None, account_id=None, request_headers:Dict={}):
        """This API returns response DpAccount of a company from mongo database.
        :param company_id : A `company_id` is a unique identifier for a particular sale channel. : type integer
        :param account_id : Unique ID of courier account : type string
        """
        payload = {}
        
        if company_id is not None:
            payload["company_id"] = company_id
        if account_id is not None:
            payload["account_id"] = account_id

        # Parameter validation
        schema = LogisticsValidator.getCourierPartnerAccount()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/logistics/v1.0/organization/{self._conf.organizationId}/company/{company_id}/courier-partner/account/{account_id}", """{"required":[{"in":"path","name":"organization_id","description":"Unique Identifier of Organization","schema":{"type":"string"},"required":true},{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"account_id","description":"Unique ID of courier account","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"organization_id","description":"Unique Identifier of Organization","schema":{"type":"string"},"required":true},{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"account_id","description":"Unique ID of courier account","schema":{"type":"string"},"required":true}]}""", serverType="partner", company_id=company_id, account_id=account_id)
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/partner/logistics/v1.0/organization/{self._conf.organizationId}/company/{company_id}/courier-partner/account/{account_id}", company_id=company_id, account_id=account_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CourierAccountResponse
            schema = CourierAccountResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCourierPartnerAccount")
                print(e)

        return response
    
    async def createCourierPartnerScheme(self, body="", request_headers:Dict={}):
        """Create Scheme for courier partner extension
        """
        payload = {}
        

        # Parameter validation
        schema = LogisticsValidator.createCourierPartnerScheme()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CourierPartnerSchemeRequestModel
        schema = CourierPartnerSchemeRequestModel()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/logistics/v1.0/organization/{self._conf.organizationId}/courier-partner/scheme/", """{"required":[{"in":"path","name":"organization_id","description":"Unique Identifier of Organization","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"organization_id","description":"Unique Identifier of Organization","schema":{"type":"string"},"required":true}]}""", serverType="partner", )
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/partner/logistics/v1.0/organization/{self._conf.organizationId}/courier-partner/scheme/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CourierPartnerSchemeModel
            schema = CourierPartnerSchemeModel()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createCourierPartnerScheme")
                print(e)

        return response
    
    async def updateCourierPartnerScheme(self, scheme_id=None, body="", request_headers:Dict={}):
        """Update Scheme for courier partner extension
        :param scheme_id : Unique Identifier of Scheme : type string
        """
        payload = {}
        
        if scheme_id is not None:
            payload["scheme_id"] = scheme_id

        # Parameter validation
        schema = LogisticsValidator.updateCourierPartnerScheme()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CourierPartnerSchemeUpdateRequest
        schema = CourierPartnerSchemeUpdateRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/logistics/v1.0/organization/{self._conf.organizationId}/courier-partner/scheme/{scheme_id}", """{"required":[{"in":"path","name":"organization_id","description":"Unique Identifier of Organization","schema":{"type":"string"},"required":true},{"in":"path","name":"scheme_id","description":"Unique Identifier of Scheme","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"organization_id","description":"Unique Identifier of Organization","schema":{"type":"string"},"required":true},{"in":"path","name":"scheme_id","description":"Unique Identifier of Scheme","schema":{"type":"string"},"required":true}]}""", serverType="partner", scheme_id=scheme_id)
        query_string = await create_query_string()

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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/partner/logistics/v1.0/organization/{self._conf.organizationId}/courier-partner/scheme/{scheme_id}", scheme_id=scheme_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CourierPartnerSchemeUpdateRequest
            schema = CourierPartnerSchemeUpdateRequest()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateCourierPartnerScheme")
                print(e)

        return response
    
    async def getCountries(self, onboarding=None, page_no=None, page_size=None, q=None, request_headers:Dict={}):
        """Retrieve of all countries.
        :param onboarding : Only fetch countries which allowed for onboard on Platform. : type boolean
        :param page_no : page number. : type integer
        :param page_size : page size. : type integer
        :param q : search. : type string
        """
        payload = {}
        
        if onboarding is not None:
            payload["onboarding"] = onboarding
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if q is not None:
            payload["q"] = q

        # Parameter validation
        schema = LogisticsValidator.getCountries()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/partner/logistics/v2.0/organization/{self._conf.organizationId}/countries", """{"required":[{"in":"path","name":"organization_id","description":"Unique Identifier of Organization","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"onboarding","description":"Only fetch countries which allowed for onboard on Platform.","schema":{"type":"boolean"},"required":false},{"in":"query","name":"page_no","description":"page number.","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"page size.","schema":{"type":"integer","default":12,"maximum":48},"required":false},{"in":"query","name":"q","description":"search.","schema":{"type":"string"},"required":false}],"query":[{"in":"query","name":"onboarding","description":"Only fetch countries which allowed for onboard on Platform.","schema":{"type":"boolean"},"required":false},{"in":"query","name":"page_no","description":"page number.","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"page size.","schema":{"type":"integer","default":12,"maximum":48},"required":false},{"in":"query","name":"q","description":"search.","schema":{"type":"string"},"required":false}],"headers":[],"path":[{"in":"path","name":"organization_id","description":"Unique Identifier of Organization","schema":{"type":"string"},"required":true}]}""", serverType="partner", onboarding=onboarding, page_no=page_no, page_size=page_size, q=q)
        query_string = await create_query_string(onboarding=onboarding, page_no=page_no, page_size=page_size, q=q)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/partner/logistics/v2.0/organization/{self._conf.organizationId}/countries", onboarding=onboarding, page_no=page_no, page_size=page_size, q=q), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetCountries
            schema = GetCountries()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCountries")
                print(e)

        return response
    