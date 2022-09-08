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
    
    documents = fields.Nested(StoreDocuments, required=False)
    
    stage = fields.Str(required=False)
    
    additional_contact_details = fields.Dict(required=False)
    
    display_name = fields.Str(required=False)
    
    ewaybill_portal_details = fields.Dict(required=False)
    
    gst_credentials = fields.Nested(StoreGstCredentials, required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    product_return_config = fields.Dict(required=False)
    
    einvoice_portal_details = fields.Nested(EInvoicePortalDetails, required=False)
    
    timing = fields.List(fields.Dict(required=False), required=False)
    

