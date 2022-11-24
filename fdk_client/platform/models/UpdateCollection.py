"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .CollectionBanner import CollectionBanner

from .UserInfo import UserInfo

from .CollectionSchedule import CollectionSchedule

from .CollectionImage import CollectionImage



from .CollectionBadge import CollectionBadge







from .CollectionQuery import CollectionQuery















from .SeoDetail import SeoDetail












class UpdateCollection(BaseSchema):
    # Catalog swagger.json

    
    banners = fields.Nested(CollectionBanner, required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    _schedule = fields.Nested(CollectionSchedule, required=False)
    
    logo = fields.Nested(CollectionImage, required=False)
    
    is_visible = fields.Boolean(required=False)
    
    badge = fields.Nested(CollectionBadge, required=False)
    
    name = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
    type = fields.Str(required=False)
    
    published = fields.Boolean(required=False)
    
    description = fields.Str(required=False)
    
    _locale_language = fields.Dict(required=False)
    
    sort_on = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    seo = fields.Nested(SeoDetail, required=False)
    
    slug = fields.Str(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    priority = fields.Int(required=False)
    

