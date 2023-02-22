"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class Hierarchy(BaseSchema):
    #  swagger.json

    
    l2 = fields.Int(required=False)
    
    l1 = fields.Int(required=False)
    
    department = fields.Int(required=False)
    
