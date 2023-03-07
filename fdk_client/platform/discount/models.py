"""Discount Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ..PlatformModel import BaseSchema





class ValidityObject(BaseSchema):
    pass


class CreateUpdateDiscount(BaseSchema):
    pass


class DiscountJob(BaseSchema):
    pass


class ListOrCalender(BaseSchema):
    pass


class FileJobResponse(BaseSchema):
    pass


class DownloadFileJob(BaseSchema):
    pass


class CancelJobResponse(BaseSchema):
    pass


class Page(BaseSchema):
    pass


class UserDetails(BaseSchema):
    pass


class BadRequestObject(BaseSchema):
    pass





class ValidityObject(BaseSchema):
    # Discount swagger.json

    
    start = fields.Str(required=False)
    
    end = fields.Str(required=False)
    


class CreateUpdateDiscount(BaseSchema):
    # Discount swagger.json

    
    name = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    app_ids = fields.List(fields.Str(required=False), required=False)
    
    extension_ids = fields.List(fields.Str(required=False), required=False)
    
    job_type = fields.Str(required=False)
    
    discount_type = fields.Str(required=False)
    
    discount_level = fields.Str(required=False)
    
    value = fields.Int(required=False)
    
    file_path = fields.Str(required=False)
    
    brand_ids = fields.List(fields.Int(required=False), required=False)
    
    store_ids = fields.List(fields.Int(required=False), required=False)
    
    validity = fields.Nested(ValidityObject, required=False)
    


class DiscountJob(BaseSchema):
    # Discount swagger.json

    
    _id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    app_ids = fields.List(fields.Str(required=False), required=False)
    
    job_type = fields.Str(required=False)
    
    discount_type = fields.Str(required=False)
    
    discount_level = fields.Str(required=False)
    
    value = fields.Int(required=False)
    
    file_path = fields.Str(required=False)
    
    brand_ids = fields.List(fields.Int(required=False), required=False)
    
    store_ids = fields.List(fields.Int(required=False), required=False)
    
    validity = fields.Nested(ValidityObject, required=False)
    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    created_by = fields.Nested(UserDetails, required=False)
    
    modified_by = fields.Nested(UserDetails, required=False)
    
    meta = fields.Dict(required=False)
    


class ListOrCalender(BaseSchema):
    # Discount swagger.json

    
    items = fields.List(fields.Nested(DiscountJob, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class FileJobResponse(BaseSchema):
    # Discount swagger.json

    
    stage = fields.Str(required=False)
    
    total = fields.Int(required=False)
    
    failed = fields.Int(required=False)
    
    company_id = fields.Int(required=False)
    
    body = fields.Dict(required=False)
    
    type = fields.Str(required=False)
    
    file_type = fields.Str(required=False)
    


class DownloadFileJob(BaseSchema):
    # Discount swagger.json

    
    brand_ids = fields.List(fields.Int(required=False), required=False)
    
    store_ids = fields.List(fields.Int(required=False), required=False)
    


class CancelJobResponse(BaseSchema):
    # Discount swagger.json

    
    success = fields.Boolean(required=False)
    


class Page(BaseSchema):
    # Discount swagger.json

    
    item_total = fields.Int(required=False)
    
    next_id = fields.Str(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    has_next = fields.Boolean(required=False)
    
    current = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    size = fields.Int(required=False)
    


class UserDetails(BaseSchema):
    # Discount swagger.json

    
    username = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    


class BadRequestObject(BaseSchema):
    # Discount swagger.json

    
    message = fields.Str(required=False)
    


