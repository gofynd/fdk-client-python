"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














from .AttributeMasterDetails import AttributeMasterDetails



from .AttributeMasterFilter import AttributeMasterFilter







from .AttributeMasterMeta import AttributeMasterMeta





from .AttributeMaster import AttributeMaster



class GenderDetail(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    is_nested = fields.Boolean(required=False)
    
    departments = fields.List(fields.Str(required=False), required=False)
    
    logo = fields.Str(required=False)
    
    enabled_for_end_consumer = fields.Boolean(required=False)
    
    details = fields.Nested(AttributeMasterDetails, required=False)
    
    filters = fields.Nested(AttributeMasterFilter, required=False)
    
    slug = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    meta = fields.Nested(AttributeMasterMeta, required=False)
    
    id = fields.Str(required=False)
    
    schema = fields.Nested(AttributeMaster, required=False)
    
