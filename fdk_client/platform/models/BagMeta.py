"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .B2BPODetails import B2BPODetails


class BagMeta(BaseSchema):
    # Orders swagger.json

    
    b2b_po_details = fields.Nested(B2BPODetails, required=False)
    

