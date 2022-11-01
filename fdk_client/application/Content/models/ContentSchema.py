"""Content Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class ContentSchema(BaseSchema):
    #  swagger.json

    
    type = fields.Str(required=False)
    
    value = fields.Dict(required=False)
    
