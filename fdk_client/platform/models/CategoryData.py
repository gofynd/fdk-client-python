"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .TicketCategory import TicketCategory


class CategoryData(BaseSchema):
    # Lead swagger.json

    
    list = fields.Nested(TicketCategory, required=False)
    

