"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .InvalidateShipmentCacheNestedResponse import InvalidateShipmentCacheNestedResponse



class InvalidateShipmentCacheResponse(BaseSchema):
    #  swagger.json

    
    response = fields.List(fields.Nested(InvalidateShipmentCacheNestedResponse, required=False), required=False)
    
