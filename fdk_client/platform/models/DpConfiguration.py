"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class DpConfiguration(BaseSchema):
    # OrderManage swagger.json

    
    shipping_by = fields.Str(required=False)
    

