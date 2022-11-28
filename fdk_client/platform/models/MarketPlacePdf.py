"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class MarketPlacePdf(BaseSchema):
    # OrderManage swagger.json

    
    invoice = fields.Str(required=False)
    
    label = fields.Str(required=False)
    

