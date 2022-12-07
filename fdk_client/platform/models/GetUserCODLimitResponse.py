"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .CODdata import CODdata




class GetUserCODLimitResponse(BaseSchema):
    # Payment swagger.json

    
    user_cod_data = fields.Nested(CODdata, required=False)
    
    success = fields.Boolean(required=False)
    
