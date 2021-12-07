"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema












class CouponValidity(BaseSchema):

    
    discount = fields.Float(required=False)
    
    code = fields.Str(required=False)
    
    valid = fields.Boolean(required=False)
    
    display_message_en = fields.Str(required=False)
    
    title = fields.Str(required=False)
    

