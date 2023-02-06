"""logistic Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .TatReqProductArticles import TatReqProductArticles





class LocationDetailsReq(BaseSchema):
    #  swagger.json

    
    from_pincode = fields.Str(required=False)
    
    articles = fields.List(fields.Nested(TatReqProductArticles, required=False), required=False)
    
    fulfillment_id = fields.Int(required=False)
    
