"""inventory Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class DBConnectionProfile(BaseSchema):
    #  swagger.json

    
    inventory = fields.Str(required=False)
    
