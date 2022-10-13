"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .TATArticlesRequest import TATArticlesRequest






class TATLocationDetailsRequest(BaseSchema):
    # Logistic swagger.json

    
    articles = fields.List(fields.Nested(TATArticlesRequest, required=False), required=False)
    
    from_pincode = fields.Str(required=False)
    
    fulfillment_id = fields.Int(required=False)
    

