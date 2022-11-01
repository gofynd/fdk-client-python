"""Inventory Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class DBParamConfig(BaseSchema):
    #  swagger.json

    
    params = fields.Dict(required=False)
    
