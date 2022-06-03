"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .CollectionQuery import CollectionQuery







from .UserInfo import UserInfo









from .Schedule import Schedule







from .SeoDetail import SeoDetail





from .CollectionBanner import CollectionBanner

from .UserInfo import UserInfo



from .CollectionBadge import CollectionBadge

from .CollectionImage import CollectionImage


class CreateCollection(BaseSchema):
    # Catalog swagger.json

    
    sort_on = fields.Str(required=False)
    
    published = fields.Boolean(required=False)
    
    meta = fields.Dict(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
    priority = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    created_by = fields.Nested(UserInfo, required=False)
    
    description = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    is_visible = fields.Boolean(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    _schedule = fields.Nested(Schedule, required=False)
    
    _locale_language = fields.Dict(required=False)
    
    app_id = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    seo = fields.Nested(SeoDetail, required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    banners = fields.Nested(CollectionBanner, required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    slug = fields.Str(required=False)
    
    badge = fields.Nested(CollectionBadge, required=False)
    
    logo = fields.Nested(CollectionImage, required=False)
    

