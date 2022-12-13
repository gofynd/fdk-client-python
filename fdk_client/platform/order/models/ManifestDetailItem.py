"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














class ManifestDetailItem(BaseSchema):
    #  swagger.json

    
    order_id = fields.Str(required=False)
    
    awb = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    
    item_qty = fields.Int(required=False)
    
    invoice_id = fields.Str(required=False)
    
