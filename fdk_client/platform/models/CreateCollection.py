"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .UserInfo import UserInfo





from .CollectionBadge import CollectionBadge



from .CollectionBanner import CollectionBanner



from .SeoDetail import SeoDetail







from .CollectionImage import CollectionImage













from .CollectionSchedule import CollectionSchedule





from .UserInfo import UserInfo

from .CollectionQuery import CollectionQuery




class CreateCollection(BaseSchema):
    # Catalog swagger.json

    
    meta = fields.Dict(required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    slug = fields.Str(required=False)
    
    sort_on = fields.Str(required=False)
    
    badge = fields.Nested(CollectionBadge, required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    banners = fields.Nested(CollectionBanner, required=False)
    
    _locale_language = fields.Dict(required=False)
    
    seo = fields.Nested(SeoDetail, required=False)
    
    name = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    logo = fields.Nested(CollectionImage, required=False)
    
    published = fields.Boolean(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    priority = fields.Int(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    _schedule = fields.Nested(CollectionSchedule, required=False)
    
    type = fields.Str(required=False)
    
    is_visible = fields.Boolean(required=False)
    
    created_by = fields.Nested(UserInfo, required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
    app_id = fields.Str(required=False)
    

