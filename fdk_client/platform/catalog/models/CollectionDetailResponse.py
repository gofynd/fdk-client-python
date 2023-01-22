"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










from .Media1 import Media1























from .CollectionQuery import CollectionQuery







from .ImageUrls import ImageUrls



class CollectionDetailResponse(BaseSchema):
    #  swagger.json

    
    priority = fields.Int(required=False)
    
    description = fields.Str(required=False)
    
    app_id = fields.Str(required=False)
    
    logo = fields.Nested(Media1, required=False)
    
    meta = fields.Dict(required=False)
    
    badge = fields.Dict(required=False)
    
    slug = fields.Str(required=False)
    
    cron = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    tag = fields.List(fields.Str(required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
    _schedule = fields.Dict(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    