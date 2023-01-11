"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema
















class ShipmentReason(BaseSchema):
    #  swagger.json

    
    reason_id = fields.Int(required=False)
    
    reason_text = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    
    feedback_type = fields.Str(required=False)
    
    flow = fields.Str(required=False)
    
    show_text_area = fields.Boolean(required=False)
    
