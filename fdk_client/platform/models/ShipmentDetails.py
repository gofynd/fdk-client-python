"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema











from .ArticleDetails import ArticleDetails




class ShipmentDetails(BaseSchema):
    # OrderManage swagger.json

    
    affiliate_shipment_id = fields.Str(required=False)
    
    shipments = fields.Int(required=False)
    
    meta = fields.Dict(required=False)
    
    fulfillment_id = fields.Int(required=False)
    
    box_type = fields.Str(required=False)
    
    articles = fields.List(fields.Nested(ArticleDetails, required=False), required=False)
    
    dp_id = fields.Int(required=False)
    

