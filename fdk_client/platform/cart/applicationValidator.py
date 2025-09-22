

"""Cart Platform Application Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema



    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
        
    
    
        
        
        
        
        
        
        
        
        
        
    
    
        
        
        
        
    
    
        
        
        
    
    
        
        
    
    
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
    
    
        
        
        
    
    
                
from .models import OrderingSource

        
        
    
    
                
from .models import OrderingSource

        
        
    
    
                
from .models import OrderingSource

        
        
    
    
        
        
        
        
        
        
        
        
        
    
    
        
        
        
        
        
        
    
    
        
        
        
        
    
    
        
        
        
        
    
    
        
        
    
    
        
        
        
    
    
        
        
        
    
    
                
from .models import OrderingSource

        
        
    
    
        
        
    
    
        
        
        
    
    
        
        
        
        
        
    
    
        
        
        
        
        
    
    
        
        
        
    
    
                
from .models import OrderingSource

        
        
        
        
        
        
        
        
        
    
    
                
from .models import OrderingSource

        
        
        
        
        
        
        
    
    
                
from .models import OrderingSource

        
        
        
        
        
        
        
    
    
        
        
        
    
    
        
        
        
        
    
    
        
        
        
        
        
        
    
    
                
from .models import OrderingSource

        
        
        
        
        
        
        
    
    
                
from .models import OrderingSource

        
        
        
        
    
    
        
        
        
        
        
        
        
        
        
    
    
        
        
    
    
        
        
        
        
        
        
        
        
        
        
    
    
        
        
        
    
    
        
        
        
        
    
    
                
from .models import OrderingSource

        
        
        
        
        
        
    
    
        
        
        
        
        
        
        
        
        
        
    
    
        
        
        
        
        
        
        
        
    
    
        
        
        
        
    
    
                
from .models import OrderingSource

        
        
        
    
    
        
        
        
        
    
    
        
        
        
    
    
                
from .models import OrderingSource

        
        
        
        
        
    
    
                
from .models import OrderingSource

        
        
        
        
        
        
        
        
        
    
    
                
from .models import OrderingSource

        
        
        
    
    
                
from .models import OrderingSource

        
        
        
        
        
    
    
                
from .models import OrderingSource

        
        
        
        
        
        

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
        
        created_by = fields.Str(required=False)
        
        reviewed_by = fields.Str(required=False)
        
        approved_start_time = fields.Str(required=False)
        
        approved_end_time = fields.Str(required=False)
        
        review_start_time = fields.Str(required=False)
        
        review_end_time = fields.Str(required=False)
        
        status = fields.Str(required=False)
         
        
    
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
         
        
    
    class deleteCoupon(BaseSchema):
        
        
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
        
        created_by = fields.Str(required=False)
        
        reviewed_by = fields.Str(required=False)
        
        approved_start_time = fields.Str(required=False)
        
        approved_end_time = fields.Str(required=False)
        
        review_start_time = fields.Str(required=False)
        
        review_end_time = fields.Str(required=False)
        
        status = fields.Str(required=False)
         
        
    
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
         
        
    
    class deletePromotion(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class getPromosCouponConfig(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        entity_type = fields.Str(required=False)
        
        is_hidden = fields.Boolean(required=False)
         
        
    
    class getPromotionOffers(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        slug = fields.Str(required=False)
        
        page_size = fields.Int(required=False)
        
        promotion_group = fields.Str(required=False)
        
        store_id = fields.Int(required=False)
        
        cart_type = fields.Str(required=False)
        
        promotion_type = fields.Str(required=False)
        
        cart_id = fields.Str(required=False)
        
        auto_apply = fields.Boolean(required=False)
         
        
    
    class getPromotionPaymentOffers(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
        
        uid = fields.Int(required=False)
         
        
    
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
         
        
    
    class updatePriceAdjustment(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class removePriceAdjustment(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class addPriceAdjustment(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getPriceAdjustments(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        cart_id = fields.Str(required=False)
         
        
    
    class fetchAndvalidateCartItems(BaseSchema):
        
        
        x__ordering__source = fields.Nested(OrderingSource, required=False)
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class checkCartServiceability(BaseSchema):
        
        
        x__ordering__source = fields.Nested(OrderingSource, required=False)
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class checkoutCart(BaseSchema):
        
        
        x__ordering__source = fields.Nested(OrderingSource, required=False)
        
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
        
        c = fields.Boolean(required=False)
         
        
    
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
         
        
    
    class overrideCart(BaseSchema):
        
        
        x__ordering__source = fields.Nested(OrderingSource, required=False)
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getCartShareLink(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getCartSharedItems(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        token = fields.Str(required=False)
         
        
    
    class updateCartWithSharedItems(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        token = fields.Str(required=False)
        
        action = fields.Str(required=False)
        
        cart_id = fields.Str(required=False)
         
        
    
    class getCartList(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        from_date = fields.Str(required=False)
        
        to_date = fields.Str(required=False)
        
        filter_on = fields.Str(required=False)
         
        
    
    class updateCartUser(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class getCart(BaseSchema):
        
        
        x__ordering__source = fields.Nested(OrderingSource, required=False)
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
        
        user_id = fields.Str(required=False)
        
        order_type = fields.Str(required=False)
        
        i = fields.Boolean(required=False)
        
        b = fields.Boolean(required=False)
        
        assign_card_id = fields.Int(required=False)
        
        buy_now = fields.Boolean(required=False)
         
        
    
    class platformAddItems(BaseSchema):
        
        
        x__ordering__source = fields.Nested(OrderingSource, required=False)
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        i = fields.Boolean(required=False)
        
        b = fields.Boolean(required=False)
        
        buy_now = fields.Boolean(required=False)
        
        order_type = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class platformUpdateCart(BaseSchema):
        
        
        x__ordering__source = fields.Nested(OrderingSource, required=False)
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
        
        i = fields.Boolean(required=False)
        
        order_type = fields.Str(required=False)
        
        b = fields.Boolean(required=False)
        
        buy_now = fields.Boolean(required=False)
         
        
    
    class deleteCart(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class getItemCount(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
        
        buy_now = fields.Boolean(required=False)
         
        
    
    class getAppCoupons(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
        
        buy_now = fields.Boolean(required=False)
        
        slug = fields.Str(required=False)
        
        store_id = fields.Str(required=False)
         
        
    
    class applyCoupon(BaseSchema):
        
        
        x__ordering__source = fields.Nested(OrderingSource, required=False)
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        i = fields.Boolean(required=False)
        
        b = fields.Boolean(required=False)
        
        p = fields.Boolean(required=False)
        
        id = fields.Str(required=False)
        
        buy_now = fields.Boolean(required=False)
         
        
    
    class removeCoupon(BaseSchema):
        
        
        x__ordering__source = fields.Nested(OrderingSource, required=False)
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        uid = fields.Str(required=False)
        
        buy_now = fields.Boolean(required=False)
         
        
    
    class getAddresses(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        cart_id = fields.Str(required=False)
        
        buy_now = fields.Boolean(required=False)
        
        mobile_no = fields.Str(required=False)
        
        checkout_mode = fields.Str(required=False)
        
        tags = fields.Str(required=False)
        
        is_default = fields.Boolean(required=False)
        
        user_id = fields.Str(required=False)
         
        
    
    class addAddress(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getAddressById(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
        
        cart_id = fields.Str(required=False)
        
        buy_now = fields.Boolean(required=False)
        
        mobile_no = fields.Str(required=False)
        
        checkout_mode = fields.Str(required=False)
        
        tags = fields.Str(required=False)
        
        is_default = fields.Boolean(required=False)
        
        user_id = fields.Str(required=False)
         
        
    
    class updateAddress(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class removeAddress(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
        
        user_id = fields.Str(required=False)
         
        
    
    class selectAddress(BaseSchema):
        
        
        x__ordering__source = fields.Nested(OrderingSource, required=False)
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        cart_id = fields.Str(required=False)
        
        buy_now = fields.Boolean(required=False)
        
        i = fields.Boolean(required=False)
        
        b = fields.Boolean(required=False)
         
        
    
    class getShipments(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        pick_at_store_uid = fields.Int(required=False)
        
        ordering_store_id = fields.Int(required=False)
        
        i = fields.Boolean(required=False)
        
        p = fields.Boolean(required=False)
        
        id = fields.Str(required=False)
        
        address_id = fields.Str(required=False)
        
        area_code = fields.Str(required=False)
        
        order_type = fields.Str(required=False)
         
        
    
    class updateShipments(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        i = fields.Boolean(required=False)
        
        p = fields.Boolean(required=False)
        
        id = fields.Str(required=False)
        
        address_id = fields.Str(required=False)
        
        area_code = fields.Str(required=False)
        
        order_type = fields.Str(required=False)
         
        
    
    class updateCartMeta(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
        
        buy_now = fields.Boolean(required=False)
         
        
    
    class platformCheckoutCart(BaseSchema):
        
        
        x__ordering__source = fields.Nested(OrderingSource, required=False)
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class getAvailableDeliveryModes(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        area_code = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class getStoreAddressByUid(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        store_uid = fields.Int(required=False)
         
        
    
    class selectPaymentMode(BaseSchema):
        
        
        x__ordering__source = fields.Nested(OrderingSource, required=False)
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
        
        buy_now = fields.Boolean(required=False)
        
        order_type = fields.Str(required=False)
         
        
    
    class validateCouponForPayment(BaseSchema):
        
        
        x__ordering__source = fields.Nested(OrderingSource, required=False)
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
        
        buy_now = fields.Boolean(required=False)
        
        address_id = fields.Str(required=False)
        
        payment_mode = fields.Str(required=False)
        
        payment_identifier = fields.Str(required=False)
        
        aggregator_name = fields.Str(required=False)
        
        merchant_code = fields.Str(required=False)
         
        
    
    class platformCheckoutCartV2(BaseSchema):
        
        
        x__ordering__source = fields.Nested(OrderingSource, required=False)
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class selectPaymentModeV2(BaseSchema):
        
        
        x__ordering__source = fields.Nested(OrderingSource, required=False)
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
        
        buy_now = fields.Boolean(required=False)
        
        order_type = fields.Str(required=False)
         
        
    
    class applyLoyaltyPoints(BaseSchema):
        
        
        x__ordering__source = fields.Nested(OrderingSource, required=False)
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
        
        i = fields.Boolean(required=False)
        
        b = fields.Boolean(required=False)
        
        buy_now = fields.Boolean(required=False)
         
        
    
    

