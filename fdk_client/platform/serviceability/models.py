"""Serviceability Platform Model"""

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


class ListViewSummary(BaseSchema):
    pass


class ListViewChannels(BaseSchema):
    pass


class ListViewProduct(BaseSchema):
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


class GetZoneFromApplicationIdViewResponse(BaseSchema):
    pass


class GetZoneFromPincodeViewRequest(BaseSchema):
    pass


class GetZoneFromPincodeViewResponse(BaseSchema):
    pass


class ServiceabilityPageResponse(BaseSchema):
    pass


class OpeningClosing(BaseSchema):
    pass


class TimmingResponse(BaseSchema):
    pass


class MobileNo(BaseSchema):
    pass


class ManagerResponse(BaseSchema):
    pass


class ProductReturnConfigResponse(BaseSchema):
    pass


class Dp(BaseSchema):
    pass


class LogisticsResponse(BaseSchema):
    pass


class ContactNumberResponse(BaseSchema):
    pass


class IntegrationTypeResponse(BaseSchema):
    pass


class DocumentsResponse(BaseSchema):
    pass


class CreatedByResponse(BaseSchema):
    pass


class ModifiedByResponse(BaseSchema):
    pass


class AddressResponse(BaseSchema):
    pass


class EinvoiceResponse(BaseSchema):
    pass


class EwayBillResponse(BaseSchema):
    pass


class GstCredentialsResponse(BaseSchema):
    pass


class WarningsResponse(BaseSchema):
    pass


class ItemResponse(BaseSchema):
    pass


class GetStoresViewResponse(BaseSchema):
    pass


class ReAssignStoreRequest(BaseSchema):
    pass


class ReAssignStoreResponse(BaseSchema):
    pass


class ApplicationCompanyDpViewResponse(BaseSchema):
    pass


class ApplicationCompanyDpViewRequest(BaseSchema):
    pass


class PincodeMopData(BaseSchema):
    pass


class PincodeMopUpdateResponse(BaseSchema):
    pass


class PincodeMOPresponse(BaseSchema):
    pass


class CommonError(BaseSchema):
    pass


class PincodeMopBulkData(BaseSchema):
    pass


class PincodeBulkViewResponse(BaseSchema):
    pass


class PincodeCodStatusListingRequest(BaseSchema):
    pass


class PincodeCodStatusListingResponse(BaseSchema):
    pass


class Error(BaseSchema):
    pass


class PincodeCodStatusListingPage(BaseSchema):
    pass


class PincodeCodStatusListingSummary(BaseSchema):
    pass


class PincodeMopUpdateAuditHistoryRequest(BaseSchema):
    pass


class PincodeMopUpdateAuditHistoryPaging(BaseSchema):
    pass


class PincodeMopUpdateAuditHistoryResponse(BaseSchema):
    pass


class PincodeMopUpdateAuditHistoryResponseData(BaseSchema):
    pass


class Page(BaseSchema):
    pass


class Dp1(BaseSchema):
    pass


class CompanyDpAccountListResponse(BaseSchema):
    pass


class ErrorResponse(BaseSchema):
    pass


class DpAccountFailureResponse(BaseSchema):
    pass


class CompanyDpAccountRequest(BaseSchema):
    pass


class CompanyDpAccountResponse(BaseSchema):
    pass


class DpSchemaInRuleListing(BaseSchema):
    pass


class DpRule(BaseSchema):
    pass


class DpRuleSuccessResponse(BaseSchema):
    pass


class FailureResponse(BaseSchema):
    pass


class DpRulesUpdateRequest(BaseSchema):
    pass


class DpRuleResponse(BaseSchema):
    pass


class DpRuleUpdateSuccessResponse(BaseSchema):
    pass


class DpMultipleRuleSuccessResponse(BaseSchema):
    pass


class DpIds(BaseSchema):
    pass


class DpRuleRequest(BaseSchema):
    pass


class DPCompanyRuleResponse(BaseSchema):
    pass


class DPCompanyRuleRequest(BaseSchema):
    pass


class DPApplicationRuleResponse(BaseSchema):
    pass


class DPApplicationRuleRequest(BaseSchema):
    pass


class SelfShipResponse(BaseSchema):
    pass


class ApplicationSelfShipConfig(BaseSchema):
    pass


class ApplicationSelfShipConfigResponse(BaseSchema):
    pass





