"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema
















from .Action import Action





















from .Media1 import Media1





from .CollectionQuery import CollectionQuery



from .ImageUrls import ImageUrls



class GetCollectionDetailNest(BaseSchema):
    #  swagger.json

    
    meta = fields.Dict(required=False)
    
    uid = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    
    badge = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    action = fields.Nested(Action, required=False)
    
    app_id = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    tag = fields.List(fields.Str(required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    _schedule = fields.Dict(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    description = fields.Str(required=False)
    
    logo = fields.Nested(Media1, required=False)
    
    cron = fields.Dict(required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    