"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .BulkInventoryPayload import BulkInventoryPayload






class BulkInventoryRequestSchemaV2(BaseSchema):
    # Catalog swagger.json

    
    payload = fields.List(fields.Nested(BulkInventoryPayload, required=False), required=False)
    
    meta = fields.Dict(required=False)
    
    company_id = fields.Int(required=False)
    

