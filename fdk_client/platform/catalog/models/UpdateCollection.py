"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .CollectionBanner import CollectionBanner



from .SeoDetail import SeoDetail



from .CollectionBadge import CollectionBadge





















from .UserInfo import UserInfo





from .CollectionImage import CollectionImage



from .CollectionQuery import CollectionQuery











from .CollectionSchedule import CollectionSchedule





class UpdateCollection(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    banners = fields.Nested(CollectionBanner, required=False)
    
    seo = fields.Nested(SeoDetail, required=False)
    
    badge = fields.Nested(CollectionBadge, required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    meta = fields.Dict(required=False)
    
    slug = fields.Str(required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    is_active = fields.Boolean(required=False)
    
    priority = fields.Int(required=False)
    
    is_visible = fields.Boolean(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    description = fields.Str(required=False)
    
    logo = fields.Nested(CollectionImage, required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
    _locale_language = fields.Dict(required=False)
    
    type = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    published = fields.Boolean(required=False)
    
    _schedule = fields.Nested(CollectionSchedule, required=False)
    
    sort_on = fields.Str(required=False)
    
