"""logistic Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class WarningsResponse(BaseSchema):
    #  swagger.json

    
    store_address = fields.Str(required=False)
    
