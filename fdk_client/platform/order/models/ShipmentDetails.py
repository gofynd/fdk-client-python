"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .ArticleDetails import ArticleDetails











class ShipmentDetails(BaseSchema):
    #  swagger.json

    
    box_type = fields.Str(required=False)
    
    dp_id = fields.Int(required=False)
    
    articles = fields.List(fields.Nested(ArticleDetails, required=False), required=False)
    
    meta = fields.Dict(required=False)
    
    shipments = fields.Int(required=False)
    
    affiliate_shipment_id = fields.Str(required=False)
    
    fulfillment_id = fields.Int(required=False)
    
