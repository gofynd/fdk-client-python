"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema












class StoreDetail(BaseSchema):
    #  swagger.json

    
    city = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    code = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
