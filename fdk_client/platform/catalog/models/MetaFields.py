"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class MetaFields(BaseSchema):
    #  swagger.json

    
    value = fields.Raw(required=False)
    
    key = fields.Raw(required=False)
    
