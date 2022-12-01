"""common Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












class Author(BaseSchema):
    #  swagger.json

    
    created_by = fields.Str(required=False)
    
    updated_by = fields.Str(required=False)
    
    creator_name = fields.Str(required=False)
    
    updator_name = fields.Str(required=False)
    
