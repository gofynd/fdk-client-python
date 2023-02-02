"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema
















class ProcessingDates(BaseSchema):
    #  swagger.json

    
    customer_pickup_slot = fields.Dict(required=False)
    
    dispatch_by_date = fields.Str(required=False)
    
    dp_pickup_slot = fields.Dict(required=False)
    
    pack_by_date = fields.Str(required=False)
    
    confirm_by_date = fields.Str(required=False)
    
    dispatch_after_date = fields.Str(required=False)
    
