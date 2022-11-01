"""Configuration Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class DefaultCurrency(BaseSchema):
    #  swagger.json

    
    ref = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
