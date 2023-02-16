"""content Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema
















from .TagSourceSchema import TagSourceSchema



class PathMappingSchema(BaseSchema):
    #  swagger.json

    
    application = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    redirect_from = fields.Str(required=False)
    
    redirect_to = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    __source = fields.Nested(TagSourceSchema, required=False)
    
