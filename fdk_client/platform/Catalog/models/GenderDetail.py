"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .AttributeMasterDetails import AttributeMasterDetails



from .AttributeMasterMeta import AttributeMasterMeta





from .AttributeMasterFilter import AttributeMasterFilter

















from .AttributeMaster import AttributeMaster



class GenderDetail(BaseSchema):
    #  swagger.json

    
    details = fields.Nested(AttributeMasterDetails, required=False)
    
    meta = fields.Nested(AttributeMasterMeta, required=False)
    
    slug = fields.Str(required=False)
    
    filters = fields.Nested(AttributeMasterFilter, required=False)
    
    enabled_for_end_consumer = fields.Boolean(required=False)
    
    id = fields.Str(required=False)
    
    is_nested = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    departments = fields.List(fields.Str(required=False), required=False)
    
    description = fields.Str(required=False)
    
    schema = fields.Nested(AttributeMaster, required=False)
    
