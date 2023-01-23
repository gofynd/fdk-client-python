"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .AttributeMasterDetails import AttributeMasterDetails

















from .AttributeMasterFilter import AttributeMasterFilter





from .AttributeMaster import AttributeMaster












class AttributeMasterSerializer(BaseSchema):
    # Catalog swagger.json

    
    synonyms = fields.Dict(required=False)
    
    departments = fields.List(fields.Str(required=False), required=False)
    
    details = fields.Nested(AttributeMasterDetails, required=False)
    
    enabled_for_end_consumer = fields.Boolean(required=False)
    
    is_nested = fields.Boolean(required=False)
    
    unit = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    created_by = fields.Dict(required=False)
    
    slug = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    filters = fields.Nested(AttributeMasterFilter, required=False)
    
    modified_on = fields.Str(required=False)
    
    variant = fields.Boolean(required=False)
    
    schema = fields.Nested(AttributeMaster, required=False)
    
    description = fields.Str(required=False)
    
    suggestion = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    modified_by = fields.Dict(required=False)
    
    raw_key = fields.Str(required=False)
    

