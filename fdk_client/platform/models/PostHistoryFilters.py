"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class PostHistoryFilters(BaseSchema):
    # Order swagger.json

    
    line_number = fields.Str(required=False)
    
    identifier = fields.Str(required=False)
    
    shipment_id = fields.Str(required=False)
    

