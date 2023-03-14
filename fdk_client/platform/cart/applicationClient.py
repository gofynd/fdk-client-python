

"""Cart Platform Client."""

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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/coupon", page_no=page_no, page_size=page_size, is_archived=is_archived, title=title, is_public=is_public, is_display=is_display, type_slug=type_slug, code=code), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/coupon", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/coupon/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
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
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/coupon/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
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
        return await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/coupon/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/promotion", page_no=page_no, page_size=page_size, q=q, is_active=is_active, promo_group=promo_group, promotion_type=promotion_type, fp_panel=fp_panel, promotion_id=promotion_id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/promotion", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
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
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=get_headers_with_signature(self._conf.domain, "get", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/promotion/{id}", id=id), query_string, headers, "", exclude_headers=exclude_headers), data="")
    
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
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=get_headers_with_signature(self._conf.domain, "put", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/promotion/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
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
        return await AiohttpHelper().aiohttp_request("PATCH", url_with_params, headers=get_headers_with_signature(self._conf.domain, "patch", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/promotion/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/cart/validate", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/cart/serviceability", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    
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
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=get_headers_with_signature(self._conf.domain, "post", await create_url_without_domain(f"/service/platform/cart/v1.0/company/{self._conf.companyId}/application/{self.applicationId}/cart/checkout", ), query_string, headers, body, exclude_headers=exclude_headers), data=body)
    

