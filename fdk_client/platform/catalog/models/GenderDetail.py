"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .AttributeMaster import AttributeMaster









from .AttributeMasterDetails import AttributeMasterDetails



from .AttributeMasterFilter import AttributeMasterFilter







from .AttributeMasterMeta import AttributeMasterMeta









class GenderDetail(BaseSchema):
    #  swagger.json

    
    schema = fields.Nested(AttributeMaster, required=False)
    
    description = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    enabled_for_end_consumer = fields.Boolean(required=False)
    
    details = fields.Nested(AttributeMasterDetails, required=False)
    
    filters = fields.Nested(AttributeMasterFilter, required=False)
    
    is_nested = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    meta = fields.Nested(AttributeMasterMeta, required=False)
    
    logo = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    departments = fields.List(fields.Str(required=False), required=False)
    
