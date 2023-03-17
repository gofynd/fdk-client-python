"""Logistic Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ..PlatformModel import BaseSchema





class ServiceabilityErrorResponse(BaseSchema):
    pass


class ApplicationServiceabilityConfig(BaseSchema):
    pass


class ApplicationServiceabilityConfigResponse(BaseSchema):
    pass


class EntityRegionView_Request(BaseSchema):
    pass


class EntityRegionView_Error(BaseSchema):
    pass


class EntityRegionView_page(BaseSchema):
    pass


class EntityRegionView_Items(BaseSchema):
    pass


class EntityRegionView_Response(BaseSchema):
    pass


class ZoneDataItem(BaseSchema):
    pass


class ListViewSummary(BaseSchema):
    pass


class ListViewProduct(BaseSchema):
    pass


class ListViewChannels(BaseSchema):
    pass


class ListViewItems(BaseSchema):
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


class GetZoneDataViewItems(BaseSchema):
    pass


class GetSingleZoneDataViewResponse(BaseSchema):
    pass


class UpdateZoneData(BaseSchema):
    pass


class ZoneUpdateRequest(BaseSchema):
    pass


class ZoneSuccessResponse(BaseSchema):
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


class ServiceabilityPageResponse(BaseSchema):
    pass


class DocumentsResponse(BaseSchema):
    pass


class AddressResponse(BaseSchema):
    pass


class ModifiedByResponse(BaseSchema):
    pass


class CreatedByResponse(BaseSchema):
    pass


class WarningsResponse(BaseSchema):
    pass


class OpeningClosing(BaseSchema):
    pass


class TimmingResponse(BaseSchema):
    pass


class ProductReturnConfigResponse(BaseSchema):
    pass


class MobileNo(BaseSchema):
    pass


class ManagerResponse(BaseSchema):
    pass


class IntegrationTypeResponse(BaseSchema):
    pass


class ContactNumberResponse(BaseSchema):
    pass


class Dp(BaseSchema):
    pass


class LogisticsResponse(BaseSchema):
    pass


class EwayBillResponse(BaseSchema):
    pass


class EinvoiceResponse(BaseSchema):
    pass


class GstCredentialsResponse(BaseSchema):
    pass


class ItemResponse(BaseSchema):
    pass


class GetStoresViewResponse(BaseSchema):
    pass





class ServiceabilityErrorResponse(BaseSchema):
    # Logistic swagger.json

    
    message = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class ApplicationServiceabilityConfig(BaseSchema):
    # Logistic swagger.json

    
    channel_id = fields.Str(required=False)
    
    serviceability_type = fields.Str(required=False)
    
    channel_type = fields.Str(required=False)
    


class ApplicationServiceabilityConfigResponse(BaseSchema):
    # Logistic swagger.json

    
    error = fields.Nested(ServiceabilityErrorResponse, required=False)
    
    data = fields.Nested(ApplicationServiceabilityConfig, required=False)
    
    success = fields.Boolean(required=False)
    


class EntityRegionView_Request(BaseSchema):
    # Logistic swagger.json

    
    sub_type = fields.List(fields.Str(required=False), required=False)
    
    parent_id = fields.List(fields.Str(required=False), required=False)
    


class EntityRegionView_Error(BaseSchema):
    # Logistic swagger.json

    
    message = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class EntityRegionView_page(BaseSchema):
    # Logistic swagger.json

    
    current = fields.Int(required=False)
    
    size = fields.Int(required=False)
    
    item_total = fields.Int(required=False)
    
    has_next = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    


class EntityRegionView_Items(BaseSchema):
    # Logistic swagger.json

    
    name = fields.Str(required=False)
    
    sub_type = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    


class EntityRegionView_Response(BaseSchema):
    # Logistic swagger.json

    
    error = fields.Nested(EntityRegionView_Error, required=False)
    
    page = fields.Nested(EntityRegionView_page, required=False)
    
    data = fields.List(fields.Nested(EntityRegionView_Items, required=False), required=False)
    
    success = fields.Boolean(required=False)
    


class ZoneDataItem(BaseSchema):
    # Logistic swagger.json

    
    current = fields.Int(required=False)
    
    size = fields.Int(required=False)
    
    item_total = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    has_next = fields.Boolean(required=False)
    


class ListViewSummary(BaseSchema):
    # Logistic swagger.json

    
    total_zones = fields.Int(required=False)
    
    total_active_zones = fields.Int(required=False)
    
    total_pincodes_served = fields.Int(required=False)
    


class ListViewProduct(BaseSchema):
    # Logistic swagger.json

    
    count = fields.Int(required=False)
    
    type = fields.Str(required=False)
    


class ListViewChannels(BaseSchema):
    # Logistic swagger.json

    
    channel_id = fields.Str(required=False)
    
    channel_type = fields.Str(required=False)
    


class ListViewItems(BaseSchema):
    # Logistic swagger.json

    
    stores_count = fields.Int(required=False)
    
    pincodes_count = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    product = fields.Nested(ListViewProduct, required=False)
    
    company_id = fields.Int(required=False)
    
    channels = fields.Nested(ListViewChannels, required=False)
    
    slug = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    zone_id = fields.Str(required=False)
    


class ListViewResponse(BaseSchema):
    # Logistic swagger.json

    
    page = fields.List(fields.Nested(ZoneDataItem, required=False), required=False)
    
    summary = fields.List(fields.Nested(ListViewSummary, required=False), required=False)
    
    items = fields.List(fields.Nested(ListViewItems, required=False), required=False)
    


class CompanyStoreView_PageItems(BaseSchema):
    # Logistic swagger.json

    
    current = fields.Int(required=False)
    
    size = fields.Int(required=False)
    
    item_total = fields.Int(required=False)
    
    has_next = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    


class CompanyStoreView_Response(BaseSchema):
    # Logistic swagger.json

    
    page = fields.List(fields.Nested(CompanyStoreView_PageItems, required=False), required=False)
    
    items = fields.List(fields.Dict(required=False), required=False)
    


class GetZoneDataViewChannels(BaseSchema):
    # Logistic swagger.json

    
    channel_id = fields.Str(required=False)
    
    channel_type = fields.Str(required=False)
    


class ZoneProductTypes(BaseSchema):
    # Logistic swagger.json

    
    tags = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    


class ZoneMappingType(BaseSchema):
    # Logistic swagger.json

    
    country = fields.Str(required=False)
    
    pincode = fields.List(fields.Str(required=False), required=False)
    
    state = fields.List(fields.Str(required=False), required=False)
    


class GetZoneDataViewItems(BaseSchema):
    # Logistic swagger.json

    
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
    # Logistic swagger.json

    
    data = fields.Nested(GetZoneDataViewItems, required=False)
    


class UpdateZoneData(BaseSchema):
    # Logistic swagger.json

    
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
    # Logistic swagger.json

    
    identifier = fields.Str(required=False)
    
    data = fields.Nested(UpdateZoneData, required=False)
    


class ZoneSuccessResponse(BaseSchema):
    # Logistic swagger.json

    
    status_code = fields.Int(required=False)
    
    success = fields.Boolean(required=False)
    


class CreateZoneData(BaseSchema):
    # Logistic swagger.json

    
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
    # Logistic swagger.json

    
    identifier = fields.Str(required=False)
    
    data = fields.Nested(CreateZoneData, required=False)
    


class ZoneResponse(BaseSchema):
    # Logistic swagger.json

    
    status_code = fields.Int(required=False)
    
    zone_id = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class GetZoneFromPincodeViewRequest(BaseSchema):
    # Logistic swagger.json

    
    pincode = fields.Str(required=False)
    
    country = fields.Str(required=False)
    


class GetZoneFromPincodeViewResponse(BaseSchema):
    # Logistic swagger.json

    
    zones = fields.List(fields.Str(required=False), required=False)
    
    serviceability_type = fields.Str(required=False)
    


class ServiceabilityPageResponse(BaseSchema):
    # Logistic swagger.json

    
    current = fields.Int(required=False)
    
    size = fields.Int(required=False)
    
    item_total = fields.Int(required=False)
    
    has_next = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    


class DocumentsResponse(BaseSchema):
    # Logistic swagger.json

    
    value = fields.Str(required=False)
    
    legal_name = fields.Str(required=False)
    
    verified = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    


class AddressResponse(BaseSchema):
    # Logistic swagger.json

    
    landmark = fields.Str(required=False)
    
    pincode = fields.Int(required=False)
    
    city = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    latitude = fields.Float(required=False)
    
    state = fields.Str(required=False)
    
    address1 = fields.Str(required=False)
    
    address2 = fields.Str(required=False)
    
    longitude = fields.Float(required=False)
    


class ModifiedByResponse(BaseSchema):
    # Logistic swagger.json

    
    username = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    


class CreatedByResponse(BaseSchema):
    # Logistic swagger.json

    
    username = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    


class WarningsResponse(BaseSchema):
    # Logistic swagger.json

    
    store_address = fields.Str(required=False)
    


class OpeningClosing(BaseSchema):
    # Logistic swagger.json

    
    hour = fields.Int(required=False)
    
    minute = fields.Int(required=False)
    


class TimmingResponse(BaseSchema):
    # Logistic swagger.json

    
    closing = fields.Nested(OpeningClosing, required=False)
    
    opening = fields.Nested(OpeningClosing, required=False)
    
    weekday = fields.Str(required=False)
    
    open = fields.Boolean(required=False)
    


class ProductReturnConfigResponse(BaseSchema):
    # Logistic swagger.json

    
    on_same_store = fields.Boolean(required=False)
    


class MobileNo(BaseSchema):
    # Logistic swagger.json

    
    country_code = fields.Int(required=False)
    
    number = fields.Str(required=False)
    


class ManagerResponse(BaseSchema):
    # Logistic swagger.json

    
    mobile_no = fields.Nested(MobileNo, required=False)
    
    name = fields.Str(required=False)
    
    email = fields.Str(required=False)
    


class IntegrationTypeResponse(BaseSchema):
    # Logistic swagger.json

    
    inventory = fields.Str(required=False)
    
    order = fields.Str(required=False)
    


class ContactNumberResponse(BaseSchema):
    # Logistic swagger.json

    
    country_code = fields.Int(required=False)
    
    number = fields.Str(required=False)
    


class Dp(BaseSchema):
    # Logistic swagger.json

    
    fm_priority = fields.Int(required=False)
    
    payment_mode = fields.Str(required=False)
    
    external_account_id = fields.Str(required=False)
    
    rvp_priority = fields.Int(required=False)
    
    assign_dp_from_sb = fields.Boolean(required=False)
    
    lm_priority = fields.Int(required=False)
    
    transport_mode = fields.Str(required=False)
    
    operations = fields.List(fields.Str(required=False), required=False)
    
    internal_account_id = fields.Str(required=False)
    
    area_code = fields.Int(required=False)
    


class LogisticsResponse(BaseSchema):
    # Logistic swagger.json

    
    override = fields.Boolean(required=False)
    
    dp = fields.Nested(Dp, required=False)
    


class EwayBillResponse(BaseSchema):
    # Logistic swagger.json

    
    enabled = fields.Boolean(required=False)
    


class EinvoiceResponse(BaseSchema):
    # Logistic swagger.json

    
    enabled = fields.Boolean(required=False)
    


class GstCredentialsResponse(BaseSchema):
    # Logistic swagger.json

    
    e_waybill = fields.Nested(EwayBillResponse, required=False)
    
    e_invoice = fields.Nested(EinvoiceResponse, required=False)
    


class ItemResponse(BaseSchema):
    # Logistic swagger.json

    
    documents = fields.List(fields.Nested(DocumentsResponse, required=False), required=False)
    
    company = fields.Int(required=False)
    
    address = fields.Nested(AddressResponse, required=False)
    
    display_name = fields.Str(required=False)
    
    modified_by = fields.Nested(ModifiedByResponse, required=False)
    
    modified_on = fields.Str(required=False)
    
    _cls = fields.Str(required=False)
    
    created_by = fields.Nested(CreatedByResponse, required=False)
    
    warnings = fields.Nested(WarningsResponse, required=False)
    
    timing = fields.List(fields.Nested(TimmingResponse, required=False), required=False)
    
    code = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    created_on = fields.Str(required=False)
    
    sub_type = fields.Str(required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigResponse, required=False)
    
    manager = fields.Nested(ManagerResponse, required=False)
    
    integration_type = fields.Nested(IntegrationTypeResponse, required=False)
    
    contact_numbers = fields.List(fields.Nested(ContactNumberResponse, required=False), required=False)
    
    uid = fields.Int(required=False)
    
    stage = fields.Str(required=False)
    
    verified_by = fields.Nested(ModifiedByResponse, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    verified_on = fields.Str(required=False)
    
    logistics = fields.Nested(LogisticsResponse, required=False)
    
    store_type = fields.Str(required=False)
    
    gst_credentials = fields.Nested(GstCredentialsResponse, required=False)
    
    name = fields.Str(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    


class GetStoresViewResponse(BaseSchema):
    # Logistic swagger.json

    
    page = fields.Nested(ServiceabilityPageResponse, required=False)
    
    items = fields.List(fields.Nested(ItemResponse, required=False), required=False)
    


