"""content Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema


















class HandpickedTagSchema(BaseSchema):
    #  swagger.json

    
    position = fields.Str(required=False)
    
    attributes = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    
    url = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    sub_type = fields.Str(required=False)
    
    content = fields.Str(required=False)
    
