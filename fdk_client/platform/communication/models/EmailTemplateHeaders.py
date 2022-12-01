"""communication Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class EmailTemplateHeaders(BaseSchema):
    #  swagger.json

    
    key = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
