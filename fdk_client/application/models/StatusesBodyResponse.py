"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class StatusesBodyResponse(BaseSchema):
    # Order swagger.json

    
    shipments = fields.Dict(required=False)
    

