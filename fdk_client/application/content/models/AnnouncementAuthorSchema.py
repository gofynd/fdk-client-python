"""content Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class AnnouncementAuthorSchema(BaseSchema):
    #  swagger.json

    
    created_by = fields.Str(required=False)
    
    modified_by = fields.Str(required=False)
    
