"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .AttributeMasterDetails import AttributeMasterDetails















from .AttributeMasterFilter import AttributeMasterFilter















from .AttributeMaster import AttributeMaster











class AttributeMasterSerializer(BaseSchema):
    #  swagger.json

    
    departments = fields.List(fields.Str(required=False), required=False)
    
    details = fields.Nested(AttributeMasterDetails, required=False)
    
    enabled_for_end_consumer = fields.Boolean(required=False)
    
    created_on = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    raw_key = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    filters = fields.Nested(AttributeMasterFilter, required=False)
    
    variant = fields.Boolean(required=False)
    
    suggestion = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    unit = fields.Str(required=False)
    
    synonyms = fields.Dict(required=False)
    
    schema = fields.Nested(AttributeMaster, required=False)
    
    slug = fields.Str(required=False)
    
    created_by = fields.Dict(required=False)
    
    is_nested = fields.Boolean(required=False)
    
    modified_by = fields.Dict(required=False)
    
