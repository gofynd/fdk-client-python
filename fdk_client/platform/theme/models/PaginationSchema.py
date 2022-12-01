"""theme Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














class PaginationSchema(BaseSchema):
    #  swagger.json

    
    size = fields.Int(required=False)
    
    item_total = fields.Int(required=False)
    
    has_next = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    
    current = fields.Int(required=False)
    
