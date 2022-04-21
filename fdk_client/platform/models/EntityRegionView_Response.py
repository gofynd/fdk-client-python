"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .EntityRegionView_page import EntityRegionView_page

from .EntityRegionView_Error import EntityRegionView_Error

from .EntityRegionView_Items import EntityRegionView_Items




class EntityRegionView_Response(BaseSchema):
    # Serviceability swagger.json

    
    page = fields.Nested(EntityRegionView_page, required=False)
    
    error = fields.Nested(EntityRegionView_Error, required=False)
    
    data = fields.List(fields.Nested(EntityRegionView_Items, required=False), required=False)
    
    success = fields.Boolean(required=False)
    

