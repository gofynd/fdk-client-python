"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .CollectionImage import CollectionImage





from .SeoDetail import SeoDetail













from .CollectionBanner import CollectionBanner

from .CollectionQuery1 import CollectionQuery1

from .CollectionBadge import CollectionBadge

from .UserInfo import UserInfo

from .Schedule import Schedule












class UpdateCollection(BaseSchema):
    # Catalog swagger.json

    
    _locale_language = fields.Dict(required=False)
    
    description = fields.Str(required=False)
    
    logo = fields.Nested(CollectionImage, required=False)
    
    priority = fields.Int(required=False)
    
    slug = fields.Str(required=False)
    
    seo = fields.Nested(SeoDetail, required=False)
    
    meta = fields.Dict(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    is_visible = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    banners = fields.Nested(CollectionBanner, required=False)
    
    query = fields.List(fields.Nested(CollectionQuery1, required=False), required=False)
    
    badge = fields.Nested(CollectionBadge, required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    _schedule = fields.Nested(Schedule, required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    sort_on = fields.Str(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    published = fields.Boolean(required=False)
    

