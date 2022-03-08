"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .CollectionBadge import CollectionBadge





from .UserInfo import UserInfo





from .CollectionMedia import CollectionMedia





from .UserInfo import UserInfo









from .Schedule import Schedule











from .SeoDetail import SeoDetail






class CreateCollection(BaseSchema):
    # Catalog swagger.json

    
    badge = fields.Nested(CollectionBadge, required=False)
    
    is_visible = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    created_by = fields.Nested(UserInfo, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    sort_on = fields.Str(required=False)
    
    media = fields.Nested(CollectionMedia, required=False)
    
    query = fields.Dict(required=False)
    
    meta = fields.Dict(required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    description = fields.Str(required=False)
    
    published = fields.Boolean(required=False)
    
    _schedule = fields.Nested(Schedule, required=False)
    
    _locale_language = fields.Dict(required=False)
    
    is_active = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    
    app_id = fields.Str(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    seo = fields.Nested(SeoDetail, required=False)
    
    slug = fields.Str(required=False)
    
    allow_facets = fields.Boolean(required=False)
    

