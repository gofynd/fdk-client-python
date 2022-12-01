"""rewards Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class PointsResponse(BaseSchema):
    #  swagger.json

    
    points = fields.Float(required=False)
    
