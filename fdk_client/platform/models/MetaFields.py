"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class MetaFields(BaseSchema):
    # Catalog swagger.json

    
    key = fields.Raw(required=False)
    
    value = fields.Raw(required=False)
    

