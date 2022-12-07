"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class CloseVideoRoomResponse(BaseSchema):
    # Lead swagger.json

    
    success = fields.Boolean(required=False)
    
