"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .GetReportListData import GetReportListData


class GetReportListRequest(BaseSchema):
    # Finance swagger.json

    
    data = fields.Nested(GetReportListData, required=False)
    

