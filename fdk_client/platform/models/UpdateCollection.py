"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .CollectionSchedule import CollectionSchedule











from .SeoDetail import SeoDetail





from .CollectionBadge import CollectionBadge

from .CollectionQuery import CollectionQuery



from .CollectionBanner import CollectionBanner













from .CollectionImage import CollectionImage



from .UserInfo import UserInfo




class UpdateCollection(BaseSchema):
    # Catalog swagger.json

    
    _schedule = fields.Nested(CollectionSchedule, required=False)
    
    name = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    sort_on = fields.Str(required=False)
    
    published = fields.Boolean(required=False)
    
    seo = fields.Nested(SeoDetail, required=False)
    
    description = fields.Str(required=False)
    
    _locale_language = fields.Dict(required=False)
    
    badge = fields.Nested(CollectionBadge, required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    banners = fields.Nested(CollectionBanner, required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    slug = fields.Str(required=False)
    
    is_visible = fields.Boolean(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    meta = fields.Dict(required=False)
    
    logo = fields.Nested(CollectionImage, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    

