"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .Shipment1 import Shipment1


class ManifestShipmentResponse(BaseSchema):
    # Orders swagger.json

    
    success = fields.Boolean(required=False)
    
    shipments = fields.List(fields.Nested(Shipment1, required=False), required=False)
    

