"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .ManifestDetailTotalShipmentPricesCount import ManifestDetailTotalShipmentPricesCount



from .ManifestFilter import ManifestFilter



class ManifestDetailMeta(BaseSchema):
    #  swagger.json

    
    total_shipment_prices_count = fields.Nested(ManifestDetailTotalShipmentPricesCount, required=False)
    
    filters = fields.Nested(ManifestFilter, required=False)
    
