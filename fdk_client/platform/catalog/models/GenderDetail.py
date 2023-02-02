"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










from .AttributeMasterMeta import AttributeMasterMeta



from .AttributeMaster import AttributeMaster









from .AttributeMasterDetails import AttributeMasterDetails





from .AttributeMasterFilter import AttributeMasterFilter





class GenderDetail(BaseSchema):
    #  swagger.json

    
    slug = fields.Str(required=False)
    
    departments = fields.List(fields.Str(required=False), required=False)
    
    description = fields.Str(required=False)
    
    meta = fields.Nested(AttributeMasterMeta, required=False)
    
    schema = fields.Nested(AttributeMaster, required=False)
    
    enabled_for_end_consumer = fields.Boolean(required=False)
    
    logo = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    details = fields.Nested(AttributeMasterDetails, required=False)
    
    id = fields.Str(required=False)
    
    filters = fields.Nested(AttributeMasterFilter, required=False)
    
    is_nested = fields.Boolean(required=False)
    
