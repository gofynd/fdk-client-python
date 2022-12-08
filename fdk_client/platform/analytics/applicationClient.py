

"""Analytics Platform Client."""

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .applicationValidator import AnalyticsValidator

class Analytics:
    def __init__(self, config, applicationId):
        self._conf = config
        self.applicationId = applicationId
    
    async def getStatiscticsGroups(self, ):
        """Get statistics groups
        """
        payload = {}
        

        # Parameter validation
        schema = AnalyticsValidator.getStatiscticsGroups()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/analytics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/stats/group", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}}]}""", )
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/analytics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/stats/group", ), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getStatiscticsGroupComponents(self, group_name=None):
        """Get statistics group components
        :param group_name : Group name : type string
        """
        payload = {}
        
        if group_name:
            payload["group_name"] = group_name
        

        # Parameter validation
        schema = AnalyticsValidator.getStatiscticsGroupComponents()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/analytics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/stats/group/{group_name}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"group_name","in":"path","description":"Group name","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"group_name","in":"path","description":"Group name","required":true,"schema":{"type":"string"}}]}""", group_name=group_name)
        query_string = await create_query_string(group_name=group_name)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/analytics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/stats/group/{group_name}", group_name=group_name), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getComponentStatsCSV(self, component_name=None):
        """Get component statistics csv
        :param component_name : Component name : type string
        """
        payload = {}
        
        if component_name:
            payload["component_name"] = component_name
        

        # Parameter validation
        schema = AnalyticsValidator.getComponentStatsCSV()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/analytics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/stats/component/{component_name}.csv", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"component_name","in":"path","description":"Component name","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"component_name","in":"path","description":"Component name","required":true,"schema":{"type":"string"}}]}""", component_name=component_name)
        query_string = await create_query_string(component_name=component_name)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/analytics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/stats/component/{component_name}.csv", component_name=component_name), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getComponentStatsPDF(self, component_name=None):
        """Get component statistics pdf
        :param component_name : Component name : type string
        """
        payload = {}
        
        if component_name:
            payload["component_name"] = component_name
        

        # Parameter validation
        schema = AnalyticsValidator.getComponentStatsPDF()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/analytics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/stats/component/{component_name}.pdf", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"component_name","in":"path","description":"Component name","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"component_name","in":"path","description":"Component name","required":true,"schema":{"type":"string"}}]}""", component_name=component_name)
        query_string = await create_query_string(component_name=component_name)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/analytics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/stats/component/{component_name}.pdf", component_name=component_name), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getComponentStats(self, component_name=None):
        """Get component statistics
        :param component_name : Component name : type string
        """
        payload = {}
        
        if component_name:
            payload["component_name"] = component_name
        

        # Parameter validation
        schema = AnalyticsValidator.getComponentStats()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/analytics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/stats/component/{component_name}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"component_name","in":"path","description":"Component name","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"component_name","in":"path","description":"Component name","required":true,"schema":{"type":"string"}}]}""", component_name=component_name)
        query_string = await create_query_string(component_name=component_name)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/analytics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/stats/component/{component_name}", component_name=component_name), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getAbandonCartList(self, from_date=None, to_date=None, page_no=None, page_size=None):
        """Get abandon carts list
        :param from_date : From date : type string
        :param to_date : To date : type string
        :param page_no : Current page number : type integer
        :param page_size : Current page size : type integer
        """
        payload = {}
        
        if from_date:
            payload["from_date"] = from_date
        
        if to_date:
            payload["to_date"] = to_date
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        

        # Parameter validation
        schema = AnalyticsValidator.getAbandonCartList()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/analytics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/cart/from/{from_date}/to/{to_date}/abandon-cart/", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"from_date","in":"path","description":"From date","required":true,"schema":{"type":"string"}},{"name":"to_date","in":"path","description":"To date","required":true,"schema":{"type":"string"}}],"optional":[{"name":"page_no","in":"query","description":"Current page number","required":false,"schema":{"type":"integer","default":0}},{"name":"page_size","in":"query","description":"Current page size","required":false,"schema":{"type":"integer","default":10}}],"query":[{"name":"page_no","in":"query","description":"Current page number","required":false,"schema":{"type":"integer","default":0}},{"name":"page_size","in":"query","description":"Current page size","required":false,"schema":{"type":"integer","default":10}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"from_date","in":"path","description":"From date","required":true,"schema":{"type":"string"}},{"name":"to_date","in":"path","description":"To date","required":true,"schema":{"type":"string"}}]}""", from_date=from_date, to_date=to_date, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(from_date=from_date, to_date=to_date, page_no=page_no, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/analytics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/cart/from/{from_date}/to/{to_date}/abandon-cart/", from_date=from_date, to_date=to_date, page_no=page_no, page_size=page_size), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getAbandonCartsCSV(self, from_date=None, to_date=None):
        """Get abandon carts csv
        :param from_date : From date : type string
        :param to_date : To date : type string
        """
        payload = {}
        
        if from_date:
            payload["from_date"] = from_date
        
        if to_date:
            payload["to_date"] = to_date
        

        # Parameter validation
        schema = AnalyticsValidator.getAbandonCartsCSV()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/analytics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/cart/{from_date}/to/{to_date}/abandon-cart.csv", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"from_date","in":"path","description":"From date","required":true,"schema":{"type":"string"}},{"name":"to_date","in":"path","description":"To date","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"from_date","in":"path","description":"From date","required":true,"schema":{"type":"string"}},{"name":"to_date","in":"path","description":"To date","required":true,"schema":{"type":"string"}}]}""", from_date=from_date, to_date=to_date)
        query_string = await create_query_string(from_date=from_date, to_date=to_date)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/analytics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/cart/{from_date}/to/{to_date}/abandon-cart.csv", from_date=from_date, to_date=to_date), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getAbandonCartDetail(self, cart_id=None):
        """Get abandon cart details
        :param cart_id : Cart Id : type string
        """
        payload = {}
        
        if cart_id:
            payload["cart_id"] = cart_id
        

        # Parameter validation
        schema = AnalyticsValidator.getAbandonCartDetail()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/analytics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/cart/abandon-cart/{cart_id}", """{"required":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"cart_id","in":"path","description":"Cart Id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"Company Id","required":true,"schema":{"type":"string"}},{"name":"application_id","in":"path","description":"Application Id","required":true,"schema":{"type":"string"}},{"name":"cart_id","in":"path","description":"Cart Id","required":true,"schema":{"type":"string"}}]}""", cart_id=cart_id)
        query_string = await create_query_string(cart_id=cart_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/analytics/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/cart/abandon-cart/{cart_id}", cart_id=cart_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    

