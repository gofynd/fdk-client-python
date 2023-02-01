"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema












class StoreDetail(BaseSchema):
    #  swagger.json

    
    code = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
