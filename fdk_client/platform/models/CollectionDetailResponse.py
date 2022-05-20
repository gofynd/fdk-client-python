"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .ImageUrls import ImageUrls























from .CollectionQuery1 import CollectionQuery1

from .Media1 import Media1


class CollectionDetailResponse(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    meta = fields.Dict(required=False)
    
    badge = fields.Dict(required=False)
    
    tag = fields.List(fields.Str(required=False), required=False)
    
    description = fields.Str(required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    app_id = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    
    slug = fields.Str(required=False)
    
    cron = fields.Dict(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    _schedule = fields.Dict(required=False)
    
    query = fields.List(fields.Nested(CollectionQuery1, required=False), required=False)
    
    logo = fields.Nested(Media1, required=False)
    

