"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .AffiliateConfig import AffiliateConfig




class Affiliate(BaseSchema):
    # Order swagger.json

    
    id = fields.Str(required=False)
    
    config = fields.Nested(AffiliateConfig, required=False)
    
    token = fields.Str(required=False)
    

