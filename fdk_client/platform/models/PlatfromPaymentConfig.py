"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .PlatformPaymentOptions import PlatformPaymentOptions




class PlatfromPaymentConfig(BaseSchema):
    # Payment swagger.json

    
    message = fields.Str(required=False)
    
    data = fields.Nested(PlatformPaymentOptions, required=False)
    
    success = fields.Boolean(required=False)
    

