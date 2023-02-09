"""logistic Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .SubtypeRequest import SubtypeRequest



class EntityListRequest(BaseSchema):
    #  swagger.json

    
    filters = fields.List(fields.Nested(SubtypeRequest, required=False), required=False)
    
