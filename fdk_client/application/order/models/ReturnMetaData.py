"""order Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema




from .ReturnMetaDataImages import ReturnMetaDataImages



class ReturnMetaData(BaseSchema):
    #  swagger.json

    
    images = fields.List(fields.Nested(ReturnMetaDataImages, required=False), required=False)
    
