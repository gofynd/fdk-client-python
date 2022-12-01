"""filestorage Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class SignUrlRequest(BaseSchema):
    #  swagger.json

    
    expiry = fields.Int(required=False)
    
    urls = fields.List(fields.Str(required=False), required=False)
    
