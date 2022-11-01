"""User Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .UserSchema import UserSchema



from .PaginationSchema import PaginationSchema



class CustomerListResponseSchema(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(UserSchema, required=False), required=False)
    
    page = fields.Nested(PaginationSchema, required=False)
    
