"""User Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class SessionDeleteResponseSchema(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Str(required=False), required=False)
    
