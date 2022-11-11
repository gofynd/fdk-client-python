"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class SEO(BaseSchema):
    #  swagger.json

    
    title = fields.Raw(required=False)
    
    description = fields.Raw(required=False)
    
