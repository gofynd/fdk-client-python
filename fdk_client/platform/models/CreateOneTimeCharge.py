"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .OneTimeChargeItem import OneTimeChargeItem






class CreateOneTimeCharge(BaseSchema):
    # Billing swagger.json

    
    name = fields.Str(required=False)
    
    charge = fields.Nested(OneTimeChargeItem, required=False)
    
    is_test = fields.Boolean(required=False)
    
    return_url = fields.Str(required=False)
    

