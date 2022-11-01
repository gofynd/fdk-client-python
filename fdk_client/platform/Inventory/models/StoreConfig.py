"""Inventory Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema














from .ProcessConfig import ProcessConfig





class StoreConfig(BaseSchema):
    #  swagger.json

    
    job_code = fields.Str(required=False)
    
    storeid = fields.Str(required=False)
    
    store_alias = fields.Str(required=False)
    
    store_file_regex = fields.Str(required=False)
    
    store_file_name = fields.Str(required=False)
    
    process_config = fields.Nested(ProcessConfig, required=False)
    
    properties = fields.Dict(required=False)
    
