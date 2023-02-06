"""logistic Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .LocationDetailsReq import LocationDetailsReq







class GetTatProductReqBody(BaseSchema):
    #  swagger.json

    
    location_details = fields.List(fields.Nested(LocationDetailsReq, required=False), required=False)
    
    to_pincode = fields.Str(required=False)
    
    action = fields.Str(required=False)
    
