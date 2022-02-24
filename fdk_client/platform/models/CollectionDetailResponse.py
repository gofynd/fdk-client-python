"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema































from .CollectionMedia import CollectionMedia


class CollectionDetailResponse(BaseSchema):
    # Catalog swagger.json

    
    is_active = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    badge = fields.Dict(required=False)
    
    slug = fields.Str(required=False)
    
    _schedule = fields.Dict(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    query = fields.Dict(required=False)
    
    meta = fields.Dict(required=False)
    
    cron = fields.Dict(required=False)
    
    app_id = fields.Str(required=False)
    
    tag = fields.List(fields.Str(required=False), required=False)
    
    media = fields.Nested(CollectionMedia, required=False)
    

