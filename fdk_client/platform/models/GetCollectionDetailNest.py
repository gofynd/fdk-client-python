"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





























from .Action import Action



from .CollectionMedia import CollectionMedia




class GetCollectionDetailNest(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    badge = fields.Dict(required=False)
    
    meta = fields.Dict(required=False)
    
    type = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    uid = fields.Str(required=False)
    
    app_id = fields.Str(required=False)
    
    cron = fields.Dict(required=False)
    
    _schedule = fields.Dict(required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    query = fields.Dict(required=False)
    
    tag = fields.List(fields.Str(required=False), required=False)
    
    action = fields.Nested(Action, required=False)
    
    description = fields.Str(required=False)
    
    media = fields.Nested(CollectionMedia, required=False)
    
    is_active = fields.Boolean(required=False)
    

