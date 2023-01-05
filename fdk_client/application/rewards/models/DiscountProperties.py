"""rewards Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema














class DiscountProperties(BaseSchema):
    #  swagger.json

    
    absolute = fields.Float(required=False)
    
    currency = fields.Str(required=False)
    
    display_absolute = fields.Str(required=False)
    
    display_percent = fields.Str(required=False)
    
    percent = fields.Float(required=False)
    
