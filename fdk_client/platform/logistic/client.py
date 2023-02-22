

""" Logistic Platform Client."""

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .validator import LogisticValidator

class Logistic:
    def __init__(self, config):
        self._conf = config
    
    async def getEntityRegionView(self, body=""):
        """This API returns response for Entity Region View.
        """
        payload = {}
        

        # Parameter validation
        schema = LogisticValidator.getEntityRegionView()
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/regions", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getListView(self, page_number=None, page_size=None, name=None, is_active=None, channel_ids=None):
        """This API returns Zone List View of the application.
        :param page_number : index of the item to start returning with : type integer
        :param page_size : determines the items to be displayed in a page : type integer
        :param name : Name of particular zone in the seller account : type string
        :param is_active : status of  zone whether active or inactive : type boolean
        :param channel_ids : zones associated with the given channel ids' : type string
        """
        payload = {}
        
        if page_number:
            payload["page_number"] = page_number
        
        if page_size:
            payload["page_size"] = page_size
        
        if name:
            payload["name"] = name
        
        if is_active:
            payload["is_active"] = is_active
        
        if channel_ids:
            payload["channel_ids"] = channel_ids
        

        # Parameter validation
        schema = LogisticValidator.getListView()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/zones", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"page_number","description":"index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"name","description":"Name of particular zone in the seller account","schema":{"type":"string"}},{"in":"query","name":"is_active","description":"status of  zone whether active or inactive","schema":{"type":"boolean"}},{"in":"query","name":"channel_ids","description":"zones associated with the given channel ids'","schema":{"type":"string"}}],"query":[{"in":"query","name":"page_number","description":"index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"name","description":"Name of particular zone in the seller account","schema":{"type":"string"}},{"in":"query","name":"is_active","description":"status of  zone whether active or inactive","schema":{"type":"boolean"}},{"in":"query","name":"channel_ids","description":"zones associated with the given channel ids'","schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}]}""", page_number=page_number, page_size=page_size, name=name, is_active=is_active, channel_ids=channel_ids)
        query_string = await create_query_string(page_number=page_number, page_size=page_size, name=name, is_active=is_active, channel_ids=channel_ids)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/zones", page_number=page_number, page_size=page_size, name=name, is_active=is_active, channel_ids=channel_ids), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getCompanyStoreView(self, page_number=None, page_size=None, zone_id=None, enabled=None, q=None):
        """This API returns Company Store View of the application.
        :param page_number : index of the item to start returning with : type integer
        :param page_size : determines the items to be displayed in a page : type integer
        :param zone_id : A `zone_id` is a unique identifier for a particular zone. : type string
        :param enabled : select enabled/all stores. : type string
        :param q : search with name as a free text : type string
        """
        payload = {}
        
        if page_number:
            payload["page_number"] = page_number
        
        if page_size:
            payload["page_size"] = page_size
        
        if zone_id:
            payload["zone_id"] = zone_id
        
        if enabled:
            payload["enabled"] = enabled
        
        if q:
            payload["q"] = q
        

        # Parameter validation
        schema = LogisticValidator.getCompanyStoreView()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/all-stores", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular company.","schema":{"type":"integer"},"required":true}],"optional":[{"in":"query","name":"page_number","description":"index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"zone_id","description":"A `zone_id` is a unique identifier for a particular zone.","schema":{"type":"string"}},{"in":"query","name":"enabled","description":"select enabled/all stores.","schema":{"type":"string"}},{"in":"query","name":"q","description":"search with name as a free text","schema":{"type":"string"}}],"query":[{"in":"query","name":"page_number","description":"index of the item to start returning with","schema":{"type":"integer","default":1,"minimum":1}},{"in":"query","name":"page_size","description":"determines the items to be displayed in a page","schema":{"type":"integer","default":10,"minimum":1}},{"in":"query","name":"zone_id","description":"A `zone_id` is a unique identifier for a particular zone.","schema":{"type":"string"}},{"in":"query","name":"enabled","description":"select enabled/all stores.","schema":{"type":"string"}},{"in":"query","name":"q","description":"search with name as a free text","schema":{"type":"string"}}],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular company.","schema":{"type":"integer"},"required":true}]}""", page_number=page_number, page_size=page_size, zone_id=zone_id, enabled=enabled, q=q)
        query_string = await create_query_string(page_number=page_number, page_size=page_size, zone_id=zone_id, enabled=enabled, q=q)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/all-stores", page_number=page_number, page_size=page_size, zone_id=zone_id, enabled=enabled, q=q), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getZoneDataView(self, zone_id=None):
        """This API returns Zone Data View of the application.
        :param zone_id : A `zone_id` is a unique identifier for a particular zone. : type string
        """
        payload = {}
        
        if zone_id:
            payload["zone_id"] = zone_id
        

        # Parameter validation
        schema = LogisticValidator.getZoneDataView()
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/zone/{zone_id}", zone_id=zone_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def updateZoneControllerView(self, zone_id=None, body=""):
        """This API returns response of updation of zone in mongo database.
        :param zone_id : A `zone_id` is a unique identifier for a particular zone. : type string
        """
        payload = {}
        
        if zone_id:
            payload["zone_id"] = zone_id
        

        # Parameter validation
        schema = LogisticValidator.updateZoneControllerView()
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
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/zone/{zone_id}", zone_id=zone_id, ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def insertZoneControllerView(self, body=""):
        """This API returns response of insertion of zone in mongo database.<br>Correction- `zone_id` in the path must be removed.<br> path is `/service/platform/logistics-internal/v1.0/company/{company_id}/zone/`
        """
        payload = {}
        

        # Parameter validation
        schema = LogisticValidator.insertZoneControllerView()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ZoneRequest
        schema = ZoneRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/zone/", """{"required":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"company_id","description":"A `company_id` is a unique identifier for a particular sale channel.","schema":{"type":"integer"},"required":true}]}""", )
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/zone/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getStore(self, store_uid=None):
        """This API returns stores data.
        :param store_uid : A `store_uid` contains a specific ID of a store. : type integer
        """
        payload = {}
        
        if store_uid:
            payload["store_uid"] = store_uid
        

        # Parameter validation
        schema = LogisticValidator.getStore()
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/stores/{store_uid}", store_uid=store_uid), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getAllStores(self, ):
        """This API returns stores data.
        """
        payload = {}
        

        # Parameter validation
        schema = LogisticValidator.getAllStores()
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/logistics/v1.0/company/{self._conf.companyId}/logistics/stores", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    

