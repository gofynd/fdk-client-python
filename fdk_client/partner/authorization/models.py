"""Authorization Partner Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PartnerModel import BaseSchema




class ClientData(BaseSchema):
    pass


class ClientScopes(BaseSchema):
    pass


class UpdateClient(BaseSchema):
    pass


class ClientMeta(BaseSchema):
    pass


class ClientResponse(BaseSchema):
    pass


class ClientListSchema(BaseSchema):
    pass


class Page(BaseSchema):
    pass





class ClientData(BaseSchema):
    # Authorization swagger.json

    
    scopes = fields.Nested(ClientScopes, required=False)
    
    grants = fields.List(fields.Str(required=False), required=False)
    
    meta = fields.Nested(ClientMeta, required=False)
    


class ClientScopes(BaseSchema):
    # Authorization swagger.json

    
    type = fields.Str(required=False)
    
    permissions = fields.List(fields.Str(required=False), required=False)
    


class UpdateClient(BaseSchema):
    # Authorization swagger.json

    
    meta = fields.Nested(ClientMeta, required=False)
    


class ClientMeta(BaseSchema):
    # Authorization swagger.json

    
    tags = fields.List(fields.Str(required=False), required=False)
    
    name = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    


class ClientResponse(BaseSchema):
    # Authorization swagger.json

    
    company_id = fields.Float(required=False)
    
    client_id = fields.Str(required=False)
    
    secret = fields.List(fields.Str(required=False), required=False)
    
    slug = fields.Str(required=False)
    
    scopes = fields.Nested(ClientScopes, required=False)
    
    grants = fields.List(fields.Str(required=False), required=False)
    
    redirect_urls = fields.List(fields.Str(required=False), required=False)
    
    access_token_lifetime = fields.Int(required=False)
    
    refresh_token_lifetime = fields.Int(required=False)
    
    meta = fields.Nested(ClientMeta, required=False)
    
    author = fields.Dict(required=False)
    
    is_active = fields.Boolean(required=False)
    
    client_type = fields.Str(required=False)
    
    organization_id = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    modified_at = fields.Str(required=False)
    
    raw_permissions = fields.List(fields.Str(required=False), required=False)
    


class ClientListSchema(BaseSchema):
    # Authorization swagger.json

    
    items = fields.List(fields.Nested(ClientResponse, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class Page(BaseSchema):
    # Authorization swagger.json

    
    item_total = fields.Int(required=False)
    
    next_id = fields.Str(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    has_next = fields.Boolean(required=False)
    
    current = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    size = fields.Int(required=False)
    
    total = fields.Int(required=False)
    


