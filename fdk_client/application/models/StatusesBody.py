"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class StatusesBody(BaseSchema):
    # Order swagger.json

    
    exclude_bags_next_state = fields.Str(required=False)
    
    shipments = fields.List(fields.Dict(required=False), required=False)
    
    status = fields.Str(required=False)
    

