"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ShipmentsRequest import ShipmentsRequest






class StatuesRequest(BaseSchema):
    # Order swagger.json

    
    shipments = fields.Nested(ShipmentsRequest, required=False)
    
    status = fields.Str(required=False)
    
    exclude_bags_next_state = fields.Str(required=False)
    

