"""configuration Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .AppStaff import AppStaff



class AppStaffResponse(BaseSchema):
    #  swagger.json

    
    staff_users = fields.List(fields.Nested(AppStaff, required=False), required=False)
    
