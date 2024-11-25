"""Serviceability Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




class UpdateZoneConfigDetails(BaseSchema):
    pass


class ServiceabilityErrorResult(BaseSchema):
    pass


class ApplicationServiceabilityConfig(BaseSchema):
    pass


class ApplicationServiceabilityConfigResult(BaseSchema):
    pass


class EntityRegionView_Details(BaseSchema):
    pass


class EntityRegionView_Error(BaseSchema):
    pass


class EntityRegionView_page(BaseSchema):
    pass


class getAppRegionZonesResult(BaseSchema):
    pass


class PageSchema(BaseSchema):
    pass


class EntityRegionView_Items(BaseSchema):
    pass


class EntityRegionView_Result(BaseSchema):
    pass


class ListViewSummary(BaseSchema):
    pass


class ZoneDataItem(BaseSchema):
    pass


class ListViewProduct(BaseSchema):
    pass


class ListViewChannels(BaseSchema):
    pass


class ListViewItems(BaseSchema):
    pass


class ListViewResult(BaseSchema):
    pass


class CompanyStoreView_PageItems(BaseSchema):
    pass


class CompanyStoreView_Result(BaseSchema):
    pass


class GetZoneDataViewChannels(BaseSchema):
    pass


class ZoneProductTypes(BaseSchema):
    pass


class ZoneMappingDetailType(BaseSchema):
    pass


class ZoneMappingType(BaseSchema):
    pass


class ZoneMappingRegions(BaseSchema):
    pass


class UpdateZoneData(BaseSchema):
    pass


class ZoneUpdateDetails(BaseSchema):
    pass


class ZoneSuccessResult(BaseSchema):
    pass


class GetZoneDataViewItems(BaseSchema):
    pass


class GetSingleZoneDataViewResult(BaseSchema):
    pass


class GetZoneByIdSchema(BaseSchema):
    pass


class CreateZoneData(BaseSchema):
    pass


class ZoneResult(BaseSchema):
    pass


class GetZoneFromPincodeViewDetails(BaseSchema):
    pass


class Zone(BaseSchema):
    pass


class GetZoneFromPincodeViewResult(BaseSchema):
    pass


class GetZoneFromApplicationIdViewResult(BaseSchema):
    pass


class ServiceabilityPageResult(BaseSchema):
    pass


class MobileNo(BaseSchema):
    pass


class ManagerResult(BaseSchema):
    pass


class ModifiedByResult(BaseSchema):
    pass


class IntegrationTypeResult(BaseSchema):
    pass


class ProductReturnConfigResult(BaseSchema):
    pass


class ContactNumberResult(BaseSchema):
    pass


class AddressResult(BaseSchema):
    pass


class CreatedByResult(BaseSchema):
    pass


class EwayBillResult(BaseSchema):
    pass


class EinvoiceResult(BaseSchema):
    pass


class GstCredentialsResult(BaseSchema):
    pass


class WarningsResult(BaseSchema):
    pass


class OpeningClosing(BaseSchema):
    pass


class TimmingResult(BaseSchema):
    pass


class DocumentsResult(BaseSchema):
    pass


class Dp(BaseSchema):
    pass


class LogisticsResult(BaseSchema):
    pass


class ItemResult(BaseSchema):
    pass


class GetStoresViewResult(BaseSchema):
    pass


class PincodeMopData(BaseSchema):
    pass


class PincodeMopUpdateResult(BaseSchema):
    pass


class PincodeMOPResult(BaseSchema):
    pass


class CommonError(BaseSchema):
    pass


class PincodeMopBulkData(BaseSchema):
    pass


class PincodeBulkViewResult(BaseSchema):
    pass


class PincodeCodStatusListingDetails(BaseSchema):
    pass


class PincodeCodStatusItem(BaseSchema):
    pass


class PincodeCodStatusListingResult(BaseSchema):
    pass


class Error(BaseSchema):
    pass


class PincodeCodStatusListingPage(BaseSchema):
    pass


class PincodeCodStatusListingSummary(BaseSchema):
    pass


class PincodeMopUpdateAuditHistoryDetails(BaseSchema):
    pass


class PincodeMopUpdateAuditHistoryPaging(BaseSchema):
    pass


class PincodeMopUpdateAuditHistoryResult(BaseSchema):
    pass


class PincodeMopUpdateAuditHistoryResultData(BaseSchema):
    pass


class ArithmeticOperations(BaseSchema):
    pass


class SchemeRulesFeatures(BaseSchema):
    pass


class SchemeRules(BaseSchema):
    pass


class CourierAccountUpdateDetails(BaseSchema):
    pass


class CourierAccount(BaseSchema):
    pass


class CourierAccountDetailsBody(BaseSchema):
    pass


class ErrorResult(BaseSchema):
    pass


class CourierPartnerAccountFailureResult(BaseSchema):
    pass


class Page(BaseSchema):
    pass


class CourierPartnerRuleCPListResult(BaseSchema):
    pass


class CourierPartnerRuleResult(BaseSchema):
    pass


class CourierPartnerList(BaseSchema):
    pass


class LocationRuleValues(BaseSchema):
    pass


class LocationRule(BaseSchema):
    pass


class StringComparisonOperations(BaseSchema):
    pass


class IntComparisonOperations(BaseSchema):
    pass


class CourierPartnerRuleConditions(BaseSchema):
    pass


class CourierPartnerRule(BaseSchema):
    pass


class FailureResult(BaseSchema):
    pass


class CourierPartnerRulesListResult(BaseSchema):
    pass


class ShipmentsArticles(BaseSchema):
    pass


class ShipmentDimension(BaseSchema):
    pass


class Shipments(BaseSchema):
    pass


class ShipmentCourierPartnerDetails(BaseSchema):
    pass


class CourierPartnerPromise(BaseSchema):
    pass


class CourierPartners(BaseSchema):
    pass


class ShipmentCourierPartners(BaseSchema):
    pass


class ShipmentCourierPartnerResult(BaseSchema):
    pass


class ShipmentsCourierPartnersServiceability(BaseSchema):
    pass


class CompanyConfig(BaseSchema):
    pass


class ZoneConfig(BaseSchema):
    pass


class ApplicationConfig(BaseSchema):
    pass


class BulkRegionJobDetails(BaseSchema):
    pass


class BulkRegionResultItemData(BaseSchema):
    pass


class BulkRegionResult(BaseSchema):
    pass


class SelfShipResult(BaseSchema):
    pass


class ApplicationSelfShipConfig(BaseSchema):
    pass


class ApplicationSelfShipConfigResult(BaseSchema):
    pass


class StoreRuleConfigData(BaseSchema):
    pass


class CustomerRadiusSchema(BaseSchema):
    pass


class StoreRuleConditionSchema(BaseSchema):
    pass


class StoreRuleDataSchema(BaseSchema):
    pass


class StorePrioritySchema(BaseSchema):
    pass


class GetStoreRulesApiResult(BaseSchema):
    pass


class CreateStoreRuleDetailsSchema(BaseSchema):
    pass


class StoreRuleResultSchema(BaseSchema):
    pass


class StoreRuleUpdateResultSchema(BaseSchema):
    pass


class ServiceabilityModel(BaseSchema):
    pass


class CourierPartnerSchemeFeatures(BaseSchema):
    pass


class CourierPartnerSchemeModel(BaseSchema):
    pass


class CourierAccountResult(BaseSchema):
    pass


class CompanyCourierPartnerAccountListResult(BaseSchema):
    pass


class PackageMaterial(BaseSchema):
    pass


class PackageMaterialResult(BaseSchema):
    pass


class PackageMaterialRule(BaseSchema):
    pass


class PackageRule(BaseSchema):
    pass


class PackageRuleResult(BaseSchema):
    pass


class Channel(BaseSchema):
    pass


class PackageMaterialRuleList(BaseSchema):
    pass


class PackageMaterialList(BaseSchema):
    pass


class PackageRuleProduct(BaseSchema):
    pass


class PackageRuleProductTag(BaseSchema):
    pass


class PackageRuleCategory(BaseSchema):
    pass


class PackageMaterialRuleQuantity(BaseSchema):
    pass


class RulePriorityDetails(BaseSchema):
    pass


class RulePriorityResult(BaseSchema):
    pass


class ArticleAssignment(BaseSchema):
    pass


class ServiceabilityLocation(BaseSchema):
    pass


class LocationDetailsServiceability(BaseSchema):
    pass


class OptimalLocationsArticles(BaseSchema):
    pass


class OptimlLocationsDetailsSchema(BaseSchema):
    pass


class OptimalLocationArticlesResult(BaseSchema):
    pass


class OptimalLocationAssignedStoresResult(BaseSchema):
    pass


class OptimalLocationsResult(BaseSchema):
    pass


class ValidationError(BaseSchema):
    pass


class StandardError(BaseSchema):
    pass


class CourierPartnerSchemeV2Features(BaseSchema):
    pass


class CourierPartnerSchemeV2DetailsModel(BaseSchema):
    pass


class CourierPartnerV2SchemeModel(BaseSchema):
    pass


class CourierPartnerSchemeV2UpdateDetails(BaseSchema):
    pass


class courierPartnerSchemeV2List(BaseSchema):
    pass


class BulkRegionServiceabilityTatDetails(BaseSchema):
    pass


class BulkRegionServiceabilityTatResultItemData(BaseSchema):
    pass


class BulkRegionServiceabilityTatResult(BaseSchema):
    pass


class HierarchyItems(BaseSchema):
    pass


class GetCountriesItems(BaseSchema):
    pass


class GetCountries(BaseSchema):
    pass





class UpdateZoneConfigDetails(BaseSchema):
    # Serviceability swagger.json

    
    serviceability_type = fields.Str(required=False)
    


class ServiceabilityErrorResult(BaseSchema):
    # Serviceability swagger.json

    
    message = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class ApplicationServiceabilityConfig(BaseSchema):
    # Serviceability swagger.json

    
    channel_id = fields.Str(required=False)
    
    serviceability_type = fields.Str(required=False)
    
    channel_type = fields.Str(required=False)
    


class ApplicationServiceabilityConfigResult(BaseSchema):
    # Serviceability swagger.json

    
    error = fields.Nested(ServiceabilityErrorResult, required=False)
    
    data = fields.Nested(ApplicationServiceabilityConfig, required=False)
    
    success = fields.Boolean(required=False)
    


class EntityRegionView_Details(BaseSchema):
    # Serviceability swagger.json

    
    sub_type = fields.List(fields.Str(required=False), required=False)
    
    parent_id = fields.List(fields.Str(required=False), required=False)
    


class EntityRegionView_Error(BaseSchema):
    # Serviceability swagger.json

    
    message = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class EntityRegionView_page(BaseSchema):
    # Serviceability swagger.json

    
    type = fields.Str(required=False)
    
    has_next = fields.Boolean(required=False)
    
    item_total = fields.Int(required=False)
    
    size = fields.Int(required=False)
    
    current = fields.Int(required=False)
    


class getAppRegionZonesResult(BaseSchema):
    # Serviceability swagger.json

    
    page = fields.List(fields.Nested(PageSchema, required=False), required=False)
    
    items = fields.List(fields.Nested(ListViewItems, required=False), required=False)
    


class PageSchema(BaseSchema):
    # Serviceability swagger.json

    
    has_next = fields.Boolean(required=False)
    
    item_total = fields.Int(required=False)
    
    size = fields.Int(required=False)
    
    current = fields.Int(required=False)
    
    type = fields.Str(required=False)
    


class EntityRegionView_Items(BaseSchema):
    # Serviceability swagger.json

    
    sub_type = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    name = fields.Str(required=False)
    


class EntityRegionView_Result(BaseSchema):
    # Serviceability swagger.json

    
    error = fields.Nested(EntityRegionView_Error, required=False)
    
    page = fields.Nested(EntityRegionView_page, required=False)
    
    data = fields.List(fields.Nested(EntityRegionView_Items, required=False), required=False)
    
    success = fields.Boolean(required=False)
    


class ListViewSummary(BaseSchema):
    # Serviceability swagger.json

    
    total_zones = fields.Int(required=False)
    
    total_pincodes_served = fields.Int(required=False)
    
    total_active_zones = fields.Int(required=False)
    


class ZoneDataItem(BaseSchema):
    # Serviceability swagger.json

    
    has_next = fields.Boolean(required=False)
    
    item_total = fields.Int(required=False)
    
    size = fields.Int(required=False)
    
    current = fields.Int(required=False)
    
    type = fields.Str(required=False)
    


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

    
    zone_id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    stores_count = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    regions_count = fields.Int(required=False)
    
    company_id = fields.Int(required=False)
    
    store_ids = fields.List(fields.Int(required=False), required=False)
    
    channels = fields.List(fields.Nested(ListViewChannels, required=False), required=False)
    


class ListViewResult(BaseSchema):
    # Serviceability swagger.json

    
    page = fields.Nested(ZoneDataItem, required=False)
    
    items = fields.List(fields.Nested(ListViewItems, required=False), required=False)
    


class CompanyStoreView_PageItems(BaseSchema):
    # Serviceability swagger.json

    
    type = fields.Str(required=False)
    
    has_next = fields.Boolean(required=False)
    
    item_total = fields.Int(required=False)
    
    size = fields.Int(required=False)
    
    current = fields.Int(required=False)
    


class CompanyStoreView_Result(BaseSchema):
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
    


class ZoneMappingDetailType(BaseSchema):
    # Serviceability swagger.json

    
    country = fields.Str(required=False)
    
    regions = fields.List(fields.Nested(ZoneMappingRegions, required=False), required=False)
    


class ZoneMappingType(BaseSchema):
    # Serviceability swagger.json

    
    country = fields.Str(required=False)
    
    regions = fields.List(fields.Str(required=False), required=False)
    


class ZoneMappingRegions(BaseSchema):
    # Serviceability swagger.json

    
    display_name = fields.Str(required=False)
    
    parent_id = fields.List(fields.Str(required=False), required=False)
    
    parent_uid = fields.Str(required=False)
    
    sub_type = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    


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
    


class ZoneUpdateDetails(BaseSchema):
    # Serviceability swagger.json

    
    identifier = fields.Str(required=False)
    
    data = fields.Nested(UpdateZoneData, required=False)
    


class ZoneSuccessResult(BaseSchema):
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
    


class GetSingleZoneDataViewResult(BaseSchema):
    # Serviceability swagger.json

    
    data = fields.Nested(GetZoneDataViewItems, required=False)
    


class GetZoneByIdSchema(BaseSchema):
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
    
    mapping = fields.List(fields.Nested(ZoneMappingDetailType, required=False), required=False)
    
    stores_count = fields.Int(required=False)
    


class CreateZoneData(BaseSchema):
    # Serviceability swagger.json

    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    channels = fields.List(fields.Nested(GetZoneDataViewChannels, required=False), required=False)
    
    store_ids = fields.List(fields.Int(required=False), required=False)
    
    region_type = fields.Str(required=False)
    
    mapping = fields.List(fields.Nested(ZoneMappingType, required=False), required=False)
    
    product = fields.Nested(ZoneProductTypes, required=False)
    


class ZoneResult(BaseSchema):
    # Serviceability swagger.json

    
    status_code = fields.Int(required=False)
    
    zone_id = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class GetZoneFromPincodeViewDetails(BaseSchema):
    # Serviceability swagger.json

    
    country = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    


class Zone(BaseSchema):
    # Serviceability swagger.json

    
    zone_id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    slug = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    store_ids = fields.List(fields.Int(required=False), required=False)
    


class GetZoneFromPincodeViewResult(BaseSchema):
    # Serviceability swagger.json

    
    serviceability_type = fields.Str(required=False)
    
    zones = fields.List(fields.Nested(Zone, required=False), required=False)
    


class GetZoneFromApplicationIdViewResult(BaseSchema):
    # Serviceability swagger.json

    
    page = fields.List(fields.Nested(ZoneDataItem, required=False), required=False)
    
    items = fields.List(fields.Nested(ListViewItems, required=False), required=False)
    


class ServiceabilityPageResult(BaseSchema):
    # Serviceability swagger.json

    
    type = fields.Str(required=False)
    
    has_next = fields.Boolean(required=False)
    
    item_total = fields.Int(required=False)
    
    size = fields.Int(required=False)
    
    current = fields.Int(required=False)
    


class MobileNo(BaseSchema):
    # Serviceability swagger.json

    
    number = fields.Str(required=False)
    
    country_code = fields.Int(required=False)
    


class ManagerResult(BaseSchema):
    # Serviceability swagger.json

    
    email = fields.Str(required=False)
    
    mobile_no = fields.Nested(MobileNo, required=False)
    
    name = fields.Str(required=False)
    


class ModifiedByResult(BaseSchema):
    # Serviceability swagger.json

    
    username = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    


class IntegrationTypeResult(BaseSchema):
    # Serviceability swagger.json

    
    inventory = fields.Str(required=False)
    
    order = fields.Str(required=False)
    


class ProductReturnConfigResult(BaseSchema):
    # Serviceability swagger.json

    
    on_same_store = fields.Boolean(required=False)
    


class ContactNumberResult(BaseSchema):
    # Serviceability swagger.json

    
    number = fields.Str(required=False)
    
    country_code = fields.Int(required=False)
    


class AddressResult(BaseSchema):
    # Serviceability swagger.json

    
    city = fields.Str(required=False)
    
    address1 = fields.Str(required=False)
    
    pincode = fields.Int(required=False)
    
    address2 = fields.Str(required=False)
    
    landmark = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    latitude = fields.Float(required=False)
    
    longitude = fields.Float(required=False)
    


class CreatedByResult(BaseSchema):
    # Serviceability swagger.json

    
    username = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    


class EwayBillResult(BaseSchema):
    # Serviceability swagger.json

    
    enabled = fields.Boolean(required=False)
    


class EinvoiceResult(BaseSchema):
    # Serviceability swagger.json

    
    enabled = fields.Boolean(required=False)
    


class GstCredentialsResult(BaseSchema):
    # Serviceability swagger.json

    
    e_waybill = fields.Nested(EwayBillResult, required=False)
    
    e_invoice = fields.Nested(EinvoiceResult, required=False)
    


class WarningsResult(BaseSchema):
    # Serviceability swagger.json

    
    store_address = fields.Str(required=False)
    


class OpeningClosing(BaseSchema):
    # Serviceability swagger.json

    
    minute = fields.Int(required=False)
    
    hour = fields.Int(required=False)
    


class TimmingResult(BaseSchema):
    # Serviceability swagger.json

    
    open = fields.Boolean(required=False)
    
    weekday = fields.Str(required=False)
    
    closing = fields.Nested(OpeningClosing, required=False)
    
    opening = fields.Nested(OpeningClosing, required=False)
    


class DocumentsResult(BaseSchema):
    # Serviceability swagger.json

    
    legal_name = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    verified = fields.Boolean(required=False)
    


class Dp(BaseSchema):
    # Serviceability swagger.json

    
    fm_priority = fields.Int(required=False)
    
    rvp_priority = fields.Int(required=False)
    
    lm_priority = fields.Int(required=False)
    
    internal_account_id = fields.Str(required=False)
    
    area_code = fields.Int(required=False, allow_none=True)
    
    payment_mode = fields.Str(required=False)
    
    operations = fields.List(fields.Str(required=False), required=False)
    
    external_account_id = fields.Str(required=False, allow_none=True)
    
    transport_mode = fields.Str(required=False)
    
    assign_dp_from_sb = fields.Boolean(required=False)
    


class LogisticsResult(BaseSchema):
    # Serviceability swagger.json

    
    override = fields.Boolean(required=False)
    
    dp = fields.Nested(Dp, required=False)
    


class ItemResult(BaseSchema):
    # Serviceability swagger.json

    
    created_on = fields.Str(required=False)
    
    manager = fields.Nested(ManagerResult, required=False)
    
    modified_by = fields.Nested(ModifiedByResult, required=False)
    
    integration_type = fields.Nested(IntegrationTypeResult, required=False)
    
    verified_on = fields.Str(required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigResult, required=False)
    
    contact_numbers = fields.List(fields.Nested(ContactNumberResult, required=False), required=False)
    
    verified_by = fields.Nested(ModifiedByResult, required=False)
    
    stage = fields.Str(required=False)
    
    address = fields.Nested(AddressResult, required=False)
    
    modified_on = fields.Str(required=False)
    
    created_by = fields.Nested(CreatedByResult, required=False)
    
    gst_credentials = fields.Nested(GstCredentialsResult, required=False)
    
    display_name = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    uid = fields.Int(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    code = fields.Str(required=False)
    
    warnings = fields.Nested(WarningsResult, required=False)
    
    name = fields.Str(required=False)
    
    timing = fields.List(fields.Nested(TimmingResult, required=False), required=False)
    
    documents = fields.List(fields.Nested(DocumentsResult, required=False), required=False)
    
    store_type = fields.Str(required=False)
    
    sub_type = fields.Str(required=False)
    
    company = fields.Int(required=False)
    
    _cls = fields.Str(required=False)
    
    logistics = fields.Nested(LogisticsResult, required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    


class GetStoresViewResult(BaseSchema):
    # Serviceability swagger.json

    
    page = fields.Nested(ServiceabilityPageResult, required=False)
    
    items = fields.List(fields.Nested(ItemResult, required=False), required=False)
    


class PincodeMopData(BaseSchema):
    # Serviceability swagger.json

    
    pincodes = fields.List(fields.Int(required=False), required=False)
    
    country = fields.Str(required=False)
    
    action = fields.Str(required=False)
    


class PincodeMopUpdateResult(BaseSchema):
    # Serviceability swagger.json

    
    pincode = fields.Int(required=False)
    
    channel_id = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    


class PincodeMOPResult(BaseSchema):
    # Serviceability swagger.json

    
    success = fields.Boolean(required=False)
    
    status_code = fields.Int(required=False)
    
    batch_id = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    action = fields.Str(required=False)
    
    pincodes = fields.List(fields.Int(required=False), required=False)
    
    updated_pincodes = fields.List(fields.Nested(PincodeMopUpdateResult, required=False), required=False)
    


class CommonError(BaseSchema):
    # Serviceability swagger.json

    
    status_code = fields.Str(required=False)
    
    error = fields.Raw(required=False)
    
    success = fields.Str(required=False)
    


class PincodeMopBulkData(BaseSchema):
    # Serviceability swagger.json

    
    batch_id = fields.Str(required=False)
    
    s3_url = fields.Str(required=False)
    


class PincodeBulkViewResult(BaseSchema):
    # Serviceability swagger.json

    
    batch_id = fields.Str(required=False)
    
    s3_url = fields.Str(required=False)
    


class PincodeCodStatusListingDetails(BaseSchema):
    # Serviceability swagger.json

    
    country = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    pincode = fields.Int(required=False, allow_none=True)
    
    current = fields.Int(required=False)
    
    page_size = fields.Int(required=False)
    


class PincodeCodStatusItem(BaseSchema):
    # Serviceability swagger.json

    
    active = fields.Boolean(required=False)
    
    pincode = fields.Str(required=False)
    


class PincodeCodStatusListingResult(BaseSchema):
    # Serviceability swagger.json

    
    country = fields.Str(required=False)
    
    data = fields.List(fields.Nested(lambda: PincodeCodStatusListingResult(exclude=('data')), required=False), required=False)
    
    success = fields.Boolean(required=False)
    
    errors = fields.List(fields.Nested(Error, required=False), required=False)
    
    page = fields.Nested(PincodeCodStatusListingPage, required=False)
    
    summary = fields.Nested(PincodeCodStatusListingSummary, required=False)
    


class Error(BaseSchema):
    # Serviceability swagger.json

    
    type = fields.Str(required=False, allow_none=True)
    
    value = fields.Str(required=False, allow_none=True)
    
    message = fields.Str(required=False, allow_none=True)
    


class PincodeCodStatusListingPage(BaseSchema):
    # Serviceability swagger.json

    
    type = fields.Str(required=False)
    
    has_next = fields.Boolean(required=False)
    
    item_total = fields.Int(required=False)
    
    size = fields.Int(required=False)
    
    current = fields.Int(required=False)
    


class PincodeCodStatusListingSummary(BaseSchema):
    # Serviceability swagger.json

    
    total_active_pincodes = fields.Int(required=False)
    
    total_inactive_pincodes = fields.Int(required=False)
    


class PincodeMopUpdateAuditHistoryDetails(BaseSchema):
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
    


class PincodeMopUpdateAuditHistoryResult(BaseSchema):
    # Serviceability swagger.json

    
    batch_id = fields.Str(required=False)
    
    entity_type = fields.Str(required=False)
    
    error_file_s3_url = fields.Str(required=False)
    
    s3_url = fields.Str(required=False)
    
    file_name = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    updated_by = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class PincodeMopUpdateAuditHistoryResultData(BaseSchema):
    # Serviceability swagger.json

    
    entity_type = fields.Str(required=False)
    
    page = fields.Nested(PincodeMopUpdateAuditHistoryPaging, required=False)
    
    data = fields.List(fields.Nested(PincodeMopUpdateAuditHistoryResult, required=False), required=False)
    


class ArithmeticOperations(BaseSchema):
    # Serviceability swagger.json

    
    lt = fields.Int(required=False, allow_none=True)
    
    gt = fields.Int(required=False, allow_none=True)
    
    lte = fields.Int(required=False, allow_none=True)
    
    gte = fields.Int(required=False, allow_none=True)
    


class SchemeRulesFeatures(BaseSchema):
    # Serviceability swagger.json

    
    quality_check = fields.Boolean(required=False)
    
    quick_response_code = fields.Boolean(required=False)
    
    e_waybill = fields.Boolean(required=False)
    
    multi_part_shipments = fields.Boolean(required=False)
    
    flammable = fields.Boolean(required=False)
    
    hazmat = fields.Boolean(required=False)
    
    battery_operated = fields.Boolean(required=False)
    


class SchemeRules(BaseSchema):
    # Serviceability swagger.json

    
    weight = fields.Nested(ArithmeticOperations, required=False)
    
    transport_type = fields.List(fields.Str(required=False), required=False)
    
    region = fields.Str(required=False)
    
    payment_mode = fields.List(fields.Str(required=False), required=False)
    
    feature = fields.Nested(SchemeRulesFeatures, required=False)
    


class CourierAccountUpdateDetails(BaseSchema):
    # Serviceability swagger.json

    
    extension_id = fields.Str(required=False)
    
    scheme_id = fields.Str(required=False)
    
    is_self_ship = fields.Boolean(required=False)
    
    stage = fields.Str(required=False)
    
    is_own_account = fields.Boolean(required=False)
    


class CourierAccount(BaseSchema):
    # Serviceability swagger.json

    
    company_id = fields.Int(required=False)
    
    extension_id = fields.Str(required=False)
    
    account_id = fields.Str(required=False)
    
    scheme_id = fields.Str(required=False)
    
    is_self_ship = fields.Boolean(required=False)
    
    stage = fields.Str(required=False)
    
    is_own_account = fields.Boolean(required=False)
    
    scheme_rules = fields.Nested(CourierPartnerSchemeModel, required=False)
    


class CourierAccountDetailsBody(BaseSchema):
    # Serviceability swagger.json

    
    extension_id = fields.Str(required=False)
    
    account_id = fields.Str(required=False)
    
    scheme_id = fields.Str(required=False)
    
    is_self_ship = fields.Boolean(required=False)
    
    stage = fields.Str(required=False)
    
    is_own_account = fields.Boolean(required=False)
    


class ErrorResult(BaseSchema):
    # Serviceability swagger.json

    
    value = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class CourierPartnerAccountFailureResult(BaseSchema):
    # Serviceability swagger.json

    
    success = fields.Boolean(required=False)
    
    error = fields.List(fields.Nested(ErrorResult, required=False), required=False)
    


class Page(BaseSchema):
    # Serviceability swagger.json

    
    item_total = fields.Int(required=False)
    
    next_id = fields.Str(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    has_next = fields.Boolean(required=False)
    
    current = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    size = fields.Int(required=False)
    


class CourierPartnerRuleCPListResult(BaseSchema):
    # Serviceability swagger.json

    
    account_id = fields.Str(required=False)
    
    extension_id = fields.Str(required=False)
    
    is_self_ship = fields.Boolean(required=False)
    
    scheme_rules = fields.Dict(required=False)
    


class CourierPartnerRuleResult(BaseSchema):
    # Serviceability swagger.json

    
    is_active = fields.Boolean(required=False)
    
    application_id = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    conditions = fields.Nested(CourierPartnerRuleConditions, required=False)
    
    sort = fields.List(fields.Str(required=False), required=False)
    
    created_by = fields.Dict(required=False, allow_none=True)
    
    id = fields.Str(required=False)
    
    modified_by = fields.Dict(required=False, allow_none=True)
    
    modified_on = fields.Str(required=False, allow_none=True)
    
    name = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    cp_list = fields.List(fields.Nested(CourierPartnerRuleCPListResult, required=False), required=False)
    


class CourierPartnerList(BaseSchema):
    # Serviceability swagger.json

    
    extension_id = fields.Str(required=False)
    
    account_id = fields.Str(required=False)
    


class LocationRuleValues(BaseSchema):
    # Serviceability swagger.json

    
    id = fields.Str(required=False)
    
    sub_type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    parent_id = fields.List(fields.Str(required=False), required=False)
    
    parent_ids = fields.List(fields.Str(required=False), required=False)
    


class LocationRule(BaseSchema):
    # Serviceability swagger.json

    
    type = fields.Str(required=False)
    
    includes = fields.List(fields.Nested(LocationRuleValues, required=False), required=False)
    


class StringComparisonOperations(BaseSchema):
    # Serviceability swagger.json

    
    includes = fields.List(fields.Str(required=False), required=False)
    


class IntComparisonOperations(BaseSchema):
    # Serviceability swagger.json

    
    includes = fields.List(fields.Int(required=False), required=False)
    


class CourierPartnerRuleConditions(BaseSchema):
    # Serviceability swagger.json

    
    forward = fields.Nested(LocationRule, required=False)
    
    reverse = fields.Nested(LocationRule, required=False)
    
    payment_mode = fields.Nested(StringComparisonOperations, required=False)
    
    category_ids = fields.Nested(IntComparisonOperations, required=False)
    
    product_ids = fields.Nested(IntComparisonOperations, required=False)
    
    product_tags = fields.Nested(StringComparisonOperations, required=False)
    
    zone_ids = fields.Nested(StringComparisonOperations, required=False)
    
    department_ids = fields.Nested(IntComparisonOperations, required=False)
    
    brand_ids = fields.Nested(IntComparisonOperations, required=False)
    
    order_place_date = fields.Nested(ArithmeticOperations, required=False)
    
    store_ids = fields.Nested(IntComparisonOperations, required=False)
    
    store_type = fields.Nested(StringComparisonOperations, required=False)
    
    store_tags = fields.Nested(StringComparisonOperations, required=False)
    
    shipment_weight = fields.Nested(ArithmeticOperations, required=False)
    
    shipment_cost = fields.Nested(ArithmeticOperations, required=False)
    
    shipment_volumetric_weight = fields.Nested(ArithmeticOperations, required=False)
    


class CourierPartnerRule(BaseSchema):
    # Serviceability swagger.json

    
    is_active = fields.Boolean(required=False)
    
    cp_list = fields.List(fields.Nested(CourierPartnerList, required=False), required=False)
    
    name = fields.Str(required=False)
    
    conditions = fields.Nested(CourierPartnerRuleConditions, required=False)
    
    sort = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    


class FailureResult(BaseSchema):
    # Serviceability swagger.json

    
    success = fields.Boolean(required=False)
    
    error = fields.List(fields.Nested(ErrorResult, required=False), required=False)
    


class CourierPartnerRulesListResult(BaseSchema):
    # Serviceability swagger.json

    
    items = fields.List(fields.Nested(CourierPartnerRuleResult, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class ShipmentsArticles(BaseSchema):
    # Serviceability swagger.json

    
    item_id = fields.Int(required=False)
    
    category_id = fields.Int(required=False)
    
    brand_id = fields.Int(required=False)
    
    department_id = fields.Int(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    


class ShipmentDimension(BaseSchema):
    # Serviceability swagger.json

    
    height = fields.Float(required=False)
    
    length = fields.Float(required=False)
    
    width = fields.Float(required=False)
    


class Shipments(BaseSchema):
    # Serviceability swagger.json

    
    id = fields.Str(required=False)
    
    location_id = fields.Float(required=False)
    
    location_tags = fields.List(fields.Str(required=False), required=False)
    
    shipment_weight = fields.Float(required=False)
    
    shipment_volumetric_weight = fields.Float(required=False)
    
    shipment_cost = fields.Float(required=False)
    
    shipment_dimension = fields.Nested(ShipmentDimension, required=False)
    
    courier_partner_schemes = fields.List(fields.Str(required=False), required=False)
    
    articles = fields.List(fields.Nested(ShipmentsArticles, required=False), required=False)
    


class ShipmentCourierPartnerDetails(BaseSchema):
    # Serviceability swagger.json

    
    from_location = fields.Nested(ShipmentsCourierPartnersServiceability, required=False)
    
    to_location = fields.Nested(ShipmentsCourierPartnersServiceability, required=False)
    
    shipments = fields.List(fields.Nested(Shipments, required=False), required=False)
    
    journey = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    


class CourierPartnerPromise(BaseSchema):
    # Serviceability swagger.json

    
    min = fields.Str(required=False)
    
    max = fields.Str(required=False)
    


class CourierPartners(BaseSchema):
    # Serviceability swagger.json

    
    extension_id = fields.Str(required=False)
    
    scheme_id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    delivery_promise = fields.Nested(CourierPartnerPromise, required=False)
    


class ShipmentCourierPartners(BaseSchema):
    # Serviceability swagger.json

    
    id = fields.Str(required=False)
    
    courier_partners = fields.List(fields.Nested(CourierPartners, required=False), required=False)
    


class ShipmentCourierPartnerResult(BaseSchema):
    # Serviceability swagger.json

    
    courier_partners = fields.List(fields.Nested(CourierPartners, required=False), required=False)
    
    shipments = fields.List(fields.Nested(ShipmentCourierPartners, required=False), required=False)
    


class ShipmentsCourierPartnersServiceability(BaseSchema):
    # Serviceability swagger.json

    
    pincode = fields.Str(required=False)
    
    sector_code = fields.Str(required=False)
    
    state_code = fields.Str(required=False)
    
    city_code = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    


class CompanyConfig(BaseSchema):
    # Serviceability swagger.json

    
    rule_ids = fields.List(fields.Str(required=False), required=False)
    
    sort = fields.List(fields.Str(required=False), required=False)
    
    logistics_as_actual = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    application_id = fields.Str(required=False)
    


class ZoneConfig(BaseSchema):
    # Serviceability swagger.json

    
    serviceability_type = fields.Str(required=False)
    
    active_count = fields.Int(required=False)
    
    total_count = fields.Int(required=False)
    


class ApplicationConfig(BaseSchema):
    # Serviceability swagger.json

    
    rule_ids = fields.List(fields.Str(required=False), required=False)
    
    sort = fields.List(fields.Str(required=False), required=False)
    
    zones = fields.Nested(ZoneConfig, required=False)
    


class BulkRegionJobDetails(BaseSchema):
    # Serviceability swagger.json

    
    file_path = fields.Str(required=False, allow_none=True)
    
    country = fields.Str(required=False)
    
    action = fields.Str(required=False)
    
    region = fields.Str(required=False)
    


class BulkRegionResultItemData(BaseSchema):
    # Serviceability swagger.json

    
    file_path = fields.Str(required=False)
    
    failed = fields.Int(required=False)
    
    failed_records = fields.List(fields.Dict(required=False), required=False)
    
    action = fields.Str(required=False)
    
    batch_id = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    success = fields.Int(required=False)
    
    region = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    total = fields.Int(required=False)
    
    error_file_path = fields.Str(required=False)
    


class BulkRegionResult(BaseSchema):
    # Serviceability swagger.json

    
    items = fields.List(fields.Nested(BulkRegionResultItemData, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class SelfShipResult(BaseSchema):
    # Serviceability swagger.json

    
    is_active = fields.Boolean(required=False)
    
    tat = fields.Float(required=False)
    


class ApplicationSelfShipConfig(BaseSchema):
    # Serviceability swagger.json

    
    self_ship = fields.Nested(SelfShipResult, required=False)
    


class ApplicationSelfShipConfigResult(BaseSchema):
    # Serviceability swagger.json

    
    error = fields.Nested(ServiceabilityErrorResult, required=False)
    
    data = fields.Nested(ApplicationSelfShipConfig, required=False)
    
    success = fields.Boolean(required=False)
    


class StoreRuleConfigData(BaseSchema):
    # Serviceability swagger.json

    
    rule_ids = fields.List(fields.Str(required=False), required=False)
    
    type_based_priority = fields.List(fields.Str(required=False), required=False)
    
    tag_based_priority = fields.List(fields.Str(required=False), required=False)
    
    store_priority = fields.List(fields.Nested(StorePrioritySchema, required=False), required=False)
    
    sort = fields.List(fields.Str(required=False), required=False)
    


class CustomerRadiusSchema(BaseSchema):
    # Serviceability swagger.json

    
    unit = fields.Str(required=False)
    
    lt = fields.Int(required=False)
    
    lte = fields.Int(required=False)
    
    gt = fields.Int(required=False)
    
    gte = fields.Int(required=False)
    


class StoreRuleConditionSchema(BaseSchema):
    # Serviceability swagger.json

    
    department_ids = fields.Nested(IntComparisonOperations, required=False)
    
    category_ids = fields.Nested(IntComparisonOperations, required=False)
    
    brand_ids = fields.Nested(IntComparisonOperations, required=False)
    
    to_location = fields.Nested(LocationRule, required=False)
    
    customer_radius = fields.Nested(CustomerRadiusSchema, required=False)
    
    store_type = fields.Nested(StringComparisonOperations, required=False)
    
    product_tags = fields.Nested(StringComparisonOperations, required=False)
    
    product_ids = fields.Nested(IntComparisonOperations, required=False)
    
    store_tags = fields.Nested(StringComparisonOperations, required=False)
    
    order_place_date = fields.Nested(ArithmeticOperations, required=False)
    
    zone_ids = fields.Nested(StringComparisonOperations, required=False)
    


class StoreRuleDataSchema(BaseSchema):
    # Serviceability swagger.json

    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    application_id = fields.Str(required=False)
    
    type_based_priority = fields.List(fields.Str(required=False), required=False)
    
    tag_based_priority = fields.List(fields.Str(required=False), required=False)
    
    store_priority = fields.List(fields.Nested(StorePrioritySchema, required=False), required=False)
    
    sort = fields.List(fields.Str(required=False), required=False)
    
    conditions = fields.Nested(StoreRuleConditionSchema, required=False)
    
    is_active = fields.Boolean(required=False)
    


class StorePrioritySchema(BaseSchema):
    # Serviceability swagger.json

    
    id = fields.Int(required=False)
    
    name = fields.Str(required=False)
    


class GetStoreRulesApiResult(BaseSchema):
    # Serviceability swagger.json

    
    items = fields.List(fields.Nested(StoreRuleDataSchema, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class CreateStoreRuleDetailsSchema(BaseSchema):
    # Serviceability swagger.json

    
    name = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    conditions = fields.Nested(StoreRuleConditionSchema, required=False)
    
    type_based_priority = fields.List(fields.Str(required=False), required=False)
    
    tag_based_priority = fields.List(fields.Str(required=False), required=False)
    
    store_priority = fields.List(fields.Nested(StorePrioritySchema, required=False), required=False)
    
    sort = fields.List(fields.Str(required=False), required=False)
    


class StoreRuleResultSchema(BaseSchema):
    # Serviceability swagger.json

    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    type_based_priority = fields.List(fields.Str(required=False), required=False)
    
    tag_based_priority = fields.List(fields.Str(required=False), required=False)
    
    store_priority = fields.List(fields.Nested(StorePrioritySchema, required=False), required=False)
    
    sort = fields.List(fields.Str(required=False), required=False)
    
    conditions = fields.Nested(StoreRuleConditionSchema, required=False)
    
    is_active = fields.Boolean(required=False)
    


class StoreRuleUpdateResultSchema(BaseSchema):
    # Serviceability swagger.json

    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    type_based_priority = fields.List(fields.Str(required=False), required=False)
    
    tag_based_priority = fields.List(fields.Str(required=False), required=False)
    
    store_priority = fields.List(fields.Nested(StorePrioritySchema, required=False), required=False)
    
    sort = fields.List(fields.Str(required=False), required=False)
    
    conditions = fields.Nested(StoreRuleConditionSchema, required=False)
    
    is_active = fields.Boolean(required=False)
    
    company_id = fields.Int(required=False)
    
    application_id = fields.Str(required=False)
    


class ServiceabilityModel(BaseSchema):
    # Serviceability swagger.json

    
    lm_cod_limit = fields.Int(required=False)
    
    is_qc = fields.Boolean(required=False)
    
    pickup_cutoff = fields.Str(required=False, allow_none=True)
    
    route_code = fields.Str(required=False, allow_none=True)
    
    is_first_mile = fields.Boolean(required=False)
    
    is_reverse_pickup = fields.Boolean(required=False, allow_none=True)
    
    is_return = fields.Boolean(required=False)
    
    is_installation = fields.Boolean(required=False)
    
    is_last_mile = fields.Boolean(required=False)
    


class CourierPartnerSchemeFeatures(BaseSchema):
    # Serviceability swagger.json

    
    doorstep_qc = fields.Boolean(required=False)
    
    qr = fields.Boolean(required=False)
    
    mps = fields.Boolean(required=False)
    
    ndr = fields.Boolean(required=False)
    
    ndr_attempts = fields.Int(required=False)
    
    dangerous_goods = fields.Boolean(required=False)
    
    fragile_goods = fields.Boolean(required=False)
    
    restricted_goods = fields.Boolean(required=False)
    
    cold_storage_goods = fields.Boolean(required=False)
    
    doorstep_exchange = fields.Boolean(required=False)
    
    doorstep_return = fields.Boolean(required=False)
    
    product_installation = fields.Boolean(required=False)
    
    openbox_delivery = fields.Boolean(required=False)
    
    status_updates = fields.Str(required=False)
    
    multi_pick_single_drop = fields.Boolean(required=False)
    
    single_pick_multi_drop = fields.Boolean(required=False)
    
    multi_pick_multi_drop = fields.Boolean(required=False)
    
    ewaybill = fields.Boolean(required=False)
    
    qc_shipment_item_quantity = fields.Int(required=False, allow_none=True)
    
    non_qc_shipment_item_quantity = fields.Int(required=False, allow_none=True)
    


class CourierPartnerSchemeModel(BaseSchema):
    # Serviceability swagger.json

    
    name = fields.Str(required=False)
    
    extension_id = fields.Str(required=False)
    
    scheme_id = fields.Str(required=False)
    
    volumetric_weight = fields.Nested(ArithmeticOperations, required=False)
    
    weight = fields.Nested(ArithmeticOperations, required=False)
    
    transport_type = fields.Str(required=False)
    
    region = fields.Str(required=False)
    
    delivery_type = fields.Str(required=False)
    
    payment_mode = fields.List(fields.Str(required=False), required=False)
    
    stage = fields.Str(required=False)
    
    feature = fields.Nested(CourierPartnerSchemeFeatures, required=False)
    


class CourierAccountResult(BaseSchema):
    # Serviceability swagger.json

    
    company_id = fields.Int(required=False)
    
    extension_id = fields.Str(required=False)
    
    account_id = fields.Str(required=False)
    
    scheme_id = fields.Str(required=False)
    
    is_self_ship = fields.Boolean(required=False)
    
    stage = fields.Str(required=False)
    
    is_own_account = fields.Boolean(required=False)
    
    scheme_rules = fields.Nested(CourierPartnerSchemeModel, required=False)
    


class CompanyCourierPartnerAccountListResult(BaseSchema):
    # Serviceability swagger.json

    
    items = fields.List(fields.Nested(CourierAccountResult, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class PackageMaterial(BaseSchema):
    # Serviceability swagger.json

    
    name = fields.Str(required=False)
    
    width = fields.Float(required=False)
    
    height = fields.Float(required=False)
    
    length = fields.Float(required=False)
    
    rules = fields.List(fields.Nested(PackageMaterialRule, required=False), required=False)
    
    store_ids = fields.List(fields.Int(required=False), required=False)
    
    weight = fields.Float(required=False)
    
    error_rate = fields.Float(required=False)
    
    package_type = fields.Str(required=False)
    
    size = fields.Str(required=False)
    
    media = fields.List(fields.Str(required=False), required=False)
    
    channels = fields.List(fields.Nested(Channel, required=False), required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    status = fields.Str(required=False)
    
    max_weight = fields.Float(required=False)
    
    package_vol_weight = fields.Float(required=False)
    
    auto_calculate = fields.Boolean(required=False)
    


class PackageMaterialResult(BaseSchema):
    # Serviceability swagger.json

    
    name = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    item_id = fields.Int(required=False)
    
    company_id = fields.Int(required=False)
    
    width = fields.Float(required=False)
    
    height = fields.Float(required=False)
    
    length = fields.Float(required=False)
    
    rules = fields.List(fields.Nested(PackageMaterialRule, required=False), required=False)
    
    store_ids = fields.List(fields.Int(required=False), required=False)
    
    weight = fields.Float(required=False)
    
    error_rate = fields.Float(required=False)
    
    package_type = fields.Str(required=False)
    
    size = fields.Str(required=False)
    
    media = fields.List(fields.Str(required=False), required=False)
    
    channels = fields.List(fields.Nested(Channel, required=False), required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    status = fields.Str(required=False)
    
    max_weight = fields.Float(required=False)
    
    package_vol_weight = fields.Float(required=False)
    
    auto_calculate = fields.Boolean(required=False)
    


class PackageMaterialRule(BaseSchema):
    # Serviceability swagger.json

    
    rule_id = fields.Str(required=False)
    
    quantity = fields.Nested(PackageMaterialRuleQuantity, required=False)
    
    weight = fields.Int(required=False)
    


class PackageRule(BaseSchema):
    # Serviceability swagger.json

    
    name = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    product_tag = fields.Nested(PackageRuleProductTag, required=False)
    
    product_id = fields.Nested(PackageRuleProduct, required=False)
    
    category_id = fields.Nested(PackageRuleCategory, required=False)
    


class PackageRuleResult(BaseSchema):
    # Serviceability swagger.json

    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    product_tag = fields.Nested(PackageRuleProductTag, required=False)
    
    product_id = fields.Nested(PackageRuleProduct, required=False)
    
    category_id = fields.Nested(PackageRuleCategory, required=False)
    


class Channel(BaseSchema):
    # Serviceability swagger.json

    
    type = fields.Str(required=False)
    
    id = fields.Str(required=False)
    


class PackageMaterialRuleList(BaseSchema):
    # Serviceability swagger.json

    
    items = fields.Nested(PackageRuleResult, required=False)
    
    page = fields.Nested(Page, required=False)
    


class PackageMaterialList(BaseSchema):
    # Serviceability swagger.json

    
    items = fields.Nested(PackageMaterialResult, required=False)
    
    page = fields.Nested(Page, required=False)
    


class PackageRuleProduct(BaseSchema):
    # Serviceability swagger.json

    
    includes = fields.List(fields.Int(required=False), required=False)
    


class PackageRuleProductTag(BaseSchema):
    # Serviceability swagger.json

    
    includes = fields.List(fields.Str(required=False), required=False)
    


class PackageRuleCategory(BaseSchema):
    # Serviceability swagger.json

    
    includes = fields.List(fields.Int(required=False), required=False)
    


class PackageMaterialRuleQuantity(BaseSchema):
    # Serviceability swagger.json

    
    min = fields.Int(required=False)
    
    max = fields.Int(required=False)
    


class RulePriorityDetails(BaseSchema):
    # Serviceability swagger.json

    
    rule_id = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    


class RulePriorityResult(BaseSchema):
    # Serviceability swagger.json

    
    success = fields.Boolean(required=False)
    


class ArticleAssignment(BaseSchema):
    # Serviceability swagger.json

    
    level = fields.Str(required=False)
    
    strategy = fields.Str(required=False)
    


class ServiceabilityLocation(BaseSchema):
    # Serviceability swagger.json

    
    longitude = fields.Str(required=False)
    
    latitude = fields.Str(required=False)
    


class LocationDetailsServiceability(BaseSchema):
    # Serviceability swagger.json

    
    pincode = fields.Str(required=False)
    
    sector = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    country_iso_code = fields.Str(required=False)
    
    location = fields.Nested(ServiceabilityLocation, required=False)
    


class OptimalLocationsArticles(BaseSchema):
    # Serviceability swagger.json

    
    item_id = fields.Int(required=False)
    
    size = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    group_id = fields.Str(required=False)
    
    is_primary_item = fields.Boolean(required=False)
    
    meta = fields.Dict(required=False)
    
    article_assignment = fields.Nested(ArticleAssignment, required=False)
    
    ignore_locations = fields.List(fields.Int(required=False), required=False)
    
    assign_locations = fields.List(fields.Int(required=False), required=False)
    
    seller_id = fields.Int(required=False)
    


class OptimlLocationsDetailsSchema(BaseSchema):
    # Serviceability swagger.json

    
    channel_id = fields.Str(required=False)
    
    channel_type = fields.Str(required=False)
    
    channel_identifier = fields.Str(required=False)
    
    to_serviceability = fields.Nested(LocationDetailsServiceability, required=False)
    
    articles = fields.List(fields.Nested(OptimalLocationsArticles, required=False), required=False)
    


class OptimalLocationArticlesResult(BaseSchema):
    # Serviceability swagger.json

    
    item_id = fields.Int(required=False)
    
    size = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    group_id = fields.Str(required=False)
    
    is_primary_item = fields.Boolean(required=False)
    
    meta = fields.Dict(required=False)
    
    article_assignment = fields.Nested(ArticleAssignment, required=False)
    
    seller_id = fields.Int(required=False)
    
    ignore_locations = fields.List(fields.Int(required=False), required=False)
    
    assign_locations = fields.List(fields.Int(required=False), required=False)
    
    price_effective = fields.Float(required=False)
    
    mto_quantity = fields.Int(required=False)
    
    _id = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    


class OptimalLocationAssignedStoresResult(BaseSchema):
    # Serviceability swagger.json

    
    store_id = fields.Int(required=False)
    
    articles = fields.List(fields.Nested(OptimalLocationArticlesResult, required=False), required=False)
    


class OptimalLocationsResult(BaseSchema):
    # Serviceability swagger.json

    
    assigned_stores = fields.List(fields.Nested(OptimalLocationAssignedStoresResult, required=False), required=False)
    
    faulty_articles = fields.List(fields.Nested(ErrorResult, required=False), required=False)
    


class ValidationError(BaseSchema):
    # Serviceability swagger.json

    
    message = fields.Str(required=False)
    
    field = fields.Str(required=False)
    


class StandardError(BaseSchema):
    # Serviceability swagger.json

    
    message = fields.Str(required=False)
    


class CourierPartnerSchemeV2Features(BaseSchema):
    # Serviceability swagger.json

    
    doorstep_qc = fields.Boolean(required=False)
    
    qr = fields.Boolean(required=False)
    
    mps = fields.Boolean(required=False)
    
    ndr = fields.Boolean(required=False)
    
    dangerous_goods = fields.Boolean(required=False)
    
    fragile_goods = fields.Boolean(required=False)
    
    restricted_goods = fields.Boolean(required=False)
    
    cold_storage_goods = fields.Boolean(required=False)
    
    doorstep_exchange = fields.Boolean(required=False)
    
    doorstep_return = fields.Boolean(required=False)
    
    product_installation = fields.Boolean(required=False)
    
    openbox_delivery = fields.Boolean(required=False)
    
    multi_pick_single_drop = fields.Boolean(required=False)
    
    single_pick_multi_drop = fields.Boolean(required=False)
    
    multi_pick_multi_drop = fields.Boolean(required=False)
    
    ewaybill = fields.Boolean(required=False)
    


class CourierPartnerSchemeV2DetailsModel(BaseSchema):
    # Serviceability swagger.json

    
    extension_id = fields.Str(required=False)
    
    scheme_id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    weight = fields.Nested(ArithmeticOperations, required=False)
    
    volumetric_weight = fields.Nested(ArithmeticOperations, required=False)
    
    transport_type = fields.Str(required=False)
    
    region = fields.Str(required=False)
    
    delivery_type = fields.Str(required=False)
    
    payment_mode = fields.List(fields.Str(required=False), required=False)
    
    stage = fields.Str(required=False)
    
    status_updates = fields.Str(required=False)
    
    ndr_attempts = fields.Int(required=False)
    
    qc_shipment_item_quantity = fields.Int(required=False, allow_none=True)
    
    non_qc_shipment_item_quantity = fields.Int(required=False, allow_none=True)
    
    feature = fields.Nested(CourierPartnerSchemeV2Features, required=False)
    


class CourierPartnerV2SchemeModel(BaseSchema):
    # Serviceability swagger.json

    
    extension_id = fields.Str(required=False)
    
    scheme_id = fields.Str(required=False)
    
    company_id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    weight = fields.Nested(ArithmeticOperations, required=False)
    
    volumetric_weight = fields.Nested(ArithmeticOperations, required=False)
    
    transport_type = fields.Str(required=False)
    
    region = fields.Str(required=False)
    
    delivery_type = fields.Str(required=False)
    
    payment_mode = fields.List(fields.Str(required=False), required=False)
    
    stage = fields.Str(required=False)
    
    status_updates = fields.Str(required=False)
    
    ndr_attempts = fields.Int(required=False)
    
    qc_shipment_item_quantity = fields.Int(required=False, allow_none=True)
    
    non_qc_shipment_item_quantity = fields.Int(required=False, allow_none=True)
    
    feature = fields.Nested(CourierPartnerSchemeV2Features, required=False)
    


class CourierPartnerSchemeV2UpdateDetails(BaseSchema):
    # Serviceability swagger.json

    
    name = fields.Str(required=False)
    
    weight = fields.Nested(ArithmeticOperations, required=False)
    
    volumetric_weight = fields.Nested(ArithmeticOperations, required=False)
    
    transport_type = fields.Str(required=False)
    
    region = fields.Str(required=False)
    
    delivery_type = fields.Str(required=False)
    
    payment_mode = fields.List(fields.Str(required=False), required=False)
    
    stage = fields.Str(required=False)
    
    status_updates = fields.Str(required=False)
    
    ndr_attempts = fields.Int(required=False)
    
    qc_shipment_item_quantity = fields.Int(required=False, allow_none=True)
    
    non_qc_shipment_item_quantity = fields.Int(required=False, allow_none=True)
    
    feature = fields.Nested(CourierPartnerSchemeV2Features, required=False)
    


class courierPartnerSchemeV2List(BaseSchema):
    # Serviceability swagger.json

    
    items = fields.List(fields.Nested(CourierPartnerV2SchemeModel, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class BulkRegionServiceabilityTatDetails(BaseSchema):
    # Serviceability swagger.json

    
    country = fields.Str(required=False)
    
    region = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class BulkRegionServiceabilityTatResultItemData(BaseSchema):
    # Serviceability swagger.json

    
    country = fields.Str(required=False)
    
    region = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    batch_id = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    failed_records = fields.List(fields.Dict(required=False), required=False)
    
    file_path = fields.Str(required=False, allow_none=True)
    


class BulkRegionServiceabilityTatResult(BaseSchema):
    # Serviceability swagger.json

    
    items = fields.List(fields.Nested(BulkRegionServiceabilityTatResultItemData, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class HierarchyItems(BaseSchema):
    # Serviceability swagger.json

    
    display_name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    


class GetCountriesItems(BaseSchema):
    # Serviceability swagger.json

    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    iso2 = fields.Str(required=False)
    
    iso3 = fields.Str(required=False)
    
    timezones = fields.List(fields.Str(required=False), required=False)
    
    hierarchy = fields.List(fields.Nested(HierarchyItems, required=False), required=False)
    
    phone_code = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    latitude = fields.Str(required=False)
    
    longitude = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    has_next_hierarchy = fields.Boolean(required=False)
    


class GetCountries(BaseSchema):
    # Serviceability swagger.json

    
    items = fields.List(fields.Nested(GetCountriesItems, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


