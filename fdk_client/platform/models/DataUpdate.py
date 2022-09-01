"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .DataUpdatePerEntity import DataUpdatePerEntity

from .RecursiveUpdate import RecursiveUpdate


class DataUpdate(BaseSchema):
    # Order swagger.json

    
    entity_ids = fields.Nested(DataUpdatePerEntity, required=False)
    
    recursive_updates = fields.Nested(RecursiveUpdate, required=False)
    

