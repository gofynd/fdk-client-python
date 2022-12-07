"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class Dates(BaseSchema):
    # Orders swagger.json

    
    order_created = fields.Str(required=False)
    
    delivery_date = fields.Raw(required=False)
    

