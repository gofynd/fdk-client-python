"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .SeoDetail import SeoDetail

from .UserInfo import UserInfo







from .CollectionImage import CollectionImage



















from .CollectionBadge import CollectionBadge



from .CollectionBanner import CollectionBanner

from .Schedule import Schedule





from .UserInfo import UserInfo


class CreateCollection(BaseSchema):
    # Catalog swagger.json

    
    is_visible = fields.Boolean(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    seo = fields.Nested(SeoDetail, required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    meta = fields.Dict(required=False)
    
    description = fields.Str(required=False)
    
    published = fields.Boolean(required=False)
    
    logo = fields.Nested(CollectionImage, required=False)
    
    _locale_language = fields.Dict(required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    sort_on = fields.Str(required=False)
    
    query = fields.Dict(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    name = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    badge = fields.Nested(CollectionBadge, required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    banners = fields.Nested(CollectionBanner, required=False)
    
    _schedule = fields.Nested(Schedule, required=False)
    
    slug = fields.Str(required=False)
    
    app_id = fields.Str(required=False)
    
    created_by = fields.Nested(UserInfo, required=False)
    

