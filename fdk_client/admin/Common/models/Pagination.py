"""Common Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema








class Pagination(BaseSchema):
    #  swagger.json

    
    page_no = fields.Int(required=False)
    
    page_size = fields.Int(required=False)
    
