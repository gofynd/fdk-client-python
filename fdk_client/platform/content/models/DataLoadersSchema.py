"""content Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema




from .DataLoaderSchema import DataLoaderSchema



class DataLoadersSchema(BaseSchema):
    #  swagger.json

    
    items = fields.List(fields.Nested(DataLoaderSchema, required=False), required=False)
    
