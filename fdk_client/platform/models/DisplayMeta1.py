"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class DisplayMeta1(BaseSchema):
    # Cart swagger.json

    
    name = fields.Str(required=False)
    
    offer_text = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    offer_label = fields.Str(required=False)
    

