"""logistic Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








from .TATArticlesResponse import TATArticlesResponse



class TATLocationDetailsResponse(BaseSchema):
    #  swagger.json

    
    from_pincode = fields.Str(required=False)
    
    fulfillment_id = fields.Int(required=False)
    
    articles = fields.List(fields.Nested(TATArticlesResponse, required=False), required=False)
    
