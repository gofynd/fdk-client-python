"""configuration Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class FreshchatCredentials(BaseSchema):
    #  swagger.json

    
    app_id = fields.Str(required=False)
    
    app_key = fields.Str(required=False)
    
    web_token = fields.Str(required=False)
    