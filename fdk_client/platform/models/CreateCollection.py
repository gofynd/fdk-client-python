"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .CollectionBanner import CollectionBanner







from .Schedule import Schedule







from .UserInfo import UserInfo

from .SeoDetail import SeoDetail







from .CollectionBadge import CollectionBadge

from .CollectionImage import CollectionImage





from .UserInfo import UserInfo













from .CollectionQuery import CollectionQuery


class CreateCollection(BaseSchema):
    # Catalog swagger.json

    
    banners = fields.Nested(CollectionBanner, required=False)
    
    slug = fields.Str(required=False)
    
    app_id = fields.Str(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    _schedule = fields.Nested(Schedule, required=False)
    
    meta = fields.Dict(required=False)
    
    _locale_language = fields.Dict(required=False)
    
    is_visible = fields.Boolean(required=False)
    
    created_by = fields.Nested(UserInfo, required=False)
    
    seo = fields.Nested(SeoDetail, required=False)
    
    type = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    description = fields.Str(required=False)
    
    badge = fields.Nested(CollectionBadge, required=False)
    
    logo = fields.Nested(CollectionImage, required=False)
    
    priority = fields.Int(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    sort_on = fields.Str(required=False)
    
    published = fields.Boolean(required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    

