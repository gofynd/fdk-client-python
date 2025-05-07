"""Cart Platform Client"""
from typing import Dict

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain
from ..PlatformConfig import PlatformConfig

from .applicationValidator import CartValidator

class Cart:
    def __init__(self, config: PlatformConfig, applicationId: str):
        self._conf = config
        self.applicationId = applicationId

    
    async def createCoupon(self, body="", request_headers:Dict={}):
        """Generate and add a new coupon to the cart.
        """
        payload = {}
        

        # Parameter validation
        schema = CartValidator.createCoupon()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CouponAdd
        schema = CouponAdd()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/coupon", """{"required":[{"in":"path","description":"Current company id","schema":{"type":"string"},"required":true,"name":"company_id"},{"in":"path","description":"Current Application _id","schema":{"type":"string"},"required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","description":"Current company id","schema":{"type":"string"},"required":true,"name":"company_id"},{"in":"path","description":"Current Application _id","schema":{"type":"string"},"required":true,"name":"application_id"}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/coupon", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CouponDetailResponseObject
            schema = CouponDetailResponseObject()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createCoupon")
                print(e)

        return response
    
    async def getCoupons(self, page_no=None, page_size=None, is_archived=None, title=None, is_public=None, is_display=None, type_slug=None, code=None, request_headers:Dict={}):
        """Retrieve a list of all created coupons for specific sales channel. It also supports searching based on text search, pagination and other flags to filter coupons.
        :param page_no :  : type integer
        :param page_size :  : type integer
        :param is_archived :  : type boolean
        :param title :  : type string
        :param is_public :  : type boolean
        :param is_display :  : type boolean
        :param type_slug :  : type string
        :param code :  : type string
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if is_archived is not None:
            payload["is_archived"] = is_archived
        if title is not None:
            payload["title"] = title
        if is_public is not None:
            payload["is_public"] = is_public
        if is_display is not None:
            payload["is_display"] = is_display
        if type_slug is not None:
            payload["type_slug"] = type_slug
        if code is not None:
            payload["code"] = code

        # Parameter validation
        schema = CartValidator.getCoupons()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/coupon", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer","default":0,"description":"current page no as per pagination"}},{"name":"page_size","in":"query","schema":{"type":"integer","default":10,"description":"Coupon max records fetched in single request"}},{"name":"is_archived","in":"query","schema":{"type":"boolean","description":"Filter by active or inactive coupon","default":false}},{"name":"title","in":"query","schema":{"type":"string","description":"Filter by `title`"}},{"name":"is_public","in":"query","schema":{"type":"boolean","description":"Filter by `is_public`"}},{"name":"is_display","in":"query","schema":{"type":"boolean","description":"Filter by `is_display`"}},{"name":"type_slug","in":"query","schema":{"type":"string","description":"Filter by coupon type"}},{"name":"code","in":"query","schema":{"type":"string","description":"Filter by `code`"}}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer","default":0,"description":"current page no as per pagination"}},{"name":"page_size","in":"query","schema":{"type":"integer","default":10,"description":"Coupon max records fetched in single request"}},{"name":"is_archived","in":"query","schema":{"type":"boolean","description":"Filter by active or inactive coupon","default":false}},{"name":"title","in":"query","schema":{"type":"string","description":"Filter by `title`"}},{"name":"is_public","in":"query","schema":{"type":"boolean","description":"Filter by `is_public`"}},{"name":"is_display","in":"query","schema":{"type":"boolean","description":"Filter by `is_display`"}},{"name":"type_slug","in":"query","schema":{"type":"string","description":"Filter by coupon type"}},{"name":"code","in":"query","schema":{"type":"string","description":"Filter by `code`"}}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}]}""", serverType="platform", page_no=page_no, page_size=page_size, is_archived=is_archived, title=title, is_public=is_public, is_display=is_display, type_slug=type_slug, code=code)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, is_archived=is_archived, title=title, is_public=is_public, is_display=is_display, type_slug=type_slug, code=code)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/coupon", page_no=page_no, page_size=page_size, is_archived=is_archived, title=title, is_public=is_public, is_display=is_display, type_slug=type_slug, code=code), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CouponsResponseObject
            schema = CouponsResponseObject()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCoupons")
                print(e)

        return response
    
    async def getCouponTags(self, request_headers:Dict={}):
        """This API helps to get coupon tags data associated to a particular application.
        """
        payload = {}
        

        # Parameter validation
        schema = CartValidator.getCouponTags()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/coupon-tags", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"integer"},"description":"ID of the application for which tags are to be fetched.","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"integer"},"description":"ID of the application for which tags are to be fetched.","in":"path","required":true,"name":"application_id"}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/coupon-tags", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import TagsViewResponseObject
            schema = TagsViewResponseObject()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCouponTags")
                print(e)

        return response
    
    async def getPromotionTags(self, request_headers:Dict={}):
        """This API helps to get Promotion tags data associated to a particular application.
        """
        payload = {}
        

        # Parameter validation
        schema = CartValidator.getPromotionTags()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/promo-tags", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"integer"},"description":"ID of the application for which tags are to be fetched.","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"integer"},"description":"ID of the application for which tags are to be fetched.","in":"path","required":true,"name":"application_id"}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/promo-tags", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import TagsViewResponseObject
            schema = TagsViewResponseObject()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPromotionTags")
                print(e)

        return response
    
    async def getCouponById(self, id=None, request_headers:Dict={}):
        """Retrieve details of a specific coupon by providing its unique identifier to obtain information such as coupon type, rules, validity period and other related information.
        :param id :  : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CartValidator.getCouponById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/coupon/{id}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"name":"id","in":"path","required":true,"schema":{"type":"string","description":"Coupon mongo _id for fetching single coupon data for editing"}}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"name":"id","in":"path","required":true,"schema":{"type":"string","description":"Coupon mongo _id for fetching single coupon data for editing"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/coupon/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CouponUpdate
            schema = CouponUpdate()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCouponById")
                print(e)

        return response
    
    async def updateCoupon(self, id=None, body="", request_headers:Dict={}):
        """Update the details of an existing coupon by specifying its unique identifier. This includes modifying coupon attributes such as discount percentage, validity period, and associated conditions. Leveraging this functionality allows businesses to quickly adapt their promotional strategies to changing market dynamics.
        :param id :  : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CartValidator.updateCoupon()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CouponUpdate
        schema = CouponUpdate()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/coupon/{id}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"name":"id","in":"path","schema":{"type":"string","description":"Coupon mongo _id for fetching single coupon data for editing"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"name":"id","in":"path","schema":{"type":"string","description":"Coupon mongo _id for fetching single coupon data for editing"},"required":true}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/coupon/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CouponDetailResponseObject
            schema = CouponDetailResponseObject()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateCoupon")
                print(e)

        return response
    
    async def updateCouponPartially(self, id=None, body="", request_headers:Dict={}):
        """Seller can make partial adjustments of an existing coupon by specifying its unique identifier. It enables businesses to modify specific attributes of the coupon while preserving other details intact.
        :param id :  : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CartValidator.updateCouponPartially()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CouponPartialUpdate
        schema = CouponPartialUpdate()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/coupon/{id}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"name":"id","in":"path","schema":{"type":"string","description":"Coupon mongo _id for fetching single coupon data for editing"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"name":"id","in":"path","schema":{"type":"string","description":"Coupon mongo _id for fetching single coupon data for editing"},"required":true}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/coupon/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SuccessMessage
            schema = SuccessMessage()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateCouponPartially")
                print(e)

        return response
    
    async def getPromotions(self, page_no=None, page_size=None, q=None, is_active=None, promo_group=None, promotion_type=None, fp_panel=None, promotion_id=None, request_headers:Dict={}):
        """Retrieve a list of all created promotions for specific sales channel. It also supports efficient text search and pagination functionalities, ensuring optimized promotion listing for streamlined navigation and management.
        :param page_no :  : type integer
        :param page_size :  : type integer
        :param q :  : type string
        :param is_active :  : type boolean
        :param promo_group :  : type string
        :param promotion_type :  : type string
        :param fp_panel :  : type string
        :param promotion_id :  : type string
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if q is not None:
            payload["q"] = q
        if is_active is not None:
            payload["is_active"] = is_active
        if promo_group is not None:
            payload["promo_group"] = promo_group
        if promotion_type is not None:
            payload["promotion_type"] = promotion_type
        if fp_panel is not None:
            payload["fp_panel"] = fp_panel
        if promotion_id is not None:
            payload["promotion_id"] = promotion_id

        # Parameter validation
        schema = CartValidator.getPromotions()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/promotion", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer","default":0,"description":"current page no as per pagination"}},{"name":"page_size","in":"query","schema":{"type":"integer","default":10,"description":"Promotion max records fetched in single request"}},{"name":"q","in":"query","schema":{"type":"string","description":"Filter by name"}},{"name":"is_active","in":"query","schema":{"type":"boolean","description":"Filter by active or inactive promotion","default":true}},{"name":"promo_group","in":"query","schema":{"type":"string","description":"Filter promotion group","enum":["product","cart","contract","ladder_price","limited_timer"]}},{"name":"promotion_type","in":"query","schema":{"type":"string","description":"Filter promotion type","x-not-enum":true}},{"name":"fp_panel","in":"query","schema":{"type":"string","description":"Filter non extension promotions"}},{"name":"promotion_id","in":"query","schema":{"type":"string","description":"Filter by promotion _id"}}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer","default":0,"description":"current page no as per pagination"}},{"name":"page_size","in":"query","schema":{"type":"integer","default":10,"description":"Promotion max records fetched in single request"}},{"name":"q","in":"query","schema":{"type":"string","description":"Filter by name"}},{"name":"is_active","in":"query","schema":{"type":"boolean","description":"Filter by active or inactive promotion","default":true}},{"name":"promo_group","in":"query","schema":{"type":"string","description":"Filter promotion group","enum":["product","cart","contract","ladder_price","limited_timer"]}},{"name":"promotion_type","in":"query","schema":{"type":"string","description":"Filter promotion type","x-not-enum":true}},{"name":"fp_panel","in":"query","schema":{"type":"string","description":"Filter non extension promotions"}},{"name":"promotion_id","in":"query","schema":{"type":"string","description":"Filter by promotion _id"}}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}]}""", serverType="platform", page_no=page_no, page_size=page_size, q=q, is_active=is_active, promo_group=promo_group, promotion_type=promotion_type, fp_panel=fp_panel, promotion_id=promotion_id)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, q=q, is_active=is_active, promo_group=promo_group, promotion_type=promotion_type, fp_panel=fp_panel, promotion_id=promotion_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/promotion", page_no=page_no, page_size=page_size, q=q, is_active=is_active, promo_group=promo_group, promotion_type=promotion_type, fp_panel=fp_panel, promotion_id=promotion_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PromotionsResponseObject
            schema = PromotionsResponseObject()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPromotions")
                print(e)

        return response
    
    async def createPromotion(self, body="", request_headers:Dict={}):
        """Creates a new promotion based on the selected promotion type. Sellers can choose from multiple supported promotion types, including percentage value, fixed amount value, bundled discount, buy X get Y items, and more, along with customizable promotion criteria to meet specific business requirements.
        """
        payload = {}
        

        # Parameter validation
        schema = CartValidator.createPromotion()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PromotionAdd
        schema = PromotionAdd()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/promotion", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/promotion", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PromotionAddResult
            schema = PromotionAddResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createPromotion")
                print(e)

        return response
    
    async def getPromotionById(self, id=None, request_headers:Dict={}):
        """Retrieve details of a specific promotion by providing its unique identifier to obtain information such as promotion type, rules, validity period and other related information.
        :param id :  : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CartValidator.getPromotionById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/promotion/{id}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"name":"id","in":"path","required":true,"schema":{"type":"string","description":"Promotion mongo _id for fetching single promotion data for editing"}}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"name":"id","in":"path","required":true,"schema":{"type":"string","description":"Promotion mongo _id for fetching single promotion data for editing"}}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/promotion/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PromotionUpdateResult
            schema = PromotionUpdateResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPromotionById")
                print(e)

        return response
    
    async def updatePromotion(self, id=None, body="", request_headers:Dict={}):
        """Update the details of an existing promotion by specifying its unique identifier. This includes modifying promotion attributes such as discount percentage, validity period, and associated conditions. Leveraging this functionality allows businesses to quickly adapt their promotional strategies to changing market dynamics.
        :param id :  : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CartValidator.updatePromotion()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PromotionUpdate
        schema = PromotionUpdate()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/promotion/{id}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"name":"id","in":"path","schema":{"type":"string","description":"Promotion mongo _id for fetching single promotion data for editing"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"name":"id","in":"path","schema":{"type":"string","description":"Promotion mongo _id for fetching single promotion data for editing"},"required":true}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/promotion/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PromotionUpdateResult
            schema = PromotionUpdateResult()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updatePromotion")
                print(e)

        return response
    
    async def updatePromotionPartially(self, id=None, body="", request_headers:Dict={}):
        """Seller can make partial adjustments of an existing promotion by specifying its unique identifier. It enables businesses to modify specific attributes of the promotion while preserving other details intact.
        :param id :  : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CartValidator.updatePromotionPartially()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PromotionPartialUpdate
        schema = PromotionPartialUpdate()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/promotion/{id}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"name":"id","in":"path","schema":{"type":"string","description":"Promotion mongo _id for fetching single promotion data for editing"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"name":"id","in":"path","schema":{"type":"string","description":"Promotion mongo _id for fetching single promotion data for editing"},"required":true}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/promotion/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SuccessMessage
            schema = SuccessMessage()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updatePromotionPartially")
                print(e)

        return response
    
    async def getPromosCouponConfig(self, entity_type=None, is_hidden=None, request_headers:Dict={}):
        """Retrieve the configuration settings related to promotions and coupons for a specific seller. It provides details of the supported types of coupons and promotions along with their descriptions, examples, and related attributes.
        :param entity_type : entity_type as promotion or coupon : type string
        :param is_hidden : promo-coupon config shown or not : type boolean
        """
        payload = {}
        
        if entity_type is not None:
            payload["entity_type"] = entity_type
        if is_hidden is not None:
            payload["is_hidden"] = is_hidden

        # Parameter validation
        schema = CartValidator.getPromosCouponConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/promo-coupons", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}],"optional":[{"name":"entity_type","description":"entity_type as promotion or coupon","in":"query","schema":{"type":"string","enum":["promotion","coupon"]}},{"name":"is_hidden","description":"promo-coupon config shown or not","in":"query","schema":{"type":"boolean"}}],"query":[{"name":"entity_type","description":"entity_type as promotion or coupon","in":"query","schema":{"type":"string","enum":["promotion","coupon"]}},{"name":"is_hidden","description":"promo-coupon config shown or not","in":"query","schema":{"type":"boolean"}}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}]}""", serverType="platform", entity_type=entity_type, is_hidden=is_hidden)
        query_string = await create_query_string(entity_type=entity_type, is_hidden=is_hidden)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/promo-coupons", entity_type=entity_type, is_hidden=is_hidden), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import ActivePromosResponseObject
            schema = ActivePromosResponseObject()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPromosCouponConfig")
                print(e)

        return response
    
    async def getCartMetaConfig(self, cart_meta_id=None, request_headers:Dict={}):
        """Get cart meta configuration by id
        :param cart_meta_id : CartMeta mongo _id for fetching single cart meta data for editing : type string
        """
        payload = {}
        
        if cart_meta_id is not None:
            payload["cart_meta_id"] = cart_meta_id

        # Parameter validation
        schema = CartValidator.getCartMetaConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/cart_configuration/{cart_meta_id}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application id","in":"path","required":true,"name":"application_id"},{"name":"cart_meta_id","in":"path","schema":{"type":"string"},"description":"CartMeta mongo _id for fetching single cart meta data for editing","required":true}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application id","in":"path","required":true,"name":"application_id"},{"name":"cart_meta_id","in":"path","schema":{"type":"string"},"description":"CartMeta mongo _id for fetching single cart meta data for editing","required":true}]}""", serverType="platform", cart_meta_id=cart_meta_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/cart_configuration/{cart_meta_id}", cart_meta_id=cart_meta_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CartMetaConfigDetailObject
            schema = CartMetaConfigDetailObject()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCartMetaConfig")
                print(e)

        return response
    
    async def updateCartMetaConfig(self, cart_meta_id=None, body="", request_headers:Dict={}):
        """Modify the configuration settings for cart metadata.
        :param cart_meta_id : CartMeta mongo _id for fetching single cart meta data for editing : type string
        """
        payload = {}
        
        if cart_meta_id is not None:
            payload["cart_meta_id"] = cart_meta_id

        # Parameter validation
        schema = CartValidator.updateCartMetaConfig()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CartMetaConfigUpdate
        schema = CartMetaConfigUpdate()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/cart_configuration/{cart_meta_id}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"name":"cart_meta_id","in":"path","schema":{"type":"string"},"description":"CartMeta mongo _id for fetching single cart meta data for editing","required":true}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"name":"cart_meta_id","in":"path","schema":{"type":"string"},"description":"CartMeta mongo _id for fetching single cart meta data for editing","required":true}]}""", serverType="platform", cart_meta_id=cart_meta_id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/cart_configuration/{cart_meta_id}", cart_meta_id=cart_meta_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CartMetaConfigUpdate
            schema = CartMetaConfigUpdate()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateCartMetaConfig")
                print(e)

        return response
    
    async def deleteCartMetaConfig(self, cart_meta_id=None, request_headers:Dict={}):
        """Delete cart meta configuration
        :param cart_meta_id : CartMeta mongo _id for fetching single cart meta data for editing : type string
        """
        payload = {}
        
        if cart_meta_id is not None:
            payload["cart_meta_id"] = cart_meta_id

        # Parameter validation
        schema = CartValidator.deleteCartMetaConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/cart_configuration/{cart_meta_id}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"name":"cart_meta_id","in":"path","schema":{"type":"string"},"description":"CartMeta mongo _id for fetching single cart meta data for editing","required":true}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"name":"cart_meta_id","in":"path","schema":{"type":"string"},"description":"CartMeta mongo _id for fetching single cart meta data for editing","required":true}]}""", serverType="platform", cart_meta_id=cart_meta_id)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/cart_configuration/{cart_meta_id}", cart_meta_id=cart_meta_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SuccessMessage
            schema = SuccessMessage()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteCartMetaConfig")
                print(e)

        return response
    
    async def getCartMetaConfigs(self, request_headers:Dict={}):
        """Fetch cart meta configuration
        """
        payload = {}
        

        # Parameter validation
        schema = CartValidator.getCartMetaConfigs()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/cart_configuration", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/cart_configuration", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CartMetaConfigListResponseObject
            schema = CartMetaConfigListResponseObject()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCartMetaConfigs")
                print(e)

        return response
    
    async def createCartMetaConfig(self, body="", request_headers:Dict={}):
        """Create custom meta configurations for carts associated with a specific sales channel. By specifying the company ID and application ID, seller can define unique cart settings, including preferences, rules, and constraints, tailored to their business needs.
        """
        payload = {}
        

        # Parameter validation
        schema = CartValidator.createCartMetaConfig()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CartMetaConfigAdd
        schema = CartMetaConfigAdd()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/cart_configuration", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/cart_configuration", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CartMetaConfigAddResponseObject
            schema = CartMetaConfigAddResponseObject()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for createCartMetaConfig")
                print(e)

        return response
    
    async def addPriceAdjustment(self, body="", request_headers:Dict={}):
        """Create new price adjustment
        """
        payload = {}
        

        # Parameter validation
        schema = CartValidator.addPriceAdjustment()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PriceAdjustmentAdd
        schema = PriceAdjustmentAdd()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/price-adjustment", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/price-adjustment", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AddPriceAdjustmentResponseObject
            schema = AddPriceAdjustmentResponseObject()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for addPriceAdjustment")
                print(e)

        return response
    
    async def getPriceAdjustments(self, cart_id=None, request_headers:Dict={}):
        """This API helps to get price adjustments data associated to a particular cart
        :param cart_id : Cart Id : type string
        """
        payload = {}
        
        if cart_id is not None:
            payload["cart_id"] = cart_id

        # Parameter validation
        schema = CartValidator.getPriceAdjustments()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/price-adjustment", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"schema":{"type":"string"},"description":"Cart Id","in":"query","required":true,"name":"cart_id"}],"optional":[],"query":[{"schema":{"type":"string"},"description":"Cart Id","in":"query","required":true,"name":"cart_id"}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}]}""", serverType="platform", cart_id=cart_id)
        query_string = await create_query_string(cart_id=cart_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/price-adjustment", cart_id=cart_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PriceAdjustmentResponsObject
            schema = PriceAdjustmentResponsObject()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getPriceAdjustments")
                print(e)

        return response
    
    async def updatePriceAdjustment(self, id=None, body="", request_headers:Dict={}):
        """Modify price adjustments for items in the cart.
        :param id :  : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CartValidator.updatePriceAdjustment()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PriceAdjustmentUpdate
        schema = PriceAdjustmentUpdate()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/price-adjustment/{id}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"name":"id","in":"path","schema":{"type":"string","description":"price adjustment id for fetching single price adjustment data for editing"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"name":"id","in":"path","schema":{"type":"string","description":"price adjustment id for fetching single price adjustment data for editing"},"required":true}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/price-adjustment/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import UpdatePriceAdjustmentResponseObject
            schema = UpdatePriceAdjustmentResponseObject()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updatePriceAdjustment")
                print(e)

        return response
    
    async def removePriceAdjustment(self, id=None, request_headers:Dict={}):
        """Remove price adjustments applied to items in the cart.
        :param id :  : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CartValidator.removePriceAdjustment()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/price-adjustment/{id}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"name":"id","in":"path","schema":{"type":"string","description":"Price Adjustment  id for fetching single price adjustment data for editing"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"name":"id","in":"path","schema":{"type":"string","description":"Price Adjustment  id for fetching single price adjustment data for editing"},"required":true}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/price-adjustment/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SuccessMessage
            schema = SuccessMessage()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for removePriceAdjustment")
                print(e)

        return response
    
    async def fetchAndvalidateCartItems(self, body="", request_headers:Dict={}):
        """Retrieve cart details for a provided list of cart items and validate its contents. This ensures accuracy and completeness in cart information, including item quantities, prices, discounts, and applicable taxes.
        """
        payload = {}
        

        # Parameter validation
        schema = CartValidator.fetchAndvalidateCartItems()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import OpenapiCartDetailsRequestObject
        schema = OpenapiCartDetailsRequestObject()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/cart/validate", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/cart/validate", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import OpenapiCartDetailsResponseObject
            schema = OpenapiCartDetailsResponseObject()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for fetchAndvalidateCartItems")
                print(e)

        return response
    
    async def checkCartServiceability(self, body="", request_headers:Dict={}):
        """Verify the serviceability of items in the cart at a specific pin code and ensure accurate delivery promises. System checks each item's availability and delivery feasibility, providing real-time information on serviceability and estimated delivery times.
        """
        payload = {}
        

        # Parameter validation
        schema = CartValidator.checkCartServiceability()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import OpenApiCartServiceabilityRequestObject
        schema = OpenApiCartServiceabilityRequestObject()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/cart/serviceability", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/cart/serviceability", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import OpenApiCartServiceabilityResponseObject
            schema = OpenApiCartServiceabilityResponseObject()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for checkCartServiceability")
                print(e)

        return response
    
    async def checkoutCart(self, body="", request_headers:Dict={}):
        """The checkout cart initiates the order creation process based on the selected address and payment method. It revalidates the cart details to ensure safe and seamless order placement.
        """
        payload = {}
        

        # Parameter validation
        schema = CartValidator.checkoutCart()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import OpenApiPlatformCheckoutReq
        schema = OpenApiPlatformCheckoutReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/cart/checkout", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/cart/checkout", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import OpenApiCheckoutResponseObject
            schema = OpenApiCheckoutResponseObject()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for checkoutCart")
                print(e)

        return response
    
    async def getAbandonedCart(self, page_no=None, page_size=None, from_date=None, to_date=None, anonymous_cart=None, last_id=None, sort_on=None, request_headers:Dict={}):
        """Retrieve the list of abandoned carts that have been active for the specified period of time and have not yet been archived for the specific sales channel.
        :param page_no :  : type integer
        :param page_size :  : type integer
        :param from_date :  : type string
        :param to_date :  : type string
        :param anonymous_cart :  : type boolean
        :param last_id :  : type string
        :param sort_on :  : type string
        """
        payload = {}
        
        if page_no is not None:
            payload["page_no"] = page_no
        if page_size is not None:
            payload["page_size"] = page_size
        if from_date is not None:
            payload["from_date"] = from_date
        if to_date is not None:
            payload["to_date"] = to_date
        if anonymous_cart is not None:
            payload["anonymous_cart"] = anonymous_cart
        if last_id is not None:
            payload["last_id"] = last_id
        if sort_on is not None:
            payload["sort_on"] = sort_on

        # Parameter validation
        schema = CartValidator.getAbandonedCart()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/abandoned/carts", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer","default":0,"description":"current page no as per pagination"}},{"name":"page_size","in":"query","schema":{"type":"integer","default":10,"description":"Coupon max records fetched in single request"}},{"name":"from_date","in":"query","schema":{"type":"string","format":"date-time","description":"Cart which are created on or after from_date"}},{"name":"to_date","in":"query","schema":{"type":"string","format":"date-time","description":"Cart which are created on or before to_date"}},{"name":"anonymous_cart","in":"query","schema":{"type":"boolean","description":"Filter by `anonymous_cart`"}},{"name":"last_id","in":"query","schema":{"type":"string","description":"pagination is done based on the last_object_id"}},{"name":"sort_on","in":"query","schema":{"type":"string","description":"on which column to sort on i.e created_on or last_modified","enum":["created_on","last_modified"]}}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer","default":0,"description":"current page no as per pagination"}},{"name":"page_size","in":"query","schema":{"type":"integer","default":10,"description":"Coupon max records fetched in single request"}},{"name":"from_date","in":"query","schema":{"type":"string","format":"date-time","description":"Cart which are created on or after from_date"}},{"name":"to_date","in":"query","schema":{"type":"string","format":"date-time","description":"Cart which are created on or before to_date"}},{"name":"anonymous_cart","in":"query","schema":{"type":"boolean","description":"Filter by `anonymous_cart`"}},{"name":"last_id","in":"query","schema":{"type":"string","description":"pagination is done based on the last_object_id"}},{"name":"sort_on","in":"query","schema":{"type":"string","description":"on which column to sort on i.e created_on or last_modified","enum":["created_on","last_modified"]}}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}]}""", serverType="platform", page_no=page_no, page_size=page_size, from_date=from_date, to_date=to_date, anonymous_cart=anonymous_cart, last_id=last_id, sort_on=sort_on)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, from_date=from_date, to_date=to_date, anonymous_cart=anonymous_cart, last_id=last_id, sort_on=sort_on)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/abandoned/carts", page_no=page_no, page_size=page_size, from_date=from_date, to_date=to_date, anonymous_cart=anonymous_cart, last_id=last_id, sort_on=sort_on), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AbandonedCartResponseObject
            schema = AbandonedCartResponseObject()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAbandonedCart")
                print(e)

        return response
    
    async def getAbandonedCartDetails(self, id=None, i=None, b=None, c=None, request_headers:Dict={}):
        """Retrieves abandoned cart details linked to a specific customer using a unique cart ID. It offers an overview of the items, quantities, prices, and other relevant information associated with the cart.
        :param id :  : type string
        :param i :  : type boolean
        :param b :  : type boolean
        :param c :  : type boolean
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        if i is not None:
            payload["i"] = i
        if b is not None:
            payload["b"] = b
        if c is not None:
            payload["c"] = c

        # Parameter validation
        schema = CartValidator.getAbandonedCartDetails()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/abandoned/cart/detail", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}],"optional":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"i","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."}},{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}},{"in":"query","name":"c","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the cod charges in breakup of cart items."}}],"query":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"i","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."}},{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}},{"in":"query","name":"c","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the cod charges in breakup of cart items."}}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}]}""", serverType="platform", id=id, i=i, b=b, c=c)
        query_string = await create_query_string(id=id, i=i, b=b, c=c)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/abandoned/cart/detail", id=id, i=i, b=b, c=c), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CartDetailResponseObject
            schema = CartDetailResponseObject()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAbandonedCartDetails")
                print(e)

        return response
    
    async def addItems(self, cart_id=None, b=None, body="", request_headers:Dict={}):
        """Add product items to the customer's existing shopping cart. If there is no existing cart associated with the customer, it creates a new one and adds the items to it.
        :param cart_id : Current Cart _id : type string
        :param b :  : type boolean
        """
        payload = {}
        
        if cart_id is not None:
            payload["cart_id"] = cart_id
        if b is not None:
            payload["b"] = b

        # Parameter validation
        schema = CartValidator.addItems()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AddCartRequestObject
        schema = AddCartRequestObject()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/abandoned/carts/{cart_id}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"schema":{"type":"string"},"description":"Current Cart _id","in":"path","required":true,"name":"cart_id"}],"optional":[{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}}],"query":[{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"schema":{"type":"string"},"description":"Current Cart _id","in":"path","required":true,"name":"cart_id"}]}""", serverType="platform", cart_id=cart_id, b=b)
        query_string = await create_query_string(b=b)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/abandoned/carts/{cart_id}", cart_id=cart_id, b=b), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AddCartDetailResponseObject
            schema = AddCartDetailResponseObject()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for addItems")
                print(e)

        return response
    
    async def updateCart(self, cart_id=None, b=None, body="", request_headers:Dict={}):
        """Customers can modify added product attributes such as quantity and size, as well as remove items from the cart.
        :param cart_id : Current Cart _id : type string
        :param b :  : type boolean
        """
        payload = {}
        
        if cart_id is not None:
            payload["cart_id"] = cart_id
        if b is not None:
            payload["b"] = b

        # Parameter validation
        schema = CartValidator.updateCart()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UpdateCartRequestObject
        schema = UpdateCartRequestObject()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/abandoned/carts/{cart_id}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"schema":{"type":"string"},"description":"Current Cart _id","in":"path","required":true,"name":"cart_id"}],"optional":[{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}}],"query":[{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"schema":{"type":"string"},"description":"Current Cart _id","in":"path","required":true,"name":"cart_id"}]}""", serverType="platform", cart_id=cart_id, b=b)
        query_string = await create_query_string(b=b)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/abandoned/carts/{cart_id}", cart_id=cart_id, b=b), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import UpdateCartDetailResponseObject
            schema = UpdateCartDetailResponseObject()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateCart")
                print(e)

        return response
    
    async def getCouponOptionValues(self, request_headers:Dict={}):
        """Retrieves the available values for coupon options used to create and update coupons.
        """
        payload = {}
        

        # Parameter validation
        schema = CartValidator.getCouponOptionValues()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/coupon_options", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/coupon_options", ), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CouponOptions
            schema = CouponOptions()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCouponOptionValues")
                print(e)

        return response
    
    async def getCouponCodeExists(self, code=None, request_headers:Dict={}):
        """Validates the presence of a coupon code for the specified sales channel to verify whether the provided code already exists or not.
        :param code :  : type string
        """
        payload = {}
        
        if code is not None:
            payload["code"] = code

        # Parameter validation
        schema = CartValidator.getCouponCodeExists()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/coupon_code_exists", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}],"optional":[{"name":"code","in":"query","schema":{"type":"string","description":"Coupon code"}}],"query":[{"name":"code","in":"query","schema":{"type":"string","description":"Coupon code"}}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}]}""", serverType="platform", code=code)
        query_string = await create_query_string(code=code)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/coupon_code_exists", code=code), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        return response
    
    async def getPromotionCodeExists(self, code=None, request_headers:Dict={}):
        """Validates the presence of a promotion code for the specified sales channel to verify whether the provided code already exists or not.
        :param code :  : type string
        """
        payload = {}
        
        if code is not None:
            payload["code"] = code

        # Parameter validation
        schema = CartValidator.getPromotionCodeExists()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/promotion_code_exists", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}],"optional":[{"name":"code","in":"query","schema":{"type":"string","description":"Promotion code"}}],"query":[{"name":"code","in":"query","schema":{"type":"string","description":"Promotion code"}}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}]}""", serverType="platform", code=code)
        query_string = await create_query_string(code=code)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/promotion_code_exists", code=code), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        return response
    
    async def overrideCart(self, body="", request_headers:Dict={}):
        """Overrides the cart's checkout process with a new provided cart items. It provides flexibility in customizing checkout flows to meet specific business requirements, enhancing the user experience and optimizing order processing workflows.
        """
        payload = {}
        

        # Parameter validation
        schema = CartValidator.overrideCart()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import OverrideCheckoutReq
        schema = OverrideCheckoutReq()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/checkout/over-ride", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/checkout/over-ride", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import OverrideCheckoutResponseObject
            schema = OverrideCheckoutResponseObject()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for overrideCart")
                print(e)

        return response
    
    async def getCartShareLink(self, body="", request_headers:Dict={}):
        """Generate a unique shareable link for the customer's cart for a specific sales channel. This link enables easy sharing of the cart contents with other users, facilitating collaborative shopping experiences.
        """
        payload = {}
        

        # Parameter validation
        schema = CartValidator.getCartShareLink()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import GetShareCartLinkRequestObject
        schema = GetShareCartLinkRequestObject()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/share-cart", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/share-cart", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetShareCartLinkResponseObject
            schema = GetShareCartLinkResponseObject()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCartShareLink")
                print(e)

        return response
    
    async def getCartSharedItems(self, token=None, request_headers:Dict={}):
        """Use this API to get the shared cart details as per the token generated using the share-cart API.
        :param token : Token of the shared short link : type string
        """
        payload = {}
        
        if token is not None:
            payload["token"] = token

        # Parameter validation
        schema = CartValidator.getCartSharedItems()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/share-cart/{token}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"name":"token","description":"Token of the shared short link","schema":{"type":"string"},"in":"path","required":true}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"name":"token","description":"Token of the shared short link","schema":{"type":"string"},"in":"path","required":true}]}""", serverType="platform", token=token)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/share-cart/{token}", token=token), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SharedCartResponseObject
            schema = SharedCartResponseObject()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCartSharedItems")
                print(e)

        return response
    
    async def updateCartWithSharedItems(self, token=None, action=None, cart_id=None, request_headers:Dict={}):
        """Customer can either merge or replace shared cart items with existing cart.
        :param token : Token of the shared short link : type string
        :param action : Operation to perform on the existing cart merge or replace. : type string
        :param cart_id :  : type string
        """
        payload = {}
        
        if token is not None:
            payload["token"] = token
        if action is not None:
            payload["action"] = action
        if cart_id is not None:
            payload["cart_id"] = cart_id

        # Parameter validation
        schema = CartValidator.updateCartWithSharedItems()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/share-cart/{token}/{action}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"name":"token","description":"Token of the shared short link","schema":{"type":"string"},"in":"path","required":true},{"name":"action","description":"Operation to perform on the existing cart merge or replace.","schema":{"type":"string","enum":["merge","replace"]},"in":"path","required":true}],"optional":[{"name":"cart_id","in":"query","schema":{"type":"string","description":"The unique identifier of the cart"}}],"query":[{"name":"cart_id","in":"query","schema":{"type":"string","description":"The unique identifier of the cart"}}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"name":"token","description":"Token of the shared short link","schema":{"type":"string"},"in":"path","required":true},{"name":"action","description":"Operation to perform on the existing cart merge or replace.","schema":{"type":"string","enum":["merge","replace"]},"in":"path","required":true}]}""", serverType="platform", token=token, action=action, cart_id=cart_id)
        query_string = await create_query_string(cart_id=cart_id)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/share-cart/{token}/{action}", token=token, action=action, cart_id=cart_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SharedCartResponseObject
            schema = SharedCartResponseObject()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateCartWithSharedItems")
                print(e)

        return response
    
    async def getCartList(self, from_date=None, to_date=None, filter_on=None, request_headers:Dict={}):
        """Retrieve the list of active carts associated with a specific customer
        :param from_date :  : type string
        :param to_date :  : type string
        :param filter_on :  : type string
        """
        payload = {}
        
        if from_date is not None:
            payload["from_date"] = from_date
        if to_date is not None:
            payload["to_date"] = to_date
        if filter_on is not None:
            payload["filter_on"] = filter_on

        # Parameter validation
        schema = CartValidator.getCartList()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/cart-list", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}],"optional":[{"name":"from_date","in":"query","schema":{"type":"string","format":"date-time","description":"Cart which are created on or after from_date. Supports ISO date format."}},{"name":"to_date","in":"query","schema":{"type":"string","format":"date-time","description":"Cart which are created on or before to_date. Supports ISO date format."}},{"name":"filter_on","in":"query","schema":{"type":"string","description":"on which column to sort on i.e created_on or last_modified","enum":["created_on","last_modified"]}}],"query":[{"name":"from_date","in":"query","schema":{"type":"string","format":"date-time","description":"Cart which are created on or after from_date. Supports ISO date format."}},{"name":"to_date","in":"query","schema":{"type":"string","format":"date-time","description":"Cart which are created on or before to_date. Supports ISO date format."}},{"name":"filter_on","in":"query","schema":{"type":"string","description":"on which column to sort on i.e created_on or last_modified","enum":["created_on","last_modified"]}}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}]}""", serverType="platform", from_date=from_date, to_date=to_date, filter_on=filter_on)
        query_string = await create_query_string(from_date=from_date, to_date=to_date, filter_on=filter_on)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/cart-list", from_date=from_date, to_date=to_date, filter_on=filter_on), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import MultiCartResponseObject
            schema = MultiCartResponseObject()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCartList")
                print(e)

        return response
    
    async def updateCartUser(self, id=None, body="", request_headers:Dict={}):
        """Modify the cart user to a new valid customer for the provided customer ID.
        :param id :  : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CartValidator.updateCartUser()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UpdateUserCartMapping
        schema = UpdateUserCartMapping()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/update-user", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}],"optional":[{"name":"id","in":"query","schema":{"type":"string","description":"cart id"}}],"query":[{"name":"id","in":"query","schema":{"type":"string","description":"cart id"}}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}]}""", serverType="platform", id=id)
        query_string = await create_query_string(id=id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/update-user", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import UserCartMappingResponseObject
            schema = UserCartMappingResponseObject()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateCartUser")
                print(e)

        return response
    
    async def getItemCount(self, id=None, buy_now=None, cart_type=None, request_headers:Dict={}):
        """Use this API to get the total number of items present in cart.
        :param id : The unique identifier of the cart. : type string
        :param buy_now : Boolean value to get buy_now cart. : type boolean
        :param cart_type : The type of cart : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        if buy_now is not None:
            payload["buy_now"] = buy_now
        if cart_type is not None:
            payload["cart_type"] = cart_type

        # Parameter validation
        schema = CartValidator.getItemCount()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/basic", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}],"optional":[{"name":"id","in":"query","description":"The unique identifier of the cart.","schema":{"type":"string"}},{"in":"query","name":"buy_now","schema":{"type":"boolean"},"description":"Boolean value to get buy_now cart."},{"in":"query","name":"cart_type","schema":{"type":"string","enum":["universal"]},"description":"The type of cart"}],"query":[{"name":"id","in":"query","description":"The unique identifier of the cart.","schema":{"type":"string"}},{"in":"query","name":"buy_now","schema":{"type":"boolean"},"description":"Boolean value to get buy_now cart."},{"in":"query","name":"cart_type","schema":{"type":"string","enum":["universal"]},"description":"The type of cart"}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}]}""", serverType="platform", id=id, buy_now=buy_now, cart_type=cart_type)
        query_string = await create_query_string(id=id, buy_now=buy_now, cart_type=cart_type)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/basic", id=id, buy_now=buy_now, cart_type=cart_type), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CartItemCountResponseObject
            schema = CartItemCountResponseObject()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getItemCount")
                print(e)

        return response
    
    async def platformAddItems(self, i=None, b=None, buy_now=None, id=None, cart_type=None, body="", request_headers:Dict={}):
        """Add product items to the customer's existing shopping cart. If there is no existing cart associated with the customer, it creates a new one and adds the items to it.
        :param i : This is a boolean value. Select `true` to retrieve all the items added in the cart. : type boolean
        :param b : This is a boolean value. Select `true` to retrieve the price breakup of cart items. : type boolean
        :param buy_now : This is a boolen value. Select `true` to set/initialize buy now cart : type boolean
        :param id : The unique identifier of the cart : type string
        :param cart_type : The type of cart : type string
        """
        payload = {}
        
        if i is not None:
            payload["i"] = i
        if b is not None:
            payload["b"] = b
        if buy_now is not None:
            payload["buy_now"] = buy_now
        if id is not None:
            payload["id"] = id
        if cart_type is not None:
            payload["cart_type"] = cart_type

        # Parameter validation
        schema = CartValidator.platformAddItems()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PlatformAddCartRequestObject
        schema = PlatformAddCartRequestObject()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/detail", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}],"optional":[{"in":"query","name":"i","schema":{"type":"boolean"},"description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."},{"in":"query","name":"b","schema":{"type":"boolean"},"description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."},{"in":"query","name":"buy_now","schema":{"type":"boolean"},"description":"This is a boolen value. Select `true` to set/initialize buy now cart"},{"in":"query","name":"id","schema":{"type":"string"},"description":"The unique identifier of the cart"},{"name":"cart_type","in":"query","schema":{"type":"string","enum":["universal"]},"description":"The type of cart"}],"query":[{"in":"query","name":"i","schema":{"type":"boolean"},"description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."},{"in":"query","name":"b","schema":{"type":"boolean"},"description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."},{"in":"query","name":"buy_now","schema":{"type":"boolean"},"description":"This is a boolen value. Select `true` to set/initialize buy now cart"},{"in":"query","name":"id","schema":{"type":"string"},"description":"The unique identifier of the cart"},{"name":"cart_type","in":"query","schema":{"type":"string","enum":["universal"]},"description":"The type of cart"}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}]}""", serverType="platform", i=i, b=b, buy_now=buy_now, id=id, cart_type=cart_type)
        query_string = await create_query_string(i=i, b=b, buy_now=buy_now, id=id, cart_type=cart_type)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/detail", i=i, b=b, buy_now=buy_now, id=id, cart_type=cart_type), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import AddCartDetailResponseObject
            schema = AddCartDetailResponseObject()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for platformAddItems")
                print(e)

        return response
    
    async def getCart(self, id=None, user_id=None, i=None, b=None, assign_card_id=None, buy_now=None, cart_type=None, request_headers:Dict={}):
        """Use this API to get details of all the items added to a cart.
        :param id : The unique identifier of the cart : type string
        :param user_id : Option to fetch cart for the provided user_id. : type string
        :param i : This is a boolean value. Select `true` to retrieve all the items added in the cart. : type boolean
        :param b : This is a boolean value. Select `true` to retrieve the price breakup of cart items. : type boolean
        :param assign_card_id : Token of user's debit or credit card : type number
        :param buy_now : This is a boolen value. Select `true` to set/initialize buy now cart : type boolean
        :param cart_type : The type of cart : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        if user_id is not None:
            payload["user_id"] = user_id
        if i is not None:
            payload["i"] = i
        if b is not None:
            payload["b"] = b
        if assign_card_id is not None:
            payload["assign_card_id"] = assign_card_id
        if buy_now is not None:
            payload["buy_now"] = buy_now
        if cart_type is not None:
            payload["cart_type"] = cart_type

        # Parameter validation
        schema = CartValidator.getCart()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/detail", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}],"optional":[{"in":"query","name":"id","schema":{"type":"string"},"description":"The unique identifier of the cart"},{"in":"query","name":"user_id","schema":{"type":"string"},"description":"Option to fetch cart for the provided user_id."},{"in":"query","name":"i","schema":{"type":"boolean"},"description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."},{"in":"query","name":"b","schema":{"type":"boolean"},"description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."},{"in":"query","name":"assign_card_id","schema":{"type":"number"},"description":"Token of user's debit or credit card"},{"in":"query","name":"buy_now","schema":{"type":"boolean"},"description":"This is a boolen value. Select `true` to set/initialize buy now cart"},{"name":"cart_type","in":"query","schema":{"type":"string","enum":["universal"]},"description":"The type of cart"}],"query":[{"in":"query","name":"id","schema":{"type":"string"},"description":"The unique identifier of the cart"},{"in":"query","name":"user_id","schema":{"type":"string"},"description":"Option to fetch cart for the provided user_id."},{"in":"query","name":"i","schema":{"type":"boolean"},"description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."},{"in":"query","name":"b","schema":{"type":"boolean"},"description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."},{"in":"query","name":"assign_card_id","schema":{"type":"number"},"description":"Token of user's debit or credit card"},{"in":"query","name":"buy_now","schema":{"type":"boolean"},"description":"This is a boolen value. Select `true` to set/initialize buy now cart"},{"name":"cart_type","in":"query","schema":{"type":"string","enum":["universal"]},"description":"The type of cart"}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}]}""", serverType="platform", id=id, user_id=user_id, i=i, b=b, assign_card_id=assign_card_id, buy_now=buy_now, cart_type=cart_type)
        query_string = await create_query_string(id=id, user_id=user_id, i=i, b=b, assign_card_id=assign_card_id, buy_now=buy_now, cart_type=cart_type)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/detail", id=id, user_id=user_id, i=i, b=b, assign_card_id=assign_card_id, buy_now=buy_now, cart_type=cart_type), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CartDetailResponseObject
            schema = CartDetailResponseObject()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getCart")
                print(e)

        return response
    
    async def platformUpdateCart(self, id=None, i=None, order_type=None, b=None, buy_now=None, cart_type=None, body="", request_headers:Dict={}):
        """Customers can modify added product attributes such as quantity and size, as well as remove items from the cart.
        :param id : The unique identifier of the cart : type string
        :param i : This is a boolean value. Select `true` to retrieve all the items added in the cart. : type boolean
        :param order_type : The order type of shipment HomeDelivery - If the customer wants the order home-delivered PickAtStore - If the customer wants the handover of an order at the store itself. : type string
        :param b : This is a boolean value. Select `true` to retrieve the price breakup of cart items. : type boolean
        :param buy_now : This is a boolen value. Select `true` to set/initialize buy now cart : type boolean
        :param cart_type : The type of cart : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        if i is not None:
            payload["i"] = i
        if order_type is not None:
            payload["order_type"] = order_type
        if b is not None:
            payload["b"] = b
        if buy_now is not None:
            payload["buy_now"] = buy_now
        if cart_type is not None:
            payload["cart_type"] = cart_type

        # Parameter validation
        schema = CartValidator.platformUpdateCart()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PlatformUpdateCartRequestObject
        schema = PlatformUpdateCartRequestObject()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/detail", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}],"optional":[{"in":"query","name":"id","schema":{"type":"string"},"description":"The unique identifier of the cart"},{"in":"query","name":"i","schema":{"type":"boolean"},"description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."},{"in":"query","name":"order_type","schema":{"type":"string","enum":["HomeDelivery","PickAtStore"]},"description":"The order type of shipment HomeDelivery - If the customer wants the order home-delivered PickAtStore - If the customer wants the handover of an order at the store itself."},{"in":"query","name":"b","schema":{"type":"boolean"},"description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."},{"in":"query","name":"buy_now","schema":{"type":"boolean"},"description":"This is a boolen value. Select `true` to set/initialize buy now cart"},{"name":"cart_type","in":"query","schema":{"type":"string","enum":["universal"]},"description":"The type of cart"}],"query":[{"in":"query","name":"id","schema":{"type":"string"},"description":"The unique identifier of the cart"},{"in":"query","name":"i","schema":{"type":"boolean"},"description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."},{"in":"query","name":"order_type","schema":{"type":"string","enum":["HomeDelivery","PickAtStore"]},"description":"The order type of shipment HomeDelivery - If the customer wants the order home-delivered PickAtStore - If the customer wants the handover of an order at the store itself."},{"in":"query","name":"b","schema":{"type":"boolean"},"description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."},{"in":"query","name":"buy_now","schema":{"type":"boolean"},"description":"This is a boolen value. Select `true` to set/initialize buy now cart"},{"name":"cart_type","in":"query","schema":{"type":"string","enum":["universal"]},"description":"The type of cart"}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}]}""", serverType="platform", id=id, i=i, order_type=order_type, b=b, buy_now=buy_now, cart_type=cart_type)
        query_string = await create_query_string(id=id, i=i, order_type=order_type, b=b, buy_now=buy_now, cart_type=cart_type)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/detail", id=id, i=i, order_type=order_type, b=b, buy_now=buy_now, cart_type=cart_type), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import UpdateCartDetailResponseObject
            schema = UpdateCartDetailResponseObject()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for platformUpdateCart")
                print(e)

        return response
    
    async def deleteCart(self, id=None, cart_type=None, body="", request_headers:Dict={}):
        """Delete all items from the user's cart and resets it to its initial state, providing a clean slate for new selections.
        :param id : The unique identifier of the cart. : type string
        :param cart_type : The type of cart : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        if cart_type is not None:
            payload["cart_type"] = cart_type

        # Parameter validation
        schema = CartValidator.deleteCart()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import DeleteCartRequestObject
        schema = DeleteCartRequestObject()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/cart_archive", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}],"optional":[{"name":"id","in":"query","description":"The unique identifier of the cart.","schema":{"type":"string"}},{"name":"cart_type","in":"query","schema":{"type":"string","enum":["universal"]},"description":"The type of cart"}],"query":[{"name":"id","in":"query","description":"The unique identifier of the cart.","schema":{"type":"string"}},{"name":"cart_type","in":"query","schema":{"type":"string","enum":["universal"]},"description":"The type of cart"}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}]}""", serverType="platform", id=id, cart_type=cart_type)
        query_string = await create_query_string(id=id, cart_type=cart_type)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/cart_archive", id=id, cart_type=cart_type), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import DeleteCartDetailResponseObject
            schema = DeleteCartDetailResponseObject()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for deleteCart")
                print(e)

        return response
    
    async def getAppCoupons(self, id=None, buy_now=None, slug=None, store_id=None, request_headers:Dict={}):
        """Retrieve a list of all available coupons that customer can apply to their carts. It provides details about each coupon, including its code, discount amount, and applicable conditions.
        :param id :  : type string
        :param buy_now :  : type boolean
        :param slug :  : type string
        :param store_id :  : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        if buy_now is not None:
            payload["buy_now"] = buy_now
        if slug is not None:
            payload["slug"] = slug
        if store_id is not None:
            payload["store_id"] = store_id

        # Parameter validation
        schema = CartValidator.getAppCoupons()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/platform-pos-coupon", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}],"optional":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart."}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is boolean to get buy_now cart"}},{"in":"query","name":"slug","schema":{"type":"string","description":"Product slug to fetch the available coupons"}},{"in":"query","name":"store_id","schema":{"type":"string","description":"Store id"}}],"query":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart."}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is boolean to get buy_now cart"}},{"in":"query","name":"slug","schema":{"type":"string","description":"Product slug to fetch the available coupons"}},{"in":"query","name":"store_id","schema":{"type":"string","description":"Store id"}}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}]}""", serverType="platform", id=id, buy_now=buy_now, slug=slug, store_id=store_id)
        query_string = await create_query_string(id=id, buy_now=buy_now, slug=slug, store_id=store_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/platform-pos-coupon", id=id, buy_now=buy_now, slug=slug, store_id=store_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import GetCouponResponseObject
            schema = GetCouponResponseObject()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAppCoupons")
                print(e)

        return response
    
    async def applyCoupon(self, i=None, b=None, p=None, id=None, buy_now=None, body="", request_headers:Dict={}):
        """Apply a coupon code to the customer's cart to trigger discounts on eligible items
        :param i :  : type boolean
        :param b :  : type boolean
        :param p :  : type boolean
        :param id :  : type string
        :param buy_now :  : type boolean
        """
        payload = {}
        
        if i is not None:
            payload["i"] = i
        if b is not None:
            payload["b"] = b
        if p is not None:
            payload["p"] = p
        if id is not None:
            payload["id"] = id
        if buy_now is not None:
            payload["buy_now"] = buy_now

        # Parameter validation
        schema = CartValidator.applyCoupon()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import ApplyCouponRequestObject
        schema = ApplyCouponRequestObject()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/platform-pos-coupon", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}],"optional":[{"in":"query","name":"i","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."}},{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}},{"in":"query","name":"p","schema":{"type":"boolean","description":"This is a boolean value. Select `true` for getting a payment option in response."}},{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is boolean to get buy_now cart"}}],"query":[{"in":"query","name":"i","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."}},{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}},{"in":"query","name":"p","schema":{"type":"boolean","description":"This is a boolean value. Select `true` for getting a payment option in response."}},{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is boolean to get buy_now cart"}}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}]}""", serverType="platform", i=i, b=b, p=p, id=id, buy_now=buy_now)
        query_string = await create_query_string(i=i, b=b, p=p, id=id, buy_now=buy_now)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/platform-pos-coupon", i=i, b=b, p=p, id=id, buy_now=buy_now), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CartDetailResponseObject
            schema = CartDetailResponseObject()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for applyCoupon")
                print(e)

        return response
    
    async def removeCoupon(self, uid=None, buy_now=None, cart_type=None, request_headers:Dict={}):
        """Remove an applied coupon from the customer's cart, thereby removing the associated discount from the cart total.
        :param uid :  : type string
        :param buy_now :  : type boolean
        :param cart_type : The type of cart : type string
        """
        payload = {}
        
        if uid is not None:
            payload["uid"] = uid
        if buy_now is not None:
            payload["buy_now"] = buy_now
        if cart_type is not None:
            payload["cart_type"] = cart_type

        # Parameter validation
        schema = CartValidator.removeCoupon()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/platform-pos-coupon", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}],"optional":[{"in":"query","name":"uid","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is boolean to get buy_now cart"}},{"in":"query","name":"cart_type","schema":{"type":"string","enum":["universal"]},"description":"The type of cart"}],"query":[{"in":"query","name":"uid","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is boolean to get buy_now cart"}},{"in":"query","name":"cart_type","schema":{"type":"string","enum":["universal"]},"description":"The type of cart"}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}]}""", serverType="platform", uid=uid, buy_now=buy_now, cart_type=cart_type)
        query_string = await create_query_string(uid=uid, buy_now=buy_now, cart_type=cart_type)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/platform-pos-coupon", uid=uid, buy_now=buy_now, cart_type=cart_type), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CartDetailResponseObject
            schema = CartDetailResponseObject()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for removeCoupon")
                print(e)

        return response
    
    async def addAddress(self, body="", request_headers:Dict={}):
        """Use this API to add an address to an account.
        """
        payload = {}
        

        # Parameter validation
        schema = CartValidator.addAddress()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PlatformAddress
        schema = PlatformAddress()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/address", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}]}""", serverType="platform", )
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/address", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import SaveAddressResponseObject
            schema = SaveAddressResponseObject()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for addAddress")
                print(e)

        return response
    
    async def getAddresses(self, cart_id=None, buy_now=None, mobile_no=None, checkout_mode=None, tags=None, is_default=None, user_id=None, request_headers:Dict={}):
        """Retrieves a list of all addresses saved by the customer, simplifying the checkout process by offering pre-saved address options for delivery.
        :param cart_id :  : type string
        :param buy_now :  : type boolean
        :param mobile_no :  : type string
        :param checkout_mode :  : type string
        :param tags :  : type string
        :param is_default :  : type boolean
        :param user_id :  : type string
        """
        payload = {}
        
        if cart_id is not None:
            payload["cart_id"] = cart_id
        if buy_now is not None:
            payload["buy_now"] = buy_now
        if mobile_no is not None:
            payload["mobile_no"] = mobile_no
        if checkout_mode is not None:
            payload["checkout_mode"] = checkout_mode
        if tags is not None:
            payload["tags"] = tags
        if is_default is not None:
            payload["is_default"] = is_default
        if user_id is not None:
            payload["user_id"] = user_id

        # Parameter validation
        schema = CartValidator.getAddresses()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/address", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}],"optional":[{"name":"cart_id","in":"query","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is boolean to get buy_now cart"}},{"in":"query","name":"mobile_no","schema":{"type":"string","description":"10-digit mobile number"}},{"in":"query","name":"checkout_mode","schema":{"type":"string","description":"Option to checkout for `self` or for `others`. By default, it is `self`.","enum":["self"]}},{"in":"query","name":"tags","schema":{"type":"string","description":"Tag given to an address, e.g. work, home, office, shop.","enum":["work","home"]}},{"in":"query","name":"is_default","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to fetch the default address."}},{"in":"query","name":"user_id","schema":{"type":"string","description":"Option to fetch address for the provided user_id."}}],"query":[{"name":"cart_id","in":"query","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is boolean to get buy_now cart"}},{"in":"query","name":"mobile_no","schema":{"type":"string","description":"10-digit mobile number"}},{"in":"query","name":"checkout_mode","schema":{"type":"string","description":"Option to checkout for `self` or for `others`. By default, it is `self`.","enum":["self"]}},{"in":"query","name":"tags","schema":{"type":"string","description":"Tag given to an address, e.g. work, home, office, shop.","enum":["work","home"]}},{"in":"query","name":"is_default","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to fetch the default address."}},{"in":"query","name":"user_id","schema":{"type":"string","description":"Option to fetch address for the provided user_id."}}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}]}""", serverType="platform", cart_id=cart_id, buy_now=buy_now, mobile_no=mobile_no, checkout_mode=checkout_mode, tags=tags, is_default=is_default, user_id=user_id)
        query_string = await create_query_string(cart_id=cart_id, buy_now=buy_now, mobile_no=mobile_no, checkout_mode=checkout_mode, tags=tags, is_default=is_default, user_id=user_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/address", cart_id=cart_id, buy_now=buy_now, mobile_no=mobile_no, checkout_mode=checkout_mode, tags=tags, is_default=is_default, user_id=user_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PlatformGetAddressesResponseObject
            schema = PlatformGetAddressesResponseObject()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAddresses")
                print(e)

        return response
    
    async def getAddressById(self, id=None, cart_id=None, buy_now=None, mobile_no=None, checkout_mode=None, tags=None, is_default=None, user_id=None, request_headers:Dict={}):
        """Retrieve a specific customer address stored in the system by providing its unique identifier. This API provides detailed information about the address, including the recipient's name, address, city, postal code, and other relevant details.
        :param id :  : type string
        :param cart_id :  : type string
        :param buy_now :  : type boolean
        :param mobile_no :  : type string
        :param checkout_mode :  : type string
        :param tags :  : type string
        :param is_default :  : type boolean
        :param user_id :  : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        if cart_id is not None:
            payload["cart_id"] = cart_id
        if buy_now is not None:
            payload["buy_now"] = buy_now
        if mobile_no is not None:
            payload["mobile_no"] = mobile_no
        if checkout_mode is not None:
            payload["checkout_mode"] = checkout_mode
        if tags is not None:
            payload["tags"] = tags
        if is_default is not None:
            payload["is_default"] = is_default
        if user_id is not None:
            payload["user_id"] = user_id

        # Parameter validation
        schema = CartValidator.getAddressById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/address/{id}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"name":"id","in":"path","schema":{"type":"string","description":"ID allotted to the selected address"},"required":true}],"optional":[{"name":"cart_id","in":"query","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is boolean to get buy_now cart"}},{"in":"query","name":"mobile_no","schema":{"type":"string","description":"10-digit mobile number"}},{"in":"query","name":"checkout_mode","schema":{"type":"string","description":"Option to checkout for self or for others","enum":["self"]}},{"in":"query","name":"tags","schema":{"type":"string","description":"Tag given to an address, e.g. work, home, office, shop.","enum":["home"]}},{"in":"query","name":"is_default","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to fetch the default address."}},{"in":"query","name":"user_id","schema":{"type":"string","description":"Option to fetch address for the provided user_id."}}],"query":[{"name":"cart_id","in":"query","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is boolean to get buy_now cart"}},{"in":"query","name":"mobile_no","schema":{"type":"string","description":"10-digit mobile number"}},{"in":"query","name":"checkout_mode","schema":{"type":"string","description":"Option to checkout for self or for others","enum":["self"]}},{"in":"query","name":"tags","schema":{"type":"string","description":"Tag given to an address, e.g. work, home, office, shop.","enum":["home"]}},{"in":"query","name":"is_default","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to fetch the default address."}},{"in":"query","name":"user_id","schema":{"type":"string","description":"Option to fetch address for the provided user_id."}}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"name":"id","in":"path","schema":{"type":"string","description":"ID allotted to the selected address"},"required":true}]}""", serverType="platform", id=id, cart_id=cart_id, buy_now=buy_now, mobile_no=mobile_no, checkout_mode=checkout_mode, tags=tags, is_default=is_default, user_id=user_id)
        query_string = await create_query_string(cart_id=cart_id, buy_now=buy_now, mobile_no=mobile_no, checkout_mode=checkout_mode, tags=tags, is_default=is_default, user_id=user_id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/address/{id}", id=id, cart_id=cart_id, buy_now=buy_now, mobile_no=mobile_no, checkout_mode=checkout_mode, tags=tags, is_default=is_default, user_id=user_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PlatformAddress
            schema = PlatformAddress()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAddressById")
                print(e)

        return response
    
    async def updateAddress(self, id=None, body="", request_headers:Dict={}):
        """Update the user address
        :param id : ID allotted to the selected address : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CartValidator.updateAddress()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PlatformAddress
        schema = PlatformAddress()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/address/{id}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"name":"id","description":"ID allotted to the selected address","schema":{"type":"string"},"in":"path","required":true}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"name":"id","description":"ID allotted to the selected address","schema":{"type":"string"},"in":"path","required":true}]}""", serverType="platform", id=id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/address/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import UpdateAddressResponseObject
            schema = UpdateAddressResponseObject()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateAddress")
                print(e)

        return response
    
    async def removeAddress(self, id=None, user_id=None, request_headers:Dict={}):
        """Remove an existing customer address from the system.
        :param id : ID allotted to the selected address : type string
        :param user_id : Option to delete address for the provided user_id. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        if user_id is not None:
            payload["user_id"] = user_id

        # Parameter validation
        schema = CartValidator.removeAddress()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/address/{id}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"name":"id","description":"ID allotted to the selected address","schema":{"type":"string"},"in":"path","required":true}],"optional":[{"name":"user_id","description":"Option to delete address for the provided user_id.","in":"query","schema":{"type":"string"}}],"query":[{"name":"user_id","description":"Option to delete address for the provided user_id.","in":"query","schema":{"type":"string"}}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"name":"id","description":"ID allotted to the selected address","schema":{"type":"string"},"in":"path","required":true}]}""", serverType="platform", id=id, user_id=user_id)
        query_string = await create_query_string(user_id=user_id)
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

        response = await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=get_headers_with_signature(self._conf.domain, "delete", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/address/{id}", id=id, user_id=user_id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import DeleteAddressResponseObject
            schema = DeleteAddressResponseObject()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for removeAddress")
                print(e)

        return response
    
    async def selectAddress(self, cart_id=None, buy_now=None, i=None, b=None, body="", request_headers:Dict={}):
        """Select an address from the saved customer addresses and validates the availability of items in the cart. Additionally, it verifies and updates the delivery promise based on the selected address.
        :param cart_id :  : type string
        :param buy_now :  : type boolean
        :param i :  : type boolean
        :param b :  : type boolean
        """
        payload = {}
        
        if cart_id is not None:
            payload["cart_id"] = cart_id
        if buy_now is not None:
            payload["buy_now"] = buy_now
        if i is not None:
            payload["i"] = i
        if b is not None:
            payload["b"] = b

        # Parameter validation
        schema = CartValidator.selectAddress()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PlatformSelectCartAddressRequestObject
        schema = PlatformSelectCartAddressRequestObject()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/select-address", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}],"optional":[{"in":"query","name":"cart_id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is boolean to get buy_now cart"}},{"in":"query","name":"i","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."}},{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}}],"query":[{"in":"query","name":"cart_id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is boolean to get buy_now cart"}},{"in":"query","name":"i","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."}},{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}]}""", serverType="platform", cart_id=cart_id, buy_now=buy_now, i=i, b=b)
        query_string = await create_query_string(cart_id=cart_id, buy_now=buy_now, i=i, b=b)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/select-address", cart_id=cart_id, buy_now=buy_now, i=i, b=b), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CartDetailResponseObject
            schema = CartDetailResponseObject()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for selectAddress")
                print(e)

        return response
    
    async def getShipments(self, pick_at_store_uid=None, ordering_store_id=None, i=None, p=None, id=None, address_id=None, area_code=None, order_type=None, request_headers:Dict={}):
        """Use this API to get shipment details, expected delivery date, items and price breakup of the shipment.
        :param pick_at_store_uid :  : type integer
        :param ordering_store_id :  : type integer
        :param i : This is a boolean value. Select `true` to retrieve all the items added in the cart. : type boolean
        :param p : This is a boolean value. Select `true` for getting a payment option in response. : type boolean
        :param id : The unique identifier of the cart : type string
        :param address_id : ID allotted to the selected address : type string
        :param area_code : The PIN Code of the destination address, e.g. 400059 : type string
        :param order_type : The order type of shipment HomeDelivery - If the customer wants the order home-delivered PickAtStore - If the customer wants the handover of an order at the store itself. : type string
        """
        payload = {}
        
        if pick_at_store_uid is not None:
            payload["pick_at_store_uid"] = pick_at_store_uid
        if ordering_store_id is not None:
            payload["ordering_store_id"] = ordering_store_id
        if i is not None:
            payload["i"] = i
        if p is not None:
            payload["p"] = p
        if id is not None:
            payload["id"] = id
        if address_id is not None:
            payload["address_id"] = address_id
        if area_code is not None:
            payload["area_code"] = area_code
        if order_type is not None:
            payload["order_type"] = order_type

        # Parameter validation
        schema = CartValidator.getShipments()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/shipment", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}],"optional":[{"in":"query","name":"pick_at_store_uid","required":false,"schema":{"type":"integer","description":"ID of the store from where the order will be picked up by the customer, assuming the order_type is `PickAtStore`. This may or may not be the same as the ID of the ordering store."}},{"in":"query","name":"ordering_store_id","required":false,"schema":{"type":"integer","description":"ID of the store where the customer is ordering from."}},{"name":"i","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart.","in":"query","schema":{"type":"boolean"}},{"name":"p","description":"This is a boolean value. Select `true` for getting a payment option in response.","in":"query","schema":{"type":"boolean"}},{"name":"id","description":"The unique identifier of the cart","in":"query","schema":{"type":"string"}},{"name":"address_id","description":"ID allotted to the selected address","in":"query","schema":{"type":"string"}},{"name":"area_code","description":"The PIN Code of the destination address, e.g. 400059","in":"query","schema":{"type":"string","x-not-enum":true}},{"name":"order_type","description":"The order type of shipment HomeDelivery - If the customer wants the order home-delivered PickAtStore - If the customer wants the handover of an order at the store itself.","in":"query","schema":{"type":"string","enum":["HomeDelivery","PickAtStore"]}}],"query":[{"in":"query","name":"pick_at_store_uid","required":false,"schema":{"type":"integer","description":"ID of the store from where the order will be picked up by the customer, assuming the order_type is `PickAtStore`. This may or may not be the same as the ID of the ordering store."}},{"in":"query","name":"ordering_store_id","required":false,"schema":{"type":"integer","description":"ID of the store where the customer is ordering from."}},{"name":"i","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart.","in":"query","schema":{"type":"boolean"}},{"name":"p","description":"This is a boolean value. Select `true` for getting a payment option in response.","in":"query","schema":{"type":"boolean"}},{"name":"id","description":"The unique identifier of the cart","in":"query","schema":{"type":"string"}},{"name":"address_id","description":"ID allotted to the selected address","in":"query","schema":{"type":"string"}},{"name":"area_code","description":"The PIN Code of the destination address, e.g. 400059","in":"query","schema":{"type":"string","x-not-enum":true}},{"name":"order_type","description":"The order type of shipment HomeDelivery - If the customer wants the order home-delivered PickAtStore - If the customer wants the handover of an order at the store itself.","in":"query","schema":{"type":"string","enum":["HomeDelivery","PickAtStore"]}}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}]}""", serverType="platform", pick_at_store_uid=pick_at_store_uid, ordering_store_id=ordering_store_id, i=i, p=p, id=id, address_id=address_id, area_code=area_code, order_type=order_type)
        query_string = await create_query_string(pick_at_store_uid=pick_at_store_uid, ordering_store_id=ordering_store_id, i=i, p=p, id=id, address_id=address_id, area_code=area_code, order_type=order_type)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/shipment", pick_at_store_uid=pick_at_store_uid, ordering_store_id=ordering_store_id, i=i, p=p, id=id, address_id=address_id, area_code=area_code, order_type=order_type), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PlatformCartShipmentsResponseObject
            schema = PlatformCartShipmentsResponseObject()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getShipments")
                print(e)

        return response
    
    async def updateShipments(self, i=None, p=None, id=None, address_id=None, area_code=None, order_type=None, body="", request_headers:Dict={}):
        """Update the quantity or delivery type of the shipments. Customers can switch the order type from Home Delivery to Pick At Store and vice versa.
        :param i : This is a boolean value. Select `true` to retrieve all the items added in the cart. : type boolean
        :param p : This is a boolean value. Select `true` for getting a payment option in response. : type boolean
        :param id : The unique identifier of the cart : type string
        :param address_id : ID allotted to an address : type string
        :param area_code : The PIN Code of the destination address, e.g. 400059 : type string
        :param order_type : The order type of shipment HomeDelivery - If the customer wants the order home-delivered PickAtStore - If the customer wants the handover of an order at the store itself. : type string
        """
        payload = {}
        
        if i is not None:
            payload["i"] = i
        if p is not None:
            payload["p"] = p
        if id is not None:
            payload["id"] = id
        if address_id is not None:
            payload["address_id"] = address_id
        if area_code is not None:
            payload["area_code"] = area_code
        if order_type is not None:
            payload["order_type"] = order_type

        # Parameter validation
        schema = CartValidator.updateShipments()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UpdateCartShipmentRequestObject
        schema = UpdateCartShipmentRequestObject()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/shipment", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}],"optional":[{"name":"i","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart.","in":"query","schema":{"type":"boolean"}},{"name":"p","description":"This is a boolean value. Select `true` for getting a payment option in response.","in":"query","schema":{"type":"boolean"}},{"name":"id","description":"The unique identifier of the cart","in":"query","schema":{"type":"string"}},{"name":"address_id","description":"ID allotted to an address","in":"query","schema":{"type":"string"}},{"name":"area_code","description":"The PIN Code of the destination address, e.g. 400059","in":"query","schema":{"type":"string","x-not-enum":true}},{"name":"order_type","description":"The order type of shipment HomeDelivery - If the customer wants the order home-delivered PickAtStore - If the customer wants the handover of an order at the store itself.","in":"query","schema":{"type":"string","enum":["HomeDelivery","PickAtStore"]}}],"query":[{"name":"i","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart.","in":"query","schema":{"type":"boolean"}},{"name":"p","description":"This is a boolean value. Select `true` for getting a payment option in response.","in":"query","schema":{"type":"boolean"}},{"name":"id","description":"The unique identifier of the cart","in":"query","schema":{"type":"string"}},{"name":"address_id","description":"ID allotted to an address","in":"query","schema":{"type":"string"}},{"name":"area_code","description":"The PIN Code of the destination address, e.g. 400059","in":"query","schema":{"type":"string","x-not-enum":true}},{"name":"order_type","description":"The order type of shipment HomeDelivery - If the customer wants the order home-delivered PickAtStore - If the customer wants the handover of an order at the store itself.","in":"query","schema":{"type":"string","enum":["HomeDelivery","PickAtStore"]}}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}]}""", serverType="platform", i=i, p=p, id=id, address_id=address_id, area_code=area_code, order_type=order_type)
        query_string = await create_query_string(i=i, p=p, id=id, address_id=address_id, area_code=area_code, order_type=order_type)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/shipment", i=i, p=p, id=id, address_id=address_id, area_code=area_code, order_type=order_type), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PlatformCartShipmentsResponseObject
            schema = PlatformCartShipmentsResponseObject()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateShipments")
                print(e)

        return response
    
    async def updateCartMeta(self, id=None, buy_now=None, user_id=None, body="", request_headers:Dict={}):
        """Add or modify metadata associated with a cart, which includes customer preferences, delivery instructions, or any special requirements related to the cart items.
        :param id :  : type string
        :param buy_now :  : type boolean
        :param user_id :  : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        if buy_now is not None:
            payload["buy_now"] = buy_now
        if user_id is not None:
            payload["user_id"] = user_id

        # Parameter validation
        schema = CartValidator.updateCartMeta()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PlatformCartMetaRequestObject
        schema = PlatformCartMetaRequestObject()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/meta", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}],"optional":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"this is boolean to get buy_now cart"}},{"in":"query","name":"user_id","schema":{"type":"string","description":"Option to update cart meta for the provided user_id"}}],"query":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"this is boolean to get buy_now cart"}},{"in":"query","name":"user_id","schema":{"type":"string","description":"Option to update cart meta for the provided user_id"}}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}]}""", serverType="platform", id=id, buy_now=buy_now, user_id=user_id)
        query_string = await create_query_string(id=id, buy_now=buy_now, user_id=user_id)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/meta", id=id, buy_now=buy_now, user_id=user_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CartMetaResponseObject
            schema = CartMetaResponseObject()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for updateCartMeta")
                print(e)

        return response
    
    async def platformCheckoutCart(self, id=None, cart_type=None, body="", request_headers:Dict={}):
        """The checkout cart initiates the order creation process based on the selected address and payment method. It revalidates the cart details to ensure safe and seamless order placement.
        :param id : The unique identifier of the cart : type string
        :param cart_type : The type of cart : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        if cart_type is not None:
            payload["cart_type"] = cart_type

        # Parameter validation
        schema = CartValidator.platformCheckoutCart()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PlatformCartCheckoutDetailRequestObject
        schema = PlatformCartCheckoutDetailRequestObject()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/checkout", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}],"optional":[{"in":"query","name":"id","required":false,"schema":{"type":"string"},"description":"The unique identifier of the cart"},{"in":"query","name":"cart_type","schema":{"type":"string","enum":["universal"]},"description":"The type of cart"}],"query":[{"in":"query","name":"id","required":false,"schema":{"type":"string"},"description":"The unique identifier of the cart"},{"in":"query","name":"cart_type","schema":{"type":"string","enum":["universal"]},"description":"The type of cart"}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}]}""", serverType="platform", id=id, cart_type=cart_type)
        query_string = await create_query_string(id=id, cart_type=cart_type)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/checkout", id=id, cart_type=cart_type), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CartCheckoutResponseObject
            schema = CartCheckoutResponseObject()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for platformCheckoutCart")
                print(e)

        return response
    
    async def getAvailableDeliveryModes(self, area_code=None, id=None, request_headers:Dict={}):
        """Retrieve a list of delivery modes (home delivery/store pickup) along with a list of available pickup stores for a given cart at a specified PIN Code.
        :param area_code :  : type string
        :param id :  : type string
        """
        payload = {}
        
        if area_code is not None:
            payload["area_code"] = area_code
        if id is not None:
            payload["id"] = id

        # Parameter validation
        schema = CartValidator.getAvailableDeliveryModes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/available-delivery-mode", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"in":"query","name":"area_code","required":true,"schema":{"type":"string","x-not-enum":true,"description":"The PIN Code of the destination address, e.g. 400059"}}],"optional":[{"name":"id","in":"query","required":false,"schema":{"type":"string","description":"The unique identifier of the cart"}}],"query":[{"in":"query","name":"area_code","required":true,"schema":{"type":"string","x-not-enum":true,"description":"The PIN Code of the destination address, e.g. 400059"}},{"name":"id","in":"query","required":false,"schema":{"type":"string","description":"The unique identifier of the cart"}}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}]}""", serverType="platform", area_code=area_code, id=id)
        query_string = await create_query_string(area_code=area_code, id=id)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/available-delivery-mode", area_code=area_code, id=id), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CartDeliveryModesResponseObject
            schema = CartDeliveryModesResponseObject()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getAvailableDeliveryModes")
                print(e)

        return response
    
    async def getStoreAddressByUid(self, store_uid=None, request_headers:Dict={}):
        """Retrieve store details by entering the unique identifier of the pickup stores. Store details include the seller's name, contact information such as email address or phone number and business address.
        :param store_uid :  : type integer
        """
        payload = {}
        
        if store_uid is not None:
            payload["store_uid"] = store_uid

        # Parameter validation
        schema = CartValidator.getStoreAddressByUid()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/store-address", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"in":"query","name":"store_uid","required":true,"schema":{"type":"integer","description":"The unique identifier of the store"}}],"optional":[],"query":[{"in":"query","name":"store_uid","required":true,"schema":{"type":"integer","description":"The unique identifier of the store"}}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}]}""", serverType="platform", store_uid=store_uid)
        query_string = await create_query_string(store_uid=store_uid)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/store-address", store_uid=store_uid), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import StoreDetailsResponseObject
            schema = StoreDetailsResponseObject()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for getStoreAddressByUid")
                print(e)

        return response
    
    async def selectPaymentMode(self, id=None, buy_now=None, order_type=None, body="", request_headers:Dict={}):
        """Customers can select a preferred payment mode from available options during the cart checkout process to securely and efficiently complete their transaction.
        :param id :  : type string
        :param buy_now :  : type boolean
        :param order_type : The order type of shipment HomeDelivery - If the customer wants the order home-delivered PickAtStore - If the customer wants the handover of an order at the store itself. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        if buy_now is not None:
            payload["buy_now"] = buy_now
        if order_type is not None:
            payload["order_type"] = order_type

        # Parameter validation
        schema = CartValidator.selectPaymentMode()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UpdateCartPaymentRequestObject
        schema = UpdateCartPaymentRequestObject()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}],"optional":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is boolean to get buy_now cart"}},{"in":"query","name":"order_type","description":"The order type of shipment HomeDelivery - If the customer wants the order home-delivered PickAtStore - If the customer wants the handover of an order at the store itself.","schema":{"type":"string","description":"This is boolean to get buy_now cart","enum":["HomeDelivery"]}}],"query":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is boolean to get buy_now cart"}},{"in":"query","name":"order_type","description":"The order type of shipment HomeDelivery - If the customer wants the order home-delivered PickAtStore - If the customer wants the handover of an order at the store itself.","schema":{"type":"string","description":"This is boolean to get buy_now cart","enum":["HomeDelivery"]}}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}]}""", serverType="platform", id=id, buy_now=buy_now, order_type=order_type)
        query_string = await create_query_string(id=id, buy_now=buy_now, order_type=order_type)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment", id=id, buy_now=buy_now, order_type=order_type), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CartDetailResponseObject
            schema = CartDetailResponseObject()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for selectPaymentMode")
                print(e)

        return response
    
    async def validateCouponForPayment(self, id=None, buy_now=None, address_id=None, payment_mode=None, payment_identifier=None, aggregator_name=None, merchant_code=None, iin=None, network=None, type=None, card_id=None, cart_type=None, request_headers:Dict={}):
        """Validates the applicability of a coupon code for the selected payment mode for the existing cart. This ensures the coupon's validity before proceeding with the payment process, enhancing user experience and preventing potential errors during transactions.
        :param id :  : type string
        :param buy_now :  : type boolean
        :param address_id :  : type string
        :param payment_mode :  : type string
        :param payment_identifier :  : type string
        :param aggregator_name :  : type string
        :param merchant_code :  : type string
        :param iin : Debit/Credit card prefix (first 6 digit) : type string
        :param network : Credit/Debit card issuer, e.g. VISA, MASTERCARD, RUPAY : type string
        :param type : card type, e.g. Credit, Debit : type string
        :param card_id : saved card token reference id : type string
        :param cart_type : type of the cart : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        if buy_now is not None:
            payload["buy_now"] = buy_now
        if address_id is not None:
            payload["address_id"] = address_id
        if payment_mode is not None:
            payload["payment_mode"] = payment_mode
        if payment_identifier is not None:
            payload["payment_identifier"] = payment_identifier
        if aggregator_name is not None:
            payload["aggregator_name"] = aggregator_name
        if merchant_code is not None:
            payload["merchant_code"] = merchant_code
        if iin is not None:
            payload["iin"] = iin
        if network is not None:
            payload["network"] = network
        if type is not None:
            payload["type"] = type
        if card_id is not None:
            payload["card_id"] = card_id
        if cart_type is not None:
            payload["cart_type"] = cart_type

        # Parameter validation
        schema = CartValidator.validateCouponForPayment()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/validate/", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}],"optional":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is boolean to get buy_now cart"}},{"in":"query","name":"address_id","schema":{"type":"string","description":"ID allotted to an address"}},{"in":"query","name":"payment_mode","schema":{"type":"string","description":"Payment mode selected by the customer"}},{"in":"query","name":"payment_identifier","schema":{"type":"string","description":"Identifier of payment like ICIC, PAYTM"}},{"in":"query","name":"aggregator_name","schema":{"type":"string","description":"Payment gateway identifier"}},{"in":"query","name":"merchant_code","schema":{"type":"string","x-not-enum":true,"description":"Identifier used by payment gateway for a given payment mode, e.g. NB_ICIC, PAYTM"}},{"in":"query","name":"iin","schema":{"type":"string"},"description":"Debit/Credit card prefix (first 6 digit)"},{"in":"query","name":"network","schema":{"type":"string"},"description":"Credit/Debit card issuer, e.g. VISA, MASTERCARD, RUPAY"},{"in":"query","name":"type","schema":{"type":"string"},"description":"card type, e.g. Credit, Debit"},{"in":"query","name":"card_id","schema":{"type":"string"},"description":"saved card token reference id"},{"in":"query","name":"cart_type","schema":{"type":"string","enum":["universal"]},"description":"type of the cart"}],"query":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is boolean to get buy_now cart"}},{"in":"query","name":"address_id","schema":{"type":"string","description":"ID allotted to an address"}},{"in":"query","name":"payment_mode","schema":{"type":"string","description":"Payment mode selected by the customer"}},{"in":"query","name":"payment_identifier","schema":{"type":"string","description":"Identifier of payment like ICIC, PAYTM"}},{"in":"query","name":"aggregator_name","schema":{"type":"string","description":"Payment gateway identifier"}},{"in":"query","name":"merchant_code","schema":{"type":"string","x-not-enum":true,"description":"Identifier used by payment gateway for a given payment mode, e.g. NB_ICIC, PAYTM"}},{"in":"query","name":"iin","schema":{"type":"string"},"description":"Debit/Credit card prefix (first 6 digit)"},{"in":"query","name":"network","schema":{"type":"string"},"description":"Credit/Debit card issuer, e.g. VISA, MASTERCARD, RUPAY"},{"in":"query","name":"type","schema":{"type":"string"},"description":"card type, e.g. Credit, Debit"},{"in":"query","name":"card_id","schema":{"type":"string"},"description":"saved card token reference id"},{"in":"query","name":"cart_type","schema":{"type":"string","enum":["universal"]},"description":"type of the cart"}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}]}""", serverType="platform", id=id, buy_now=buy_now, address_id=address_id, payment_mode=payment_mode, payment_identifier=payment_identifier, aggregator_name=aggregator_name, merchant_code=merchant_code, iin=iin, network=network, type=type, card_id=card_id, cart_type=cart_type)
        query_string = await create_query_string(id=id, buy_now=buy_now, address_id=address_id, payment_mode=payment_mode, payment_identifier=payment_identifier, aggregator_name=aggregator_name, merchant_code=merchant_code, iin=iin, network=network, type=type, card_id=card_id, cart_type=cart_type)
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

        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/payment/validate/", id=id, buy_now=buy_now, address_id=address_id, payment_mode=payment_mode, payment_identifier=payment_identifier, aggregator_name=aggregator_name, merchant_code=merchant_code, iin=iin, network=network, type=type, card_id=card_id, cart_type=cart_type), query_string, headers, "", exclude_headers=exclude_headers), data="", debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import PaymentCouponValidate
            schema = PaymentCouponValidate()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for validateCouponForPayment")
                print(e)

        return response
    
    async def platformCheckoutCartV2(self, id=None, cart_type=None, body="", request_headers:Dict={}):
        """The checkout cart initiates the order creation process based on the items in the user’s cart,  their selected address, and chosen payment methods. It also supports multiple payment method  options and revalidates the cart details to ensure a secure and seamless order placement.
        :param id : The unique identifier of the cart : type string
        :param cart_type : The type of cart : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        if cart_type is not None:
            payload["cart_type"] = cart_type

        # Parameter validation
        schema = CartValidator.platformCheckoutCartV2()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PlatformCartCheckoutDetailV2RequestObject
        schema = PlatformCartCheckoutDetailV2RequestObject()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/checkout", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}],"optional":[{"in":"query","name":"id","required":false,"schema":{"type":"string"},"description":"The unique identifier of the cart"},{"in":"query","name":"cart_type","schema":{"type":"string","enum":["universal"]},"description":"The type of cart"}],"query":[{"in":"query","name":"id","required":false,"schema":{"type":"string"},"description":"The unique identifier of the cart"},{"in":"query","name":"cart_type","schema":{"type":"string","enum":["universal"]},"description":"The type of cart"}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}]}""", serverType="platform", id=id, cart_type=cart_type)
        query_string = await create_query_string(id=id, cart_type=cart_type)
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

        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/cart/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/checkout", id=id, cart_type=cart_type), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CartCheckoutResponseObject
            schema = CartCheckoutResponseObject()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for platformCheckoutCartV2")
                print(e)

        return response
    
    async def selectPaymentModeV2(self, id=None, buy_now=None, order_type=None, body="", request_headers:Dict={}):
        """Selection of payment mode that supports multiple MOP(mode of payment).
        :param id :  : type string
        :param buy_now :  : type boolean
        :param order_type : The order type of shipment HomeDelivery - If the customer wants the order home-delivered PickAtStore - If the customer wants the handover of an order at the store itself. : type string
        """
        payload = {}
        
        if id is not None:
            payload["id"] = id
        if buy_now is not None:
            payload["buy_now"] = buy_now
        if order_type is not None:
            payload["order_type"] = order_type

        # Parameter validation
        schema = CartValidator.selectPaymentModeV2()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UpdateCartPaymentRequestV2
        schema = UpdateCartPaymentRequestV2()
        schema.dump(schema.load(body))

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/payment", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}],"optional":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is boolean to get buy_now cart"}},{"in":"query","name":"order_type","description":"The order type of shipment HomeDelivery - If the customer wants the order home-delivered PickAtStore - If the customer wants the handover of an order at the store itself.","schema":{"type":"string","description":"This is boolean to get buy_now cart","enum":["HomeDelivery","PickAtStore"]}}],"query":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"buy_now","schema":{"type":"boolean","description":"This is boolean to get buy_now cart"}},{"in":"query","name":"order_type","description":"The order type of shipment HomeDelivery - If the customer wants the order home-delivered PickAtStore - If the customer wants the handover of an order at the store itself.","schema":{"type":"string","description":"This is boolean to get buy_now cart","enum":["HomeDelivery","PickAtStore"]}}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}]}""", serverType="platform", id=id, buy_now=buy_now, order_type=order_type)
        query_string = await create_query_string(id=id, buy_now=buy_now, order_type=order_type)
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

        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/cart/v2.0/company/{self._conf.companyId}/application/{self.applicationId}/payment", id=id, buy_now=buy_now, order_type=order_type), query_string, headers, body, exclude_headers=exclude_headers), data=body, debug=(self._conf.logLevel=="DEBUG"))

        if 200 <= int(response['status_code']) < 300:
            from .models import CartDetailResponseObject
            schema = CartDetailResponseObject()
            try:
                schema.load(response["json"])
            except Exception as e:
                print("Response Validation failed for selectPaymentModeV2")
                print(e)

        return response
    