"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .CollectionBanner import CollectionBanner

from .UserInfo import UserInfo





from .CollectionSchedule import CollectionSchedule



from .CollectionImage import CollectionImage



from .CollectionQuery import CollectionQuery



from .CollectionBadge import CollectionBadge



















from .SeoDetail import SeoDetail


class UpdateCollection(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    published = fields.Boolean(required=False)
    
    banners = fields.Nested(CollectionBanner, required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    is_active = fields.Boolean(required=False)
    
    meta = fields.Dict(required=False)
    
    _schedule = fields.Nested(CollectionSchedule, required=False)
    
    is_visible = fields.Boolean(required=False)
    
    logo = fields.Nested(CollectionImage, required=False)
    
    description = fields.Str(required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    badge = fields.Nested(CollectionBadge, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    slug = fields.Str(required=False)
    
    sort_on = fields.Str(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    
    _locale_language = fields.Dict(required=False)
    
    priority = fields.Int(required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    seo = fields.Nested(SeoDetail, required=False)
    

