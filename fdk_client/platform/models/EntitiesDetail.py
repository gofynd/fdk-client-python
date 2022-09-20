"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .EntityBody import EntityBody


class EntitiesDetail(BaseSchema):
    # Order swagger.json

    
    entity_id = fields.Nested(EntityBody, required=False)
    

