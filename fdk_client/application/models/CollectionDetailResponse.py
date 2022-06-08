"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .ImageUrls import ImageUrls



















from .Media import Media










class CollectionDetailResponse(BaseSchema):
    # Catalog swagger.json

    
    is_active = fields.Boolean(required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    query = fields.Dict(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    meta = fields.Dict(required=False)
    
    tag = fields.List(fields.Str(required=False), required=False)
    
    _schedule = fields.Dict(required=False)
    
    badge = fields.Dict(required=False)
    
    app_id = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    
    description = fields.Str(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    logo = fields.Nested(Media, required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    cron = fields.Dict(required=False)
    
    type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    