class ServiceabilityErrorResponse(BaseSchema):
    # Serviceability swagger.json

    
    value = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    message = fields.Str(required=False)
    


class ApplicationServiceabilityConfig(BaseSchema):
    # Serviceability swagger.json

    
    serviceability_type = fields.Str(required=False)
    
    channel_id = fields.Str(required=False)
    
    channel_type = fields.Str(required=False)
    


class ApplicationServiceabilityConfigResponse(BaseSchema):
    # Serviceability swagger.json

    
    success = fields.Boolean(required=False)
    
    error = fields.Nested(ServiceabilityErrorResponse, required=False)
    
    data = fields.Nested(ApplicationServiceabilityConfig, required=False)
    


class EntityRegionView_Request(BaseSchema):
    # Serviceability swagger.json

    
    sub_type = fields.List(fields.Str(required=False), required=False)
    
    parent_id = fields.List(fields.Str(required=False), required=False)
    


class EntityRegionView_page(BaseSchema):
    # Serviceability swagger.json

    
    item_total = fields.Int(required=False)
    
    size = fields.Int(required=False)
    
    has_next = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    
    current = fields.Int(required=False)
    


class EntityRegionView_Error(BaseSchema):
    # Serviceability swagger.json

    
    value = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    message = fields.Str(required=False)
    


class EntityRegionView_Items(BaseSchema):
    # Serviceability swagger.json

    
    uid = fields.Str(required=False)
    
    sub_type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    


class EntityRegionView_Response(BaseSchema):
    # Serviceability swagger.json

    
    page = fields.Nested(EntityRegionView_page, required=False)
    
    success = fields.Boolean(required=False)
    
    error = fields.Nested(EntityRegionView_Error, required=False)
    
    data = fields.List(fields.Nested(EntityRegionView_Items, required=False), required=False)
    


class ZoneDataItem(BaseSchema):
    # Serviceability swagger.json

    
    type = fields.Str(required=False)
    
    item_total = fields.Int(required=False)
    
    size = fields.Int(required=False)
    
    has_next = fields.Boolean(required=False)
    
    current = fields.Int(required=False)
    


class ListViewSummary(BaseSchema):
    # Serviceability swagger.json

    
    total_zones = fields.Int(required=False)
    
    total_active_zones = fields.Int(required=False)
    
    total_pincodes_served = fields.Int(required=False)
    


class ListViewChannels(BaseSchema):
    # Serviceability swagger.json

    
    channel_id = fields.Str(required=False)
    
    channel_type = fields.Str(required=False)
    


class ListViewProduct(BaseSchema):
    # Serviceability swagger.json

    
    type = fields.Str(required=False)
    
    count = fields.Int(required=False)
    


class ListViewItems(BaseSchema):
    # Serviceability swagger.json

    
    slug = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    pincodes_count = fields.Int(required=False)
    
    zone_id = fields.Str(required=False)
    
    channels = fields.Nested(ListViewChannels, required=False)
    
    company_id = fields.Int(required=False)
    
    stores_count = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    product = fields.Nested(ListViewProduct, required=False)
    


class ListViewResponse(BaseSchema):
    # Serviceability swagger.json

    
    page = fields.List(fields.Nested(ZoneDataItem, required=False), required=False)
    
    summary = fields.List(fields.Nested(ListViewSummary, required=False), required=False)
    
    items = fields.List(fields.Nested(ListViewItems, required=False), required=False)
    


class CompanyStoreView_PageItems(BaseSchema):
    # Serviceability swagger.json

    
    item_total = fields.Int(required=False)
    
    size = fields.Int(required=False)
    
    has_next = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    
    current = fields.Int(required=False)
    


class CompanyStoreView_Response(BaseSchema):
    # Serviceability swagger.json

    
    page = fields.List(fields.Nested(CompanyStoreView_PageItems, required=False), required=False)
    
    items = fields.List(fields.Dict(required=False), required=False)
    


class GetZoneDataViewChannels(BaseSchema):
    # Serviceability swagger.json

    
    channel_id = fields.Str(required=False)
    
    channel_type = fields.Str(required=False)
    


class ZoneProductTypes(BaseSchema):
    # Serviceability swagger.json

    
    type = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    


class ZoneMappingType(BaseSchema):
    # Serviceability swagger.json

    
    country = fields.Str(required=False)
    
    pincode = fields.List(fields.Str(required=False), required=False)
    
    state = fields.List(fields.Str(required=False), required=False)
    


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

    
    identifier = fields.Str(required=False)
    
    data = fields.Nested(UpdateZoneData, required=False)
    


