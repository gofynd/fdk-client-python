"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema










from .ProductListingAction import ProductListingAction









from .CollectionQuery import CollectionQuery















from .Media import Media





from .ImageUrls import ImageUrls













class GetCollectionDetailNest(BaseSchema):
    #  swagger.json

    
    type = fields.Str(required=False)
    
    cron = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    tag = fields.List(fields.Str(required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
    uid = fields.Str(required=False)
    
    app_id = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    description = fields.Str(required=False)
    
    logo = fields.Nested(Media, required=False)
    
    meta = fields.Dict(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    sort_on = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    badge = fields.Dict(required=False)
    
    _schedule = fields.Dict(required=False)
    
