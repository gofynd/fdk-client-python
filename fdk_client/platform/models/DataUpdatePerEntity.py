"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class DataUpdatePerEntity(BaseSchema):
    # Order swagger.json

    
    entity_id = fields.Dict(required=False)
    

