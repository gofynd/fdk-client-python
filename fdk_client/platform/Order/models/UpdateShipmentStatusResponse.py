"""Order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class UpdateShipmentStatusResponse(BaseSchema):
    #  swagger.json

    
    shipments = fields.Dict(required=False)
    
    error_shipments = fields.List(fields.Raw(required=False), required=False)
    
