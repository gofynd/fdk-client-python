"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .Language import Language

from .Language import Language

from .Language import Language


class LocaleLanguage(BaseSchema):
    # Content swagger.json

    
    hi = fields.Nested(Language, required=False)
    
    ar = fields.Nested(Language, required=False)
    
    en_us = fields.Nested(Language, required=False)
    

