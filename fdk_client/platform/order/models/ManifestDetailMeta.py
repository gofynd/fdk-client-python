"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ManifestFilter import ManifestFilter



from .ManifestDetailTotalShipmentPricesCount import ManifestDetailTotalShipmentPricesCount



class ManifestDetailMeta(BaseSchema):
    #  swagger.json

    
    filters = fields.Nested(ManifestFilter, required=False)
    
    total_shipment_prices_count = fields.Nested(ManifestDetailTotalShipmentPricesCount, required=False)
    
