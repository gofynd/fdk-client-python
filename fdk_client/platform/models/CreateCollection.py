"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Schedule import Schedule













from .UserInfo import UserInfo

from .UserInfo import UserInfo





from .SeoDetail import SeoDetail









from .CollectionBadge import CollectionBadge



from .CollectionBanner import CollectionBanner

from .CollectionImage import CollectionImage










class CreateCollection(BaseSchema):
    # Catalog swagger.json

    
    _schedule = fields.Nested(Schedule, required=False)
    
    type = fields.Str(required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    slug = fields.Str(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    is_visible = fields.Boolean(required=False)
    
    created_by = fields.Nested(UserInfo, required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    app_id = fields.Str(required=False)
    
    published = fields.Boolean(required=False)
    
    seo = fields.Nested(SeoDetail, required=False)
    
    sort_on = fields.Str(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    _locale_language = fields.Dict(required=False)
    
    badge = fields.Nested(CollectionBadge, required=False)
    
    query = fields.Dict(required=False)
    
    banners = fields.Nested(CollectionBanner, required=False)
    
    logo = fields.Nested(CollectionImage, required=False)
    
    description = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    meta = fields.Dict(required=False)
    

