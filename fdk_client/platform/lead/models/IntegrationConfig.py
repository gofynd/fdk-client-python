"""lead Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema
















from .CategoryData import CategoryData











class IntegrationConfig(BaseSchema):
    #  swagger.json

    
    _id = fields.Str(required=False)
    
    integration_type = fields.Str(required=False)
    
    base_url = fields.Str(required=False)
    
    create_ticket_apikey = fields.Str(required=False)
    
    update_ticket_apikey = fields.Str(required=False)
    
    category_sync_apikey = fields.Str(required=False)
    
    category_data = fields.Nested(CategoryData, required=False)
    
    webhook_apikey = fields.Str(required=False)
    
    config_completed = fields.Boolean(required=False)
    
    allow_ticket_creation = fields.Boolean(required=False)
    
    show_listing = fields.Boolean(required=False)
    