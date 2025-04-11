"""Discount Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




class ValidityObject(BaseSchema):
    pass


class CreateUpdateDiscount(BaseSchema):
    pass


class DiscountMeta(BaseSchema):
    pass


class DiscountJob(BaseSchema):
    pass


class FileJobBody(BaseSchema):
    pass


class ListOrCalender(BaseSchema):
    pass


class DiscountItems(BaseSchema):
    pass


class BulkDiscount(BaseSchema):
    pass


class FileJobResponseSchema(BaseSchema):
    pass


class FileJobRequestSchema(BaseSchema):
    pass


class DownloadFileJob(BaseSchema):
    pass


class CancelJobResponseSchema(BaseSchema):
    pass


class Page(BaseSchema):
    pass


class UserDetails(BaseSchema):
    pass


class BadRequestObject(BaseSchema):
    pass


class BadRequestData(BaseSchema):
    pass


class BadRequestObjectGet(BaseSchema):
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
    
    app_id = fields.Str(required=False)
    
    job_type = fields.Str(required=False)
    
    discount_type = fields.Str(required=False)
    
    discount_level = fields.Str(required=False)
    
    value = fields.Int(required=False)
    
    file_path = fields.Str(required=False)
    
    brand_ids = fields.List(fields.Int(required=False), required=False)
    
    store_ids = fields.List(fields.Int(required=False), required=False)
    
    factory_type_ids = fields.List(fields.Str(required=False), required=False)
    
    validity = fields.Nested(ValidityObject, required=False)
    
    discount_meta = fields.Nested(DiscountMeta, required=False)
    


class DiscountMeta(BaseSchema):
    # Discount swagger.json

    
    timer = fields.Boolean(required=False)
    
    hours = fields.Float(required=False)
    
    minutes = fields.Float(required=False)
    


class DiscountJob(BaseSchema):
    # Discount swagger.json

    
    _id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    app_id = fields.Str(required=False)
    
    job_type = fields.Str(required=False)
    
    discount_type = fields.Str(required=False)
    
    discount_level = fields.Str(required=False)
    
    value = fields.Int(required=False)
    
    file_path = fields.Str(required=False)
    
    brand_ids = fields.List(fields.Int(required=False), required=False)
    
    store_ids = fields.List(fields.Int(required=False), required=False)
    
    factory_type_ids = fields.List(fields.Str(required=False), required=False)
    
    discount_meta = fields.Nested(DiscountMeta, required=False)
    
    validity = fields.Nested(ValidityObject, required=False)
    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    created_by = fields.Nested(UserDetails, required=False)
    
    modified_by = fields.Nested(UserDetails, required=False)
    
    meta = fields.Dict(required=False)
    


class FileJobBody(BaseSchema):
    # Discount swagger.json

    
    name = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    app_id = fields.Str(required=False)
    
    job_type = fields.Str(required=False)
    
    discount_type = fields.Str(required=False)
    
    discount_level = fields.Str(required=False)
    
    value = fields.Int(required=False)
    
    file_path = fields.Str(required=False)
    
    brand_ids = fields.List(fields.Int(required=False), required=False)
    
    store_ids = fields.List(fields.Int(required=False), required=False)
    
    factory_type_ids = fields.List(fields.Str(required=False), required=False)
    
    discount_meta = fields.Nested(DiscountMeta, required=False)
    
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
    


class DiscountItems(BaseSchema):
    # Discount swagger.json

    
    item_code = fields.Str(required=False)
    
    brand_name = fields.Str(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    store_code = fields.Str(required=False)
    
    price_zone = fields.Str(required=False)
    
    discount_type = fields.Str(required=False)
    
    value = fields.Float(required=False)
    
    discount_meta = fields.Nested(DiscountMeta, required=False)
    


class BulkDiscount(BaseSchema):
    # Discount swagger.json

    
    company_id = fields.Int(required=False)
    
    items = fields.List(fields.Nested(DiscountItems, required=False), required=False)
    


class FileJobResponseSchema(BaseSchema):
    # Discount swagger.json

    
    stage = fields.Str(required=False)
    
    total = fields.Int(required=False)
    
    failed = fields.Int(required=False)
    
    company_id = fields.Int(required=False)
    
    body = fields.Nested(FileJobBody, required=False)
    
    type = fields.Str(required=False)
    
    file_type = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    file_path = fields.Str(required=False)
    
    progress = fields.Int(required=False)
    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    created_by = fields.Nested(UserDetails, required=False)
    


class FileJobRequestSchema(BaseSchema):
    # Discount swagger.json

    
    name = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    company_id = fields.Int(required=False)
    
    app_id = fields.Str(required=False)
    
    job_type = fields.Str(required=False)
    
    discount_type = fields.Str(required=False)
    
    discount_level = fields.Str(required=False)
    
    file_path = fields.Str(required=False)
    
    brand_ids = fields.List(fields.Int(required=False), required=False)
    
    store_ids = fields.List(fields.Int(required=False), required=False)
    
    validity = fields.Nested(ValidityObject, required=False)
    
    meta = fields.Dict(required=False)
    


class DownloadFileJob(BaseSchema):
    # Discount swagger.json

    
    app_id = fields.Str(required=False)
    


class CancelJobResponseSchema(BaseSchema):
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
    
    total = fields.Int(required=False)
    


class UserDetails(BaseSchema):
    # Discount swagger.json

    
    username = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    


class BadRequestObject(BaseSchema):
    # Discount swagger.json

    
    message = fields.Str(required=False)
    


class BadRequestData(BaseSchema):
    # Discount swagger.json

    
    message = fields.Str(required=False)
    


class BadRequestObjectGet(BaseSchema):
    # Discount swagger.json

    
    message = fields.Str(required=False)
    
    error = fields.Str(required=False)
    
    data = fields.Nested(BadRequestData, required=False)
    


