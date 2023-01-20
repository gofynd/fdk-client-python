"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class OrderBagArticle(BaseSchema):
    #  swagger.json

    
    uid = fields.Str(required=False)
    
    identifiers = fields.Dict(required=False)
    
    return_config = fields.Dict(required=False)
    
