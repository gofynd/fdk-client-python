"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .ShipmentDetails import ShipmentDetails


class GenerateBulkShipmentLabel(BaseSchema):
    # OrderInvoiceEngine swagger.json

    
    label_type = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    template_id = fields.Float(required=False)
    
    shipments = fields.List(fields.Nested(ShipmentDetails, required=False), required=False)
    

