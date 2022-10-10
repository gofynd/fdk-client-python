"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema











from .BoxDetails import BoxDetails


class GenerateBulkBoxLabel(BaseSchema):
    # DocumentEngine swagger.json

    
    stock_transfer_id = fields.Str(required=False)
    
    label_type = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    seller_name = fields.Str(required=False)
    
    template_id = fields.Float(required=False)
    
    box_details = fields.List(fields.Nested(BoxDetails, required=False), required=False)
    

