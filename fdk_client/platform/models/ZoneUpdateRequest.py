"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .UpdateZoneData import UpdateZoneData


class ZoneUpdateRequest(BaseSchema):
    # Serviceability swagger.json

    
    identifier = fields.Str(required=False)
    
    data = fields.Nested(UpdateZoneData, required=False)
    

