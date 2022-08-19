"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .AffiliateConfig import AffiliateConfig






class Affiliate(BaseSchema):
    # Order swagger.json

    
    config = fields.Nested(AffiliateConfig, required=False)
    
    id = fields.Str(required=False)
    
    token = fields.Str(required=False)
    

