"""Discount Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .DiscountJob import DiscountJob



from .Page import Page



class ListOrCalender(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(DiscountJob, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
