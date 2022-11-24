"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .DiscountItems import DiscountItems


class BulkDiscount(BaseSchema):
    # Discount swagger.json

    
    company_id = fields.Int(required=False)
    
    items = fields.List(fields.Nested(DiscountItems, required=False), required=False)
    

