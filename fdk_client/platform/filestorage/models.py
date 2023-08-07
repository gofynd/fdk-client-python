"""FileStorage Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




class FailedResponse(BaseSchema):
    pass


class CDN(BaseSchema):
    pass


class Upload(BaseSchema):
    pass


class StartResponse(BaseSchema):
    pass


class StartRequest(BaseSchema):
    pass


class CompleteResponse(BaseSchema):
    pass


class Opts(BaseSchema):
    pass


class CopyFileTask(BaseSchema):
    pass


class BulkUploadResponse(BaseSchema):
    pass


class Destination(BaseSchema):
    pass


class BulkRequest(BaseSchema):
    pass


class Urls(BaseSchema):
    pass


class SignUrlResponse(BaseSchema):
    pass


class SignUrlRequest(BaseSchema):
    pass


class Page(BaseSchema):
    pass


class DbRecord(BaseSchema):
    pass


class BrowseResponse(BaseSchema):
    pass


class Status(BaseSchema):
    pass


class FileSrc(BaseSchema):
    pass


class File(BaseSchema):
    pass


class BulkUploadFailFileResponseItems(BaseSchema):
    pass


class BulkUploadFailResponse(BaseSchema):
    pass





class FailedResponse(BaseSchema):
    # FileStorage swagger.json

    
    message = fields.Str(required=False)
    


class CDN(BaseSchema):
    # FileStorage swagger.json

    
    url = fields.Str(required=False)
    
    absolute_url = fields.Str(required=False)
    
    relative_url = fields.Str(required=False)
    


class Upload(BaseSchema):
    # FileStorage swagger.json

    
    expiry = fields.Int(required=False)
    
    url = fields.Str(required=False)
    


class StartResponse(BaseSchema):
    # FileStorage swagger.json

    
    file_name = fields.Str(required=False)
    
    file_path = fields.Str(required=False)
    
    content_type = fields.Str(required=False)
    
    method = fields.Str(required=False)
    
    namespace = fields.Str(required=False)
    
    operation = fields.Str(required=False)
    
    size = fields.Int(required=False)
    
    upload = fields.Nested(Upload, required=False)
    
    cdn = fields.Nested(CDN, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    


class StartRequest(BaseSchema):
    # FileStorage swagger.json

    
    file_name = fields.Str(required=False)
    
    content_type = fields.Str(required=False)
    
    size = fields.Int(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    params = fields.Dict(required=False)
    


class CompleteResponse(BaseSchema):
    # FileStorage swagger.json

    
    _id = fields.Str(required=False)
    
    file_name = fields.Str(required=False)
    
    file_path = fields.Str(required=False)
    
    content_type = fields.Str(required=False)
    
    namespace = fields.Str(required=False)
    
    operation = fields.Str(required=False)
    
    size = fields.Int(required=False)
    
    upload = fields.Nested(Upload, required=False)
    
    cdn = fields.Nested(CDN, required=False)
    
    success = fields.Boolean(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    


class Opts(BaseSchema):
    # FileStorage swagger.json

    
    attempts = fields.Int(required=False)
    
    timestamp = fields.Int(required=False)
    
    delay = fields.Int(required=False)
    


class CopyFileTask(BaseSchema):
    # FileStorage swagger.json

    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    data = fields.Nested(BulkRequest, required=False)
    
    opts = fields.Nested(Opts, required=False)
    
    progress = fields.Int(required=False)
    
    delay = fields.Int(required=False)
    
    timestamp = fields.Int(required=False)
    
    attempts_made = fields.Int(required=False)
    
    stacktrace = fields.List(fields.Str(required=False), required=False)
    
    finished_on = fields.Int(required=False)
    
    processed_on = fields.Int(required=False)
    


class BulkUploadResponse(BaseSchema):
    # FileStorage swagger.json

    
    tracking_url = fields.Str(required=False)
    
    task = fields.Nested(CopyFileTask, required=False)
    


class Destination(BaseSchema):
    # FileStorage swagger.json

    
    namespace = fields.Str(required=False)
    
    rewrite = fields.Str(required=False)
    
    basepath = fields.Str(required=False)
    


class BulkRequest(BaseSchema):
    # FileStorage swagger.json

    
    urls = fields.List(fields.Str(required=False), required=False)
    
    destination = fields.Nested(Destination, required=False)
    


class Urls(BaseSchema):
    # FileStorage swagger.json

    
    url = fields.Str(required=False)
    
    signed_url = fields.Str(required=False)
    
    expiry = fields.Int(required=False)
    


class SignUrlResponse(BaseSchema):
    # FileStorage swagger.json

    
    urls = fields.List(fields.Nested(Urls, required=False), required=False)
    


class SignUrlRequest(BaseSchema):
    # FileStorage swagger.json

    
    expiry = fields.Int(required=False)
    
    urls = fields.List(fields.Str(required=False), required=False)
    


class Page(BaseSchema):
    # FileStorage swagger.json

    
    item_total = fields.Int(required=False)
    
    next_id = fields.Str(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    has_next = fields.Boolean(required=False)
    
    current = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    size = fields.Int(required=False)
    


class DbRecord(BaseSchema):
    # FileStorage swagger.json

    
    success = fields.Boolean(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    _id = fields.Str(required=False)
    
    file_name = fields.Str(required=False)
    
    operation = fields.Str(required=False)
    
    namespace = fields.Str(required=False)
    
    content_type = fields.Str(required=False)
    
    file_path = fields.Str(required=False)
    
    upload = fields.Nested(Upload, required=False)
    
    cdn = fields.Nested(CDN, required=False)
    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    


class BrowseResponse(BaseSchema):
    # FileStorage swagger.json

    
    items = fields.List(fields.Nested(DbRecord, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class Status(BaseSchema):
    # FileStorage swagger.json

    
    total = fields.Float(required=False)
    
    failed = fields.Float(required=False)
    
    succeeded = fields.Float(required=False)
    
    result = fields.Str(required=False)
    


class FileSrc(BaseSchema):
    # FileStorage swagger.json

    
    method = fields.Str(required=False)
    
    url = fields.Str(required=False)
    
    namespace = fields.Str(required=False)
    


class File(BaseSchema):
    # FileStorage swagger.json

    
    src = fields.Nested(FileSrc, required=False)
    


class BulkUploadFailFileResponseItems(BaseSchema):
    # FileStorage swagger.json

    
    success = fields.Boolean(required=False)
    
    error = fields.Str(required=False)
    
    file = fields.Nested(File, required=False)
    
    stage = fields.Str(required=False)
    


class BulkUploadFailResponse(BaseSchema):
    # FileStorage swagger.json

    
    status = fields.Nested(Status, required=False)
    
    files = fields.List(fields.Nested(BulkUploadFailFileResponseItems, required=False), required=False)
    


