"""configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .LaunchPage import LaunchPage











class LandingPageFeature(BaseSchema):
    #  swagger.json

    
    launch_page = fields.Nested(LaunchPage, required=False)
    
    continue_as_guest = fields.Boolean(required=False)
    
    login_btn_text = fields.Str(required=False)
    
    show_domain_textbox = fields.Boolean(required=False)
    
    show_register_btn = fields.Boolean(required=False)
    
