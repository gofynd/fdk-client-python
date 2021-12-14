"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .Currency import Currency


class CurrenciesResponse(BaseSchema):
    # Configuration swagger.json

    
    items = fields.List(fields.Nested(Currency, required=False), required=False)
    

