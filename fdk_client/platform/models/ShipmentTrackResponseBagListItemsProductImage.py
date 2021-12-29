"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class ShipmentTrackResponseBagListItemsProductImage(BaseSchema):
    # Order swagger.json

    
    aspect_ratio = fields.Str(required=False)
    
    url = fields.Str(required=False)
    

