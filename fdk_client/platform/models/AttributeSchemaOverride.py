"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .AttributeMaster import AttributeMaster




class AttributeSchemaOverride(BaseSchema):
    # Catalog swagger.json

    
    schema = fields.Nested(AttributeMaster, required=False)
    
    attribute = fields.Str(required=False)
    

