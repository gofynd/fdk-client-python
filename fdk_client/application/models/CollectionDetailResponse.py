"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .Media import Media







from .CollectionQuery import CollectionQuery













from .ImageUrls import ImageUrls










class CollectionDetailResponse(BaseSchema):
    # Catalog swagger.json

    
    tag = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    logo = fields.Nested(Media, required=False)
    
    _schedule = fields.Dict(required=False)
    
    meta = fields.Dict(required=False)
    
    is_active = fields.Boolean(required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
    priority = fields.Int(required=False)
    
    cron = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    
    badge = fields.Dict(required=False)
    
    slug = fields.Str(required=False)
    
    sort_on = fields.Str(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    description = fields.Str(required=False)
    
    app_id = fields.Str(required=False)
    
    allow_sort = fields.Boolean(required=False)
    

