"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema













from .AttributeMaster import AttributeMaster

from .AttributeMasterMeta import AttributeMasterMeta

from .AttributeMasterFilter import AttributeMasterFilter

from .AttributeMasterDetails import AttributeMasterDetails






class GenderDetail(BaseSchema):

    
    name = fields.Str(required=False)
    
    departments = fields.List(fields.Str(required=False), required=False)
    
    logo = fields.Str(required=False)
    
    enabled_for_end_consumer = fields.Boolean(required=False)
    
    description = fields.Str(required=False)
    
    is_nested = fields.Boolean(required=False)
    
    schema = fields.Nested(AttributeMaster, required=False)
    
    meta = fields.Nested(AttributeMasterMeta, required=False)
    
    filters = fields.Nested(AttributeMasterFilter, required=False)
    
    details = fields.Nested(AttributeMasterDetails, required=False)
    
    id = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    

