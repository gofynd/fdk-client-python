"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .RecursiveUpdate import RecursiveUpdate

from .DataUpdatePerEntity import DataUpdatePerEntity


class DataUpdate(BaseSchema):
    # Order swagger.json

    
    recursive_updates = fields.Nested(RecursiveUpdate, required=False)
    
    entity_ids = fields.Nested(DataUpdatePerEntity, required=False)
    

