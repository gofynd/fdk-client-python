"""Catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








from .CollectionQuery import CollectionQuery







from .Media import Media







from .ImageUrls import ImageUrls























class CollectionDetailResponse(BaseSchema):
    #  swagger.json

    
    type = fields.Str(required=False)
    
    cron = fields.Dict(required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
    app_id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    logo = fields.Nested(Media, required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    sort_on = fields.Str(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    badge = fields.Dict(required=False)
    
    is_active = fields.Boolean(required=False)
    
    meta = fields.Dict(required=False)
    
    tag = fields.List(fields.Str(required=False), required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    priority = fields.Int(required=False)
    
    description = fields.Str(required=False)
    
    _schedule = fields.Dict(required=False)
    
    slug = fields.Str(required=False)
    
