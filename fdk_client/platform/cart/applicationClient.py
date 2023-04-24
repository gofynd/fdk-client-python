

"""Cart Platform Client"""

from ...common.aiohttp_helper import AiohttpHelper
from ...common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .applicationValidator import CartValidator

class Cart:
    def __init__(self, config, applicationId):
        self._conf = config
        self.applicationId = applicationId

    
    async def getCoupons(self, page_no=None, page_size=None, is_archived=None, title=None, is_public=None, is_display=None, type_slug=None, code=None):
        """Get coupon list with pagination
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
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if is_archived:
            payload["is_archived"] = is_archived
        
        if title:
            payload["title"] = title
        
        if is_public:
            payload["is_public"] = is_public
        
        if is_display:
            payload["is_display"] = is_display
        
        if type_slug:
            payload["type_slug"] = type_slug
        
        if code:
            payload["code"] = code
        

        # Parameter validation
        schema = CartValidator.getCoupons()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/coupon", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer","default":0,"description":"current page no as per pagination"}},{"name":"page_size","in":"query","schema":{"type":"integer","default":10,"description":"Coupon max records fetched in single request"}},{"name":"is_archived","in":"query","schema":{"type":"boolean","description":"Filter by active or inactive coupon","default":false}},{"name":"title","in":"query","schema":{"type":"string","description":"Filter by `title`"}},{"name":"is_public","in":"query","schema":{"type":"boolean","description":"Filter by `is_public`"}},{"name":"is_display","in":"query","schema":{"type":"boolean","description":"Filter by `is_display`"}},{"name":"type_slug","in":"query","schema":{"type":"string","description":"Filter by coupon type"}},{"name":"code","in":"query","schema":{"type":"string","description":"Filter by `code`"}}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer","default":0,"description":"current page no as per pagination"}},{"name":"page_size","in":"query","schema":{"type":"integer","default":10,"description":"Coupon max records fetched in single request"}},{"name":"is_archived","in":"query","schema":{"type":"boolean","description":"Filter by active or inactive coupon","default":false}},{"name":"title","in":"query","schema":{"type":"string","description":"Filter by `title`"}},{"name":"is_public","in":"query","schema":{"type":"boolean","description":"Filter by `is_public`"}},{"name":"is_display","in":"query","schema":{"type":"boolean","description":"Filter by `is_display`"}},{"name":"type_slug","in":"query","schema":{"type":"string","description":"Filter by coupon type"}},{"name":"code","in":"query","schema":{"type":"string","description":"Filter by `code`"}}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}]}""", page_no=page_no, page_size=page_size, is_archived=is_archived, title=title, is_public=is_public, is_display=is_display, type_slug=type_slug, code=code)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, is_archived=is_archived, title=title, is_public=is_public, is_display=is_display, type_slug=type_slug, code=code)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/coupon", page_no=page_no, page_size=page_size, is_archived=is_archived, title=title, is_public=is_public, is_display=is_display, type_slug=type_slug, code=code), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        from .models import CouponsResponse
        schema = CouponsResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getCoupons")
            print(e)

        

        return response
    
    async def createCoupon(self, body=""):
        """Create new coupon
        """
        payload = {}
        

        # Parameter validation
        schema = CartValidator.createCoupon()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CouponAdd
        schema = CouponAdd()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/coupon", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/coupon", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        from .models import SuccessMessage
        schema = SuccessMessage()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for createCoupon")
            print(e)

        

        return response
    
    async def getCouponById(self, id=None):
        """Get single coupon details with `id` in path param
        :param id :  : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CartValidator.getCouponById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/coupon/{id}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"name":"id","in":"path","required":true,"schema":{"type":"string","description":"Coupon mongo _id for fetching single coupon data for editing"}}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"name":"id","in":"path","required":true,"schema":{"type":"string","description":"Coupon mongo _id for fetching single coupon data for editing"}}]}""", id=id)
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/coupon/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        from .models import CouponUpdate
        schema = CouponUpdate()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getCouponById")
            print(e)

        

        return response
    
    async def updateCoupon(self, id=None, body=""):
        """Update coupon with id sent in `id`
        :param id :  : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CartValidator.updateCoupon()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CouponUpdate
        schema = CouponUpdate()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/coupon/{id}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"name":"id","in":"path","schema":{"type":"string","description":"Coupon mongo _id for fetching single coupon data for editing"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"name":"id","in":"path","schema":{"type":"string","description":"Coupon mongo _id for fetching single coupon data for editing"},"required":true}]}""", id=id)
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
        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/coupon/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        from .models import SuccessMessage
        schema = SuccessMessage()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for updateCoupon")
            print(e)

        

        return response
    
    async def updateCouponPartially(self, id=None, body=""):
        """Update archive/unarchive and change schedule for coupon
        :param id :  : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CartValidator.updateCouponPartially()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import CouponPartialUpdate
        schema = CouponPartialUpdate()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/coupon/{id}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"name":"id","in":"path","schema":{"type":"string","description":"Coupon mongo _id for fetching single coupon data for editing"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"name":"id","in":"path","schema":{"type":"string","description":"Coupon mongo _id for fetching single coupon data for editing"},"required":true}]}""", id=id)
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
        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/coupon/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        from .models import SuccessMessage
        schema = SuccessMessage()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for updateCouponPartially")
            print(e)

        

        return response
    
    async def getPromotions(self, page_no=None, page_size=None, q=None, is_active=None, promo_group=None, promotion_type=None, fp_panel=None, promotion_id=None):
        """Get promotion list with pagination
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
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if q:
            payload["q"] = q
        
        if is_active:
            payload["is_active"] = is_active
        
        if promo_group:
            payload["promo_group"] = promo_group
        
        if promotion_type:
            payload["promotion_type"] = promotion_type
        
        if fp_panel:
            payload["fp_panel"] = fp_panel
        
        if promotion_id:
            payload["promotion_id"] = promotion_id
        

        # Parameter validation
        schema = CartValidator.getPromotions()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/promotion", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer","default":0,"description":"current page no as per pagination"}},{"name":"page_size","in":"query","schema":{"type":"integer","default":10,"description":"Promotion max records fetched in single request"}},{"name":"q","in":"query","schema":{"type":"string","description":"Filter by name"}},{"name":"is_active","in":"query","schema":{"type":"boolean","description":"Filter by active or inactive promotion","default":true}},{"name":"promo_group","in":"query","schema":{"type":"string","description":"Filter promotion group","enum":["product","cart","contract","ladder_price","limited_timer"]}},{"name":"promotion_type","in":"query","schema":{"type":"string","description":"Filter promotion type"}},{"name":"fp_panel","in":"query","schema":{"type":"string","description":"Filter non extension promotions"}},{"name":"promotion_id","in":"query","schema":{"type":"string","description":"Filter by promotion _id"}}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer","default":0,"description":"current page no as per pagination"}},{"name":"page_size","in":"query","schema":{"type":"integer","default":10,"description":"Promotion max records fetched in single request"}},{"name":"q","in":"query","schema":{"type":"string","description":"Filter by name"}},{"name":"is_active","in":"query","schema":{"type":"boolean","description":"Filter by active or inactive promotion","default":true}},{"name":"promo_group","in":"query","schema":{"type":"string","description":"Filter promotion group","enum":["product","cart","contract","ladder_price","limited_timer"]}},{"name":"promotion_type","in":"query","schema":{"type":"string","description":"Filter promotion type"}},{"name":"fp_panel","in":"query","schema":{"type":"string","description":"Filter non extension promotions"}},{"name":"promotion_id","in":"query","schema":{"type":"string","description":"Filter by promotion _id"}}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}]}""", page_no=page_no, page_size=page_size, q=q, is_active=is_active, promo_group=promo_group, promotion_type=promotion_type, fp_panel=fp_panel, promotion_id=promotion_id)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, q=q, is_active=is_active, promo_group=promo_group, promotion_type=promotion_type, fp_panel=fp_panel, promotion_id=promotion_id)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/promotion", page_no=page_no, page_size=page_size, q=q, is_active=is_active, promo_group=promo_group, promotion_type=promotion_type, fp_panel=fp_panel, promotion_id=promotion_id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        from .models import PromotionsResponse
        schema = PromotionsResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getPromotions")
            print(e)

        

        return response
    
    async def createPromotion(self, body=""):
        """Create new promotion
        """
        payload = {}
        

        # Parameter validation
        schema = CartValidator.createPromotion()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PromotionAdd
        schema = PromotionAdd()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/promotion", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/promotion", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        from .models import PromotionAdd
        schema = PromotionAdd()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for createPromotion")
            print(e)

        

        return response
    
    async def getPromotionById(self, id=None):
        """Get single promotion details with `id` in path param
        :param id :  : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CartValidator.getPromotionById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/promotion/{id}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"name":"id","in":"path","required":true,"schema":{"type":"string","description":"Promotion mongo _id for fetching single promotion data for editing"}}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"name":"id","in":"path","required":true,"schema":{"type":"string","description":"Promotion mongo _id for fetching single promotion data for editing"}}]}""", id=id)
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
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/promotion/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        from .models import PromotionUpdate
        schema = PromotionUpdate()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getPromotionById")
            print(e)

        

        return response
    
    async def updatePromotion(self, id=None, body=""):
        """Update promotion with id sent in `id`
        :param id :  : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CartValidator.updatePromotion()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PromotionUpdate
        schema = PromotionUpdate()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/promotion/{id}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"name":"id","in":"path","schema":{"type":"string","description":"Promotion mongo _id for fetching single promotion data for editing"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"name":"id","in":"path","schema":{"type":"string","description":"Promotion mongo _id for fetching single promotion data for editing"},"required":true}]}""", id=id)
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
        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/promotion/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        from .models import PromotionUpdate
        schema = PromotionUpdate()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for updatePromotion")
            print(e)

        

        return response
    
    async def updatePromotionPartially(self, id=None, body=""):
        """Update publish/unpublish and change schedule for promotion
        :param id :  : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        

        # Parameter validation
        schema = CartValidator.updatePromotionPartially()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import PromotionPartialUpdate
        schema = PromotionPartialUpdate()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/promotion/{id}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"name":"id","in":"path","schema":{"type":"string","description":"Promotion mongo _id for fetching single promotion data for editing"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"name":"id","in":"path","schema":{"type":"string","description":"Promotion mongo _id for fetching single promotion data for editing"},"required":true}]}""", id=id)
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
        response = await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/promotion/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        from .models import SuccessMessage
        schema = SuccessMessage()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for updatePromotionPartially")
            print(e)

        

        return response
    
    async def fetchAndvalidateCartItems(self, body=""):
        """Get all the details of cart for a list of provided `cart_items`
        """
        payload = {}
        

        # Parameter validation
        schema = CartValidator.fetchAndvalidateCartItems()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import OpenapiCartDetailsRequest
        schema = OpenapiCartDetailsRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/cart/validate", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/cart/validate", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        from .models import OpenapiCartDetailsResponse
        schema = OpenapiCartDetailsResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for fetchAndvalidateCartItems")
            print(e)

        

        return response
    
    async def checkCartServiceability(self, body=""):
        """Check Pincode serviceability for cart items provided in `cart_items` and address pincode in `shipping_address`
        """
        payload = {}
        

        # Parameter validation
        schema = CartValidator.checkCartServiceability()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import OpenApiCartServiceabilityRequest
        schema = OpenApiCartServiceabilityRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/cart/serviceability", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/cart/serviceability", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        from .models import OpenApiCartServiceabilityResponse
        schema = OpenApiCartServiceabilityResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for checkCartServiceability")
            print(e)

        

        return response
    
    async def checkoutCart(self, body=""):
        """Generate Fynd order for cart details send with provided `cart_items`
        """
        payload = {}
        

        # Parameter validation
        schema = CartValidator.checkoutCart()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import OpenApiPlatformCheckoutReq
        schema = OpenApiPlatformCheckoutReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/cart/checkout", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}],"optional":[],"query":[],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}]}""", )
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
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/cart/checkout", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        from .models import OpenApiCheckoutResponse
        schema = OpenApiCheckoutResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for checkoutCart")
            print(e)

        

        return response
    
    async def getAbandonedCart(self, page_no=None, page_size=None, from_date=None, to_date=None, anonymous_cart=None, last_id=None, sort_on=None):
        """Get abandoned cart list with pagination
        :param page_no :  : type integer
        :param page_size :  : type integer
        :param from_date :  : type string
        :param to_date :  : type string
        :param anonymous_cart :  : type boolean
        :param last_id :  : type string
        :param sort_on :  : type string
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if from_date:
            payload["from_date"] = from_date
        
        if to_date:
            payload["to_date"] = to_date
        
        if anonymous_cart:
            payload["anonymous_cart"] = anonymous_cart
        
        if last_id:
            payload["last_id"] = last_id
        
        if sort_on:
            payload["sort_on"] = sort_on
        

        # Parameter validation
        schema = CartValidator.getAbandonedCart()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/abandoned/carts", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer","default":0,"description":"current page no as per pagination"}},{"name":"page_size","in":"query","schema":{"type":"integer","default":10,"description":"Coupon max records fetched in single request"}},{"name":"from_date","in":"query","schema":{"type":"string","description":"Cart which are created on or after from_date"}},{"name":"to_date","in":"query","schema":{"type":"string","description":"Cart which are created on or before to_date"}},{"name":"anonymous_cart","in":"query","schema":{"type":"boolean","description":"Filter by `anonymous_cart`"}},{"name":"last_id","in":"query","schema":{"type":"string","description":"pagination is done based on the last_object_id"}},{"name":"sort_on","in":"query","schema":{"type":"string","description":"on which column to sort on i.e created_on or last_modified"}}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer","default":0,"description":"current page no as per pagination"}},{"name":"page_size","in":"query","schema":{"type":"integer","default":10,"description":"Coupon max records fetched in single request"}},{"name":"from_date","in":"query","schema":{"type":"string","description":"Cart which are created on or after from_date"}},{"name":"to_date","in":"query","schema":{"type":"string","description":"Cart which are created on or before to_date"}},{"name":"anonymous_cart","in":"query","schema":{"type":"boolean","description":"Filter by `anonymous_cart`"}},{"name":"last_id","in":"query","schema":{"type":"string","description":"pagination is done based on the last_object_id"}},{"name":"sort_on","in":"query","schema":{"type":"string","description":"on which column to sort on i.e created_on or last_modified"}}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}]}""", page_no=page_no, page_size=page_size, from_date=from_date, to_date=to_date, anonymous_cart=anonymous_cart, last_id=last_id, sort_on=sort_on)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, from_date=from_date, to_date=to_date, anonymous_cart=anonymous_cart, last_id=last_id, sort_on=sort_on)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/abandoned/carts", page_no=page_no, page_size=page_size, from_date=from_date, to_date=to_date, anonymous_cart=anonymous_cart, last_id=last_id, sort_on=sort_on), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        from .models import AbandonedCartResponse
        schema = AbandonedCartResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getAbandonedCart")
            print(e)

        

        return response
    
    async def getAbandonedCartDetails(self, id=None, i=None, b=None):
        """Use this API to get details of all the items added to a cart.
        :param id :  : type string
        :param i :  : type boolean
        :param b :  : type boolean
        """
        payload = {}
        
        if id:
            payload["id"] = id
        
        if i:
            payload["i"] = i
        
        if b:
            payload["b"] = b
        

        # Parameter validation
        schema = CartValidator.getAbandonedCartDetails()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/abandoned/cart/detail", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}],"optional":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"i","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."}},{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}}],"query":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"i","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."}},{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"}]}""", id=id, i=i, b=b)
        query_string = await create_query_string(id=id, i=i, b=b)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/abandoned/cart/detail", id=id, i=i, b=b), query_string, headers, "", exclude_headers=exclude_headers), data="")

        

        from .models import CartDetailResponse
        schema = CartDetailResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for getAbandonedCartDetails")
            print(e)

        

        return response
    
    async def addItems(self, cart_id=None, b=None, body=""):
        """Use this API to add items to the abandoned cart.
        :param cart_id : Current Cart _id : type string
        :param b :  : type boolean
        """
        payload = {}
        
        if cart_id:
            payload["cart_id"] = cart_id
        
        if b:
            payload["b"] = b
        

        # Parameter validation
        schema = CartValidator.addItems()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import AddCartRequest
        schema = AddCartRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/abandoned/carts/{cart_id}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"schema":{"type":"string"},"description":"Current Cart _id","in":"path","required":true,"name":"cart_id"}],"optional":[{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}}],"query":[{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"schema":{"type":"string"},"description":"Current Cart _id","in":"path","required":true,"name":"cart_id"}]}""", cart_id=cart_id, b=b)
        query_string = await create_query_string(cart_id=cart_id, b=b)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/abandoned/carts/{cart_id}", cart_id=cart_id, b=b), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        from .models import AddCartDetailResponse
        schema = AddCartDetailResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for addItems")
            print(e)

        

        return response
    
    async def updateCart(self, cart_id=None, b=None, body=""):
        """<p>Use this API to update items added to the cart with the help of a request object containing attributes like item_quantity and item_size. These attributes will be fetched from the following APIs</p> <ul> <li><font color="monochrome">operation</font> Operation for current api call. <b>update_item</b> for update items. <b>remove_item</b> for removing items.</li> <li> <font color="monochrome">item_id</font>  "/platform/content/v1/products/"</li> <li> <font color="monochrome">item_size</font>   "/platform/content/v1/products/:slug/sizes/"</li> <li> <font color="monochrome">quantity</font>  item quantity (must be greater than or equal to 1)</li> <li> <font color="monochrome">article_id</font>   "/content​/v1​/products​/:identifier​/sizes​/price​/"</li> <li> <font color="monochrome">item_index</font>  item position in the cart (must be greater than or equal to 0)</li> </ul>
        :param cart_id : Current Cart _id : type string
        :param b :  : type boolean
        """
        payload = {}
        
        if cart_id:
            payload["cart_id"] = cart_id
        
        if b:
            payload["b"] = b
        

        # Parameter validation
        schema = CartValidator.updateCart()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models import UpdateCartRequest
        schema = UpdateCartRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(self._conf.domain, f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/abandoned/carts/{cart_id}", """{"required":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"schema":{"type":"string"},"description":"Current Cart _id","in":"path","required":true,"name":"cart_id"}],"optional":[{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}}],"query":[{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}}],"headers":[],"path":[{"schema":{"type":"string"},"description":"Current company id","in":"path","required":true,"name":"company_id"},{"schema":{"type":"string"},"description":"Current Application _id","in":"path","required":true,"name":"application_id"},{"schema":{"type":"string"},"description":"Current Cart _id","in":"path","required":true,"name":"cart_id"}]}""", cart_id=cart_id, b=b)
        query_string = await create_query_string(cart_id=cart_id, b=b)
        headers = {
            "Authorization": "Bearer " + await self._conf.getAccessToken()
        }
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        response = await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/abandoned/carts/{cart_id}", cart_id=cart_id, b=b), query_string, headers, body, exclude_headers=exclude_headers), data=body)

        

        from .models import UpdateCartDetailResponse
        schema = UpdateCartDetailResponse()
        try:
            schema.dump(schema.load(response))
        except Exception as e:
            print("Response Validation failed for updateCart")
            print(e)

        

        return response
    

