"""FileStorage Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class CDN(BaseSchema):
    #  swagger.json

    
    url = fields.Str(required=False)
    
