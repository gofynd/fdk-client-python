"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .PostHistoryFilters import PostHistoryFilters



from .PostHistoryData import PostHistoryData



class PostActivityHistory(BaseSchema):
    #  swagger.json

    
    filters = fields.List(fields.Nested(PostHistoryFilters, required=False), required=False)
    
    data = fields.Nested(PostHistoryData, required=False)
    
