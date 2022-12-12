"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class Products(BaseSchema):
    # OrderManage swagger.json

    
    identifier = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    line_number = fields.Int(required=False)
    