class ZoneSuccessResponse(BaseSchema):
    # Serviceability swagger.json

    
    success = fields.Boolean(required=False)
    
    status_code = fields.Int(required=False)
    


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

    
    identifier = fields.Str(required=False)
    
    data = fields.Nested(CreateZoneData, required=False)
    


class ZoneResponse(BaseSchema):
    # Serviceability swagger.json

    
    success = fields.Boolean(required=False)
    
    status_code = fields.Int(required=False)
    
    zone_id = fields.Str(required=False)
    


class GetZoneFromApplicationIdViewResponse(BaseSchema):
    # Serviceability swagger.json

    
    page = fields.List(fields.Nested(ZoneDataItem, required=False), required=False)
    
    items = fields.List(fields.Nested(ListViewItems, required=False), required=False)
    


class GetZoneFromPincodeViewRequest(BaseSchema):
    # Serviceability swagger.json

    
    country = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    


class GetZoneFromPincodeViewResponse(BaseSchema):
    # Serviceability swagger.json

    
    zones = fields.List(fields.Str(required=False), required=False)
    
    serviceability_type = fields.Str(required=False)
    


class ServiceabilityPageResponse(BaseSchema):
    # Serviceability swagger.json

    
    item_total = fields.Int(required=False)
    
    size = fields.Int(required=False)
    
    has_next = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    
    current = fields.Int(required=False)
    


class OpeningClosing(BaseSchema):
    # Serviceability swagger.json

    
    hour = fields.Int(required=False)
    
    minute = fields.Int(required=False)
    


class TimmingResponse(BaseSchema):
    # Serviceability swagger.json

    
    weekday = fields.Str(required=False)
    
    open = fields.Boolean(required=False)
    
    closing = fields.Nested(OpeningClosing, required=False)
    
    opening = fields.Nested(OpeningClosing, required=False)
    


class MobileNo(BaseSchema):
    # Serviceability swagger.json

    
    country_code = fields.Int(required=False)
    
    number = fields.Str(required=False)
    


class ManagerResponse(BaseSchema):
    # Serviceability swagger.json

    
    email = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    mobile_no = fields.Nested(MobileNo, required=False)
    


class ProductReturnConfigResponse(BaseSchema):
    # Serviceability swagger.json

    
    on_same_store = fields.Boolean(required=False)
    


class Dp(BaseSchema):
    # Serviceability swagger.json

    
    internal_account_id = fields.Str(required=False)
    
    rvp_priority = fields.Int(required=False)
    
    fm_priority = fields.Int(required=False)
    
    operations = fields.List(fields.Str(required=False), required=False)
    
    payment_mode = fields.Str(required=False)
    
    assign_dp_from_sb = fields.Boolean(required=False)
    
    transport_mode = fields.Str(required=False)
    
    external_account_id = fields.Str(required=False)
    
    area_code = fields.Int(required=False)
    
    lm_priority = fields.Int(required=False)
    


class LogisticsResponse(BaseSchema):
    # Serviceability swagger.json

    
    override = fields.Boolean(required=False)
    
    dp = fields.Nested(Dp, required=False)
    


class ContactNumberResponse(BaseSchema):
    # Serviceability swagger.json

    
    country_code = fields.Int(required=False)
    
    number = fields.Str(required=False)
    


class IntegrationTypeResponse(BaseSchema):
    # Serviceability swagger.json

    
    order = fields.Str(required=False)
    
    inventory = fields.Str(required=False)
    


class DocumentsResponse(BaseSchema):
    # Serviceability swagger.json

    
    value = fields.Str(required=False)
    
    verified = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    
    legal_name = fields.Str(required=False)
    


class CreatedByResponse(BaseSchema):
    # Serviceability swagger.json

    
    user_id = fields.Str(required=False)
    
    username = fields.Str(required=False)
    


class ModifiedByResponse(BaseSchema):
    # Serviceability swagger.json

    
    user_id = fields.Str(required=False)
    
    username = fields.Str(required=False)
    


class AddressResponse(BaseSchema):
    # Serviceability swagger.json

    
    latitude = fields.Float(required=False)
    
    city = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    landmark = fields.Str(required=False)
    
    pincode = fields.Int(required=False)
    
    state = fields.Str(required=False)
    
    address2 = fields.Str(required=False)
    
    address1 = fields.Str(required=False)
    
    longitude = fields.Float(required=False)
    


