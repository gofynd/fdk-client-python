"""theme Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class Custom(BaseSchema):
    #  swagger.json

    
    props = fields.Dict(required=False)
    
