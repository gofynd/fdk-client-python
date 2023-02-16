"""audittrail Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class EntityTypeObj(BaseSchema):
    #  swagger.json

    
    entity_value = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
