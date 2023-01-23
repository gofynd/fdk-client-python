"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class ProductSortOn(BaseSchema):
    #  swagger.json

    
    is_selected = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
