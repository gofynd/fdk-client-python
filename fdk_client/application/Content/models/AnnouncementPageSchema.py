"""Content Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ...ApplicationModel import BaseSchema








class AnnouncementPageSchema(BaseSchema):
    #  swagger.json

    
    page_slug = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
