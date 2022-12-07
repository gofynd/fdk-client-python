"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ManifestFilter import ManifestFilter

from .ManifestDetailTotalShipmentPricesCount import ManifestDetailTotalShipmentPricesCount


class ManifestDetailMeta(BaseSchema):
    # Orders swagger.json

    
    filters = fields.Nested(ManifestFilter, required=False)
    
    total_shipment_prices_count = fields.Nested(ManifestDetailTotalShipmentPricesCount, required=False)
    

