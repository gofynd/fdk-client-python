"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class ReqBodyPresignedPOST(BaseSchema):
    # Order swagger.json

    
    event = fields.Str(required=False)
    
    media_type = fields.List(fields.Raw(required=False), required=False)
    

