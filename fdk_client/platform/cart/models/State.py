"""cart Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class State(BaseSchema):
    #  swagger.json

    
    is_public = fields.Boolean(required=False)
    
    is_display = fields.Boolean(required=False)
    
    is_archived = fields.Boolean(required=False)
    
