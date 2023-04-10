"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .MetaFields import MetaFields

from .ApplicationItemSEO import ApplicationItemSEO





from .ApplicationItemMOQ import ApplicationItemMOQ


class ApplicationItemMeta(BaseSchema):
    # Catalog swagger.json

    
    _custom_json = fields.Dict(required=False)
    
    alt_text = fields.Dict(required=False)
    
    _custom_meta = fields.List(fields.Nested(MetaFields, required=False), required=False)
    
    seo = fields.Nested(ApplicationItemSEO, required=False)
    
    is_cod = fields.Boolean(required=False)
    
    is_gift = fields.Boolean(required=False)
    
    moq = fields.Nested(ApplicationItemMOQ, required=False)
    

