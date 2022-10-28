"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .Schedule import Schedule



from .CollectionQuery import CollectionQuery







from .CollectionImage import CollectionImage

from .SeoDetail import SeoDetail



from .UserInfo import UserInfo









from .CollectionBanner import CollectionBanner





from .CollectionBadge import CollectionBadge





from .UserInfo import UserInfo






class CreateCollection(BaseSchema):
    # Catalog swagger.json

    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    name = fields.Str(required=False)
    
    _schedule = fields.Nested(Schedule, required=False)
    
    priority = fields.Int(required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
    slug = fields.Str(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    meta = fields.Dict(required=False)
    
    logo = fields.Nested(CollectionImage, required=False)
    
    seo = fields.Nested(SeoDetail, required=False)
    
    sort_on = fields.Str(required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    _locale_language = fields.Dict(required=False)
    
    description = fields.Str(required=False)
    
    is_visible = fields.Boolean(required=False)
    
    banners = fields.Nested(CollectionBanner, required=False)
    
    is_active = fields.Boolean(required=False)
    
    app_id = fields.Str(required=False)
    
    badge = fields.Nested(CollectionBadge, required=False)
    
    type = fields.Str(required=False)
    
    published = fields.Boolean(required=False)
    
    created_by = fields.Nested(UserInfo, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    allow_sort = fields.Boolean(required=False)
    

