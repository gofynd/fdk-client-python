"""logistic Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .TATArticlesRequest import TATArticlesRequest





class TATLocationDetailsRequest(BaseSchema):
    #  swagger.json

    
    from_pincode = fields.Str(required=False)
    
    articles = fields.List(fields.Nested(TATArticlesRequest, required=False), required=False)
    
    fulfillment_id = fields.Int(required=False)
    
