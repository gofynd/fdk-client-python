

"""Cart Application Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..ApplicationModel import BaseSchema



    
    
                
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
    
    
    class getCart(BaseSchema):
        
        
        x__ordering__source = fields.Nested(OrderingSource, required=False)
        
        id = fields.Str(required=False)
        
        i = fields.Boolean(required=False)
        
        b = fields.Boolean(required=False)
        
        c = fields.Boolean(required=False)
        
        assign_card_id = fields.Int(required=False)
        
        area_code = fields.Str(required=False)
        
        buy_now = fields.Boolean(required=False)
        
        order_type = fields.Str(required=False)
         
        
    
    class getCartLastModified(BaseSchema):
        
        
        id = fields.Str(required=False)
         
        
    
    class addItems(BaseSchema):
        
        
        x__ordering__source = fields.Nested(OrderingSource, required=False)
        
        i = fields.Boolean(required=False)
        
        b = fields.Boolean(required=False)
        
        area_code = fields.Str(required=False)
        
        buy_now = fields.Boolean(required=False)
        
        id = fields.Str(required=False)
        
        order_type = fields.Str(required=False)
         
        
    
    class updateCart(BaseSchema):
        
        
        x__ordering__source = fields.Nested(OrderingSource, required=False)
        
        id = fields.Str(required=False)
        
        i = fields.Boolean(required=False)
        
        b = fields.Boolean(required=False)
        
        area_code = fields.Str(required=False)
        
        buy_now = fields.Boolean(required=False)
        
        cart_type = fields.Str(required=False)
        
        order_type = fields.Str(required=False)
         
        
    
    class updateCartBreakup(BaseSchema):
        
        
        x__ordering__source = fields.Nested(OrderingSource, required=False)
        
        id = fields.Str(required=False)
        
        i = fields.Boolean(required=False)
        
        b = fields.Boolean(required=False)
        
        buy_now = fields.Boolean(required=False)
        
        cart_type = fields.Str(required=False)
         
        
    
    class deleteCart(BaseSchema):
        
        
        id = fields.Str(required=False)
         
        
    
    class getItemCount(BaseSchema):
        
        
        id = fields.Str(required=False)
        
        buy_now = fields.Boolean(required=False)
         
        
    
    class getCoupons(BaseSchema):
        
        
        id = fields.Str(required=False)
        
        buy_now = fields.Boolean(required=False)
        
        product_slug = fields.Str(required=False)
        
        store_id = fields.Str(required=False)
         
        
    
    class applyCoupon(BaseSchema):
        
        
        x__ordering__source = fields.Nested(OrderingSource, required=False)
        
        i = fields.Boolean(required=False)
        
        b = fields.Boolean(required=False)
        
        p = fields.Boolean(required=False)
        
        id = fields.Str(required=False)
        
        buy_now = fields.Boolean(required=False)
        
        cart_type = fields.Str(required=False)
         
        
    
    class removeCoupon(BaseSchema):
        
        
        x__ordering__source = fields.Nested(OrderingSource, required=False)
        
        id = fields.Str(required=False)
        
        buy_now = fields.Boolean(required=False)
         
        
    
    class getBulkDiscountOffers(BaseSchema):
        
        
        item_id = fields.Int(required=False)
        
        article_id = fields.Str(required=False)
        
        uid = fields.Int(required=False)
        
        slug = fields.Str(required=False)
         
        
    
    class applyRewardPoints(BaseSchema):
        
        
        x__ordering__source = fields.Nested(OrderingSource, required=False)
        
        id = fields.Str(required=False)
        
        i = fields.Boolean(required=False)
        
        b = fields.Boolean(required=False)
        
        buy_now = fields.Boolean(required=False)
         
        
    
    class getAddresses(BaseSchema):
        
        
        cart_id = fields.Str(required=False)
        
        buy_now = fields.Boolean(required=False)
        
        mobile_no = fields.Str(required=False)
        
        checkout_mode = fields.Str(required=False)
        
        tags = fields.Str(required=False)
        
        is_default = fields.Boolean(required=False)
         
        
    
    class addAddress(BaseSchema):
        
        pass 
        
    
    class getAddressById(BaseSchema):
        
        
        id = fields.Str(required=False)
        
        cart_id = fields.Str(required=False)
        
        buy_now = fields.Boolean(required=False)
        
        mobile_no = fields.Str(required=False)
        
        checkout_mode = fields.Str(required=False)
        
        tags = fields.Str(required=False)
        
        is_default = fields.Boolean(required=False)
         
        
    
    class updateAddress(BaseSchema):
        
        
        id = fields.Str(required=False)
         
        
    
    class removeAddress(BaseSchema):
        
        
        id = fields.Str(required=False)
         
        
    
    class selectAddress(BaseSchema):
        
        
        x__ordering__source = fields.Nested(OrderingSource, required=False)
        
        cart_id = fields.Str(required=False)
        
        buy_now = fields.Boolean(required=False)
        
        i = fields.Boolean(required=False)
        
        b = fields.Boolean(required=False)
         
        
    
    class selectPaymentMode(BaseSchema):
        
        
        x__ordering__source = fields.Nested(OrderingSource, required=False)
        
        id = fields.Str(required=False)
        
        buy_now = fields.Boolean(required=False)
         
        
    
    class validateCouponForPayment(BaseSchema):
        
        
        x__ordering__source = fields.Nested(OrderingSource, required=False)
        
        id = fields.Str(required=False)
        
        buy_now = fields.Boolean(required=False)
        
        address_id = fields.Str(required=False)
        
        payment_mode = fields.Str(required=False)
        
        payment_identifier = fields.Str(required=False)
        
        aggregator_name = fields.Str(required=False)
        
        merchant_code = fields.Str(required=False)
        
        iin = fields.Str(required=False)
        
        network = fields.Str(required=False)
        
        type = fields.Str(required=False)
        
        card_id = fields.Str(required=False)
        
        cart_type = fields.Str(required=False)
         
        
    
    class getShipments(BaseSchema):
        
        
        p = fields.Boolean(required=False)
        
        id = fields.Str(required=False)
        
        buy_now = fields.Boolean(required=False)
        
        address_id = fields.Str(required=False)
        
        area_code = fields.Str(required=False)
        
        order_type = fields.Str(required=False)
         
        
    
    class checkoutCart(BaseSchema):
        
        
        x__ordering__source = fields.Nested(OrderingSource, required=False)
        
        buy_now = fields.Boolean(required=False)
        
        cart_type = fields.Str(required=False)
         
        
    
    class updateCartMeta(BaseSchema):
        
        
        id = fields.Str(required=False)
        
        buy_now = fields.Boolean(required=False)
         
        
    
    class getCartShareLink(BaseSchema):
        
        pass 
        
    
    class getCartSharedItems(BaseSchema):
        
        
        token = fields.Str(required=False)
         
        
    
    class updateCartWithSharedItems(BaseSchema):
        
        
        token = fields.Str(required=False)
        
        action = fields.Str(required=False)
         
        
    
    class getPromotionOffers(BaseSchema):
        
        
        slug = fields.Str(required=False)
        
        page_size = fields.Int(required=False)
        
        promotion_group = fields.Str(required=False)
        
        store_id = fields.Int(required=False)
        
        cart_type = fields.Str(required=False)
        
        promotion_type = fields.Str(required=False)
        
        cart_id = fields.Str(required=False)
        
        auto_apply = fields.Boolean(required=False)
         
        
    
    class getLadderOffers(BaseSchema):
        
        
        slug = fields.Str(required=False)
        
        store_id = fields.Str(required=False)
        
        promotion_id = fields.Str(required=False)
        
        page_size = fields.Int(required=False)
         
        
    
    class getPromotionPaymentOffers(BaseSchema):
        
        
        id = fields.Str(required=False)
        
        uid = fields.Int(required=False)
         
        
    
    class checkoutCartV2(BaseSchema):
        
        
        x__ordering__source = fields.Nested(OrderingSource, required=False)
        
        buy_now = fields.Boolean(required=False)
        
        cart_type = fields.Str(required=False)
         
        
    
    


