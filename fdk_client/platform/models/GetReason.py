"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class GetReason(BaseSchema):
    # Finance swagger.json

    
    reason_type = fields.Str(required=False)
    

