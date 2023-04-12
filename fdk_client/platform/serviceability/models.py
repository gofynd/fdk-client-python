"""Serviceability Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




class ApplicationServiceabilityConfig(BaseSchema):
    pass


class ServiceabilityrErrorResponse(BaseSchema):
    pass


class ApplicationServiceabilityConfigResponse(BaseSchema):
    pass


class EntityRegionView_Request(BaseSchema):
    pass


class EntityRegionView_page(BaseSchema):
    pass


class EntityRegionView_Items(BaseSchema):
    pass


class EntityRegionView_Error(BaseSchema):
    pass


class EntityRegionView_Response(BaseSchema):
    pass


class ZoneDataItem(BaseSchema):
    pass


class ListViewProduct(BaseSchema):
    pass


class ListViewChannels(BaseSchema):
    pass


class ListViewItems(BaseSchema):
    pass


class ListViewSummary(BaseSchema):
    pass


class ListViewResponse(BaseSchema):
    pass


class CompanyStoreView_PageItems(BaseSchema):
    pass


class CompanyStoreView_Response(BaseSchema):
    pass


class GetZoneDataViewChannels(BaseSchema):
    pass


class ZoneProductTypes(BaseSchema):
    pass


class ZoneMappingType(BaseSchema):
    pass


class UpdateZoneData(BaseSchema):
    pass


class ZoneUpdateRequest(BaseSchema):
    pass


class ZoneSuccessResponse(BaseSchema):
    pass


class GetZoneDataViewItems(BaseSchema):
    pass


class GetSingleZoneDataViewResponse(BaseSchema):
    pass


class CreateZoneData(BaseSchema):
    pass


class ZoneRequest(BaseSchema):
    pass


class ZoneResponse(BaseSchema):
    pass


class GetZoneFromPincodeViewRequest(BaseSchema):
    pass


class GetZoneFromPincodeViewResponse(BaseSchema):
    pass


class AddressResponse(BaseSchema):
    pass


class ContactNumberResponse(BaseSchema):
    pass


class IntegrationTypeResponse(BaseSchema):
    pass


class CreatedByResponse(BaseSchema):
    pass


class MobileNo(BaseSchema):
    pass


class ManagerResponse(BaseSchema):
    pass


class ProductReturnConfigResponse(BaseSchema):
    pass


class ModifiedByResponse(BaseSchema):
    pass


class EwayBillResponse(BaseSchema):
    pass


class EinvoiceResponse(BaseSchema):
    pass


class GstCredentialsResponse(BaseSchema):
    pass


class DocumentsResponse(BaseSchema):
    pass


class Dp(BaseSchema):
    pass


class LogisticsResponse(BaseSchema):
    pass


class OpeningClosing(BaseSchema):
    pass


class TimmingResponse(BaseSchema):
    pass


class WarningsResponse(BaseSchema):
    pass


class ItemResponse(BaseSchema):
    pass


class PageResponse(BaseSchema):
    pass


class GetStoresViewResponse(BaseSchema):
    pass





class ApplicationServiceabilityConfig(BaseSchema):
    # Serviceability swagger.json

    
    serviceability_type = fields.Str(required=False)
    
    channel_id = fields.Str(required=False)
    
    channel_type = fields.Str(required=False)
    


class ServiceabilityrErrorResponse(BaseSchema):
    # Serviceability swagger.json

    
    value = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class ApplicationServiceabilityConfigResponse(BaseSchema):
    # Serviceability swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.Nested(ApplicationServiceabilityConfig, required=False)
    
    error = fields.Nested(ServiceabilityrErrorResponse, required=False)
    


class EntityRegionView_Request(BaseSchema):
    # Serviceability swagger.json

    
    parent_id = fields.List(fields.Str(required=False), required=False)
    
    sub_type = fields.List(fields.Str(required=False), required=False)
    


class EntityRegionView_page(BaseSchema):
    # Serviceability swagger.json

    
    type = fields.Str(required=False)
    
    current = fields.Int(required=False)
    
    size = fields.Int(required=False)
    
    item_total = fields.Int(required=False)
    
    has_next = fields.Boolean(required=False)
    


class EntityRegionView_Items(BaseSchema):
    # Serviceability swagger.json

    
    sub_type = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    name = fields.Str(required=False)
    


class EntityRegionView_Error(BaseSchema):
    # Serviceability swagger.json

    
    value = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class EntityRegionView_Response(BaseSchema):
    # Serviceability swagger.json

    
    success = fields.Boolean(required=False)
    
    page = fields.Nested(EntityRegionView_page, required=False)
    
    data = fields.List(fields.Nested(EntityRegionView_Items, required=False), required=False)
    
    error = fields.Nested(EntityRegionView_Error, required=False)
    


class ZoneDataItem(BaseSchema):
    # Serviceability swagger.json

    
    current = fields.Int(required=False)
    
    size = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    item_total = fields.Int(required=False)
    
    has_next = fields.Boolean(required=False)
    


class ListViewProduct(BaseSchema):
    # Serviceability swagger.json

    
    count = fields.Int(required=False)
    
    type = fields.Str(required=False)
    


class ListViewChannels(BaseSchema):
    # Serviceability swagger.json

    
    channel_id = fields.Str(required=False)
    
    channel_type = fields.Str(required=False)
    


class ListViewItems(BaseSchema):
    # Serviceability swagger.json

    
    pincodes_count = fields.Int(required=False)
    
    slug = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    zone_id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    stores_count = fields.Int(required=False)
    
    product = fields.Nested(ListViewProduct, required=False)
    
    channels = fields.Nested(ListViewChannels, required=False)
    
    is_active = fields.Boolean(required=False)
    


class ListViewSummary(BaseSchema):
    # Serviceability swagger.json

    
    total_zones = fields.Int(required=False)
    
    total_active_zones = fields.Int(required=False)
    
    total_pincodes_served = fields.Int(required=False)
    


class ListViewResponse(BaseSchema):
    # Serviceability swagger.json

    
    page = fields.List(fields.Nested(ZoneDataItem, required=False), required=False)
    
    items = fields.List(fields.Nested(ListViewItems, required=False), required=False)
    
    summary = fields.List(fields.Nested(ListViewSummary, required=False), required=False)
    


class CompanyStoreView_PageItems(BaseSchema):
    # Serviceability swagger.json

    
    type = fields.Str(required=False)
    
    current = fields.Int(required=False)
    
    size = fields.Int(required=False)
    
    item_total = fields.Int(required=False)
    
    has_next = fields.Boolean(required=False)
    


class CompanyStoreView_Response(BaseSchema):
    # Serviceability swagger.json

    
    items = fields.List(fields.Dict(required=False), required=False)
    
    page = fields.List(fields.Nested(CompanyStoreView_PageItems, required=False), required=False)
    


class GetZoneDataViewChannels(BaseSchema):
    # Serviceability swagger.json

    
    channel_id = fields.Str(required=False)
    
    channel_type = fields.Str(required=False)
    


class ZoneProductTypes(BaseSchema):
    # Serviceability swagger.json

    
    tags = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    


class ZoneMappingType(BaseSchema):
    # Serviceability swagger.json

    
    state = fields.List(fields.Str(required=False), required=False)
    
    country = fields.Str(required=False)
    
    pincode = fields.List(fields.Str(required=False), required=False)
    


class UpdateZoneData(BaseSchema):
    # Serviceability swagger.json

    
    zone_id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    channels = fields.List(fields.Nested(GetZoneDataViewChannels, required=False), required=False)
    
    product = fields.Nested(ZoneProductTypes, required=False)
    
    store_ids = fields.List(fields.Int(required=False), required=False)
    
    region_type = fields.Str(required=False)
    
    mapping = fields.List(fields.Nested(ZoneMappingType, required=False), required=False)
    
    assignment_preference = fields.Str(required=False)
    


class ZoneUpdateRequest(BaseSchema):
    # Serviceability swagger.json

    
    data = fields.Nested(UpdateZoneData, required=False)
    
    identifier = fields.Str(required=False)
    


class ZoneSuccessResponse(BaseSchema):
    # Serviceability swagger.json

    
    success = fields.Boolean(required=False)
    
    status_code = fields.Int(required=False)
    


class GetZoneDataViewItems(BaseSchema):
    # Serviceability swagger.json

    
    zone_id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    channels = fields.List(fields.Nested(GetZoneDataViewChannels, required=False), required=False)
    
    product = fields.Nested(ZoneProductTypes, required=False)
    
    store_ids = fields.List(fields.Int(required=False), required=False)
    
    region_type = fields.Str(required=False)
    
    mapping = fields.List(fields.Nested(ZoneMappingType, required=False), required=False)
    
    assignment_preference = fields.Str(required=False)
    
    stores_count = fields.Int(required=False)
    
    pincodes_count = fields.Int(required=False)
    


class GetSingleZoneDataViewResponse(BaseSchema):
    # Serviceability swagger.json

    
    data = fields.Nested(GetZoneDataViewItems, required=False)
    


class CreateZoneData(BaseSchema):
    # Serviceability swagger.json

    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    channels = fields.List(fields.Nested(GetZoneDataViewChannels, required=False), required=False)
    
    product = fields.Nested(ZoneProductTypes, required=False)
    
    store_ids = fields.List(fields.Int(required=False), required=False)
    
    region_type = fields.Str(required=False)
    
    mapping = fields.List(fields.Nested(ZoneMappingType, required=False), required=False)
    
    assignment_preference = fields.Str(required=False)
    


class ZoneRequest(BaseSchema):
    # Serviceability swagger.json

    
    data = fields.Nested(CreateZoneData, required=False)
    
    identifier = fields.Str(required=False)
    


class ZoneResponse(BaseSchema):
    # Serviceability swagger.json

    
    success = fields.Boolean(required=False)
    
    status_code = fields.Int(required=False)
    
    zone_id = fields.Str(required=False)
    


class GetZoneFromPincodeViewRequest(BaseSchema):
    # Serviceability swagger.json

    
    country = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    


class GetZoneFromPincodeViewResponse(BaseSchema):
    # Serviceability swagger.json

    
    serviceability_type = fields.Str(required=False)
    
    zones = fields.List(fields.Str(required=False), required=False)
    


class AddressResponse(BaseSchema):
    # Serviceability swagger.json

    
    address2 = fields.Str(required=False)
    
    longitude = fields.Float(required=False)
    
    city = fields.Str(required=False)
    
    address1 = fields.Str(required=False)
    
    latitude = fields.Float(required=False)
    
    landmark = fields.Str(required=False)
    
    pincode = fields.Int(required=False)
    
    state = fields.Str(required=False)
    
    country = fields.Str(required=False)
    


class ContactNumberResponse(BaseSchema):
    # Serviceability swagger.json

    
    country_code = fields.Int(required=False)
    
    number = fields.Str(required=False)
    


class IntegrationTypeResponse(BaseSchema):
    # Serviceability swagger.json

    
    order = fields.Str(required=False)
    
    inventory = fields.Str(required=False)
    


class CreatedByResponse(BaseSchema):
    # Serviceability swagger.json

    
    user_id = fields.Str(required=False)
    
    username = fields.Str(required=False)
    


class MobileNo(BaseSchema):
    # Serviceability swagger.json

    
    country_code = fields.Int(required=False)
    
    number = fields.Str(required=False)
    


class ManagerResponse(BaseSchema):
    # Serviceability swagger.json

    
    mobile_no = fields.Nested(MobileNo, required=False)
    
    name = fields.Str(required=False)
    
    email = fields.Str(required=False)
    


class ProductReturnConfigResponse(BaseSchema):
    # Serviceability swagger.json

    
    on_same_store = fields.Boolean(required=False)
    


class ModifiedByResponse(BaseSchema):
    # Serviceability swagger.json

    
    user_id = fields.Str(required=False)
    
    username = fields.Str(required=False)
    


class EwayBillResponse(BaseSchema):
    # Serviceability swagger.json

    
    enabled = fields.Boolean(required=False)
    


class EinvoiceResponse(BaseSchema):
    # Serviceability swagger.json

    
    enabled = fields.Boolean(required=False)
    


class GstCredentialsResponse(BaseSchema):
    # Serviceability swagger.json

    
    e_waybill = fields.Nested(EwayBillResponse, required=False)
    
    e_invoice = fields.Nested(EinvoiceResponse, required=False)
    


class DocumentsResponse(BaseSchema):
    # Serviceability swagger.json

    
    legal_name = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    verified = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    


class Dp(BaseSchema):
    # Serviceability swagger.json

    
    external_account_id = fields.Str(required=False)
    
    rvp_priority = fields.Int(required=False)
    
    area_code = fields.Int(required=False)
    
    lm_priority = fields.Int(required=False)
    
    assign_dp_from_sb = fields.Boolean(required=False)
    
    transport_mode = fields.Str(required=False)
    
    fm_priority = fields.Int(required=False)
    
    payment_mode = fields.Str(required=False)
    
    operations = fields.List(fields.Str(required=False), required=False)
    
    internal_account_id = fields.Str(required=False)
    


class LogisticsResponse(BaseSchema):
    # Serviceability swagger.json

    
    dp = fields.Nested(Dp, required=False)
    
    override = fields.Boolean(required=False)
    


class OpeningClosing(BaseSchema):
    # Serviceability swagger.json

    
    hour = fields.Int(required=False)
    
    minute = fields.Int(required=False)
    


class TimmingResponse(BaseSchema):
    # Serviceability swagger.json

    
    opening = fields.Nested(OpeningClosing, required=False)
    
    closing = fields.Nested(OpeningClosing, required=False)
    
    open = fields.Boolean(required=False)
    
    weekday = fields.Str(required=False)
    


class WarningsResponse(BaseSchema):
    # Serviceability swagger.json

    
    store_address = fields.Str(required=False)
    


class ItemResponse(BaseSchema):
    # Serviceability swagger.json

    
    address = fields.Nested(AddressResponse, required=False)
    
    verified_on = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    _cls = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    contact_numbers = fields.List(fields.Nested(ContactNumberResponse, required=False), required=False)
    
    integration_type = fields.Nested(IntegrationTypeResponse, required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    created_by = fields.Nested(CreatedByResponse, required=False)
    
    stage = fields.Str(required=False)
    
    manager = fields.Nested(ManagerResponse, required=False)
    
    modified_on = fields.Str(required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigResponse, required=False)
    
    verified_by = fields.Nested(ModifiedByResponse, required=False)
    
    store_type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    company = fields.Int(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    code = fields.Str(required=False)
    
    gst_credentials = fields.Nested(GstCredentialsResponse, required=False)
    
    documents = fields.List(fields.Nested(DocumentsResponse, required=False), required=False)
    
    logistics = fields.Nested(LogisticsResponse, required=False)
    
    uid = fields.Int(required=False)
    
    timing = fields.List(fields.Nested(TimmingResponse, required=False), required=False)
    
    warnings = fields.Nested(WarningsResponse, required=False)
    
    modified_by = fields.Nested(ModifiedByResponse, required=False)
    
    sub_type = fields.Str(required=False)
    


class PageResponse(BaseSchema):
    # Serviceability swagger.json

    
    type = fields.Str(required=False)
    
    current = fields.Int(required=False)
    
    size = fields.Int(required=False)
    
    item_total = fields.Int(required=False)
    
    has_next = fields.Boolean(required=False)
    


class GetStoresViewResponse(BaseSchema):
    # Serviceability swagger.json

    
    items = fields.List(fields.Nested(ItemResponse, required=False), required=False)
    
    page = fields.Nested(PageResponse, required=False)
    

