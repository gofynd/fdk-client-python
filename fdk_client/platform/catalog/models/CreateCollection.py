"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .CollectionBanner import CollectionBanner





from .UserInfo import UserInfo





















from .CollectionBadge import CollectionBadge



from .SeoDetail import SeoDetail





from .CollectionQuery import CollectionQuery









from .CollectionImage import CollectionImage





from .UserInfo import UserInfo





from .CollectionSchedule import CollectionSchedule





class CreateCollection(BaseSchema):
    #  swagger.json

    
    banners = fields.Nested(CollectionBanner, required=False)
    
    slug = fields.Str(required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    _locale_language = fields.Dict(required=False)
    
    is_visible = fields.Boolean(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    meta = fields.Dict(required=False)
    
    type = fields.Str(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    published = fields.Boolean(required=False)
    
    badge = fields.Nested(CollectionBadge, required=False)
    
    seo = fields.Nested(SeoDetail, required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
    app_id = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    
    logo = fields.Nested(CollectionImage, required=False)
    
    sort_on = fields.Str(required=False)
    
    created_by = fields.Nested(UserInfo, required=False)
    
    is_active = fields.Boolean(required=False)
    
    _schedule = fields.Nested(CollectionSchedule, required=False)
    
    name = fields.Str(required=False)
    
