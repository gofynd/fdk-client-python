"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class PlatformOrderUpdate(BaseSchema):
    #  swagger.json

    
    order_id = fields.Str(required=False)
    
