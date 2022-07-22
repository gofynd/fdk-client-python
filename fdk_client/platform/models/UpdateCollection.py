"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .CollectionBadge import CollectionBadge



from .UserInfo import UserInfo



from .SeoDetail import SeoDetail

from .CollectionQuery import CollectionQuery





from .CollectionImage import CollectionImage













from .CollectionBanner import CollectionBanner

from .Schedule import Schedule










class UpdateCollection(BaseSchema):
    # Catalog swagger.json

    
    meta = fields.Dict(required=False)
    
    badge = fields.Nested(CollectionBadge, required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    published = fields.Boolean(required=False)
    
    seo = fields.Nested(SeoDetail, required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
    _locale_language = fields.Dict(required=False)
    
    sort_on = fields.Str(required=False)
    
    logo = fields.Nested(CollectionImage, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    is_active = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    banners = fields.Nested(CollectionBanner, required=False)
    
    _schedule = fields.Nested(Schedule, required=False)
    
    description = fields.Str(required=False)
    
    is_visible = fields.Boolean(required=False)
    
    slug = fields.Str(required=False)
    
    allow_facets = fields.Boolean(required=False)
    

