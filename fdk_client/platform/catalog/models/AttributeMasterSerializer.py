"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema


















from .AttributeMaster import AttributeMaster















from .AttributeMasterFilter import AttributeMasterFilter





from .AttributeMasterDetails import AttributeMasterDetails









class AttributeMasterSerializer(BaseSchema):
    #  swagger.json

    
    logo = fields.Str(required=False)
    
    enabled_for_end_consumer = fields.Boolean(required=False)
    
    is_nested = fields.Boolean(required=False)
    
    created_by = fields.Dict(required=False)
    
    synonyms = fields.Dict(required=False)
    
    unit = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    schema = fields.Nested(AttributeMaster, required=False)
    
    modified_by = fields.Dict(required=False)
    
    description = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    name = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    suggestion = fields.Str(required=False)
    
    filters = fields.Nested(AttributeMasterFilter, required=False)
    
    slug = fields.Str(required=False)
    
    details = fields.Nested(AttributeMasterDetails, required=False)
    
    departments = fields.List(fields.Str(required=False), required=False)
    
    raw_key = fields.Str(required=False)
    
    variant = fields.Boolean(required=False)
    
