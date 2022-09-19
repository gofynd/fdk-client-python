"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ApplicationItemMOQ import ApplicationItemMOQ

from .MetaFields import MetaFields




class ApplicationItemMeta(BaseSchema):
    # Catalog swagger.json

    
    moq = fields.Nested(ApplicationItemMOQ, required=False)
    
    _custom_meta = fields.List(fields.Nested(MetaFields, required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    

