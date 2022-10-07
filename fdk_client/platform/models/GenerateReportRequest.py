"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .GenerateReportPlatform import GenerateReportPlatform


class GenerateReportRequest(BaseSchema):
    # Finance swagger.json

    
    data = fields.Nested(GenerateReportPlatform, required=False)
    

