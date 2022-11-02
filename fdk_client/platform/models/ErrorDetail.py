"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class ErrorDetail(BaseSchema):
    # OrderManage swagger.json

    
    message = fields.Str(required=False)
    

