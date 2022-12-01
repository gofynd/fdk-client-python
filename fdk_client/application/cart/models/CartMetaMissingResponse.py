"""cart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class CartMetaMissingResponse(BaseSchema):
    #  swagger.json

    
    errors = fields.List(fields.Str(required=False), required=False)
    
