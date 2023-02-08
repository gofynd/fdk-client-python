"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema


















from .BannerImage import BannerImage







from .ImageUrls import ImageUrls



from .CollectionQuery import CollectionQuery

















class CollectionCreateResponse(BaseSchema):
    #  swagger.json

    
    allow_facets = fields.Boolean(required=False)
    
    sort_on = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    app_id = fields.Str(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    name = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    
    logo = fields.Nested(BannerImage, required=False)
    
    meta = fields.Dict(required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
    slug = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    cron = fields.Dict(required=False)
    
    _schedule = fields.Dict(required=False)
    
    type = fields.Str(required=False)
    
    tag = fields.List(fields.Str(required=False), required=False)
    
    badge = fields.Dict(required=False)
    
