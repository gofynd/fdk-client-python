"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class ApplicationBrandJson(BaseSchema):
    #  swagger.json

    
    _custom_json = fields.Dict(required=False)
    
