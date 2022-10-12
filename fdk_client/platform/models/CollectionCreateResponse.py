"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

















from .ImageUrls import ImageUrls









from .CollectionQuery import CollectionQuery





from .BannerImage import BannerImage






class CollectionCreateResponse(BaseSchema):
    # Catalog swagger.json

    
    allow_sort = fields.Boolean(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    badge = fields.Dict(required=False)
    
    app_id = fields.Str(required=False)
    
    sort_on = fields.Str(required=False)
    
    _schedule = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    
    tag = fields.List(fields.Str(required=False), required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    description = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    
    meta = fields.Dict(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
    slug = fields.Str(required=False)
    
    cron = fields.Dict(required=False)
    
    logo = fields.Nested(BannerImage, required=False)
    
    type = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    

