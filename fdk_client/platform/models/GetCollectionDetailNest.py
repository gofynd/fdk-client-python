"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .ImageUrls import ImageUrls

















from .CollectionQuery import CollectionQuery







from .Action import Action







from .Media1 import Media1


class GetCollectionDetailNest(BaseSchema):
    # Catalog swagger.json

    
    badge = fields.Dict(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    cron = fields.Dict(required=False)
    
    _schedule = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    
    slug = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    type = fields.Str(required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
    uid = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    app_id = fields.Str(required=False)
    
    action = fields.Nested(Action, required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    tag = fields.List(fields.Str(required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    logo = fields.Nested(Media1, required=False)
    

