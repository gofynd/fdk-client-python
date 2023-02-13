"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .AffiliateMeta import AffiliateMeta


class AffiliateBagDetails(BaseSchema):
    # Orders swagger.json

    
    loyalty_discount = fields.Float(required=False)
    
    affiliate_bag_id = fields.Str(required=False)
    
    employee_discount = fields.Float(required=False)
    
    affiliate_order_id = fields.Str(required=False)
    
    affiliate_meta = fields.Nested(AffiliateMeta, required=False)
    
