"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








from .CollectionBadge import CollectionBadge



from .CollectionSchedule import CollectionSchedule







from .UserInfo import UserInfo



from .SeoDetail import SeoDetail









from .UserInfo import UserInfo













from .CollectionBanner import CollectionBanner









from .CollectionImage import CollectionImage







from .CollectionQuery import CollectionQuery



class CreateCollection(BaseSchema):
    #  swagger.json

    
    name = fields.Str(required=False)
    
    app_id = fields.Str(required=False)
    
    badge = fields.Nested(CollectionBadge, required=False)
    
    _schedule = fields.Nested(CollectionSchedule, required=False)
    
    _locale_language = fields.Dict(required=False)
    
    type = fields.Str(required=False)
    
    created_by = fields.Nested(UserInfo, required=False)
    
    seo = fields.Nested(SeoDetail, required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    is_active = fields.Boolean(required=False)
    
    slug = fields.Str(required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    published = fields.Boolean(required=False)
    
    meta = fields.Dict(required=False)
    
    is_visible = fields.Boolean(required=False)
    
    description = fields.Str(required=False)
    
    banners = fields.Nested(CollectionBanner, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    sort_on = fields.Str(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    logo = fields.Nested(CollectionImage, required=False)
    
    priority = fields.Int(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
