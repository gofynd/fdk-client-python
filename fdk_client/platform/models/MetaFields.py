"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class MetaFields(BaseSchema):
    # Catalog swagger.json

    
    value = fields.Raw(required=False)
    
    key = fields.Raw(required=False)
    

