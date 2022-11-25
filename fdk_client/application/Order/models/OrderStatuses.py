"""Order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










class OrderStatuses(BaseSchema):
    #  swagger.json

    
    is_selected = fields.Boolean(required=False)
    
    value = fields.Int(required=False)
    
    display = fields.Str(required=False)
    
