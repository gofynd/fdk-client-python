"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .GetEngineData import GetEngineData


class GetEngineRequest(BaseSchema):
    # Finance swagger.json

    
    data = fields.Nested(GetEngineData, required=False)
    

