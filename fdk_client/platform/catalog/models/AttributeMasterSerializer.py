"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .AttributeMasterDetails import AttributeMasterDetails









from .AttributeMasterFilter import AttributeMasterFilter

























from .AttributeMaster import AttributeMaster





class AttributeMasterSerializer(BaseSchema):
    #  swagger.json

    
    is_nested = fields.Boolean(required=False)
    
    synonyms = fields.Dict(required=False)
    
    details = fields.Nested(AttributeMasterDetails, required=False)
    
    modified_by = fields.Dict(required=False)
    
    logo = fields.Str(required=False)
    
    raw_key = fields.Str(required=False)
    
    filters = fields.Nested(AttributeMasterFilter, required=False)
    
    created_by = fields.Dict(required=False)
    
    enabled_for_end_consumer = fields.Boolean(required=False)
    
    variant = fields.Boolean(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    created_on = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    departments = fields.List(fields.Str(required=False), required=False)
    
    unit = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    suggestion = fields.Str(required=False)
    
    schema = fields.Nested(AttributeMaster, required=False)
    
    modified_on = fields.Str(required=False)
    
