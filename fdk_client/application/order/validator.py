

"""Order Application Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..ApplicationModel import BaseSchema



    
    
        
    
    
        
        
        
        
        
        
    
    
        
        
        
        
        
        
        
        
    
    
        
        
    
    
        
    
    
        
        
    
    
        
    
    
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
    
    
        

class OrderValidator:
    
    
    class getShipmentRefundSummary(BaseSchema):
        
        
        shipment_id = fields.Str(required=False)
         
        
    
    class getRefundOptions(BaseSchema):
        
        
        shipment_id = fields.Str(required=False)
        
        bag_ids = fields.Str(required=False)
        
        state = fields.Str(required=False)
        
        optin_app_id = fields.Str(required=False)
        
        optin_company_id = fields.Int(required=False)
        
        status = fields.Str(required=False)
         
        
    
    class getOrders(BaseSchema):
        
        
        status = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        from_date = fields.Str(required=False)
        
        to_date = fields.Str(required=False)
        
        start_date = fields.Str(required=False)
        
        end_date = fields.Str(required=False)
        
        custom_meta = fields.Str(required=False)
         
        
    
    class getOrderById(BaseSchema):
        
        
        order_id = fields.Str(required=False)
        
        allow_inactive = fields.Boolean(required=False)
         
        
    
    class getPosOrderById(BaseSchema):
        
        
        order_id = fields.Str(required=False)
         
        
    
    class getShipmentById(BaseSchema):
        
        
        shipment_id = fields.Str(required=False)
        
        allow_inactive = fields.Boolean(required=False)
         
        
    
    class getInvoiceByShipmentId(BaseSchema):
        
        
        shipment_id = fields.Str(required=False)
         
        
    
    class trackShipment(BaseSchema):
        
        
        shipment_id = fields.Str(required=False)
         
        
    
    class getCustomerDetailsByShipmentId(BaseSchema):
        
        
        order_id = fields.Str(required=False)
        
        shipment_id = fields.Str(required=False)
         
        
    
    class sendOtpToShipmentCustomer(BaseSchema):
        
        
        order_id = fields.Str(required=False)
        
        shipment_id = fields.Str(required=False)
         
        
    
    class verifyOtpShipmentCustomer(BaseSchema):
        
        
        order_id = fields.Str(required=False)
        
        shipment_id = fields.Str(required=False)
         
        
    
    class getShipmentBagReasons(BaseSchema):
        
        
        shipment_id = fields.Str(required=False)
        
        bag_id = fields.Str(required=False)
         
        
    
    class getShipmentReasons(BaseSchema):
        
        
        shipment_id = fields.Str(required=False)
         
        
    
    class updateShipmentStatus(BaseSchema):
        
        
        shipment_id = fields.Str(required=False)
         
        
    
    


