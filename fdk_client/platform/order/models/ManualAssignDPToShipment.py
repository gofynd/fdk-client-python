"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












class ManualAssignDPToShipment(BaseSchema):
    #  swagger.json

    
    order_type = fields.Str(required=False)
    
    dp_id = fields.Int(required=False)
    
    shipment_ids = fields.List(fields.Str(required=False), required=False)
    
    qc_required = fields.Str(required=False)
    
