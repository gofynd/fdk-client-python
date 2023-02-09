"""logistic Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














class ZoneDataItem(BaseSchema):
    #  swagger.json

    
    current = fields.Int(required=False)
    
    size = fields.Int(required=False)
    
    item_total = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    has_next = fields.Boolean(required=False)
    
