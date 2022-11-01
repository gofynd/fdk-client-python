"""Order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .DataShipmentAddress import DataShipmentAddress





class GetShipmentAddressResponse(BaseSchema):
    #  swagger.json

    
    message = fields.Str(required=False)
    
    data = fields.Nested(DataShipmentAddress, required=False)
    
    success = fields.Boolean(required=False)
    
