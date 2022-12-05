"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class StatusesBody(BaseSchema):
    # Order swagger.json

    
    shipments = fields.Dict(required=False)
    
    exclude_bags_next_state = fields.Str(required=False)
    
    status = fields.Str(required=False)
    

