"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

















from .ImageUrls import ImageUrls



from .ProductListingAction import ProductListingAction

















from .Media import Media



from .CollectionQuery import CollectionQuery


class GetCollectionDetailNest(BaseSchema):
    # Catalog swagger.json

    
    slug = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    badge = fields.Dict(required=False)
    
    cron = fields.Dict(required=False)
    
    sort_on = fields.Str(required=False)
    
    app_id = fields.Str(required=False)
    
    _schedule = fields.Dict(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    priority = fields.Int(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    name = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    tag = fields.List(fields.Str(required=False), required=False)
    
    meta = fields.Dict(required=False)
    
    description = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    logo = fields.Nested(Media, required=False)
    
    uid = fields.Str(required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    

