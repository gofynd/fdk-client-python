"""PosCart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class CartMetaResponse(BaseSchema):
    #  swagger.json

    
    message = fields.Str(required=False)
    
