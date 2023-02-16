"""logistic Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class OpeningClosing(BaseSchema):
    #  swagger.json

    
    minute = fields.Int(required=False)
    
    hour = fields.Int(required=False)
    
