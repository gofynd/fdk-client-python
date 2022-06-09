"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .CollectionBanner import CollectionBanner













from .CollectionBadge import CollectionBadge

from .CollectionImage import CollectionImage











from .UserInfo import UserInfo







from .Schedule import Schedule

from .CollectionQuery1 import CollectionQuery1

from .UserInfo import UserInfo

from .SeoDetail import SeoDetail




class CreateCollection(BaseSchema):
    # Catalog swagger.json

    
    slug = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    banners = fields.Nested(CollectionBanner, required=False)
    
    published = fields.Boolean(required=False)
    
    _locale_language = fields.Dict(required=False)
    
    is_visible = fields.Boolean(required=False)
    
    priority = fields.Int(required=False)
    
    app_id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    badge = fields.Nested(CollectionBadge, required=False)
    
    logo = fields.Nested(CollectionImage, required=False)
    
    is_active = fields.Boolean(required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    description = fields.Str(required=False)
    
    created_by = fields.Nested(UserInfo, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    meta = fields.Dict(required=False)
    
    type = fields.Str(required=False)
    
    _schedule = fields.Nested(Schedule, required=False)
    
    query = fields.List(fields.Nested(CollectionQuery1, required=False), required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    seo = fields.Nested(SeoDetail, required=False)
    
    sort_on = fields.Str(required=False)
    

