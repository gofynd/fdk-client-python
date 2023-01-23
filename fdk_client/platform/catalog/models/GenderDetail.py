"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












from .AttributeMasterFilter import AttributeMasterFilter





from .AttributeMasterDetails import AttributeMasterDetails



from .AttributeMaster import AttributeMaster







from .AttributeMasterMeta import AttributeMasterMeta





class GenderDetail(BaseSchema):
    #  swagger.json

    
    slug = fields.Str(required=False)
    
    is_nested = fields.Boolean(required=False)
    
    description = fields.Str(required=False)
    
    enabled_for_end_consumer = fields.Boolean(required=False)
    
    filters = fields.Nested(AttributeMasterFilter, required=False)
    
    logo = fields.Str(required=False)
    
    details = fields.Nested(AttributeMasterDetails, required=False)
    
    schema = fields.Nested(AttributeMaster, required=False)
    
    id = fields.Str(required=False)
    
    departments = fields.List(fields.Str(required=False), required=False)
    
    meta = fields.Nested(AttributeMasterMeta, required=False)
    
    name = fields.Str(required=False)
    
