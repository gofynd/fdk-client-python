"""Analytics Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema
















class AbandonCartDetail(BaseSchema):
    #  swagger.json

    
    _id = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
    cart_value = fields.Str(required=False)
    
    articles = fields.List(fields.Dict(required=False), required=False)
    
    breakup = fields.Dict(required=False)
    
    address = fields.Dict(required=False)
    
