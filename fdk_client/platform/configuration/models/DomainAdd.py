"""configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class DomainAdd(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
