"""user Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class Accountkit(BaseSchema):
    #  swagger.json

    
    app_id = fields.Str(required=False)
    
