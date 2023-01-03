"""payment Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














class CODdata(BaseSchema):
    #  swagger.json

    
    is_active = fields.Boolean(required=False)
    
    user_id = fields.Str(required=False)
    
    usages = fields.Int(required=False)
    
    limit = fields.Int(required=False)
    
    remaining_limit = fields.Int(required=False)
    
