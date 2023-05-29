

"""Communication Platform Client"""

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .applicationValidator import CommunicationValidator

class Communication:
    def __init__(self, config, applicationId):
        self._conf = config
        self.applicationId = applicationId

    
    async def getCampaigns(self, page_no=None, page_size=None, sort=None):
        """Get campaigns
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        :param sort : To sort based on created_at : type object
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if sort:
            payload["sort"] = sort
        

        # Parameter validation
        schema = CommunicationValidator.getCampaigns()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/campaigns/campaigns", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}]}""", page_no=page_no, page_size=page_size, sort=sort)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, sort=sort)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/campaigns/campaigns", page_no=page_no, page_size=page_size, sort=sort), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        from .models import Campaigns
        schema = Campaigns()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getCampaigns")
            print(e)

        

        return response
    
    async def createCampaign(self, body=""):
        """Create campaign
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.createCampaign()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CampaignReq
        schema = CampaignReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/campaigns/campaigns", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/campaigns/campaigns", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        from .models import Campaign
        schema = Campaign()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for createCampaign")
            print(e)

        

        return response
    
    async def getCampaignById(self, id=None):
        """Get campaign by id
        :param id : Campaign id : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CommunicationValidator.getCampaignById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/campaigns/campaigns/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Campaign id","required":true,"schema":{"type":"string","example":"6009a1ea1f6a61d88e80a867"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Campaign id","required":true,"schema":{"type":"string","example":"6009a1ea1f6a61d88e80a867"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/campaigns/campaigns/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        from .models import Campaign
        schema = Campaign()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getCampaignById")
            print(e)

        

        return response
    
    async def updateCampaignById(self, id=None, body=""):
        """Update campaign by id
        :param id : Campaign id : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CommunicationValidator.updateCampaignById()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CampaignReq
        schema = CampaignReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/campaigns/campaigns/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Campaign id","required":true,"schema":{"type":"string","example":"6009a1ea1f6a61d88e80a867"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Campaign id","required":true,"schema":{"type":"string","example":"6009a1ea1f6a61d88e80a867"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/campaigns/campaigns/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        from .models import Campaign
        schema = Campaign()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for updateCampaignById")
            print(e)

        

        return response
    
    async def getStatsOfCampaignById(self, id=None):
        """Get stats of campaign by id
        :param id : Campaign id : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CommunicationValidator.getStatsOfCampaignById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/campaigns/get-stats/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Campaign id","required":true,"schema":{"type":"string","example":"6009a1ea1f6a61d88e80a867"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Campaign id","required":true,"schema":{"type":"string","example":"6009a1ea1f6a61d88e80a867"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/campaigns/get-stats/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        from .models import GetStats
        schema = GetStats()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getStatsOfCampaignById")
            print(e)

        

        return response
    
    async def getAudiences(self, page_no=None, page_size=None, sort=None):
        """Get audiences
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        :param sort : To sort based on created_at : type object
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if sort:
            payload["sort"] = sort
        

        # Parameter validation
        schema = CommunicationValidator.getAudiences()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/datasources", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}]}""", page_no=page_no, page_size=page_size, sort=sort)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, sort=sort)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/datasources", page_no=page_no, page_size=page_size, sort=sort), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        from .models import Audiences
        schema = Audiences()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getAudiences")
            print(e)

        

        return response
    
    async def createAudience(self, body=""):
        """Create audience
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.createAudience()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AudienceReq
        schema = AudienceReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/datasources", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/datasources", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        from .models import Audience
        schema = Audience()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for createAudience")
            print(e)

        

        return response
    
    async def getBigqueryHeaders(self, body=""):
        """Get bigquery headers
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.getBigqueryHeaders()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import BigqueryHeadersReq
        schema = BigqueryHeadersReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/bigquery-headers", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/bigquery-headers", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        from .models import BigqueryHeadersRes
        schema = BigqueryHeadersRes()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getBigqueryHeaders")
            print(e)

        

        return response
    
    async def getAudienceById(self, id=None):
        """Get audience by id
        :param id : Audience id : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CommunicationValidator.getAudienceById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/datasources/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Audience id","required":true,"schema":{"type":"string","example":"5fb6675c09fd901023917a5f"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Audience id","required":true,"schema":{"type":"string","example":"5fb6675c09fd901023917a5f"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/datasources/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        from .models import Audience
        schema = Audience()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getAudienceById")
            print(e)

        

        return response
    
    async def updateAudienceById(self, id=None, body=""):
        """Update audience by id
        :param id : Audience id : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CommunicationValidator.updateAudienceById()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AudienceReq
        schema = AudienceReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/datasources/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Audience id","required":true,"schema":{"type":"string","example":"5fb6675c09fd901023917a5f"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Audience id","required":true,"schema":{"type":"string","example":"5fb6675c09fd901023917a5f"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/datasources/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        from .models import Audience
        schema = Audience()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for updateAudienceById")
            print(e)

        

        return response
    
    async def getNSampleRecordsFromCsv(self, body=""):
        """Get n sample records from csv
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.getNSampleRecordsFromCsv()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import GetNRecordsCsvReq
        schema = GetNRecordsCsvReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/get-n-records", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sources/get-n-records", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        from .models import GetNRecordsCsvRes
        schema = GetNRecordsCsvRes()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getNSampleRecordsFromCsv")
            print(e)

        

        return response
    
    async def getEmailProviders(self, page_no=None, page_size=None, sort=None):
        """Get email providers
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        :param sort : To sort based on created_at : type object
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if sort:
            payload["sort"] = sort
        

        # Parameter validation
        schema = CommunicationValidator.getEmailProviders()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/providers", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}]}""", page_no=page_no, page_size=page_size, sort=sort)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, sort=sort)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/providers", page_no=page_no, page_size=page_size, sort=sort), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        from .models import EmailProviders
        schema = EmailProviders()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getEmailProviders")
            print(e)

        

        return response
    
    async def createEmailProvider(self, body=""):
        """Create email provider
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.createEmailProvider()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import EmailProviderReq
        schema = EmailProviderReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/providers", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/providers", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        from .models import EmailProvider
        schema = EmailProvider()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for createEmailProvider")
            print(e)

        

        return response
    
    async def getEmailProviderById(self, id=None):
        """Get email provider by id
        :param id : Email provider id : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CommunicationValidator.getEmailProviderById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/providers/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Email provider id","required":true,"schema":{"type":"string","example":"5fd9fd44c474a7e3d5d376d6"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Email provider id","required":true,"schema":{"type":"string","example":"5fd9fd44c474a7e3d5d376d6"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/providers/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        from .models import EmailProvider
        schema = EmailProvider()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getEmailProviderById")
            print(e)

        

        return response
    
    async def updateEmailProviderById(self, id=None, body=""):
        """Update email provider by id
        :param id : Email provider id : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CommunicationValidator.updateEmailProviderById()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import EmailProviderReq
        schema = EmailProviderReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/providers/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Email provider id","required":true,"schema":{"type":"string","example":"5fd9fd44c474a7e3d5d376d6"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Email provider id","required":true,"schema":{"type":"string","example":"5fd9fd44c474a7e3d5d376d6"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/providers/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        from .models import EmailProvider
        schema = EmailProvider()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for updateEmailProviderById")
            print(e)

        

        return response
    
    async def getEmailTemplates(self, page_no=None, page_size=None, sort=None):
        """Get email templates
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        :param sort : To sort based on created_at : type object
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if sort:
            payload["sort"] = sort
        

        # Parameter validation
        schema = CommunicationValidator.getEmailTemplates()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/templates", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}]}""", page_no=page_no, page_size=page_size, sort=sort)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, sort=sort)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/templates", page_no=page_no, page_size=page_size, sort=sort), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        from .models import EmailTemplates
        schema = EmailTemplates()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getEmailTemplates")
            print(e)

        

        return response
    
    async def createEmailTemplate(self, body=""):
        """Create email template
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.createEmailTemplate()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import EmailTemplateReq
        schema = EmailTemplateReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/templates", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/templates", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        from .models import EmailTemplateRes
        schema = EmailTemplateRes()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for createEmailTemplate")
            print(e)

        

        return response
    
    async def getSystemEmailTemplates(self, page_no=None, page_size=None, sort=None):
        """Get system email templates
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        :param sort : To sort based on created_at : type object
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if sort:
            payload["sort"] = sort
        

        # Parameter validation
        schema = CommunicationValidator.getSystemEmailTemplates()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/system-templates", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}]}""", page_no=page_no, page_size=page_size, sort=sort)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, sort=sort)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/system-templates", page_no=page_no, page_size=page_size, sort=sort), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        from .models import SystemEmailTemplates
        schema = SystemEmailTemplates()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getSystemEmailTemplates")
            print(e)

        

        return response
    
    async def getEmailTemplateById(self, id=None):
        """Get email template by id
        :param id : Email template id : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CommunicationValidator.getEmailTemplateById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/templates/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Email template id","required":true,"schema":{"type":"string","example":"5ef42a49c8b67d279c27a980"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Email template id","required":true,"schema":{"type":"string","example":"5ef42a49c8b67d279c27a980"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/templates/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        from .models import EmailTemplate
        schema = EmailTemplate()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getEmailTemplateById")
            print(e)

        

        return response
    
    async def updateEmailTemplateById(self, id=None, body=""):
        """Update email template by id
        :param id : Email template id : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CommunicationValidator.updateEmailTemplateById()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import EmailTemplateReq
        schema = EmailTemplateReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/templates/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Email template id","required":true,"schema":{"type":"string","example":"5ef42a49c8b67d279c27a980"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Email template id","required":true,"schema":{"type":"string","example":"5ef42a49c8b67d279c27a980"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/templates/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        from .models import EmailTemplateRes
        schema = EmailTemplateRes()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for updateEmailTemplateById")
            print(e)

        

        return response
    
    async def deleteEmailTemplateById(self, id=None):
        """Delete email template by id
        :param id : Email template id : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CommunicationValidator.deleteEmailTemplateById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/templates/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Email template id","required":true,"schema":{"type":"string","example":"5ef42a49c8b67d279c27a980"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Email template id","required":true,"schema":{"type":"string","example":"5ef42a49c8b67d279c27a980"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/email/templates/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        from .models import EmailTemplateDeleteSuccessRes
        schema = EmailTemplateDeleteSuccessRes()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for deleteEmailTemplateById")
            print(e)

        

        return response
    
    async def sendCommunicationSynchronously(self, body=""):
        """Send email or sms synchronously
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.sendCommunicationSynchronously()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import EngineRequest
        schema = EngineRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/engine/send-instant", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/engine/send-instant", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        from .models import EngineResponse
        schema = EngineResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for sendCommunicationSynchronously")
            print(e)

        

        return response
    
    async def sendCommunicationAsynchronously(self, body=""):
        """Send email or sms asynchronously
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.sendCommunicationAsynchronously()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import EngineRequest
        schema = EngineRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/engine/send-async", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/engine/send-async", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        from .models import EngineResponse
        schema = EngineResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for sendCommunicationAsynchronously")
            print(e)

        

        return response
    
    async def getEventSubscriptions(self, page_no=None, page_size=None, populate=None):
        """Get event subscriptions
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        :param populate : populate fields : type string
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if populate:
            payload["populate"] = populate
        

        # Parameter validation
        schema = CommunicationValidator.getEventSubscriptions()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/event/event-subscriptions", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"populate","in":"query","schema":{"type":"string"},"description":"populate fields"}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"populate","in":"query","schema":{"type":"string"},"description":"populate fields"}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}]}""", page_no=page_no, page_size=page_size, populate=populate)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, populate=populate)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/event/event-subscriptions", page_no=page_no, page_size=page_size, populate=populate), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        from .models import EventSubscriptions
        schema = EventSubscriptions()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getEventSubscriptions")
            print(e)

        

        return response
    
    async def getJobs(self, page_no=None, page_size=None, sort=None):
        """Get jobs
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        :param sort : To sort based on created_at : type object
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if sort:
            payload["sort"] = sort
        

        # Parameter validation
        schema = CommunicationValidator.getJobs()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/jobs/jobs", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}]}""", page_no=page_no, page_size=page_size, sort=sort)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, sort=sort)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/jobs/jobs", page_no=page_no, page_size=page_size, sort=sort), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        from .models import Jobs
        schema = Jobs()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getJobs")
            print(e)

        

        return response
    
    async def triggerCampaignJob(self, body=""):
        """Trigger campaign job
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.triggerCampaignJob()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import TriggerJobRequest
        schema = TriggerJobRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/jobs/trigger-job", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/jobs/trigger-job", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        from .models import TriggerJobResponse
        schema = TriggerJobResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for triggerCampaignJob")
            print(e)

        

        return response
    
    async def getJobLogs(self, page_no=None, page_size=None, sort=None):
        """Get job logs
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        :param sort : To sort based on created_at : type object
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if sort:
            payload["sort"] = sort
        

        # Parameter validation
        schema = CommunicationValidator.getJobLogs()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/jobs/logs", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}]}""", page_no=page_no, page_size=page_size, sort=sort)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, sort=sort)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/jobs/logs", page_no=page_no, page_size=page_size, sort=sort), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        from .models import JobLogs
        schema = JobLogs()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getJobLogs")
            print(e)

        

        return response
    
    async def getCommunicationLogs(self, page_id=None, page_size=None, sort=None, query=None):
        """Get communication logs
        :param page_id : Current page no : type string
        :param page_size : Current request items count : type integer
        :param sort : To sort based on _id : type object
        :param query :  : type object
        """
        payload = {}
        
        if page_id:
            payload["page_id"] = page_id
        
        if page_size:
            payload["page_size"] = page_size
        
        if sort:
            payload["sort"] = sort
        
        if query:
            payload["query"] = query
        

        # Parameter validation
        schema = CommunicationValidator.getCommunicationLogs()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/log", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[{"name":"page_id","in":"query","schema":{"type":"string"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"_id":{"type":"integer"}}},"description":"To sort based on _id"},{"name":"query","in":"query","schema":{"type":"object"}}],"query":[{"name":"page_id","in":"query","schema":{"type":"string"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"_id":{"type":"integer"}}},"description":"To sort based on _id"},{"name":"query","in":"query","schema":{"type":"object"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}]}""", page_id=page_id, page_size=page_size, sort=sort, query=query)
        query_string = await create_query_string(page_id=page_id, page_size=page_size, sort=sort, query=query)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/log", page_id=page_id, page_size=page_size, sort=sort, query=query), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        from .models import Logs
        schema = Logs()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getCommunicationLogs")
            print(e)

        

        return response
    
    async def sendOtp(self, body=""):
        """Send OTP Comms via email and sms
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.sendOtp()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SendOtpCommsReq
        schema = SendOtpCommsReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/otp/send-otp-comms", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/otp/send-otp-comms", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        from .models import SendOtpCommsRes
        schema = SendOtpCommsRes()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for sendOtp")
            print(e)

        

        return response
    
    async def verfiyOtp(self, body=""):
        """Verify OTP sent via email and sms
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.verfiyOtp()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import VerifyOtpCommsReq
        schema = VerifyOtpCommsReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/otp/verify-otp-comms", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/otp/verify-otp-comms", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        from .models import VerifyOtpCommsSuccessRes
        schema = VerifyOtpCommsSuccessRes()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for verfiyOtp")
            print(e)

        

        return response
    
    async def getSmsProviders(self, page_no=None, page_size=None, sort=None):
        """Get sms providers
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        :param sort : To sort based on created_at : type object
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if sort:
            payload["sort"] = sort
        

        # Parameter validation
        schema = CommunicationValidator.getSmsProviders()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/providers", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}]}""", page_no=page_no, page_size=page_size, sort=sort)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, sort=sort)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/providers", page_no=page_no, page_size=page_size, sort=sort), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        from .models import SmsProviders
        schema = SmsProviders()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getSmsProviders")
            print(e)

        

        return response
    
    async def createSmsProvider(self, body=""):
        """Create sms provider
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.createSmsProvider()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SmsProviderReq
        schema = SmsProviderReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/providers", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/providers", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        from .models import SmsProvider
        schema = SmsProvider()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for createSmsProvider")
            print(e)

        

        return response
    
    async def getSmsProviderById(self, id=None):
        """Get sms provider by id
        :param id : Sms provider id : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CommunicationValidator.getSmsProviderById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/providers/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Sms provider id","required":true,"schema":{"type":"string","example":"5fd9fd07c474a7710dd376d5"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Sms provider id","required":true,"schema":{"type":"string","example":"5fd9fd07c474a7710dd376d5"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/providers/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        from .models import SmsProvider
        schema = SmsProvider()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getSmsProviderById")
            print(e)

        

        return response
    
    async def updateSmsProviderById(self, id=None, body=""):
        """Update sms provider by id
        :param id : Sms provider id : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CommunicationValidator.updateSmsProviderById()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SmsProviderReq
        schema = SmsProviderReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/providers/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Sms provider id","required":true,"schema":{"type":"string","example":"5fd9fd07c474a7710dd376d5"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Sms provider id","required":true,"schema":{"type":"string","example":"5fd9fd07c474a7710dd376d5"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/providers/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        from .models import SmsProvider
        schema = SmsProvider()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for updateSmsProviderById")
            print(e)

        

        return response
    
    async def getSmsTemplates(self, page_no=None, page_size=None, sort=None):
        """Get sms templates
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        :param sort : To sort based on created_at : type object
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if sort:
            payload["sort"] = sort
        

        # Parameter validation
        schema = CommunicationValidator.getSmsTemplates()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/templates", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}]}""", page_no=page_no, page_size=page_size, sort=sort)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, sort=sort)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/templates", page_no=page_no, page_size=page_size, sort=sort), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        from .models import SmsTemplates
        schema = SmsTemplates()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getSmsTemplates")
            print(e)

        

        return response
    
    async def createSmsTemplate(self, body=""):
        """Create sms template
        """
        payload = {}
        

        # Parameter validation
        schema = CommunicationValidator.createSmsTemplate()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SmsTemplateReq
        schema = SmsTemplateReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/templates", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/templates", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        from .models import SmsTemplateRes
        schema = SmsTemplateRes()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for createSmsTemplate")
            print(e)

        

        return response
    
    async def getSmsTemplateById(self, id=None):
        """Get sms template by id
        :param id : Sms template id : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CommunicationValidator.getSmsTemplateById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/templates/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Sms template id","required":true,"schema":{"type":"string","example":"5ef42a49c8b67d279c27a980"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Sms template id","required":true,"schema":{"type":"string","example":"5ef42a49c8b67d279c27a980"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/templates/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        from .models import SmsTemplate
        schema = SmsTemplate()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getSmsTemplateById")
            print(e)

        

        return response
    
    async def updateSmsTemplateById(self, id=None, body=""):
        """Update sms template by id
        :param id : Sms template id : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CommunicationValidator.updateSmsTemplateById()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import SmsTemplateReq
        schema = SmsTemplateReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/templates/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Sms template id","required":true,"schema":{"type":"string","example":"5ef42a49c8b67d279c27a980"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Sms template id","required":true,"schema":{"type":"string","example":"5ef42a49c8b67d279c27a980"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/templates/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        from .models import SmsTemplateRes
        schema = SmsTemplateRes()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for updateSmsTemplateById")
            print(e)

        

        return response
    
    async def deleteSmsTemplateById(self, id=None):
        """Delete sms template by id
        :param id : Sms template id : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CommunicationValidator.deleteSmsTemplateById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/templates/{id}", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Sms template id","required":true,"schema":{"type":"string","example":"5ef42a49c8b67d279c27a980"}}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}},{"in":"path","name":"id","description":"Sms template id","required":true,"schema":{"type":"string","example":"5ef42a49c8b67d279c27a980"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/templates/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        from .models import SmsTemplateDeleteSuccessRes
        schema = SmsTemplateDeleteSuccessRes()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for deleteSmsTemplateById")
            print(e)

        

        return response
    
    async def getSystemSystemTemplates(self, page_no=None, page_size=None, sort=None):
        """Get system sms templates
        :param page_no : Current page no : type integer
        :param page_size : Current request items count : type integer
        :param sort : To sort based on created_at : type object
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if sort:
            payload["sort"] = sort
        

        # Parameter validation
        schema = CommunicationValidator.getSystemSystemTemplates()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/system-templates", """{"required":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"Current page no"},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"Current request items count"},{"name":"sort","in":"query","schema":{"type":"object","properties":{"created_at":{"type":"integer"}}},"description":"To sort based on created_at"}],"headers":[],"path":[{"in":"path","name":"company_id","description":"Company id","required":true,"schema":{"type":"string","example":"1"}},{"in":"path","name":"application_id","description":"Application id","required":true,"schema":{"type":"string","example":"5ea6821b3425bb07c82a25c1"}}]}""", page_no=page_no, page_size=page_size, sort=sort)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, sort=sort)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/communication/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/sms/system-templates", page_no=page_no, page_size=page_size, sort=sort), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        from .models import SystemSmsTemplates
        schema = SystemSmsTemplates()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getSystemSystemTemplates")
            print(e)

        

        return response
    

