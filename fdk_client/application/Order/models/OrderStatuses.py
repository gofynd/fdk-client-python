"""Order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class OrderStatuses(BaseSchema):
    #  swagger.json

    
    display = fields.Str(required=False)
    
    value = fields.Int(required=False)
    
    is_selected = fields.Boolean(required=False)
    
