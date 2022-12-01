"""share Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class UrlInfo(BaseSchema):
    #  swagger.json

    
    original = fields.Str(required=False)
    
    short = fields.Str(required=False)
    
    hash = fields.Str(required=False)
    
