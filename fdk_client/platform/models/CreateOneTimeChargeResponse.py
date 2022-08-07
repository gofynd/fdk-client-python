"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .OneTimeChargeEntity import OneTimeChargeEntity




class CreateOneTimeChargeResponse(BaseSchema):
    # Billing swagger.json

    
    subscription = fields.Nested(OneTimeChargeEntity, required=False)
    
    confirm_url = fields.Str(required=False)
    

