"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .AnnouncementResponse import AnnouncementResponse


class AnnouncementsResponse(BaseSchema):
    # Order swagger.json

    
    announcements = fields.List(fields.Nested(AnnouncementResponse, required=False), required=False)
    

