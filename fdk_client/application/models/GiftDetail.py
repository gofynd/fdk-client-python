"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class GiftDetail(BaseSchema):
    # Cart swagger.json

    
    gift_message = fields.Str(required=False)
    
    is_gift_applied = fields.Boolean(required=False)
    

