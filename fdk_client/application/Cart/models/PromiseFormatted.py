"""Cart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class PromiseFormatted(BaseSchema):
    #  swagger.json

    
    max = fields.Str(required=False)
    
    min = fields.Str(required=False)
    
