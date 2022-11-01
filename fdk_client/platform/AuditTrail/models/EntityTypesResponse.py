"""AuditTrail Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .EntityTypeObj import EntityTypeObj



class EntityTypesResponse(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(EntityTypeObj, required=False), required=False)
    
