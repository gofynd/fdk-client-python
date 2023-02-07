"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .DisplayMetaDict import DisplayMetaDict





from .DisplayMetaDict import DisplayMetaDict



from .DisplayMetaDict import DisplayMetaDict





class DisplayMeta(BaseSchema):
    #  swagger.json

    
    title = fields.Str(required=False)
    
    remove = fields.Nested(DisplayMetaDict, required=False)
    
    subtitle = fields.Str(required=False)
    
    apply = fields.Nested(DisplayMetaDict, required=False)
    
    auto = fields.Nested(DisplayMetaDict, required=False)
    
    description = fields.Str(required=False)
    
