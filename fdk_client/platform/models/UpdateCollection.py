"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .CollectionQuery import CollectionQuery



from .CollectionBadge import CollectionBadge





from .CollectionImage import CollectionImage



from .UserInfo import UserInfo





from .SeoDetail import SeoDetail

from .Schedule import Schedule









from .CollectionBanner import CollectionBanner








class UpdateCollection(BaseSchema):
    # Catalog swagger.json

    
    sort_on = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
    meta = fields.Dict(required=False)
    
    badge = fields.Nested(CollectionBadge, required=False)
    
    _locale_language = fields.Dict(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    logo = fields.Nested(CollectionImage, required=False)
    
    description = fields.Str(required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    name = fields.Str(required=False)
    
    seo = fields.Nested(SeoDetail, required=False)
    
    _schedule = fields.Nested(Schedule, required=False)
    
    is_visible = fields.Boolean(required=False)
    
    priority = fields.Int(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    banners = fields.Nested(CollectionBanner, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    published = fields.Boolean(required=False)
    

