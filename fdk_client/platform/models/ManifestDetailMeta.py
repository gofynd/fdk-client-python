"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ManifestDetailTotalShipmentPricesCount import ManifestDetailTotalShipmentPricesCount

from .ManifestFilter import ManifestFilter


class ManifestDetailMeta(BaseSchema):
    # Order swagger.json

    
    total_shipment_prices_count = fields.Nested(ManifestDetailTotalShipmentPricesCount, required=False)
    
    filters = fields.Nested(ManifestFilter, required=False)
    

