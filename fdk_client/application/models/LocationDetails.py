"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .Articles import Articles




class LocationDetails(BaseSchema):
    # Logistic swagger.json

    
    from_pincode = fields.Str(required=False)
    
    articles = fields.List(fields.Nested(Articles, required=False), required=False)
    
    fulfillment_id = fields.Int(required=False)
    

