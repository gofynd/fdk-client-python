"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class SEOData(BaseSchema):
    # Catalog swagger.json

    
    description = fields.Raw(required=False)
    
    title = fields.Raw(required=False)
    
