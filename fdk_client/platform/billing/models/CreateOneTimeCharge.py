"""billing Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .OneTimeChargeItem import OneTimeChargeItem







class CreateOneTimeCharge(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    charge = fields.Nested(OneTimeChargeItem, required=False)
    
    is_test = fields.Boolean(required=False)
    
    return_url = fields.Str(required=False)
    
