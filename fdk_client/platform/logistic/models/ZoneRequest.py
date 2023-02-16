"""logistic Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .CreateZoneData import CreateZoneData



class ZoneRequest(BaseSchema):
    #  swagger.json

    
    identifier = fields.Str(required=False)
    
    data = fields.Nested(CreateZoneData, required=False)
    
