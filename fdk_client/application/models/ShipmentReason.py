"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema














class ShipmentReason(BaseSchema):
    # Order swagger.json

    
    show_text_area = fields.Boolean(required=False)
    
    feedback_type = fields.Str(required=False)
    
    reason_text = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    
    flow = fields.Str(required=False)
    
    reason_id = fields.Int(required=False)
    

