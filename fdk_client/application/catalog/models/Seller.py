"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class Seller(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    count = fields.Int(required=False)
    
    uid = fields.Int(required=False)
    
