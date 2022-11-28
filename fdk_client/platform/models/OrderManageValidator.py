"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

class OrderManageValidator:
    
    class createOrder(BaseSchema):
        
        company_id = fields.Int(required=False)
         
    
    class invalidateShipmentCache(BaseSchema):
        
        company_id = fields.Int(required=False)
         
    
    class reassignLocation(BaseSchema):
        
        company_id = fields.Int(required=False)
         
    
    class updateShipmentLock(BaseSchema):
        
        company_id = fields.Int(required=False)
         
    
    class getAnnouncements(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        date = fields.Str(required=False)
         
    
    class updateAddress(BaseSchema):
        
        shipment_id = fields.Str(required=False)
        
        name = fields.Str(required=False)
        
        address = fields.Str(required=False)
        
        address_type = fields.Str(required=False)
        
        pincode = fields.Str(required=False)
        
        phone = fields.Str(required=False)
        
        email = fields.Str(required=False)
        
        landmark = fields.Str(required=False)
        
        address_category = fields.Str(required=False)
        
        city = fields.Str(required=False)
        
        state = fields.Str(required=False)
        
        country = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
         
    
    class click2Call(BaseSchema):
        
        caller = fields.Str(required=False)
        
        receiver = fields.Str(required=False)
        
        bag_id = fields.Str(required=False)
        
        calling_to = fields.Str(required=False)
        
        caller_id = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
         
    
    class statusUpdateInternalV4(BaseSchema):
        
        company_id = fields.Int(required=False)
         
    
    class processManifest(BaseSchema):
        
        company_id = fields.Int(required=False)
         
    
    class getRoleBasedActions(BaseSchema):
        
        company_id = fields.Int(required=False)
         
    
    class getShipmentHistory(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        shipment_id = fields.Int(required=False)
        
        bag_id = fields.Int(required=False)
         
    
    class sendSmsNinja(BaseSchema):
        
        company_id = fields.Int(required=False)
         
    
    class checkOrderStatus(BaseSchema):
        
        company_id = fields.Int(required=False)
         
    