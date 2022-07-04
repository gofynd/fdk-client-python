"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .ImageUrls import ImageUrls

from .Action import Action











from .CollectionQuery import CollectionQuery







from .Media1 import Media1










class GetCollectionDetailNest(BaseSchema):
    # Catalog swagger.json

    
    _schedule = fields.Dict(required=False)
    
    cron = fields.Dict(required=False)
    
    description = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    action = fields.Nested(Action, required=False)
    
    name = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    
    badge = fields.Dict(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    is_active = fields.Boolean(required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    app_id = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    logo = fields.Nested(Media1, required=False)
    
    type = fields.Str(required=False)
    
    tag = fields.List(fields.Str(required=False), required=False)
    
    meta = fields.Dict(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    

