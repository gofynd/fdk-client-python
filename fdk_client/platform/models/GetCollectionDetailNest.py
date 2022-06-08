"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .Action import Action

from .ImageUrls import ImageUrls





from .Media1 import Media1











from .CollectionQuery1 import CollectionQuery1
















class GetCollectionDetailNest(BaseSchema):
    # Catalog swagger.json

    
    cron = fields.Dict(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    action = fields.Nested(Action, required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    meta = fields.Dict(required=False)
    
    _schedule = fields.Dict(required=False)
    
    logo = fields.Nested(Media1, required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    description = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    priority = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    query = fields.List(fields.Nested(CollectionQuery1, required=False), required=False)
    
    uid = fields.Str(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    badge = fields.Dict(required=False)
    
    slug = fields.Str(required=False)
    
    app_id = fields.Str(required=False)
    
    tag = fields.List(fields.Str(required=False), required=False)
    
    name = fields.Str(required=False)
    

