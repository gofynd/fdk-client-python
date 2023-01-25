"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














class PriceArticle(BaseSchema):
    #  swagger.json

    
    marked = fields.Float(required=False)
    
    transfer = fields.Float(required=False)
    
    effective = fields.Float(required=False)
    
    currency = fields.Str(required=False)
    
    tp_notes = fields.Dict(required=False)
    
