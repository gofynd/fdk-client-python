"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .SeoDetail import SeoDetail













from .Schedule import Schedule









from .UserInfo import UserInfo



from .UserInfo import UserInfo

from .CollectionBadge import CollectionBadge



from .CollectionMedia import CollectionMedia




class CreateCollection(BaseSchema):
    # Catalog swagger.json

    
    meta = fields.Dict(required=False)
    
    sort_on = fields.Str(required=False)
    
    published = fields.Boolean(required=False)
    
    _locale_language = fields.Dict(required=False)
    
    seo = fields.Nested(SeoDetail, required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    description = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    query = fields.Dict(required=False)
    
    is_visible = fields.Boolean(required=False)
    
    _schedule = fields.Nested(Schedule, required=False)
    
    slug = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    app_id = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    created_by = fields.Nested(UserInfo, required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    badge = fields.Nested(CollectionBadge, required=False)
    
    name = fields.Str(required=False)
    
    media = fields.Nested(CollectionMedia, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    

