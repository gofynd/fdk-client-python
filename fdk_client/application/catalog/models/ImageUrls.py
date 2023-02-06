"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .Media import Media



from .Media import Media



class ImageUrls(BaseSchema):
    #  swagger.json

    
    landscape = fields.Nested(Media, required=False)
    
    portrait = fields.Nested(Media, required=False)
    
