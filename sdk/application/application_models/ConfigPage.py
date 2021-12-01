"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema






class ConfigPage(BaseSchema):

    
    settings = fields.Dict(required=False)
    
    page = fields.Str(required=False)
    

