"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .EntityRegionView_Items import EntityRegionView_Items

from .EntityRegionView_Error import EntityRegionView_Error



from .EntityRegionView_page import EntityRegionView_page


class EntityRegionView_Response_schema(BaseSchema):
    # Serviceability swagger.json

    
    data = fields.List(fields.Nested(EntityRegionView_Items, required=False), required=False)
    
    error = fields.Nested(EntityRegionView_Error, required=False)
    
    success = fields.Boolean(required=False)
    
    page = fields.Nested(EntityRegionView_page, required=False)
    

