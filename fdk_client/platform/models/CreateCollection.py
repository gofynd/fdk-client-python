"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .CollectionSchedule import CollectionSchedule



from .CollectionBanner import CollectionBanner





from .UserInfo import UserInfo













from .SeoDetail import SeoDetail



from .UserInfo import UserInfo





from .CollectionQuery import CollectionQuery



from .CollectionBadge import CollectionBadge

from .CollectionImage import CollectionImage




class CreateCollection(BaseSchema):
    # Catalog swagger.json

    
    is_active = fields.Boolean(required=False)
    
    meta = fields.Dict(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    _schedule = fields.Nested(CollectionSchedule, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    banners = fields.Nested(CollectionBanner, required=False)
    
    type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    created_by = fields.Nested(UserInfo, required=False)
    
    app_id = fields.Str(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    _locale_language = fields.Dict(required=False)
    
    slug = fields.Str(required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    description = fields.Str(required=False)
    
    seo = fields.Nested(SeoDetail, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    priority = fields.Int(required=False)
    
    sort_on = fields.Str(required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
    published = fields.Boolean(required=False)
    
    badge = fields.Nested(CollectionBadge, required=False)
    
    logo = fields.Nested(CollectionImage, required=False)
    
    is_visible = fields.Boolean(required=False)
    

