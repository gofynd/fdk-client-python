"""configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class LaunchPage(BaseSchema):
    #  swagger.json

    
    page_type = fields.Str(required=False)
    
    params = fields.Dict(required=False)
    
    query = fields.Dict(required=False)
    
