"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema






class TicketSubCategory(BaseSchema):

    
    key = fields.Str(required=False)
    
    display = fields.Str(required=False)
    

