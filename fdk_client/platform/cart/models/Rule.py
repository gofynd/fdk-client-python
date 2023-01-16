"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














class Rule(BaseSchema):
    #  swagger.json

    
    value = fields.Float(required=False)
    
    discount_qty = fields.Float(required=False)
    
    key = fields.Float(required=False)
    
    max = fields.Float(required=False)
    
    min = fields.Float(required=False)
    
