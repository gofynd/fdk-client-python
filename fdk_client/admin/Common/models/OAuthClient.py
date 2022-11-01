"""Common Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .Scopes import Scopes

















from .Meta import Meta



from .Author import Author













class OAuthClient(BaseSchema):
    #  swagger.json

    
    id = fields.Str(required=False)
    
    scopes = fields.Nested(Scopes, required=False)
    
    secret = fields.List(fields.Str(required=False), required=False)
    
    grants = fields.List(fields.Str(required=False), required=False)
    
    redirect_urls = fields.List(fields.Str(required=False), required=False)
    
    access_token_lifetime = fields.Float(required=False)
    
    refresh_token_lifetime = fields.Float(required=False)
    
    is_active = fields.Boolean(required=False)
    
    client_type = fields.Str(required=False)
    
    meta = fields.Nested(Meta, required=False)
    
    author = fields.Nested(Author, required=False)
    
    client_id = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    modified_at = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    __v = fields.Float(required=False)
    
