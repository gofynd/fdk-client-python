"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






























from .AttributeMasterFilter import AttributeMasterFilter







from .AttributeMasterDetails import AttributeMasterDetails



from .AttributeMaster import AttributeMaster







class AttributeMasterSerializer(BaseSchema):
    #  swagger.json

    
    unit = fields.Str(required=False)
    
    is_nested = fields.Boolean(required=False)
    
    created_on = fields.Str(required=False)
    
    variant = fields.Boolean(required=False)
    
    raw_key = fields.Str(required=False)
    
    suggestion = fields.Str(required=False)
    
    departments = fields.List(fields.Str(required=False), required=False)
    
    logo = fields.Str(required=False)
    
    modified_by = fields.Dict(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    description = fields.Str(required=False)
    
    synonyms = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    
    filters = fields.Nested(AttributeMasterFilter, required=False)
    
    enabled_for_end_consumer = fields.Boolean(required=False)
    
    modified_on = fields.Str(required=False)
    
    details = fields.Nested(AttributeMasterDetails, required=False)
    
    schema = fields.Nested(AttributeMaster, required=False)
    
    created_by = fields.Dict(required=False)
    
    slug = fields.Str(required=False)
    
