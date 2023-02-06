"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










from .Action import Action









from .ImageUrls import ImageUrls





from .CollectionQuery import CollectionQuery





from .Media1 import Media1



















class GetCollectionDetailNest(BaseSchema):
    #  swagger.json

    
    is_active = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    
    cron = fields.Dict(required=False)
    
    action = fields.Nested(Action, required=False)
    
    name = fields.Str(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    uid = fields.Str(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    priority = fields.Int(required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
    app_id = fields.Str(required=False)
    
    logo = fields.Nested(Media1, required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    _schedule = fields.Dict(required=False)
    
    meta = fields.Dict(required=False)
    
    slug = fields.Str(required=False)
    
    badge = fields.Dict(required=False)
    
    description = fields.Str(required=False)
    
    tag = fields.List(fields.Str(required=False), required=False)
    
