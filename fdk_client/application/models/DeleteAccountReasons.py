"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class DeleteAccountReasons(BaseSchema):
    # User swagger.json

    
    reason_text = fields.Str(required=False)
    

