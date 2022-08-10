"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





























from .ImageUrls import ImageUrls



from .Media1 import Media1


class CollectionDetailResponse(BaseSchema):
    # Catalog swagger.json

    
    description = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    is_active = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    tag = fields.List(fields.Str(required=False), required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    badge = fields.Dict(required=False)
    
    slug = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    query = fields.Dict(required=False)
    
    _schedule = fields.Dict(required=False)
    
    app_id = fields.Str(required=False)
    
    cron = fields.Dict(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    logo = fields.Nested(Media1, required=False)
    

