"""theme Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class UpgradableThemeSchema(BaseSchema):
    #  swagger.json

    
    parent_theme = fields.Str(required=False)
    
    applied_theme = fields.Str(required=False)
    
    upgrade = fields.Boolean(required=False)
    
