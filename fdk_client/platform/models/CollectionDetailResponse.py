"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .CollectionQuery import CollectionQuery















from .Media1 import Media1







from .ImageUrls import ImageUrls






class CollectionDetailResponse(BaseSchema):
    # Catalog swagger.json

    
    meta = fields.Dict(required=False)
    
    priority = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
    slug = fields.Str(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    description = fields.Str(required=False)
    
    app_id = fields.Str(required=False)
    
    badge = fields.Dict(required=False)
    
    is_active = fields.Boolean(required=False)
    
    logo = fields.Nested(Media1, required=False)
    
    type = fields.Str(required=False)
    
    _schedule = fields.Dict(required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    tag = fields.List(fields.Str(required=False), required=False)
    
    cron = fields.Dict(required=False)
    

