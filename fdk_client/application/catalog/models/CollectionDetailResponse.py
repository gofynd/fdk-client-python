"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .Media import Media









from .CollectionQuery import CollectionQuery

















from .ImageUrls import ImageUrls

















class CollectionDetailResponse(BaseSchema):
    #  swagger.json

    
    logo = fields.Nested(Media, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    priority = fields.Int(required=False)
    
    description = fields.Str(required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
    meta = fields.Dict(required=False)
    
    badge = fields.Dict(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    slug = fields.Str(required=False)
    
    tag = fields.List(fields.Str(required=False), required=False)
    
    name = fields.Str(required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    type = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    cron = fields.Dict(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    sort_on = fields.Str(required=False)
    
    _schedule = fields.Dict(required=False)
    
    app_id = fields.Str(required=False)
    