class EinvoiceResponse(BaseSchema):
    # Serviceability swagger.json

    
    enabled = fields.Boolean(required=False)
    


class EwayBillResponse(BaseSchema):
    # Serviceability swagger.json

    
    enabled = fields.Boolean(required=False)
    


class GstCredentialsResponse(BaseSchema):
    # Serviceability swagger.json

    
    e_invoice = fields.Nested(EinvoiceResponse, required=False)
    
    e_waybill = fields.Nested(EwayBillResponse, required=False)
    


class WarningsResponse(BaseSchema):
    # Serviceability swagger.json

    
    store_address = fields.Str(required=False)
    


class ItemResponse(BaseSchema):
    # Serviceability swagger.json

    
    company = fields.Int(required=False)
    
    sub_type = fields.Str(required=False)
    
    timing = fields.List(fields.Nested(TimmingResponse, required=False), required=False)
    
    manager = fields.Nested(ManagerResponse, required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigResponse, required=False)
    
    store_type = fields.Str(required=False)
    
    logistics = fields.Nested(LogisticsResponse, required=False)
    
    contact_numbers = fields.List(fields.Nested(ContactNumberResponse, required=False), required=False)
    
    integration_type = fields.Nested(IntegrationTypeResponse, required=False)
    
    verified_on = fields.Str(required=False)
    
    documents = fields.List(fields.Nested(DocumentsResponse, required=False), required=False)
    
    created_by = fields.Nested(CreatedByResponse, required=False)
    
    created_on = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    display_name = fields.Str(required=False)
    
    modified_by = fields.Nested(ModifiedByResponse, required=False)
    
    name = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    verified_by = fields.Nested(ModifiedByResponse, required=False)
    
    address = fields.Nested(AddressResponse, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    code = fields.Str(required=False)
    
    _cls = fields.Str(required=False)
    
    gst_credentials = fields.Nested(GstCredentialsResponse, required=False)
    
    modified_on = fields.Str(required=False)
    
    warnings = fields.Nested(WarningsResponse, required=False)
    
    stage = fields.Str(required=False)
    


class GetStoresViewResponse(BaseSchema):
    # Serviceability swagger.json

    
    page = fields.Nested(ServiceabilityPageResponse, required=False)
    
    items = fields.List(fields.Nested(ItemResponse, required=False), required=False)
    


class ReAssignStoreRequest(BaseSchema):
    # Serviceability swagger.json

    
    articles = fields.List(fields.Dict(required=False), required=False)
    
    to_pincode = fields.Str(required=False)
    
    ignored_locations = fields.List(fields.Str(required=False), required=False)
    
    identifier = fields.Str(required=False)
    
    configuration = fields.Dict(required=False)
    


class ReAssignStoreResponse(BaseSchema):
    # Serviceability swagger.json

    
    articles = fields.List(fields.Dict(required=False), required=False)
    
    success = fields.Boolean(required=False)
    
    error = fields.Dict(required=False)
    
    to_pincode = fields.Str(required=False)
    


class ApplicationCompanyDpViewResponse(BaseSchema):
    # Serviceability swagger.json

    
    application_id = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    courier_partner_id = fields.Int(required=False)
    
    company_id = fields.Int(required=False)
    


class ApplicationCompanyDpViewRequest(BaseSchema):
    # Serviceability swagger.json

    
    dp_id = fields.Str(required=False)
    


class PincodeMopData(BaseSchema):
    # Serviceability swagger.json

    
    pincodes = fields.List(fields.Int(required=False), required=False)
    
    country = fields.Str(required=False)
    
    action = fields.Str(required=False)
    


class PincodeMopUpdateResponse(BaseSchema):
    # Serviceability swagger.json

    
    pincode = fields.Int(required=False)
    
    channel_id = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    


class PincodeMOPresponse(BaseSchema):
    # Serviceability swagger.json

    
    success = fields.Boolean(required=False)
    
    status_code = fields.Int(required=False)
    
    batch_id = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    action = fields.Str(required=False)
    
    pincodes = fields.List(fields.Int(required=False), required=False)
    
    updated_pincodes = fields.List(fields.Nested(PincodeMopUpdateResponse, required=False), required=False)
    


class CommonError(BaseSchema):
    # Serviceability swagger.json

    
    success = fields.Str(required=False)
    
    status_code = fields.Str(required=False)
    
    error = fields.Raw(required=False)
    


class PincodeMopBulkData(BaseSchema):
    # Serviceability swagger.json

    
    batch_id = fields.Str(required=False)
    
    s3_url = fields.Str(required=False)
    


class PincodeBulkViewResponse(BaseSchema):
    # Serviceability swagger.json

    
    batch_id = fields.Str(required=False)
    
    s3_url = fields.Str(required=False)
    


class PincodeCodStatusListingRequest(BaseSchema):
    # Serviceability swagger.json

    
    country = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    pincode = fields.Int(required=False)
    
    current = fields.Int(required=False)
    
    page_size = fields.Int(required=False)
    


class PincodeCodStatusListingResponse(BaseSchema):
    # Serviceability swagger.json

    
    country = fields.Str(required=False)
    
    data = fields.List(fields.Nested(lambda: PincodeCodStatusListingResponse(exclude=('data')), required=False), required=False)
    
    success = fields.Boolean(required=False)
    
    errors = fields.List(fields.Nested(Error, required=False), required=False)
    
    page = fields.Nested(PincodeCodStatusListingPage, required=False)
    
    summary = fields.Nested(PincodeCodStatusListingSummary, required=False)
    


class Error(BaseSchema):
    # Serviceability swagger.json

    
    type = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    message = fields.Str(required=False)
    


class PincodeCodStatusListingPage(BaseSchema):
    # Serviceability swagger.json

    
    item_total = fields.Int(required=False)
    
    size = fields.Int(required=False)
    
    has_next = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    
    current = fields.Int(required=False)
    


class PincodeCodStatusListingSummary(BaseSchema):
    # Serviceability swagger.json

    
    total_active_pincodes = fields.Int(required=False)
    
    total_inactive_pincodes = fields.Int(required=False)
    


class PincodeMopUpdateAuditHistoryRequest(BaseSchema):
    # Serviceability swagger.json

    
    entity_type = fields.Str(required=False)
    
    file_name = fields.Str(required=False)
    


class PincodeMopUpdateAuditHistoryPaging(BaseSchema):
    # Serviceability swagger.json

    
    type = fields.Str(required=False)
    
    size = fields.Int(required=False)
    
    current = fields.Int(required=False)
    
    has_next = fields.Boolean(required=False)
    
    item_total = fields.Int(required=False)
    


class PincodeMopUpdateAuditHistoryResponse(BaseSchema):
    # Serviceability swagger.json

    
    batch_id = fields.Str(required=False)
    
    entity_type = fields.Str(required=False)
    
    error_file_s3_url = fields.Str(required=False)
    
    s3_url = fields.Str(required=False)
    
    file_name = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    updated_by = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class PincodeMopUpdateAuditHistoryResponseData(BaseSchema):
    # Serviceability swagger.json

    
    entity_type = fields.Str(required=False)
    
    page = fields.Nested(PincodeMopUpdateAuditHistoryPaging, required=False)
    
    data = fields.List(fields.Nested(PincodeMopUpdateAuditHistoryResponse, required=False), required=False)
    


class Page(BaseSchema):
    # Serviceability swagger.json

    
    item_total = fields.Int(required=False)
    
    next_id = fields.Str(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    has_next = fields.Boolean(required=False)
    
    current = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    size = fields.Int(required=False)
    


class Dp1(BaseSchema):
    # Serviceability swagger.json

    
    plan_id = fields.Str(required=False)
    
    is_self_ship = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    dp_id = fields.Str(required=False)
    
    account_id = fields.Str(required=False)
    
    plan_rules = fields.Dict(required=False)
    
    stage = fields.Str(required=False)
    


class CompanyDpAccountListResponse(BaseSchema):
    # Serviceability swagger.json

    
    page = fields.Nested(Page, required=False)
    
    success = fields.Boolean(required=False)
    
    items = fields.List(fields.Nested(Dp1, required=False), required=False)
    


class ErrorResponse(BaseSchema):
    # Serviceability swagger.json

    
    value = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    message = fields.Str(required=False)
    


class DpAccountFailureResponse(BaseSchema):
    # Serviceability swagger.json

    
    success = fields.Boolean(required=False)
    
    status_code = fields.Int(required=False)
    
    error = fields.List(fields.Nested(ErrorResponse, required=False), required=False)
    


class CompanyDpAccountRequest(BaseSchema):
    # Serviceability swagger.json

    
    data = fields.List(fields.Nested(Dp1, required=False), required=False)
    


class CompanyDpAccountResponse(BaseSchema):
    # Serviceability swagger.json

    
    success = fields.Boolean(required=False)
    


class DpSchemaInRuleListing(BaseSchema):
    # Serviceability swagger.json

    
    plan_id = fields.Str(required=False)
    
    is_self_ship = fields.Boolean(required=False)
    
    priority = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    dp_id = fields.Str(required=False)
    
    account_id = fields.Str(required=False)
    
    plan_rules = fields.Dict(required=False)
    
    stage = fields.Str(required=False)
    


class DpRule(BaseSchema):
    # Serviceability swagger.json

    
    name = fields.Str(required=False)
    
    dp_ids = fields.Dict(required=False)
    
    company_id = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    conditions = fields.List(fields.Dict(required=False), required=False)
    


class DpRuleSuccessResponse(BaseSchema):
    # Serviceability swagger.json

    
    success = fields.Boolean(required=False)
    
    status_code = fields.Int(required=False)
    
    data = fields.Nested(DpRule, required=False)
    


class FailureResponse(BaseSchema):
    # Serviceability swagger.json

    
    success = fields.Boolean(required=False)
    
    status_code = fields.Int(required=False)
    
    error = fields.List(fields.Nested(ErrorResponse, required=False), required=False)
    


class DpRulesUpdateRequest(BaseSchema):
    # Serviceability swagger.json

    
    dp_ids = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    conditions = fields.List(fields.Dict(required=False), required=False)
    


class DpRuleResponse(BaseSchema):
    # Serviceability swagger.json

    
    modified_by = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    created_by = fields.Dict(required=False)
    
    dp_ids = fields.Dict(required=False)
    
    company_id = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    conditions = fields.List(fields.Str(required=False), required=False)
    


class DpRuleUpdateSuccessResponse(BaseSchema):
    # Serviceability swagger.json

    
    success = fields.Boolean(required=False)
    
    status_code = fields.Int(required=False)
    
    data = fields.Nested(DpRuleResponse, required=False)
    


class DpMultipleRuleSuccessResponse(BaseSchema):
    # Serviceability swagger.json

    
    page = fields.Nested(Page, required=False)
    
    success = fields.Boolean(required=False)
    
    items = fields.List(fields.Nested(DpRule, required=False), required=False)
    


class DpIds(BaseSchema):
    # Serviceability swagger.json

    
    enabled = fields.Boolean(required=False)
    
    priority = fields.Int(required=False)
    
    meta = fields.Dict(required=False)
    


class DpRuleRequest(BaseSchema):
    # Serviceability swagger.json

    
    name = fields.Str(required=False)
    
    dp_ids = fields.Dict(required=False)
    
    company_id = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    conditions = fields.List(fields.Dict(required=False), required=False)
    


class DPCompanyRuleResponse(BaseSchema):
    # Serviceability swagger.json

    
    success = fields.Boolean(required=False)
    
    status_code = fields.Int(required=False)
    
    data = fields.List(fields.Nested(DpRuleResponse, required=False), required=False)
    


class DPCompanyRuleRequest(BaseSchema):
    # Serviceability swagger.json

    
    rule_ids = fields.List(fields.Str(required=False), required=False)
    


class DPApplicationRuleResponse(BaseSchema):
    # Serviceability swagger.json

    
    success = fields.Boolean(required=False)
    
    status_code = fields.Boolean(required=False)
    
    data = fields.List(fields.Nested(DpRuleResponse, required=False), required=False)
    


class DPApplicationRuleRequest(BaseSchema):
    # Serviceability swagger.json

    
    shipping_rules = fields.List(fields.Str(required=False), required=False)
    


class SelfShipResponse(BaseSchema):
    # Serviceability swagger.json

    
    active = fields.Boolean(required=False)
    
    tat = fields.Float(required=False)
    


class ApplicationSelfShipConfig(BaseSchema):
    # Serviceability swagger.json

    
    self_ship = fields.Nested(SelfShipResponse, required=False)
    


class ApplicationSelfShipConfigResponse(BaseSchema):
    # Serviceability swagger.json

    
    success = fields.Boolean(required=False)
    
    error = fields.Nested(ServiceabilityErrorResponse, required=False)
    
    id = fields.Str(required=False)
    
    self_ship = fields.Nested(ApplicationSelfShipConfig, required=False)
    


