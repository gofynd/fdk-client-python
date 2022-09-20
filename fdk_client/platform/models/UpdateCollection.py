"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

















from .CollectionQuery import CollectionQuery

from .CollectionBadge import CollectionBadge







from .SeoDetail import SeoDetail









from .CollectionBanner import CollectionBanner

from .CollectionImage import CollectionImage

from .UserInfo import UserInfo



from .Schedule import Schedule


class UpdateCollection(BaseSchema):
    # Catalog swagger.json

    
    priority = fields.Int(required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    sort_on = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    is_visible = fields.Boolean(required=False)
    
    _locale_language = fields.Dict(required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
    badge = fields.Nested(CollectionBadge, required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    published = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    
    seo = fields.Nested(SeoDetail, required=False)
    
    meta = fields.Dict(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    description = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    banners = fields.Nested(CollectionBanner, required=False)
    
    logo = fields.Nested(CollectionImage, required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    is_active = fields.Boolean(required=False)
    
    _schedule = fields.Nested(Schedule, required=False)
    

