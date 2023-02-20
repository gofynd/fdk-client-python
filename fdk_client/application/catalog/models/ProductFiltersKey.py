"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema












class ProductFiltersKey(BaseSchema):
    #  swagger.json

    
    logo = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    display = fields.Str(required=False)
    
    kind = fields.Str(required=False)
    
