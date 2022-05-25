"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .CollectionImage import CollectionImage



from .CollectionBanner import CollectionBanner





from .SeoDetail import SeoDetail



from .Schedule import Schedule

from .UserInfo import UserInfo





from .CollectionQuery import CollectionQuery











from .UserInfo import UserInfo



from .CollectionBadge import CollectionBadge








class CreateCollection(BaseSchema):
    # Catalog swagger.json

    
    description = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    logo = fields.Nested(CollectionImage, required=False)
    
    slug = fields.Str(required=False)
    
    banners = fields.Nested(CollectionBanner, required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    seo = fields.Nested(SeoDetail, required=False)
    
    name = fields.Str(required=False)
    
    _schedule = fields.Nested(Schedule, required=False)
    
    created_by = fields.Nested(UserInfo, required=False)
    
    type = fields.Str(required=False)
    
    sort_on = fields.Str(required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    app_id = fields.Str(required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    published = fields.Boolean(required=False)
    
    _locale_language = fields.Dict(required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    badge = fields.Nested(CollectionBadge, required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    priority = fields.Int(required=False)
    
    is_visible = fields.Boolean(required=False)
    

