"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema












class ResponseGetInvoiceShipment1(BaseSchema):
    #  swagger.json

    
    success = fields.Boolean(required=False)
    
    shipment_id = fields.Str(required=False)
    
    presigned_url = fields.Str(required=False)
    
    presigned_type = fields.Str(required=False)
    
