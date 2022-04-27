"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .Schedule import Schedule

from .CollectionBanner import CollectionBanner





from .SeoDetail import SeoDetail











from .UserInfo import UserInfo





from .CollectionBadge import CollectionBadge



from .CollectionImage import CollectionImage




class UpdateCollection(BaseSchema):
    # Catalog swagger.json

    
    _custom_json = fields.Dict(required=False)
    
    is_visible = fields.Boolean(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    published = fields.Boolean(required=False)
    
    _schedule = fields.Nested(Schedule, required=False)
    
    banners = fields.Nested(CollectionBanner, required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    query = fields.Dict(required=False)
    
    seo = fields.Nested(SeoDetail, required=False)
    
    slug = fields.Str(required=False)
    
    sort_on = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    description = fields.Str(required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    name = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    badge = fields.Nested(CollectionBadge, required=False)
    
    _locale_language = fields.Dict(required=False)
    
    logo = fields.Nested(CollectionImage, required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    

