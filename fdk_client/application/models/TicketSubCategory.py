"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class TicketSubCategory(BaseSchema):
    # Lead swagger.json

    
    key = fields.Str(required=False)
    
    display = fields.Str(required=False)
    
    sub_categories = fields.Nested(lambda: TicketSubCategory(exclude=('sub_categories')), required=False)
    

