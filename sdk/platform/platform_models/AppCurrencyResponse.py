"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema



from .DefaultCurrency import DefaultCurrency

from .Currency import Currency


class AppCurrencyResponse(BaseSchema):

    
    application = fields.Str(required=False)
    
    default_currency = fields.Nested(DefaultCurrency, required=False)
    
    supported_currency = fields.List(fields.Nested(Currency, required=False), required=False)
    

