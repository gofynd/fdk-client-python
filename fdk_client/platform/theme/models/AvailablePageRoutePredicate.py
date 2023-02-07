"""theme Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class AvailablePageRoutePredicate(BaseSchema):
    #  swagger.json

    
    selected = fields.Str(required=False)
    
    exact_url = fields.Str(required=False)
    
    query = fields.Dict(required=False)
    
