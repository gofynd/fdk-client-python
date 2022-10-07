"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .Page import Page

from .DownloadReportItems import DownloadReportItems


class DownloadReportList(BaseSchema):
    # Finance swagger.json

    
    item_count = fields.Int(required=False)
    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(DownloadReportItems, required=False), required=False)
    

