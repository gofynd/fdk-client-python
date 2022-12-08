"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class SEO(BaseSchema):
    #  swagger.json

    
    description = fields.Raw(required=False)
    
    title = fields.Raw(required=False)
    
