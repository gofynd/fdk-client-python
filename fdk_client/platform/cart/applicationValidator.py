

"""Cart Platform Application Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema



    
    
        
        
        
        
        
        
        
        
        
        
    
    
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
        
        
        
        
        
        
        
    
    
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
        
        
        
        
        
        
        
    
    
        
        
        
        
        
    
    
        
        
        
        
    
    
        
        
        
        
    
    
        
        
    
    
        
        
        
    
    
        
        
        

class CartValidator:
    
    
    class getCoupons(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        is_archived = fields.Boolean(required=False)
        
        title = fields.Str(required=False)
        
        is_public = fields.Boolean(required=False)
        
        is_display = fields.Boolean(required=False)
        
        type_slug = fields.Str(required=False)
        
        code = fields.Str(required=False)
         
        
    
    class createCoupon(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getCouponById(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class updateCoupon(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class updateCouponPartially(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class getPromotions(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        q = fields.Str(required=False)
        
        is_active = fields.Boolean(required=False)
        
        promo_group = fields.Str(required=False)
        
        promotion_type = fields.Str(required=False)
        
        fp_panel = fields.Str(required=False)
        
        promotion_id = fields.Str(required=False)
         
        
    
    class createPromotion(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getPromotionById(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class updatePromotion(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class updatePromotionPartially(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class updateCartMetaConfig(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        cart_meta_id = fields.Str(required=False)
         
        
    
    class fetchCartMetaConfig(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class createCartMetaConfig(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class fetchAndvalidateCartItems(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class checkCartServiceability(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class checkoutCart(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getAbandonedCart(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        from_date = fields.Str(required=False)
        
        to_date = fields.Str(required=False)
        
        anonymous_cart = fields.Boolean(required=False)
        
        last_id = fields.Str(required=False)
        
        sort_on = fields.Str(required=False)
         
        
    
    class getAbandonedCartDetails(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
        
        i = fields.Boolean(required=False)
        
        b = fields.Boolean(required=False)
         
        
    
    class addItems(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        cart_id = fields.Str(required=False)
        
        b = fields.Boolean(required=False)
         
        
    
    class updateCart(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        cart_id = fields.Str(required=False)
        
        b = fields.Boolean(required=False)
         
        
    
    class getCouponOptionValues(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getCouponCodeExists(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        code = fields.Str(required=False)
         
        
    
    class getPromotionCodeExists(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        code = fields.Str(required=False)
         
        
    
    

