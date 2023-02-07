"""theme Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .ConfigPage import ConfigPage





class ListSchemaItem(BaseSchema):
    #  swagger.json

    
    global_config = fields.Dict(required=False)
    
    page = fields.List(fields.Nested(ConfigPage, required=False), required=False)
    
    name = fields.Str(required=False)
    
