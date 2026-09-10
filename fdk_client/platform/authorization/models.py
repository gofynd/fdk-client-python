"""Authorization Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




class Page(BaseSchema):
    pass


class StandardError(BaseSchema):
    pass


class ValidationErrors(BaseSchema):
    pass


class ApplicationStaff(BaseSchema):
    pass


class ApplicationStaffPage(BaseSchema):
    pass


class ValidationError(BaseSchema):
    pass





class Page(BaseSchema):
    # Authorization swagger.json

    
    item_total = fields.Int(required=False)
    
    next_id = fields.Str(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    has_next = fields.Boolean(required=False)
    
    current = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    size = fields.Int(required=False)
    
    page_size = fields.Int(required=False)
    


class StandardError(BaseSchema):
    # Authorization swagger.json

    
    message = fields.Str(required=False)
    


class ValidationErrors(BaseSchema):
    # Authorization swagger.json

    
    errors = fields.List(fields.Nested(ValidationError, required=False), required=False)
    


class ApplicationStaff(BaseSchema):
    # Authorization swagger.json

    
    application = fields.Str(required=False)
    
    user = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    order_incent = fields.Boolean(required=False)
    
    stores = fields.List(fields.Int(required=False), required=False)
    
    employee_code = fields.Str(required=False)
    
    first_name = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    
    profile_pic_url = fields.Str(required=False)
    


class ApplicationStaffPage(BaseSchema):
    # Authorization swagger.json

    
    items = fields.List(fields.Nested(ApplicationStaff, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class ValidationError(BaseSchema):
    # Authorization swagger.json

    
    message = fields.Str(required=False)
    
    field = fields.Str(required=False)
    


