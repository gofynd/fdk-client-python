"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .StatisticsData import StatisticsData




class EdcDeviceStatsResponse(BaseSchema):
    # Payment swagger.json

    
    statistics = fields.Nested(StatisticsData, required=False)
    
    success = fields.Boolean(required=False)
    

