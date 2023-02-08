"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema


















from .SeoDetail import SeoDetail











from .CollectionImage import CollectionImage







from .CollectionBanner import CollectionBanner





from .CollectionQuery import CollectionQuery



from .UserInfo import UserInfo







from .UserInfo import UserInfo



from .CollectionSchedule import CollectionSchedule





from .CollectionBadge import CollectionBadge



class CreateCollection(BaseSchema):
    #  swagger.json

    
    allow_facets = fields.Boolean(required=False)
    
    published = fields.Boolean(required=False)
    
    sort_on = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    app_id = fields.Str(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    seo = fields.Nested(SeoDetail, required=False)
    
    name = fields.Str(required=False)
    
    _locale_language = fields.Dict(required=False)
    
    priority = fields.Int(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    logo = fields.Nested(CollectionImage, required=False)
    
    meta = fields.Dict(required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    banners = fields.Nested(CollectionBanner, required=False)
    
    is_visible = fields.Boolean(required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    slug = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    created_by = fields.Nested(UserInfo, required=False)
    
    _schedule = fields.Nested(CollectionSchedule, required=False)
    
    type = fields.Str(required=False)
    
    badge = fields.Nested(CollectionBadge, required=False)
    
