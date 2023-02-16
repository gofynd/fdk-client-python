"""configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class Links(BaseSchema):
    #  swagger.json

    
    title = fields.Str(required=False)
    
    link = fields.Str(required=False)
    
