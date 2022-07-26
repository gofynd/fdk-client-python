"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .CollectionImage import CollectionImage





from .SeoDetail import SeoDetail



from .CollectionBanner import CollectionBanner





from .Schedule import Schedule



from .CollectionBadge import CollectionBadge



from .UserInfo import UserInfo














class UpdateCollection(BaseSchema):
    # Catalog swagger.json

    
    allow_sort = fields.Boolean(required=False)
    
    is_visible = fields.Boolean(required=False)
    
    logo = fields.Nested(CollectionImage, required=False)
    
    published = fields.Boolean(required=False)
    
    _locale_language = fields.Dict(required=False)
    
    seo = fields.Nested(SeoDetail, required=False)
    
    slug = fields.Str(required=False)
    
    banners = fields.Nested(CollectionBanner, required=False)
    
    sort_on = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    _schedule = fields.Nested(Schedule, required=False)
    
    description = fields.Str(required=False)
    
    badge = fields.Nested(CollectionBadge, required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    is_active = fields.Boolean(required=False)
    
    query = fields.Dict(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    meta = fields.Dict(required=False)
    

