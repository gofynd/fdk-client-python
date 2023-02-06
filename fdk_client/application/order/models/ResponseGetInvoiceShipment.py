"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema












class ResponseGetInvoiceShipment(BaseSchema):
    #  swagger.json

    
    presigned_url = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    presigned_type = fields.Str(required=False)
    
