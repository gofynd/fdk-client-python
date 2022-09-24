"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .UserInfo import UserInfo





from .CollectionBadge import CollectionBadge











from .UserInfo import UserInfo

from .CollectionBanner import CollectionBanner











from .Schedule import Schedule





from .SeoDetail import SeoDetail

from .CollectionImage import CollectionImage

from .CollectionQuery import CollectionQuery




class CreateCollection(BaseSchema):
    # Catalog swagger.json

    
    is_visible = fields.Boolean(required=False)
    
    description = fields.Str(required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    is_active = fields.Boolean(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    badge = fields.Nested(CollectionBadge, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    slug = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    _locale_language = fields.Dict(required=False)
    
    sort_on = fields.Str(required=False)
    
    created_by = fields.Nested(UserInfo, required=False)
    
    banners = fields.Nested(CollectionBanner, required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    published = fields.Boolean(required=False)
    
    meta = fields.Dict(required=False)
    
    _schedule = fields.Nested(Schedule, required=False)
    
    priority = fields.Int(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    seo = fields.Nested(SeoDetail, required=False)
    
    logo = fields.Nested(CollectionImage, required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
    app_id = fields.Str(required=False)
    

