"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema



from .AttributeDetail import AttributeDetail


class AttributeMetadata(BaseSchema):

    
    title = fields.Str(required=False)
    
    details = fields.List(fields.Nested(AttributeDetail, required=False), required=False)
    

