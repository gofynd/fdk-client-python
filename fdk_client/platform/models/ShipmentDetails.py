"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .ArticleDetails import ArticleDetails






class ShipmentDetails(BaseSchema):
    # Order swagger.json

    
    dp_id = fields.Int(required=False)
    
    box_type = fields.Str(required=False)
    
    affiliate_shipment_id = fields.Str(required=False)
    
    fulfillment_id = fields.Int(required=False)
    
    articles = fields.List(fields.Nested(ArticleDetails, required=False), required=False)
    
    meta = fields.Dict(required=False)
    
    shipments = fields.Int(required=False)
    

