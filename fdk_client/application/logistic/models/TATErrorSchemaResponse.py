"""logistic Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class TATErrorSchemaResponse(BaseSchema):
    #  swagger.json

    
    value = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
