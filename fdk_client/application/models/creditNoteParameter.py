"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class creditNoteParameter(BaseSchema):
    # Order swagger.json

    
    expires_in = fields.Int(required=False)
    

