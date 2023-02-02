"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .SeoDetail import SeoDetail



from .CollectionQuery import CollectionQuery





from .CollectionBanner import CollectionBanner









from .CollectionImage import CollectionImage









from .UserInfo import UserInfo













from .CollectionSchedule import CollectionSchedule



from .CollectionBadge import CollectionBadge









from .UserInfo import UserInfo







class CreateCollection(BaseSchema):
    #  swagger.json

    
    seo = fields.Nested(SeoDetail, required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    banners = fields.Nested(CollectionBanner, required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    priority = fields.Int(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    logo = fields.Nested(CollectionImage, required=False)
    
    app_id = fields.Str(required=False)
    
    _locale_language = fields.Dict(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    description = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    published = fields.Boolean(required=False)
    
    _schedule = fields.Nested(CollectionSchedule, required=False)
    
    badge = fields.Nested(CollectionBadge, required=False)
    
    sort_on = fields.Str(required=False)
    
    is_visible = fields.Boolean(required=False)
    
    is_active = fields.Boolean(required=False)
    
    created_by = fields.Nested(UserInfo, required=False)
    
    meta = fields.Dict(required=False)
    
    slug = fields.Str(required=False)
    
