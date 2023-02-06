"""inventory Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




















from .GStore import GStore



class GCompany(BaseSchema):
    #  swagger.json

    
    _id = fields.Str(required=False)
    
    integration = fields.Str(required=False)
    
    level = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    opted = fields.Boolean(required=False)
    
    permissions = fields.List(fields.Str(required=False), required=False)
    
    token = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    stores = fields.List(fields.Nested(GStore, required=False), required=False)
    
