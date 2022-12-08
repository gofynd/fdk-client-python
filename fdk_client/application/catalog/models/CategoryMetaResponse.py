"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .ImageUrls import ImageUrls



from .Media import Media







class CategoryMetaResponse(BaseSchema):
    #  swagger.json

    
    banners = fields.Nested(ImageUrls, required=False)
    
    logo = fields.Nested(Media, required=False)
    
    name = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
