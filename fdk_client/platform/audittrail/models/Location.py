"""audittrail Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






class Location(BaseSchema):
    #  swagger.json

    
    extra_meta = fields.Dict(required=False)
    
