"""inventory Public Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PublicModel import BaseSchema






















from .StoreData import StoreData



class GStore(BaseSchema):
    #  swagger.json

    
    _id = fields.Str(required=False)
    
    integration = fields.Str(required=False)
    
    level = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    opted = fields.Boolean(required=False)
    
    permissions = fields.List(fields.Str(required=False), required=False)
    
    token = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    data = fields.Nested(StoreData, required=False)
    
