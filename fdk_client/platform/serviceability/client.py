"""Serviceability Platform Client"""
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..PlatformConfig import PlatformConfig

from .validator import ServiceabilityValidator

class Serviceability:
    def __init__(self, config: PlatformConfig):
        self._conf = config

    
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
        schema = ServiceabilityValidator.bulkServiceability()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import BulkRegionJobSerializer
        schema = BulkRegionJobSerializer()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/{extension_id}/scheme/{scheme_id}/serviceability/bulk", """{"required":[{"in":"path","name":"company_id","description":"Unique Identifier of Company","schema":{"type":"integer"},"required":true},{"in":"path","name":"extension_id","description":"Unique Identifier of CP Extension","schema":{"type":"string"},"required":true},{"in":"path","name":"scheme_id","description":"Unique identifier of a scheme","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique Identifier of Company","schema":{"type":"integer"},"required":true},{"in":"path","name":"extension_id","description":"Unique Identifier of CP Extension","schema":{"type":"string"},"required":true},{"in":"path","name":"scheme_id","description":"Unique identifier of a scheme","schema":{"type":"string"},"required":true}]}""", serverType="platform", extension_id=extension_id, scheme_id=scheme_id)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/{extension_id}/scheme/{scheme_id}/serviceability/bulk", extension_id=extension_id, scheme_id=scheme_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

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
        schema = ServiceabilityValidator.getBulkServiceability()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/{extension_id}/scheme/{scheme_id}/serviceability/bulk", """{"required":[{"in":"path","name":"company_id","description":"Unique Identifier of Company","schema":{"type":"integer"},"required":true},{"in":"path","name":"extension_id","description":"Unique Identifier of CP Extension","schema":{"type":"string"},"required":true},{"in":"path","name":"scheme_id","description":"Unique identifier of a scheme","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"determines the items to be displayed in a page","schema":{"type":"integer","default":12,"minimum":1}},{"in":"query","name":"batch_id","description":"Unique identifier of bulk job","schema":{"type":"string"}},{"in":"query","name":"action","description":"import or export bulk type","schema":{"type":"string"}},{"in":"query","name":"status","description":"Status of the bulk actions","schema":{"type":"string"}},{"in":"query","name":"country","description":"Country for which bulk job is initiated","schema":{"type":"string"}},{"in":"query","name":"region","description":"Region for which bulk job is initiated","schema":{"type":"string"}},{"in":"query","name":"start_date","description":"Fetch job history after a particule date","schema":{"type":"string"}},{"in":"query","name":"end_date","description":"Fetch job history before a particule date","schema":{"type":"string"}}],"query":[{"in":"query","name":"page_no","description":"index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"determines the items to be displayed in a page","schema":{"type":"integer","default":12,"minimum":1}},{"in":"query","name":"batch_id","description":"Unique identifier of bulk job","schema":{"type":"string"}},{"in":"query","name":"action","description":"import or export bulk type","schema":{"type":"string"}},{"in":"query","name":"status","description":"Status of the bulk actions","schema":{"type":"string"}},{"in":"query","name":"country","description":"Country for which bulk job is initiated","schema":{"type":"string"}},{"in":"query","name":"region","description":"Region for which bulk job is initiated","schema":{"type":"string"}},{"in":"query","name":"start_date","description":"Fetch job history after a particule date","schema":{"type":"string"}},{"in":"query","name":"end_date","description":"Fetch job history before a particule date","schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique Identifier of Company","schema":{"type":"integer"},"required":true},{"in":"path","name":"extension_id","description":"Unique Identifier of CP Extension","schema":{"type":"string"},"required":true},{"in":"path","name":"scheme_id","description":"Unique identifier of a scheme","schema":{"type":"string"},"required":true}]}""", serverType="platform", extension_id=extension_id, scheme_id=scheme_id, page_no=page_no, page_size=page_size, batch_id=batch_id, action=action, status=status, country=country, region=region, start_date=start_date, end_date=end_date)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/{extension_id}/scheme/{scheme_id}/serviceability/bulk", extension_id=extension_id, scheme_id=scheme_id, page_no=page_no, page_size=page_size, batch_id=batch_id, action=action, status=status, country=country, region=region, start_date=start_date, end_date=end_date), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BulkRegionResponse
            schema = BulkRegionResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getBulkServiceability")
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
        from .models import BulkRegionServiceabilityTatRequest
        schema = BulkRegionServiceabilityTatRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/localities/bulk-sample", """{"required":[{"in":"path","name":"company_id","description":"Unique Identifier of Company","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique Identifier of Company","schema":{"type":"integer"},"required":true}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/localities/bulk-sample", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

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
        schema = ServiceabilityValidator.getSampleFileServiceabilityStatus()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/localities/bulk-sample", """{"required":[{"in":"path","name":"company_id","description":"Unique Identifier of Company","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"determines the items to be displayed in a page","schema":{"type":"integer","default":12,"minimum":1}},{"in":"query","name":"batch_id","description":"Batch id of the execution","schema":{"type":"string"}}],"query":[{"in":"query","name":"page_no","description":"index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"determines the items to be displayed in a page","schema":{"type":"integer","default":12,"minimum":1}},{"in":"query","name":"batch_id","description":"Batch id of the execution","schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique Identifier of Company","schema":{"type":"integer"},"required":true}]}""", serverType="platform", page_no=page_no, page_size=page_size, batch_id=batch_id)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, batch_id=batch_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/localities/bulk-sample", page_no=page_no, page_size=page_size, batch_id=batch_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

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
        schema = ServiceabilityValidator.bulkTat()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import BulkRegionJobSerializer
        schema = BulkRegionJobSerializer()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/{extension_id}/scheme/{scheme_id}/tat", """{"required":[{"in":"path","name":"company_id","description":"Unique Identifier of Company","schema":{"type":"integer"},"required":true},{"in":"path","name":"extension_id","description":"Unique Identifier of CP Extension","schema":{"type":"string"},"required":true},{"in":"path","name":"scheme_id","description":"Unique identifier of a scheme","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique Identifier of Company","schema":{"type":"integer"},"required":true},{"in":"path","name":"extension_id","description":"Unique Identifier of CP Extension","schema":{"type":"string"},"required":true},{"in":"path","name":"scheme_id","description":"Unique identifier of a scheme","schema":{"type":"string"},"required":true}]}""", serverType="platform", extension_id=extension_id, scheme_id=scheme_id)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/{extension_id}/scheme/{scheme_id}/tat", extension_id=extension_id, scheme_id=scheme_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

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
        schema = ServiceabilityValidator.getBulkTat()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/{extension_id}/scheme/{scheme_id}/tat", """{"required":[{"in":"path","name":"company_id","description":"Unique Identifier of Company","schema":{"type":"integer"},"required":true},{"in":"path","name":"extension_id","description":"Unique Identifier of CP Extension","schema":{"type":"string"},"required":true},{"in":"path","name":"scheme_id","description":"Unique identifier of a scheme","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"determines the items to be displayed in a page","schema":{"type":"integer","default":12,"minimum":1}},{"in":"query","name":"batch_id","description":"Unique identifier of bulk job","schema":{"type":"string"}},{"in":"query","name":"action","description":"import or export bulk type","schema":{"type":"string"}},{"in":"query","name":"status","description":"Status of the bulk actions","schema":{"type":"string"}},{"in":"query","name":"country","description":"Country for which bulk job is initiated","schema":{"type":"string"}},{"in":"query","name":"region","description":"Region for which bulk job is initiated","schema":{"type":"string"}},{"in":"query","name":"start_date","description":"Fetch job history after a particule date","schema":{"type":"string"}},{"in":"query","name":"end_date","description":"Fetch job history before a particule date","schema":{"type":"string"}}],"query":[{"in":"query","name":"page_no","description":"index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"determines the items to be displayed in a page","schema":{"type":"integer","default":12,"minimum":1}},{"in":"query","name":"batch_id","description":"Unique identifier of bulk job","schema":{"type":"string"}},{"in":"query","name":"action","description":"import or export bulk type","schema":{"type":"string"}},{"in":"query","name":"status","description":"Status of the bulk actions","schema":{"type":"string"}},{"in":"query","name":"country","description":"Country for which bulk job is initiated","schema":{"type":"string"}},{"in":"query","name":"region","description":"Region for which bulk job is initiated","schema":{"type":"string"}},{"in":"query","name":"start_date","description":"Fetch job history after a particule date","schema":{"type":"string"}},{"in":"query","name":"end_date","description":"Fetch job history before a particule date","schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique Identifier of Company","schema":{"type":"integer"},"required":true},{"in":"path","name":"extension_id","description":"Unique Identifier of CP Extension","schema":{"type":"string"},"required":true},{"in":"path","name":"scheme_id","description":"Unique identifier of a scheme","schema":{"type":"string"},"required":true}]}""", serverType="platform", extension_id=extension_id, scheme_id=scheme_id, page_no=page_no, page_size=page_size, batch_id=batch_id, action=action, status=status, country=country, region=region, start_date=start_date, end_date=end_date)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/{extension_id}/scheme/{scheme_id}/tat", extension_id=extension_id, scheme_id=scheme_id, page_no=page_no, page_size=page_size, batch_id=batch_id, action=action, status=status, country=country, region=region, start_date=start_date, end_date=end_date), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import BulkRegionResponse
            schema = BulkRegionResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getBulkTat")
                print(e)

        return response
    
    async def updateCompanySelfShip(self, body="", request_headers:Dict={}):
        """Updates Self Ship at company level
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.updateCompanySelfShip()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CompanySelfShip
        schema = CompanySelfShip()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/selfship", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}]}""", serverType="platform", )
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
            from .models import CompanySelfShip
            schema = CompanySelfShip()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateCompanySelfShip")
                print(e)

        return response
    
    async def getCompanySelfShip(self, request_headers:Dict={}):
        """Updates Self Ship at company level
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.getCompanySelfShip()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/selfship", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}]}""", serverType="platform", )
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
            from .models import CompanySelfShip
            schema = CompanySelfShip()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCompanySelfShip")
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
        from .models import CourierPartnerSchemeModel
        schema = CourierPartnerSchemeModel()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/scheme", """{"required":[{"in":"path","name":"company_id","description":"Unique identifier for the company","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique identifier for the company","schema":{"type":"integer"},"required":true}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/scheme", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

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
        schema = ServiceabilityValidator.updateCourierPartnerScheme()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CourierPartnerSchemeUpdateRequest
        schema = CourierPartnerSchemeUpdateRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/scheme/{scheme_id}", """{"required":[{"in":"path","name":"company_id","description":"Unique Identifier of Organization","schema":{"type":"integer"},"required":true},{"in":"path","name":"scheme_id","description":"Unique Identifier of Scheme","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Unique Identifier of Organization","schema":{"type":"integer"},"required":true},{"in":"path","name":"scheme_id","description":"Unique Identifier of Scheme","schema":{"type":"string"},"required":true}]}""", serverType="platform", scheme_id=scheme_id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/scheme/{scheme_id}", scheme_id=scheme_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CourierPartnerSchemeUpdateRequest
            schema = CourierPartnerSchemeUpdateRequest()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateCourierPartnerScheme")
                print(e)

        return response
    
    async def createCourierPartnerAccount(self, body="", request_headers:Dict={}):
        """Retrieves a list of courier partner accounts.
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.createCourierPartnerAccount()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CourierAccount
        schema = CourierAccount()
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
            from .models import CourierAccount
            schema = CourierAccount()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createCourierPartnerAccount")
                print(e)

        return response
    
    async def getCourierPartnerAccounts(self, page_no=None, page_size=None, stage=None, payment_mode=None, transport_type=None, account_ids=None, self_ship=None, own_account=None, q=None, request_headers:Dict={}):
        """Retrieves a list of courier partner accounts.
        :param page_no : index of the item to start returning with : type integer
        :param page_size : determines the items to be displayed in a page : type integer
        :param stage : stage of the account. enabled/disabled : type string
        :param payment_mode : Filters dp accounts based on payment mode : type string
        :param transport_type : Filters dp accounts based on transport_type : type string
        :param account_ids : Filters dp accounts based on their ids : type array
        :param self_ship : To filter self ship/non self ship dp accounts : type boolean
        :param own_account : Filters seller owned or admin owned dp accounts : type boolean
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/account", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"stage","description":"stage of the account. enabled/disabled","schema":{"type":"string"}},{"in":"query","name":"payment_mode","description":"Filters dp accounts based on payment mode","schema":{"type":"string"}},{"in":"query","name":"transport_type","description":"Filters dp accounts based on transport_type","schema":{"type":"string"}},{"in":"query","name":"account_ids","description":"Filters dp accounts based on their ids","schema":{"type":"array","items":{"type":"string"}}},{"in":"query","name":"self_ship","description":"To filter self ship/non self ship dp accounts","schema":{"type":"boolean"}},{"in":"query","name":"own_account","description":"Filters seller owned or admin owned dp accounts","schema":{"type":"boolean"}},{"in":"query","name":"q","description":"Filters dp accounts based on case sensitive partial account name","schema":{"type":"string"}}],"query":[{"in":"query","name":"page_no","description":"index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"stage","description":"stage of the account. enabled/disabled","schema":{"type":"string"}},{"in":"query","name":"payment_mode","description":"Filters dp accounts based on payment mode","schema":{"type":"string"}},{"in":"query","name":"transport_type","description":"Filters dp accounts based on transport_type","schema":{"type":"string"}},{"in":"query","name":"account_ids","description":"Filters dp accounts based on their ids","schema":{"type":"array","items":{"type":"string"}}},{"in":"query","name":"self_ship","description":"To filter self ship/non self ship dp accounts","schema":{"type":"boolean"}},{"in":"query","name":"own_account","description":"Filters seller owned or admin owned dp accounts","schema":{"type":"boolean"}},{"in":"query","name":"q","description":"Filters dp accounts based on case sensitive partial account name","schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}]}""", serverType="platform", page_no=page_no, page_size=page_size, stage=stage, payment_mode=payment_mode, transport_type=transport_type, account_ids=account_ids, self_ship=self_ship, own_account=own_account, q=q)
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
            from .models import CompanyCourierPartnerAccountListResponse
            schema = CompanyCourierPartnerAccountListResponse()
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
        from .models import CourierAccount
        schema = CourierAccount()
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
            from .models import CourierAccount
            schema = CourierAccount()
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
            from .models import CourierAccountResponse
            schema = CourierAccountResponse()
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
        from .models import CompanyConfigurationShema
        schema = CompanyConfigurationShema()
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
    
    async def createPackageMaterial(self, page_no=None, body="", request_headers:Dict={}):
        """Creates a packaging material
        :param page_no : index of the item to start returning with : type integer
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/packaging-materials", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller.","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"index of the item to start returning with","schema":{"type":"integer"},"required":false}],"query":[{"in":"query","name":"page_no","description":"index of the item to start returning with","schema":{"type":"integer"},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular seller.","schema":{"type":"integer"},"required":true}]}""", serverType="platform", page_no=page_no)
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
            from .models import PackageMaterialResponse
            schema = PackageMaterialResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createPackageMaterial")
                print(e)

        return response
    
    async def getPackageMaterialList(self, page_no=None, page_size=None, q=None, size=None, package_type=None, request_headers:Dict={}):
        """Retrieves a list of packaging materials
        :param page_no : index of the item to start returning with : type integer
        :param page_size : determines the items to be displayed in a page : type integer
        :param q : perform regex search on items matching name for given value : type string
        :param size : filters items based on given size : type string
        :param package_type : filters items based on given package_type : type string
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/packaging-materials", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"index of the item to start returning with","schema":{"type":"integer","default":1}},{"in":"query","name":"page_size","description":"determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"q","description":"perform regex search on items matching name for given value","schema":{"type":"string"}},{"in":"query","name":"size","description":"filters items based on given size","schema":{"type":"string"}},{"in":"query","name":"package_type","description":"filters items based on given package_type","schema":{"type":"string"}}],"query":[{"in":"query","name":"page_no","description":"index of the item to start returning with","schema":{"type":"integer","default":1}},{"in":"query","name":"page_size","description":"determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"q","description":"perform regex search on items matching name for given value","schema":{"type":"string"}},{"in":"query","name":"size","description":"filters items based on given size","schema":{"type":"string"}},{"in":"query","name":"package_type","description":"filters items based on given package_type","schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}]}""", serverType="platform", page_no=page_no, page_size=page_size, q=q, size=size, package_type=package_type)
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
            from .models import PackageMaterialList
            schema = PackageMaterialList()
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
        from .models import PackageRuleRequest
        schema = PackageRuleRequest()
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
    
    async def getPackageMaterialRuleDetails(self, rule_id=None, page_no=None, page_size=None, is_active=None, request_headers:Dict={}):
        """This API returns details of package materials rule.
        :param rule_id : A `package_material_rule_id` is a unique identifier for a Package Material Rule : type string
        :param page_no : index of the item to start returning with : type integer
        :param page_size : determines the items to be displayed in a page : type integer
        :param is_active : filters items based on given is_active : type string
        """
        payload = {}
        
        if rule_id is not None:
            payload["rule_id"] = rule_id
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if is_active is not None:
            payload["is_active"] = is_active

        # Parameter validation
        schema = ServiceabilityValidator.getPackageMaterialRuleDetails()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/packaging-material/rules/{rule_id}/details", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"rule_id","description":"A `package_material_rule_id` is a unique identifier for a Package Material Rule","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"index of the item to start returning with","schema":{"type":"integer","default":1}},{"in":"query","name":"page_size","description":"determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"is_active","description":"filters items based on given is_active","schema":{"type":"string"}}],"query":[{"in":"query","name":"page_no","description":"index of the item to start returning with","schema":{"type":"integer","default":1}},{"in":"query","name":"page_size","description":"determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"is_active","description":"filters items based on given is_active","schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular company.","schema":{"type":"integer"},"required":true},{"in":"path","name":"rule_id","description":"A `package_material_rule_id` is a unique identifier for a Package Material Rule","schema":{"type":"string"},"required":true}]}""", serverType="platform", rule_id=rule_id, page_no=page_no, page_size=page_size, is_active=is_active)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, is_active=is_active)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/packaging-material/rules/{rule_id}/details", rule_id=rule_id, page_no=page_no, page_size=page_size, is_active=is_active), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PackageRuleResult
            schema = PackageRuleResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPackageMaterialRuleDetails")
                print(e)

        return response
    
    async def getListPackageMaterialRuleDetails(self, page_no=None, page_size=None, is_active=None, request_headers:Dict={}):
        """This API returns response of Package Materials Rules from mongo database.
        :param page_no : index of the item to start returning with : type integer
        :param page_size : determines the items to be displayed in a page : type integer
        :param is_active : filters items based on given is_active : type string
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if is_active is not None:
            payload["is_active"] = is_active

        # Parameter validation
        schema = ServiceabilityValidator.getListPackageMaterialRuleDetails()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/packaging-material/rules/details", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"index of the item to start returning with","schema":{"type":"integer","default":1}},{"in":"query","name":"page_size","description":"determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"is_active","description":"filters items based on given is_active","schema":{"type":"string"}}],"query":[{"in":"query","name":"page_no","description":"index of the item to start returning with","schema":{"type":"integer","default":1}},{"in":"query","name":"page_size","description":"determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"is_active","description":"filters items based on given is_active","schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}]}""", serverType="platform", page_no=page_no, page_size=page_size, is_active=is_active)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, is_active=is_active)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/packaging-material/rules/details", page_no=page_no, page_size=page_size, is_active=is_active), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PackageMaterialRuleList
            schema = PackageMaterialRuleList()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getListPackageMaterialRuleDetails")
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
        from .models import PackageRuleRequest
        schema = PackageRuleRequest()
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
            from .models import PackageMaterialResponse
            schema = PackageMaterialResponse()
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
            from .models import PackageMaterialResponse
            schema = PackageMaterialResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPackageMaterials")
                print(e)

        return response
    
    async def getInstalledCourierPartnerExtensions(self, page_no=None, page_size=None, is_installed=None, request_headers:Dict={}):
        """This API returns response of Package Materials Rules from mongo database.
        :param page_no : index of the item to start returning with : type integer
        :param page_size : determines the items to be displayed in a page : type integer
        :param is_installed : filter to get installed extensions only : type string
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier-partner/list", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"is_installed","description":"filter to get installed extensions only","schema":{"type":"string","enum":[true,false]}}],"query":[{"in":"query","name":"page_no","description":"index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"is_installed","description":"filter to get installed extensions only","schema":{"type":"string","enum":[true,false]}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}]}""", serverType="platform", page_no=page_no, page_size=page_size, is_installed=is_installed)
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
    
    async def getLocalitiesByPrefix(self, page_no=None, page_size=None, q=None, request_headers:Dict={}):
        """Get localities that start with a specified prefix.
        :param page_no : Starting index of the items. : type integer
        :param page_size : Number of items per page. : type integer
        :param q : Localities starting with the specified prefix. : type string
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if q is not None:
            payload["q"] = q

        # Parameter validation
        schema = ServiceabilityValidator.getLocalitiesByPrefix()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/localities", """{"required":[{"in":"path","name":"company_id","description":"The unique identifier of the company.","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"page_no","description":"Starting index of the items.","schema":{"type":"integer","default":1,"minimum":1},"required":false},{"in":"query","name":"page_size","description":"Number of items per page.","required":false,"schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"q","description":"Localities starting with the specified prefix.","schema":{"type":"string"},"required":false}],"query":[{"in":"query","name":"page_no","description":"Starting index of the items.","schema":{"type":"integer","default":1,"minimum":1},"required":false},{"in":"query","name":"page_size","description":"Number of items per page.","required":false,"schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"q","description":"Localities starting with the specified prefix.","schema":{"type":"string"},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"The unique identifier of the company.","schema":{"type":"integer"},"required":true}]}""", serverType="platform", page_no=page_no, page_size=page_size, q=q)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, q=q)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/localities", page_no=page_no, page_size=page_size, q=q), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetLocalities
            schema = GetLocalities()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getLocalitiesByPrefix")
                print(e)

        return response
    
    async def getLocality(self, locality_type=None, locality_value=None, country=None, state=None, city=None, request_headers:Dict={}):
        """Get Locality data
        :param locality_type : A `locality_type` contains value geographical division. : type string
        :param locality_value : A `locality_value` contains a specific name of the locality. : type string
        :param country : A `country` contains a specific value of the country iso2 code. : type string
        :param state : A `state` contains a specific value of the state, province. : type string
        :param city : A `city` contains a specific value of the city. : type string
        """
        payload = {}
        
        if locality_type is not None:
            payload["locality_type"] = locality_type
        if locality_value is not None:
            payload["locality_value"] = locality_value
        if country is not None:
            payload["country"] = country
        if state is not None:
            payload["state"] = state
        if city is not None:
            payload["city"] = city

        # Parameter validation
        schema = ServiceabilityValidator.getLocality()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/localities/{locality_type}/{locality_value}", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"locality_type","description":"A `locality_type` contains value geographical division.","schema":{"type":"string","enum":["pincode","sector"]},"required":true},{"in":"path","name":"locality_value","description":"A `locality_value` contains a specific name of the locality.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"country","description":"A `country` contains a specific value of the country iso2 code.","schema":{"type":"string"},"required":false},{"in":"query","name":"state","description":"A `state` contains a specific value of the state, province.","schema":{"type":"string"},"required":false},{"in":"query","name":"city","description":"A `city` contains a specific value of the city.","schema":{"type":"string"},"required":false}],"query":[{"in":"query","name":"country","description":"A `country` contains a specific value of the country iso2 code.","schema":{"type":"string"},"required":false},{"in":"query","name":"state","description":"A `state` contains a specific value of the state, province.","schema":{"type":"string"},"required":false},{"in":"query","name":"city","description":"A `city` contains a specific value of the city.","schema":{"type":"string"},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"locality_type","description":"A `locality_type` contains value geographical division.","schema":{"type":"string","enum":["pincode","sector"]},"required":true},{"in":"path","name":"locality_value","description":"A `locality_value` contains a specific name of the locality.","schema":{"type":"string"},"required":true}]}""", serverType="platform", locality_type=locality_type, locality_value=locality_value, country=country, state=state, city=city)
        query_string = await create_query_string(country=country, state=state, city=city)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/localities/{locality_type}/{locality_value}", locality_type=locality_type, locality_value=locality_value, country=country, state=state, city=city), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetLocality
            schema = GetLocality()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getLocality")
                print(e)

        return response
    
    async def getLocalities(self, locality_type=None, country=None, state=None, city=None, page_no=None, page_size=None, q=None, name=None, request_headers:Dict={}):
        """Get Localities data.
        :param locality_type : A `locality_type` contains unique geographical division. : type string
        :param country : A `country` contains a specific value of the country iso2 code. : type string
        :param state : A `state` contains a specific value of the state, province. : type string
        :param city : A `city` contains a specific value of the city. : type string
        :param page_no : page number. : type integer
        :param page_size : page size. : type integer
        :param q : search. : type string
        :param name : Search for localities. Either provide a full name or a search term. : type string
        """
        payload = {}
        
        if locality_type is not None:
            payload["locality_type"] = locality_type
        if country is not None:
            payload["country"] = country
        if state is not None:
            payload["state"] = state
        if city is not None:
            payload["city"] = city
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if q is not None:
            payload["q"] = q
        if name is not None:
            payload["name"] = name

        # Parameter validation
        schema = ServiceabilityValidator.getLocalities()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/localities/{locality_type}", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"locality_type","description":"A `locality_type` contains unique geographical division.","schema":{"type":"string","enum":["state","city","pincode","sector"]},"required":true}],"optional":[{"in":"query","name":"country","description":"A `country` contains a specific value of the country iso2 code.","schema":{"type":"string"},"required":false},{"in":"query","name":"state","description":"A `state` contains a specific value of the state, province.","schema":{"type":"string"},"required":false},{"in":"query","name":"city","description":"A `city` contains a specific value of the city.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_no","description":"page number.","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"page size.","schema":{"type":"integer","default":12,"maximum":1000},"required":false},{"in":"query","name":"q","description":"search.","schema":{"type":"string"},"required":false},{"in":"query","name":"name","description":"Search for localities. Either provide a full name or a search term.","schema":{"type":"string"}}],"query":[{"in":"query","name":"country","description":"A `country` contains a specific value of the country iso2 code.","schema":{"type":"string"},"required":false},{"in":"query","name":"state","description":"A `state` contains a specific value of the state, province.","schema":{"type":"string"},"required":false},{"in":"query","name":"city","description":"A `city` contains a specific value of the city.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_no","description":"page number.","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"page size.","schema":{"type":"integer","default":12,"maximum":1000},"required":false},{"in":"query","name":"q","description":"search.","schema":{"type":"string"},"required":false},{"in":"query","name":"name","description":"Search for localities. Either provide a full name or a search term.","schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"locality_type","description":"A `locality_type` contains unique geographical division.","schema":{"type":"string","enum":["state","city","pincode","sector"]},"required":true}]}""", serverType="platform", locality_type=locality_type, country=country, state=state, city=city, page_no=page_no, page_size=page_size, q=q, name=name)
        query_string = await create_query_string(country=country, state=state, city=city, page_no=page_no, page_size=page_size, q=q, name=name)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/localities/{locality_type}", locality_type=locality_type, country=country, state=state, city=city, page_no=page_no, page_size=page_size, q=q, name=name), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetLocalities
            schema = GetLocalities()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getLocalities")
                print(e)

        return response
    
    async def getCountry(self, country_iso_code=None, request_headers:Dict={}):
        """Retrieve data for a single country and address format.
        :param country_iso_code : The `country_iso_code` is ISO-2 (alpha-2) code for the country. : type string
        """
        payload = {}
        
        if country_iso_code is not None:
            payload["country_iso_code"] = country_iso_code

        # Parameter validation
        schema = ServiceabilityValidator.getCountry()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/countries/{country_iso_code}", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"country_iso_code","description":"The `country_iso_code` is ISO-2 (alpha-2) code for the country.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"country_iso_code","description":"The `country_iso_code` is ISO-2 (alpha-2) code for the country.","schema":{"type":"string"},"required":true}]}""", serverType="platform", country_iso_code=country_iso_code)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/countries/{country_iso_code}", country_iso_code=country_iso_code), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetCountry
            schema = GetCountry()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCountry")
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v2.0/company/{self._conf.companyId}/countries", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"onboard","description":"Only fetch countries which allowed for onboard on Platform.","schema":{"type":"boolean"},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results. Default value is 1.","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"The number of items to retrieve in each page. Default value is 12","schema":{"type":"integer","default":12,"maximum":300},"required":false},{"in":"query","name":"q","description":"The search string to search in the list of countries by name.","schema":{"type":"string"},"required":false},{"in":"query","name":"hierarchy","description":"The search filter to filter countries based on their available hierarchy.","schema":{"type":"string"},"required":false}],"query":[{"in":"query","name":"onboard","description":"Only fetch countries which allowed for onboard on Platform.","schema":{"type":"boolean"},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results. Default value is 1.","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"The number of items to retrieve in each page. Default value is 12","schema":{"type":"integer","default":12,"maximum":300},"required":false},{"in":"query","name":"q","description":"The search string to search in the list of countries by name.","schema":{"type":"string"},"required":false},{"in":"query","name":"hierarchy","description":"The search filter to filter countries based on their available hierarchy.","schema":{"type":"string"},"required":false}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}]}""", serverType="platform", onboard=onboard, page_no=page_no, page_size=page_size, q=q, hierarchy=hierarchy)
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
    
    async def validateAddress(self, country_iso_code=None, template_name=None, body="", request_headers:Dict={}):
        """Validate given address wrt template
        :param country_iso_code : The ISO code of the country. : type string
        :param template_name : The type of address form. : type string
        """
        payload = {}
        
        if country_iso_code is not None:
            payload["country_iso_code"] = country_iso_code
        if template_name is not None:
            payload["template_name"] = template_name

        # Parameter validation
        schema = ServiceabilityValidator.validateAddress()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ValidateAddressRequest
        schema = ValidateAddressRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/country/{country_iso_code}/address/templates/{template_name}/validate", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"country_iso_code","description":"The ISO code of the country.","schema":{"type":"string"},"required":true},{"in":"path","name":"template_name","description":"The type of address form.","schema":{"type":"string","enum":["checkout_form","store_os_form","default_display"]},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"country_iso_code","description":"The ISO code of the country.","schema":{"type":"string"},"required":true},{"in":"path","name":"template_name","description":"The type of address form.","schema":{"type":"string","enum":["checkout_form","store_os_form","default_display"]},"required":true}]}""", serverType="platform", country_iso_code=country_iso_code, template_name=template_name)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/country/{country_iso_code}/address/templates/{template_name}/validate", country_iso_code=country_iso_code, template_name=template_name), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ValidateAddressRequest
            schema = ValidateAddressRequest()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for validateAddress")
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
            from .models import OptimalLocationsResponse
            schema = OptimalLocationsResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getOptimalLocations")
                print(e)

        return response
    