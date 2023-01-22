"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class Weight(BaseSchema):
    #  swagger.json

    
    unit = fields.Str(required=False)
    
    is_default = fields.Boolean(required=False)
    
    shipping = fields.Float(required=False)
    