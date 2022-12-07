"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema












class Size(BaseSchema):
    #  swagger.json

    
    value = fields.Raw(required=False)
    
    display = fields.Raw(required=False)
    
    is_available = fields.Boolean(required=False)
    
    quantity = fields.Int(required=False)
    