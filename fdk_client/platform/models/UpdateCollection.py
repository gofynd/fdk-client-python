"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .SeoDetail import SeoDetail

from .CollectionSchedule import CollectionSchedule





from .CollectionBadge import CollectionBadge









from .CollectionImage import CollectionImage



from .CollectionBanner import CollectionBanner

from .UserInfo import UserInfo













from .CollectionQuery import CollectionQuery


class UpdateCollection(BaseSchema):
    # Catalog swagger.json

    
    sort_on = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    is_visible = fields.Boolean(required=False)
    
    seo = fields.Nested(SeoDetail, required=False)
    
    _schedule = fields.Nested(CollectionSchedule, required=False)
    
    name = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    
    badge = fields.Nested(CollectionBadge, required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    slug = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    logo = fields.Nested(CollectionImage, required=False)
    
    is_active = fields.Boolean(required=False)
    
    banners = fields.Nested(CollectionBanner, required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    type = fields.Str(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    _locale_language = fields.Dict(required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    published = fields.Boolean(required=False)
    
    meta = fields.Dict(required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    

