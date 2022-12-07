"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ShipmentsResponse import ShipmentsResponse



class StatuesResponse(BaseSchema):
    #  swagger.json

    
    shipments = fields.Nested(ShipmentsResponse, required=False)
    
