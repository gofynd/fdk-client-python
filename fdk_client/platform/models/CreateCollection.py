"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .CollectionBadge import CollectionBadge

from .UserInfo import UserInfo

from .SeoDetail import SeoDetail

from .CollectionBanner import CollectionBanner







from .CollectionSchedule import CollectionSchedule



from .UserInfo import UserInfo

from .CollectionImage import CollectionImage





















from .CollectionQuery import CollectionQuery


class CreateCollection(BaseSchema):
    # Catalog swagger.json

    
    app_id = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    badge = fields.Nested(CollectionBadge, required=False)
    
    created_by = fields.Nested(UserInfo, required=False)
    
    seo = fields.Nested(SeoDetail, required=False)
    
    banners = fields.Nested(CollectionBanner, required=False)
    
    meta = fields.Dict(required=False)
    
    is_visible = fields.Boolean(required=False)
    
    sort_on = fields.Str(required=False)
    
    _schedule = fields.Nested(CollectionSchedule, required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    logo = fields.Nested(CollectionImage, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    priority = fields.Int(required=False)
    
    published = fields.Boolean(required=False)
    
    _locale_language = fields.Dict(required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    

