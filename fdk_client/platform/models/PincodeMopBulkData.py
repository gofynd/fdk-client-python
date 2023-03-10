"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class PincodeMopBulkData(BaseSchema):
    # Serviceability swagger.json

    
    batch_id = fields.Str(required=False)
    
    s3_url = fields.Str(required=False)
    

