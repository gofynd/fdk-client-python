"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

class OrderManageValidator:
    
    class statusInternalUpdate(BaseSchema):
        
        company_id = fields.Int(required=False)
         
    
    class getShipmentHistory(BaseSchema):
        
        company_id = fields.Int(required=False)
        
        bag_id = fields.Int(required=False)
         
    