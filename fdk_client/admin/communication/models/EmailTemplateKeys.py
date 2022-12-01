"""communication Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...PlatformModel import BaseSchema










class EmailTemplateKeys(BaseSchema):
    #  swagger.json

    
    to = fields.Str(required=False)
    
    cc = fields.Str(required=False)
    
    bcc = fields.Str(required=False)
    
