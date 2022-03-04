"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .Media import Media





from .ProductListingAction import ProductListingAction













from .ImageUrls import ImageUrls










class GetCollectionDetailNest(BaseSchema):
    # Catalog swagger.json

    
    meta = fields.Dict(required=False)
    
    tag = fields.List(fields.Str(required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    app_id = fields.Str(required=False)
    
    logo = fields.Nested(Media, required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    badge = fields.Dict(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    slug = fields.Str(required=False)
    
    query = fields.Dict(required=False)
    
    uid = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    _schedule = fields.Dict(required=False)
    
    cron = fields.Dict(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    description = fields.Str(required=False)
    

