"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .Media import Media



from .Media import Media



class CategoryBanner(BaseSchema):
    #  swagger.json

    
    portrait = fields.Nested(Media, required=False)
    
    landscape = fields.Nested(Media, required=False)
    
