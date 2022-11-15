"""Cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class DisplayMetaDict(BaseSchema):
    #  swagger.json

    
    subtitle = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
