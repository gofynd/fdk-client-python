"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ManifestDetailItem import ManifestDetailItem

from .ManifestDetail import ManifestDetail

from .ManifestPage import ManifestPage




class ManifestDetailResponse(BaseSchema):
    # Order swagger.json

    
    items = fields.List(fields.Nested(ManifestDetailItem, required=False), required=False)
    
    manifest_details = fields.List(fields.Nested(ManifestDetail, required=False), required=False)
    
    page = fields.Nested(ManifestPage, required=False)
    
    additional_shipment_count = fields.Int(required=False)
    

