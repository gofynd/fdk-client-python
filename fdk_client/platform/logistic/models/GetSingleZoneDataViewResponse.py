"""logistic Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .GetZoneDataViewItems import GetZoneDataViewItems



class GetSingleZoneDataViewResponse(BaseSchema):
    #  swagger.json

    
    data = fields.Nested(GetZoneDataViewItems, required=False)
    
