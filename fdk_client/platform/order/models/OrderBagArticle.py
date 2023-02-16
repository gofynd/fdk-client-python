"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class OrderBagArticle(BaseSchema):
    #  swagger.json

    
    return_config = fields.Dict(required=False)
    
    identifiers = fields.Dict(required=False)
    
    uid = fields.Str(required=False)
    
