"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

























from .CollectionMedia import CollectionMedia

from .Action import Action










class GetCollectionDetailNest(BaseSchema):
    # Catalog swagger.json

    
    slug = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    
    query = fields.Dict(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    tag = fields.List(fields.Str(required=False), required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    
    _schedule = fields.Dict(required=False)
    
    media = fields.Nested(CollectionMedia, required=False)
    
    action = fields.Nested(Action, required=False)
    
    cron = fields.Dict(required=False)
    
    badge = fields.Dict(required=False)
    
    app_id = fields.Str(required=False)
    
    description = fields.Str(required=False)
    

