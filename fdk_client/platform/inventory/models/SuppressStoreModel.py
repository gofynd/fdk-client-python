"""inventory Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class SuppressStoreModel(BaseSchema):
    #  swagger.json

    
    stores = fields.List(fields.Int(required=False), required=False)
    
