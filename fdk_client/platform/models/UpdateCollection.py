"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .CollectionBanner import CollectionBanner





from .CollectionBadge import CollectionBadge



from .SeoDetail import SeoDetail







from .CollectionImage import CollectionImage





from .UserInfo import UserInfo













from .Schedule import Schedule




class UpdateCollection(BaseSchema):
    # Catalog swagger.json

    
    banners = fields.Nested(CollectionBanner, required=False)
    
    _locale_language = fields.Dict(required=False)
    
    is_active = fields.Boolean(required=False)
    
    badge = fields.Nested(CollectionBadge, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    seo = fields.Nested(SeoDetail, required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    description = fields.Str(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    logo = fields.Nested(CollectionImage, required=False)
    
    query = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    meta = fields.Dict(required=False)
    
    published = fields.Boolean(required=False)
    
    is_visible = fields.Boolean(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    slug = fields.Str(required=False)
    
    _schedule = fields.Nested(Schedule, required=False)
    
    sort_on = fields.Str(required=False)
    

