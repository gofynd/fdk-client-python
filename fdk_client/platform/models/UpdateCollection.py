"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .CollectionBadge import CollectionBadge



from .UserInfo import UserInfo

from .CollectionSchedule import CollectionSchedule



from .SeoDetail import SeoDetail







from .CollectionImage import CollectionImage

from .CollectionQuery import CollectionQuery















from .CollectionBanner import CollectionBanner


class UpdateCollection(BaseSchema):
    # Catalog swagger.json

    
    _custom_json = fields.Dict(required=False)
    
    published = fields.Boolean(required=False)
    
    _locale_language = fields.Dict(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    badge = fields.Nested(CollectionBadge, required=False)
    
    slug = fields.Str(required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    _schedule = fields.Nested(CollectionSchedule, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    seo = fields.Nested(SeoDetail, required=False)
    
    sort_on = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    
    logo = fields.Nested(CollectionImage, required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
    is_visible = fields.Boolean(required=False)
    
    priority = fields.Int(required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    description = fields.Str(required=False)
    
    banners = fields.Nested(CollectionBanner, required=False)
    

