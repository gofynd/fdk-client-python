"""user Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






class ArchiveUserSuccess(BaseSchema):
    #  swagger.json

    
    success = fields.Boolean(required=False)
    