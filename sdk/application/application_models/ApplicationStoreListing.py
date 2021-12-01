"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .AppStore import AppStore

from .StoreDepartments import StoreDepartments

from .Page import Page


class ApplicationStoreListing(BaseSchema):

    
    items = fields.List(fields.Nested(AppStore, required=False), required=False)
    
    filters = fields.List(fields.Nested(StoreDepartments, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

