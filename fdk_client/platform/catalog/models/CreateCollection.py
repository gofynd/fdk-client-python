"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema












from .CollectionBadge import CollectionBadge









from .CollectionImage import CollectionImage



from .CollectionSchedule import CollectionSchedule





from .SeoDetail import SeoDetail







from .CollectionBanner import CollectionBanner





from .CollectionQuery import CollectionQuery











from .UserInfo import UserInfo







from .UserInfo import UserInfo



class CreateCollection(BaseSchema):
    #  swagger.json

    
    tags = fields.List(fields.Str(required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    description = fields.Str(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    badge = fields.Nested(CollectionBadge, required=False)
    
    _locale_language = fields.Dict(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    meta = fields.Dict(required=False)
    
    logo = fields.Nested(CollectionImage, required=False)
    
    _schedule = fields.Nested(CollectionSchedule, required=False)
    
    priority = fields.Int(required=False)
    
    seo = fields.Nested(SeoDetail, required=False)
    
    slug = fields.Str(required=False)
    
    app_id = fields.Str(required=False)
    
    banners = fields.Nested(CollectionBanner, required=False)
    
    type = fields.Str(required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
    sort_on = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    published = fields.Boolean(required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    is_visible = fields.Boolean(required=False)
    
    is_active = fields.Boolean(required=False)
    
    created_by = fields.Nested(UserInfo, required=False)
    
