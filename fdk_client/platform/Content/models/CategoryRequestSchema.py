"""Content Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class CategoryRequestSchema(BaseSchema):
    #  swagger.json

    
    slug = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
