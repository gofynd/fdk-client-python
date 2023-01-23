"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .CollectionBanner import CollectionBanner







from .CollectionBadge import CollectionBadge



















from .CollectionSchedule import CollectionSchedule





from .CollectionImage import CollectionImage





from .UserInfo import UserInfo



from .UserInfo import UserInfo



from .SeoDetail import SeoDetail



from .CollectionQuery import CollectionQuery













class CreateCollection(BaseSchema):
    #  swagger.json

    
    banners = fields.Nested(CollectionBanner, required=False)
    
    name = fields.Str(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    badge = fields.Nested(CollectionBadge, required=False)
    
    priority = fields.Int(required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    app_id = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    meta = fields.Dict(required=False)
    
    _locale_language = fields.Dict(required=False)
    
    _schedule = fields.Nested(CollectionSchedule, required=False)
    
    is_visible = fields.Boolean(required=False)
    
    logo = fields.Nested(CollectionImage, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    created_by = fields.Nested(UserInfo, required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    seo = fields.Nested(SeoDetail, required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
    published = fields.Boolean(required=False)
    
    is_active = fields.Boolean(required=False)
    
    sort_on = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
