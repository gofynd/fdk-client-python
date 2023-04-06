"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class DeleteCartRequest(BaseSchema):
    # Cart swagger.json

    
    cart_id_list = fields.List(fields.Str(required=False), required=False)
    

