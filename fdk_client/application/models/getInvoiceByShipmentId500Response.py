"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class getInvoiceByShipmentId500Response(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    presigned_type = fields.Str(required=False)
    

