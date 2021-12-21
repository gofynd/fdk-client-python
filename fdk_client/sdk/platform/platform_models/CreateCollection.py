"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema







from .UserInfo import UserInfo

from .CollectionBadge import CollectionBadge









from .SeoDetail import SeoDetail



from .UserInfo import UserInfo

from .CollectionImage import CollectionImage









from .CollectionBanner import CollectionBanner









from .Schedule import Schedule




class CreateCollection(BaseSchema):
    # Catalog swagger.json

    
    meta = fields.Dict(required=False)
    
    description = fields.Str(required=False)
    
    is_visible = fields.Boolean(required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    badge = fields.Nested(CollectionBadge, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    seo = fields.Nested(SeoDetail, required=False)
    
    sort_on = fields.Str(required=False)
    
    created_by = fields.Nested(UserInfo, required=False)
    
    logo = fields.Nested(CollectionImage, required=False)
    
    published = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    
    _locale_language = fields.Dict(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    banners = fields.Nested(CollectionBanner, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    query = fields.Dict(required=False)
    
    app_id = fields.Str(required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    _schedule = fields.Nested(Schedule, required=False)
    
    is_active = fields.Boolean(required=False)
    

