"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .ImageUrls import ImageUrls

























from .Action import Action



from .Media1 import Media1


class GetCollectionDetailNest(BaseSchema):
    # Catalog swagger.json

    
    allow_sort = fields.Boolean(required=False)
    
    _schedule = fields.Dict(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    type = fields.Str(required=False)
    
    query = fields.Dict(required=False)
    
    description = fields.Str(required=False)
    
    app_id = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    cron = fields.Dict(required=False)
    
    tag = fields.List(fields.Str(required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    name = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    badge = fields.Dict(required=False)
    
    action = fields.Nested(Action, required=False)
    
    meta = fields.Dict(required=False)
    
    logo = fields.Nested(Media1, required=False)
    

