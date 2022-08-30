"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ArticleDetails import ArticleDetails














class ShipmentDetails(BaseSchema):
    # Order swagger.json

    
    articles = fields.List(fields.Nested(ArticleDetails, required=False), required=False)
    
    meta = fields.Dict(required=False)
    
    dp_id = fields.Int(required=False)
    
    fulfillment_id = fields.Int(required=False)
    
    shipments = fields.Int(required=False)
    
    affiliate_shipment_id = fields.Str(required=False)
    
    box_type = fields.Str(required=False)
    
