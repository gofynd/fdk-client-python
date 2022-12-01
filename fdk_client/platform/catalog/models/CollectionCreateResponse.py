"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




















from .ImageUrls import ImageUrls











from .CollectionQuery import CollectionQuery



from .BannerImage import BannerImage











class CollectionCreateResponse(BaseSchema):
    #  swagger.json

    
    type = fields.Str(required=False)
    
    app_id = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    description = fields.Str(required=False)
    
    _schedule = fields.Dict(required=False)
    
    priority = fields.Int(required=False)
    
    sort_on = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    tag = fields.List(fields.Str(required=False), required=False)
    
    slug = fields.Str(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
    logo = fields.Nested(BannerImage, required=False)
    
    cron = fields.Dict(required=False)
    
    meta = fields.Dict(required=False)
    
    badge = fields.Dict(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
