"""filestorage Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class Urls(BaseSchema):
    #  swagger.json

    
    url = fields.Str(required=False)
    
    signed_url = fields.Str(required=False)
    
    expiry = fields.Int(required=False)
    
