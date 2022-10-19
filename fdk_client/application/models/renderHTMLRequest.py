"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class renderHTMLRequest(BaseSchema):
    # Payment swagger.json

    
    base64_html = fields.Str(required=False)
    

