"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class FollowIdsData(BaseSchema):
    #  swagger.json

    
    brands = fields.List(fields.Int(required=False), required=False)
    
    products = fields.List(fields.Int(required=False), required=False)
    
    collections = fields.List(fields.Int(required=False), required=False)
    
