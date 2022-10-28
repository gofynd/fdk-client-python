"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .EntityRegionViewItems import EntityRegionViewItems

from .EntityRegionViewPage import EntityRegionViewPage

from .EntityRegionViewError import EntityRegionViewError


class EntityRegionViewResponse(BaseSchema):
    # Serviceability swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.List(fields.Nested(EntityRegionViewItems, required=False), required=False)
    
    page = fields.Nested(EntityRegionViewPage, required=False)
    
    error = fields.Nested(EntityRegionViewError, required=False)
    

