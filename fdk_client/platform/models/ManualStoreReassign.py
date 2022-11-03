"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class ManualStoreReassign(BaseSchema):
    # OrderManage swagger.json

    
    reason_text = fields.Str(required=False)
    
    store_id = fields.Int(required=False)
    
    reason_id = fields.List(fields.Int(required=False), required=False)
    
    shipment_id = fields.Str(required=False)
    

