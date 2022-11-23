"""Order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class EffectiveValues(BaseSchema):
    #  swagger.json

    
    min = fields.Float(required=False)
    
    max = fields.Float(required=False)
    
