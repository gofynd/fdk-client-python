"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class OriginalFilter(BaseSchema):
    # OrderManage swagger.json

    
    affiliate_id = fields.Str(required=False)
    
    affiliate_shipment_id = fields.Str(required=False)
    

