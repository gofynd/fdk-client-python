"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class ManifestDetailTotalShipmentPricesCount(BaseSchema):
    # Orders swagger.json

    
    total_price = fields.Float(required=False)
    
    shipment_count = fields.Int(required=False)
    

