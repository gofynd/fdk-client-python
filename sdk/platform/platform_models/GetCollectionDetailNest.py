"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema













from .ActionPage import ActionPage











from .ImageUrls import ImageUrls







from .Media1 import Media1






class GetCollectionDetailNest(BaseSchema):

    
    _schedule = fields.Dict(required=False)
    
    description = fields.Str(required=False)
    
    cron = fields.Dict(required=False)
    
    type = fields.Str(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    badge = fields.Dict(required=False)
    
    action = fields.Nested(ActionPage, required=False)
    
    app_id = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    query = fields.Dict(required=False)
    
    meta = fields.Dict(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    tag = fields.List(fields.Str(required=False), required=False)
    
    uid = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    logo = fields.Nested(Media1, required=False)
    
    slug = fields.Str(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    

