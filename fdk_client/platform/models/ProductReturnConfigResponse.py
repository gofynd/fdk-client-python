"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class ProductReturnConfigResponse(BaseSchema):
    # Serviceability swagger.json

    
    on_same_store = fields.Boolean(required=False)
    

