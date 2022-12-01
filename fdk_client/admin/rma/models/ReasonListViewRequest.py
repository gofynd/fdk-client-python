"""rma Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class ReasonListViewRequest(BaseSchema):
    #  swagger.json

    
    display_name = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    slug = fields.Str(required=False)
    
