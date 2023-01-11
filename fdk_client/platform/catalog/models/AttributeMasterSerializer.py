"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












from .AttributeMasterFilter import AttributeMasterFilter









from .AttributeMaster import AttributeMaster





















from .AttributeMasterDetails import AttributeMasterDetails





class AttributeMasterSerializer(BaseSchema):
    #  swagger.json

    
    suggestion = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    is_nested = fields.Boolean(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    filters = fields.Nested(AttributeMasterFilter, required=False)
    
    slug = fields.Str(required=False)
    
    variant = fields.Boolean(required=False)
    
    synonyms = fields.Dict(required=False)
    
    schema = fields.Nested(AttributeMaster, required=False)
    
    enabled_for_end_consumer = fields.Boolean(required=False)
    
    created_by = fields.Dict(required=False)
    
    logo = fields.Str(required=False)
    
    unit = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    modified_by = fields.Dict(required=False)
    
    departments = fields.List(fields.Str(required=False), required=False)
    
    modified_on = fields.Str(required=False)
    
    raw_key = fields.Str(required=False)
    
    details = fields.Nested(AttributeMasterDetails, required=False)
    
    description = fields.Str(required=False)
    
