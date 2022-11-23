"""Payment Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














class CODdata(BaseSchema):
    #  swagger.json

    
    user_id = fields.Str(required=False)
    
    remaining_limit = fields.Int(required=False)
    
    usages = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    limit = fields.Int(required=False)
    
