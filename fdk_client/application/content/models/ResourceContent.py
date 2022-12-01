"""content Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class ResourceContent(BaseSchema):
    #  swagger.json

    
    type = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
