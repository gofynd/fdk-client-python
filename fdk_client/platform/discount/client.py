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
        """Retrieve a list of discounts. You can also retrieve discounts using filter query parameters. There are additional optional parameters that can be specified in the parameters of the request when retrieving discount
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
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/discount/v1.0/company/{self._conf.companyId}/job/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[{"name":"view","in":"query","description":"listing or calender.  Default is listing.","required":false,"schema":{"type":"string","enum":["listing","calender"]}},{"name":"q","in":"query","description":"The search query. This can be a partial or complete name of a discount.","required":false,"schema":{"type":"string"}},{"name":"page_no","in":"query","description":"page number. Default is 1.","required":false,"schema":{"type":"integer"}},{"name":"page_size","in":"query","description":"page size. Default is 12.","required":false,"schema":{"type":"integer"}},{"name":"archived","in":"query","description":"archived. Default is false.","required":false,"schema":{"type":"boolean","enum":[true,false]}},{"name":"month","in":"query","description":"month. Default is current month.","required":false,"schema":{"type":"integer"}},{"name":"year","in":"query","description":"year. Default is current year.","required":false,"schema":{"type":"integer"}},{"name":"type","in":"query","description":"basic or custom.","required":false,"schema":{"type":"string"}},{"name":"app_ids","in":"query","description":"application ids.","required":false,"schema":{"type":"array","items":{"type":"string"}}}],"query":[{"name":"view","in":"query","description":"listing or calender.  Default is listing.","required":false,"schema":{"type":"string","enum":["listing","calender"]}},{"name":"q","in":"query","description":"The search query. This can be a partial or complete name of a discount.","required":false,"schema":{"type":"string"}},{"name":"page_no","in":"query","description":"page number. Default is 1.","required":false,"schema":{"type":"integer"}},{"name":"page_size","in":"query","description":"page size. Default is 12.","required":false,"schema":{"type":"integer"}},{"name":"archived","in":"query","description":"archived. Default is false.","required":false,"schema":{"type":"boolean","enum":[true,false]}},{"name":"month","in":"query","description":"month. Default is current month.","required":false,"schema":{"type":"integer"}},{"name":"year","in":"query","description":"year. Default is current year.","required":false,"schema":{"type":"integer"}},{"name":"type","in":"query","description":"basic or custom.","required":false,"schema":{"type":"string"}},{"name":"app_ids","in":"query","description":"application ids.","required":false,"schema":{"type":"array","items":{"type":"string"}}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", view=view, q=q, page_no=page_no, page_size=page_size, archived=archived, month=month, year=year, type=type, app_ids=app_ids)
        query_string = await create_query_string(view=view, q=q, page_no=page_no, page_size=page_size, archived=archived, month=month, year=year, type=type, app_ids=app_ids)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/discount/v1.0/company/{self._conf.companyId}/job/", view=view, q=q, page_no=page_no, page_size=page_size, archived=archived, month=month, year=year, type=type, app_ids=app_ids), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

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
        """Creates a discount. There are additional optional parameters that can be specified in the body of the request when creating a discount
        """
        payload = {}
        

        # Parameter validation
        schema = DiscountValidator.createDiscount()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CreateUpdateDiscount
        schema = CreateUpdateDiscount()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/discount/v1.0/company/{self._conf.companyId}/job/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/discount/v1.0/company/{self._conf.companyId}/job/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

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
        """Retrieve a single discount by its id.
        :param id : unique id. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = DiscountValidator.getDiscount()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/discount/v1.0/company/{self._conf.companyId}/job/{id}/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"id","in":"path","description":"unique id.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"id","in":"path","description":"unique id.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/discount/v1.0/company/{self._conf.companyId}/job/{id}/", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

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
        """Update an existing discount by its id. Discount can only be updated after 5 min from last updated time stamp (modified_on).
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/discount/v1.0/company/{self._conf.companyId}/job/{id}/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"id","in":"path","description":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"id","in":"path","description":"id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/discount/v1.0/company/{self._conf.companyId}/job/{id}/", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

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
        """Enables users to create custom discounts in bulk by providing the multiple products in requestBody. It allows for the efficient creation of multiple discounts simultaneously, streamlining the discount management process.
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/discount/v1.0/company/{self._conf.companyId}/job/{id}/items/", """{"required":[{"name":"company_id","in":"path","description":"A `company_id` is the unique identifier of the company.","required":true,"schema":{"type":"integer"}},{"name":"id","in":"path","description":"Job ID of the discount.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"A `company_id` is the unique identifier of the company.","required":true,"schema":{"type":"integer"}},{"name":"id","in":"path","description":"Job ID of the discount.","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/discount/v1.0/company/{self._conf.companyId}/job/{id}/items/", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        return response
    
    async def validateDiscountFile(self, discount=None, body="", request_headers:Dict={}):
        """Validates the discount file for any discrepancies. like item should be valid etc..
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/discount/v1.0/company/{self._conf.companyId}/file/validation/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}}],"optional":[{"name":"discount","in":"query","description":"discount","required":false,"schema":{"type":"string"}}],"query":[{"name":"discount","in":"query","description":"discount","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}}]}""", serverType="platform", discount=discount)
        query_string = await create_query_string(discount=discount)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/discount/v1.0/company/{self._conf.companyId}/file/validation/", discount=discount), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

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
        """Retrieve a discount file by its type, it could be product or inventory.
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

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/discount/v1.0/company/{self._conf.companyId}/file/{type}/download/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"type","in":"path","description":"type","required":true,"schema":{"type":"string","enum":["product","inventory"]}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"type","in":"path","description":"type","required":true,"schema":{"type":"string","enum":["product","inventory"]}}]}""", serverType="platform", type=type)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/discount/v1.0/company/{self._conf.companyId}/file/{type}/download/", type=type), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

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
        """Retrieve a validation job of a discount by its id.
        :param id : id : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = DiscountValidator.getValidationJob()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/discount/v1.0/company/{self._conf.companyId}/file/validation/{id}/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"id","in":"path","description":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"id","in":"path","description":"id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/discount/v1.0/company/{self._conf.companyId}/file/validation/{id}/", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

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
        """Cancel validation job of a discount by its id.
        :param id : id : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = DiscountValidator.cancelValidationJob()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/discount/v1.0/company/{self._conf.companyId}/file/validation/{id}/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"id","in":"path","description":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"id","in":"path","description":"id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/discount/v1.0/company/{self._conf.companyId}/file/validation/{id}/", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

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
        """Retrieve a discount download job by its id.
        :param id : id : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = DiscountValidator.getDownloadJob()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/discount/v1.0/company/{self._conf.companyId}/file/download/{id}/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"id","in":"path","description":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"id","in":"path","description":"id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/discount/v1.0/company/{self._conf.companyId}/file/download/{id}/", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

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
        """Cancel a discount download job by its id.
        :param id : id : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = DiscountValidator.cancelDownloadJob()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/discount/v1.0/company/{self._conf.companyId}/file/download/{id}/", """{"required":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"id","in":"path","description":"id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"company_id","in":"path","description":"company_id","required":true,"schema":{"type":"integer"}},{"name":"id","in":"path","description":"id","required":true,"schema":{"type":"string"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/discount/v1.0/company/{self._conf.companyId}/file/download/{id}/", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CancelJobResponse
            schema = CancelJobResponse()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for cancelDownloadJob")
                print(e)

        return response
    