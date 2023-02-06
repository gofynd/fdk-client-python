"""lead Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class CreatedOn(BaseSchema):
    #  swagger.json

    
    user_agent = fields.Str(required=False)
    
