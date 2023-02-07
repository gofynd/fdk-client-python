"""content Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class Orientation(BaseSchema):
    #  swagger.json

    
    portrait = fields.List(fields.Str(required=False), required=False)
    
    landscape = fields.List(fields.Str(required=False), required=False)
    
