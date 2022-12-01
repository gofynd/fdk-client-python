"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .CollectionImage import CollectionImage





from .UserInfo import UserInfo





from .CollectionQuery import CollectionQuery







from .CollectionBadge import CollectionBadge





from .CollectionSchedule import CollectionSchedule









from .SeoDetail import SeoDetail



from .UserInfo import UserInfo











from .CollectionBanner import CollectionBanner









class CreateCollection(BaseSchema):
    #  swagger.json

    
    sort_on = fields.Str(required=False)
    
    published = fields.Boolean(required=False)
    
    logo = fields.Nested(CollectionImage, required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    name = fields.Str(required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    badge = fields.Nested(CollectionBadge, required=False)
    
    is_visible = fields.Boolean(required=False)
    
    _schedule = fields.Nested(CollectionSchedule, required=False)
    
    app_id = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    seo = fields.Nested(SeoDetail, required=False)
    
    created_by = fields.Nested(UserInfo, required=False)
    
    slug = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    _locale_language = fields.Dict(required=False)
    
    is_active = fields.Boolean(required=False)
    
    banners = fields.Nested(CollectionBanner, required=False)
    
    description = fields.Str(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    meta = fields.Dict(required=False)
    
