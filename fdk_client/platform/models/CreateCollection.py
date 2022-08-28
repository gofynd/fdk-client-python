"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .SeoDetail import SeoDetail



from .UserInfo import UserInfo









from .CollectionBadge import CollectionBadge



from .Schedule import Schedule











from .CollectionImage import CollectionImage







from .UserInfo import UserInfo

from .CollectionQuery import CollectionQuery

from .CollectionBanner import CollectionBanner


class CreateCollection(BaseSchema):
    # Catalog swagger.json

    
    tags = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    seo = fields.Nested(SeoDetail, required=False)
    
    is_visible = fields.Boolean(required=False)
    
    created_by = fields.Nested(UserInfo, required=False)
    
    name = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    description = fields.Str(required=False)
    
    badge = fields.Nested(CollectionBadge, required=False)
    
    sort_on = fields.Str(required=False)
    
    _schedule = fields.Nested(Schedule, required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    slug = fields.Str(required=False)
    
    published = fields.Boolean(required=False)
    
    meta = fields.Dict(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    logo = fields.Nested(CollectionImage, required=False)
    
    app_id = fields.Str(required=False)
    
    _locale_language = fields.Dict(required=False)
    
    is_active = fields.Boolean(required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
    banners = fields.Nested(CollectionBanner, required=False)
    

