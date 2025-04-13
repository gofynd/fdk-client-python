"""FileStorage Partner Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PartnerModel import BaseSchema




class SizeConstraints(BaseSchema):
    pass


class SaveProxy(BaseSchema):
    pass


class ProxyFileData(BaseSchema):
    pass


class ProxyFile(BaseSchema):
    pass


class FetchProxyDetails(BaseSchema):
    pass


class NamespaceDetails(BaseSchema):
    pass


class AllNamespaceDetails(BaseSchema):
    pass


class CDN(BaseSchema):
    pass


class Upload(BaseSchema):
    pass


class FileUpload(BaseSchema):
    pass


class FileUploadStart(BaseSchema):
    pass


class CreatedBy(BaseSchema):
    pass


class FileUploadComplete(BaseSchema):
    pass


class FailedBrowseFilesResult(BaseSchema):
    pass





class SizeConstraints(BaseSchema):
    # FileStorage swagger.json

    
    max = fields.Int(required=False)
    


class SaveProxy(BaseSchema):
    # FileStorage swagger.json

    
    id = fields.Int(required=False)
    
    token = fields.Str(required=False)
    


class ProxyFileData(BaseSchema):
    # FileStorage swagger.json

    
    email = fields.Str(required=False)
    
    password = fields.Str(required=False)
    


class ProxyFile(BaseSchema):
    # FileStorage swagger.json

    
    id = fields.Int(required=False)
    
    customer = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    price = fields.Float(required=False)
    
    data = fields.Nested(ProxyFileData, required=False)
    
    url = fields.Str(required=False)
    


class FetchProxyDetails(BaseSchema):
    # FileStorage swagger.json

    
    data = fields.Dict(required=False)
    
    support = fields.Dict(required=False)
    


class NamespaceDetails(BaseSchema):
    # FileStorage swagger.json

    
    namespace = fields.Str(required=False)
    
    valid_content_types = fields.List(fields.Str(required=False), required=False)
    
    size = fields.Nested(SizeConstraints, required=False)
    
    file_acl = fields.Str(required=False)
    


class AllNamespaceDetails(BaseSchema):
    # FileStorage swagger.json

    
    items = fields.List(fields.Nested(NamespaceDetails, required=False), required=False)
    


class CDN(BaseSchema):
    # FileStorage swagger.json

    
    url = fields.Str(required=False)
    
    absolute_url = fields.Str(required=False)
    
    relative_url = fields.Str(required=False)
    


class Upload(BaseSchema):
    # FileStorage swagger.json

    
    expiry = fields.Int(required=False)
    
    url = fields.Str(required=False)
    


class FileUpload(BaseSchema):
    # FileStorage swagger.json

    
    file_name = fields.Str(required=False)
    
    file_path = fields.Str(required=False)
    
    content_type = fields.Str(required=False)
    
    method = fields.Str(required=False)
    
    namespace = fields.Str(required=False)
    
    operation = fields.Str(required=False)
    
    size = fields.Int(required=False)
    
    upload = fields.Nested(Upload, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    


class FileUploadStart(BaseSchema):
    # FileStorage swagger.json

    
    file_name = fields.Str(required=False)
    
    content_type = fields.Str(required=False)
    
    size = fields.Int(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    params = fields.Dict(required=False)
    


class CreatedBy(BaseSchema):
    # FileStorage swagger.json

    
    username = fields.Str(required=False)
    


class FileUploadComplete(BaseSchema):
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
    
    created_by = fields.Nested(CreatedBy, required=False)
    


class FailedBrowseFilesResult(BaseSchema):
    # FileStorage swagger.json

    
    message = fields.Str(required=False)
    


