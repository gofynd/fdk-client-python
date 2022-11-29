"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .EntityRegionViewError import EntityRegionViewError

from .EntityRegionViewItems import EntityRegionViewItems

from .EntityRegionViewPage import EntityRegionViewPage




class EntityRegionViewResponse(BaseSchema):
    # Serviceability swagger.json

    
    error = fields.Nested(EntityRegionViewError, required=False)
    
    data = fields.List(fields.Nested(EntityRegionViewItems, required=False), required=False)
    
    page = fields.Nested(EntityRegionViewPage, required=False)
    
    success = fields.Boolean(required=False)
    

