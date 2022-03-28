"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .SeoDetail import SeoDetail







from .CollectionMedia import CollectionMedia















from .CollectionBadge import CollectionBadge

from .Schedule import Schedule







from .UserInfo import UserInfo






class UpdateCollection(BaseSchema):
    # Catalog swagger.json

    
    seo = fields.Nested(SeoDetail, required=False)
    
    published = fields.Boolean(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    query = fields.Dict(required=False)
    
    media = fields.Nested(CollectionMedia, required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    badge = fields.Nested(CollectionBadge, required=False)
    
    _schedule = fields.Nested(Schedule, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    meta = fields.Dict(required=False)
    
    _locale_language = fields.Dict(required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    is_visible = fields.Boolean(required=False)
    
    sort_on = fields.Str(required=False)
    

