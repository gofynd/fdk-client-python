"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

class OrdersValidator:
    
    class getOrderShipmentDetails(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        shipment_id = fields.Str(required=False)
         
    
    class getShipmentDetails(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        order_id = fields.Str(required=False)
         
    
    class getShipmentToManifest(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        group_entity = fields.Str(required=False)
        
        sales_channel = fields.Str(required=False)
        
        dp_ids = fields.Str(required=False)
         
    