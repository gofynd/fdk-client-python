"""Serviceability Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




class PlatformShipmentsRequestSchema(BaseSchema):
    pass


class PlatformShipmentsResponseSchema(BaseSchema):
    pass


class ShipmentsErrorResult(BaseSchema):
    pass


class FulfillmentOption(BaseSchema):
    pass


class FulfillmentOptionsList(BaseSchema):
    pass


class FulfillmentOptionProducts(BaseSchema):
    pass


class FulfillmentOptionStores(BaseSchema):
    pass


class FulfillmentOptionBulkValidate(BaseSchema):
    pass


class FulfillmentOptionBulkValidateData(BaseSchema):
    pass


class FulfillmentOptionBulk(BaseSchema):
    pass


class FulfillmentOptionBulkData(BaseSchema):
    pass


class OperationResponseSchema(BaseSchema):
    pass


class SelfshipSchema(BaseSchema):
    pass


class ServiceabilityErrorResult(BaseSchema):
    pass


class UpdateZoneData(BaseSchema):
    pass


class ZoneUpdateSuccessResult(BaseSchema):
    pass


class ServiceabilityDeleteErrorResult(BaseSchema):
    pass


class ZoneDeleteSuccessResult(BaseSchema):
    pass


class ListViewSchema(BaseSchema):
    pass


class GetZoneByIdSchema(BaseSchema):
    pass


class CommonErrorResult(BaseSchema):
    pass


class CreateZoneDataSchema(BaseSchema):
    pass


class ZoneBulkExport(BaseSchema):
    pass


class GetZoneBulkExport(BaseSchema):
    pass


class CreateBulkZoneData(BaseSchema):
    pass


class ZoneSchema(BaseSchema):
    pass


class CreateBulkZoneResult(BaseSchema):
    pass


class BulkCreateZoneExport(BaseSchema):
    pass


class PincodeMopData(BaseSchema):
    pass


class PincodeMOPResult(BaseSchema):
    pass


class PincodeMopUpdateAuditError(BaseSchema):
    pass


class PincodeMopBulkError(BaseSchema):
    pass


class CommonError(BaseSchema):
    pass


class PincodeMopBulkData(BaseSchema):
    pass


class PincodeBulkViewResult(BaseSchema):
    pass


class PincodeCodStatusListingDetails(BaseSchema):
    pass


class PincodeCodStatusListingResult(BaseSchema):
    pass


class PincodeMopUpdateAuditHistoryDetails(BaseSchema):
    pass


class PincodeMopUpdateAuditHistoryResultData(BaseSchema):
    pass


class BulkGeoAreaDetails(BaseSchema):
    pass


class BulkGeoAreaResult(BaseSchema):
    pass


class BulkGeoAreaGetResult(BaseSchema):
    pass


class GeoAreaBulkCreationResult(BaseSchema):
    pass


class GeoAreaBulkExportResult(BaseSchema):
    pass


class GeoAreaRequestBody(BaseSchema):
    pass


class GeoAreaErrorResult(BaseSchema):
    pass


class GeoAreaResponseBody(BaseSchema):
    pass


class GeoAreaPutResponseBody(BaseSchema):
    pass


class GeoAreaGetResponseBody(BaseSchema):
    pass


class GeoAreaDetails(BaseSchema):
    pass


class Error(BaseSchema):
    pass


class CourierAccountDetailsBody(BaseSchema):
    pass


class CourierPartnerRuleResult(BaseSchema):
    pass


class CourierPartnerRule(BaseSchema):
    pass


class BulkFailureResult(BaseSchema):
    pass


class FailureResult(BaseSchema):
    pass


class CourierPartnerRulesListResult(BaseSchema):
    pass


class ShipmentCourierPartnerDetails(BaseSchema):
    pass


class ShipmentCourierPartnerResult(BaseSchema):
    pass


class CompanyConfig(BaseSchema):
    pass


class ApplicationConfigPatch(BaseSchema):
    pass


class ApplicationConfigPatchResult(BaseSchema):
    pass


class BulkRegionJobDetails(BaseSchema):
    pass


class BulkRegionResultItemData(BaseSchema):
    pass


class BulkRegionResult(BaseSchema):
    pass


class StoreRuleConfigData(BaseSchema):
    pass


class StoreRuleDataSchema(BaseSchema):
    pass


class GetStoreRulesApiResult(BaseSchema):
    pass


class CreateStoreRuleDetailsSchema(BaseSchema):
    pass


class StoreRuleResultSchema(BaseSchema):
    pass


class StoreRuleUpdateResultSchema(BaseSchema):
    pass


class CourierAccountResult(BaseSchema):
    pass


class CompanyCourierPartnerAccountListResult(BaseSchema):
    pass


class PackageMaterial(BaseSchema):
    pass


class PackageMaterialNotFound(BaseSchema):
    pass


class PackageMaterialsErrorResult(BaseSchema):
    pass


class PackageMaterialResult(BaseSchema):
    pass


class PackageRule(BaseSchema):
    pass


class PackageRuleResult(BaseSchema):
    pass


class PackagesListResult(BaseSchema):
    pass


class PackageItem(BaseSchema):
    pass


class RulePriorityDetails(BaseSchema):
    pass


class RulePriorityResult(BaseSchema):
    pass


class OptimalLocationsResult(BaseSchema):
    pass


class OptimlLocationsRequestSchema(BaseSchema):
    pass


class ValidationError(BaseSchema):
    pass


class StandardError(BaseSchema):
    pass


class CourierPartnerSchemeDetailsModel(BaseSchema):
    pass


class CourierPartnerSchemeModelSchema(BaseSchema):
    pass


class CourierPartnerSchemeUpdateDetailsSchema(BaseSchema):
    pass


class CourierPartnerSchemeList(BaseSchema):
    pass


class BulkRegionServiceabilityTatDetails(BaseSchema):
    pass


class BulkRegionServiceabilityTatResultItemData(BaseSchema):
    pass


class BulkRegionServiceabilityTatResult(BaseSchema):
    pass


class GetCountries(BaseSchema):
    pass


class GetLocalities(BaseSchema):
    pass


class GetCountry(BaseSchema):
    pass


class BulkImportLocalitiesDetails(BaseSchema):
    pass


class BulkImportLocalitiesResult(BaseSchema):
    pass


class BulkErrorResult(BaseSchema):
    pass


class LocalitiesBulkExport(BaseSchema):
    pass


class LocalitiesBulkExportFetch(BaseSchema):
    pass


class LocalitiesErrorResult(BaseSchema):
    pass


class GetLocality(BaseSchema):
    pass


class ValidateAddress(BaseSchema):
    pass


class ErrorResult(BaseSchema):
    pass


class ApplicationConfigPut(BaseSchema):
    pass


class ApplicationConfigPutDetail(BaseSchema):
    pass


class ApplicationConfigGetResult(BaseSchema):
    pass


class InstallCourierPartnerResponseSchema(BaseSchema):
    pass


class GetLocalitiesBulkHistory(BaseSchema):
    pass


class CompanyConfigurationSchema(BaseSchema):
    pass


class PlatformLocationArticles(BaseSchema):
    pass


class PlatformLocationArticle(BaseSchema):
    pass


class ParentItemIdentifiers(BaseSchema):
    pass


class PlatformShipmentsToServiceability(BaseSchema):
    pass


class PlatformShipmentsSchema(BaseSchema):
    pass


class Packaging(BaseSchema):
    pass


class Dimension(BaseSchema):
    pass


class FulfillmentOptionItem(BaseSchema):
    pass


class ShipmentsPromise(BaseSchema):
    pass


class CustomerPromise(BaseSchema):
    pass


class ShipmentPromiseMeta(BaseSchema):
    pass


class SellerPromise(BaseSchema):
    pass


class CourierPartnerPromise(BaseSchema):
    pass


class CourierPartnerAttributes(BaseSchema):
    pass


class CourierPartnerTAT(BaseSchema):
    pass


class CustomerInitialPromise(BaseSchema):
    pass


class ShipmentsArticle(BaseSchema):
    pass


class ShipmentDimension(BaseSchema):
    pass


class ShipmentsMeta(BaseSchema):
    pass


class ShipmentsCourierPartner(BaseSchema):
    pass


class AreaCode(BaseSchema):
    pass


class TAT(BaseSchema):
    pass


class BusinessUnit(BaseSchema):
    pass


class FulfillmentStores(BaseSchema):
    pass


class FulfillmentProducts(BaseSchema):
    pass


class CourierPartnerSchemes(BaseSchema):
    pass


class CourierPartnerScheme(BaseSchema):
    pass


class FulfillmentOptionProduct(BaseSchema):
    pass


class NetQuantity(BaseSchema):
    pass


class Trader(BaseSchema):
    pass


class ProductPublish(BaseSchema):
    pass


class TaxIdentifier(BaseSchema):
    pass


class ReturnConfig(BaseSchema):
    pass


class CustomOrder(BaseSchema):
    pass


class Size(BaseSchema):
    pass


class Identifier(BaseSchema):
    pass


class Page(BaseSchema):
    pass


class FulfillmentOptionStore(BaseSchema):
    pass


class Address(BaseSchema):
    pass


class LatLong(BaseSchema):
    pass


class StoreDistance(BaseSchema):
    pass


class StoreTimingDetails(BaseSchema):
    pass


class StoreTiming(BaseSchema):
    pass


class Time(BaseSchema):
    pass


class FulfillmentOptionValidate(BaseSchema):
    pass


class ProductSchema(BaseSchema):
    pass


class StoresSchema(BaseSchema):
    pass


class CreatedBy(BaseSchema):
    pass


class ModifiedBy(BaseSchema):
    pass


class ListViewItems(BaseSchema):
    pass


class GeoArea(BaseSchema):
    pass


class ListViewProduct(BaseSchema):
    pass


class Summary(BaseSchema):
    pass


class RegionSchema(BaseSchema):
    pass


class ZoneStores(BaseSchema):
    pass


class ZoneProduct(BaseSchema):
    pass


class ZoneBulkItem(BaseSchema):
    pass


class PincodeMopUpdateResult(BaseSchema):
    pass


class PincodeCodStatusItem(BaseSchema):
    pass


class PincodeCodStatusListingSummary(BaseSchema):
    pass


class PincodeMopUpdateAuditHistoryPaging(BaseSchema):
    pass


class PincodeMopUpdateAuditHistoryResult(BaseSchema):
    pass


class Area(BaseSchema):
    pass


class GeoAreaResponseDetail(BaseSchema):
    pass


class GeoAreaItemResult(BaseSchema):
    pass


class AreaExpanded(BaseSchema):
    pass


class Country(BaseSchema):
    pass


class Region(BaseSchema):
    pass


class Page2(BaseSchema):
    pass


class CourierPartnerRuleConditions(BaseSchema):
    pass


class LocationRule(BaseSchema):
    pass


class LocationRuleValues(BaseSchema):
    pass


class StringComparisonOperations(BaseSchema):
    pass


class IntComparisonOperations(BaseSchema):
    pass


class DateOperations(BaseSchema):
    pass


class ArithmeticOperations(BaseSchema):
    pass


class CourierPartnerRuleCPListResult(BaseSchema):
    pass


class CourierPartnerSchemeDefaultTat(BaseSchema):
    pass


class CourierPartnerSchemeTat(BaseSchema):
    pass


class CourierPartnerSchemeFeatures(BaseSchema):
    pass


class CourierPartnerList(BaseSchema):
    pass


class ShipmentsCourierPartnersServiceability(BaseSchema):
    pass


class CPShipments(BaseSchema):
    pass


class ShipmentsArticles(BaseSchema):
    pass


class ArticleWeight(BaseSchema):
    pass


class ArticleAttributes(BaseSchema):
    pass


class ArticleDimension(BaseSchema):
    pass


class ArticleSet(BaseSchema):
    pass


class ArticleSizeDistribution(BaseSchema):
    pass


class SetSize(BaseSchema):
    pass


class ArticleDeliverySlots(BaseSchema):
    pass


class ArticleReturnReason(BaseSchema):
    pass


class CourierPartners(BaseSchema):
    pass


class ShipmentCourierPartners(BaseSchema):
    pass


class CourierPartnerConfig(BaseSchema):
    pass


class BuyboxRuleConfig(BaseSchema):
    pass


class PromiseConfig(BaseSchema):
    pass


class StorePromiseAttributeConfig(BaseSchema):
    pass


class DeliveryServiceAttributeConfig(BaseSchema):
    pass


class BufferField(BaseSchema):
    pass


class StorePrioritySchema(BaseSchema):
    pass


class StoreRuleConditionSchema(BaseSchema):
    pass


class CustomerRadiusSchema(BaseSchema):
    pass


class CourierPartnerSchemeModel(BaseSchema):
    pass


class PackageMaterialRule(BaseSchema):
    pass


class PackageMaterialRuleQuantity(BaseSchema):
    pass


class Channel(BaseSchema):
    pass


class PackageRuleCategory(BaseSchema):
    pass


class PackageRuleProduct(BaseSchema):
    pass


class PackageRuleProductTag(BaseSchema):
    pass


class PackageRuleDepartmentId(BaseSchema):
    pass


class PackageRuleProductAttributes(BaseSchema):
    pass


class PackageChannel(BaseSchema):
    pass


class StoreFilter(BaseSchema):
    pass


class PackageRuleSchema(BaseSchema):
    pass


class Quantity(BaseSchema):
    pass


class PackagePageInfo(BaseSchema):
    pass


class OptimalLocationAssignedStoresResult(BaseSchema):
    pass


class OptimalLocationArticlesResult(BaseSchema):
    pass


class ArticleAssignment(BaseSchema):
    pass


class LocationDetailsServiceability(BaseSchema):
    pass


class ServiceabilityLocation(BaseSchema):
    pass


class OptimalLocationsArticles(BaseSchema):
    pass


class GetCountriesItems(BaseSchema):
    pass


class HierarchyItems(BaseSchema):
    pass


class CurrencyObject(BaseSchema):
    pass


class Localities(BaseSchema):
    pass


class PincodeLatLongData(BaseSchema):
    pass


class LocalityParent(BaseSchema):
    pass


class CountryMetaFields(BaseSchema):
    pass


class ApplicationFields(BaseSchema):
    pass


class GetCountryFieldsAddress(BaseSchema):
    pass


class FieldValidation(BaseSchema):
    pass


class FieldValidationRegex(BaseSchema):
    pass


class LengthValidation(BaseSchema):
    pass


class GetCountryFieldsAddressValues(BaseSchema):
    pass


class GetOneOrAll(BaseSchema):
    pass


class GetOneOrAllParams(BaseSchema):
    pass


class GetOneOrAllPath(BaseSchema):
    pass


class GetOneOrAllQuery(BaseSchema):
    pass


class GetCountryFieldsAddressTemplateApplication(BaseSchema):
    pass


class CountryHierarchy(BaseSchema):
    pass


class GetCountryFields(BaseSchema):
    pass


class GetCountryFieldsAddressTemplate(BaseSchema):
    pass


class LocalityParents(BaseSchema):
    pass


class ZoneConfig(BaseSchema):
    pass


class PromiseType(BaseSchema):
    pass


class InstallCourierPartnerItemsSchema(BaseSchema):
    pass


class HistoryObject(BaseSchema):
    pass





class PlatformShipmentsRequestSchema(BaseSchema):
    # Serviceability swagger.json

    
    journey = fields.Str(required=False)
    
    location_articles = fields.List(fields.Nested(PlatformLocationArticles, required=False), required=False)
    
    to_serviceability = fields.Nested(PlatformShipmentsToServiceability, required=False)
    
    payment_mode = fields.Str(required=False, allow_none=True)
    


class PlatformShipmentsResponseSchema(BaseSchema):
    # Serviceability swagger.json

    
    is_cod_available = fields.Boolean(required=False)
    
    shipments = fields.List(fields.Nested(PlatformShipmentsSchema, required=False), required=False)
    


class ShipmentsErrorResult(BaseSchema):
    # Serviceability swagger.json

    
    message = fields.Str(required=False, allow_none=True)
    
    type = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class FulfillmentOption(BaseSchema):
    # Serviceability swagger.json

    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    application_id = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    is_default = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    business_unit = fields.List(fields.Nested(BusinessUnit, required=False), required=False)
    
    fulfillment_stores = fields.Nested(FulfillmentStores, required=False)
    
    products = fields.Nested(FulfillmentProducts, required=False)
    
    cp_schemes = fields.Nested(CourierPartnerSchemes, required=False)
    
    id = fields.Str(required=False)
    


class FulfillmentOptionsList(BaseSchema):
    # Serviceability swagger.json

    
    items = fields.List(fields.Nested(FulfillmentOptionItem, required=False), required=False)
    


class FulfillmentOptionProducts(BaseSchema):
    # Serviceability swagger.json

    
    items = fields.Nested(FulfillmentOptionProduct, required=False)
    
    page = fields.Nested(Page, required=False)
    


class FulfillmentOptionStores(BaseSchema):
    # Serviceability swagger.json

    
    items = fields.List(fields.Nested(FulfillmentOptionStore, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class FulfillmentOptionBulkValidate(BaseSchema):
    # Serviceability swagger.json

    
    store_type = fields.Str(required=False)
    
    file_path = fields.Str(required=False)
    
    action = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    fulfillment_option_slug = fields.Str(required=False)
    
    request = fields.Nested(FulfillmentOptionValidate, required=False)
    


class FulfillmentOptionBulkValidateData(BaseSchema):
    # Serviceability swagger.json

    
    request_id = fields.Str(required=False)
    


class FulfillmentOptionBulk(BaseSchema):
    # Serviceability swagger.json

    
    file_path = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class FulfillmentOptionBulkData(BaseSchema):
    # Serviceability swagger.json

    
    request_id = fields.Str(required=False)
    
    request = fields.Nested(FulfillmentOptionValidate, required=False)
    
    fulfillment_option_slug = fields.Str(required=False)
    
    file_url = fields.Str(required=False)
    
    total = fields.Int(required=False)
    
    success = fields.Int(required=False)
    
    failed = fields.Int(required=False)
    
    action = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    updated_by = fields.Str(required=False, allow_none=True)
    
    type = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    application_id = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    


class OperationResponseSchema(BaseSchema):
    # Serviceability swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class SelfshipSchema(BaseSchema):
    # Serviceability swagger.json

    
    tat = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    unit = fields.Str(required=False)
    


class ServiceabilityErrorResult(BaseSchema):
    # Serviceability swagger.json

    
    message = fields.Str(required=False, allow_none=True)
    
    value = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class UpdateZoneData(BaseSchema):
    # Serviceability swagger.json

    
    zone_id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    geo_areas = fields.List(fields.Str(required=False), required=False)
    
    company_id = fields.Int(required=False)
    
    application_id = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    product = fields.Nested(ProductSchema, required=False)
    
    stores = fields.Nested(StoresSchema, required=False)
    


class ZoneUpdateSuccessResult(BaseSchema):
    # Serviceability swagger.json

    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    application_id = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    geo_areas = fields.List(fields.Str(required=False), required=False)
    
    product = fields.Nested(ProductSchema, required=False)
    
    stores = fields.Nested(StoresSchema, required=False)
    
    zone_id = fields.Str(required=False)
    
    created_by = fields.Nested(CreatedBy, required=False)
    
    modified_by = fields.Nested(ModifiedBy, required=False)
    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    


class ServiceabilityDeleteErrorResult(BaseSchema):
    # Serviceability swagger.json

    
    error = fields.List(fields.Nested(ServiceabilityErrorResult, required=False), required=False)
    


class ZoneDeleteSuccessResult(BaseSchema):
    # Serviceability swagger.json

    
    message = fields.Str(required=False)
    


class ListViewSchema(BaseSchema):
    # Serviceability swagger.json

    
    items = fields.List(fields.Nested(ListViewItems, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class GetZoneByIdSchema(BaseSchema):
    # Serviceability swagger.json

    
    zone_id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    product = fields.Nested(ProductSchema, required=False)
    
    stores = fields.Nested(StoresSchema, required=False)
    
    created_by = fields.Nested(CreatedBy, required=False)
    
    modified_by = fields.Nested(ModifiedBy, required=False)
    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    overlapping_file_url = fields.Str(required=False, allow_none=True)
    
    geo_areas = fields.List(fields.Str(required=False), required=False)
    
    overlapping_zone_names = fields.List(fields.Str(required=False), required=False)
    


class CommonErrorResult(BaseSchema):
    # Serviceability swagger.json

    
    error = fields.List(fields.Nested(Error, required=False), required=False)
    


class CreateZoneDataSchema(BaseSchema):
    # Serviceability swagger.json

    
    fulfillment_option_slug = fields.Str(required=False, allow_none=True)
    
    is_active = fields.Boolean(required=False)
    
    slug = fields.Str(required=False)
    
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

    
    items = fields.Raw(required=False)
    


class CreateBulkZoneData(BaseSchema):
    # Serviceability swagger.json

    
    file_url = fields.Raw(required=False)
    
    product_type = fields.Str(required=False)
    


class ZoneSchema(BaseSchema):
    # Serviceability swagger.json

    
    name = fields.Raw(required=False)
    
    fulfillment_option_slug = fields.Str(required=False, allow_none=True)
    
    slug = fields.Raw(required=False)
    
    company_id = fields.Raw(required=False)
    
    application_id = fields.Raw(required=False)
    
    is_active = fields.Raw(required=False)
    
    geo_areas = fields.Raw(required=False)
    
    stores = fields.Raw(required=False)
    
    product = fields.Raw(required=False)
    
    created_by = fields.Nested(CreatedBy, required=False)
    
    modified_by = fields.Nested(ModifiedBy, required=False)
    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    stage = fields.Raw(required=False)
    
    zone_id = fields.Raw(required=False)
    


class CreateBulkZoneResult(BaseSchema):
    # Serviceability swagger.json

    
    zone_id = fields.Raw(required=False)
    


class BulkCreateZoneExport(BaseSchema):
    # Serviceability swagger.json

    
    placeholder = fields.Raw(required=False)
    


class PincodeMopData(BaseSchema):
    # Serviceability swagger.json

    
    pincodes = fields.List(fields.Int(required=False), required=False)
    
    country = fields.Str(required=False)
    
    action = fields.Str(required=False)
    


class PincodeMOPResult(BaseSchema):
    # Serviceability swagger.json

    
    success = fields.Boolean(required=False)
    
    status_code = fields.Int(required=False)
    
    batch_id = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    action = fields.Str(required=False)
    
    pincodes = fields.List(fields.Int(required=False), required=False)
    
    updated_pincodes = fields.List(fields.Nested(PincodeMopUpdateResult, required=False), required=False)
    


class PincodeMopUpdateAuditError(BaseSchema):
    # Serviceability swagger.json

    
    status = fields.Int(required=False)
    
    success = fields.Boolean(required=False)
    


class PincodeMopBulkError(BaseSchema):
    # Serviceability swagger.json

    
    batch_id = fields.Str(required=False)
    
    status_code = fields.Int(required=False)
    
    error = fields.List(fields.Nested(Error, required=False), required=False)
    
    success = fields.Boolean(required=False)
    


class CommonError(BaseSchema):
    # Serviceability swagger.json

    
    status_code = fields.Int(required=False)
    
    error = fields.List(fields.Nested(Error, required=False), required=False)
    
    success = fields.Boolean(required=False)
    


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
    


class PincodeCodStatusListingResult(BaseSchema):
    # Serviceability swagger.json

    
    country = fields.Str(required=False)
    
    data = fields.List(fields.Nested(PincodeCodStatusItem, required=False), required=False)
    
    success = fields.Boolean(required=False)
    
    errors = fields.List(fields.Nested(Error, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
    summary = fields.Nested(PincodeCodStatusListingSummary, required=False)
    


class PincodeMopUpdateAuditHistoryDetails(BaseSchema):
    # Serviceability swagger.json

    
    entity_type = fields.Str(required=False)
    
    file_name = fields.Str(required=False)
    


class PincodeMopUpdateAuditHistoryResultData(BaseSchema):
    # Serviceability swagger.json

    
    entity_type = fields.Str(required=False)
    
    page = fields.Nested(PincodeMopUpdateAuditHistoryPaging, required=False)
    
    data = fields.List(fields.Nested(PincodeMopUpdateAuditHistoryResult, required=False), required=False)
    


class BulkGeoAreaDetails(BaseSchema):
    # Serviceability swagger.json

    
    file_url = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class BulkGeoAreaResult(BaseSchema):
    # Serviceability swagger.json

    
    geoarea_id = fields.Str(required=False)
    


class BulkGeoAreaGetResult(BaseSchema):
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
    
    updated_by = fields.Str(required=False, allow_none=True)
    
    type = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    


class GeoAreaRequestBody(BaseSchema):
    # Serviceability swagger.json

    
    is_polygon = fields.Boolean(required=False, allow_none=True)
    
    is_active = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    areas = fields.List(fields.Nested(Area, required=False), required=False)
    
    region_type = fields.Str(required=False, allow_none=True)
    


class GeoAreaErrorResult(BaseSchema):
    # Serviceability swagger.json

    
    error = fields.List(fields.Nested(GeoAreaResponseDetail, required=False), required=False)
    


class GeoAreaResponseBody(BaseSchema):
    # Serviceability swagger.json

    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    areas = fields.List(fields.Nested(Area, required=False), required=False)
    
    region_type = fields.Str(required=False, allow_none=True)
    
    is_polygon = fields.Boolean(required=False, allow_none=True)
    
    type = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    created_by = fields.Nested(CreatedBy, required=False)
    
    modified_by = fields.Nested(ModifiedBy, required=False)
    
    geoarea_id = fields.Str(required=False)
    


class GeoAreaPutResponseBody(BaseSchema):
    # Serviceability swagger.json

    
    name = fields.Str(required=False)
    
    geoarea_id = fields.Str(required=False)
    
    is_polygon = fields.Boolean(required=False, allow_none=True)
    
    slug = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    areas = fields.List(fields.Nested(Area, required=False), required=False)
    
    region_type = fields.Str(required=False, allow_none=True)
    
    type = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    created_by = fields.Nested(CreatedBy, required=False)
    
    modified_by = fields.Nested(ModifiedBy, required=False)
    
    upload_type = fields.Str(required=False)
    


class GeoAreaGetResponseBody(BaseSchema):
    # Serviceability swagger.json

    
    items = fields.List(fields.Nested(GeoAreaItemResult, required=False), required=False)
    
    page = fields.Nested(Page2, required=False)
    


class GeoAreaDetails(BaseSchema):
    # Serviceability swagger.json

    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    application_id = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    is_polygon = fields.Boolean(required=False, allow_none=True)
    
    geoarea_id = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    
    region_type = fields.Str(required=False, allow_none=True)
    
    areas = fields.List(fields.Nested(AreaExpanded, required=False), required=False)
    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    created_by = fields.Nested(CreatedBy, required=False)
    
    modified_by = fields.Nested(ModifiedBy, required=False)
    


class Error(BaseSchema):
    # Serviceability swagger.json

    
    type = fields.Str(required=False, allow_none=True)
    
    value = fields.Str(required=False, allow_none=True)
    
    message = fields.Str(required=False, allow_none=True)
    


class CourierAccountDetailsBody(BaseSchema):
    # Serviceability swagger.json

    
    extension_id = fields.Str(required=False)
    
    account_id = fields.Str(required=False)
    
    scheme_id = fields.Str(required=False)
    
    is_self_ship = fields.Boolean(required=False)
    
    stage = fields.Str(required=False)
    
    is_own_account = fields.Boolean(required=False)
    


class CourierPartnerRuleResult(BaseSchema):
    # Serviceability swagger.json

    
    is_active = fields.Boolean(required=False)
    
    application_id = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    manual_priority = fields.List(fields.Str(required=False), required=False)
    
    filters = fields.Str(required=False, allow_none=True)
    
    conditions = fields.Nested(CourierPartnerRuleConditions, required=False)
    
    sort = fields.List(fields.Str(required=False), required=False)
    
    created_by = fields.Nested(CreatedBy, required=False)
    
    id = fields.Str(required=False)
    
    modified_by = fields.Nested(ModifiedBy, required=False)
    
    modified_on = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    cp_list = fields.List(fields.Nested(CourierPartnerRuleCPListResult, required=False), required=False)
    


class CourierPartnerRule(BaseSchema):
    # Serviceability swagger.json

    
    is_active = fields.Boolean(required=False)
    
    cp_list = fields.List(fields.Nested(CourierPartnerList, required=False), required=False)
    
    name = fields.Str(required=False)
    
    manual_priority = fields.List(fields.Str(required=False), required=False)
    
    filters = fields.Str(required=False, allow_none=True)
    
    conditions = fields.Nested(CourierPartnerRuleConditions, required=False)
    
    sort = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    


class BulkFailureResult(BaseSchema):
    # Serviceability swagger.json

    
    success = fields.Boolean(required=False)
    
    error = fields.List(fields.Nested(Error, required=False), required=False)
    


class FailureResult(BaseSchema):
    # Serviceability swagger.json

    
    success = fields.Boolean(required=False)
    
    error = fields.List(fields.Nested(Error, required=False), required=False)
    


class CourierPartnerRulesListResult(BaseSchema):
    # Serviceability swagger.json

    
    items = fields.List(fields.Nested(CourierPartnerRuleResult, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class ShipmentCourierPartnerDetails(BaseSchema):
    # Serviceability swagger.json

    
    from_location = fields.Nested(ShipmentsCourierPartnersServiceability, required=False)
    
    to_location = fields.Nested(ShipmentsCourierPartnersServiceability, required=False)
    
    shipments = fields.List(fields.Nested(CPShipments, required=False), required=False)
    
    journey = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    


class ShipmentCourierPartnerResult(BaseSchema):
    # Serviceability swagger.json

    
    courier_partners = fields.List(fields.Nested(CourierPartners, required=False), required=False)
    
    shipments = fields.List(fields.Nested(ShipmentCourierPartners, required=False), required=False)
    
    delivery_promise = fields.Nested(CourierPartnerPromise, required=False)
    


class CompanyConfig(BaseSchema):
    # Serviceability swagger.json

    
    company_id = fields.Int(required=False)
    
    is_rate_card_enabled = fields.Boolean(required=False)
    
    sort = fields.List(fields.Str(required=False), required=False)
    
    logistics_as_actual = fields.Str(required=False)
    


class ApplicationConfigPatch(BaseSchema):
    # Serviceability swagger.json

    
    courier_partner_config = fields.Nested(CourierPartnerConfig, required=False)
    
    buybox_rule_config = fields.Nested(BuyboxRuleConfig, required=False)
    
    promise_config = fields.Nested(PromiseConfig, required=False)
    


class ApplicationConfigPatchResult(BaseSchema):
    # Serviceability swagger.json

    
    success = fields.Boolean(required=False)
    


class BulkRegionJobDetails(BaseSchema):
    # Serviceability swagger.json

    
    file_path = fields.Str(required=False)
    
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
    
    modified_on = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    


class BulkRegionResult(BaseSchema):
    # Serviceability swagger.json

    
    items = fields.List(fields.Nested(BulkRegionResultItemData, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class StoreRuleConfigData(BaseSchema):
    # Serviceability swagger.json

    
    rule_ids = fields.List(fields.Str(required=False), required=False)
    
    type_based_priority = fields.List(fields.Str(required=False), required=False)
    
    tag_based_priority = fields.List(fields.Str(required=False), required=False)
    
    store_priority = fields.List(fields.Nested(StorePrioritySchema, required=False), required=False)
    
    sort = fields.List(fields.Str(required=False), required=False)
    
    meta_sort_priority = fields.Dict(required=False)
    
    manual_priority = fields.List(fields.Int(required=False), required=False)
    


class StoreRuleDataSchema(BaseSchema):
    # Serviceability swagger.json

    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    manual_priority = fields.List(fields.Int(required=False), required=False)
    
    meta_sort_priority = fields.Dict(required=False)
    
    meta_conditions = fields.Dict(required=False)
    
    filters = fields.Str(required=False, allow_none=True)
    
    company_id = fields.Int(required=False)
    
    application_id = fields.Str(required=False)
    
    type_based_priority = fields.List(fields.Str(required=False), required=False)
    
    tag_based_priority = fields.List(fields.Str(required=False), required=False)
    
    store_priority = fields.List(fields.Nested(StorePrioritySchema, required=False), required=False)
    
    sort = fields.List(fields.Str(required=False), required=False)
    
    conditions = fields.Nested(StoreRuleConditionSchema, required=False)
    
    is_active = fields.Boolean(required=False)
    


class GetStoreRulesApiResult(BaseSchema):
    # Serviceability swagger.json

    
    items = fields.List(fields.Nested(StoreRuleDataSchema, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class CreateStoreRuleDetailsSchema(BaseSchema):
    # Serviceability swagger.json

    
    name = fields.Str(required=False)
    
    manual_priority = fields.List(fields.Int(required=False), required=False)
    
    meta_sort_priority = fields.Dict(required=False)
    
    meta_conditions = fields.Dict(required=False)
    
    filters = fields.Str(required=False, allow_none=True)
    
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
    
    manual_priority = fields.List(fields.Int(required=False), required=False)
    
    meta_sort_priority = fields.Dict(required=False)
    
    meta_conditions = fields.Dict(required=False)
    
    filters = fields.Str(required=False, allow_none=True)
    
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
    
    manual_priority = fields.List(fields.Int(required=False), required=False)
    
    meta_sort_priority = fields.Dict(required=False)
    
    meta_conditions = fields.Dict(required=False)
    
    filters = fields.Str(required=False, allow_none=True)
    
    type = fields.Str(required=False)
    
    type_based_priority = fields.List(fields.Str(required=False), required=False)
    
    tag_based_priority = fields.List(fields.Str(required=False), required=False)
    
    store_priority = fields.List(fields.Nested(StorePrioritySchema, required=False), required=False)
    
    sort = fields.List(fields.Str(required=False), required=False)
    
    conditions = fields.Nested(StoreRuleConditionSchema, required=False)
    
    is_active = fields.Boolean(required=False)
    
    company_id = fields.Int(required=False)
    
    application_id = fields.Str(required=False)
    


class CourierAccountResult(BaseSchema):
    # Serviceability swagger.json

    
    account_id = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    scheme_id = fields.Str(required=False)
    
    extension_id = fields.Str(required=False)
    
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
    


class PackageMaterialNotFound(BaseSchema):
    # Serviceability swagger.json

    
    status_code = fields.Int(required=False)
    
    success = fields.Boolean(required=False)
    


class PackageMaterialsErrorResult(BaseSchema):
    # Serviceability swagger.json

    
    value = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    error = fields.Str(required=False)
    


class PackageMaterialResult(BaseSchema):
    # Serviceability swagger.json

    
    company_id = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
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
    


class PackageRule(BaseSchema):
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
    


class PackageRuleResult(BaseSchema):
    # Serviceability swagger.json

    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    product_tag = fields.Nested(PackageRuleProductTag, required=False)
    
    product_id = fields.Nested(PackageRuleProduct, required=False)
    
    department_id = fields.Nested(PackageRuleDepartmentId, required=False)
    
    product_attributes = fields.Nested(PackageRuleProductAttributes, required=False)
    
    category_id = fields.Nested(PackageRuleCategory, required=False)
    


class PackagesListResult(BaseSchema):
    # Serviceability swagger.json

    
    items = fields.List(fields.Nested(PackageItem, required=False), required=False)
    
    page = fields.Nested(PackagePageInfo, required=False)
    


class PackageItem(BaseSchema):
    # Serviceability swagger.json

    
    name = fields.Str(required=False)
    
    weight = fields.Float(required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    length = fields.Float(required=False)
    
    channels = fields.List(fields.Nested(PackageChannel, required=False), required=False)
    
    package_type = fields.Str(required=False)
    
    rules = fields.List(fields.Nested(PackageRuleSchema, required=False), required=False)
    
    height = fields.Float(required=False)
    
    error_rate = fields.Float(required=False)
    
    width = fields.Float(required=False)
    
    is_active = fields.Boolean(required=False)
    
    size = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    max_weight = fields.Float(required=False)
    
    media = fields.List(fields.Dict(required=False), required=False)
    
    package_vol_weight = fields.Float(required=False)
    
    status = fields.Str(required=False)
    
    auto_calculate = fields.Boolean(required=False)
    
    id = fields.Str(required=False)
    


class RulePriorityDetails(BaseSchema):
    # Serviceability swagger.json

    
    rule_id = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    


class RulePriorityResult(BaseSchema):
    # Serviceability swagger.json

    
    success = fields.Boolean(required=False)
    


class OptimalLocationsResult(BaseSchema):
    # Serviceability swagger.json

    
    assigned_stores = fields.List(fields.Nested(OptimalLocationAssignedStoresResult, required=False), required=False)
    
    faulty_articles = fields.List(fields.Nested(Error, required=False), required=False)
    


class OptimlLocationsRequestSchema(BaseSchema):
    # Serviceability swagger.json

    
    channel_id = fields.Str(required=False)
    
    channel_type = fields.Str(required=False)
    
    channel_identifier = fields.Str(required=False)
    
    to_serviceability = fields.Nested(LocationDetailsServiceability, required=False)
    
    articles = fields.List(fields.Nested(OptimalLocationsArticles, required=False), required=False)
    


class ValidationError(BaseSchema):
    # Serviceability swagger.json

    
    message = fields.Str(required=False)
    
    field = fields.Str(required=False)
    


class StandardError(BaseSchema):
    # Serviceability swagger.json

    
    message = fields.Str(required=False)
    


class CourierPartnerSchemeDetailsModel(BaseSchema):
    # Serviceability swagger.json

    
    extension_id = fields.Str(required=False)
    
    scheme_id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    default_forward_pickup_cutoff = fields.Str(required=False, allow_none=True)
    
    default_reverse_pickup_cutoff = fields.Str(required=False, allow_none=True)
    
    default_cutoff_timezone = fields.Str(required=False, allow_none=True)
    
    default_tat = fields.Nested(CourierPartnerSchemeDefaultTat, required=False)
    
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
    
    feature = fields.Nested(CourierPartnerSchemeFeatures, required=False)
    


class CourierPartnerSchemeModelSchema(BaseSchema):
    # Serviceability swagger.json

    
    created_by = fields.Nested(CreatedBy, required=False)
    
    created_on = fields.Str(required=False)
    
    modified_by = fields.Nested(ModifiedBy, required=False)
    
    modified_on = fields.Str(required=False)
    
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
    
    feature = fields.Nested(CourierPartnerSchemeFeatures, required=False)
    
    default_forward_pickup_cutoff = fields.Str(required=False, allow_none=True)
    
    default_reverse_pickup_cutoff = fields.Str(required=False, allow_none=True)
    
    default_cutoff_timezone = fields.Str(required=False, allow_none=True)
    
    default_tat = fields.Nested(CourierPartnerSchemeDefaultTat, required=False)
    


class CourierPartnerSchemeUpdateDetailsSchema(BaseSchema):
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
    
    feature = fields.Nested(CourierPartnerSchemeFeatures, required=False)
    


class CourierPartnerSchemeList(BaseSchema):
    # Serviceability swagger.json

    
    items = fields.List(fields.Nested(CourierPartnerSchemeModelSchema, required=False), required=False)
    
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
    


class GetCountries(BaseSchema):
    # Serviceability swagger.json

    
    items = fields.List(fields.Nested(GetCountriesItems, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class GetLocalities(BaseSchema):
    # Serviceability swagger.json

    
    items = fields.List(fields.Nested(Localities, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class GetCountry(BaseSchema):
    # Serviceability swagger.json

    
    meta = fields.Nested(CountryMetaFields, required=False)
    
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
    


class BulkImportLocalitiesDetails(BaseSchema):
    # Serviceability swagger.json

    
    file_url = fields.Str(required=False)
    


class BulkImportLocalitiesResult(BaseSchema):
    # Serviceability swagger.json

    
    batch_id = fields.Str(required=False)
    
    file_url = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class BulkErrorResult(BaseSchema):
    # Serviceability swagger.json

    
    success = fields.Boolean(required=False)
    
    status_code = fields.Int(required=False)
    
    error = fields.Str(required=False)
    
    batch_id = fields.Str(required=False)
    
    total_count = fields.Int(required=False)
    
    total_error_count = fields.Int(required=False)
    
    error_file_url = fields.Str(required=False)
    


class LocalitiesBulkExport(BaseSchema):
    # Serviceability swagger.json

    
    country_iso_code = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    batch_id = fields.Str(required=False)
    
    offset = fields.Int(required=False)
    
    type = fields.Str(required=False)
    


class LocalitiesBulkExportFetch(BaseSchema):
    # Serviceability swagger.json

    
    batch_id = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    download_percentage = fields.Int(required=False)
    
    url_path = fields.Str(required=False, allow_none=True)
    


class LocalitiesErrorResult(BaseSchema):
    # Serviceability swagger.json

    
    success = fields.Boolean(required=False)
    
    status_code = fields.Int(required=False)
    
    error = fields.Str(required=False)
    


class GetLocality(BaseSchema):
    # Serviceability swagger.json

    
    meta = fields.Dict(required=False)
    
    parent_uid = fields.Str(required=False, allow_none=True)
    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    custom_meta = fields.Dict(required=False)
    
    parent_ids = fields.List(fields.Str(required=False), required=False)
    
    localities = fields.List(fields.Nested(LocalityParent, required=False), required=False)
    
    type = fields.Str(required=False)
    
    parents = fields.Nested(LocalityParents, required=False)
    


class ValidateAddress(BaseSchema):
    # Serviceability swagger.json

    
    address = fields.Str(required=False)
    
    address1 = fields.Str(required=False)
    
    address_meta = fields.Dict(required=False)
    
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
    


class ErrorResult(BaseSchema):
    # Serviceability swagger.json

    
    success = fields.Boolean(required=False)
    
    error = fields.Nested(Error, required=False)
    


class ApplicationConfigPut(BaseSchema):
    # Serviceability swagger.json

    
    rule_ids = fields.List(fields.Str(required=False), required=False)
    
    sort = fields.List(fields.Str(required=False), required=False)
    
    manual_priority = fields.List(fields.Str(required=False), required=False)
    
    application_id = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    


class ApplicationConfigPutDetail(BaseSchema):
    # Serviceability swagger.json

    
    rule_ids = fields.List(fields.Str(required=False), required=False)
    
    sort = fields.List(fields.Str(required=False), required=False)
    
    manual_priority = fields.List(fields.Str(required=False), required=False)
    


class ApplicationConfigGetResult(BaseSchema):
    # Serviceability swagger.json

    
    zones = fields.Nested(ZoneConfig, required=False)
    
    courier_partner_config = fields.Nested(CourierPartnerConfig, required=False)
    
    buybox_rule_config = fields.Nested(BuyboxRuleConfig, required=False)
    
    promise_types = fields.List(fields.Nested(PromiseType, required=False), required=False)
    
    promise_config = fields.Nested(PromiseConfig, required=False)
    


class InstallCourierPartnerResponseSchema(BaseSchema):
    # Serviceability swagger.json

    
    items = fields.List(fields.Nested(InstallCourierPartnerItemsSchema, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class GetLocalitiesBulkHistory(BaseSchema):
    # Serviceability swagger.json

    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(HistoryObject, required=False), required=False)
    


class CompanyConfigurationSchema(BaseSchema):
    # Serviceability swagger.json

    
    is_rate_card_enabled = fields.Boolean(required=False)
    
    sort = fields.List(fields.Str(required=False), required=False)
    


class PlatformLocationArticles(BaseSchema):
    # Serviceability swagger.json

    
    articles = fields.List(fields.Nested(PlatformLocationArticle, required=False), required=False)
    
    fulfillment_location_id = fields.Int(required=False)
    
    fulfillment_tags = fields.List(fields.Str(required=False), required=False)
    
    fulfillment_type = fields.Str(required=False)
    


class PlatformLocationArticle(BaseSchema):
    # Serviceability swagger.json

    
    price = fields.Float(required=False)
    
    item_id = fields.Int(required=False)
    
    size = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    parent_item_identifiers = fields.Nested(ParentItemIdentifiers, required=False)
    


class ParentItemIdentifiers(BaseSchema):
    # Serviceability swagger.json

    
    identifier = fields.Str(required=False)
    
    parent_item_id = fields.Str(required=False)
    
    parent_item_size = fields.Str(required=False)
    


class PlatformShipmentsToServiceability(BaseSchema):
    # Serviceability swagger.json

    
    pincode = fields.Str(required=False)
    
    sector = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    country_iso_code = fields.Str(required=False)
    


class PlatformShipmentsSchema(BaseSchema):
    # Serviceability swagger.json

    
    tags = fields.List(fields.Str(required=False), required=False)
    
    packaging = fields.Nested(Packaging, required=False)
    
    fulfillment_option = fields.Nested(FulfillmentOptionItem, required=False)
    
    weight = fields.Float(required=False)
    
    shipment_type = fields.Str(required=False)
    
    is_auto_assign = fields.Boolean(required=False)
    
    volumetric_weight = fields.Float(required=False)
    
    fulfillment_tags = fields.List(fields.Str(required=False), required=False)
    
    promise = fields.Nested(ShipmentsPromise, required=False)
    
    is_ewaybill_enabled = fields.Boolean(required=False)
    
    is_mto = fields.Boolean(required=False)
    
    articles = fields.List(fields.Nested(ShipmentsArticle, required=False), required=False)
    
    fulfillment_type = fields.Str(required=False)
    
    mps = fields.Boolean(required=False)
    
    fulfillment_location_id = fields.Int(required=False)
    
    courier_partners = fields.List(fields.Nested(ShipmentsCourierPartner, required=False), required=False)
    
    count = fields.Int(required=False)
    
    is_cod_available = fields.Boolean(required=False)
    


class Packaging(BaseSchema):
    # Serviceability swagger.json

    
    name = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    dimension = fields.Nested(Dimension, required=False)
    


class Dimension(BaseSchema):
    # Serviceability swagger.json

    
    length = fields.Float(required=False)
    
    width = fields.Float(required=False)
    
    height = fields.Float(required=False)
    


class FulfillmentOptionItem(BaseSchema):
    # Serviceability swagger.json

    
    slug = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    is_default = fields.Boolean(required=False)
    
    id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    


class ShipmentsPromise(BaseSchema):
    # Serviceability swagger.json

    
    min = fields.Str(required=False)
    
    max = fields.Str(required=False)
    
    customer_promise = fields.Nested(CustomerPromise, required=False)
    
    meta = fields.Nested(ShipmentPromiseMeta, required=False)
    


class CustomerPromise(BaseSchema):
    # Serviceability swagger.json

    
    min = fields.Str(required=False)
    
    max = fields.Str(required=False)
    


class ShipmentPromiseMeta(BaseSchema):
    # Serviceability swagger.json

    
    seller_promise = fields.Nested(SellerPromise, required=False)
    
    courier_partner_promise = fields.Nested(CourierPartnerPromise, required=False)
    
    customer_initial_promise = fields.Nested(CustomerInitialPromise, required=False)
    


class SellerPromise(BaseSchema):
    # Serviceability swagger.json

    
    min = fields.Str(required=False)
    
    max = fields.Str(required=False)
    


class CourierPartnerPromise(BaseSchema):
    # Serviceability swagger.json

    
    min = fields.Str(required=False)
    
    max = fields.Str(required=False)
    
    attributes = fields.Nested(CourierPartnerAttributes, required=False)
    


class CourierPartnerAttributes(BaseSchema):
    # Serviceability swagger.json

    
    tat = fields.Nested(CourierPartnerTAT, required=False)
    


class CourierPartnerTAT(BaseSchema):
    # Serviceability swagger.json

    
    min = fields.Int(required=False)
    
    max = fields.Int(required=False)
    


class CustomerInitialPromise(BaseSchema):
    # Serviceability swagger.json

    
    min = fields.Str(required=False)
    
    max = fields.Str(required=False)
    


class ShipmentsArticle(BaseSchema):
    # Serviceability swagger.json

    
    id = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    item_id = fields.Int(required=False)
    
    size = fields.Str(required=False)
    
    price = fields.Float(required=False)
    
    price_marked = fields.Float(required=False, allow_none=True)
    
    department_id = fields.Int(required=False)
    
    weight = fields.Float(required=False)
    
    attributes = fields.Dict(required=False)
    
    category_id = fields.Int(required=False)
    
    brand_id = fields.Int(required=False)
    
    dimension = fields.Nested(ShipmentDimension, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    manufacturing_time = fields.Int(required=False)
    
    manufacturing_time_unit = fields.Str(required=False)
    
    set = fields.Dict(required=False)
    
    is_set = fields.Boolean(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    return_reason = fields.Str(required=False, allow_none=True)
    
    group_id = fields.Str(required=False)
    
    meta = fields.Nested(ShipmentsMeta, required=False)
    
    is_mto = fields.Boolean(required=False)
    
    sla = fields.Str(required=False)
    


class ShipmentDimension(BaseSchema):
    # Serviceability swagger.json

    
    height = fields.Float(required=False)
    
    length = fields.Float(required=False)
    
    width = fields.Float(required=False)
    
    is_default = fields.Boolean(required=False)
    
    unit = fields.Str(required=False)
    


class ShipmentsMeta(BaseSchema):
    # Serviceability swagger.json

    
    is_set = fields.Boolean(required=False)
    
    set = fields.Dict(required=False)
    
    is_set_article = fields.Boolean(required=False)
    
    set_quantity = fields.Int(required=False)
    
    split_article_id = fields.Str(required=False)
    
    promo_ids = fields.List(fields.Str(required=False), required=False)
    


class ShipmentsCourierPartner(BaseSchema):
    # Serviceability swagger.json

    
    extension_id = fields.Str(required=False)
    
    scheme_id = fields.Str(required=False)
    
    area_code = fields.Nested(AreaCode, required=False)
    
    tat = fields.Nested(TAT, required=False)
    
    display_name = fields.Str(required=False)
    
    is_qc_enabled = fields.Boolean(required=False)
    
    is_self_ship = fields.Boolean(required=False)
    
    is_own_account = fields.Boolean(required=False)
    
    ndr_attempts = fields.Int(required=False)
    
    forward_pickup_cutoff = fields.Str(required=False, allow_none=True)
    
    reverse_pickup_cutoff = fields.Str(required=False, allow_none=True)
    
    qc_shipment_item_quantity = fields.Int(required=False, allow_none=True)
    
    non_qc_shipment_item_quantity = fields.Int(required=False, allow_none=True)
    


class AreaCode(BaseSchema):
    # Serviceability swagger.json

    
    source = fields.Str(required=False)
    
    destination = fields.Str(required=False)
    


class TAT(BaseSchema):
    # Serviceability swagger.json

    
    min = fields.Int(required=False)
    
    max = fields.Int(required=False)
    


class BusinessUnit(BaseSchema):
    # Serviceability swagger.json

    
    name = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    


class FulfillmentStores(BaseSchema):
    # Serviceability swagger.json

    
    values = fields.List(fields.Int(required=False), required=False)
    
    type = fields.Str(required=False)
    


class FulfillmentProducts(BaseSchema):
    # Serviceability swagger.json

    
    values = fields.List(fields.Int(required=False), required=False)
    
    type = fields.Str(required=False)
    


class CourierPartnerSchemes(BaseSchema):
    # Serviceability swagger.json

    
    values = fields.List(fields.Nested(CourierPartnerScheme, required=False), required=False)
    
    type = fields.Str(required=False)
    


class CourierPartnerScheme(BaseSchema):
    # Serviceability swagger.json

    
    scheme_id = fields.Str(required=False)
    
    cp_ext_id = fields.Str(required=False)
    


class FulfillmentOptionProduct(BaseSchema):
    # Serviceability swagger.json

    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    category_slug = fields.Str(required=False)
    
    category_uid = fields.Int(required=False)
    
    short_description = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    brand_uid = fields.Int(required=False)
    
    currency = fields.Str(required=False)
    
    item_code = fields.Str(required=False)
    
    item_type = fields.Str(required=False)
    
    net_quantity = fields.Nested(NetQuantity, required=False)
    
    multi_size = fields.Boolean(required=False)
    
    is_set = fields.Boolean(required=False)
    
    is_dependent = fields.Boolean(required=False)
    
    is_active = fields.Boolean(required=False)
    
    is_image_less_product = fields.Boolean(required=False)
    
    size_guide = fields.Str(required=False)
    
    teaser_tag = fields.Dict(required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    product_group_tag = fields.List(fields.Str(required=False), required=False)
    
    departments = fields.List(fields.Int(required=False), required=False)
    
    company_id = fields.Int(required=False)
    
    company_ids = fields.List(fields.Int(required=False), required=False)
    
    country_of_origin = fields.Str(required=False)
    
    change_request_id = fields.Str(required=False)
    
    trader = fields.Nested(Trader, required=False)
    
    trader_type = fields.Str(required=False)
    
    product_publish = fields.Nested(ProductPublish, required=False)
    
    tax_identifier = fields.Nested(TaxIdentifier, required=False)
    
    return_config = fields.Nested(ReturnConfig, required=False)
    
    custom_order = fields.Nested(CustomOrder, required=False)
    
    sizes = fields.List(fields.Nested(Size, required=False), required=False)
    
    media = fields.List(fields.Str(required=False), required=False)
    
    variant_media = fields.Dict(required=False)
    
    variants = fields.Dict(required=False)
    
    no_of_boxes = fields.Int(required=False)
    
    _custom_json = fields.Dict(required=False)
    


class NetQuantity(BaseSchema):
    # Serviceability swagger.json

    
    value = fields.Float(required=False)
    
    unit = fields.Str(required=False)
    


class Trader(BaseSchema):
    # Serviceability swagger.json

    
    name = fields.Str(required=False)
    
    address = fields.Str(required=False)
    


class ProductPublish(BaseSchema):
    # Serviceability swagger.json

    
    product_online_date = fields.Str(required=False)
    
    is_set = fields.Boolean(required=False)
    


class TaxIdentifier(BaseSchema):
    # Serviceability swagger.json

    
    hsn_code = fields.Str(required=False)
    
    hsn_code_id = fields.Str(required=False)
    
    reporting_hsn = fields.Str(required=False)
    


class ReturnConfig(BaseSchema):
    # Serviceability swagger.json

    
    returnable = fields.Boolean(required=False)
    
    time = fields.Int(required=False)
    
    unit = fields.Str(required=False)
    


class CustomOrder(BaseSchema):
    # Serviceability swagger.json

    
    is_custom_order = fields.Boolean(required=False)
    
    manufacturing_time = fields.Int(required=False)
    
    manufacturing_time_unit = fields.Str(required=False)
    


class Size(BaseSchema):
    # Serviceability swagger.json

    
    size = fields.Str(required=False)
    
    size_priority = fields.Int(required=False)
    
    item_dimensions_unit_of_measure = fields.Str(required=False)
    
    price_transfer = fields.Float(required=False)
    
    item_height = fields.Float(required=False)
    
    item_length = fields.Float(required=False)
    
    item_width = fields.Float(required=False)
    
    item_weight = fields.Float(required=False)
    
    item_weight_unit_of_measure = fields.Str(required=False)
    
    price = fields.Float(required=False)
    
    price_effective = fields.Float(required=False)
    
    is_set = fields.Boolean(required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    identifiers = fields.List(fields.Nested(Identifier, required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    


class Identifier(BaseSchema):
    # Serviceability swagger.json

    
    gtin_type = fields.Str(required=False)
    
    gtin_value = fields.Str(required=False)
    
    primary = fields.Boolean(required=False)
    


class Page(BaseSchema):
    # Serviceability swagger.json

    
    item_total = fields.Int(required=False)
    
    next_id = fields.Str(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    has_next = fields.Boolean(required=False)
    
    current = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    size = fields.Int(required=False)
    
    page_size = fields.Int(required=False)
    


class FulfillmentOptionStore(BaseSchema):
    # Serviceability swagger.json

    
    uid = fields.Int(required=False)
    
    store_code = fields.Str(required=False)
    
    address = fields.Nested(Address, required=False)
    
    company_id = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    store_type = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    avg_order_processing_time = fields.Int(required=False)
    
    timezone = fields.Str(required=False)
    
    holiday_list = fields.List(fields.List(fields.Str(required=False), required=False), required=False)
    
    customfields = fields.Dict(required=False)
    
    is_open = fields.Boolean(required=False)
    
    promise_customfields = fields.Dict(required=False)
    
    distance = fields.Nested(StoreDistance, required=False)
    
    timing = fields.Nested(StoreTimingDetails, required=False)
    


class Address(BaseSchema):
    # Serviceability swagger.json

    
    address1 = fields.Str(required=False)
    
    address2 = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    
    postal_code = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    latitude = fields.Float(required=False)
    
    longitude = fields.Float(required=False)
    
    country_code = fields.Str(required=False)
    
    lat_long = fields.Nested(LatLong, required=False)
    


class LatLong(BaseSchema):
    # Serviceability swagger.json

    
    type = fields.Str(required=False)
    
    coordinates = fields.List(fields.Float(required=False), required=False)
    


class StoreDistance(BaseSchema):
    # Serviceability swagger.json

    
    value = fields.Float(required=False, allow_none=True)
    
    unit = fields.Str(required=False)
    
    reason = fields.Str(required=False, allow_none=True)
    


class StoreTimingDetails(BaseSchema):
    # Serviceability swagger.json

    
    operational_timing = fields.List(fields.Nested(StoreTiming, required=False), required=False)
    
    order_acceptance_timing = fields.List(fields.Nested(StoreTiming, required=False), required=False)
    


class StoreTiming(BaseSchema):
    # Serviceability swagger.json

    
    weekday = fields.Str(required=False)
    
    open = fields.Boolean(required=False)
    
    opening = fields.Nested(Time, required=False)
    
    closing = fields.Nested(Time, required=False)
    


class Time(BaseSchema):
    # Serviceability swagger.json

    
    hour = fields.Int(required=False)
    
    minute = fields.Int(required=False)
    


class FulfillmentOptionValidate(BaseSchema):
    # Serviceability swagger.json

    
    entity_filter_type = fields.Str(required=False)
    
    fulfillment_option_type = fields.Str(required=False)
    


class ProductSchema(BaseSchema):
    # Serviceability swagger.json

    
    type = fields.Str(required=False)
    
    values = fields.List(fields.Raw(required=False), required=False)
    


class StoresSchema(BaseSchema):
    # Serviceability swagger.json

    
    type = fields.Str(required=False)
    
    values = fields.List(fields.Int(required=False), required=False)
    


class CreatedBy(BaseSchema):
    # Serviceability swagger.json

    
    id = fields.Str(required=False, allow_none=True)
    


class ModifiedBy(BaseSchema):
    # Serviceability swagger.json

    
    id = fields.Str(required=False, allow_none=True)
    


class ListViewItems(BaseSchema):
    # Serviceability swagger.json

    
    zone_id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    geo_areas = fields.List(fields.Nested(GeoArea, required=False), required=False)
    
    slug = fields.Str(required=False)
    
    stores = fields.Nested(ListViewProduct, required=False)
    
    is_active = fields.Boolean(required=False)
    
    product = fields.Nested(ListViewProduct, required=False)
    
    company_id = fields.Int(required=False)
    
    application_id = fields.Str(required=False)
    
    created_by = fields.Nested(CreatedBy, required=False)
    
    modified_by = fields.Nested(ModifiedBy, required=False)
    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    summary = fields.Nested(Summary, required=False)
    


class GeoArea(BaseSchema):
    # Serviceability swagger.json

    
    id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    


class ListViewProduct(BaseSchema):
    # Serviceability swagger.json

    
    type = fields.Str(required=False)
    
    values = fields.List(fields.Str(required=False), required=False)
    


class Summary(BaseSchema):
    # Serviceability swagger.json

    
    stores_count = fields.Int(required=False)
    
    products_count = fields.Int(required=False)
    
    regions = fields.List(fields.Nested(RegionSchema, required=False), required=False)
    


class RegionSchema(BaseSchema):
    # Serviceability swagger.json

    
    name = fields.Str(required=False)
    
    count = fields.Int(required=False)
    


class ZoneStores(BaseSchema):
    # Serviceability swagger.json

    
    type = fields.Raw(required=False)
    
    values = fields.Raw(required=False)
    


class ZoneProduct(BaseSchema):
    # Serviceability swagger.json

    
    type = fields.Raw(required=False)
    
    values = fields.Raw(required=False)
    


class ZoneBulkItem(BaseSchema):
    # Serviceability swagger.json

    
    batch_id = fields.Str(required=False)
    
    file_path = fields.Str(required=False, allow_none=True)
    
    total = fields.Raw(required=False)
    
    failed = fields.Raw(required=False)
    
    error_file_url = fields.Str(required=False, allow_none=True)
    
    action = fields.Raw(required=False)
    
    updated_at = fields.Raw(required=False)
    
    updated_by = fields.Raw(required=False)
    
    type = fields.Raw(required=False)
    
    stage = fields.Raw(required=False)
    


class PincodeMopUpdateResult(BaseSchema):
    # Serviceability swagger.json

    
    pincode = fields.Int(required=False)
    
    channel_id = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    


class PincodeCodStatusItem(BaseSchema):
    # Serviceability swagger.json

    
    active = fields.Boolean(required=False)
    
    pincode = fields.Str(required=False)
    


class PincodeCodStatusListingSummary(BaseSchema):
    # Serviceability swagger.json

    
    total_active_pincodes = fields.Int(required=False)
    
    total_inactive_pincodes = fields.Int(required=False)
    


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
    


class Area(BaseSchema):
    # Serviceability swagger.json

    
    regions = fields.List(fields.Str(required=False), required=False)
    
    country = fields.Str(required=False)
    


class GeoAreaResponseDetail(BaseSchema):
    # Serviceability swagger.json

    
    type = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    message = fields.Str(required=False, allow_none=True)
    


class GeoAreaItemResult(BaseSchema):
    # Serviceability swagger.json

    
    company_id = fields.Int(required=False)
    
    application_id = fields.Str(required=False)
    
    geoarea_id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    region_type = fields.Str(required=False, allow_none=True)
    
    type = fields.Str(required=False)
    
    areas = fields.List(fields.Nested(AreaExpanded, required=False), required=False)
    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    created_by = fields.Nested(CreatedBy, required=False)
    
    modified_by = fields.Nested(ModifiedBy, required=False)
    


class AreaExpanded(BaseSchema):
    # Serviceability swagger.json

    
    country = fields.Nested(Country, required=False)
    
    regions = fields.List(fields.Nested(Region, required=False), required=False)
    


class Country(BaseSchema):
    # Serviceability swagger.json

    
    uid = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    


class Region(BaseSchema):
    # Serviceability swagger.json

    
    uid = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    sub_type = fields.Str(required=False)
    
    parent_id = fields.List(fields.Str(required=False), required=False)
    


class Page2(BaseSchema):
    # Serviceability swagger.json

    
    size = fields.Int(required=False)
    
    item_total = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    current = fields.Int(required=False)
    
    has_next = fields.Boolean(required=False)
    


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
    
    order_place_date = fields.Nested(DateOperations, required=False)
    
    store_ids = fields.Nested(IntComparisonOperations, required=False)
    
    store_type = fields.Nested(StringComparisonOperations, required=False)
    
    store_tags = fields.Nested(StringComparisonOperations, required=False)
    
    shipment_weight = fields.Nested(ArithmeticOperations, required=False)
    
    shipment_cost = fields.Nested(ArithmeticOperations, required=False)
    
    shipment_volumetric_weight = fields.Nested(ArithmeticOperations, required=False)
    
    store_customer_location = fields.Nested(StringComparisonOperations, required=False)
    


class LocationRule(BaseSchema):
    # Serviceability swagger.json

    
    type = fields.Str(required=False)
    
    includes = fields.List(fields.Nested(LocationRuleValues, required=False), required=False)
    


class LocationRuleValues(BaseSchema):
    # Serviceability swagger.json

    
    uid = fields.Str(required=False)
    
    sub_type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    parent_id = fields.List(fields.Str(required=False), required=False)
    
    parent_ids = fields.List(fields.Str(required=False), required=False)
    
    id = fields.Str(required=False)
    


class StringComparisonOperations(BaseSchema):
    # Serviceability swagger.json

    
    includes = fields.List(fields.Str(required=False), required=False)
    


class IntComparisonOperations(BaseSchema):
    # Serviceability swagger.json

    
    includes = fields.List(fields.Int(required=False), required=False)
    


class DateOperations(BaseSchema):
    # Serviceability swagger.json

    
    lte = fields.Str(required=False)
    
    gte = fields.Str(required=False)
    


class ArithmeticOperations(BaseSchema):
    # Serviceability swagger.json

    
    lt = fields.Int(required=False, allow_none=True)
    
    gt = fields.Int(required=False, allow_none=True)
    
    lte = fields.Int(required=False, allow_none=True)
    
    gte = fields.Int(required=False, allow_none=True)
    


class CourierPartnerRuleCPListResult(BaseSchema):
    # Serviceability swagger.json

    
    account_id = fields.Str(required=False)
    
    extension_id = fields.Str(required=False)
    
    is_self_ship = fields.Boolean(required=False)
    
    scheme_rules = fields.Nested(CourierPartnerSchemeDetailsModel, required=False)
    
    stage = fields.Str(required=False)
    


class CourierPartnerSchemeDefaultTat(BaseSchema):
    # Serviceability swagger.json

    
    enabled = fields.Boolean(required=False)
    
    tat = fields.Nested(CourierPartnerSchemeTat, required=False)
    


class CourierPartnerSchemeTat(BaseSchema):
    # Serviceability swagger.json

    
    min = fields.Int(required=False)
    
    max = fields.Int(required=False)
    
    unit = fields.Str(required=False)
    


class CourierPartnerSchemeFeatures(BaseSchema):
    # Serviceability swagger.json

    
    doorstep_qc = fields.Boolean(required=False)
    
    qr = fields.Boolean(required=False)
    
    mps = fields.Boolean(required=False)
    
    b2b = fields.Boolean(required=False)
    
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
    


class CourierPartnerList(BaseSchema):
    # Serviceability swagger.json

    
    extension_id = fields.Str(required=False)
    
    account_id = fields.Str(required=False)
    


class ShipmentsCourierPartnersServiceability(BaseSchema):
    # Serviceability swagger.json

    
    pincode = fields.Str(required=False)
    
    sector_code = fields.Str(required=False)
    
    state_code = fields.Str(required=False)
    
    city_code = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    


class CPShipments(BaseSchema):
    # Serviceability swagger.json

    
    id = fields.Str(required=False)
    
    location_id = fields.Float(required=False)
    
    location_tags = fields.List(fields.Str(required=False), required=False)
    
    shipment_weight = fields.Float(required=False)
    
    shipment_volumetric_weight = fields.Float(required=False)
    
    shipment_cost = fields.Float(required=False)
    
    shipment_dimension = fields.Nested(ShipmentDimension, required=False)
    
    courier_partner_schemes = fields.List(fields.Str(required=False), required=False)
    
    location_type = fields.Str(required=False)
    
    articles = fields.List(fields.Nested(ShipmentsArticles, required=False), required=False)
    


class ShipmentsArticles(BaseSchema):
    # Serviceability swagger.json

    
    id = fields.Str(required=False)
    
    item_id = fields.Int(required=False)
    
    sla = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    size = fields.Str(required=False)
    
    group_id = fields.Str(required=False)
    
    weight = fields.Nested(ArticleWeight, required=False)
    
    attributes = fields.Nested(ArticleAttributes, required=False)
    
    category_id = fields.Int(required=False)
    
    department_id = fields.Int(required=False)
    
    dimension = fields.Nested(ArticleDimension, required=False)
    
    price = fields.Float(required=False)
    
    brand_id = fields.Int(required=False)
    
    quantity = fields.Int(required=False)
    
    manufacturing_time = fields.Int(required=False)
    
    manufacturing_time_unit = fields.Str(required=False)
    
    mto_quantity = fields.Int(required=False)
    
    is_gift = fields.Boolean(required=False)
    
    is_set = fields.Boolean(required=False)
    
    set = fields.Nested(ArticleSet, required=False)
    
    set_quantity = fields.Int(required=False)
    
    delivery_slots = fields.Nested(ArticleDeliverySlots, required=False)
    
    return_reason = fields.Nested(ArticleReturnReason, required=False)
    


class ArticleWeight(BaseSchema):
    # Serviceability swagger.json

    
    shipping = fields.Int(required=False)
    
    unit = fields.Str(required=False)
    
    is_default = fields.Boolean(required=False)
    


class ArticleAttributes(BaseSchema):
    # Serviceability swagger.json

    
    battery_operated = fields.Str(required=False)
    
    is_flammable = fields.Str(required=False)
    


class ArticleDimension(BaseSchema):
    # Serviceability swagger.json

    
    height = fields.Float(required=False)
    
    is_default = fields.Boolean(required=False)
    
    length = fields.Float(required=False)
    
    unit = fields.Str(required=False)
    
    width = fields.Float(required=False)
    


class ArticleSet(BaseSchema):
    # Serviceability swagger.json

    
    name = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    size_distribution = fields.Nested(ArticleSizeDistribution, required=False)
    


class ArticleSizeDistribution(BaseSchema):
    # Serviceability swagger.json

    
    sizes = fields.List(fields.Nested(SetSize, required=False), required=False)
    


class SetSize(BaseSchema):
    # Serviceability swagger.json

    
    pieces = fields.Int(required=False)
    
    size = fields.Str(required=False)
    


class ArticleDeliverySlots(BaseSchema):
    # Serviceability swagger.json

    
    delivery_date = fields.Str(required=False)
    
    min_slot = fields.Str(required=False)
    
    max_slot = fields.Str(required=False)
    


class ArticleReturnReason(BaseSchema):
    # Serviceability swagger.json

    
    qc_type = fields.List(fields.Str(required=False), required=False)
    


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
    
    delivery_promise = fields.Nested(CourierPartnerPromise, required=False)
    


class CourierPartnerConfig(BaseSchema):
    # Serviceability swagger.json

    
    rule_ids = fields.List(fields.Str(required=False), required=False)
    
    sort = fields.List(fields.Str(required=False), required=False)
    
    manual_priority = fields.List(fields.Str(required=False), required=False)
    


class BuyboxRuleConfig(BaseSchema):
    # Serviceability swagger.json

    
    store_type_priority = fields.List(fields.Str(required=False), required=False)
    
    store_tag_priority = fields.List(fields.Str(required=False), required=False)
    
    sort = fields.List(fields.Str(required=False), required=False)
    


class PromiseConfig(BaseSchema):
    # Serviceability swagger.json

    
    store_attributes = fields.Nested(StorePromiseAttributeConfig, required=False)
    
    delivery_service_attributes = fields.Nested(DeliveryServiceAttributeConfig, required=False)
    
    buffer_field = fields.Nested(BufferField, required=False)
    


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
    
    is_all_dps_considered = fields.Boolean(required=False)
    


class BufferField(BaseSchema):
    # Serviceability swagger.json

    
    unit = fields.Str(required=False)
    
    value = fields.Int(required=False)
    
    enabled = fields.Boolean(required=False)
    


class StorePrioritySchema(BaseSchema):
    # Serviceability swagger.json

    
    id = fields.Int(required=False)
    
    name = fields.Str(required=False)
    


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
    
    order_place_date = fields.Nested(DateOperations, required=False)
    
    zone_ids = fields.Nested(StringComparisonOperations, required=False)
    


class CustomerRadiusSchema(BaseSchema):
    # Serviceability swagger.json

    
    unit = fields.Str(required=False)
    
    lt = fields.Int(required=False)
    
    lte = fields.Int(required=False)
    
    gt = fields.Int(required=False)
    
    gte = fields.Int(required=False)
    


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
    


class PackageMaterialRule(BaseSchema):
    # Serviceability swagger.json

    
    rule_id = fields.Str(required=False)
    
    quantity = fields.Nested(PackageMaterialRuleQuantity, required=False)
    
    weight = fields.Int(required=False)
    


class PackageMaterialRuleQuantity(BaseSchema):
    # Serviceability swagger.json

    
    min = fields.Int(required=False)
    
    max = fields.Int(required=False)
    


class Channel(BaseSchema):
    # Serviceability swagger.json

    
    type = fields.Str(required=False)
    
    id = fields.Str(required=False)
    


class PackageRuleCategory(BaseSchema):
    # Serviceability swagger.json

    
    includes = fields.List(fields.Int(required=False), required=False)
    


class PackageRuleProduct(BaseSchema):
    # Serviceability swagger.json

    
    includes = fields.List(fields.Int(required=False), required=False)
    


class PackageRuleProductTag(BaseSchema):
    # Serviceability swagger.json

    
    includes = fields.List(fields.Str(required=False), required=False)
    


class PackageRuleDepartmentId(BaseSchema):
    # Serviceability swagger.json

    
    includes = fields.List(fields.Int(required=False), required=False)
    


class PackageRuleProductAttributes(BaseSchema):
    # Serviceability swagger.json

    
    includes = fields.List(fields.Dict(required=False), required=False)
    


class PackageChannel(BaseSchema):
    # Serviceability swagger.json

    
    store_filter = fields.Nested(StoreFilter, required=False)
    
    app_id = fields.Str(required=False)
    


class StoreFilter(BaseSchema):
    # Serviceability swagger.json

    
    type = fields.Str(required=False)
    
    ids = fields.List(fields.Int(required=False), required=False)
    


class PackageRuleSchema(BaseSchema):
    # Serviceability swagger.json

    
    quantity = fields.Nested(Quantity, required=False)
    
    rule_id = fields.Str(required=False)
    
    weight = fields.Float(required=False)
    


class Quantity(BaseSchema):
    # Serviceability swagger.json

    
    min = fields.Int(required=False)
    
    max = fields.Int(required=False)
    


class PackagePageInfo(BaseSchema):
    # Serviceability swagger.json

    
    type = fields.Str(required=False)
    
    size = fields.Int(required=False)
    
    current = fields.Int(required=False)
    
    has_next = fields.Boolean(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    item_total = fields.Int(required=False)
    


class OptimalLocationAssignedStoresResult(BaseSchema):
    # Serviceability swagger.json

    
    store_id = fields.Int(required=False)
    
    articles = fields.List(fields.Nested(OptimalLocationArticlesResult, required=False), required=False)
    


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
    


class ArticleAssignment(BaseSchema):
    # Serviceability swagger.json

    
    level = fields.Str(required=False)
    
    strategy = fields.Str(required=False)
    


class LocationDetailsServiceability(BaseSchema):
    # Serviceability swagger.json

    
    pincode = fields.Str(required=False)
    
    sector = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    country_iso_code = fields.Str(required=False)
    
    location = fields.Nested(ServiceabilityLocation, required=False)
    


class ServiceabilityLocation(BaseSchema):
    # Serviceability swagger.json

    
    longitude = fields.Str(required=False)
    
    latitude = fields.Str(required=False)
    


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
    


class GetCountriesItems(BaseSchema):
    # Serviceability swagger.json

    
    id = fields.Str(required=False)
    
    sub_type = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    iso2 = fields.Str(required=False)
    
    iso3 = fields.Str(required=False)
    
    timezones = fields.List(fields.Str(required=False), required=False)
    
    hierarchy = fields.List(fields.Nested(HierarchyItems, required=False), required=False)
    
    phone_code = fields.Str(required=False)
    
    currency = fields.Nested(CurrencyObject, required=False)
    
    type = fields.Str(required=False)
    
    latitude = fields.Str(required=False)
    
    longitude = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    has_next_hierarchy = fields.Boolean(required=False)
    


class HierarchyItems(BaseSchema):
    # Serviceability swagger.json

    
    name = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    


class CurrencyObject(BaseSchema):
    # Serviceability swagger.json

    
    code = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    symbol = fields.Str(required=False)
    


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
    
    localities = fields.List(fields.Nested(LocalityParent, required=False), required=False)
    
    code = fields.Str(required=False)
    
    iso2 = fields.Str(required=False)
    
    iso3 = fields.Str(required=False)
    
    currency = fields.Dict(required=False)
    
    phone_code = fields.Str(required=False)
    
    hierarchy = fields.Dict(required=False)
    
    latitude = fields.Str(required=False)
    
    longitude = fields.Str(required=False)
    


class PincodeLatLongData(BaseSchema):
    # Serviceability swagger.json

    
    type = fields.Str(required=False)
    
    coordinates = fields.List(fields.Float(required=False), required=False)
    


class LocalityParent(BaseSchema):
    # Serviceability swagger.json

    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    parent_ids = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    
    serviceability = fields.Dict(required=False)
    
    parent_uid = fields.Str(required=False, allow_none=True)
    
    code = fields.Str(required=False)
    
    iso2 = fields.Str(required=False)
    
    iso3 = fields.Str(required=False)
    
    currency = fields.Dict(required=False)
    
    phone_code = fields.Str(required=False)
    
    hierarchy = fields.Dict(required=False)
    
    latitude = fields.Str(required=False)
    
    longitude = fields.Str(required=False)
    


class CountryMetaFields(BaseSchema):
    # Serviceability swagger.json

    
    application_fields = fields.Nested(ApplicationFields, required=False)
    


class ApplicationFields(BaseSchema):
    # Serviceability swagger.json

    
    address = fields.List(fields.Nested(GetCountryFieldsAddress, required=False), required=False)
    
    serviceability_fields = fields.List(fields.Str(required=False), required=False)
    
    address_template = fields.Nested(GetCountryFieldsAddressTemplateApplication, required=False)
    


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
    


class GetCountryFieldsAddressValues(BaseSchema):
    # Serviceability swagger.json

    
    get_one = fields.Nested(GetOneOrAll, required=False)
    
    get_all = fields.Nested(GetOneOrAll, required=False)
    


class GetOneOrAll(BaseSchema):
    # Serviceability swagger.json

    
    operation_id = fields.Str(required=False)
    
    params = fields.Nested(GetOneOrAllParams, required=False)
    


class GetOneOrAllParams(BaseSchema):
    # Serviceability swagger.json

    
    path = fields.Nested(GetOneOrAllPath, required=False)
    
    query = fields.Nested(GetOneOrAllQuery, required=False)
    


class GetOneOrAllPath(BaseSchema):
    # Serviceability swagger.json

    
    type = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class GetOneOrAllQuery(BaseSchema):
    # Serviceability swagger.json

    
    country = fields.Str(required=False, allow_none=True)
    
    state = fields.Str(required=False, allow_none=True)
    
    city = fields.Str(required=False, allow_none=True)
    
    sector = fields.Str(required=False, allow_none=True)
    


class GetCountryFieldsAddressTemplateApplication(BaseSchema):
    # Serviceability swagger.json

    
    checkout_form = fields.Str(required=False)
    
    store_os_form = fields.Str(required=False)
    
    default_display = fields.Str(required=False)
    


class CountryHierarchy(BaseSchema):
    # Serviceability swagger.json

    
    display_name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    


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
    


class LocalityParents(BaseSchema):
    # Serviceability swagger.json

    
    city = fields.Dict(required=False, allow_none=True)
    
    state = fields.Dict(required=False, allow_none=True)
    
    country = fields.Dict(required=False, allow_none=True)
    


class ZoneConfig(BaseSchema):
    # Serviceability swagger.json

    
    serviceability_type = fields.Str(required=False)
    
    active_count = fields.Int(required=False)
    
    total_count = fields.Int(required=False)
    


class PromiseType(BaseSchema):
    # Serviceability swagger.json

    
    display_name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    is_default = fields.Boolean(required=False)
    
    is_all_dps_considered = fields.Boolean(required=False)
    


class InstallCourierPartnerItemsSchema(BaseSchema):
    # Serviceability swagger.json

    
    description = fields.Str(required=False)
    
    extention_type = fields.Str(required=False)
    
    is_hidden = fields.Boolean(required=False)
    
    is_installed = fields.Boolean(required=False)
    
    launch_type = fields.Str(required=False)
    
    logo = fields.Dict(required=False)
    
    modified_at = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    organization_id = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    


class HistoryObject(BaseSchema):
    # Serviceability swagger.json

    
    batch_id = fields.Str(required=False)
    
    entity_type = fields.Str(required=False)
    
    error_file_url = fields.Str(required=False, allow_none=True)
    
    file_path = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    updated_by = fields.Str(required=False)
    
    updated_at = fields.Str(required=False, allow_none=True)
    
    total_count = fields.Int(required=False)
    
    total_error_count = fields.Int(required=False)
    


