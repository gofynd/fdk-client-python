"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class OrderPriority(BaseSchema):
    # OrderManage swagger.json

    
    fulfilment_priority = fields.Int(required=False)
    
    affiliate_priority_code = fields.Str(required=False)
    
    fulfilment_priority_text = fields.Str(required=False)
    
