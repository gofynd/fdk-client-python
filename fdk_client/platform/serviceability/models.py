"""Serviceability Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




class BulkRegionServiceabilityTatRequest(BaseSchema):
    pass


class BulkRegionServiceabilityTatResponseItemData(BaseSchema):
    pass


class BulkRegionServiceabilityTatResponse(BaseSchema):
    pass


class CourierPartnerSchemeUpdateRequest(BaseSchema):
    pass


class CourierPartnerSchemeModel(BaseSchema):
    pass


class ZoneBulkErrorResponse(BaseSchema):
    pass


class ZoneBulkValidationRequestSchema(BaseSchema):
    pass


class BulkZoneOverrideResponseSchema(BaseSchema):
    pass


class ZoneBulkImportResponse(BaseSchema):
    pass


class ZoneOverrideSchema(BaseSchema):
    pass


class BulkZoneOverrideSchema(BaseSchema):
    pass


class ZoneBulkValidationErrorResponse(BaseSchema):
    pass


class ZoneBulkValidationResponse(BaseSchema):
    pass


class ZoneBulkValidationStatusResponse(BaseSchema):
    pass


class ZoneOverrideResponseSchema(BaseSchema):
    pass


class StandardError(BaseSchema):
    pass


class ValidationError(BaseSchema):
    pass


class ZoneOverrideStatusResponseSchema(BaseSchema):
    pass


class OverrideStatusSchema(BaseSchema):
    pass


class BulkZoneOverrideStatusSchema(BaseSchema):
    pass


class GetExportPriceZoneHistory(BaseSchema):
    pass


class PriceBulkGeoAreaExportRequestPayload(BaseSchema):
    pass


class GetBulkPriceZoneHistory(BaseSchema):
    pass


class Pagination(BaseSchema):
    pass


class BulkPriceZoneItem(BaseSchema):
    pass


class PriceBulkGeoAreaPayload(BaseSchema):
    pass


class RuleConditionIntegerDetail(BaseSchema):
    pass


class RuleConditionStringDetail(BaseSchema):
    pass


class RuleResponseIntegerDetail(BaseSchema):
    pass


class RuleResponseStringDetail(BaseSchema):
    pass


class CourierPartnerRuleResponseDetailConditions(BaseSchema):
    pass


class CourierPartnerRuleResponseDetailSchema(BaseSchema):
    pass


class StoreLocationDetail(BaseSchema):
    pass


class StoreRuleLocationDetailSchema(BaseSchema):
    pass


class StoreRuleConditionDetailSchema(BaseSchema):
    pass


class StoreRuleDataDetailsSchema(BaseSchema):
    pass


class OptimalLocationArticlesResponse(BaseSchema):
    pass


class OptimalLocationAssignedStoresResponse(BaseSchema):
    pass


class OptimalLocationsResponse(BaseSchema):
    pass


class ArticleAssignment(BaseSchema):
    pass


class OptimalLocationsArticles(BaseSchema):
    pass


class ServiceabilityLocation(BaseSchema):
    pass


class LocationDetailsServiceability(BaseSchema):
    pass


class OptimlLocationsRequestSchema(BaseSchema):
    pass


class ErrorResponseV3(BaseSchema):
    pass


class ErrorObject(BaseSchema):
    pass


class ValidateAddressRequest(BaseSchema):
    pass


class CountryObject(BaseSchema):
    pass


class GetCountries(BaseSchema):
    pass


class CurrencyObject(BaseSchema):
    pass


class CountryHierarchy(BaseSchema):
    pass


class GetCountry(BaseSchema):
    pass


class GetCountryFields(BaseSchema):
    pass


class GetCountryFieldsAddressTemplate(BaseSchema):
    pass


class FieldValidation(BaseSchema):
    pass


class FieldValidationRegex(BaseSchema):
    pass


class LengthValidation(BaseSchema):
    pass


class GetOneOrAllQuery(BaseSchema):
    pass


class GetOneOrAllPath(BaseSchema):
    pass


class GetOneOrAllParams(BaseSchema):
    pass


class GetOneOrAll(BaseSchema):
    pass


class GetCountryFieldsAddressValues(BaseSchema):
    pass


class GetCountryFieldsAddress(BaseSchema):
    pass


class PincodeLatLongData(BaseSchema):
    pass


class Localities(BaseSchema):
    pass


class GetLocalities(BaseSchema):
    pass


class LocalityParent(BaseSchema):
    pass


class GetLocality(BaseSchema):
    pass


class ApplicationConfigPutResponse(BaseSchema):
    pass


class PromiseType(BaseSchema):
    pass


class BuyboxRuleConfig(BaseSchema):
    pass


class CourierPartnerConfig(BaseSchema):
    pass


class ZoneConfig(BaseSchema):
    pass


class ApplicationConfigGetResponse(BaseSchema):
    pass


class ApplicationConfigPutRequest(BaseSchema):
    pass


class InstallCourierPartnerItemsSchema(BaseSchema):
    pass


class InstallCourierPartnerResponseSchema(BaseSchema):
    pass


class UpdateZoneConfigRequest(BaseSchema):
    pass


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


class getAppRegionZonesResponse(BaseSchema):
    pass


class PageSchema(BaseSchema):
    pass


class EntityRegionView_Items(BaseSchema):
    pass


class EntityRegionView_Response(BaseSchema):
    pass


class ListViewSummary(BaseSchema):
    pass


class ProductSchema(BaseSchema):
    pass


class ProductDetailsSchema(BaseSchema):
    pass


class StoresSchema(BaseSchema):
    pass


class StoresDetailsSchema(BaseSchema):
    pass


class DetailsSchema(BaseSchema):
    pass


class StoreValueDetailsSchema(BaseSchema):
    pass


class SummarySchema(BaseSchema):
    pass


class RegionSchema(BaseSchema):
    pass


class ServiceabilityDeleteErrorResponse(BaseSchema):
    pass


class ListViewResponseV2(BaseSchema):
    pass


class ListViewItemsV2(BaseSchema):
    pass


class SummaryRegions(BaseSchema):
    pass


class Summary(BaseSchema):
    pass


class GeoArea(BaseSchema):
    pass


class ListViewProductV2(BaseSchema):
    pass


class ZoneDataItem(BaseSchema):
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


class UpdateZoneDataV2(BaseSchema):
    pass


class ZoneUpdateSuccessResponse(BaseSchema):
    pass


class ZoneDeleteSuccessResponse(BaseSchema):
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


class GetZoneByIdSchema(BaseSchema):
    pass


class GetZoneByIdDetailsSchema(BaseSchema):
    pass


class GeoAreaDetailsSchema(BaseSchema):
    pass


class CreateZoneV2Data(BaseSchema):
    pass


class ZoneBulkExport(BaseSchema):
    pass


class GetZoneBulkExport(BaseSchema):
    pass


class ZoneBulkItem(BaseSchema):
    pass


class CreateBulkZoneData(BaseSchema):
    pass


class ZoneStores(BaseSchema):
    pass


class ZoneProduct(BaseSchema):
    pass


class ZoneResponseV2(BaseSchema):
    pass


class CreateBulkZoneResponse(BaseSchema):
    pass


class GetBulkZoneHistory(BaseSchema):
    pass


class BulkZoneItems(BaseSchema):
    pass


class PageV2(BaseSchema):
    pass


class BulkCreateZoneExport(BaseSchema):
    pass


class CreateZoneData(BaseSchema):
    pass


class ZoneResponse(BaseSchema):
    pass


class GetZoneFromPincodeViewRequest(BaseSchema):
    pass


class Zone(BaseSchema):
    pass


class GetZoneFromPincodeViewResponse(BaseSchema):
    pass


class GetZoneFromApplicationIdViewResponse(BaseSchema):
    pass


class ServiceabilityPageResponse(BaseSchema):
    pass


class MobileNo(BaseSchema):
    pass


class ManagerResponse(BaseSchema):
    pass


class ModifiedByResponse(BaseSchema):
    pass


class IntegrationTypeResponse(BaseSchema):
    pass


class ProductReturnConfigResponse(BaseSchema):
    pass


class ContactNumberResponse(BaseSchema):
    pass


class AddressResponse(BaseSchema):
    pass


class CreatedByResponse(BaseSchema):
    pass


class EwayBillResponse(BaseSchema):
    pass


class EinvoiceResponse(BaseSchema):
    pass


class GstCredentialsResponse(BaseSchema):
    pass


class WarningsResponse(BaseSchema):
    pass


class OpeningClosing(BaseSchema):
    pass


class TimmingResponse(BaseSchema):
    pass


class DocumentsResponse(BaseSchema):
    pass


class Dp(BaseSchema):
    pass


class LogisticsResponse(BaseSchema):
    pass


class ItemResponse(BaseSchema):
    pass


class GetStoresViewResponse(BaseSchema):
    pass


class ReAssignStoreRequest(BaseSchema):
    pass


class ServiceabilityZoneErrorResult(BaseSchema):
    pass


class ServiceabilityZoneNonMarketplaceErrorResult(BaseSchema):
    pass


class ReAssignStoreResponse(BaseSchema):
    pass


class PincodeMopData(BaseSchema):
    pass


class PincodeMopUpdateResponse(BaseSchema):
    pass


class PincodeMOPresponse(BaseSchema):
    pass


class CommonError(BaseSchema):
    pass


class MoPCommonError(BaseSchema):
    pass


class PincodeMopBulkData(BaseSchema):
    pass


class PincodeBulkViewResponse(BaseSchema):
    pass


class PincodeCodStatusListingRequest(BaseSchema):
    pass


class PincodeCodDataSchema(BaseSchema):
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


class ArithmeticOperations(BaseSchema):
    pass


class SchemeRulesFeatures(BaseSchema):
    pass


class SchemeRules(BaseSchema):
    pass


class CourierAccount(BaseSchema):
    pass


class BulkGeoAreaDetails(BaseSchema):
    pass


class BulkGeoAreaResult(BaseSchema):
    pass


class PriceGeoAreaExportResult(BaseSchema):
    pass


class BulkGeoAreaGetResponse(BaseSchema):
    pass


class GeoAreaBulkCreationResult(BaseSchema):
    pass


class GeoAreaBulkExportResult(BaseSchema):
    pass


class GeoAreaRequestBody(BaseSchema):
    pass


class GeoAreaErrorResult(BaseSchema):
    pass


class ErrorResponseItem(BaseSchema):
    pass


class ConflictingArea(BaseSchema):
    pass


class GeoAreaResponseDetail(BaseSchema):
    pass


class ErrorResponseDetail(BaseSchema):
    pass


class GeoAreaResponseBody(BaseSchema):
    pass


class GeoAreaPutResponseBody(BaseSchema):
    pass


class Area(BaseSchema):
    pass


class Region(BaseSchema):
    pass


class RegionV2(BaseSchema):
    pass


class Country(BaseSchema):
    pass


class AreaExpanded(BaseSchema):
    pass


class AreaExpandedV2(BaseSchema):
    pass


class GeoAreaResponse(BaseSchema):
    pass


class GeoAreaGetResponseBody(BaseSchema):
    pass


class GeoAreaItemResponse(BaseSchema):
    pass


class ErrorResponseV2(BaseSchema):
    pass


class ErrorResponse(BaseSchema):
    pass


class PackageMaterialNotFound(BaseSchema):
    pass


class PackageMaterialsErrorResponse(BaseSchema):
    pass


class CourierPartnerAccountFailureResponse(BaseSchema):
    pass


class Page(BaseSchema):
    pass


class Page2(BaseSchema):
    pass


class CourierPartnerList(BaseSchema):
    pass


class LocationRuleValues(BaseSchema):
    pass


class LocationRuleValuesV2(BaseSchema):
    pass


class LocationRule(BaseSchema):
    pass


class LocationRuleV2(BaseSchema):
    pass


class StringComparisonOperations(BaseSchema):
    pass


class IntComparisonOperations(BaseSchema):
    pass


class CourierPartnerRuleConditions(BaseSchema):
    pass


class CourierPartnerRuleResponseConditions(BaseSchema):
    pass


class CourierPartnerRule(BaseSchema):
    pass


class CourierPartnerRuleResponse(BaseSchema):
    pass


class CourierPartnerRuleResponseSchema(BaseSchema):
    pass


class FailureResponse(BaseSchema):
    pass


class CourierPartnerRulesListResponse(BaseSchema):
    pass


class CompanyConfig(BaseSchema):
    pass


class StorePromiseAttributeConfig(BaseSchema):
    pass


class DeliveryServiceAttributeConfig(BaseSchema):
    pass


class BufferField(BaseSchema):
    pass


class PromiseConfig(BaseSchema):
    pass


class ApplicationConfig(BaseSchema):
    pass


class ApplicationConfigPatchRequest(BaseSchema):
    pass


class ApplicationConfigPatchResponse(BaseSchema):
    pass


class BulkRegionJobSerializer(BaseSchema):
    pass


class BulkRegionResponseItemData(BaseSchema):
    pass


class BulkRegionResponse(BaseSchema):
    pass


class SelfShipResponse(BaseSchema):
    pass


class ApplicationSelfShipConfig(BaseSchema):
    pass


class ApplicationSelfShipConfigResponse(BaseSchema):
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


class GetStoreRulesApiResponse(BaseSchema):
    pass


class CreateStoreRuleRequestSchema(BaseSchema):
    pass


class StoreRuleResponseSchema(BaseSchema):
    pass


class StoreRuleUpdateResponseSchema(BaseSchema):
    pass


class ServiceabilityModel(BaseSchema):
    pass


class CourierPartnerSchemeFeatures(BaseSchema):
    pass


class CourierAccountSchemeResponse(BaseSchema):
    pass


class CourierAccountResponse(BaseSchema):
    pass


class CompanyCourierPartnerAccountListResponse(BaseSchema):
    pass


class PackageMaterial(BaseSchema):
    pass


class PackageMaterialResponse(BaseSchema):
    pass


class PackageMaterialRule(BaseSchema):
    pass


class PackageMpStores(BaseSchema):
    pass


class PackageRuleRequest(BaseSchema):
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


class PackageRuleProductAttributes(BaseSchema):
    pass


class PackageRuleDepartmentId(BaseSchema):
    pass


class PackageMaterialRuleQuantity(BaseSchema):
    pass


class RulePriorityRequest(BaseSchema):
    pass


class RulePriorityResponse(BaseSchema):
    pass


class CompanySelfShip(BaseSchema):
    pass


class ArithmeticOperationsV2(BaseSchema):
    pass


class CompanyConfigurationShema(BaseSchema):
    pass





class BulkRegionServiceabilityTatRequest(BaseSchema):
    # Serviceability swagger.json

    
    country = fields.Str(required=False)
    
    region = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class BulkRegionServiceabilityTatResponseItemData(BaseSchema):
    # Serviceability swagger.json

    
    country = fields.Str(required=False)
    
    region = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    batch_id = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    failed_records = fields.List(fields.Dict(required=False), required=False)
    
    file_path = fields.Str(required=False, allow_none=True)
    


class BulkRegionServiceabilityTatResponse(BaseSchema):
    # Serviceability swagger.json

    
    items = fields.List(fields.Nested(BulkRegionServiceabilityTatResponseItemData, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class CourierPartnerSchemeUpdateRequest(BaseSchema):
    # Serviceability swagger.json

    
    name = fields.Str(required=False)
    
    weight = fields.Nested(ArithmeticOperations, required=False)
    
    volumetric_weight = fields.Nested(ArithmeticOperations, required=False)
    
    transport_type = fields.Str(required=False)
    
    region = fields.Str(required=False)
    
    delivery_type = fields.Str(required=False)
    
    payment_mode = fields.List(fields.Str(required=False), required=False)
    
    stage = fields.Str(required=False)
    
    feature = fields.Nested(CourierPartnerSchemeFeatures, required=False)
    


class CourierPartnerSchemeModel(BaseSchema):
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
    
    feature = fields.Nested(CourierPartnerSchemeFeatures, required=False)
    


class ZoneBulkErrorResponse(BaseSchema):
    # Serviceability swagger.json

    
    error = fields.Str(required=False)
    


class ZoneBulkValidationRequestSchema(BaseSchema):
    # Serviceability swagger.json

    
    file_url = fields.Str(required=False)
    
    product_type = fields.Str(required=False)
    


class BulkZoneOverrideResponseSchema(BaseSchema):
    # Serviceability swagger.json

    
    batch_id = fields.Str(required=False)
    


class ZoneBulkImportResponse(BaseSchema):
    # Serviceability swagger.json

    
    batch_id = fields.Str(required=False)
    
    file_path = fields.Str(required=False)
    
    product_type = fields.Str(required=False)
    
    total = fields.Int(required=False)
    
    failed = fields.Int(required=False)
    
    error_file_url = fields.Str(required=False, allow_none=True)
    
    action = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    updated_by = fields.Dict(required=False)
    
    type = fields.Str(required=False)
    
    company_id = fields.Str(required=False)
    
    application_id = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    


class ZoneOverrideSchema(BaseSchema):
    # Serviceability swagger.json

    
    allow_override = fields.Boolean(required=False)
    


class BulkZoneOverrideSchema(BaseSchema):
    # Serviceability swagger.json

    
    allow_override = fields.Boolean(required=False)
    
    overridding_correction_file_url = fields.Str(required=False)
    


class ZoneBulkValidationErrorResponse(BaseSchema):
    # Serviceability swagger.json

    
    error = fields.Raw(required=False)
    


class ZoneBulkValidationResponse(BaseSchema):
    # Serviceability swagger.json

    
    batch_id = fields.Str(required=False)
    


class ZoneBulkValidationStatusResponse(BaseSchema):
    # Serviceability swagger.json

    
    batch_id = fields.Str(required=False)
    
    file_path = fields.Str(required=False)
    
    product_type = fields.Str(required=False)
    
    total = fields.Int(required=False)
    
    failed = fields.Int(required=False)
    
    error_file_url = fields.Str(required=False, allow_none=True)
    
    action = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    updated_by = fields.Dict(required=False)
    
    type = fields.Str(required=False)
    
    company_id = fields.Str(required=False)
    
    application_id = fields.Str(required=False)
    
    file_url = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    


class ZoneOverrideResponseSchema(BaseSchema):
    # Serviceability swagger.json

    
    zone_id = fields.Str(required=False)
    
    allow_override = fields.Boolean(required=False)
    


class StandardError(BaseSchema):
    # Serviceability swagger.json

    
    message = fields.Str(required=False)
    


class ValidationError(BaseSchema):
    # Serviceability swagger.json

    
    message = fields.Str(required=False)
    
    field = fields.Str(required=False)
    


class ZoneOverrideStatusResponseSchema(BaseSchema):
    # Serviceability swagger.json

    
    overriding_process_status = fields.Str(required=False)
    


class OverrideStatusSchema(BaseSchema):
    # Serviceability swagger.json

    
    overriding_process_status = fields.Str(required=False)
    


class BulkZoneOverrideStatusSchema(BaseSchema):
    # Serviceability swagger.json

    
    items = fields.List(fields.Nested(OverrideStatusSchema, required=False), required=False)
    


class GetExportPriceZoneHistory(BaseSchema):
    # Serviceability swagger.json

    
    batch_id = fields.Str(required=False)
    
    file_path = fields.Str(required=False, allow_none=True)
    
    total = fields.Int(required=False)
    
    failed = fields.Int(required=False)
    
    error_file_url = fields.Str(required=False, allow_none=True)
    
    action = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    updated_by = fields.Str(required=False, allow_none=True)
    
    type = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    


class PriceBulkGeoAreaExportRequestPayload(BaseSchema):
    # Serviceability swagger.json

    
    type = fields.Str(required=False)
    


class GetBulkPriceZoneHistory(BaseSchema):
    # Serviceability swagger.json

    
    page = fields.Nested(Pagination, required=False)
    
    items = fields.List(fields.Nested(BulkPriceZoneItem, required=False), required=False)
    


class Pagination(BaseSchema):
    # Serviceability swagger.json

    
    type = fields.Str(required=False)
    
    size = fields.Int(required=False)
    
    current = fields.Int(required=False)
    
    has_next = fields.Boolean(required=False)
    
    item_total = fields.Int(required=False)
    


class BulkPriceZoneItem(BaseSchema):
    # Serviceability swagger.json

    
    batch_id = fields.Str(required=False)
    
    entity_type = fields.Str(required=False)
    
    error_file_url = fields.Str(required=False, allow_none=True)
    
    file_path = fields.Str(required=False)
    
    file_name = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    updated_by = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    


class PriceBulkGeoAreaPayload(BaseSchema):
    # Serviceability swagger.json

    
    type = fields.Str(required=False)
    
    file_url = fields.Str(required=False)
    


class RuleConditionIntegerDetail(BaseSchema):
    # Serviceability swagger.json

    
    text = fields.Str(required=False, allow_none=True)
    
    value = fields.Int(required=False, allow_none=True)
    
    stage = fields.Boolean(required=False, allow_none=True)
    


class RuleConditionStringDetail(BaseSchema):
    # Serviceability swagger.json

    
    text = fields.Str(required=False, allow_none=True)
    
    value = fields.Str(required=False, allow_none=True)
    
    stage = fields.Boolean(required=False, allow_none=True)
    


class RuleResponseIntegerDetail(BaseSchema):
    # Serviceability swagger.json

    
    includes = fields.List(fields.Nested(RuleConditionIntegerDetail, required=False), required=False)
    


class RuleResponseStringDetail(BaseSchema):
    # Serviceability swagger.json

    
    includes = fields.List(fields.Nested(RuleConditionStringDetail, required=False), required=False)
    


class CourierPartnerRuleResponseDetailConditions(BaseSchema):
    # Serviceability swagger.json

    
    forward = fields.Nested(LocationRule, required=False)
    
    reverse = fields.Nested(LocationRule, required=False)
    
    payment_mode = fields.Nested(StringComparisonOperations, required=False)
    
    category_ids = fields.Nested(RuleResponseIntegerDetail, required=False)
    
    product_ids = fields.Nested(RuleResponseIntegerDetail, required=False)
    
    product_tags = fields.Nested(StringComparisonOperations, required=False)
    
    zone_ids = fields.Nested(RuleResponseStringDetail, required=False)
    
    department_ids = fields.Nested(RuleResponseIntegerDetail, required=False)
    
    brand_ids = fields.Nested(RuleResponseIntegerDetail, required=False)
    
    order_place_date = fields.Nested(ArithmeticOperationsV2, required=False)
    
    store_ids = fields.Nested(RuleResponseIntegerDetail, required=False)
    
    store_type = fields.Nested(StringComparisonOperations, required=False)
    
    store_tags = fields.Nested(StringComparisonOperations, required=False)
    
    shipment_weight = fields.Nested(ArithmeticOperations, required=False)
    
    shipment_cost = fields.Nested(ArithmeticOperations, required=False)
    
    shipment_volumetric_weight = fields.Nested(ArithmeticOperations, required=False)
    
    company_ids = fields.Nested(RuleResponseIntegerDetail, required=False)
    
    promise_types = fields.Nested(StringComparisonOperations, required=False)
    


class CourierPartnerRuleResponseDetailSchema(BaseSchema):
    # Serviceability swagger.json

    
    id = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    cp_list = fields.List(fields.Nested(CourierPartnerList, required=False), required=False)
    
    name = fields.Str(required=False)
    
    conditions = fields.Nested(CourierPartnerRuleResponseDetailConditions, required=False)
    
    manual_priority = fields.List(fields.Str(required=False), required=False)
    
    sort = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    
    application_id = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    shipment_adjustment_type = fields.Str(required=False, allow_none=True)
    


class StoreLocationDetail(BaseSchema):
    # Serviceability swagger.json

    
    uid = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    sub_type = fields.Str(required=False)
    
    parent_id = fields.Str(required=False, allow_none=True)
    
    parent_uid = fields.Str(required=False, allow_none=True)
    


class StoreRuleLocationDetailSchema(BaseSchema):
    # Serviceability swagger.json

    
    includes = fields.List(fields.Nested(StoreLocationDetail, required=False), required=False)
    


class StoreRuleConditionDetailSchema(BaseSchema):
    # Serviceability swagger.json

    
    department_ids = fields.Nested(RuleResponseIntegerDetail, required=False)
    
    category_ids = fields.Nested(RuleResponseIntegerDetail, required=False)
    
    brand_ids = fields.Nested(RuleResponseIntegerDetail, required=False)
    
    to_location = fields.Nested(StoreRuleLocationDetailSchema, required=False)
    
    customer_radius = fields.Nested(CustomerRadiusSchema, required=False)
    
    store_type = fields.Nested(StringComparisonOperations, required=False)
    
    product_tags = fields.Nested(StringComparisonOperations, required=False)
    
    product_ids = fields.Nested(RuleResponseIntegerDetail, required=False)
    
    store_tags = fields.Nested(StringComparisonOperations, required=False)
    
    order_place_date = fields.Nested(ArithmeticOperationsV2, required=False)
    
    zone_ids = fields.Nested(RuleResponseStringDetail, required=False)
    
    company_ids = fields.Nested(RuleResponseIntegerDetail, required=False)
    


class StoreRuleDataDetailsSchema(BaseSchema):
    # Serviceability swagger.json

    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    application_id = fields.Str(required=False)
    
    type_based_priority = fields.List(fields.Str(required=False), required=False)
    
    tag_based_priority = fields.List(fields.Str(required=False), required=False)
    
    store_priority = fields.List(fields.Nested(StorePrioritySchema, required=False), required=False)
    
    sort = fields.List(fields.Str(required=False), required=False)
    
    manual_priority = fields.List(fields.Int(required=False), required=False)
    
    conditions = fields.Nested(StoreRuleConditionDetailSchema, required=False)
    
    is_active = fields.Boolean(required=False)
    
    meta_sort_priority = fields.Dict(required=False, allow_none=True)
    
    meta_conditions = fields.Dict(required=False, allow_none=True)
    


class OptimalLocationArticlesResponse(BaseSchema):
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
    


class OptimalLocationAssignedStoresResponse(BaseSchema):
    # Serviceability swagger.json

    
    store_id = fields.Int(required=False)
    
    articles = fields.List(fields.Nested(OptimalLocationArticlesResponse, required=False), required=False)
    


class OptimalLocationsResponse(BaseSchema):
    # Serviceability swagger.json

    
    assigned_stores = fields.List(fields.Nested(OptimalLocationAssignedStoresResponse, required=False), required=False)
    
    faulty_articles = fields.List(fields.Nested(ErrorResponse, required=False), required=False)
    


class ArticleAssignment(BaseSchema):
    # Serviceability swagger.json

    
    level = fields.Str(required=False)
    
    strategy = fields.Str(required=False)
    


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
    


class OptimlLocationsRequestSchema(BaseSchema):
    # Serviceability swagger.json

    
    channel_id = fields.Str(required=False)
    
    channel_type = fields.Str(required=False)
    
    channel_identifier = fields.Str(required=False)
    
    to_serviceability = fields.Nested(LocationDetailsServiceability, required=False)
    
    articles = fields.List(fields.Nested(OptimalLocationsArticles, required=False), required=False)
    


class ErrorResponseV3(BaseSchema):
    # Serviceability swagger.json

    
    success = fields.Boolean(required=False)
    
    error = fields.Nested(ErrorObject, required=False)
    


class ErrorObject(BaseSchema):
    # Serviceability swagger.json

    
    type = fields.Str(required=False, allow_none=True)
    
    value = fields.Str(required=False, allow_none=True)
    
    message = fields.Str(required=False, allow_none=True)
    


class ValidateAddressRequest(BaseSchema):
    # Serviceability swagger.json

    
    address = fields.Str(required=False)
    
    address1 = fields.Str(required=False)
    
    address2 = fields.Str(required=False)
    
    area = fields.Str(required=False)
    
    landmark = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    
    sector = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    name = fields.Str(required=False, allow_none=True)
    
    phone = fields.Str(required=False, allow_none=True)
    
    email = fields.Str(required=False, allow_none=True)
    
    country_iso_code = fields.Str(required=False)
    


class CountryObject(BaseSchema):
    # Serviceability swagger.json

    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    iso2 = fields.Str(required=False)
    
    iso3 = fields.Str(required=False)
    
    timezones = fields.List(fields.Str(required=False), required=False)
    
    hierarchy = fields.List(fields.Nested(CountryHierarchy, required=False), required=False)
    
    phone_code = fields.Str(required=False)
    
    latitude = fields.Str(required=False)
    
    longitude = fields.Str(required=False)
    
    currency = fields.Nested(CurrencyObject, required=False)
    
    type = fields.Str(required=False)
    


class GetCountries(BaseSchema):
    # Serviceability swagger.json

    
    items = fields.List(fields.Nested(CountryObject, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class CurrencyObject(BaseSchema):
    # Serviceability swagger.json

    
    code = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    symbol = fields.Str(required=False)
    


class CountryHierarchy(BaseSchema):
    # Serviceability swagger.json

    
    display_name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    


class GetCountry(BaseSchema):
    # Serviceability swagger.json

    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    iso2 = fields.Str(required=False)
    
    iso3 = fields.Str(required=False)
    
    timezones = fields.List(fields.Str(required=False), required=False)
    
    hierarchy = fields.List(fields.Nested(CountryHierarchy, required=False), required=False)
    
    phone_code = fields.Str(required=False)
    
    latitude = fields.Str(required=False)
    
    longitude = fields.Str(required=False)
    
    currency = fields.Nested(CurrencyObject, required=False)
    
    type = fields.Str(required=False)
    
    fields = fields.Nested(GetCountryFields, required=False)
    


class GetCountryFields(BaseSchema):
    # Serviceability swagger.json

    
    address = fields.List(fields.Nested(GetCountryFieldsAddress, required=False), required=False)
    
    serviceability_fields = fields.List(fields.Str(required=False), required=False)
    
    address_template = fields.Nested(GetCountryFieldsAddressTemplate, required=False)
    


class GetCountryFieldsAddressTemplate(BaseSchema):
    # Serviceability swagger.json

    
    checkout_form = fields.Str(required=False)
    
    store_os_form = fields.Str(required=False)
    
    default_display = fields.Str(required=False)
    


class FieldValidation(BaseSchema):
    # Serviceability swagger.json

    
    type = fields.Str(required=False)
    
    regex = fields.Nested(FieldValidationRegex, required=False)
    


class FieldValidationRegex(BaseSchema):
    # Serviceability swagger.json

    
    value = fields.Str(required=False)
    
    length = fields.Nested(LengthValidation, required=False)
    


class LengthValidation(BaseSchema):
    # Serviceability swagger.json

    
    min = fields.Int(required=False, allow_none=True)
    
    max = fields.Int(required=False, allow_none=True)
    


class GetOneOrAllQuery(BaseSchema):
    # Serviceability swagger.json

    
    country = fields.Str(required=False, allow_none=True)
    
    state = fields.Str(required=False, allow_none=True)
    
    city = fields.Str(required=False, allow_none=True)
    
    sector = fields.Str(required=False, allow_none=True)
    


class GetOneOrAllPath(BaseSchema):
    # Serviceability swagger.json

    
    type = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class GetOneOrAllParams(BaseSchema):
    # Serviceability swagger.json

    
    path = fields.Nested(GetOneOrAllPath, required=False)
    
    query = fields.Nested(GetOneOrAllQuery, required=False)
    


class GetOneOrAll(BaseSchema):
    # Serviceability swagger.json

    
    operation_id = fields.Str(required=False)
    
    params = fields.Nested(GetOneOrAllParams, required=False)
    


class GetCountryFieldsAddressValues(BaseSchema):
    # Serviceability swagger.json

    
    get_one = fields.Nested(GetOneOrAll, required=False)
    
    get_all = fields.Nested(GetOneOrAll, required=False)
    


class GetCountryFieldsAddress(BaseSchema):
    # Serviceability swagger.json

    
    display_name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    required = fields.Boolean(required=False)
    
    edit = fields.Boolean(required=False)
    
    input = fields.Str(required=False)
    
    validation = fields.Nested(FieldValidation, required=False)
    
    values = fields.Nested(GetCountryFieldsAddressValues, required=False)
    
    error_text = fields.Str(required=False, allow_none=True)
    


class PincodeLatLongData(BaseSchema):
    # Serviceability swagger.json

    
    type = fields.Str(required=False)
    
    coordinates = fields.List(fields.Float(required=False), required=False)
    


class Localities(BaseSchema):
    # Serviceability swagger.json

    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    parent_ids = fields.List(fields.Str(required=False), required=False)
    
    meta = fields.Dict(required=False)
    
    type = fields.Str(required=False)
    
    lat_long = fields.Nested(PincodeLatLongData, required=False)
    
    parent_uid = fields.Str(required=False, allow_none=True)
    
    code = fields.Str(required=False)
    
    localities = fields.List(fields.Nested(LocalityParent, required=False), required=False)
    
    iso2 = fields.Str(required=False)
    
    iso3 = fields.Str(required=False)
    
    currency = fields.Dict(required=False)
    
    phone_code = fields.Str(required=False)
    
    hierarchy = fields.Dict(required=False)
    
    latitude = fields.Str(required=False)
    
    longitude = fields.Str(required=False)
    


class GetLocalities(BaseSchema):
    # Serviceability swagger.json

    
    items = fields.List(fields.Nested(Localities, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class LocalityParent(BaseSchema):
    # Serviceability swagger.json

    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    parent_ids = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    
    serviceability = fields.Dict(required=False)
    
    code = fields.Str(required=False)
    
    parent_uid = fields.Str(required=False, allow_none=True)
    
    iso2 = fields.Str(required=False)
    
    iso3 = fields.Str(required=False)
    
    currency = fields.Dict(required=False)
    
    phone_code = fields.Str(required=False)
    
    hierarchy = fields.Dict(required=False)
    
    latitude = fields.Str(required=False)
    
    longitude = fields.Str(required=False)
    


class GetLocality(BaseSchema):
    # Serviceability swagger.json

    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    parent_ids = fields.List(fields.Str(required=False), required=False)
    
    parent_uid = fields.Str(required=False, allow_none=True)
    
    type = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    localities = fields.List(fields.Nested(LocalityParent, required=False), required=False)
    


class ApplicationConfigPutResponse(BaseSchema):
    # Serviceability swagger.json

    
    rule_ids = fields.List(fields.Str(required=False), required=False)
    
    sort = fields.List(fields.Str(required=False), required=False)
    
    manual_priority = fields.List(fields.Str(required=False), required=False)
    
    application_id = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    


class PromiseType(BaseSchema):
    # Serviceability swagger.json

    
    display_name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    is_default = fields.Boolean(required=False)
    


class BuyboxRuleConfig(BaseSchema):
    # Serviceability swagger.json

    
    store_type_priority = fields.List(fields.Str(required=False), required=False)
    
    store_tag_priority = fields.List(fields.Str(required=False), required=False)
    
    sort = fields.List(fields.Str(required=False), required=False)
    


class CourierPartnerConfig(BaseSchema):
    # Serviceability swagger.json

    
    rule_ids = fields.List(fields.Str(required=False), required=False)
    
    sort = fields.List(fields.Str(required=False), required=False)
    
    manual_priority = fields.List(fields.Str(required=False), required=False)
    


class ZoneConfig(BaseSchema):
    # Serviceability swagger.json

    
    serviceability_type = fields.Str(required=False)
    
    active_count = fields.Int(required=False)
    
    total_count = fields.Int(required=False)
    


class ApplicationConfigGetResponse(BaseSchema):
    # Serviceability swagger.json

    
    zones = fields.Nested(ZoneConfig, required=False)
    
    courier_partner_config = fields.Nested(CourierPartnerConfig, required=False)
    
    buybox_rule_config = fields.Nested(BuyboxRuleConfig, required=False)
    
    promise_config = fields.Nested(PromiseConfig, required=False)
    
    promise_types = fields.List(fields.Nested(PromiseType, required=False), required=False)
    


class ApplicationConfigPutRequest(BaseSchema):
    # Serviceability swagger.json

    
    rule_ids = fields.List(fields.Str(required=False), required=False)
    
    sort = fields.List(fields.Str(required=False), required=False)
    
    manual_priority = fields.List(fields.Str(required=False), required=False)
    


class InstallCourierPartnerItemsSchema(BaseSchema):
    # Serviceability swagger.json

    
    base_url = fields.Str(required=False)
    
    callbacks = fields.Dict(required=False)
    
    contact_email = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    developed_by_name = fields.Str(required=False)
    
    ext_version = fields.Str(required=False)
    
    extention_type = fields.Str(required=False)
    
    is_coming_soon = fields.Boolean(required=False)
    
    is_hidden = fields.Boolean(required=False)
    
    is_installed = fields.Boolean(required=False)
    
    launch_type = fields.Str(required=False)
    
    logo = fields.Dict(required=False)
    
    modified_at = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    organization_id = fields.Str(required=False)
    
    partner = fields.Dict(required=False)
    
    scope = fields.List(fields.Str(required=False), required=False)
    
    whitelisted_urls = fields.List(fields.Str(required=False), required=False)
    
    __v = fields.Int(required=False)
    
    _id = fields.Str(required=False)
    


class InstallCourierPartnerResponseSchema(BaseSchema):
    # Serviceability swagger.json

    
    items = fields.List(fields.Nested(InstallCourierPartnerItemsSchema, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class UpdateZoneConfigRequest(BaseSchema):
    # Serviceability swagger.json

    
    serviceability_type = fields.Str(required=False)
    


class ServiceabilityErrorResponse(BaseSchema):
    # Serviceability swagger.json

    
    message = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class ApplicationServiceabilityConfig(BaseSchema):
    # Serviceability swagger.json

    
    channel_id = fields.Str(required=False)
    
    serviceability_type = fields.Str(required=False)
    
    channel_type = fields.Str(required=False)
    


class ApplicationServiceabilityConfigResponse(BaseSchema):
    # Serviceability swagger.json

    
    error = fields.Nested(ServiceabilityErrorResponse, required=False)
    
    data = fields.Nested(ApplicationServiceabilityConfig, required=False)
    
    success = fields.Boolean(required=False)
    


class EntityRegionView_Request(BaseSchema):
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
    


class getAppRegionZonesResponse(BaseSchema):
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
    


class EntityRegionView_Response(BaseSchema):
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
    


class ProductSchema(BaseSchema):
    # Serviceability swagger.json

    
    type = fields.Str(required=False)
    
    values = fields.List(fields.Int(required=False), required=False)
    


class ProductDetailsSchema(BaseSchema):
    # Serviceability swagger.json

    
    type = fields.Str(required=False)
    
    values = fields.List(fields.Nested(DetailsSchema, required=False), required=False)
    


class StoresSchema(BaseSchema):
    # Serviceability swagger.json

    
    type = fields.Str(required=False)
    
    values = fields.List(fields.Int(required=False), required=False)
    


class StoresDetailsSchema(BaseSchema):
    # Serviceability swagger.json

    
    type = fields.Str(required=False)
    
    values = fields.List(fields.Nested(StoreValueDetailsSchema, required=False), required=False)
    


class DetailsSchema(BaseSchema):
    # Serviceability swagger.json

    
    name = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class StoreValueDetailsSchema(BaseSchema):
    # Serviceability swagger.json

    
    text = fields.Str(required=False)
    
    value = fields.Int(required=False)
    


class SummarySchema(BaseSchema):
    # Serviceability swagger.json

    
    stores_count = fields.Int(required=False)
    
    products_count = fields.Int(required=False)
    
    regions = fields.List(fields.Nested(RegionSchema, required=False), required=False)
    


class RegionSchema(BaseSchema):
    # Serviceability swagger.json

    
    name = fields.Str(required=False)
    
    count = fields.Int(required=False)
    


class ServiceabilityDeleteErrorResponse(BaseSchema):
    # Serviceability swagger.json

    
    error = fields.List(fields.Nested(ServiceabilityErrorResponse, required=False), required=False)
    


class ListViewResponseV2(BaseSchema):
    # Serviceability swagger.json

    
    items = fields.List(fields.Nested(ListViewItemsV2, required=False), required=False)
    
    page = fields.Nested(ZoneDataItem, required=False)
    


class ListViewItemsV2(BaseSchema):
    # Serviceability swagger.json

    
    zone_id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    access_level = fields.Str(required=False)
    
    geo_areas = fields.List(fields.Nested(GeoArea, required=False), required=False)
    
    slug = fields.Str(required=False)
    
    stores = fields.Nested(ListViewProductV2, required=False)
    
    is_active = fields.Boolean(required=False)
    
    is_opted = fields.Boolean(required=False)
    
    is_public_opted = fields.Boolean(required=False)
    
    product = fields.Nested(ListViewProductV2, required=False)
    
    company_id = fields.Int(required=False)
    
    application_id = fields.Str(required=False)
    
    created_by = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    modified_by = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    summary = fields.Nested(Summary, required=False)
    


class SummaryRegions(BaseSchema):
    # Serviceability swagger.json

    
    regions = fields.List(fields.Nested(RegionSchema, required=False), required=False)
    


class Summary(BaseSchema):
    # Serviceability swagger.json

    
    stores_count = fields.Int(required=False)
    
    products_count = fields.Int(required=False)
    
    regions = fields.List(fields.Nested(RegionSchema, required=False), required=False)
    


class GeoArea(BaseSchema):
    # Serviceability swagger.json

    
    id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    


class ListViewProductV2(BaseSchema):
    # Serviceability swagger.json

    
    type = fields.Str(required=False)
    
    values = fields.List(fields.Str(required=False), required=False)
    


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
    
    channels = fields.List(fields.Nested(ListViewChannels, required=False), required=False)
    


class ListViewResponse(BaseSchema):
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
    


class UpdateZoneDataV2(BaseSchema):
    # Serviceability swagger.json

    
    zone_id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    access_level = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    geo_areas = fields.List(fields.Str(required=False), required=False)
    
    company_id = fields.Int(required=False)
    
    application_id = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    is_opted = fields.Boolean(required=False)
    
    product = fields.Nested(ProductSchema, required=False)
    
    stores = fields.Nested(StoresSchema, required=False)
    


class ZoneUpdateSuccessResponse(BaseSchema):
    # Serviceability swagger.json

    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    access_level = fields.Str(required=False)
    
    application_id = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    is_opted = fields.Boolean(required=False)
    
    geo_areas = fields.List(fields.Str(required=False), required=False)
    
    product = fields.Nested(ProductSchema, required=False)
    
    stores = fields.Nested(StoresSchema, required=False)
    
    zone_id = fields.Str(required=False)
    
    created_by = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    modified_by = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    summary = fields.Nested(Summary, required=False)
    


class ZoneDeleteSuccessResponse(BaseSchema):
    # Serviceability swagger.json

    
    message = fields.Str(required=False)
    


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
    


class GetSingleZoneDataViewResponse(BaseSchema):
    # Serviceability swagger.json

    
    data = fields.Nested(GetZoneDataViewItems, required=False)
    


class GetZoneByIdSchema(BaseSchema):
    # Serviceability swagger.json

    
    zone_id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    is_opted = fields.Boolean(required=False)
    
    product = fields.Nested(ProductSchema, required=False)
    
    stores = fields.Nested(StoresSchema, required=False)
    
    created_by = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    modified_by = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    overlapping_file_url = fields.Str(required=False, allow_none=True)
    
    geo_areas = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    
    overlapping_zone_names = fields.List(fields.Str(required=False), required=False)
    


class GetZoneByIdDetailsSchema(BaseSchema):
    # Serviceability swagger.json

    
    zone_id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    is_opted = fields.Boolean(required=False)
    
    product = fields.Nested(ProductDetailsSchema, required=False)
    
    stores = fields.Nested(StoresDetailsSchema, required=False)
    
    stage = fields.Str(required=False)
    
    overlapping_file_url = fields.Str(required=False, allow_none=True)
    
    geo_areas = fields.List(fields.Nested(GeoAreaDetailsSchema, required=False), required=False)
    
    type = fields.Str(required=False)
    
    access_level = fields.Str(required=False)
    
    overlapping_zone_names = fields.List(fields.Str(required=False), required=False)
    


class GeoAreaDetailsSchema(BaseSchema):
    # Serviceability swagger.json

    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    


class CreateZoneV2Data(BaseSchema):
    # Serviceability swagger.json

    
    is_active = fields.Boolean(required=False)
    
    slug = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    access_level = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    application_id = fields.Str(required=False)
    
    geo_areas = fields.List(fields.Str(required=False), required=False)
    
    stores = fields.Nested(ZoneStores, required=False)
    
    product = fields.Nested(ZoneProduct, required=False)
    


class ZoneBulkExport(BaseSchema):
    # Serviceability swagger.json

    
    batch_id = fields.Str(required=False)
    


class GetZoneBulkExport(BaseSchema):
    # Serviceability swagger.json

    
    items = fields.List(fields.Nested(ZoneBulkItem, required=False), required=False)
    


class ZoneBulkItem(BaseSchema):
    # Serviceability swagger.json

    
    batch_id = fields.Str(required=False)
    
    file_path = fields.Str(required=False, allow_none=True)
    
    total = fields.Int(required=False)
    
    failed = fields.Int(required=False)
    
    error_file_url = fields.Str(required=False, allow_none=True)
    
    action = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    updated_by = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    


class CreateBulkZoneData(BaseSchema):
    # Serviceability swagger.json

    
    file_url = fields.Str(required=False)
    
    product_type = fields.Str(required=False)
    


class ZoneStores(BaseSchema):
    # Serviceability swagger.json

    
    type = fields.Str(required=False)
    
    values = fields.List(fields.Int(required=False), required=False)
    


class ZoneProduct(BaseSchema):
    # Serviceability swagger.json

    
    type = fields.Str(required=False)
    
    values = fields.List(fields.Int(required=False), required=False)
    


class ZoneResponseV2(BaseSchema):
    # Serviceability swagger.json

    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    access_level = fields.Str(required=False)
    
    application_id = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    is_public_opted = fields.Boolean(required=False)
    
    is_opted = fields.Boolean(required=False)
    
    geo_areas = fields.List(fields.Str(required=False), required=False)
    
    stores = fields.Nested(ListViewProductV2, required=False)
    
    product = fields.Nested(ListViewProductV2, required=False)
    
    created_by = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    modified_by = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    zone_id = fields.Str(required=False)
    
    summary = fields.Nested(SummaryRegions, required=False)
    


class CreateBulkZoneResponse(BaseSchema):
    # Serviceability swagger.json

    
    zone_id = fields.Str(required=False)
    


class GetBulkZoneHistory(BaseSchema):
    # Serviceability swagger.json

    
    items = fields.List(fields.Nested(BulkZoneItems, required=False), required=False)
    
    page = fields.Nested(PageV2, required=False)
    


class BulkZoneItems(BaseSchema):
    # Serviceability swagger.json

    
    batch_id = fields.Str(required=False)
    
    entity_type = fields.Str(required=False)
    
    error_file_url = fields.Str(required=False, allow_none=True)
    
    file_path = fields.Str(required=False)
    
    file_name = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    updated_by = fields.Str(required=False, allow_none=True)
    
    stage = fields.Str(required=False)
    


class PageV2(BaseSchema):
    # Serviceability swagger.json

    
    type = fields.Str(required=False)
    
    size = fields.Float(required=False)
    
    current = fields.Float(required=False)
    
    has_next = fields.Boolean(required=False)
    
    item_total = fields.Float(required=False)
    


class BulkCreateZoneExport(BaseSchema):
    # Serviceability swagger.json

    
    placeholder = fields.Str(required=False)
    


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
    
    assignment_preference = fields.Str(required=False)
    


class ZoneResponse(BaseSchema):
    # Serviceability swagger.json

    
    status_code = fields.Int(required=False)
    
    zone_id = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class GetZoneFromPincodeViewRequest(BaseSchema):
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
    
    assignment_preference = fields.Str(required=False)
    


class GetZoneFromPincodeViewResponse(BaseSchema):
    # Serviceability swagger.json

    
    serviceability_type = fields.Str(required=False)
    
    zones = fields.List(fields.Nested(Zone, required=False), required=False)
    


class GetZoneFromApplicationIdViewResponse(BaseSchema):
    # Serviceability swagger.json

    
    page = fields.List(fields.Nested(ZoneDataItem, required=False), required=False)
    
    items = fields.List(fields.Nested(ListViewItems, required=False), required=False)
    


class ServiceabilityPageResponse(BaseSchema):
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
    


class ManagerResponse(BaseSchema):
    # Serviceability swagger.json

    
    email = fields.Str(required=False)
    
    mobile_no = fields.Nested(MobileNo, required=False)
    
    name = fields.Str(required=False)
    


class ModifiedByResponse(BaseSchema):
    # Serviceability swagger.json

    
    username = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    


class IntegrationTypeResponse(BaseSchema):
    # Serviceability swagger.json

    
    inventory = fields.Str(required=False)
    
    order = fields.Str(required=False)
    


class ProductReturnConfigResponse(BaseSchema):
    # Serviceability swagger.json

    
    on_same_store = fields.Boolean(required=False)
    


class ContactNumberResponse(BaseSchema):
    # Serviceability swagger.json

    
    number = fields.Str(required=False)
    
    country_code = fields.Int(required=False)
    


class AddressResponse(BaseSchema):
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
    


class CreatedByResponse(BaseSchema):
    # Serviceability swagger.json

    
    username = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    


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
    


class WarningsResponse(BaseSchema):
    # Serviceability swagger.json

    
    store_address = fields.Str(required=False)
    


class OpeningClosing(BaseSchema):
    # Serviceability swagger.json

    
    minute = fields.Int(required=False)
    
    hour = fields.Int(required=False)
    


class TimmingResponse(BaseSchema):
    # Serviceability swagger.json

    
    open = fields.Boolean(required=False)
    
    weekday = fields.Str(required=False)
    
    closing = fields.Nested(OpeningClosing, required=False)
    
    opening = fields.Nested(OpeningClosing, required=False)
    


class DocumentsResponse(BaseSchema):
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
    


class LogisticsResponse(BaseSchema):
    # Serviceability swagger.json

    
    override = fields.Boolean(required=False)
    
    dp = fields.Nested(Dp, required=False)
    


class ItemResponse(BaseSchema):
    # Serviceability swagger.json

    
    created_on = fields.Str(required=False)
    
    manager = fields.Nested(ManagerResponse, required=False)
    
    modified_by = fields.Nested(ModifiedByResponse, required=False)
    
    integration_type = fields.Nested(IntegrationTypeResponse, required=False)
    
    verified_on = fields.Str(required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigResponse, required=False)
    
    contact_numbers = fields.List(fields.Nested(ContactNumberResponse, required=False), required=False)
    
    verified_by = fields.Nested(ModifiedByResponse, required=False)
    
    stage = fields.Str(required=False)
    
    address = fields.Nested(AddressResponse, required=False)
    
    modified_on = fields.Str(required=False)
    
    created_by = fields.Nested(CreatedByResponse, required=False)
    
    gst_credentials = fields.Nested(GstCredentialsResponse, required=False)
    
    display_name = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    uid = fields.Int(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    code = fields.Str(required=False)
    
    warnings = fields.Nested(WarningsResponse, required=False)
    
    name = fields.Str(required=False)
    
    timing = fields.List(fields.Nested(TimmingResponse, required=False), required=False)
    
    documents = fields.List(fields.Nested(DocumentsResponse, required=False), required=False)
    
    store_type = fields.Str(required=False)
    
    sub_type = fields.Str(required=False)
    
    company = fields.Int(required=False)
    
    _cls = fields.Str(required=False)
    
    logistics = fields.Nested(LogisticsResponse, required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    


class GetStoresViewResponse(BaseSchema):
    # Serviceability swagger.json

    
    page = fields.Nested(ServiceabilityPageResponse, required=False)
    
    items = fields.List(fields.Nested(ItemResponse, required=False), required=False)
    


class ReAssignStoreRequest(BaseSchema):
    # Serviceability swagger.json

    
    to_pincode = fields.Str(required=False)
    
    identifier = fields.Str(required=False)
    
    configuration = fields.Dict(required=False)
    
    ignored_locations = fields.List(fields.Str(required=False), required=False)
    
    articles = fields.List(fields.Dict(required=False), required=False)
    


class ServiceabilityZoneErrorResult(BaseSchema):
    # Serviceability swagger.json

    
    error = fields.List(fields.Nested(ServiceabilityErrorResponse, required=False), required=False)
    


class ServiceabilityZoneNonMarketplaceErrorResult(BaseSchema):
    # Serviceability swagger.json

    
    error = fields.Str(required=False)
    


class ReAssignStoreResponse(BaseSchema):
    # Serviceability swagger.json

    
    to_pincode = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    error = fields.Dict(required=False)
    
    articles = fields.List(fields.Dict(required=False), required=False)
    


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

    
    batch_id = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    status_code = fields.Int(required=False)
    
    country = fields.Str(required=False)
    
    action = fields.Str(required=False)
    
    pincodes = fields.List(fields.Int(required=False), required=False)
    
    updated_pincodes = fields.List(fields.Nested(PincodeMopUpdateResponse, required=False), required=False)
    


class CommonError(BaseSchema):
    # Serviceability swagger.json

    
    status_code = fields.Int(required=False)
    
    error = fields.List(fields.Nested(ErrorResponse, required=False), required=False)
    
    success = fields.Boolean(required=False)
    


class MoPCommonError(BaseSchema):
    # Serviceability swagger.json

    
    batch_id = fields.Str(required=False)
    
    status_code = fields.Int(required=False)
    
    error = fields.List(fields.Nested(ErrorResponse, required=False), required=False)
    
    success = fields.Boolean(required=False)
    


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
    
    pincode = fields.Int(required=False, allow_none=True)
    
    current = fields.Int(required=False)
    
    page_size = fields.Int(required=False)
    


class PincodeCodDataSchema(BaseSchema):
    # Serviceability swagger.json

    
    pincode = fields.Str(required=False)
    
    active = fields.Boolean(required=False)
    


class PincodeCodStatusListingResponse(BaseSchema):
    # Serviceability swagger.json

    
    country = fields.Str(required=False)
    
    data = fields.List(fields.Nested(PincodeCodDataSchema, required=False), required=False)
    
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
    


class CourierAccount(BaseSchema):
    # Serviceability swagger.json

    
    extension_id = fields.Str(required=False)
    
    account_id = fields.Str(required=False)
    
    scheme_id = fields.Str(required=False)
    
    is_self_ship = fields.Boolean(required=False)
    
    stage = fields.Str(required=False)
    
    is_own_account = fields.Boolean(required=False)
    
    company_id = fields.Int(required=False)
    
    scheme_rules = fields.Dict(required=False)
    


class BulkGeoAreaDetails(BaseSchema):
    # Serviceability swagger.json

    
    file_url = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class BulkGeoAreaResult(BaseSchema):
    # Serviceability swagger.json

    
    geoarea_id = fields.Str(required=False)
    


class PriceGeoAreaExportResult(BaseSchema):
    # Serviceability swagger.json

    
    batch_id = fields.Str(required=False)
    


class BulkGeoAreaGetResponse(BaseSchema):
    # Serviceability swagger.json

    
    batch_id = fields.Str(required=False)
    
    file_path = fields.Str(required=False, allow_none=True)
    
    total = fields.Int(required=False)
    
    failed = fields.Int(required=False)
    
    error_file_url = fields.Str(required=False, allow_none=True)
    
    action = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    updated_by = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    file_url = fields.Str(required=False, allow_none=True)
    


class GeoAreaBulkCreationResult(BaseSchema):
    # Serviceability swagger.json

    
    batch_id = fields.Str(required=False)
    


class GeoAreaBulkExportResult(BaseSchema):
    # Serviceability swagger.json

    
    batch_id = fields.Str(required=False)
    
    file_path = fields.Str(required=False, allow_none=True)
    
    total = fields.Int(required=False)
    
    failed = fields.Int(required=False)
    
    error_file_url = fields.Str(required=False, allow_none=True)
    
    action = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    updated_by = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    


class GeoAreaRequestBody(BaseSchema):
    # Serviceability swagger.json

    
    is_active = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    areas = fields.List(fields.Nested(Area, required=False), required=False)
    
    region_type = fields.Str(required=False)
    


class GeoAreaErrorResult(BaseSchema):
    # Serviceability swagger.json

    
    error = fields.List(fields.Nested(GeoAreaResponseDetail, required=False), required=False)
    


class ErrorResponseItem(BaseSchema):
    # Serviceability swagger.json

    
    message = fields.Str(required=False)
    
    error_name = fields.Str(required=False)
    
    error_code = fields.Int(required=False)
    
    value = fields.Str(required=False)
    
    conflicting_areas = fields.List(fields.Nested(ConflictingArea, required=False), required=False)
    


class ConflictingArea(BaseSchema):
    # Serviceability swagger.json

    
    geoarea_id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    


class GeoAreaResponseDetail(BaseSchema):
    # Serviceability swagger.json

    
    type = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    message = fields.Str(required=False)
    


class ErrorResponseDetail(BaseSchema):
    # Serviceability swagger.json

    
    items = fields.List(fields.Nested(ErrorResponseItem, required=False), required=False)
    


class GeoAreaResponseBody(BaseSchema):
    # Serviceability swagger.json

    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    areas = fields.List(fields.Nested(Area, required=False), required=False)
    
    region_type = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    created_by = fields.Str(required=False)
    
    modified_by = fields.Str(required=False)
    
    geoarea_id = fields.Str(required=False)
    


class GeoAreaPutResponseBody(BaseSchema):
    # Serviceability swagger.json

    
    name = fields.Str(required=False)
    
    geoarea_id = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    areas = fields.List(fields.Nested(Area, required=False), required=False)
    
    region_type = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    created_by = fields.Str(required=False)
    
    modified_by = fields.Str(required=False)
    
    upload_type = fields.Str(required=False)
    


class Area(BaseSchema):
    # Serviceability swagger.json

    
    regions = fields.List(fields.Str(required=False), required=False)
    
    country = fields.Str(required=False)
    


class Region(BaseSchema):
    # Serviceability swagger.json

    
    uid = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    sub_type = fields.Str(required=False)
    
    parent_id = fields.List(fields.Str(required=False), required=False)
    


class RegionV2(BaseSchema):
    # Serviceability swagger.json

    
    uid = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    sub_type = fields.Str(required=False)
    
    parent_id = fields.List(fields.Str(required=False), required=False)
    


class Country(BaseSchema):
    # Serviceability swagger.json

    
    uid = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    


class AreaExpanded(BaseSchema):
    # Serviceability swagger.json

    
    country = fields.Nested(Country, required=False)
    
    regions = fields.List(fields.Nested(Region, required=False), required=False)
    


class AreaExpandedV2(BaseSchema):
    # Serviceability swagger.json

    
    country = fields.Nested(Country, required=False)
    
    regions = fields.List(fields.Nested(RegionV2, required=False), required=False)
    


class GeoAreaResponse(BaseSchema):
    # Serviceability swagger.json

    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    application_id = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    geoarea_id = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    
    region_type = fields.Str(required=False)
    
    areas = fields.List(fields.Nested(AreaExpanded, required=False), required=False)
    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    created_by = fields.Str(required=False)
    
    modified_by = fields.Str(required=False)
    


class GeoAreaGetResponseBody(BaseSchema):
    # Serviceability swagger.json

    
    items = fields.List(fields.Nested(GeoAreaItemResponse, required=False), required=False)
    
    page = fields.Nested(Page2, required=False)
    


class GeoAreaItemResponse(BaseSchema):
    # Serviceability swagger.json

    
    company_id = fields.Int(required=False)
    
    application_id = fields.Str(required=False)
    
    geoarea_id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    region_type = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    areas = fields.List(fields.Nested(AreaExpandedV2, required=False), required=False)
    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    created_by = fields.Str(required=False)
    
    modified_by = fields.Str(required=False)
    


class ErrorResponseV2(BaseSchema):
    # Serviceability swagger.json

    
    success = fields.Boolean(required=False)
    
    error = fields.Str(required=False)
    


class ErrorResponse(BaseSchema):
    # Serviceability swagger.json

    
    value = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    error = fields.Str(required=False)
    


class PackageMaterialNotFound(BaseSchema):
    # Serviceability swagger.json

    
    status_code = fields.Int(required=False)
    
    success = fields.Boolean(required=False)
    


class PackageMaterialsErrorResponse(BaseSchema):
    # Serviceability swagger.json

    
    value = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    error = fields.Str(required=False)
    


class CourierPartnerAccountFailureResponse(BaseSchema):
    # Serviceability swagger.json

    
    success = fields.Boolean(required=False)
    
    error = fields.List(fields.Nested(ErrorResponse, required=False), required=False)
    


class Page(BaseSchema):
    # Serviceability swagger.json

    
    item_total = fields.Int(required=False)
    
    next_id = fields.Str(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    has_next = fields.Boolean(required=False)
    
    current = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    size = fields.Int(required=False)
    
    total = fields.Int(required=False)
    


class Page2(BaseSchema):
    # Serviceability swagger.json

    
    size = fields.Int(required=False)
    
    item_total = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    current = fields.Int(required=False)
    
    has_next = fields.Boolean(required=False)
    


class CourierPartnerList(BaseSchema):
    # Serviceability swagger.json

    
    extension_id = fields.Str(required=False)
    
    account_id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    is_self_ship = fields.Boolean(required=False)
    
    scheme_rules = fields.Dict(required=False)
    
    stage = fields.Str(required=False)
    


class LocationRuleValues(BaseSchema):
    # Serviceability swagger.json

    
    uid = fields.Str(required=False)
    
    sub_type = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    parent_uid = fields.Str(required=False)
    
    parent_id = fields.List(fields.Str(required=False), required=False)
    


class LocationRuleValuesV2(BaseSchema):
    # Serviceability swagger.json

    
    id = fields.Str(required=False)
    
    sub_type = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    parent_uid = fields.Str(required=False)
    
    parent_id = fields.List(fields.Str(required=False), required=False)
    


class LocationRule(BaseSchema):
    # Serviceability swagger.json

    
    type = fields.Str(required=False)
    
    includes = fields.List(fields.Nested(LocationRuleValues, required=False), required=False)
    


class LocationRuleV2(BaseSchema):
    # Serviceability swagger.json

    
    type = fields.Str(required=False)
    
    includes = fields.List(fields.Nested(LocationRuleValuesV2, required=False), required=False)
    


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
    
    order_place_date = fields.Nested(ArithmeticOperationsV2, required=False)
    
    store_ids = fields.Nested(IntComparisonOperations, required=False)
    
    store_type = fields.Nested(StringComparisonOperations, required=False)
    
    store_tags = fields.Nested(StringComparisonOperations, required=False)
    
    shipment_weight = fields.Nested(ArithmeticOperations, required=False)
    
    shipment_cost = fields.Nested(ArithmeticOperations, required=False)
    
    shipment_volumetric_weight = fields.Nested(ArithmeticOperations, required=False)
    
    company_ids = fields.Nested(IntComparisonOperations, required=False)
    
    promise_types = fields.Nested(StringComparisonOperations, required=False)
    


class CourierPartnerRuleResponseConditions(BaseSchema):
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
    
    order_place_date = fields.Nested(ArithmeticOperationsV2, required=False)
    
    store_ids = fields.Nested(IntComparisonOperations, required=False)
    
    store_type = fields.Nested(StringComparisonOperations, required=False)
    
    store_tags = fields.Nested(StringComparisonOperations, required=False)
    
    shipment_weight = fields.Nested(ArithmeticOperations, required=False)
    
    shipment_cost = fields.Nested(ArithmeticOperations, required=False)
    
    shipment_volumetric_weight = fields.Nested(ArithmeticOperations, required=False)
    
    company_ids = fields.Nested(IntComparisonOperations, required=False)
    
    promise_types = fields.Nested(StringComparisonOperations, required=False)
    


class CourierPartnerRule(BaseSchema):
    # Serviceability swagger.json

    
    id = fields.Str(required=False)
    
    application_id = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    cp_list = fields.List(fields.Nested(CourierPartnerList, required=False), required=False)
    
    name = fields.Str(required=False)
    
    conditions = fields.Nested(CourierPartnerRuleConditions, required=False)
    
    manual_priority = fields.List(fields.Str(required=False), required=False)
    
    sort = fields.List(fields.Str(required=False), required=False)
    
    shipment_adjustment_type = fields.Str(required=False, allow_none=True)
    
    type = fields.Str(required=False)
    


class CourierPartnerRuleResponse(BaseSchema):
    # Serviceability swagger.json

    
    is_active = fields.Boolean(required=False)
    
    cp_list = fields.List(fields.Nested(CourierPartnerList, required=False), required=False)
    
    name = fields.Str(required=False)
    
    conditions = fields.Nested(CourierPartnerRuleResponseConditions, required=False)
    
    manual_priority = fields.List(fields.Str(required=False), required=False)
    
    sort = fields.List(fields.Str(required=False), required=False)
    
    shipment_adjustment_type = fields.Str(required=False, allow_none=True)
    
    type = fields.Str(required=False)
    


class CourierPartnerRuleResponseSchema(BaseSchema):
    # Serviceability swagger.json

    
    id = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    cp_list = fields.List(fields.Nested(CourierPartnerList, required=False), required=False)
    
    name = fields.Str(required=False)
    
    conditions = fields.Nested(CourierPartnerRuleResponseConditions, required=False)
    
    manual_priority = fields.List(fields.Str(required=False), required=False)
    
    sort = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    
    application_id = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    shipment_adjustment_type = fields.Str(required=False, allow_none=True)
    


class FailureResponse(BaseSchema):
    # Serviceability swagger.json

    
    success = fields.Boolean(required=False)
    
    error = fields.List(fields.Nested(ErrorResponse, required=False), required=False)
    


class CourierPartnerRulesListResponse(BaseSchema):
    # Serviceability swagger.json

    
    items = fields.List(fields.Nested(CourierPartnerRuleResponseSchema, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class CompanyConfig(BaseSchema):
    # Serviceability swagger.json

    
    company_id = fields.Int(required=False)
    
    sort = fields.List(fields.Str(required=False), required=False)
    
    logistics_as_actual = fields.Str(required=False)
    


class StorePromiseAttributeConfig(BaseSchema):
    # Serviceability swagger.json

    
    is_operational_timing_enabled = fields.Boolean(required=False)
    
    is_order_acceptance_timing_enabled = fields.Boolean(required=False)
    
    is_average_processing_time = fields.Boolean(required=False)
    
    is_holiday_enabled = fields.Boolean(required=False)
    


class DeliveryServiceAttributeConfig(BaseSchema):
    # Serviceability swagger.json

    
    is_pickup_cutoff_time_enabled = fields.Boolean(required=False)
    
    is_service_tat_enabled = fields.Boolean(required=False)
    
    is_holiday_enabled = fields.Boolean(required=False)
    


class BufferField(BaseSchema):
    # Serviceability swagger.json

    
    unit = fields.Str(required=False)
    
    value = fields.Int(required=False)
    
    enabled = fields.Boolean(required=False)
    


class PromiseConfig(BaseSchema):
    # Serviceability swagger.json

    
    store_attributes = fields.Nested(StorePromiseAttributeConfig, required=False)
    
    delivery_service_attributes = fields.Nested(DeliveryServiceAttributeConfig, required=False)
    
    buffer_field = fields.Nested(BufferField, required=False)
    


class ApplicationConfig(BaseSchema):
    # Serviceability swagger.json

    
    rule_ids = fields.List(fields.Str(required=False), required=False)
    
    sort = fields.List(fields.Str(required=False), required=False)
    
    application_id = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    manual_priority = fields.List(fields.Str(required=False), required=False)
    
    zones = fields.Nested(ZoneConfig, required=False)
    
    buybox_rule_config = fields.Nested(BuyboxRuleConfig, required=False)
    
    promise_types = fields.List(fields.Nested(PromiseType, required=False), required=False)
    
    promise_config = fields.Nested(PromiseConfig, required=False)
    


class ApplicationConfigPatchRequest(BaseSchema):
    # Serviceability swagger.json

    
    courier_partner_config = fields.Nested(CourierPartnerConfig, required=False)
    
    buybox_rule_config = fields.Nested(BuyboxRuleConfig, required=False)
    
    promise_config = fields.Nested(PromiseConfig, required=False)
    


class ApplicationConfigPatchResponse(BaseSchema):
    # Serviceability swagger.json

    
    success = fields.Boolean(required=False)
    


class BulkRegionJobSerializer(BaseSchema):
    # Serviceability swagger.json

    
    file_path = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    action = fields.Str(required=False)
    
    region = fields.Str(required=False)
    


class BulkRegionResponseItemData(BaseSchema):
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
    


class BulkRegionResponse(BaseSchema):
    # Serviceability swagger.json

    
    items = fields.List(fields.Nested(BulkRegionResponseItemData, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class SelfShipResponse(BaseSchema):
    # Serviceability swagger.json

    
    is_active = fields.Boolean(required=False)
    
    tat = fields.Float(required=False)
    


class ApplicationSelfShipConfig(BaseSchema):
    # Serviceability swagger.json

    
    self_ship = fields.Dict(required=False, allow_none=True)
    


class ApplicationSelfShipConfigResponse(BaseSchema):
    # Serviceability swagger.json

    
    error = fields.Nested(ServiceabilityErrorResponse, required=False)
    
    data = fields.Nested(ApplicationSelfShipConfig, required=False)
    
    success = fields.Boolean(required=False)
    


class StoreRuleConfigData(BaseSchema):
    # Serviceability swagger.json

    
    rule_ids = fields.List(fields.Str(required=False), required=False)
    
    type_based_priority = fields.List(fields.Str(required=False), required=False)
    
    tag_based_priority = fields.List(fields.Str(required=False), required=False)
    
    store_priority = fields.List(fields.Nested(StorePrioritySchema, required=False), required=False)
    
    sort = fields.List(fields.Str(required=False), required=False)
    
    manual_priority = fields.List(fields.Int(required=False), required=False)
    
    meta_sort_priority = fields.Dict(required=False)
    


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
    
    to_location = fields.Nested(LocationRuleV2, required=False)
    
    customer_radius = fields.Nested(CustomerRadiusSchema, required=False)
    
    store_type = fields.Nested(StringComparisonOperations, required=False)
    
    product_tags = fields.Nested(StringComparisonOperations, required=False)
    
    product_ids = fields.Nested(IntComparisonOperations, required=False)
    
    store_tags = fields.Nested(StringComparisonOperations, required=False)
    
    order_place_date = fields.Nested(ArithmeticOperationsV2, required=False)
    
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
    
    manual_priority = fields.List(fields.Int(required=False), required=False)
    
    meta_sort_priority = fields.Dict(required=False)
    
    meta_conditions = fields.Dict(required=False)
    
    conditions = fields.Nested(StoreRuleConditionSchema, required=False)
    
    is_active = fields.Boolean(required=False)
    


class StorePrioritySchema(BaseSchema):
    # Serviceability swagger.json

    
    id = fields.Int(required=False)
    
    name = fields.Str(required=False)
    


class GetStoreRulesApiResponse(BaseSchema):
    # Serviceability swagger.json

    
    items = fields.List(fields.Nested(StoreRuleDataSchema, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class CreateStoreRuleRequestSchema(BaseSchema):
    # Serviceability swagger.json

    
    name = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    conditions = fields.Nested(StoreRuleConditionSchema, required=False)
    
    type_based_priority = fields.List(fields.Str(required=False), required=False)
    
    tag_based_priority = fields.List(fields.Str(required=False), required=False)
    
    store_priority = fields.List(fields.Nested(StorePrioritySchema, required=False), required=False)
    
    manual_priority = fields.List(fields.Int(required=False), required=False)
    
    sort = fields.List(fields.Str(required=False), required=False)
    


class StoreRuleResponseSchema(BaseSchema):
    # Serviceability swagger.json

    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    type_based_priority = fields.List(fields.Str(required=False), required=False)
    
    tag_based_priority = fields.List(fields.Str(required=False), required=False)
    
    store_priority = fields.List(fields.Nested(StorePrioritySchema, required=False), required=False)
    
    sort = fields.List(fields.Str(required=False), required=False)
    
    manual_priority = fields.List(fields.Int(required=False), required=False)
    
    conditions = fields.Nested(StoreRuleConditionSchema, required=False)
    
    is_active = fields.Boolean(required=False)
    


class StoreRuleUpdateResponseSchema(BaseSchema):
    # Serviceability swagger.json

    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    type_based_priority = fields.List(fields.Str(required=False), required=False)
    
    tag_based_priority = fields.List(fields.Str(required=False), required=False)
    
    store_priority = fields.List(fields.Nested(StorePrioritySchema, required=False), required=False)
    
    sort = fields.List(fields.Str(required=False), required=False)
    
    manual_priority = fields.List(fields.Int(required=False), required=False)
    
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
    


class CourierAccountSchemeResponse(BaseSchema):
    # Serviceability swagger.json

    
    name = fields.Str(required=False)
    
    extension_id = fields.Str(required=False)
    
    scheme_id = fields.Str(required=False)
    
    weight = fields.Nested(ArithmeticOperations, required=False)
    
    transport_type = fields.Str(required=False)
    
    region = fields.Str(required=False)
    
    delivery_type = fields.Str(required=False)
    
    payment_mode = fields.List(fields.Str(required=False), required=False)
    
    stage = fields.Str(required=False)
    
    feature = fields.Nested(CourierPartnerSchemeFeatures, required=False)
    


class CourierAccountResponse(BaseSchema):
    # Serviceability swagger.json

    
    company_id = fields.Int(required=False)
    
    extension_id = fields.Str(required=False)
    
    account_id = fields.Str(required=False)
    
    scheme_id = fields.Str(required=False)
    
    is_self_ship = fields.Boolean(required=False)
    
    stage = fields.Str(required=False)
    
    is_own_account = fields.Boolean(required=False)
    
    scheme_rules = fields.Nested(CourierAccountSchemeResponse, required=False)
    


class CompanyCourierPartnerAccountListResponse(BaseSchema):
    # Serviceability swagger.json

    
    items = fields.List(fields.Nested(CourierAccountResponse, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class PackageMaterial(BaseSchema):
    # Serviceability swagger.json

    
    company_id = fields.Float(required=False)
    
    item_id = fields.Float(required=False)
    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    width = fields.Float(required=False)
    
    height = fields.Float(required=False)
    
    length = fields.Float(required=False)
    
    weight = fields.Float(required=False)
    
    auto_calculate = fields.Boolean(required=False)
    
    max_weight = fields.Float(required=False)
    
    package_vol_weight = fields.Float(required=False)
    
    error_rate = fields.Float(required=False)
    
    channels = fields.List(fields.Nested(Channel, required=False), required=False)
    
    package_type = fields.Str(required=False)
    
    size = fields.Str(required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    rules = fields.List(fields.Nested(PackageMaterialRule, required=False), required=False)
    
    store_ids = fields.List(fields.Int(required=False), required=False)
    
    mp_stores = fields.List(fields.Nested(PackageMpStores, required=False), required=False)
    
    media = fields.List(fields.Str(required=False), required=False)
    
    status = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    


class PackageMaterialResponse(BaseSchema):
    # Serviceability swagger.json

    
    company_id = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    item_id = fields.Int(required=False)
    
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
    
    is_active = fields.Boolean(required=False)
    
    status = fields.Str(required=False)
    
    max_weight = fields.Float(required=False)
    
    package_vol_weight = fields.Float(required=False)
    
    auto_calculate = fields.Boolean(required=False)
    
    mp_stores = fields.List(fields.Nested(PackageMpStores, required=False), required=False)
    


class PackageMaterialRule(BaseSchema):
    # Serviceability swagger.json

    
    rule_id = fields.Str(required=False)
    
    quantity = fields.Nested(PackageMaterialRuleQuantity, required=False)
    
    weight = fields.Int(required=False)
    
    company_id = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    id = fields.Str(required=False)
    


class PackageMpStores(BaseSchema):
    # Serviceability swagger.json

    
    app_name = fields.Str(required=False)
    
    app_id = fields.Str(required=False)
    
    store_ids = fields.List(fields.Int(required=False), required=False)
    
    store_data = fields.Raw(required=False)
    


class PackageRuleRequest(BaseSchema):
    # Serviceability swagger.json

    
    name = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    category_id = fields.Nested(PackageRuleCategory, required=False)
    
    product_id = fields.Nested(PackageRuleProduct, required=False)
    
    product_tag = fields.Nested(PackageRuleProductTag, required=False)
    
    department_id = fields.Nested(PackageRuleDepartmentId, required=False)
    
    product_attributes = fields.Nested(PackageRuleProductAttributes, required=False)
    
    type = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    


class PackageRule(BaseSchema):
    # Serviceability swagger.json

    
    name = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    item_id = fields.Int(required=False)
    
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
    
    mp_stores = fields.List(fields.Nested(PackageMpStores, required=False), required=False)
    


class PackageRuleResult(BaseSchema):
    # Serviceability swagger.json

    
    is_active = fields.Boolean(required=False)
    
    company_id = fields.Int(required=False)
    
    product_id = fields.Nested(PackageRuleProduct, required=False)
    
    category_id = fields.Nested(PackageRuleCategory, required=False)
    
    department_id = fields.Nested(PackageRuleDepartmentId, required=False)
    
    product_tag = fields.Nested(PackageRuleProductTag, required=False)
    
    product_attributes = fields.Nested(PackageRuleProductAttributes, required=False)
    
    name = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    id = fields.Str(required=False)
    


class Channel(BaseSchema):
    # Serviceability swagger.json

    
    type = fields.Str(required=False)
    
    id = fields.Str(required=False)
    


class PackageMaterialRuleList(BaseSchema):
    # Serviceability swagger.json

    
    items = fields.List(fields.Nested(PackageRuleResult, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class PackageMaterialList(BaseSchema):
    # Serviceability swagger.json

    
    items = fields.Raw(required=False)
    
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
    


class PackageRuleProductAttributes(BaseSchema):
    # Serviceability swagger.json

    
    includes = fields.List(fields.Dict(required=False), required=False)
    


class PackageRuleDepartmentId(BaseSchema):
    # Serviceability swagger.json

    
    includes = fields.List(fields.Int(required=False), required=False)
    


class PackageMaterialRuleQuantity(BaseSchema):
    # Serviceability swagger.json

    
    min = fields.Int(required=False)
    
    max = fields.Int(required=False)
    


class RulePriorityRequest(BaseSchema):
    # Serviceability swagger.json

    
    rule_id = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    


class RulePriorityResponse(BaseSchema):
    # Serviceability swagger.json

    
    success = fields.Boolean(required=False)
    


class CompanySelfShip(BaseSchema):
    # Serviceability swagger.json

    
    is_active = fields.Boolean(required=False)
    
    tat = fields.Float(required=False)
    
    unit = fields.Str(required=False)
    


class ArithmeticOperationsV2(BaseSchema):
    # Serviceability swagger.json

    
    lt = fields.Str(required=False)
    
    gt = fields.Str(required=False)
    
    lte = fields.Str(required=False)
    
    gte = fields.Str(required=False)
    


class CompanyConfigurationShema(BaseSchema):
    # Serviceability swagger.json

    
    sort = fields.List(fields.Str(required=False), required=False)
    


