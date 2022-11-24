"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class Click2CallResponse(BaseSchema):
    # OrderManage swagger.json

    
    status = fields.Boolean(required=False)
    
    call_id = fields.Str(required=False)
    

