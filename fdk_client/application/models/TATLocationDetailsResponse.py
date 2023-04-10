"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .TATArticlesResponse import TATArticlesResponse






class TATLocationDetailsResponse(BaseSchema):
    # Logistic swagger.json

    
    articles = fields.List(fields.Nested(TATArticlesResponse, required=False), required=False)
    
    fulfillment_id = fields.Int(required=False)
    
    from_pincode = fields.Str(required=False)
    

