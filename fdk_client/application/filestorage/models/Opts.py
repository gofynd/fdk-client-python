"""filestorage Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class Opts(BaseSchema):
    #  swagger.json

    
    attempts = fields.Int(required=False)
    
    timestamp = fields.Int(required=False)
    
    delay = fields.Int(required=False)
    
