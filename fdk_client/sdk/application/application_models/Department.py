"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema









from .Media import Media


class Department(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    priority_order = fields.Int(required=False)
    
    uid = fields.Int(required=False)
    
    slug = fields.Str(required=False)
    
    logo = fields.Nested(Media, required=False)
    

