"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema























from .AttributeMasterDetails import AttributeMasterDetails





from .AttributeMaster import AttributeMaster

from .AttributeMasterFilter import AttributeMasterFilter










class AttributeMasterSerializer(BaseSchema):
    # Catalog swagger.json

    
    departments = fields.List(fields.Str(required=False), required=False)
    
    modified_on = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    unit = fields.Str(required=False)
    
    suggestion = fields.Str(required=False)
    
    raw_key = fields.Str(required=False)
    
    variant = fields.Boolean(required=False)
    
    slug = fields.Str(required=False)
    
    synonyms = fields.Dict(required=False)
    
    logo = fields.Str(required=False)
    
    is_nested = fields.Boolean(required=False)
    
    details = fields.Nested(AttributeMasterDetails, required=False)
    
    modified_by = fields.Dict(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    schema = fields.Nested(AttributeMaster, required=False)
    
    filters = fields.Nested(AttributeMasterFilter, required=False)
    
    description = fields.Str(required=False)
    
    enabled_for_end_consumer = fields.Boolean(required=False)
    
    created_by = fields.Dict(required=False)
    
    created_on = fields.Str(required=False)
    

