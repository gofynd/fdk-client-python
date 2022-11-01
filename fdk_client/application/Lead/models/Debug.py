"""Lead Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class Debug(BaseSchema):
    #  swagger.json

    
    source = fields.Str(required=False)
    
    platform = fields.Str(required=False)
    
