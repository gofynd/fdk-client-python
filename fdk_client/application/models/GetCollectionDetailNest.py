"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .Media import Media















from .ImageUrls import ImageUrls









from .CollectionQuery import CollectionQuery



from .ProductListingAction import ProductListingAction






class GetCollectionDetailNest(BaseSchema):
    # Catalog swagger.json

    
    priority = fields.Int(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    cron = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    
    logo = fields.Nested(Media, required=False)
    
    sort_on = fields.Str(required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    badge = fields.Dict(required=False)
    
    description = fields.Str(required=False)
    
    tag = fields.List(fields.Str(required=False), required=False)
    
    _schedule = fields.Dict(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    uid = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    is_active = fields.Boolean(required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    app_id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    

