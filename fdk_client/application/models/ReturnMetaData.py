"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ReturnMetaDataImages import ReturnMetaDataImages


class ReturnMetaData(BaseSchema):
    # Order swagger.json

    
    images = fields.List(fields.Nested(ReturnMetaDataImages, required=False), required=False)
    

