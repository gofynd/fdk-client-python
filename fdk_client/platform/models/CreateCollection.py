"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .CollectionQuery import CollectionQuery

from .SeoDetail import SeoDetail

















from .CollectionBanner import CollectionBanner

from .CollectionSchedule import CollectionSchedule

from .CollectionImage import CollectionImage





from .UserInfo import UserInfo

from .UserInfo import UserInfo



from .CollectionBadge import CollectionBadge








class CreateCollection(BaseSchema):
    # Catalog swagger.json

    
    published = fields.Boolean(required=False)
    
    description = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
    seo = fields.Nested(SeoDetail, required=False)
    
    meta = fields.Dict(required=False)
    
    is_visible = fields.Boolean(required=False)
    
    priority = fields.Int(required=False)
    
    _locale_language = fields.Dict(required=False)
    
    sort_on = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    slug = fields.Str(required=False)
    
    banners = fields.Nested(CollectionBanner, required=False)
    
    _schedule = fields.Nested(CollectionSchedule, required=False)
    
    logo = fields.Nested(CollectionImage, required=False)
    
    name = fields.Str(required=False)
    
    app_id = fields.Str(required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    created_by = fields.Nested(UserInfo, required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    badge = fields.Nested(CollectionBadge, required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    

