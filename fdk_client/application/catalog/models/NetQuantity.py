"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class NetQuantity(BaseSchema):
    #  swagger.json

    
    unit = fields.Raw(required=False)
    
    value = fields.Float(required=False)
    
