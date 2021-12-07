"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema








class CollectionListingFilterTag(BaseSchema):

    
    is_selected = fields.Boolean(required=False)
    
    display = fields.Str(required=False)
    
    name = fields.Str(required=False)
    

