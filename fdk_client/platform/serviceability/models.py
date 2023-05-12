"""Serviceability Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




class ServiceabilityrErrorResponse(BaseSchema):
    pass


class ApplicationServiceabilityConfig(BaseSchema):
    pass


class ApplicationServiceabilityConfigResponse(BaseSchema):
    pass


class EntityRegionView_Request(BaseSchema):
    pass


class EntityRegionView_page(BaseSchema):
    pass


class EntityRegionView_Error(BaseSchema):
    pass


class EntityRegionView_Items(BaseSchema):
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


class OpeningClosing(BaseSchema):
    pass


class TimmingResponse(BaseSchema):
    pass


class ModifiedByResponse(BaseSchema):
    pass


class WarningsResponse(BaseSchema):
    pass


class IntegrationTypeResponse(BaseSchema):
    pass


class CreatedByResponse(BaseSchema):
    pass


class ProductReturnConfigResponse(BaseSchema):
    pass


class MobileNo(BaseSchema):
    pass


class ManagerResponse(BaseSchema):
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


class AddressResponse(BaseSchema):
    pass


class DocumentsResponse(BaseSchema):
    pass


class ContactNumberResponse(BaseSchema):
    pass


class ItemResponse(BaseSchema):
    pass


class ServiceabilityPageResponse(BaseSchema):
    pass


class GetStoresViewResponse(BaseSchema):
    pass


class ReAssignStoreRequest(BaseSchema):
    pass


class ReAssignStoreResponse(BaseSchema):
    pass





class ServiceabilityrErrorResponse(BaseSchema):
    # Serviceability swagger.json

    
    type = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class ApplicationServiceabilityConfig(BaseSchema):
    # Serviceability swagger.json

    
    channel_type = fields.Str(required=False)
    
    channel_id = fields.Str(required=False)
    
    serviceability_type = fields.Str(required=False)
    


class ApplicationServiceabilityConfigResponse(BaseSchema):
    # Serviceability swagger.json

    
    error = fields.Nested(ServiceabilityrErrorResponse, required=False)
    
    data = fields.Nested(ApplicationServiceabilityConfig, required=False)
    
    success = fields.Boolean(required=False)
    


class EntityRegionView_Request(BaseSchema):
    # Serviceability swagger.json

    
    sub_type = fields.List(fields.Str(required=False), required=False)
    
    parent_id = fields.List(fields.Str(required=False), required=False)
    


class EntityRegionView_page(BaseSchema):
    # Serviceability swagger.json

    
    has_next = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    
    item_total = fields.Int(required=False)
    
    size = fields.Int(required=False)
    
    current = fields.Int(required=False)
    


class EntityRegionView_Error(BaseSchema):
    # Serviceability swagger.json

    
    type = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class EntityRegionView_Items(BaseSchema):
    # Serviceability swagger.json

    
    name = fields.Str(required=False)
    
    sub_type = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    


class EntityRegionView_Response(BaseSchema):
    # Serviceability swagger.json

    
    page = fields.Nested(EntityRegionView_page, required=False)
    
    error = fields.Nested(EntityRegionView_Error, required=False)
    
    data = fields.List(fields.Nested(EntityRegionView_Items, required=False), required=False)
    
    success = fields.Boolean(required=False)
    


class ZoneDataItem(BaseSchema):
    # Serviceability swagger.json

    
    has_next = fields.Boolean(required=False)
    
    item_total = fields.Int(required=False)
    
    size = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    current = fields.Int(required=False)
    


class ListViewProduct(BaseSchema):
    # Serviceability swagger.json

    
    type = fields.Str(required=False)
    
    count = fields.Int(required=False)
    


class ListViewChannels(BaseSchema):
    # Serviceability swagger.json

    
    channel_type = fields.Str(required=False)
    
    channel_id = fields.Str(required=False)
    


class ListViewItems(BaseSchema):
    # Serviceability swagger.json

    
    name = fields.Str(required=False)
    
    zone_id = fields.Str(required=False)
    
    pincodes_count = fields.Int(required=False)
    
    slug = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    product = fields.Nested(ListViewProduct, required=False)
    
    stores_count = fields.Int(required=False)
    
    company_id = fields.Int(required=False)
    
    channels = fields.Nested(ListViewChannels, required=False)
    


class ListViewSummary(BaseSchema):
    # Serviceability swagger.json

    
    total_zones = fields.Int(required=False)
    
    total_pincodes_served = fields.Int(required=False)
    
    total_active_zones = fields.Int(required=False)
    


class ListViewResponse(BaseSchema):
    # Serviceability swagger.json

    
    page = fields.List(fields.Nested(ZoneDataItem, required=False), required=False)
    
    items = fields.List(fields.Nested(ListViewItems, required=False), required=False)
    
    summary = fields.List(fields.Nested(ListViewSummary, required=False), required=False)
    


class CompanyStoreView_PageItems(BaseSchema):
    # Serviceability swagger.json

    
    has_next = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    
    item_total = fields.Int(required=False)
    
    size = fields.Int(required=False)
    
    current = fields.Int(required=False)
    


class CompanyStoreView_Response(BaseSchema):
    # Serviceability swagger.json

    
    items = fields.List(fields.Dict(required=False), required=False)
    
    page = fields.List(fields.Nested(CompanyStoreView_PageItems, required=False), required=False)
    


class GetZoneDataViewChannels(BaseSchema):
    # Serviceability swagger.json

    
    channel_type = fields.Str(required=False)
    
    channel_id = fields.Str(required=False)
    


class ZoneProductTypes(BaseSchema):
    # Serviceability swagger.json

    
    type = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    


class ZoneMappingType(BaseSchema):
    # Serviceability swagger.json

    
    state = fields.List(fields.Str(required=False), required=False)
    
    pincode = fields.List(fields.Str(required=False), required=False)
    
    country = fields.Str(required=False)
    


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

    
    status_code = fields.Int(required=False)
    
    success = fields.Boolean(required=False)
    


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

    
    zone_id = fields.Str(required=False)
    
    status_code = fields.Int(required=False)
    
    success = fields.Boolean(required=False)
    


class GetZoneFromPincodeViewRequest(BaseSchema):
    # Serviceability swagger.json

    
    pincode = fields.Str(required=False)
    
    country = fields.Str(required=False)
    


class GetZoneFromPincodeViewResponse(BaseSchema):
    # Serviceability swagger.json

    
    zones = fields.List(fields.Str(required=False), required=False)
    
    serviceability_type = fields.Str(required=False)
    


class OpeningClosing(BaseSchema):
    # Serviceability swagger.json

    
    minute = fields.Int(required=False)
    
    hour = fields.Int(required=False)
    


class TimmingResponse(BaseSchema):
    # Serviceability swagger.json

    
    open = fields.Boolean(required=False)
    
    weekday = fields.Str(required=False)
    
    opening = fields.Nested(OpeningClosing, required=False)
    
    closing = fields.Nested(OpeningClosing, required=False)
    


class ModifiedByResponse(BaseSchema):
    # Serviceability swagger.json

    
    user_id = fields.Str(required=False)
    
    username = fields.Str(required=False)
    


class WarningsResponse(BaseSchema):
    # Serviceability swagger.json

    
    store_address = fields.Str(required=False)
    


class IntegrationTypeResponse(BaseSchema):
    # Serviceability swagger.json

    
    inventory = fields.Str(required=False)
    
    order = fields.Str(required=False)
    


class CreatedByResponse(BaseSchema):
    # Serviceability swagger.json

    
    user_id = fields.Str(required=False)
    
    username = fields.Str(required=False)
    


class ProductReturnConfigResponse(BaseSchema):
    # Serviceability swagger.json

    
    on_same_store = fields.Boolean(required=False)
    


class MobileNo(BaseSchema):
    # Serviceability swagger.json

    
    number = fields.Str(required=False)
    
    country_code = fields.Int(required=False)
    


class ManagerResponse(BaseSchema):
    # Serviceability swagger.json

    
    name = fields.Str(required=False)
    
    mobile_no = fields.Nested(MobileNo, required=False)
    
    email = fields.Str(required=False)
    


class Dp(BaseSchema):
    # Serviceability swagger.json

    
    external_account_id = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
    rvp_priority = fields.Int(required=False)
    
    area_code = fields.Int(required=False)
    
    lm_priority = fields.Int(required=False)
    
    transport_mode = fields.Str(required=False)
    
    fm_priority = fields.Int(required=False)
    
    operations = fields.List(fields.Str(required=False), required=False)
    
    assign_dp_from_sb = fields.Boolean(required=False)
    
    internal_account_id = fields.Str(required=False)
    


class LogisticsResponse(BaseSchema):
    # Serviceability swagger.json

    
    dp = fields.Nested(Dp, required=False)
    
    override = fields.Boolean(required=False)
    


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
    


class AddressResponse(BaseSchema):
    # Serviceability swagger.json

    
    landmark = fields.Str(required=False)
    
    address2 = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    pincode = fields.Int(required=False)
    
    longitude = fields.Float(required=False)
    
    address1 = fields.Str(required=False)
    
    latitude = fields.Float(required=False)
    


class DocumentsResponse(BaseSchema):
    # Serviceability swagger.json

    
    type = fields.Str(required=False)
    
    legal_name = fields.Str(required=False)
    
    verified = fields.Boolean(required=False)
    
    value = fields.Str(required=False)
    


class ContactNumberResponse(BaseSchema):
    # Serviceability swagger.json

    
    number = fields.Str(required=False)
    
    country_code = fields.Int(required=False)
    


class ItemResponse(BaseSchema):
    # Serviceability swagger.json

    
    timing = fields.List(fields.Nested(TimmingResponse, required=False), required=False)
    
    display_name = fields.Str(required=False)
    
    verified_by = fields.Nested(ModifiedByResponse, required=False)
    
    warnings = fields.Nested(WarningsResponse, required=False)
    
    verified_on = fields.Str(required=False)
    
    integration_type = fields.Nested(IntegrationTypeResponse, required=False)
    
    created_by = fields.Nested(CreatedByResponse, required=False)
    
    company = fields.Int(required=False)
    
    sub_type = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigResponse, required=False)
    
    name = fields.Str(required=False)
    
    manager = fields.Nested(ManagerResponse, required=False)
    
    uid = fields.Int(required=False)
    
    _cls = fields.Str(required=False)
    
    logistics = fields.Nested(LogisticsResponse, required=False)
    
    gst_credentials = fields.Nested(GstCredentialsResponse, required=False)
    
    modified_by = fields.Nested(ModifiedByResponse, required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    stage = fields.Str(required=False)
    
    address = fields.Nested(AddressResponse, required=False)
    
    created_on = fields.Str(required=False)
    
    documents = fields.List(fields.Nested(DocumentsResponse, required=False), required=False)
    
    store_type = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    contact_numbers = fields.List(fields.Nested(ContactNumberResponse, required=False), required=False)
    


class ServiceabilityPageResponse(BaseSchema):
    # Serviceability swagger.json

    
    has_next = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    
    item_total = fields.Int(required=False)
    
    size = fields.Int(required=False)
    
    current = fields.Int(required=False)
    


class GetStoresViewResponse(BaseSchema):
    # Serviceability swagger.json

    
    items = fields.List(fields.Nested(ItemResponse, required=False), required=False)
    
    page = fields.Nested(ServiceabilityPageResponse, required=False)
    


class ReAssignStoreRequest(BaseSchema):
    # Serviceability swagger.json

    
    to_pincode = fields.Str(required=False)
    
    articles = fields.List(fields.Dict(required=False), required=False)
    
    configuration = fields.Dict(required=False)
    
    identifier = fields.Str(required=False)
    
    ignored_locations = fields.List(fields.Str(required=False), required=False)
    


class ReAssignStoreResponse(BaseSchema):
    # Serviceability swagger.json

    
    articles = fields.List(fields.Dict(required=False), required=False)
    
    to_pincode = fields.Str(required=False)
    
    error = fields.Dict(required=False)
    
    success = fields.Boolean(required=False)
    


