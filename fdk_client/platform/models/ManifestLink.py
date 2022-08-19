"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class ManifestLink(BaseSchema):
    # OrderInvoiceEngine swagger.json

    
    name = fields.Str(required=False)
    
    manifest_id = fields.Str(required=False)
    

