"""filestorage Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema






from .Destination import Destination



from .ReqConfiguration import ReqConfiguration



class BulkRequest(BaseSchema):
    #  swagger.json

    
    urls = fields.List(fields.Str(required=False), required=False)
    
    destination = fields.Nested(Destination, required=False)
    
    configuration = fields.Nested(ReqConfiguration, required=False)
    
