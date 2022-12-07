"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class ProductsReasons(BaseSchema):
    # OrderManage swagger.json

    
    data = fields.Dict(required=False)
    
    filters = fields.List(fields.Dict(required=False), required=False)
    

