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


class DestinationNamespace(BaseSchema):
    pass


class CopyFiles(BaseSchema):
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


class InvoiceTypesResponse(BaseSchema):
    pass


class DummyTemplateDataItems(BaseSchema):
    pass


class Status(BaseSchema):
    pass


class FileSrc(BaseSchema):
    pass


class File(BaseSchema):
    pass


class FilesSuccess(BaseSchema):
    pass


class BulkUploadSyncMode(BaseSchema):
    pass


class BulkUploadFailResponse(BaseSchema):
    pass


class pdfRender(BaseSchema):
    pass


class pdfConfig(BaseSchema):
    pass


class PdfConfigSuccess(BaseSchema):
    pass


class PdfConfigSaveSuccess(BaseSchema):
    pass


class PdfDefaultTemplateSuccess(BaseSchema):
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
    


class DestinationNamespace(BaseSchema):
    # FileStorage swagger.json

    
    namespace = fields.Str(required=False)
    


class CopyFiles(BaseSchema):
    # FileStorage swagger.json

    
    urls = fields.List(fields.Str(required=False), required=False)
    
    destination = fields.Nested(DestinationNamespace, required=False)
    


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
    


class InvoiceTypesResponse(BaseSchema):
    # FileStorage swagger.json

    
    _id = fields.Str(required=False)
    
    pdf_type_id = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    format = fields.List(fields.Str(required=False), required=False)
    
    __v = fields.Int(required=False)
    
    visibility = fields.Boolean(required=False)
    
    schema = fields.Dict(required=False)
    


class DummyTemplateDataItems(BaseSchema):
    # FileStorage swagger.json

    
    _id = fields.Str(required=False)
    
    pdf_type_id = fields.Float(required=False)
    
    payload = fields.Dict(required=False)
    
    __v = fields.Int(required=False)
    


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
    


class FilesSuccess(BaseSchema):
    # FileStorage swagger.json

    
    success = fields.Boolean(required=False)
    
    file = fields.Nested(File, required=False)
    


class BulkUploadSyncMode(BaseSchema):
    # FileStorage swagger.json

    
    status = fields.Nested(Status, required=False)
    
    files = fields.List(fields.Nested(FilesSuccess, required=False), required=False)
    


class BulkUploadFailResponse(BaseSchema):
    # FileStorage swagger.json

    
    status = fields.Nested(Status, required=False)
    


class pdfRender(BaseSchema):
    # FileStorage swagger.json

    
    format = fields.Str(required=False)
    
    payload = fields.Dict(required=False)
    
    template = fields.Str(required=False)
    


class pdfConfig(BaseSchema):
    # FileStorage swagger.json

    
    format = fields.Str(required=False)
    
    template = fields.Str(required=False)
    
    pdf_type_id = fields.Int(required=False)
    


class PdfConfigSuccess(BaseSchema):
    # FileStorage swagger.json

    
    _id = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    application_id = fields.Str(required=False)
    
    pdf_type_id = fields.Int(required=False)
    
    format = fields.Str(required=False)
    
    template = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    


class PdfConfigSaveSuccess(BaseSchema):
    # FileStorage swagger.json

    
    _id = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    application_id = fields.Str(required=False)
    
    pdf_type_id = fields.Int(required=False)
    
    format = fields.Str(required=False)
    
    template = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    


class PdfDefaultTemplateSuccess(BaseSchema):
    # FileStorage swagger.json

    
    _id = fields.Str(required=False)
    
    pdf_type_id = fields.Int(required=False)
    
    format = fields.Str(required=False)
    
    template = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    


