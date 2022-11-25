"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class MarketPlacePdf(BaseSchema):
    # Order swagger.json

    
    label = fields.Str(required=False)
    
    invoice = fields.Str(required=False)
    

