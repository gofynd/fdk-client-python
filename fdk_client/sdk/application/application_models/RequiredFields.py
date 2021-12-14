"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .PlatformEmail import PlatformEmail

from .PlatformMobile import PlatformMobile


class RequiredFields(BaseSchema):
    # User swagger.json

    
    email = fields.Nested(PlatformEmail, required=False)
    
    mobile = fields.Nested(PlatformMobile, required=False)
    

