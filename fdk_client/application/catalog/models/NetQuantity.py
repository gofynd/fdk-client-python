"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class NetQuantity(BaseSchema):
    #  swagger.json

    
    value = fields.Float(required=False)
    
    unit = fields.Str(required=False)
    
