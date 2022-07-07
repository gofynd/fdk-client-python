"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .AttributeMasterFilter import AttributeMasterFilter

from .AttributeMasterMeta import AttributeMasterMeta









from .AttributeMaster import AttributeMaster





from .AttributeMasterDetails import AttributeMasterDetails


class GenderDetail(BaseSchema):
    # Catalog swagger.json

    
    id = fields.Str(required=False)
    
    is_nested = fields.Boolean(required=False)
    
    filters = fields.Nested(AttributeMasterFilter, required=False)
    
    meta = fields.Nested(AttributeMasterMeta, required=False)
    
    departments = fields.List(fields.Str(required=False), required=False)
    
    logo = fields.Str(required=False)
    
    enabled_for_end_consumer = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    schema = fields.Nested(AttributeMaster, required=False)
    
    slug = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    details = fields.Nested(AttributeMasterDetails, required=False)
    

