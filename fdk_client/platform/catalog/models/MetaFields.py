"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class MetaFields(BaseSchema):
    #  swagger.json

    
    key = fields.Raw(required=False)
    
    value = fields.Raw(required=False)
    
