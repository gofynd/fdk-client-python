"""logistic Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .UpdateZoneData import UpdateZoneData



class ZoneUpdateRequest(BaseSchema):
    #  swagger.json

    
    identifier = fields.Str(required=False)
    
    data = fields.Nested(UpdateZoneData, required=False)
    
