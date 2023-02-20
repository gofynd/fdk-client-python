"""order Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .PostHistoryData import PostHistoryData



from .PostHistoryFilters import PostHistoryFilters



class PostActivityHistory(BaseSchema):
    #  swagger.json

    
    data = fields.Nested(PostHistoryData, required=False)
    
    filters = fields.List(fields.Nested(PostHistoryFilters, required=False), required=False)
    
