"""Cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class DisplayMetaDict(BaseSchema):
    #  swagger.json

    
    title = fields.Str(required=False)
    
    subtitle = fields.Str(required=False)
    
