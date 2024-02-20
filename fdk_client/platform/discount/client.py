"""Discount Platform Client"""
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..PlatformConfig import PlatformConfig

from .validator import DiscountValidator

class Discount:
    def __init__(self, config: PlatformConfig):
        self._conf = config

    
    async def getDiscounts(self, view=None, q=None, page_no=None, page_size=None, archived=None, month=None, year=None, type=None, app_ids=None, request_headers:Dict={}):
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
        
        if view is not None:
            payload["view"] = view
        if q is not None:
            payload["q"] = q
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if archived is not None:
            payload["archived"] = archived
        if month is not None:
            payload["month"] = month
        if year is not None:
            payload["year"] = year
        if type is not None:
            payload["type"] = type
        if app_ids is not None:
            payload["app_ids"] = app_ids

        # Parameter validation
        schema = DiscountValidator.getDiscounts()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/discount/v1.0/company/{self._conf.companyId}/job/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"},"examples":{"400":{"value":90},"success_basic":{"value":90},"success_custom":{"value":90}}}],"optional":[{"name":"view","in":"query","description":"listing or calender.  Default is listing.","required":false,"schema":{"type":"string","enum":["listing","calender"]},"examples":{"400":{"value":"test"}}},{"name":"q","in":"query","description":"The search query. This can be a partial or complete name of a discount.","required":false,"schema":{"type":"string"},"examples":{"400":{"value":"Contract Test Custom"},"success_basic":{"value":"Contract Test Basic"},"success_custom":{"value":"Contract Test Custom"}}},{"name":"page_no","in":"query","description":"page number. Default is 1.","required":false,"schema":{"type":"integer"},"examples":{"400":{"value":1},"success_basic":{"value":1},"success_custom":{"value":1}}},{"name":"page_size","in":"query","description":"page size. Default is 12.","required":false,"schema":{"type":"integer"},"examples":{"400":{"value":10},"success_basic":{"value":10},"success_custom":{"value":10}}},{"name":"archived","in":"query","description":"archived. Default is false.","required":false,"schema":{"type":"boolean","enum":[true,false]}},{"name":"month","in":"query","description":"month. Default is current month.","required":false,"schema":{"type":"integer"},"examples":{"400":{"value":1},"success_basic":{"value":1},"success_custom":{"value":1}}},{"name":"year","in":"query","description":"year. Default is current year.","required":false,"schema":{"type":"integer"},"examples":{"400":{"value":2090},"success_basic":{"value":2090},"success_custom":{"value":2090}}},{"name":"type","in":"query","description":"basic or custom.","required":false,"schema":{"type":"string"},"examples":{"400":{"value":"basic"},"success_basic":{"value":"basic"},"success_custom":{"value":"custom"}}},{"name":"app_ids","in":"query","description":"application ids.","required":false,"schema":{"type":"array","items":{"type":"string"}},"examples":{"400":{"value":["646f43ee3b7f8c2847e31fb0"]},"success_basic":{"value":["646f43ee3b7f8c2847e31fb0"]},"success_custom":{"value":["646f43ee3b7f8c2847e31fb0"]}}}],"query":[{"name":"view","in":"query","description":"listing or calender.  Default is listing.","required":false,"schema":{"type":"string","enum":["listing","calender"]},"examples":{"400":{"value":"test"}}},{"name":"q","in":"query","description":"The search query. This can be a partial or complete name of a discount.","required":false,"schema":{"type":"string"},"examples":{"400":{"value":"Contract Test Custom"},"success_basic":{"value":"Contract Test Basic"},"success_custom":{"value":"Contract Test Custom"}}},{"name":"page_no","in":"query","description":"page number. Default is 1.","required":false,"schema":{"type":"integer"},"examples":{"400":{"value":1},"success_basic":{"value":1},"success_custom":{"value":1}}},{"name":"page_size","in":"query","description":"page size. Default is 12.","required":false,"schema":{"type":"integer"},"examples":{"400":{"value":10},"success_basic":{"value":10},"success_custom":{"value":10}}},{"name":"archived","in":"query","description":"archived. Default is false.","required":false,"schema":{"type":"boolean","enum":[true,false]}},{"name":"month","in":"query","description":"month. Default is current month.","required":false,"schema":{"type":"integer"},"examples":{"400":{"value":1},"success_basic":{"value":1},"success_custom":{"value":1}}},{"name":"year","in":"query","description":"year. Default is current year.","required":false,"schema":{"type":"integer"},"examples":{"400":{"value":2090},"success_basic":{"value":2090},"success_custom":{"value":2090}}},{"name":"type","in":"query","description":"basic or custom.","required":false,"schema":{"type":"string"},"examples":{"400":{"value":"basic"},"success_basic":{"value":"basic"},"success_custom":{"value":"custom"}}},{"name":"app_ids","in":"query","description":"application ids.","required":false,"schema":{"type":"array","items":{"type":"string"}},"examples":{"400":{"value":["646f43ee3b7f8c2847e31fb0"]},"success_basic":{"value":["646f43ee3b7f8c2847e31fb0"]},"success_custom":{"value":["646f43ee3b7f8c2847e31fb0"]}}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"},"examples":{"400":{"value":90},"success_basic":{"value":90},"success_custom":{"value":90}}}]}""", view=view, q=q, page_no=page_no, page_size=page_size, archived=archived, month=month, year=year, type=type, app_ids=app_ids)
        query_string = await create_query_string(view=view, q=q, page_no=page_no, page_size=page_size, archived=archived, month=month, year=year, type=type, app_ids=app_ids)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/discount/v1.0/company/{self._conf.companyId}/job/", view=view, q=q, page_no=page_no, page_size=page_size, archived=archived, month=month, year=year, type=type, app_ids=app_ids), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import ListOrCalender
            schema = ListOrCalender()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getDiscounts")
                print(e)

        return response
    
    async def createDiscount(self, body="", request_headers:Dict={}):
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/discount/v1.0/company/{self._conf.companyId}/job/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"},"examples":{"400":{"value":90},"success_basic":{"value":90},"success_custom":{"value":90}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"},"examples":{"400":{"value":90},"success_basic":{"value":90},"success_custom":{"value":90}}}]}""", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/discount/v1.0/company/{self._conf.companyId}/job/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import DiscountJob
            schema = DiscountJob()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createDiscount")
                print(e)

        return response
    
    async def getDiscount(self, id=None, request_headers:Dict={}):
        """Fetch discount.
        :param id : unique id. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = DiscountValidator.getDiscount()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/discount/v1.0/company/{self._conf.companyId}/job/{id}/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"},"examples":{"400":{"value":90},"success_basic":{"value":90},"success_custom":{"value":90}}},{"name":"id","in":"path","description":"unique id.","required":true,"schema":{"type":"string"},"examples":{"400":{"value":"test"},"success_basic":{"value":"64a7c915c160922f34ba4f12"},"success_custom":{"value":"62c538dd6c0f710007ac6dbf"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"},"examples":{"400":{"value":90},"success_basic":{"value":90},"success_custom":{"value":90}}},{"name":"id","in":"path","description":"unique id.","required":true,"schema":{"type":"string"},"examples":{"400":{"value":"test"},"success_basic":{"value":"64a7c915c160922f34ba4f12"},"success_custom":{"value":"62c538dd6c0f710007ac6dbf"}}}]}""", id=id)
        query_string = await create_query_string(id=id)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/discount/v1.0/company/{self._conf.companyId}/job/{id}/", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import DiscountJob
            schema = DiscountJob()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getDiscount")
                print(e)

        return response
    
    async def updateDiscount(self, id=None, body="", request_headers:Dict={}):
        """Update Discount.
        :param id : id : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = DiscountValidator.updateDiscount()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateUpdateDiscount
        schema = CreateUpdateDiscount()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/discount/v1.0/company/{self._conf.companyId}/job/{id}/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"},"examples":{"400":{"value":90},"success_basic":{"value":90},"success_custom":{"value":90}}},{"name":"id","in":"path","description":"id","required":true,"schema":{"type":"string"},"examples":{"400":{"value":"62c538dd6c0f710007ac6dbf"},"success_basic":{"value":"64a7c915c160922f34ba4f12"},"success_custom":{"value":"62c538dd6c0f710007ac6dbf"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"},"examples":{"400":{"value":90},"success_basic":{"value":90},"success_custom":{"value":90}}},{"name":"id","in":"path","description":"id","required":true,"schema":{"type":"string"},"examples":{"400":{"value":"62c538dd6c0f710007ac6dbf"},"success_basic":{"value":"64a7c915c160922f34ba4f12"},"success_custom":{"value":"62c538dd6c0f710007ac6dbf"}}}]}""", id=id)
        query_string = await create_query_string(id=id)

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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/discount/v1.0/company/{self._conf.companyId}/job/{id}/", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import DiscountJob
            schema = DiscountJob()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateDiscount")
                print(e)

        return response
    
    async def upsertDiscountItems(self, id=None, body="", request_headers:Dict={}):
        """Create custom discounts through API.
        :param id : Job ID of the discount. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = DiscountValidator.upsertDiscountItems()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import BulkDiscount
        schema = BulkDiscount()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/discount/v1.0/company/{self._conf.companyId}/job/{id}/items/", """{"required":[{"name":"company_id","in":"path","description":"A `company_id` is the unique identifier of the company.","required":true,"schema":{"type":"integer"},"examples":{"400":{"value":90},"success_product":{"value":90},"success_inventory":{"value":90}}},{"name":"id","in":"path","description":"Job ID of the discount.","required":true,"schema":{"type":"string"},"examples":{"400":{"value":"64a7c915c160922f34ba4f12"},"success_product":{"value":"603f54c3f6f7fd000925925b"},"success_inventory":{"value":"6040f016099e3a0009fe591e"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"A `company_id` is the unique identifier of the company.","required":true,"schema":{"type":"integer"},"examples":{"400":{"value":90},"success_product":{"value":90},"success_inventory":{"value":90}}},{"name":"id","in":"path","description":"Job ID of the discount.","required":true,"schema":{"type":"string"},"examples":{"400":{"value":"64a7c915c160922f34ba4f12"},"success_product":{"value":"603f54c3f6f7fd000925925b"},"success_inventory":{"value":"6040f016099e3a0009fe591e"}}}]}""", id=id)
        query_string = await create_query_string(id=id)

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/discount/v1.0/company/{self._conf.companyId}/job/{id}/items/", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        return response
    
    async def validateDiscountFile(self, discount=None, body="", request_headers:Dict={}):
        """Validate File.
        :param discount : discount : type string
        """
        payload = {}
        
        if discount is not None:
            payload["discount"] = discount

        # Parameter validation
        schema = DiscountValidator.validateDiscountFile()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import FileJobRequest
        schema = FileJobRequest()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/discount/v1.0/company/{self._conf.companyId}/file/validation/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"},"examples":{"400":{"value":90},"success":{"value":"90"}}}],"optional":[{"name":"discount","in":"query","description":"discount","required":false,"schema":{"type":"string"},"examples":{"400":{"value":"6512735aa98e0ed14ef1f1fd"},"success":{"value":"6512735aa98e0ed14ef1f1fd"}}}],"query":[{"name":"discount","in":"query","description":"discount","required":false,"schema":{"type":"string"},"examples":{"400":{"value":"6512735aa98e0ed14ef1f1fd"},"success":{"value":"6512735aa98e0ed14ef1f1fd"}}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"},"examples":{"400":{"value":90},"success":{"value":"90"}}}]}""", discount=discount)
        query_string = await create_query_string(discount=discount)

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/discount/v1.0/company/{self._conf.companyId}/file/validation/", discount=discount), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import FileJobResponse
            schema = FileJobResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for validateDiscountFile")
                print(e)

        return response
    
    async def downloadDiscountFile(self, type=None, body="", request_headers:Dict={}):
        """Validate File.
        :param type : type : type string
        """
        payload = {}
        
        if type is not None:
            payload["type"] = type

        # Parameter validation
        schema = DiscountValidator.downloadDiscountFile()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import DownloadFileJob
        schema = DownloadFileJob()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/discount/v1.0/company/{self._conf.companyId}/file/{type}/download/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"},"examples":{"400":{"value":90},"success":{"value":90}}},{"name":"type","in":"path","description":"type","required":true,"schema":{"type":"string","enum":["product","inventory"]},"examples":{"400":{"value":"test"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"},"examples":{"400":{"value":90},"success":{"value":90}}},{"name":"type","in":"path","description":"type","required":true,"schema":{"type":"string","enum":["product","inventory"]},"examples":{"400":{"value":"test"}}}]}""", type=type)
        query_string = await create_query_string(type=type)

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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/discount/v1.0/company/{self._conf.companyId}/file/{type}/download/", type=type), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        if 200 <= int(response['status_code']) < 300:
            from .models import FileJobResponse
            schema = FileJobResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for downloadDiscountFile")
                print(e)

        return response
    
    async def getValidationJob(self, id=None, request_headers:Dict={}):
        """Validate File Job.
        :param id : id : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = DiscountValidator.getValidationJob()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/discount/v1.0/company/{self._conf.companyId}/file/validation/{id}/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"},"examples":{"400":{"value":90},"success":{"value":90}}},{"name":"id","in":"path","description":"id","required":true,"schema":{"type":"string"},"examples":{"400":{"value":"652b7d4fd25ec5b4acd798c1"},"success":{"value":"6519669e7fc0cd03ce111ab9"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"},"examples":{"400":{"value":90},"success":{"value":90}}},{"name":"id","in":"path","description":"id","required":true,"schema":{"type":"string"},"examples":{"400":{"value":"652b7d4fd25ec5b4acd798c1"},"success":{"value":"6519669e7fc0cd03ce111ab9"}}}]}""", id=id)
        query_string = await create_query_string(id=id)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/discount/v1.0/company/{self._conf.companyId}/file/validation/{id}/", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import FileJobResponse
            schema = FileJobResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getValidationJob")
                print(e)

        return response
    
    async def cancelValidationJob(self, id=None, request_headers:Dict={}):
        """Cancel Validation Job.
        :param id : id : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = DiscountValidator.cancelValidationJob()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/discount/v1.0/company/{self._conf.companyId}/file/validation/{id}/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"},"examples":{"400":{"value":90},"success":{"value":90}}},{"name":"id","in":"path","description":"id","required":true,"schema":{"type":"string"},"examples":{"400":{"value":"652b7d4fd25ec5b4acd798c1"},"success":{"value":"6519669e7fc0cd03ce111ab9"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"},"examples":{"400":{"value":90},"success":{"value":90}}},{"name":"id","in":"path","description":"id","required":true,"schema":{"type":"string"},"examples":{"400":{"value":"652b7d4fd25ec5b4acd798c1"},"success":{"value":"6519669e7fc0cd03ce111ab9"}}}]}""", id=id)
        query_string = await create_query_string(id=id)

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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/discount/v1.0/company/{self._conf.companyId}/file/validation/{id}/", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import CancelJobResponse
            schema = CancelJobResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for cancelValidationJob")
                print(e)

        return response
    
    async def getDownloadJob(self, id=None, request_headers:Dict={}):
        """Download File Job.
        :param id : id : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = DiscountValidator.getDownloadJob()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/discount/v1.0/company/{self._conf.companyId}/file/download/{id}/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"},"examples":{"400":{"value":90},"success":{"value":90}}},{"name":"id","in":"path","description":"id","required":true,"schema":{"type":"string"},"examples":{"400":{"value":"test"},"success":{"value":"651b00ef29aedf98f98a8cbd"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"},"examples":{"400":{"value":90},"success":{"value":90}}},{"name":"id","in":"path","description":"id","required":true,"schema":{"type":"string"},"examples":{"400":{"value":"test"},"success":{"value":"651b00ef29aedf98f98a8cbd"}}}]}""", id=id)
        query_string = await create_query_string(id=id)

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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/discount/v1.0/company/{self._conf.companyId}/file/download/{id}/", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import FileJobResponse
            schema = FileJobResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getDownloadJob")
                print(e)

        return response
    
    async def cancelDownloadJob(self, id=None, request_headers:Dict={}):
        """Cancel Download Job.
        :param id : id : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = DiscountValidator.cancelDownloadJob()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/discount/v1.0/company/{self._conf.companyId}/file/download/{id}/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"},"examples":{"400":{"value":1},"success":{"value":1}}},{"name":"id","in":"path","description":"id","required":true,"schema":{"type":"string"},"examples":{"400":{"value":"test"},"success":{"value":"651b00ef29aedf98f98a8cbd"}}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"},"examples":{"400":{"value":1},"success":{"value":1}}},{"name":"id","in":"path","description":"id","required":true,"schema":{"type":"string"},"examples":{"400":{"value":"test"},"success":{"value":"651b00ef29aedf98f98a8cbd"}}}]}""", id=id)
        query_string = await create_query_string(id=id)

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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/discount/v1.0/company/{self._conf.companyId}/file/download/{id}/", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        if 200 <= int(response['status_code']) < 300:
            from .models import CancelJobResponse
            schema = CancelJobResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for cancelDownloadJob")
                print(e)

        return response
    