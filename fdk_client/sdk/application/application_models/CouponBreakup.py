"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema














class CouponBreakup(BaseSchema):
    # Cart swagger.json

    
    value = fields.Float(required=False)
    
    type = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    is_applied = fields.Boolean(required=False)
    

