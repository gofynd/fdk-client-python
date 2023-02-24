"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ArticleGiftDetail import ArticleGiftDetail










class CartMetaRequest(BaseSchema):
    # Cart swagger.json

    
    gift_details = fields.Nested(ArticleGiftDetail, required=False)
    
    checkout_mode = fields.Str(required=False)
    
    gstin = fields.Str(required=False)
    
    comment = fields.Str(required=False)
    
    pick_up_customer_details = fields.Dict(required=False)
    

