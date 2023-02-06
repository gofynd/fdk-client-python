"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema
















class ApplicationDepartment(BaseSchema):
    #  swagger.json

    
    is_active = fields.Boolean(required=False)
    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    app_id = fields.Str(required=False)
    
