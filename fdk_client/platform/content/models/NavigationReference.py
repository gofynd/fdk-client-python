"""content Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .LocaleLanguage import LocaleLanguage







from .Action import Action











class NavigationReference(BaseSchema):
    #  swagger.json

    
    acl = fields.List(fields.Str(required=False), required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    _locale_language = fields.Nested(LocaleLanguage, required=False)
    
    image = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    action = fields.Nested(Action, required=False)
    
    active = fields.Boolean(required=False)
    
    display = fields.Str(required=False)
    
    sort_order = fields.Int(required=False)
    
    sub_navigation = fields.List(fields.Nested(lambda: NavigationReference(exclude=('sub_navigation')), required=False), required=False)
    
