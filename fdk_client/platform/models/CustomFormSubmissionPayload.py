"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .KeyValue import KeyValue


class CustomFormSubmissionPayload(BaseSchema):
    # Lead swagger.json

    
    response = fields.List(fields.Nested(KeyValue, required=False), required=False)
    

