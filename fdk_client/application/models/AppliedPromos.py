"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema













from .AppliedFreeArticles import AppliedFreeArticles


class AppliedPromos(BaseSchema):
    # Order swagger.json

    
    amount = fields.Float(required=False)
    
    promo_id = fields.Str(required=False)
    
    promotion_name = fields.Str(required=False)
    
    promotion_type = fields.Str(required=False)
    
    article_quantity = fields.Float(required=False)
    
    mrp_promotion = fields.Boolean(required=False)
    
    applied_free_articles = fields.Nested(AppliedFreeArticles, required=False)
    
