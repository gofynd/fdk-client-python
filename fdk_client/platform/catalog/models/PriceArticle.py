"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














class PriceArticle(BaseSchema):
    #  swagger.json

    
    transfer = fields.Float(required=False)
    
    tp_notes = fields.Dict(required=False)
    
    effective = fields.Float(required=False)
    
    marked = fields.Float(required=False)
    
    currency = fields.Str(required=False)
    
