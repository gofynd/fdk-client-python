"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .EntityRegionViewItems import EntityRegionViewItems



from .EntityRegionViewError import EntityRegionViewError

from .EntityRegionViewPage import EntityRegionViewPage


class EntityRegionViewResponse(BaseSchema):
    # Serviceability swagger.json

    
    data = fields.List(fields.Nested(EntityRegionViewItems, required=False), required=False)
    
    success = fields.Boolean(required=False)
    
    error = fields.Nested(EntityRegionViewError, required=False)
    
    page = fields.Nested(EntityRegionViewPage, required=False)
    

