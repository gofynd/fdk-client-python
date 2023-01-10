"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class LatLong(BaseSchema):
    #  swagger.json

    
    type = fields.Str(required=False)
    
    coordinates = fields.List(fields.Float(required=False), required=False)
    
