"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .CollectionQuery import CollectionQuery





from .CollectionBadge import CollectionBadge







from .UserInfo import UserInfo



from .Schedule import Schedule



from .CollectionBanner import CollectionBanner

















from .CollectionImage import CollectionImage

from .SeoDetail import SeoDetail



from .UserInfo import UserInfo


class CreateCollection(BaseSchema):
    # Catalog swagger.json

    
    description = fields.Str(required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
    priority = fields.Int(required=False)
    
    app_id = fields.Str(required=False)
    
    badge = fields.Nested(CollectionBadge, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    is_active = fields.Boolean(required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    _locale_language = fields.Dict(required=False)
    
    _schedule = fields.Nested(Schedule, required=False)
    
    name = fields.Str(required=False)
    
    banners = fields.Nested(CollectionBanner, required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    meta = fields.Dict(required=False)
    
    is_visible = fields.Boolean(required=False)
    
    slug = fields.Str(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    sort_on = fields.Str(required=False)
    
    logo = fields.Nested(CollectionImage, required=False)
    
    seo = fields.Nested(SeoDetail, required=False)
    
    published = fields.Boolean(required=False)
    
    created_by = fields.Nested(UserInfo, required=False)
    

