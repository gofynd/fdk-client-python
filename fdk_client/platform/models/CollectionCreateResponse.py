"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





















from .ImageUrls import ImageUrls



from .BannerImage import BannerImage










class CollectionCreateResponse(BaseSchema):
    # Catalog swagger.json

    
    _schedule = fields.Dict(required=False)
    
    type = fields.Str(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    app_id = fields.Str(required=False)
    
    query = fields.Dict(required=False)
    
    tag = fields.List(fields.Str(required=False), required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    badge = fields.Dict(required=False)
    
    meta = fields.Dict(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    name = fields.Str(required=False)
    
    logo = fields.Nested(BannerImage, required=False)
    
    description = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    slug = fields.Str(required=False)
    
    cron = fields.Dict(required=False)
    

