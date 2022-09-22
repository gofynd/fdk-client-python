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

    
    ewaybill_portal_details = fields.Dict(required=False)
    
    gst_number = fields.Str(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    documents = fields.Nested(StoreDocuments, required=False)
    
    stage = fields.Str(required=False)
    
    timing = fields.List(fields.Dict(required=False), required=False)
    
    gst_credentials = fields.Nested(StoreGstCredentials, required=False)
    
    additional_contact_details = fields.Dict(required=False)
    
    einvoice_portal_details = fields.Nested(EInvoicePortalDetails, required=False)
    
    product_return_config = fields.Dict(required=False)
    
    display_name = fields.Str(required=False)
    

