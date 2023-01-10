"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema


















class ArticleDetails(BaseSchema):
    #  swagger.json

    
    dimension = fields.Dict(required=False)
    
    weight = fields.Dict(required=False)
    
    category = fields.Dict(required=False)
    
    quantity = fields.Int(required=False)
    
    attributes = fields.Dict(required=False)
    
    _id = fields.Str(required=False)
    
    brand_id = fields.Int(required=False)
    
