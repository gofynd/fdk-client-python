"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema













from .ArticleDetails1 import ArticleDetails1


class ShipmentDetails(BaseSchema):
    # Order swagger.json

    
    box_type = fields.Str(required=False)
    
    fulfillment_id = fields.Int(required=False)
    
    dp_id = fields.Int(required=False)
    
    shipments = fields.Int(required=False)
    
    affiliate_shipment_id = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    articles = fields.List(fields.Nested(ArticleDetails1, required=False), required=False)
    

