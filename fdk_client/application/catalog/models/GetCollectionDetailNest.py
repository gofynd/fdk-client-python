"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .CollectionQuery import CollectionQuery









from .ImageUrls import ImageUrls























from .ProductListingAction import ProductListingAction





from .Media import Media









class GetCollectionDetailNest(BaseSchema):
    #  swagger.json

    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    app_id = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    tag = fields.List(fields.Str(required=False), required=False)
    
    description = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    sort_on = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    
    cron = fields.Dict(required=False)
    
    priority = fields.Int(required=False)
    
    _schedule = fields.Dict(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    is_active = fields.Boolean(required=False)
    
    logo = fields.Nested(Media, required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    badge = fields.Dict(required=False)
    
    allow_sort = fields.Boolean(required=False)
    