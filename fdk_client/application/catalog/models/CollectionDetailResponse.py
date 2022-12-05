"""catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




















from .ImageUrls import ImageUrls



from .CollectionQuery import CollectionQuery









from .Media import Media













class CollectionDetailResponse(BaseSchema):
    #  swagger.json

    
    tag = fields.List(fields.Str(required=False), required=False)
    
    badge = fields.Dict(required=False)
    
    cron = fields.Dict(required=False)
    
    app_id = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    sort_on = fields.Str(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    slug = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    logo = fields.Nested(Media, required=False)
    
    priority = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    _schedule = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    
