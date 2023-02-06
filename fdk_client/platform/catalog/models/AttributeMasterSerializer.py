"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






















from .AttributeMaster import AttributeMaster







from .AttributeMasterFilter import AttributeMasterFilter













from .AttributeMasterDetails import AttributeMasterDetails





class AttributeMasterSerializer(BaseSchema):
    #  swagger.json

    
    suggestion = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    modified_by = fields.Dict(required=False)
    
    unit = fields.Str(required=False)
    
    raw_key = fields.Str(required=False)
    
    synonyms = fields.Dict(required=False)
    
    is_nested = fields.Boolean(required=False)
    
    description = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    schema = fields.Nested(AttributeMaster, required=False)
    
    enabled_for_end_consumer = fields.Boolean(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    filters = fields.Nested(AttributeMasterFilter, required=False)
    
    variant = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    departments = fields.List(fields.Str(required=False), required=False)
    
    created_by = fields.Dict(required=False)
    
    details = fields.Nested(AttributeMasterDetails, required=False)
    
    modified_on = fields.Str(required=False)
    
