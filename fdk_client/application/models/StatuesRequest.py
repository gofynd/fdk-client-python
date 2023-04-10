"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ShipmentsRequest1 import ShipmentsRequest1






class StatuesRequest(BaseSchema):
    # Order swagger.json

    
    shipments = fields.List(fields.Nested(ShipmentsRequest1, required=False), required=False)
    
    exclude_bags_next_state = fields.Str(required=False)
    
    status = fields.Str(required=False)
    

