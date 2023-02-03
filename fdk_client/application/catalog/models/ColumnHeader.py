"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class ColumnHeader(BaseSchema):
    #  swagger.json

    
    value = fields.Str(required=False)
    
    convertable = fields.Boolean(required=False)
    
