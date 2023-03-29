"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .GiftDetail import GiftDetail


class ArticleGiftDetail(BaseSchema):
    # Cart swagger.json

    
    article_id = fields.Nested(GiftDetail, required=False)
    

