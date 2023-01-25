"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .StoreDocuments import StoreDocuments





from .StoreGstCredentials import StoreGstCredentials

from .EInvoicePortalDetails import EInvoicePortalDetails








class StoreMeta(BaseSchema):
    # Order swagger.json

    
    gst_number = fields.Str(required=False)
    
    additional_contact_details = fields.Dict(required=False)
    
    stage = fields.Str(required=False)
    
    documents = fields.Nested(StoreDocuments, required=False)
    
    display_name = fields.Str(required=False)
    
    timing = fields.List(fields.Dict(required=False), required=False)
    
    gst_credentials = fields.Nested(StoreGstCredentials, required=False)
    
    einvoice_portal_details = fields.Nested(EInvoicePortalDetails, required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    product_return_config = fields.Dict(required=False)
    
    ewaybill_portal_details = fields.Dict(required=False)
    

