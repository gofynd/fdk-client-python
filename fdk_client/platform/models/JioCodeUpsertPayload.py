"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .JioCodeUpsertDataSet import JioCodeUpsertDataSet


class JioCodeUpsertPayload(BaseSchema):
    # Orders swagger.json

    
    data = fields.List(fields.Nested(JioCodeUpsertDataSet, required=False), required=False)
    

