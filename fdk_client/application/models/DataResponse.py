"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Error import Error



from .Meta import Meta





from .Parents import Parents




class DataResponse(BaseSchema):
    # Logistic swagger.json

    
    error = fields.Nested(Error, required=False)
    
    sub_type = fields.Str(required=False)
    
    meta = fields.Nested(Meta, required=False)
    
    uid = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    parents = fields.List(fields.Nested(Parents, required=False), required=False)
    
    name = fields.Str(required=False)
    

