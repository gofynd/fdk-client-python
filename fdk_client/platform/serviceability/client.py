

"""Serviceability Platform Client"""

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .validator import ServiceabilityValidator

class Serviceability:
    def __init__(self, config):
        self._conf = config

    
    async def getEntityRegionView(self, body=""):
        """This API returns response for Entity Region View.
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.getEntityRegionView()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import EntityRegionView_Request
        schema = EntityRegionView_Request()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/regions", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/regions", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import EntityRegionView_Response
            schema = EntityRegionView_Response()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getEntityRegionView")
                print(e)

        

        return response
    
    async def getListView(self, page_number=None, page_size=None, name=None, is_active=None, channel_ids=None, q=None):
        """This API returns Zone List View of the application.
        :param page_number : index of the item to start returning with : type integer
        :param page_size : determines the items to be displayed in a page : type integer
        :param name : Name of particular zone in the seller account : type string
        :param is_active : status of  zone whether active or inactive : type boolean
        :param channel_ids : zones associated with the given channel ids' : type string
        :param q : search with name as a free text : type string
        """
        payload = {}
        
        if page_number is not None:
            payload["page_number"] = page_number
        
        if page_size is not None:
            payload["page_size"] = page_size
        
        if name is not None:
            payload["name"] = name
        
        if is_active is not None:
            payload["is_active"] = is_active
        
        if channel_ids is not None:
            payload["channel_ids"] = channel_ids
        
        if q is not None:
            payload["q"] = q
        

        # Parameter validation
        schema = ServiceabilityValidator.getListView()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/zones", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"page_number","description":"index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"name","description":"Name of particular zone in the seller account","schema":{"type":"string"}},{"in":"query","name":"is_active","description":"status of  zone whether active or inactive","schema":{"type":"boolean"}},{"in":"query","name":"channel_ids","description":"zones associated with the given channel ids'","schema":{"type":"string"}},{"in":"query","name":"q","description":"search with name as a free text","schema":{"type":"string"}}],"query":[{"in":"query","name":"page_number","description":"index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"name","description":"Name of particular zone in the seller account","schema":{"type":"string"}},{"in":"query","name":"is_active","description":"status of  zone whether active or inactive","schema":{"type":"boolean"}},{"in":"query","name":"channel_ids","description":"zones associated with the given channel ids'","schema":{"type":"string"}},{"in":"query","name":"q","description":"search with name as a free text","schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}]}""", page_number=page_number, page_size=page_size, name=name, is_active=is_active, channel_ids=channel_ids, q=q)
        query_string = await create_query_string(page_number=page_number, page_size=page_size, name=name, is_active=is_active, channel_ids=channel_ids, q=q)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/zones", page_number=page_number, page_size=page_size, name=name, is_active=is_active, channel_ids=channel_ids, q=q), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import ListViewResponse
            schema = ListViewResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getListView")
                print(e)

        

        return response
    
    async def getCompanyStoreView(self, page_number=None, page_size=None):
        """This API returns Company Store View of the application.
        :param page_number : index of the item to start returning with : type integer
        :param page_size : determines the items to be displayed in a page : type integer
        """
        payload = {}
        
        if page_number is not None:
            payload["page_number"] = page_number
        
        if page_size is not None:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = ServiceabilityValidator.getCompanyStoreView()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/all-stores", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular company.","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"page_number","description":"index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}}],"query":[{"in":"query","name":"page_number","description":"index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular company.","schema":{"type":"integer"},"required":true}]}""", page_number=page_number, page_size=page_size)
        query_string = await create_query_string(page_number=page_number, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/all-stores", page_number=page_number, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import CompanyStoreView_Response
            schema = CompanyStoreView_Response()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCompanyStoreView")
                print(e)

        

        return response
    
    async def updateZoneControllerView(self, zone_id=None, body=""):
        """This API returns response of updation of zone in mongo database.
        :param zone_id : A `zone_id` is a unique identifier for a particular zone. : type string
        """
        payload = {}
        
        if zone_id is not None:
            payload["zone_id"] = zone_id
        

        # Parameter validation
        schema = ServiceabilityValidator.updateZoneControllerView()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ZoneUpdateRequest
        schema = ZoneUpdateRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/zone/{zone_id}", """{"required":[{"in":"path","name":"zone_id","description":"A `zone_id` is a unique identifier for a particular zone.","schema":{"type":"string"},"required":true},{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"zone_id","description":"A `zone_id` is a unique identifier for a particular zone.","schema":{"type":"string"},"required":true},{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}]}""", zone_id=zone_id, )
        query_string = await create_query_string(zone_id=zone_id, )
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/zone/{zone_id}", zone_id=zone_id, ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import ZoneSuccessResponse
            schema = ZoneSuccessResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateZoneControllerView")
                print(e)

        

        return response
    
    async def getZoneDataView(self, zone_id=None):
        """This API returns Zone Data View of the application.
        :param zone_id : A `zone_id` is a unique identifier for a particular zone. : type string
        """
        payload = {}
        
        if zone_id is not None:
            payload["zone_id"] = zone_id
        

        # Parameter validation
        schema = ServiceabilityValidator.getZoneDataView()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/zone/{zone_id}", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"zone_id","description":"A `zone_id` is a unique identifier for a particular zone.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"zone_id","description":"A `zone_id` is a unique identifier for a particular zone.","schema":{"type":"string"},"required":true}]}""", zone_id=zone_id)
        query_string = await create_query_string(zone_id=zone_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/zone/{zone_id}", zone_id=zone_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import GetSingleZoneDataViewResponse
            schema = GetSingleZoneDataViewResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getZoneDataView")
                print(e)

        

        return response
    
    async def createZone(self, body=""):
        """This API allows you to create a new zone with the specified information. A zone enables serviceability based on given pincodes or regions. By creating a zone and including specific pincodes or regions, you can ensure that the stores associated with the zone are serviceable for those added pincodes or regions. This functionality is particularly useful when you need to ensure serviceability for multiple pincodes or regions by grouping them into a single zone.
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.createZone()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ZoneRequest
        schema = ZoneRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/zone", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/zone", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import ZoneResponse
            schema = ZoneResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createZone")
                print(e)

        

        return response
    
    async def getZoneListView(self, page_number=None, page_no=None, page_size=None, name=None, is_active=None, channel_ids=None, q=None, zone_id=None):
        """This API returns Zone List View of the application.
        :param page_number : index of the item to start returning with : type integer
        :param page_no : index of the item to start returning with : type integer
        :param page_size : determines the items to be displayed in a page : type integer
        :param name : Name of particular zone in the seller account : type string
        :param is_active : status of  zone whether active or inactive : type boolean
        :param channel_ids : zones associated with the given channel ids' : type string
        :param q : search with name as a free text : type string
        :param zone_id : list of zones to query for : type array
        """
        payload = {}
        
        if page_number is not None:
            payload["page_number"] = page_number
        
        if page_no is not None:
            payload["page_no"] = page_no
        
        if page_size is not None:
            payload["page_size"] = page_size
        
        if name is not None:
            payload["name"] = name
        
        if is_active is not None:
            payload["is_active"] = is_active
        
        if channel_ids is not None:
            payload["channel_ids"] = channel_ids
        
        if q is not None:
            payload["q"] = q
        
        if zone_id is not None:
            payload["zone_id"] = zone_id
        

        # Parameter validation
        schema = ServiceabilityValidator.getZoneListView()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/zones-list", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"page_number","description":"index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_no","description":"index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"name","description":"Name of particular zone in the seller account","schema":{"type":"string"}},{"in":"query","name":"is_active","description":"status of  zone whether active or inactive","schema":{"type":"boolean"}},{"in":"query","name":"channel_ids","description":"zones associated with the given channel ids'","schema":{"type":"string"}},{"in":"query","name":"q","description":"search with name as a free text","schema":{"type":"string"}},{"in":"query","name":"zone_id","description":"list of zones to query for","schema":{"type":"array","items":{"type":"string"}}}],"query":[{"in":"query","name":"page_number","description":"index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_no","description":"index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"name","description":"Name of particular zone in the seller account","schema":{"type":"string"}},{"in":"query","name":"is_active","description":"status of  zone whether active or inactive","schema":{"type":"boolean"}},{"in":"query","name":"channel_ids","description":"zones associated with the given channel ids'","schema":{"type":"string"}},{"in":"query","name":"q","description":"search with name as a free text","schema":{"type":"string"}},{"in":"query","name":"zone_id","description":"list of zones to query for","schema":{"type":"array","items":{"type":"string"}}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}]}""", page_number=page_number, page_no=page_no, page_size=page_size, name=name, is_active=is_active, channel_ids=channel_ids, q=q, zone_id=zone_id)
        query_string = await create_query_string(page_number=page_number, page_no=page_no, page_size=page_size, name=name, is_active=is_active, channel_ids=channel_ids, q=q, zone_id=zone_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/zones-list", page_number=page_number, page_no=page_no, page_size=page_size, name=name, is_active=is_active, channel_ids=channel_ids, q=q, zone_id=zone_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import ListViewResponse
            schema = ListViewResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getZoneListView")
                print(e)

        

        return response
    
    async def getStore(self, store_uid=None):
        """This API returns stores data.
        :param store_uid : A `store_uid` contains a specific ID of a store. : type integer
        """
        payload = {}
        
        if store_uid is not None:
            payload["store_uid"] = store_uid
        

        # Parameter validation
        schema = ServiceabilityValidator.getStore()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/stores/{store_uid}", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"store_uid","description":"A `store_uid` contains a specific ID of a store.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"store_uid","description":"A `store_uid` contains a specific ID of a store.","schema":{"type":"integer"},"required":true}]}""", store_uid=store_uid)
        query_string = await create_query_string(store_uid=store_uid)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/stores/{store_uid}", store_uid=store_uid), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import GetStoresViewResponse
            schema = GetStoresViewResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getStore")
                print(e)

        

        return response
    
    async def getAllStores(self, ):
        """This API returns stores data.
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.getAllStores()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/logistics/stores", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/logistics/stores", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import GetStoresViewResponse
            schema = GetStoresViewResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAllStores")
                print(e)

        

        return response
    
    async def getOptimalLocations(self, body=""):
        """This API returns serviceable store of the item.
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.getOptimalLocations()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ReAssignStoreRequest
        schema = ReAssignStoreRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/reassign", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/reassign", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import ReAssignStoreResponse
            schema = ReAssignStoreResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getOptimalLocations")
                print(e)

        

        return response
    
    async def upsertDpAccount(self, body=""):
        """This API returns response of upsertion of DpAccount in mongo database.
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.upsertDpAccount()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CompanyDpAccountRequest
        schema = CompanyDpAccountRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier/account", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier/account", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import CompanyDpAccountResponse
            schema = CompanyDpAccountResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for upsertDpAccount")
                print(e)

        

        return response
    
    async def getDpAccount(self, page_number=None, page_size=None, stage=None, payment_mode=None, transport_type=None):
        """This API returns response DpAccount of a company from mongo database.
        :param page_number : index of the item to start returning with : type integer
        :param page_size : determines the items to be displayed in a page : type integer
        :param stage : stage of the account. enabled/disabled : type string
        :param payment_mode : Filters dp accounts based on payment mode : type string
        :param transport_type : Filters dp accounts based on transport_type : type string
        """
        payload = {}
        
        if page_number is not None:
            payload["page_number"] = page_number
        
        if page_size is not None:
            payload["page_size"] = page_size
        
        if stage is not None:
            payload["stage"] = stage
        
        if payment_mode is not None:
            payload["payment_mode"] = payment_mode
        
        if transport_type is not None:
            payload["transport_type"] = transport_type
        

        # Parameter validation
        schema = ServiceabilityValidator.getDpAccount()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier/account", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"page_number","description":"index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"stage","description":"stage of the account. enabled/disabled","schema":{"type":"string"}},{"in":"query","name":"payment_mode","description":"Filters dp accounts based on payment mode","schema":{"type":"string"}},{"in":"query","name":"transport_type","description":"Filters dp accounts based on transport_type","schema":{"type":"string"}}],"query":[{"in":"query","name":"page_number","description":"index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"stage","description":"stage of the account. enabled/disabled","schema":{"type":"string"}},{"in":"query","name":"payment_mode","description":"Filters dp accounts based on payment mode","schema":{"type":"string"}},{"in":"query","name":"transport_type","description":"Filters dp accounts based on transport_type","schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}]}""", page_number=page_number, page_size=page_size, stage=stage, payment_mode=payment_mode, transport_type=transport_type)
        query_string = await create_query_string(page_number=page_number, page_size=page_size, stage=stage, payment_mode=payment_mode, transport_type=transport_type)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier/account", page_number=page_number, page_size=page_size, stage=stage, payment_mode=payment_mode, transport_type=transport_type), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import CompanyDpAccountListResponse
            schema = CompanyDpAccountListResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getDpAccount")
                print(e)

        

        return response
    
    async def updateDpRule(self, rule_uid=None, body=""):
        """This API updates and returns response of DpRules from mongo database.
        :param rule_uid : A `rule_uid` is a unique identifier for a particular Dp. : type string
        """
        payload = {}
        
        if rule_uid is not None:
            payload["rule_uid"] = rule_uid
        

        # Parameter validation
        schema = ServiceabilityValidator.updateDpRule()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import DpRulesUpdateRequest
        schema = DpRulesUpdateRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier/rules/{rule_uid}", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"rule_uid","description":"A `rule_uid` is a unique identifier for a particular Dp.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"rule_uid","description":"A `rule_uid` is a unique identifier for a particular Dp.","schema":{"type":"string"},"required":true}]}""", rule_uid=rule_uid)
        query_string = await create_query_string(rule_uid=rule_uid)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier/rules/{rule_uid}", rule_uid=rule_uid), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import DpRuleUpdateSuccessResponse
            schema = DpRuleUpdateSuccessResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateDpRule")
                print(e)

        

        return response
    
    async def getDpRules(self, rule_uid=None):
        """This API returns response of DpRules from mongo database.
        :param rule_uid : A `rule_uid` is a unique identifier for a particular Dp. : type string
        """
        payload = {}
        
        if rule_uid is not None:
            payload["rule_uid"] = rule_uid
        

        # Parameter validation
        schema = ServiceabilityValidator.getDpRules()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier/rules/{rule_uid}", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"rule_uid","description":"A `rule_uid` is a unique identifier for a particular Dp.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true},{"in":"path","name":"rule_uid","description":"A `rule_uid` is a unique identifier for a particular Dp.","schema":{"type":"string"},"required":true}]}""", rule_uid=rule_uid)
        query_string = await create_query_string(rule_uid=rule_uid)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier/rules/{rule_uid}", rule_uid=rule_uid), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import DpRuleSuccessResponse
            schema = DpRuleSuccessResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getDpRules")
                print(e)

        

        return response
    
    async def upsertDpRules(self, body=""):
        """This API returns response of upsert of DpRules in mongo database.
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.upsertDpRules()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import DpRuleRequest
        schema = DpRuleRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier/rules", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier/rules", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import DpRuleSuccessResponse
            schema = DpRuleSuccessResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for upsertDpRules")
                print(e)

        

        return response
    
    async def getDpRuleInsert(self, page_number=None, page_size=None):
        """This API returns response of DpRules from mongo database.
        :param page_number : index of the item to start returning with : type integer
        :param page_size : determines the items to be displayed in a page : type integer
        """
        payload = {}
        
        if page_number is not None:
            payload["page_number"] = page_number
        
        if page_size is not None:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = ServiceabilityValidator.getDpRuleInsert()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier/rules", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"page_number","description":"index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}}],"query":[{"in":"query","name":"page_number","description":"index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}]}""", page_number=page_number, page_size=page_size)
        query_string = await create_query_string(page_number=page_number, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier/rules", page_number=page_number, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import DpMultipleRuleSuccessResponse
            schema = DpMultipleRuleSuccessResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getDpRuleInsert")
                print(e)

        

        return response
    
    async def upsertDpCompanyRules(self, body=""):
        """This API returns response of upsert of DpCompanyRules in mongo database.
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.upsertDpCompanyRules()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import DPCompanyRuleRequest
        schema = DPCompanyRuleRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier/priority", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier/priority", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        if 200 <= int(response['status_code']) < 300:
            from .models import DPCompanyRuleResponse
            schema = DPCompanyRuleResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for upsertDpCompanyRules")
                print(e)

        

        return response
    
    async def getDpCompanyRules(self, ):
        """This API returns response of all DpCompanyRules from mongo database.
        """
        payload = {}
        

        # Parameter validation
        schema = ServiceabilityValidator.getDpCompanyRules()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier/priority", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/courier/priority", ), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        if 200 <= int(response['status_code']) < 300:
            from .models import DPCompanyRuleResponse
            schema = DPCompanyRuleResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getDpCompanyRules")
                print(e)

        

        return response
    

