"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .UserDataSet import UserDataSet



from .ShipmentDataSet import ShipmentDataSet




class OrderDataSet(BaseSchema):
    # Orders swagger.json

    
    user_info = fields.Nested(UserDataSet, required=False)
    
    order_created_time = fields.Str(required=False)
    
    shipments = fields.List(fields.Nested(ShipmentDataSet, required=False), required=False)
    
    order_id = fields.Str(required=False)
    
