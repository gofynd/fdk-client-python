"""Order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class Store(BaseSchema):
    #  swagger.json

    
    id = fields.Int(required=False)
    