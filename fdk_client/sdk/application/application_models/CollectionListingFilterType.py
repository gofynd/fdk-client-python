"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema








class CollectionListingFilterType(BaseSchema):
    # Catalog swagger.json

    
    display = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    is_selected = fields.Boolean(required=False)
    

