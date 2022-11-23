"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .AttributeMasterFilter import AttributeMasterFilter



from .AttributeMaster import AttributeMaster

















from .AttributeMasterDetails import AttributeMasterDetails





from .AttributeMasterMeta import AttributeMasterMeta



class GenderDetail(BaseSchema):
    #  swagger.json

    
    filters = fields.Nested(AttributeMasterFilter, required=False)
    
    schema = fields.Nested(AttributeMaster, required=False)
    
    logo = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    is_nested = fields.Boolean(required=False)
    
    id = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    departments = fields.List(fields.Str(required=False), required=False)
    
    details = fields.Nested(AttributeMasterDetails, required=False)
    
    enabled_for_end_consumer = fields.Boolean(required=False)
    
    meta = fields.Nested(AttributeMasterMeta, required=False)
    
