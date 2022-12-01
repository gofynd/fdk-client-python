"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class Validity(BaseSchema):
    #  swagger.json

    
    priority = fields.Int(required=False)
    
