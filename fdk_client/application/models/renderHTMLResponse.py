"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class renderHTMLResponse(BaseSchema):
    # Payment swagger.json

    
    html = fields.Str(required=False)
    
    status = fields.Boolean(required=False)
    

