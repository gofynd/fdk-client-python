"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












class ManualAssignDPToShipment(BaseSchema):
    #  swagger.json

    
    dp_id = fields.Int(required=False)
    
    qc_required = fields.Str(required=False)
    
    shipment_ids = fields.List(fields.Str(required=False), required=False)
    
    order_type = fields.Str(required=False)
    
