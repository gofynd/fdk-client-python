"""audittrail Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .EntityObject import EntityObject







class LogMetaObj(BaseSchema):
    #  swagger.json

    
    modifier = fields.Dict(required=False)
    
    application = fields.Str(required=False)
    
    entity = fields.Nested(EntityObject, required=False)
    
    device_info = fields.Dict(required=False)
    
    location = fields.Dict(required=False)
    
