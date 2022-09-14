"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .ArticlesResponse import ArticlesResponse




class LocationDetailsResponse(BaseSchema):
    # Logistic swagger.json

    
    from_pincode = fields.Str(required=False)
    
    articles = fields.List(fields.Nested(ArticlesResponse, required=False), required=False)
    
    fulfillment_id = fields.Int(required=False)
    

