"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ManifestPage import ManifestPage



from .ManifestDetail import ManifestDetail

from .ManifestDetailItem import ManifestDetailItem


class ManifestDetailResponse(BaseSchema):
    # Orders swagger.json

    
    page = fields.Nested(ManifestPage, required=False)
    
    additional_shipment_count = fields.Int(required=False)
    
    manifest_details = fields.List(fields.Nested(ManifestDetail, required=False), required=False)
    
    items = fields.List(fields.Nested(ManifestDetailItem, required=False), required=False)
    

