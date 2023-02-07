"""content Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class DataLoaderSourceSchema(BaseSchema):
    #  swagger.json

    
    type = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
