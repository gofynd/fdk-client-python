"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .CollectionQuery1 import CollectionQuery1





from .BannerImage import BannerImage



















from .ImageUrls import ImageUrls




class CollectionCreateResponse(BaseSchema):
    # Catalog swagger.json

    
    sort_on = fields.Str(required=False)
    
    cron = fields.Dict(required=False)
    
    slug = fields.Str(required=False)
    
    tag = fields.List(fields.Str(required=False), required=False)
    
    query = fields.List(fields.Nested(CollectionQuery1, required=False), required=False)
    
    meta = fields.Dict(required=False)
    
    badge = fields.Dict(required=False)
    
    logo = fields.Nested(BannerImage, required=False)
    
    type = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    name = fields.Str(required=False)
    
    _schedule = fields.Dict(required=False)
    
    priority = fields.Int(required=False)
    
    app_id = fields.Str(required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    is_active = fields.Boolean(required=False)
    

