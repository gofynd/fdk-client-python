"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema














class AttributeObject(BaseSchema):

    
    description = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    value = fields.Float(required=False)
    

