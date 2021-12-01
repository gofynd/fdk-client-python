"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .RedirectDevice import RedirectDevice

from .RedirectDevice import RedirectDevice

from .WebRedirect import WebRedirect




class Redirects(BaseSchema):

    
    ios = fields.Nested(RedirectDevice, required=False)
    
    android = fields.Nested(RedirectDevice, required=False)
    
    web = fields.Nested(WebRedirect, required=False)
    
    force_web = fields.Boolean(required=False)
    

