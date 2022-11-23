"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .CollectionBanner import CollectionBanner



from .UserInfo import UserInfo







from .UserInfo import UserInfo







from .CollectionBadge import CollectionBadge





















from .CollectionSchedule import CollectionSchedule





from .SeoDetail import SeoDetail



from .CollectionQuery import CollectionQuery



from .CollectionImage import CollectionImage





class CreateCollection(BaseSchema):
    #  swagger.json

    
    is_active = fields.Boolean(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    banners = fields.Nested(CollectionBanner, required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    meta = fields.Dict(required=False)
    
    priority = fields.Int(required=False)
    
    created_by = fields.Nested(UserInfo, required=False)
    
    app_id = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    badge = fields.Nested(CollectionBadge, required=False)
    
    is_visible = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    sort_on = fields.Str(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    published = fields.Boolean(required=False)
    
    slug = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    
    _schedule = fields.Nested(CollectionSchedule, required=False)
    
    _locale_language = fields.Dict(required=False)
    
    seo = fields.Nested(SeoDetail, required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
    logo = fields.Nested(CollectionImage, required=False)
    
    description = fields.Str(required=False)
    
