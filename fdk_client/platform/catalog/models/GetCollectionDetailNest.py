"""catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .Action import Action



from .Media1 import Media1











from .ImageUrls import ImageUrls

















from .CollectionQuery import CollectionQuery













class GetCollectionDetailNest(BaseSchema):
    #  swagger.json

    
    action = fields.Nested(Action, required=False)
    
    logo = fields.Nested(Media1, required=False)
    
    _schedule = fields.Dict(required=False)
    
    is_active = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    tag = fields.List(fields.Str(required=False), required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    meta = fields.Dict(required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    slug = fields.Str(required=False)
    
    app_id = fields.Str(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    cron = fields.Dict(required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
    uid = fields.Str(required=False)
    
    badge = fields.Dict(required=False)
    
    priority = fields.Int(required=False)
    
    description = fields.Str(required=False)
    
    type = fields.Str(required=False)
    