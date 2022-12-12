"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema














class ProcessingDates(BaseSchema):
    # Order swagger.json

    
    dp_pickup_slot = fields.Dict(required=False)
    
    confirm_by_date = fields.Str(required=False)
    
    pack_by_date = fields.Str(required=False)
    
    dispatch_after_date = fields.Str(required=False)
    
    customer_pickup_slot = fields.Dict(required=False)
    
    dispatch_by_date = fields.Str(required=False)
    

