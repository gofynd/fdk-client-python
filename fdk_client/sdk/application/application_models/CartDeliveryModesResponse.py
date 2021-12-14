"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema






class CartDeliveryModesResponse(BaseSchema):
    # PosCart swagger.json

    
    pickup_stores = fields.List(fields.Int(required=False), required=False)
    
    available_modes = fields.List(fields.Str(required=False), required=False)
    

