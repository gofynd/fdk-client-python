"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .ArticleDetails1 import ArticleDetails1











class ShipmentDetails(BaseSchema):
    #  swagger.json

    
    fulfillment_id = fields.Int(required=False)
    
    affiliate_shipment_id = fields.Str(required=False)
    
    articles = fields.List(fields.Nested(ArticleDetails1, required=False), required=False)
    
    meta = fields.Dict(required=False)
    
    dp_id = fields.Int(required=False)
    
    box_type = fields.Str(required=False)
    
    shipments = fields.Int(required=False)
    
