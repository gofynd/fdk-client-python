

""" Discount Platform Client."""

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .validator import DiscountValidator

class Discount:
    def __init__(self, config):
        self._conf = config
    
    async def getDiscounts(self, view=None, q=None, page_no=None, page_size=None, archived=None, month=None, year=None, type=None, app_ids=None):
        """Fetch discount list.
        :param view : listing or calender.  Default is listing. : type string
        :param q : The search query. This can be a partial or complete name of a discount. : type string
        :param page_no : page number. Default is 1. : type integer
        :param page_size : page size. Default is 12. : type integer
        :param archived : archived. Default is false. : type boolean
        :param month : month. Default is current month. : type integer
        :param year : year. Default is current year. : type integer
        :param type : basic or custom. : type string
        :param app_ids : application ids. : type array
        """
        payload = {}
        
        if view:
            payload["view"] = view
        
        if q:
            payload["q"] = q
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if archived:
            payload["archived"] = archived
        
        if month:
            payload["month"] = month
        
        if year:
            payload["year"] = year
        
        if type:
            payload["type"] = type
        
        if app_ids:
            payload["app_ids"] = app_ids
        

        # Parameter validation
        schema = DiscountValidator.getDiscounts()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/discount/v1.0/company/{self._conf.companyId}/job/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[{"name":"view","in":"query","description":"listing or calender.  Default is listing.","required":false,"schema":{"type":"string","enum":["listing","calender"]}},{"name":"q","in":"query","description":"The search query. This can be a partial or complete name of a discount.","required":false,"schema":{"type":"string"}},{"name":"page_no","in":"query","description":"page number. Default is 1.","required":false,"schema":{"type":"integer"}},{"name":"page_size","in":"query","description":"page size. Default is 12.","required":false,"schema":{"type":"integer"}},{"name":"archived","in":"query","description":"archived. Default is false.","required":false,"schema":{"type":"boolean","enum":[true,false]}},{"name":"month","in":"query","description":"month. Default is current month.","required":false,"schema":{"type":"integer"}},{"name":"year","in":"query","description":"year. Default is current year.","required":false,"schema":{"type":"integer"}},{"name":"type","in":"query","description":"basic or custom.","required":false,"schema":{"type":"string"}},{"name":"app_ids","in":"query","description":"application ids.","required":false,"schema":{"type":"array","items":{"type":"string"}}}],"query":[{"name":"view","in":"query","description":"listing or calender.  Default is listing.","required":false,"schema":{"type":"string","enum":["listing","calender"]}},{"name":"q","in":"query","description":"The search query. This can be a partial or complete name of a discount.","required":false,"schema":{"type":"string"}},{"name":"page_no","in":"query","description":"page number. Default is 1.","required":false,"schema":{"type":"integer"}},{"name":"page_size","in":"query","description":"page size. Default is 12.","required":false,"schema":{"type":"integer"}},{"name":"archived","in":"query","description":"archived. Default is false.","required":false,"schema":{"type":"boolean","enum":[true,false]}},{"name":"month","in":"query","description":"month. Default is current month.","required":false,"schema":{"type":"integer"}},{"name":"year","in":"query","description":"year. Default is current year.","required":false,"schema":{"type":"integer"}},{"name":"type","in":"query","description":"basic or custom.","required":false,"schema":{"type":"string"}},{"name":"app_ids","in":"query","description":"application ids.","required":false,"schema":{"type":"array","items":{"type":"string"}}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}}]}""", view=view, q=q, page_no=page_no, page_size=page_size, archived=archived, month=month, year=year, type=type, app_ids=app_ids)
        query_string = await create_query_string(view=view, q=q, page_no=page_no, page_size=page_size, archived=archived, month=month, year=year, type=type, app_ids=app_ids)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/discount/v1.0/company/{self._conf.companyId}/job/", view=view, q=q, page_no=page_no, page_size=page_size, archived=archived, month=month, year=year, type=type, app_ids=app_ids), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def createDiscount(self, body=""):
        """Create Discount.
        """
        payload = {}
        

        # Parameter validation
        schema = DiscountValidator.createDiscount()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateUpdateDiscount
        schema = CreateUpdateDiscount()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/discount/v1.0/company/{self._conf.companyId}/job/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}}]}""", )
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/discount/v1.0/company/{self._conf.companyId}/job/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getDiscount(self, id=None):
        """Fetch discount.
        :param id : unique id. : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = DiscountValidator.getDiscount()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/discount/v1.0/company/{self._conf.companyId}/job/{id}/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"id","in":"path","description":"unique id.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"id","in":"path","description":"unique id.","required":true,"schema":{"type":"string"}}]}""", id=id)
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/discount/v1.0/company/{self._conf.companyId}/job/{id}/", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def updateDiscount(self, id=None, body=""):
        """Create Discount.
        :param id : id : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = DiscountValidator.updateDiscount()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateUpdateDiscount
        schema = CreateUpdateDiscount()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/discount/v1.0/company/{self._conf.companyId}/job/{id}/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"id","in":"path","description":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"id","in":"path","description":"id","required":true,"schema":{"type":"string"}}]}""", id=id)
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
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/discount/v1.0/company/{self._conf.companyId}/job/{id}/", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def upsertDiscountItems(self, id=None, body=""):
        """Create custom discounts through API.
        :param id : Job ID of the discount. : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = DiscountValidator.upsertDiscountItems()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import BulkDiscount
        schema = BulkDiscount()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/discount/v1.0/company/{self._conf.companyId}/job/{id}/items/", """{"required":[{"name":"company_id","in":"path","description":"A `company_id` is the unique identifier of the company.","required":true,"schema":{"type":"integer"}},{"name":"id","in":"path","description":"Job ID of the discount.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"A `company_id` is the unique identifier of the company.","required":true,"schema":{"type":"integer"}},{"name":"id","in":"path","description":"Job ID of the discount.","required":true,"schema":{"type":"string"}}]}""", id=id)
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/discount/v1.0/company/{self._conf.companyId}/job/{id}/items/", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def validateDiscountFile(self, discount=None, body=""):
        """Validate File.
        :param discount : discount : type string
        """
        payload = {}
        
        if discount:
            payload["discount"] = discount
        

        # Parameter validation
        schema = DiscountValidator.validateDiscountFile()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import DiscountJob
        schema = DiscountJob()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/discount/v1.0/company/{self._conf.companyId}/file/validation/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[{"name":"discount","in":"query","description":"discount","required":false,"schema":{"type":"string"}}],"query":[{"name":"discount","in":"query","description":"discount","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}}]}""", discount=discount)
        query_string = await create_query_string(discount=discount)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/discount/v1.0/company/{self._conf.companyId}/file/validation/", discount=discount), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def downloadDiscountFile(self, type=None, body=""):
        """Validate File.
        :param type : type : type string
        """
        payload = {}
        
        if type:
            payload["type"] = type
        

        # Parameter validation
        schema = DiscountValidator.downloadDiscountFile()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import DownloadFileJob
        schema = DownloadFileJob()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/discount/v1.0/company/{self._conf.companyId}/file/{type}/download/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"type","in":"path","description":"type","required":true,"schema":{"type":"string","enum":["product","inventory"]}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"type","in":"path","description":"type","required":true,"schema":{"type":"string","enum":["product","inventory"]}}]}""", type=type)
        query_string = await create_query_string(type=type)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/discount/v1.0/company/{self._conf.companyId}/file/{type}/download/", type=type), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
    async def getValidationJob(self, id=None):
        """Validate File Job.
        :param id : id : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = DiscountValidator.getValidationJob()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/discount/v1.0/company/{self._conf.companyId}/file/validation/{id}/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"id","in":"path","description":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"id","in":"path","description":"id","required":true,"schema":{"type":"string"}}]}""", id=id)
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/discount/v1.0/company/{self._conf.companyId}/file/validation/{id}/", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def cancelValidationJob(self, id=None):
        """Cancel Validation Job.
        :param id : id : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = DiscountValidator.cancelValidationJob()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/discount/v1.0/company/{self._conf.companyId}/file/validation/{id}/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"id","in":"path","description":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"id","in":"path","description":"id","required":true,"schema":{"type":"string"}}]}""", id=id)
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
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/discount/v1.0/company/{self._conf.companyId}/file/validation/{id}/", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def getDownloadJob(self, id=None):
        """Download File Job.
        :param id : id : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = DiscountValidator.getDownloadJob()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/discount/v1.0/company/{self._conf.companyId}/file/download/{id}/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"id","in":"path","description":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"id","in":"path","description":"id","required":true,"schema":{"type":"string"}}]}""", id=id)
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/discount/v1.0/company/{self._conf.companyId}/file/download/{id}/", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
    async def cancelDownloadJob(self, id=None):
        """Cancel Download Job.
        :param id : id : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = DiscountValidator.cancelDownloadJob()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/discount/v1.0/company/{self._conf.companyId}/file/download/{id}/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"id","in":"path","description":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"id","in":"path","description":"id","required":true,"schema":{"type":"string"}}]}""", id=id)
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
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/discount/v1.0/company/{self._conf.companyId}/file/download/{id}/", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    

