"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .EntityRegionView_Error import EntityRegionView_Error

from .EntityRegionView_Items import EntityRegionView_Items

from .EntityRegionView_page import EntityRegionView_page




class EntityRegionView_Response(BaseSchema):
    # Serviceability swagger.json

    
    error = fields.Nested(EntityRegionView_Error, required=False)
    
    data = fields.List(fields.Nested(EntityRegionView_Items, required=False), required=False)
    
    page = fields.Nested(EntityRegionView_page, required=False)
    
    success = fields.Boolean(required=False)
    
