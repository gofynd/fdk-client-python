"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class ResponseGetInvoiceShipment(BaseSchema):
    # Order swagger.json

    
    presigned_url = fields.Str(required=False)
    
    presigned_type = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    shipment_id = fields.Str(required=False)
    

