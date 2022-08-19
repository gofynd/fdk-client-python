"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Document import Document

from .Document import Document

from .Document import Document

from .Document import Document


class Documents1(BaseSchema):
    # Order swagger.json

    
    digital_signature = fields.Nested(Document, required=False)
    
    cin = fields.Nested(Document, required=False)
    
    gst = fields.Nested(Document, required=False)
    
    pan = fields.Nested(Document, required=False)
    

