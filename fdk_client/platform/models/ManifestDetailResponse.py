"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ManifestDetail import ManifestDetail



from .ManifestPage import ManifestPage

from .ManifestDetailItem import ManifestDetailItem


class ManifestDetailResponse(BaseSchema):
    # Order swagger.json

    
    manifest_details = fields.List(fields.Nested(ManifestDetail, required=False), required=False)
    
    additional_shipment_count = fields.Int(required=False)
    
    page = fields.Nested(ManifestPage, required=False)
    
    items = fields.List(fields.Nested(ManifestDetailItem, required=False), required=False)
    

