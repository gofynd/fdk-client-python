"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema











from .RestrictedCategoryResponseInfoSerializer import RestrictedCategoryResponseInfoSerializer


class RestrictedCategoryResponseSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    code = fields.Str(required=False)
    
    fulfilment_type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    store_type = fields.Str(required=False)
    
    restricted_categories = fields.List(fields.Nested(RestrictedCategoryResponseInfoSerializer, required=False), required=False)
    

