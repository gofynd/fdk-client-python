"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Document import Document


class StoreDocuments(BaseSchema):
    # Orders swagger.json

    
    gst = fields.Nested(Document, required=False)
    

