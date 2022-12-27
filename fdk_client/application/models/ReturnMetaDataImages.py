"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class ReturnMetaDataImages(BaseSchema):
    # Order swagger.json

    
    url = fields.Str(required=False)
    

