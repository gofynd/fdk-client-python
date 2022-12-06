"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .UserInfo import UserInfo





from .CollectionImage import CollectionImage





from .CollectionBadge import CollectionBadge





from .CollectionBanner import CollectionBanner









from .SeoDetail import SeoDetail



from .CollectionSchedule import CollectionSchedule











from .CollectionQuery import CollectionQuery















class UpdateCollection(BaseSchema):
    #  swagger.json

    
    modified_by = fields.Nested(UserInfo, required=False)
    
    priority = fields.Int(required=False)
    
    logo = fields.Nested(CollectionImage, required=False)
    
    description = fields.Str(required=False)
    
    badge = fields.Nested(CollectionBadge, required=False)
    
    meta = fields.Dict(required=False)
    
    banners = fields.Nested(CollectionBanner, required=False)
    
    _locale_language = fields.Dict(required=False)
    
    slug = fields.Str(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    seo = fields.Nested(SeoDetail, required=False)
    
    _schedule = fields.Nested(CollectionSchedule, required=False)
    
    published = fields.Boolean(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    is_visible = fields.Boolean(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
    sort_on = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
