"""lead Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class CategoryData(BaseSchema):
    #  swagger.json

    
    _id = fields.Str(required=False)
    
    timestamps = fields.Dict(required=False)
    
