"""content Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema






from .AdminAnnouncementSchema import AdminAnnouncementSchema



class CreateAnnouncementSchema(BaseSchema):
    #  swagger.json

    
    message = fields.Str(required=False)
    
    data = fields.Nested(AdminAnnouncementSchema, required=False)
    
