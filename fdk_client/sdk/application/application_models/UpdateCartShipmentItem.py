"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema








class UpdateCartShipmentItem(BaseSchema):
    # PosCart swagger.json

    
    article_uid = fields.Str(required=False)
    
    shipment_type = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    

