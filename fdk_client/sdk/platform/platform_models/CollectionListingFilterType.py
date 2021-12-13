"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema








class CollectionListingFilterType(BaseSchema):

    
    is_selected = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    display = fields.Str(required=False)
    

