"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema



from .Destination import Destination

from .ReqConfiguration import ReqConfiguration


class BulkRequest(BaseSchema):
    # FileStorage swagger.json

    
    urls = fields.List(fields.Str(required=False), required=False)
    
    destination = fields.Nested(Destination, required=False)
    
    configuration = fields.Nested(ReqConfiguration, required=False)
    

