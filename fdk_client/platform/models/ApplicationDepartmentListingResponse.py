"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ApplicationDepartment import ApplicationDepartment

from .Page import Page


class ApplicationDepartmentListingResponse(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(ApplicationDepartment, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

