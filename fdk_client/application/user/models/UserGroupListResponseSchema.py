"""user Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .UserGroupResponseSchema import UserGroupResponseSchema



from .PaginationSchema import PaginationSchema



class UserGroupListResponseSchema(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(UserGroupResponseSchema, required=False), required=False)
    
    page = fields.Nested(PaginationSchema, required=False)
    
