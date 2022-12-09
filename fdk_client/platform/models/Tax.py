"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class Tax(BaseSchema):
    # OrderManage swagger.json

    
    amount = fields.Dict(required=False)
    
    breakup = fields.List(fields.Dict(required=False), required=False)
    
    tax_exempt = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    

