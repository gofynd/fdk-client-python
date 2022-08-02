"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema















from .CollectionBanner import CollectionBanner





from .CollectionQuery import CollectionQuery





from .CollectionImage import CollectionImage





from .Schedule import Schedule





from .SeoDetail import SeoDetail



from .UserInfo import UserInfo

from .CollectionBadge import CollectionBadge


class UpdateCollection(BaseSchema):
    # Catalog swagger.json

    
    _locale_language = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    
    is_visible = fields.Boolean(required=False)
    
    sort_on = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    description = fields.Str(required=False)
    
    banners = fields.Nested(CollectionBanner, required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    published = fields.Boolean(required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
    type = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    logo = fields.Nested(CollectionImage, required=False)
    
    priority = fields.Int(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    _schedule = fields.Nested(Schedule, required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    seo = fields.Nested(SeoDetail, required=False)
    
    slug = fields.Str(required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    badge = fields.Nested(CollectionBadge, required=False)
    

