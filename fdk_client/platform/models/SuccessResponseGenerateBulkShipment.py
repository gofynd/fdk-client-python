"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class SuccessResponseGenerateBulkShipment(BaseSchema):
    # OrderInvoiceEngine swagger.json

    
    success = fields.Boolean(required=False)
    
    job_id = fields.Float(required=False)
    

