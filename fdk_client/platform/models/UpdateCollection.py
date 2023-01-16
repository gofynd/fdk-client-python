"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



















from .CollectionImage import CollectionImage

from .SeoDetail import SeoDetail





from .CollectionSchedule import CollectionSchedule



from .CollectionQuery import CollectionQuery

from .UserInfo import UserInfo

from .CollectionBanner import CollectionBanner





from .CollectionBadge import CollectionBadge






class UpdateCollection(BaseSchema):
    # Catalog swagger.json

    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    slug = fields.Str(required=False)
    
    published = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    _locale_language = fields.Dict(required=False)
    
    sort_on = fields.Str(required=False)
    
    is_visible = fields.Boolean(required=False)
    
    logo = fields.Nested(CollectionImage, required=False)
    
    seo = fields.Nested(SeoDetail, required=False)
    
    priority = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    _schedule = fields.Nested(CollectionSchedule, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    banners = fields.Nested(CollectionBanner, required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    meta = fields.Dict(required=False)
    
    badge = fields.Nested(CollectionBadge, required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    description = fields.Str(required=False)
    

