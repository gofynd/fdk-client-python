"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class ManifestDetailTotalShipmentPricesCount(BaseSchema):
    #  swagger.json

    
    shipment_count = fields.Int(required=False)
    
    total_price = fields.Float(required=False)
    
