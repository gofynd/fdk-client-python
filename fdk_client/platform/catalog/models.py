"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema


from .enums import *



class StoreTagsResponseSchema(BaseSchema):
    pass


class DiscountMeta(BaseSchema):
    pass


class ProductMinMaxPrice(BaseSchema):
    pass


class ProductPrice(BaseSchema):
    pass


class ProductPricesPage(BaseSchema):
    pass


class ProductPriceItem(BaseSchema):
    pass


class ProductPrices(BaseSchema):
    pass


class ProductFiltersKeysOnly(BaseSchema):
    pass


class GetQueryFiltersKeysResponseSchema(BaseSchema):
    pass


class GetQueryFiltersValuesResponseSchema(BaseSchema):
    pass


class ProductQueryFiltersValue(BaseSchema):
    pass


class CompanyDRIListResponseSchema(BaseSchema):
    pass


class CompanyDRIResponseSchema(BaseSchema):
    pass


class SearchResponseSchema(BaseSchema):
    pass


class MerchandisingQuery(BaseSchema):
    pass


class MerchandisingSearchQuery(BaseSchema):
    pass


class MerchandisingFilter(BaseSchema):
    pass


class MerchandisingRuleQuery(BaseSchema):
    pass


class MerchandisingRulesList(BaseSchema):
    pass


class MerchDataItem(BaseSchema):
    pass


class MerchSearchQuery(BaseSchema):
    pass


class MerchQueryCondition(BaseSchema):
    pass


class MerchFilter(BaseSchema):
    pass


class SuccessResponseMerchandising(BaseSchema):
    pass


class MerchandiseQueryResponseSchema(BaseSchema):
    pass


class Filter(BaseSchema):
    pass


class MerchandisingRuleQueryPart(BaseSchema):
    pass


class MerchandisingRuleQueryPost(BaseSchema):
    pass


class MerchandisingRuleSave(BaseSchema):
    pass


class PinItem(BaseSchema):
    pass


class PinItemRequestSchema(BaseSchema):
    pass


class PinRequestSchema(BaseSchema):
    pass


class PinResponseSchema(BaseSchema):
    pass


class HideAttribute(BaseSchema):
    pass


class HideAttributeRequestSchema(BaseSchema):
    pass


class HideResponseSchema(BaseSchema):
    pass


class HideRequestSchema(BaseSchema):
    pass


class PostBoostAttribute(BaseSchema):
    pass


class BoostAttribute(BaseSchema):
    pass


class GetMerchandisingRuleBoostAction(BaseSchema):
    pass


class PostMerchandisingRuleBoostAction(BaseSchema):
    pass


class GetMerchandisingRuleBuryAction(BaseSchema):
    pass


class Action(BaseSchema):
    pass


class AllSizes(BaseSchema):
    pass


class AllowSingleRequestSchema(BaseSchema):
    pass


class AppCatalogConfiguration(BaseSchema):
    pass


class AppCategoryReturnConfig(BaseSchema):
    pass


class ReturnConfigResponseSchema(BaseSchema):
    pass


class AppCategoryReturnConfigResponseSchema(BaseSchema):
    pass


class AppConfiguration(BaseSchema):
    pass


class AppConfigurationCreateDetail(BaseSchema):
    pass


class AppConfigurationDetail(BaseSchema):
    pass


class ValueConfigType(BaseSchema):
    pass


class AppConfigurationsFilter(BaseSchema):
    pass


class AppConfigurationsFilterResponseSchema(BaseSchema):
    pass


class ApplicationBrandJson(BaseSchema):
    pass


class ApplicationCategoryJson(BaseSchema):
    pass


class ApplicationDepartment(BaseSchema):
    pass


class ApplicationDepartmentJson(BaseSchema):
    pass


class ApplicationDepartmentListingResponseSchema(BaseSchema):
    pass


class ApplicationItemMOQ(BaseSchema):
    pass


class ApplicationItemMeta(BaseSchema):
    pass


class ApplicationItemSeoSitemap(BaseSchema):
    pass


class ApplicationItemSEO(BaseSchema):
    pass


class ApplicationProductsSchema(BaseSchema):
    pass


class ApplicationProductListingResponseSchema(BaseSchema):
    pass


class OperatorsResponseSchema(BaseSchema):
    pass


class ApplicationStoreJson(BaseSchema):
    pass


class AppReturnConfigResponseSchema(BaseSchema):
    pass


class ArticleStoreResponseSchema(BaseSchema):
    pass


class AttributeDetailsGroup(BaseSchema):
    pass


class AttributeMaster(BaseSchema):
    pass


class AttributeMasterDetails(BaseSchema):
    pass


class AttributeMasterFilter(BaseSchema):
    pass


class AttributeMasterMandatoryDetails(BaseSchema):
    pass


class AttributeMasterMeta(BaseSchema):
    pass


class AttributeMasterSchema(BaseSchema):
    pass


class AttributeSchemaRange(BaseSchema):
    pass


class AutoCompleteMedia(BaseSchema):
    pass


class AutocompleteAction(BaseSchema):
    pass


class AutocompletePageAction(BaseSchema):
    pass


class AutocompleteResult(BaseSchema):
    pass


class BannerImage(BaseSchema):
    pass


class BaseAppCategoryReturnConfig(BaseSchema):
    pass


class BaseAppCategoryReturnConfigResponseSchema(BaseSchema):
    pass


class Brand(BaseSchema):
    pass


class BrandLogo(BaseSchema):
    pass


class BrandItem(BaseSchema):
    pass


class ApplicationCategoryListingSchema(BaseSchema):
    pass


class ApplicationCategoryListingItemSchema(BaseSchema):
    pass


class ApplicationBrandListingSchema(BaseSchema):
    pass


class ApplicationBrandListingItemSchema(BaseSchema):
    pass


class BrandListingResponseSchema(BaseSchema):
    pass


class BrandMeta(BaseSchema):
    pass


class BrandMeta1(BaseSchema):
    pass


class BulkAssetResponseSchema(BaseSchema):
    pass


class BulkInventoryGet(BaseSchema):
    pass


class BulkInventoryGetItems(BaseSchema):
    pass


class BulkProductUploadJob(BaseSchema):
    pass


class BulkProductJob(BaseSchema):
    pass


class BulkProductRequestSchema(BaseSchema):
    pass


class CatalogInsightBrand(BaseSchema):
    pass


class CatalogInsightItem(BaseSchema):
    pass


class CatalogInsightResponseSchema(BaseSchema):
    pass


class CategoriesResponseSchema(BaseSchema):
    pass


class Category(BaseSchema):
    pass


class CategoryItems(BaseSchema):
    pass


class CategoryListingResponseSchema(BaseSchema):
    pass


class CategoryMapping(BaseSchema):
    pass


class CategoryMappingValues(BaseSchema):
    pass


class CategoryResponseSchema(BaseSchema):
    pass


class Child(BaseSchema):
    pass


class CollectionBadge(BaseSchema):
    pass


class CollectionBanner(BaseSchema):
    pass


class CollectionBannerResponseSchema(BaseSchema):
    pass


class CollectionCreateResponseSchema(BaseSchema):
    pass


class CollectionImage(BaseSchema):
    pass


class CollectionImageResponseSchema(BaseSchema):
    pass


class CollectionListingFilter(BaseSchema):
    pass


class CollectionListingFilterTag(BaseSchema):
    pass


class CollectionListingFilterType(BaseSchema):
    pass


class CollectionQuery(BaseSchema):
    pass


class CollectionSchedule(BaseSchema):
    pass


class CompanyBrandDetail(BaseSchema):
    pass


class CompanyMeta(BaseSchema):
    pass


class CompanyMeta1(BaseSchema):
    pass


class ConfigErrorResponseSchema(BaseSchema):
    pass


class ConfigSuccessResponseSchema(BaseSchema):
    pass


class ConfigurationBucketPoints(BaseSchema):
    pass


class ConfigurationListing(BaseSchema):
    pass


class ConfigurationListingFilter(BaseSchema):
    pass


class ConfigurationListingFilterConfig(BaseSchema):
    pass


class ConfigurationListingFilterValue(BaseSchema):
    pass


class ConfigurationListingSort(BaseSchema):
    pass


class ConfigurationListingSortConfig(BaseSchema):
    pass


class ConfigurationProduct(BaseSchema):
    pass


class ConfigurationProductDetailsGroups(BaseSchema):
    pass


class ConfigurationProductDetailsConfig(BaseSchema):
    pass


class ConfigurationProductDetailsAttribute(BaseSchema):
    pass


class ConfigurationProductConfig(BaseSchema):
    pass


class ConfigurationProductSimilar(BaseSchema):
    pass


class ConfigurationProductVariant(BaseSchema):
    pass


class ConfigurationProductVariantConfig(BaseSchema):
    pass


class CreateAutocompleteKeyword(BaseSchema):
    pass


class CreateAutocompleteWordsResponseSchema(BaseSchema):
    pass


class CreateCollection(BaseSchema):
    pass


class RerankingBoostItems(BaseSchema):
    pass


class GetSearchRerankDetailResponseSchema(BaseSchema):
    pass


class BoostItem(BaseSchema):
    pass


class GetSearchRerankItemResponseSchema(BaseSchema):
    pass


class GetSearchRerankResponseSchema(BaseSchema):
    pass


class CreateSearchRerankResponseSchema(BaseSchema):
    pass


class UpdateSearchRerankResponseSchema(BaseSchema):
    pass


class UpdateSearchRerankRequestSchema(BaseSchema):
    pass


class CreateSearchRerankRequestSchema(BaseSchema):
    pass


class CreateSearchConfigurationRequestSchema(BaseSchema):
    pass


class CreateSearchConfigurationResponseSchema(BaseSchema):
    pass


class CreateSearchKeyword(BaseSchema):
    pass


class CreateUpdateAppReturnConfig(BaseSchema):
    pass


class CrossSellingResponseSchema(BaseSchema):
    pass


class CustomOrder(BaseSchema):
    pass


class DateMeta(BaseSchema):
    pass


class DefaultKeyRequestSchema(BaseSchema):
    pass


class DeleteAppCategoryReturnConfig(BaseSchema):
    pass


class DeleteResponseSchema(BaseSchema):
    pass


class DeleteSearchConfigurationResponseSchema(BaseSchema):
    pass


class DeleteSearchRerankConfigurationResponseSchema(BaseSchema):
    pass


class Department(BaseSchema):
    pass


class DepartmentCategoryTree(BaseSchema):
    pass


class DepartmentIdentifier(BaseSchema):
    pass


class DepartmentResponseSchema(BaseSchema):
    pass


class ValidationFailedResponseSchema(BaseSchema):
    pass


class DepartmentsResponseSchema(BaseSchema):
    pass


class DimensionResponseSchema(BaseSchema):
    pass


class InventoryDimensionResponseSchema(BaseSchema):
    pass


class Document(BaseSchema):
    pass


class EntityConfiguration(BaseSchema):
    pass


class ErrorResponseSchema(BaseSchema):
    pass


class CategoryErrorResponseSchema(BaseSchema):
    pass


class FilerList(BaseSchema):
    pass


class RawProduct(BaseSchema):
    pass


class RawProductListingResponseSchema(BaseSchema):
    pass


class GTIN(BaseSchema):
    pass


class AttributeDetail(BaseSchema):
    pass


class GetAddressSchema(BaseSchema):
    pass


class GetAllSizes(BaseSchema):
    pass


class FilterResponseSchema(BaseSchema):
    pass


class ValueItem(BaseSchema):
    pass


class GetAppCatalogConfiguration(BaseSchema):
    pass


class GetAppCatalogEntityConfiguration(BaseSchema):
    pass


class GetAutocompleteWordsData(BaseSchema):
    pass


class GetAutocompleteWordsResponseSchema(BaseSchema):
    pass


class GetCatalogConfigurationDetailsProduct(BaseSchema):
    pass


class FilterItem(BaseSchema):
    pass


class CompareFilter(BaseSchema):
    pass


class SimilarFilter(BaseSchema):
    pass


class VariantFilter(BaseSchema):
    pass


class DetailFilter(BaseSchema):
    pass


class DetailFilterValues(BaseSchema):
    pass


class DisplayType(BaseSchema):
    pass


class SimilarItem(BaseSchema):
    pass


class VariantItem(BaseSchema):
    pass


class GetCatalogConfigurationDetailsSchemaListing(BaseSchema):
    pass


class GetCatalogConfigurationMetaData(BaseSchema):
    pass


class GetCollectionDetailNest(BaseSchema):
    pass


class GetCollectionListingResponseSchema(BaseSchema):
    pass


class GetCompanySchema(BaseSchema):
    pass


class ConditionItem(BaseSchema):
    pass


class DataItem(BaseSchema):
    pass


class ValueTypeItem(BaseSchema):
    pass


class SortTypeItem(BaseSchema):
    pass


class GetConfigMetadataResponseSchema(BaseSchema):
    pass


class GetConfigMetadataValues(BaseSchema):
    pass


class AttributeType(BaseSchema):
    pass


class DataType(BaseSchema):
    pass


class ListingValueConfigType(BaseSchema):
    pass


class SizeLimitConfiguration(BaseSchema):
    pass


class ListingDataType(BaseSchema):
    pass


class GetListingConfigResponseSchema(BaseSchema):
    pass


class GetConfigResponseSchema(BaseSchema):
    pass


class ConfigItem(BaseSchema):
    pass


class AttributeConfig(BaseSchema):
    pass


class GetDepartment(BaseSchema):
    pass


class GetInventories(BaseSchema):
    pass


class InventoryWeightResponseSchema(BaseSchema):
    pass


class TraderResponseSchema(BaseSchema):
    pass


class Identifier(BaseSchema):
    pass


class GetInventoriesResponseSchema(BaseSchema):
    pass


class GetLocationSchema(BaseSchema):
    pass


class GetProductBundleCreateResponseSchema(BaseSchema):
    pass


class GetProductBundleListingResponseSchema(BaseSchema):
    pass


class GetProductBundleResponseSchema(BaseSchema):
    pass


class GetProducts(BaseSchema):
    pass


class GetCollectionDetailResponseSchema(BaseSchema):
    pass


class CommonResponseSchemaCollection(BaseSchema):
    pass


class GetQueryFiltersResponseSchema(BaseSchema):
    pass


class CollectionProductSortOn(BaseSchema):
    pass


class CollectionProductFilters(BaseSchema):
    pass


class CollectionProductFiltersValue(BaseSchema):
    pass


class GetCollectionItemsResponseSchema(BaseSchema):
    pass


class CollectionItemSchemaV2(BaseSchema):
    pass


class CollectionItemUpdateSchema(BaseSchema):
    pass


class CollectionQuerySchemaV2(BaseSchema):
    pass


class GetSearchConfigurationResponseSchema(BaseSchema):
    pass


class GetSearchWordsData(BaseSchema):
    pass


class GetSearchWordsResponseSchema(BaseSchema):
    pass


class GlobalValidation(BaseSchema):
    pass


class Guide(BaseSchema):
    pass


class HSNCodesResponseSchema(BaseSchema):
    pass


class HSNData(BaseSchema):
    pass


class HSNDataInsertV2(BaseSchema):
    pass


class Hierarchy(BaseSchema):
    pass


class HsnCodesListingResponseSchemaV2(BaseSchema):
    pass


class Image(BaseSchema):
    pass


class ImageUrls(BaseSchema):
    pass


class InventoryBulkRequestSchema(BaseSchema):
    pass


class InventoryConfig(BaseSchema):
    pass


class InventoryCreateRequestSchema(BaseSchema):
    pass


class InventoryExportFilter(BaseSchema):
    pass


class InventoryExportJobResponseSchema(BaseSchema):
    pass


class InventoryExportItem(BaseSchema):
    pass


class InventoryExportJobListFilters(BaseSchema):
    pass


class InventoryExportJobListStats(BaseSchema):
    pass


class InventoryExportJobList(BaseSchema):
    pass


class InventoryExportJobListResponseSchema(BaseSchema):
    pass


class InventoryExportQuantityFilter(BaseSchema):
    pass


class ExportPatchRequestSchema(BaseSchema):
    pass


class InventoryExportRequestSchema(BaseSchema):
    pass


class EditInventoryDataDownloadsResponseSchema(BaseSchema):
    pass


class EditInventoryDownloadsResponseSchema(BaseSchema):
    pass


class InventoryExportFiltersResponseSchema(BaseSchema):
    pass


class Stats(BaseSchema):
    pass


class InventoryExportResponseSchema(BaseSchema):
    pass


class InventoryFailedReason(BaseSchema):
    pass


class InventoryJobPayload(BaseSchema):
    pass


class InventoryPage(BaseSchema):
    pass


class InventoryPayload(BaseSchema):
    pass


class InventoryV2RequestSchema(BaseSchema):
    pass


class InventoryIdentifier(BaseSchema):
    pass


class InventoryGeoLocation(BaseSchema):
    pass


class InventoryMobileNumber(BaseSchema):
    pass


class InventoryAddress(BaseSchema):
    pass


class InventoryManager(BaseSchema):
    pass


class InventoryStore(BaseSchema):
    pass


class InventoryResponseSchema(BaseSchema):
    pass


class InventoryResponseItem(BaseSchema):
    pass


class InventoryResponsePaginated(BaseSchema):
    pass


class ApplicationInventorySellerIdentifierResponsePaginated(BaseSchema):
    pass


class InventorySellerResponseSchema(BaseSchema):
    pass


class InventorySet(BaseSchema):
    pass


class InventoryStockResponseSchema(BaseSchema):
    pass


class InventoryUpdateResponseSchema(BaseSchema):
    pass


class InventoryValidationResponseSchema(BaseSchema):
    pass


class InvoiceCredSchema(BaseSchema):
    pass


class InvoiceDetailsSchema(BaseSchema):
    pass


class Items(BaseSchema):
    pass


class PriceRange(BaseSchema):
    pass


class ProductPriceRangeSchema(BaseSchema):
    pass


class LimitedProductData(BaseSchema):
    pass


class ListSizeGuide(BaseSchema):
    pass


class LocationDayWiseSchema(BaseSchema):
    pass


class LocationTimingSchema(BaseSchema):
    pass


class LocationIntegrationType(BaseSchema):
    pass


class LocationListSchema(BaseSchema):
    pass


class LocationManagerSchema(BaseSchema):
    pass


class Logo(BaseSchema):
    pass


class MOQData(BaseSchema):
    pass


class ManufacturerResponseSchema(BaseSchema):
    pass


class InventoryManufacturerResponseSchema(BaseSchema):
    pass


class Media(BaseSchema):
    pass


class Media1(BaseSchema):
    pass


class DepartmentMedia(BaseSchema):
    pass


class Meta(BaseSchema):
    pass


class GuideHeaders(BaseSchema):
    pass


class GuideValues(BaseSchema):
    pass


class Header(BaseSchema):
    pass


class MetaDataListingFilterMetaResponseSchema(BaseSchema):
    pass


class MetaDataListingFilterResponseSchema(BaseSchema):
    pass


class MetaDataListingResponseSchema(BaseSchema):
    pass


class MetaDataListingSortMetaResponseSchema(BaseSchema):
    pass


class MetaDataListingSortResponseSchema(BaseSchema):
    pass


class MetaFields(BaseSchema):
    pass


class NetQuantity(BaseSchema):
    pass


class NetQuantityResponseSchema(BaseSchema):
    pass


class NextSchedule(BaseSchema):
    pass


class OptinCompanyBrandDetailsView(BaseSchema):
    pass


class OptinAddress(BaseSchema):
    pass


class OptinDocument(BaseSchema):
    pass


class OptinBusinessCountryInfo(BaseSchema):
    pass


class OptinCompanyDetail(BaseSchema):
    pass


class OptinCompanyMetrics(BaseSchema):
    pass


class OptinStoreDetails(BaseSchema):
    pass


class OwnerAppItemResponseSchema(BaseSchema):
    pass


class Page(BaseSchema):
    pass


class PageResponseSchema(BaseSchema):
    pass


class PageResponseType(BaseSchema):
    pass


class Price(BaseSchema):
    pass


class ProductListingDetailPrice(BaseSchema):
    pass


class PriceArticle(BaseSchema):
    pass


class PriceMeta(BaseSchema):
    pass


class ProdcutTemplateCategoriesResponseSchema(BaseSchema):
    pass


class Product(BaseSchema):
    pass


class ProductAttributesResponseSchema(BaseSchema):
    pass


class ProductBrand(BaseSchema):
    pass


class ProductBulkAssets(BaseSchema):
    pass


class ProductBulkRequestSchema(BaseSchema):
    pass


class InventoryBulkJob(BaseSchema):
    pass


class ProductBulkResponseSchema(BaseSchema):
    pass


class InventoryBulkResponseSchema(BaseSchema):
    pass


class ProductBulkRequestSchemaList(BaseSchema):
    pass


class ProductBundleItem(BaseSchema):
    pass


class ProductBundleRequestSchema(BaseSchema):
    pass


class ProductBundleUpdateRequestSchema(BaseSchema):
    pass


class ProductConfigurationDownloads(BaseSchema):
    pass


class ProductCreateUpdateSizesSchema(BaseSchema):
    pass


class ProductCreateUpdateSchemaV2(BaseSchema):
    pass


class ProductDetail(BaseSchema):
    pass


class ApplicationProductCategoryItem(BaseSchema):
    pass


class ApplicationProductMedia(BaseSchema):
    pass


class ProductDetailAttribute(BaseSchema):
    pass


class ProductDetailGroupedAttribute(BaseSchema):
    pass


class PatchProductDownloadsDataResponseSchema(BaseSchema):
    pass


class PatchProductDownloadsResponseSchema(BaseSchema):
    pass


class ProductDownloadFilters(BaseSchema):
    pass


class CreateProductDownloadsDataResponseSchema(BaseSchema):
    pass


class CreateProductDownloadsResponseSchema(BaseSchema):
    pass


class GetProductDownloadsResponseSchema(BaseSchema):
    pass


class ProductDownloadsResponseSchema(BaseSchema):
    pass


class ProductFilters(BaseSchema):
    pass


class ProductFiltersKey(BaseSchema):
    pass


class ProductFiltersValue(BaseSchema):
    pass


class ApplicationCategoryAction(BaseSchema):
    pass


class ApplicationCategoryItem(BaseSchema):
    pass


class CategoryPageAction(BaseSchema):
    pass


class CategoryQuery(BaseSchema):
    pass


class CategoryImage(BaseSchema):
    pass


class PageAction(BaseSchema):
    pass


class ActionObject(BaseSchema):
    pass


class ProductListingPrice(BaseSchema):
    pass


class ProductListingResponseSchema(BaseSchema):
    pass


class ProductListingResponseV2Schema(BaseSchema):
    pass


class ProductVerificationModel(BaseSchema):
    pass


class ProductPublish(BaseSchema):
    pass


class ProductPublished(BaseSchema):
    pass


class ProductReturnConfigSchema(BaseSchema):
    pass


class ProductReturnConfigBaseSchema(BaseSchema):
    pass


class SizeDetails(BaseSchema):
    pass


class ProductSchemaV2(BaseSchema):
    pass


class ProductSize(BaseSchema):
    pass


class ProductSizeDeleteDataResponseSchema(BaseSchema):
    pass


class ProductSizeDeleteResponseSchema(BaseSchema):
    pass


class ProductSortOn(BaseSchema):
    pass


class ProductTagsViewResponseSchema(BaseSchema):
    pass


class ProductTemplate(BaseSchema):
    pass


class ProductTemplateDownloadsExport(BaseSchema):
    pass


class ProductTemplateExportFilterRequestSchema(BaseSchema):
    pass


class ProductTemplateExportResponseSchema(BaseSchema):
    pass


class ProductVariants(BaseSchema):
    pass


class CompanyVerificationStats(BaseSchema):
    pass


class CompanyVerificationResponseSchema(BaseSchema):
    pass


class ProductVariantsResponseSchema(BaseSchema):
    pass


class Properties(BaseSchema):
    pass


class Quantities(BaseSchema):
    pass


class QuantitiesArticle(BaseSchema):
    pass


class Quantity(BaseSchema):
    pass


class QuantityBase(BaseSchema):
    pass


class ReturnConfig(BaseSchema):
    pass


class InventoryReturnConfig(BaseSchema):
    pass


class ReturnConfig2(BaseSchema):
    pass


class Sitemap(BaseSchema):
    pass


class PageQuery(BaseSchema):
    pass


class ApplicationCollectionItemSeoPage(BaseSchema):
    pass


class ApplicationCollectionItemSeoAction(BaseSchema):
    pass


class ApplicationCollectionItemSeoBreadcrumbs(BaseSchema):
    pass


class ApplicationItemSeoAction(BaseSchema):
    pass


class ApplicationItemSeoBreadcrumbs(BaseSchema):
    pass


class ApplicationItemSeoMetaTagItem(BaseSchema):
    pass


class ApplicationItemSeoMetaTags(BaseSchema):
    pass


class Metatags(BaseSchema):
    pass


class SizePromotionThreshold(BaseSchema):
    pass


class SEOData(BaseSchema):
    pass


class SearchKeywordResult(BaseSchema):
    pass


class SearchableAttribute(BaseSchema):
    pass


class SecondLevelChild(BaseSchema):
    pass


class SellerPhoneNumber(BaseSchema):
    pass


class CollectionSeoDetail(BaseSchema):
    pass


class SeoDetail(BaseSchema):
    pass


class SetSize(BaseSchema):
    pass


class SingleCategoryResponseSchema(BaseSchema):
    pass


class VariantTypesResponseSchema(BaseSchema):
    pass


class VariantTypeItem(BaseSchema):
    pass


class SingleProductResponseSchema(BaseSchema):
    pass


class Size(BaseSchema):
    pass


class SizeDistribution(BaseSchema):
    pass


class SizeGuideItem(BaseSchema):
    pass


class SizeGuideResponseSchema(BaseSchema):
    pass


class Time(BaseSchema):
    pass


class Timing(BaseSchema):
    pass


class UserSchemaCustom(BaseSchema):
    pass


class Manager(BaseSchema):
    pass


class MobileNo(BaseSchema):
    pass


class IntegrationType(BaseSchema):
    pass


class Address(BaseSchema):
    pass


class StoreDetail(BaseSchema):
    pass


class StoreMeta(BaseSchema):
    pass


class SuccessResponseSchema(BaseSchema):
    pass


class TaxIdentifier(BaseSchema):
    pass


class TaxSlab(BaseSchema):
    pass


class TeaserTag(BaseSchema):
    pass


class TemplateDetails(BaseSchema):
    pass


class TemplateGlobalValidationData(BaseSchema):
    pass


class TemplateValidationData(BaseSchema):
    pass


class TemplatesResponseSchema(BaseSchema):
    pass


class TemplatesGlobalValidationResponseSchema(BaseSchema):
    pass


class ThirdLevelChild(BaseSchema):
    pass


class Trader(BaseSchema):
    pass


class Trader1(BaseSchema):
    pass


class UpdateCollection(BaseSchema):
    pass


class UpdateSearchConfigurationRequestSchema(BaseSchema):
    pass


class UpdateSearchConfigurationResponseSchema(BaseSchema):
    pass


class UpdatedResponseSchema(BaseSchema):
    pass


class UserCommon(BaseSchema):
    pass


class UserDetail(BaseSchema):
    pass


class UserDetail1(BaseSchema):
    pass


class UserInfo(BaseSchema):
    pass


class UserSchema(BaseSchema):
    pass


class ValidateIdentifier(BaseSchema):
    pass


class ValidateProduct(BaseSchema):
    pass


class ValidateSizeGuide(BaseSchema):
    pass


class VerifiedBy(BaseSchema):
    pass


class WeightResponseSchema(BaseSchema):
    pass


class WeightResponseSchema1(BaseSchema):
    pass


class Marketplaces(BaseSchema):
    pass


class GetAllMarketplaces(BaseSchema):
    pass


class CreateMarketplaceOptinRequestSchema(BaseSchema):
    pass


class UpdateMarketplaceOptinRequestSchema(BaseSchema):
    pass


class CreateMarketplaceOptinResponseSchema(BaseSchema):
    pass


class GetProductTemplateSlugItemsSchema(BaseSchema):
    pass


class GetProductTemplateSlugResponseSchema(BaseSchema):
    pass


class UpdateMarketplaceOptinResponseSchema(BaseSchema):
    pass


class AutocompleteRequestSchema(BaseSchema):
    pass


class AutocompleteUpsertResponseSchema(BaseSchema):
    pass


class AutocompleteErrorResponseSchemaSchema(BaseSchema):
    pass


class AutocompleteResponseSchema(BaseSchema):
    pass


class ProductListingActionPage(BaseSchema):
    pass


class ProductListingAction(BaseSchema):
    pass


class AutocompleteItem(BaseSchema):
    pass


class AutocompletePreviewResponseSchema(BaseSchema):
    pass


class CreateAppPriceFactoryRequestSchema(BaseSchema):
    pass


class CreateAppPriceFactoryResponseSchema(BaseSchema):
    pass


class AppPriceFactory(BaseSchema):
    pass


class EditAppPriceFactoryRequestSchema(BaseSchema):
    pass


class GetAppPriceFactoryResponseSchema(BaseSchema):
    pass


class CreateAppPriceFactoryProduct(BaseSchema):
    pass


class PriceFactorySizes(BaseSchema):
    pass


class CompanySizes(BaseSchema):
    pass


class CreateAppPriceFactoryProductItem(BaseSchema):
    pass


class CreatePriceFactoryProductRequestSchema(BaseSchema):
    pass


class CreateAppPriceFactoryProductResponseSchema(BaseSchema):
    pass


class FailedRecordsData(BaseSchema):
    pass


class CreatePriceFactoryProductResponseSchema(BaseSchema):
    pass


class CreateAppPriceFactoryProductsResponseSchema(BaseSchema):
    pass


class CreateAppPriceFactoryProductBulkJobRequestSchema(BaseSchema):
    pass


class CreateAppPriceFactoryProductExportJobRequestSchema(BaseSchema):
    pass


class CreateAppPriceFactoryProductExportJobResponseSchema(BaseSchema):
    pass


class AppPriceFactoryProductExportPollJobResponseSchema(BaseSchema):
    pass


class CreateAppPriceFactoryProductExportJobPollResponseSchema(BaseSchema):
    pass


class CreateAppPriceFactoryProductBulkJobResponseSchema(BaseSchema):
    pass


class CreateAppPriceFactoryProductBulkJobValidateResponseSchema(BaseSchema):
    pass


class CreateAppPriceFactoryProductBulkJobPollResponseSchema(BaseSchema):
    pass


class SynonymListResponseSchema(BaseSchema):
    pass


class SynonymResponseSchema(BaseSchema):
    pass


class SynonymListErrorResponseSchemaSchema(BaseSchema):
    pass


class SynonymCreateRequestSchema(BaseSchema):
    pass


class SynonymCreateResponseSchema(BaseSchema):
    pass


class SynonymUpdateResponseSchema(BaseSchema):
    pass


class SynonymCreateErrorSchema(BaseSchema):
    pass


class SynonymDeleteResponseSchemaSchema(BaseSchema):
    pass


class SynonymUploadRequestSchema(BaseSchema):
    pass


class SynonymUploadResponseSchema(BaseSchema):
    pass


class SynonymExportResponseSchema(BaseSchema):
    pass


class SynonymUploadErrorSchema(BaseSchema):
    pass


class SynonymBulkValidateRequestSchema(BaseSchema):
    pass


class SynonymBulkValidateResponseSchema(BaseSchema):
    pass


class SynonymBulkValidateErrorSchema(BaseSchema):
    pass


class SynonymBulkProcessRequestSchema(BaseSchema):
    pass


class SynonymBulkProcessResponseSchema(BaseSchema):
    pass


class SynonymBulkProcessErrorSchema(BaseSchema):
    pass


class SynonymBulkPollResponseSchema(BaseSchema):
    pass


class SynonymBulkPollErrorSchema(BaseSchema):
    pass


class PriceFactoryCreateErrorSchema(BaseSchema):
    pass


class PriceGroupedByZone(BaseSchema):
    pass


class AppPriceByIdResponseSchema(BaseSchema):
    pass


class TemplatesValidationResponseSchema(BaseSchema):
    pass


class ActionPage(BaseSchema):
    pass


class Price1(BaseSchema):
    pass


class MultiCategoriesSchema(BaseSchema):
    pass


class CustomMeta(BaseSchema):
    pass


class ValidationErrors(BaseSchema):
    pass


class ValidationError(BaseSchema):
    pass





class StoreTagsResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    tags = fields.List(fields.Str(required=False), required=False)
    
    success = fields.Boolean(required=False)
    


class DiscountMeta(BaseSchema):
    # Catalog swagger.json

    
    start = fields.Str(required=False)
    
    end = fields.Str(required=False)
    
    timer = fields.Boolean(required=False)
    


class ProductMinMaxPrice(BaseSchema):
    # Catalog swagger.json

    
    min = fields.Float(required=False)
    
    max = fields.Float(required=False)
    


class ProductPrice(BaseSchema):
    # Catalog swagger.json

    
    selling = fields.Nested(ProductMinMaxPrice, required=False)
    
    effective = fields.Nested(ProductMinMaxPrice, required=False)
    
    marked = fields.Nested(ProductMinMaxPrice, required=False)
    
    currency = fields.Str(required=False)
    


class ProductPricesPage(BaseSchema):
    # Catalog swagger.json

    
    type = fields.Str(required=False)
    
    current = fields.Float(required=False)
    
    size = fields.Float(required=False)
    
    item_total = fields.Float(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    has_next = fields.Boolean(required=False)
    


class ProductPriceItem(BaseSchema):
    # Catalog swagger.json

    
    discount_meta = fields.Nested(DiscountMeta, required=False)
    
    product_name = fields.Str(required=False)
    
    item_id = fields.Float(required=False)
    
    factory_type_id = fields.Str(required=False)
    
    price = fields.Nested(ProductPrice, required=False)
    
    store_id = fields.Float(required=False)
    
    is_sellable = fields.Boolean(required=False)
    
    seller_id = fields.Float(required=False)
    
    delivery_zone_ids = fields.List(fields.Str(required=False), required=False)
    
    sizes = fields.List(fields.Str(required=False), required=False)
    


class ProductPrices(BaseSchema):
    # Catalog swagger.json

    
    data = fields.List(fields.Nested(ProductPriceItem, required=False), required=False)
    
    page = fields.Nested(ProductPricesPage, required=False)
    


class ProductFiltersKeysOnly(BaseSchema):
    # Catalog swagger.json

    
    key = fields.Nested(ProductFiltersKey, required=False)
    


class GetQueryFiltersKeysResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    filters = fields.List(fields.Nested(ProductFiltersKeysOnly, required=False), required=False)
    
    operators = fields.Dict(required=False)
    
    sort_on = fields.List(fields.Nested(ProductSortOn, required=False), required=False)
    


class GetQueryFiltersValuesResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    values = fields.List(fields.Nested(ProductQueryFiltersValue, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class ProductQueryFiltersValue(BaseSchema):
    # Catalog swagger.json

    
    display = fields.Str(required=False)
    
    count = fields.Int(required=False)
    
    is_selected = fields.Boolean(required=False)
    
    value = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    


class CompanyDRIListResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(CompanyDRIResponseSchema, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class CompanyDRIResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    tags = fields.List(fields.Str(required=False), required=False)
    
    responsibilities = fields.List(fields.Str(required=False), required=False)
    
    responsibilities_display_name = fields.List(fields.Str(required=False), required=False)
    
    uid = fields.Int(required=False)
    
    company_id = fields.Int(required=False)
    
    status = fields.Boolean(required=False)
    
    contact = fields.Dict(required=False)
    
    contact_details = fields.Dict(required=False)
    


class SearchResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    _id = fields.Str(required=False)
    
    query = fields.Nested(MerchandisingQuery, required=False)
    
    is_active = fields.Boolean(required=False)
    
    merchandising_rule_id = fields.Str(required=False)
    
    rule_name = fields.Str(required=False)
    
    application_id = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    zone_id = fields.Str(required=False)
    
    _schedule = fields.Dict(required=False)
    


class MerchandisingQuery(BaseSchema):
    # Catalog swagger.json

    
    query_condition = fields.Str(required=False)
    
    query = fields.Nested(MerchandisingSearchQuery, required=False)
    
    filter = fields.List(fields.Nested(MerchandisingFilter, required=False), required=False)
    


class MerchandisingSearchQuery(BaseSchema):
    # Catalog swagger.json

    
    condition = fields.Str(required=False)
    
    search_query = fields.Str(required=False)
    
    synonyms = fields.Str(required=False)
    


class MerchandisingFilter(BaseSchema):
    # Catalog swagger.json

    
    attribute = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class MerchandisingRuleQuery(BaseSchema):
    # Catalog swagger.json

    
    condition = fields.Str(required=False)
    
    search_query = fields.Str(required=False)
    
    synonyms = fields.Boolean(required=False)
    


class MerchandisingRulesList(BaseSchema):
    # Catalog swagger.json

    
    data = fields.List(fields.Nested(MerchDataItem, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class MerchDataItem(BaseSchema):
    # Catalog swagger.json

    
    query = fields.Nested(MerchSearchQuery, required=False)
    
    action = fields.List(fields.Str(required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    merchandising_rule_id = fields.Str(required=False)
    
    rule_name = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    zone_id = fields.Str(required=False)
    
    application_id = fields.Str(required=False)
    


class MerchSearchQuery(BaseSchema):
    # Catalog swagger.json

    
    query_condition = fields.Str(required=False)
    
    query = fields.Nested(MerchQueryCondition, required=False)
    
    filter = fields.List(fields.Nested(MerchFilter, required=False), required=False)
    


class MerchQueryCondition(BaseSchema):
    # Catalog swagger.json

    
    condition = fields.Str(required=False)
    
    search_query = fields.Str(required=False)
    
    synonyms = fields.Str(required=False)
    


class MerchFilter(BaseSchema):
    # Catalog swagger.json

    
    attribute = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class SuccessResponseMerchandising(BaseSchema):
    # Catalog swagger.json

    
    message = fields.Str(required=False)
    


class MerchandiseQueryResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    message = fields.Str(required=False)
    
    merchandising_rule_id = fields.Str(required=False)
    


class Filter(BaseSchema):
    # Catalog swagger.json

    
    attribute = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class MerchandisingRuleQueryPart(BaseSchema):
    # Catalog swagger.json

    
    filter = fields.List(fields.Nested(Filter, required=False), required=False)
    
    query_condition = fields.Str(required=False)
    
    query = fields.Nested(MerchandisingRuleQuery, required=False)
    


class MerchandisingRuleQueryPost(BaseSchema):
    # Catalog swagger.json

    
    query = fields.Nested(MerchandisingRuleQueryPart, required=False)
    
    zone_id = fields.Str(required=False)
    


class MerchandisingRuleSave(BaseSchema):
    # Catalog swagger.json

    
    rule_name = fields.Str(required=False)
    
    _schedule = fields.Nested(CollectionSchedule, required=False)
    
    is_active = fields.Boolean(required=False)
    


class PinItem(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    position = fields.Int(required=False)
    


class PinItemRequestSchema(BaseSchema):
    # Catalog swagger.json

    
    action = fields.Str(required=False)
    
    item_id = fields.Str(required=False)
    
    position = fields.Int(required=False)
    


class PinRequestSchema(BaseSchema):
    # Catalog swagger.json

    
    action_value = fields.List(fields.Nested(PinItemRequestSchema, required=False), required=False)
    


class PinResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    data = fields.List(fields.Nested(PinItem, required=False), required=False)
    


class HideAttribute(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    


class HideAttributeRequestSchema(BaseSchema):
    # Catalog swagger.json

    
    action = fields.Str(required=False)
    
    item_id = fields.Int(required=False)
    


class HideResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    data = fields.List(fields.Nested(HideAttribute, required=False), required=False)
    


class HideRequestSchema(BaseSchema):
    # Catalog swagger.json

    
    action_value = fields.List(fields.Nested(HideAttributeRequestSchema, required=False), required=False)
    


class PostBoostAttribute(BaseSchema):
    # Catalog swagger.json

    
    attribute = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    strength = fields.Int(required=False)
    
    action = fields.Str(required=False)
    


class BoostAttribute(BaseSchema):
    # Catalog swagger.json

    
    attribute = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    strength = fields.Int(required=False)
    


class GetMerchandisingRuleBoostAction(BaseSchema):
    # Catalog swagger.json

    
    data = fields.List(fields.Nested(BoostAttribute, required=False), required=False)
    


class PostMerchandisingRuleBoostAction(BaseSchema):
    # Catalog swagger.json

    
    action_value = fields.List(fields.Nested(PostBoostAttribute, required=False), required=False)
    


class GetMerchandisingRuleBuryAction(BaseSchema):
    # Catalog swagger.json

    
    data = fields.List(fields.Nested(BoostAttribute, required=False), required=False)
    


class Action(BaseSchema):
    # Catalog swagger.json

    
    type = fields.Str(required=False)
    
    page = fields.Nested(ActionPage, required=False)
    
    popup = fields.Nested(ActionPage, required=False)
    


class AllSizes(BaseSchema):
    # Catalog swagger.json

    
    identifiers = fields.List(fields.Nested(ValidateIdentifier, required=False), required=False)
    
    item_dimensions_unit_of_measure = fields.Str(required=False)
    
    item_height = fields.Float(required=False)
    
    item_length = fields.Float(required=False)
    
    item_weight = fields.Float(required=False)
    
    item_weight_unit_of_measure = fields.Str(required=False)
    
    item_width = fields.Float(required=False)
    
    size = fields.Str(required=False)
    


class AllowSingleRequestSchema(BaseSchema):
    # Catalog swagger.json

    
    allow_single = fields.Boolean(required=False)
    


class AppCatalogConfiguration(BaseSchema):
    # Catalog swagger.json

    
    app_id = fields.Str(required=False)
    
    config_id = fields.Str(required=False)
    
    config_type = fields.Str(required=False)
    
    created_by = fields.Dict(required=False)
    
    created_on = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    listing = fields.Nested(ConfigurationListing, required=False)
    
    modified_by = fields.Dict(required=False)
    
    modified_on = fields.Str(required=False)
    
    product = fields.Nested(ConfigurationProduct, required=False)
    
    type = fields.Str(required=False)
    


class AppCategoryReturnConfig(BaseSchema):
    # Catalog swagger.json

    
    category_id = fields.Int(required=False)
    
    return_config = fields.Nested(ProductReturnConfigBaseSchema, required=False)
    


class ReturnConfigResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    returnable = fields.Boolean(required=False)
    
    time = fields.Int(required=False)
    
    unit = fields.Str(required=False)
    


class AppCategoryReturnConfigResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    app_id = fields.Str(required=False)
    
    category_id = fields.Int(required=False)
    
    logo = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    return_config = fields.Nested(ProductReturnConfigBaseSchema, required=False)
    


class AppConfiguration(BaseSchema):
    # Catalog swagger.json

    
    app_id = fields.Str(required=False)
    
    config_id = fields.Str(required=False)
    
    config_type = fields.Str(required=False)
    
    created_by = fields.Dict(required=False)
    
    created_on = fields.Str(required=False)
    
    listing = fields.Nested(ConfigurationListing, required=False)
    
    modified_by = fields.Dict(required=False)
    
    modified_on = fields.Str(required=False)
    
    product = fields.Nested(ConfigurationProduct, required=False)
    
    type = fields.Str(required=False)
    


class AppConfigurationCreateDetail(BaseSchema):
    # Catalog swagger.json

    
    app_id = fields.Str(required=False)
    
    attributes = fields.List(fields.Nested(AttributeDetailsGroup, required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    is_default = fields.Boolean(required=False)
    
    logo = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    
    slug = fields.Str(required=False)
    
    template_slugs = fields.List(fields.Str(required=False), required=False)
    


class AppConfigurationDetail(BaseSchema):
    # Catalog swagger.json

    
    app_id = fields.Str(required=False)
    
    attributes = fields.List(fields.Nested(AttributeDetailsGroup, required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    is_default = fields.Boolean(required=False)
    
    logo = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    
    slug = fields.Str(required=False)
    
    template_slugs = fields.List(fields.Str(required=False), required=False)
    


class ValueConfigType(BaseSchema):
    # Catalog swagger.json

    
    bucket_points = fields.List(fields.Dict(required=False), required=False)
    
    map = fields.Dict(required=False)
    
    sort = fields.Str(required=False)
    
    condition = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class AppConfigurationsFilter(BaseSchema):
    # Catalog swagger.json

    
    app_id = fields.Str(required=False)
    
    allow_single = fields.Boolean(required=False)
    
    attribute_name = fields.Str(required=False)
    
    value_config = fields.Nested(ValueConfigType, required=False)
    
    type = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    is_default = fields.Boolean(required=False)
    
    key = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    


class AppConfigurationsFilterResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    id = fields.Str(required=False)
    
    app_id = fields.Str(required=False)
    
    allow_single = fields.Boolean(required=False)
    
    attribute_name = fields.Str(required=False)
    
    value_config = fields.Nested(ValueConfigType, required=False)
    
    type = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    is_default = fields.Boolean(required=False)
    
    key = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    


class ApplicationBrandJson(BaseSchema):
    # Catalog swagger.json

    
    _custom_json = fields.Dict(required=False)
    


class ApplicationCategoryJson(BaseSchema):
    # Catalog swagger.json

    
    _custom_json = fields.Dict(required=False)
    


class ApplicationDepartment(BaseSchema):
    # Catalog swagger.json

    
    _custom_json = fields.Dict(required=False)
    
    app_id = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    logo = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    


class ApplicationDepartmentJson(BaseSchema):
    # Catalog swagger.json

    
    _custom_json = fields.Dict(required=False)
    


class ApplicationDepartmentListingResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(ApplicationDepartment, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class ApplicationItemMOQ(BaseSchema):
    # Catalog swagger.json

    
    increment_unit = fields.Int(required=False)
    
    maximum = fields.Int(required=False)
    
    minimum = fields.Int(required=False)
    


class ApplicationItemMeta(BaseSchema):
    # Catalog swagger.json

    
    _custom_json = fields.Dict(required=False)
    
    _custom_meta = fields.List(fields.Nested(MetaFields, required=False), required=False)
    
    alt_text = fields.Dict(required=False)
    
    is_cod = fields.Boolean(required=False)
    
    is_gift = fields.Boolean(required=False)
    
    moq = fields.Nested(ApplicationItemMOQ, required=False)
    
    seo = fields.Nested(ApplicationItemSEO, required=False)
    
    size_promotion_threshold = fields.Nested(SizePromotionThreshold, required=False)
    


class ApplicationItemSeoSitemap(BaseSchema):
    # Catalog swagger.json

    
    priority = fields.Float(required=False)
    
    frequency = fields.Str(required=False)
    


class ApplicationItemSEO(BaseSchema):
    # Catalog swagger.json

    
    description = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    sitemap = fields.Nested(ApplicationItemSeoSitemap, required=False)
    
    breadcrumbs = fields.List(fields.Nested(ApplicationItemSeoBreadcrumbs, required=False), required=False)
    
    meta_tags = fields.List(fields.Nested(ApplicationItemSeoMetaTags, required=False), required=False)
    
    canonical_url = fields.Str(required=False)
    


class ApplicationProductsSchema(BaseSchema):
    # Catalog swagger.json

    
    attributes = fields.Dict(required=False)
    
    brand = fields.Nested(ProductBrand, required=False)
    
    color = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    discount = fields.Str(required=False)
    
    has_variant = fields.Boolean(required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    image_nature = fields.Str(required=False)
    
    item_code = fields.Str(required=False)
    
    item_type = fields.Str(required=False)
    
    medias = fields.List(fields.Nested(Media, required=False), required=False)
    
    name = fields.Str(required=False)
    
    price = fields.Nested(ProductListingPrice, required=False)
    
    product_online_date = fields.Str(required=False)
    
    promo_meta = fields.Dict(required=False)
    
    rating = fields.Float(required=False)
    
    rating_count = fields.Int(required=False)
    
    sellable = fields.Boolean(required=False)
    
    short_description = fields.Str(required=False)
    
    similars = fields.List(fields.Str(required=False), required=False)
    
    slug = fields.Str(required=False)
    
    teaser_tag = fields.Dict(required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    popularity = fields.Int(required=False)
    
    brand_uid = fields.Int(required=False)
    
    category_uid = fields.Int(required=False)
    
    verification_status = fields.Int(required=False)
    
    channel_identifier = fields.Str(required=False)
    
    category_slug = fields.Str(required=False)
    
    size_guide = fields.Str(required=False)
    
    l3_categories = fields.List(fields.Int(required=False), required=False)
    
    store_ids = fields.List(fields.Int(required=False), required=False)
    
    company_ids = fields.List(fields.Int(required=False), required=False)
    
    departments = fields.List(fields.Int(required=False), required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    l3_category_names = fields.List(fields.Str(required=False), required=False)
    
    sizes = fields.List(fields.Str(required=False), required=False)
    
    product_group_tag = fields.List(fields.Str(required=False), required=False)
    
    multi_size = fields.Boolean(required=False)
    
    is_gift = fields.Boolean(required=False)
    
    is_cod = fields.Boolean(required=False)
    
    is_dependent = fields.Boolean(required=False)
    
    is_available = fields.Boolean(required=False)
    
    moq = fields.Nested(ApplicationItemMOQ, required=False)
    
    seo = fields.Nested(ApplicationItemSEO, required=False)
    
    variants = fields.Dict(required=False)
    
    variant_media = fields.Dict(required=False)
    
    variant_group = fields.Dict(required=False)
    
    multi_categories = fields.List(fields.Nested(MultiCategoriesSchema, required=False), required=False)
    
    template_tag = fields.Str(required=False)
    
    net_quantity = fields.Dict(required=False)
    
    custom_order = fields.Nested(CustomOrder, required=False)
    
    country_of_origin = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    identifiers = fields.List(fields.Str(required=False), required=False)
    
    item_id = fields.Int(required=False)
    
    _custom_meta = fields.List(fields.Nested(CustomMeta, required=False), required=False)
    
    discount_percentage = fields.Int(required=False)
    


class ApplicationProductListingResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    filters = fields.List(fields.Nested(ProductFilters, required=False), required=False)
    
    items = fields.List(fields.Nested(ApplicationProductsSchema, required=False), required=False)
    
    operators = fields.Nested(OperatorsResponseSchema, required=False)
    
    page = fields.Nested(Page, required=False)
    
    sort_on = fields.List(fields.Nested(ProductSortOn, required=False), required=False)
    


class OperatorsResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    btw = fields.Str(required=False)
    
    lte = fields.Str(required=False)
    
    gte = fields.Str(required=False)
    
    gt = fields.Str(required=False)
    
    lt = fields.Str(required=False)
    
    nin = fields.Str(required=False)
    


class ApplicationStoreJson(BaseSchema):
    # Catalog swagger.json

    
    _custom_json = fields.Dict(required=False)
    


class AppReturnConfigResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    created_by = fields.Nested(UserInfo, required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    app_id = fields.Str(required=False)
    
    category_count = fields.Int(required=False)
    
    company_id = fields.Int(required=False)
    
    modified_on = fields.Str(required=False)
    
    return_config_level = fields.Str(required=False)
    


class ArticleStoreResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    store_code = fields.Str(required=False)
    
    store_type = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    


class AttributeDetailsGroup(BaseSchema):
    # Catalog swagger.json

    
    display_type = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    key = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    
    slug = fields.Str(required=False)
    
    unit = fields.Str(required=False)
    


class AttributeMaster(BaseSchema):
    # Catalog swagger.json

    
    allowed_values = fields.List(fields.Str(required=False), required=False)
    
    format = fields.Str(required=False)
    
    mandatory = fields.Boolean(required=False)
    
    multi = fields.Boolean(required=False)
    
    range = fields.Nested(AttributeSchemaRange, required=False)
    
    type = fields.Str(required=False)
    


class AttributeMasterDetails(BaseSchema):
    # Catalog swagger.json

    
    display_type = fields.Str(required=False)
    


class AttributeMasterFilter(BaseSchema):
    # Catalog swagger.json

    
    ddepends_on = fields.List(fields.Str(required=False), required=False)
    
    indexing = fields.Boolean(required=False)
    
    priority = fields.Int(required=False)
    


class AttributeMasterMandatoryDetails(BaseSchema):
    # Catalog swagger.json

    
    l3_keys = fields.List(fields.Str(required=False), required=False)
    


class AttributeMasterMeta(BaseSchema):
    # Catalog swagger.json

    
    enriched = fields.Boolean(required=False)
    
    mandatory_details = fields.Nested(AttributeMasterMandatoryDetails, required=False)
    


class AttributeMasterSchema(BaseSchema):
    # Catalog swagger.json

    
    created_by = fields.Dict(required=False)
    
    created_on = fields.Str(required=False)
    
    departments = fields.List(fields.Str(required=False), required=False)
    
    description = fields.Str(required=False)
    
    details = fields.Nested(AttributeMasterDetails, required=False)
    
    enabled_for_end_consumer = fields.Boolean(required=False)
    
    filters = fields.Nested(AttributeMasterFilter, required=False)
    
    is_nested = fields.Boolean(required=False)
    
    logo = fields.Str(required=False)
    
    modified_by = fields.Dict(required=False)
    
    modified_on = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    raw_key = fields.Str(required=False)
    
    schema = fields.Nested(AttributeMaster, required=False)
    
    suggestion = fields.Str(required=False)
    
    synonyms = fields.Dict(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    unit = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    variant = fields.Boolean(required=False)
    


class AttributeSchemaRange(BaseSchema):
    # Catalog swagger.json

    
    min = fields.Int(required=False)
    
    max = fields.Int(required=False)
    


class AutoCompleteMedia(BaseSchema):
    # Catalog swagger.json

    
    aspect_ratio = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    url = fields.Str(required=False)
    


class AutocompleteAction(BaseSchema):
    # Catalog swagger.json

    
    page = fields.Nested(AutocompletePageAction, required=False)
    
    type = fields.Str(required=False)
    


class AutocompletePageAction(BaseSchema):
    # Catalog swagger.json

    
    params = fields.Dict(required=False)
    
    query = fields.Dict(required=False)
    
    type = fields.Str(required=False)
    
    url = fields.Str(required=False)
    


class AutocompleteResult(BaseSchema):
    # Catalog swagger.json

    
    _custom_json = fields.Dict(required=False)
    
    action = fields.Nested(AutocompleteAction, required=False)
    
    display = fields.Str(required=False)
    
    logo = fields.Nested(AutoCompleteMedia, required=False)
    


class BannerImage(BaseSchema):
    # Catalog swagger.json

    
    aspect_ratio = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    url = fields.Str(required=False)
    


class BaseAppCategoryReturnConfig(BaseSchema):
    # Catalog swagger.json

    
    data = fields.List(fields.Nested(AppCategoryReturnConfig, required=False), required=False)
    


class BaseAppCategoryReturnConfigResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    data = fields.List(fields.Nested(AppCategoryReturnConfigResponseSchema, required=False), required=False)
    
    page = fields.Nested(PageResponseSchema, required=False)
    


class Brand(BaseSchema):
    # Catalog swagger.json

    
    logo = fields.Nested(Logo, required=False)
    
    name = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    


class BrandLogo(BaseSchema):
    # Catalog swagger.json

    
    url = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class BrandItem(BaseSchema):
    # Catalog swagger.json

    
    action = fields.Nested(Action, required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    departments = fields.List(fields.Int(required=False), required=False)
    
    discount = fields.Str(required=False)
    
    logo = fields.Nested(BrandLogo, required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    


class ApplicationCategoryListingSchema(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(ApplicationCategoryListingItemSchema, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class ApplicationCategoryListingItemSchema(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    departments = fields.List(fields.Int(required=False), required=False)
    
    attr_name = fields.Str(required=False)
    
    landscape_url = fields.Str(required=False)
    
    portrait_url = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    priority = fields.Int(required=False)
    
    created_by = fields.Nested(UserInfo, required=False)
    
    created_on = fields.Str(required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    modified_on = fields.Str(required=False)
    
    app_id = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    uid = fields.Int(required=False)
    


class ApplicationBrandListingSchema(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(ApplicationBrandListingItemSchema, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class ApplicationBrandListingItemSchema(BaseSchema):
    # Catalog swagger.json

    
    _custom_json = fields.Dict(required=False)
    
    _locale_language = fields.Dict(required=False)
    
    brand_banner_portrait_url = fields.Str(required=False)
    
    brand_banner_url = fields.Str(required=False)
    
    brand_logo_url = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    slug_key = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    
    uid = fields.Int(required=False)
    
    created_on = fields.Str(required=False)
    
    last_updated = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    departments = fields.List(fields.Int(required=False), required=False)
    


class BrandListingResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(BrandItem, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
    modified_on = fields.Str(required=False)
    


class BrandMeta(BaseSchema):
    # Catalog swagger.json

    
    id = fields.Int(required=False)
    
    name = fields.Str(required=False)
    


class BrandMeta1(BaseSchema):
    # Catalog swagger.json

    
    id = fields.Int(required=False)
    
    name = fields.Str(required=False)
    


class BulkAssetResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(Items, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class BulkInventoryGet(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(BulkInventoryGetItems, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class BulkInventoryGetItems(BaseSchema):
    # Catalog swagger.json

    
    cancelled = fields.Int(required=False)
    
    cancelled_records = fields.List(fields.Str(required=False), required=False)
    
    company_id = fields.Int(required=False)
    
    created_by = fields.Dict(required=False)
    
    created_on = fields.Str(required=False)
    
    failed = fields.Int(required=False)
    
    failed_records = fields.List(fields.Str(required=False), required=False)
    
    file_path = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    modified_by = fields.Dict(required=False)
    
    modified_on = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    succeed = fields.Int(required=False)
    
    total = fields.Int(required=False)
    


class BulkProductUploadJob(BaseSchema):
    # Catalog swagger.json

    
    company_id = fields.Int(required=False)
    
    total = fields.Int(required=False)
    
    succeed = fields.Int(required=False)
    
    stage = fields.Str(required=False)
    
    file_path = fields.Str(required=False)
    
    template_tag = fields.Str(required=False)
    
    tracking_url = fields.Str(required=False)
    


class BulkProductJob(BaseSchema):
    # Catalog swagger.json

    
    company_id = fields.Int(required=False)
    
    template_tag = fields.Str(required=False)
    
    product_type = fields.Str(required=False)
    
    department = fields.Str(required=False)
    
    file_path = fields.Str(required=False)
    


class BulkProductRequestSchema(BaseSchema):
    # Catalog swagger.json

    
    batch_id = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    data = fields.List(fields.Dict(required=False), required=False)
    
    template_tag = fields.Str(required=False)
    


class CatalogInsightBrand(BaseSchema):
    # Catalog swagger.json

    
    article_freshness = fields.Int(required=False)
    
    available_articles = fields.Int(required=False)
    
    available_sizes = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    total_articles = fields.Int(required=False)
    
    total_sizes = fields.Int(required=False)
    


class CatalogInsightItem(BaseSchema):
    # Catalog swagger.json

    
    count = fields.Int(required=False)
    
    out_of_stock_count = fields.Int(required=False)
    
    sellable_count = fields.Int(required=False)
    


class CatalogInsightResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    brand_distribution = fields.Nested(CatalogInsightBrand, required=False)
    
    item = fields.Nested(CatalogInsightItem, required=False)
    


class CategoriesResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    slug_key = fields.Str(required=False)
    
    template_slug = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    


class Category(BaseSchema):
    # Catalog swagger.json

    
    created_by = fields.Dict(required=False)
    
    created_on = fields.Str(required=False)
    
    departments = fields.List(fields.Int(required=False), required=False)
    
    hierarchy = fields.List(fields.Nested(Hierarchy, required=False), required=False)
    
    id = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    level = fields.Int(required=False)
    
    marketplaces = fields.Nested(CategoryMapping, required=False)
    
    media = fields.Nested(Media1, required=False)
    
    modified_by = fields.Dict(required=False)
    
    modified_on = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    
    slug = fields.Str(required=False)
    
    synonyms = fields.List(fields.Str(required=False), required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    uid = fields.Int(required=False)
    


class CategoryItems(BaseSchema):
    # Catalog swagger.json

    
    _custom_json = fields.Dict(required=False, allow_none=True)
    
    action = fields.Nested(Action, required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    childs = fields.List(fields.Nested(Child, required=False), required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    


class CategoryListingResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    data = fields.List(fields.Nested(DepartmentCategoryTree, required=False), required=False)
    
    departments = fields.List(fields.Nested(DepartmentIdentifier, required=False), required=False)
    


class CategoryMapping(BaseSchema):
    # Catalog swagger.json

    
    ajio = fields.Nested(CategoryMappingValues, required=False)
    
    facebook = fields.Nested(CategoryMappingValues, required=False)
    
    google = fields.Nested(CategoryMappingValues, required=False)
    


class CategoryMappingValues(BaseSchema):
    # Catalog swagger.json

    
    catalog_id = fields.Int(required=False)
    
    name = fields.Str(required=False)
    


class CategoryResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(Category, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class Child(BaseSchema):
    # Catalog swagger.json

    
    _custom_json = fields.Dict(required=False)
    
    action = fields.Nested(Action, required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    childs = fields.List(fields.Nested(SecondLevelChild, required=False), required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    


class CollectionBadge(BaseSchema):
    # Catalog swagger.json

    
    color = fields.Str(required=False)
    
    text = fields.Str(required=False)
    


class CollectionBanner(BaseSchema):
    # Catalog swagger.json

    
    landscape = fields.Nested(CollectionImage, required=False)
    
    portrait = fields.Nested(CollectionImage, required=False)
    


class CollectionBannerResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    landscape = fields.Nested(CollectionImageResponseSchema, required=False)
    
    portrait = fields.Nested(CollectionImageResponseSchema, required=False)
    


class CollectionCreateResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    badge = fields.Nested(CollectionBadge, required=False)
    
    banners = fields.Nested(CollectionBannerResponseSchema, required=False)
    
    cron = fields.Dict(required=False)
    
    description = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    logo = fields.Nested(CollectionImageResponseSchema, required=False)
    
    meta = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    
    is_searchable = fields.Boolean(required=False)
    
    priority = fields.Int(required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
    seo = fields.Nested(SeoDetail, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    _locale_language = fields.Dict(required=False)
    
    _schedule = fields.Nested(CollectionSchedule, required=False)
    
    action = fields.Nested(Action, required=False)
    
    uid = fields.Str(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    app_id = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    sort_on = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    


class CollectionImage(BaseSchema):
    # Catalog swagger.json

    
    aspect_ratio = fields.Str(required=False)
    
    url = fields.Str(required=False)
    
    secure_url = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class CollectionImageResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    type = fields.Str(required=False)
    
    url = fields.Str(required=False)
    


class CollectionListingFilter(BaseSchema):
    # Catalog swagger.json

    
    tags = fields.List(fields.Nested(CollectionListingFilterTag, required=False), required=False)
    
    type = fields.List(fields.Nested(CollectionListingFilterType, required=False), required=False)
    


class CollectionListingFilterTag(BaseSchema):
    # Catalog swagger.json

    
    display = fields.Str(required=False)
    
    is_selected = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    


class CollectionListingFilterType(BaseSchema):
    # Catalog swagger.json

    
    display = fields.Str(required=False)
    
    is_selected = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    


class CollectionQuery(BaseSchema):
    # Catalog swagger.json

    
    attribute = fields.Str(required=False)
    
    op = fields.Str(required=False)
    
    value = fields.List(fields.Str(required=False), required=False)
    


class CollectionSchedule(BaseSchema):
    # Catalog swagger.json

    
    cron = fields.Str(required=False, allow_none=True)
    
    duration = fields.Int(required=False, allow_none=True)
    
    end = fields.Str(required=False, allow_none=True)
    
    next_schedule = fields.List(fields.Nested(NextSchedule, required=False), required=False)
    
    start = fields.Str(required=False)
    


class CompanyBrandDetail(BaseSchema):
    # Catalog swagger.json

    
    brand_id = fields.Int(required=False)
    
    brand_name = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    total_article = fields.Int(required=False)
    
    logo = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    
    id = fields.Int(required=False)
    


class CompanyMeta(BaseSchema):
    # Catalog swagger.json

    
    id = fields.Int(required=False)
    


class CompanyMeta1(BaseSchema):
    # Catalog swagger.json

    
    id = fields.Int(required=False)
    


class ConfigErrorResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    code = fields.Str(required=False)
    
    errors = fields.Dict(required=False)
    
    message = fields.Str(required=False)
    


class ConfigSuccessResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    message = fields.Str(required=False)
    


class ConfigurationBucketPoints(BaseSchema):
    # Catalog swagger.json

    
    display = fields.Str(required=False)
    
    end = fields.Float(required=False)
    
    start = fields.Float(required=False)
    


class ConfigurationListing(BaseSchema):
    # Catalog swagger.json

    
    filter = fields.Nested(ConfigurationListingFilter, required=False)
    
    sort = fields.Nested(ConfigurationListingSort, required=False)
    


class ConfigurationListingFilter(BaseSchema):
    # Catalog swagger.json

    
    allow_single = fields.Boolean(required=False)
    
    attribute_config = fields.List(fields.Nested(ConfigurationListingFilterConfig, required=False), required=False)
    


class ConfigurationListingFilterConfig(BaseSchema):
    # Catalog swagger.json

    
    display_name = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    key = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    value_config = fields.Nested(ConfigurationListingFilterValue, required=False)
    


class ConfigurationListingFilterValue(BaseSchema):
    # Catalog swagger.json

    
    bucket_points = fields.List(fields.Nested(ConfigurationBucketPoints, required=False), required=False)
    
    condition = fields.Str(required=False)
    
    map = fields.Dict(required=False)
    
    map_values = fields.List(fields.Dict(required=False), required=False)
    
    priority = fields.List(fields.Str(required=False), required=False)
    
    sort = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class ConfigurationListingSort(BaseSchema):
    # Catalog swagger.json

    
    config = fields.List(fields.Nested(ConfigurationListingSortConfig, required=False), required=False)
    
    default_key = fields.Str(required=False)
    


class ConfigurationListingSortConfig(BaseSchema):
    # Catalog swagger.json

    
    is_active = fields.Boolean(required=False)
    
    key = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    


class ConfigurationProduct(BaseSchema):
    # Catalog swagger.json

    
    similar = fields.Nested(ConfigurationProductSimilar, required=False)
    
    variant = fields.Nested(ConfigurationProductVariant, required=False)
    
    details_groups = fields.Nested(ConfigurationProductDetailsGroups, required=False)
    


class ConfigurationProductDetailsGroups(BaseSchema):
    # Catalog swagger.json

    
    config = fields.List(fields.Nested(ConfigurationProductDetailsConfig, required=False), required=False)
    


class ConfigurationProductDetailsConfig(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    
    template_slugs = fields.List(fields.Str(required=False), required=False)
    
    attributes = fields.List(fields.Nested(ConfigurationProductDetailsAttribute, required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    


class ConfigurationProductDetailsAttribute(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    display_type = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    key = fields.Str(required=False)
    


class ConfigurationProductConfig(BaseSchema):
    # Catalog swagger.json

    
    is_active = fields.Boolean(required=False)
    
    key = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    
    size = fields.Nested(ProductSize, required=False)
    
    subtitle = fields.Str(required=False)
    
    title = fields.Str(required=False)
    


class ConfigurationProductSimilar(BaseSchema):
    # Catalog swagger.json

    
    config = fields.List(fields.Nested(ConfigurationProductConfig, required=False), required=False)
    


class ConfigurationProductVariant(BaseSchema):
    # Catalog swagger.json

    
    config = fields.List(fields.Nested(ConfigurationProductVariantConfig, required=False), required=False)
    


class ConfigurationProductVariantConfig(BaseSchema):
    # Catalog swagger.json

    
    display_type = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    key = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    
    size = fields.Nested(ProductSize, required=False)
    


class CreateAutocompleteKeyword(BaseSchema):
    # Catalog swagger.json

    
    _custom_json = fields.Dict(required=False)
    
    app_id = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    results = fields.List(fields.Nested(AutocompleteResult, required=False), required=False)
    
    words = fields.List(fields.Str(required=False), required=False)
    
    action = fields.Nested(AutocompleteAction, required=False)
    


class CreateAutocompleteWordsResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    results = fields.List(fields.Nested(AutocompleteResult, required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    app_id = fields.Str(required=False)
    
    words = fields.List(fields.Str(required=False), required=False)
    


class CreateCollection(BaseSchema):
    # Catalog swagger.json

    
    _custom_json = fields.Dict(required=False)
    
    _locale_language = fields.Dict(required=False)
    
    _schedule = fields.Nested(CollectionSchedule, required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    app_id = fields.Str(required=False)
    
    badge = fields.Nested(CollectionBadge, required=False)
    
    banners = fields.Nested(CollectionBanner, required=False)
    
    created_by = fields.Nested(UserInfo, required=False)
    
    description = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    is_visible = fields.Boolean(required=False)
    
    logo = fields.Nested(CollectionImage, required=False)
    
    meta = fields.Dict(required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    name = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    
    published = fields.Boolean(required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
    seo = fields.Nested(SeoDetail, required=False)
    
    slug = fields.Str(required=False)
    
    is_searchable = fields.Boolean(required=False)
    
    sort_on = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    


class RerankingBoostItems(BaseSchema):
    # Catalog swagger.json

    
    boost = fields.List(fields.Nested(BoostItem, required=False), required=False)
    


class GetSearchRerankDetailResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    ranking = fields.Nested(RerankingBoostItems, required=False)
    
    is_active = fields.Boolean(required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    created_by = fields.Nested(UserInfo, required=False)
    
    words = fields.List(fields.Str(required=False), required=False)
    
    app_id = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    id = fields.Str(required=False)
    


class BoostItem(BaseSchema):
    # Catalog swagger.json

    
    attribute_key = fields.Str(required=False)
    
    attribute_value = fields.Str(required=False)
    


class GetSearchRerankItemResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    words = fields.List(fields.Str(required=False), required=False)
    
    app_id = fields.Str(required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    ranking = fields.Nested(RerankingBoostItems, required=False)
    
    created_by = fields.Nested(UserInfo, required=False)
    
    is_active = fields.Boolean(required=False)
    
    id = fields.Str(required=False)
    


class GetSearchRerankResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(GetSearchRerankItemResponseSchema, required=False), required=False)
    
    page = fields.Nested(PageResponseSchema, required=False)
    


class CreateSearchRerankResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    words = fields.List(fields.Str(required=False), required=False)
    
    app_id = fields.Str(required=False)
    
    ranking = fields.Nested(RerankingBoostItems, required=False)
    
    is_active = fields.Boolean(required=False)
    
    created_on = fields.Str(required=False)
    
    created_by = fields.Nested(UserInfo, required=False)
    
    modified_on = fields.Str(required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    


class UpdateSearchRerankResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    words = fields.List(fields.Str(required=False), required=False)
    
    app_id = fields.Str(required=False)
    
    ranking = fields.Nested(RerankingBoostItems, required=False)
    
    is_active = fields.Boolean(required=False)
    
    created_on = fields.Str(required=False)
    
    created_by = fields.Nested(UserInfo, required=False)
    
    modified_on = fields.Str(required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    


class UpdateSearchRerankRequestSchema(BaseSchema):
    # Catalog swagger.json

    
    words = fields.List(fields.Str(required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    application_id = fields.Str(required=False)
    
    ranking = fields.Nested(RerankingBoostItems, required=False)
    


class CreateSearchRerankRequestSchema(BaseSchema):
    # Catalog swagger.json

    
    words = fields.List(fields.Str(required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    application_id = fields.Str(required=False)
    
    ranking = fields.Nested(RerankingBoostItems, required=False)
    


class CreateSearchConfigurationRequestSchema(BaseSchema):
    # Catalog swagger.json

    
    application_id = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    created_by = fields.Nested(UserSchema, required=False)
    
    created_on = fields.Str(required=False)
    
    is_proximity_enabled = fields.Boolean(required=False)
    
    modified_by = fields.Nested(UserSchema, required=False)
    
    modified_on = fields.Str(required=False)
    
    proximity = fields.Int(required=False)
    
    searchable_attributes = fields.List(fields.Nested(SearchableAttribute, required=False), required=False)
    


class CreateSearchConfigurationResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    success = fields.Boolean(required=False)
    


class CreateSearchKeyword(BaseSchema):
    # Catalog swagger.json

    
    _custom_json = fields.Dict(required=False)
    
    app_id = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    result = fields.Nested(SearchKeywordResult, required=False)
    
    words = fields.List(fields.Str(required=False), required=False)
    


class CreateUpdateAppReturnConfig(BaseSchema):
    # Catalog swagger.json

    
    app_id = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    return_config_level = fields.Str(required=False)
    


class CrossSellingResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    articles = fields.Int(required=False)
    
    products = fields.Int(required=False)
    


class CustomOrder(BaseSchema):
    # Catalog swagger.json

    
    manufacturing_time_unit = fields.Str(required=False)
    
    is_custom_order = fields.Boolean(required=False)
    
    manufacturing_time = fields.Int(required=False)
    


class DateMeta(BaseSchema):
    # Catalog swagger.json

    
    added_on_store = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    inventory_updated_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    


class DefaultKeyRequestSchema(BaseSchema):
    # Catalog swagger.json

    
    default_key = fields.Str(required=False)
    


class DeleteAppCategoryReturnConfig(BaseSchema):
    # Catalog swagger.json

    
    category_ids = fields.List(fields.Int(required=False), required=False)
    


class DeleteResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    message = fields.Str(required=False)
    


class DeleteSearchConfigurationResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    success = fields.Boolean(required=False)
    


class DeleteSearchRerankConfigurationResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class Department(BaseSchema):
    # Catalog swagger.json

    
    logo = fields.Nested(DepartmentMedia, required=False)
    
    name = fields.Str(required=False)
    
    priority_order = fields.Int(required=False)
    
    slug = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    


class DepartmentCategoryTree(BaseSchema):
    # Catalog swagger.json

    
    department = fields.Str(required=False)
    
    items = fields.List(fields.Nested(CategoryItems, required=False), required=False)
    


class DepartmentIdentifier(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    


class DepartmentResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(Department, required=False), required=False)
    


class ValidationFailedResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    message = fields.Str(required=False)
    


class DepartmentsResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(GetDepartment, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class DimensionResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    height = fields.Float(required=False)
    
    is_default = fields.Boolean(required=False)
    
    length = fields.Float(required=False)
    
    unit = fields.Str(required=False)
    
    width = fields.Float(required=False)
    


class InventoryDimensionResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    height = fields.Float(required=False)
    
    length = fields.Float(required=False)
    
    unit = fields.Str(required=False)
    
    width = fields.Float(required=False)
    


class Document(BaseSchema):
    # Catalog swagger.json

    
    legal_name = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    url = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    verified = fields.Boolean(required=False)
    


class EntityConfiguration(BaseSchema):
    # Catalog swagger.json

    
    app_id = fields.Str(required=False)
    
    config_id = fields.Str(required=False)
    
    config_type = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    listing = fields.Nested(GetCatalogConfigurationDetailsSchemaListing, required=False)
    
    product = fields.Nested(GetCatalogConfigurationDetailsProduct, required=False)
    


class ErrorResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    code = fields.Float(required=False)
    
    error = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    status = fields.Int(required=False)
    


class CategoryErrorResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    code = fields.Str(required=False)
    
    error = fields.Dict(required=False)
    
    message = fields.Str(required=False)
    


class FilerList(BaseSchema):
    # Catalog swagger.json

    
    display = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class RawProduct(BaseSchema):
    # Catalog swagger.json

    
    _custom_json = fields.Dict(required=False)
    
    all_company_ids = fields.List(fields.Int(required=False), required=False)
    
    all_identifiers = fields.List(fields.Str(required=False), required=False)
    
    all_sizes = fields.List(fields.Dict(required=False), required=False)
    
    attributes = fields.Dict(required=False)
    
    brand = fields.Nested(Brand, required=False)
    
    brand_uid = fields.Int(required=False)
    
    category = fields.Dict(required=False)
    
    category_slug = fields.Str(required=False)
    
    category_uid = fields.Int(required=False)
    
    company_id = fields.Int(required=False)
    
    country_of_origin = fields.Str(required=False)
    
    created_by = fields.Dict(required=False)
    
    created_on = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    custom_order = fields.Dict(required=False)
    
    departments = fields.List(fields.Int(required=False), required=False)
    
    description = fields.Str(required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    hsn_code = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    image_nature = fields.Str(required=False)
    
    images = fields.List(fields.Str(required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    is_dependent = fields.Boolean(required=False)
    
    is_expirable = fields.Boolean(required=False)
    
    is_image_less_product = fields.Boolean(required=False)
    
    is_physical = fields.Boolean(required=False)
    
    is_set = fields.Boolean(required=False)
    
    item_code = fields.Str(required=False)
    
    item_type = fields.Str(required=False)
    
    l3_mapping = fields.List(fields.Str(required=False), required=False)
    
    media = fields.List(fields.Nested(Media, required=False), required=False)
    
    modified_by = fields.Dict(required=False)
    
    modified_on = fields.Str(required=False)
    
    moq = fields.Dict(required=False)
    
    multi_size = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    net_quantity = fields.Nested(NetQuantityResponseSchema, required=False)
    
    no_of_boxes = fields.Int(required=False)
    
    pending = fields.Str(required=False)
    
    primary_color = fields.Str(required=False)
    
    product_group_tag = fields.List(fields.Str(required=False), required=False)
    
    product_publish = fields.Nested(ProductPublished, required=False)
    
    return_config = fields.Nested(ReturnConfigResponseSchema, required=False)
    
    short_description = fields.Str(required=False)
    
    size_guide = fields.Str(required=False)
    
    sizes = fields.List(fields.Dict(required=False), required=False)
    
    slug = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    tax_identifier = fields.Nested(TaxIdentifier, required=False)
    
    teaser_tag = fields.Dict(required=False)
    
    template_tag = fields.Str(required=False)
    
    trader = fields.List(fields.Nested(Trader, required=False), required=False)
    
    uid = fields.Int(required=False)
    
    variant_group = fields.Dict(required=False)
    
    variant_media = fields.Dict(required=False)
    
    variants = fields.Dict(required=False)
    
    verified_by = fields.Nested(VerifiedBy, required=False)
    
    verified_on = fields.Str(required=False)
    
    store_id_list = fields.List(fields.Str(required=False), required=False)
    
    action = fields.Str(required=False)
    


class RawProductListingResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(RawProduct, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class GTIN(BaseSchema):
    # Catalog swagger.json

    
    gtin_type = fields.Str(required=False)
    
    gtin_value = fields.Str(required=False)
    
    primary = fields.Boolean(required=False)
    


class AttributeDetail(BaseSchema):
    # Catalog swagger.json

    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    created_by = fields.Nested(UserInfo, required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    departments = fields.List(fields.Str(required=False), required=False)
    
    description = fields.Str(required=False)
    
    details = fields.Nested(AttributeMasterDetails, required=False)
    
    enabled_for_end_consumer = fields.Boolean(required=False)
    
    filters = fields.Nested(AttributeMasterFilter, required=False)
    
    _id = fields.Str(required=False)
    
    is_nested = fields.Boolean(required=False)
    
    logo = fields.Str(required=False)
    
    meta = fields.Nested(AttributeMasterMeta, required=False)
    
    name = fields.Str(required=False)
    
    schema = fields.Nested(AttributeMaster, required=False)
    
    slug = fields.Str(required=False)
    
    variant = fields.Boolean(required=False)
    


class GetAddressSchema(BaseSchema):
    # Catalog swagger.json

    
    address1 = fields.Str(required=False)
    
    address2 = fields.Str(required=False)
    
    address_type = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    landmark = fields.Str(required=False)
    
    latitude = fields.Float(required=False)
    
    longitude = fields.Float(required=False)
    
    pincode = fields.Int(required=False)
    
    state = fields.Str(required=False)
    


class GetAllSizes(BaseSchema):
    # Catalog swagger.json

    
    all_sizes = fields.List(fields.Nested(AllSizes, required=False), required=False)
    


class FilterResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    values = fields.List(fields.Nested(ValueItem, required=False), required=False)
    


class ValueItem(BaseSchema):
    # Catalog swagger.json

    
    text = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class GetAppCatalogConfiguration(BaseSchema):
    # Catalog swagger.json

    
    data = fields.Nested(AppCatalogConfiguration, required=False)
    
    is_default = fields.Boolean(required=False)
    


class GetAppCatalogEntityConfiguration(BaseSchema):
    # Catalog swagger.json

    
    data = fields.Nested(EntityConfiguration, required=False)
    
    is_default = fields.Boolean(required=False)
    


class GetAutocompleteWordsData(BaseSchema):
    # Catalog swagger.json

    
    results = fields.List(fields.Nested(AutocompleteResult, required=False), required=False)
    
    app_id = fields.Str(required=False)
    
    words = fields.List(fields.Str(required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    uid = fields.Str(required=False)
    


class GetAutocompleteWordsResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(GetAutocompleteWordsData, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class GetCatalogConfigurationDetailsProduct(BaseSchema):
    # Catalog swagger.json

    
    compare = fields.Nested(CompareFilter, required=False)
    
    similar = fields.Nested(SimilarFilter, required=False)
    
    variant = fields.Nested(VariantFilter, required=False)
    
    detail = fields.Nested(DetailFilter, required=False)
    


class FilterItem(BaseSchema):
    # Catalog swagger.json

    
    key = fields.Str(required=False)
    
    display = fields.Str(required=False)
    
    filter_types = fields.List(fields.Str(required=False), required=False)
    
    units = fields.List(fields.Str(required=False), required=False)
    


class CompareFilter(BaseSchema):
    # Catalog swagger.json

    
    data = fields.List(fields.Nested(FilterItem, required=False), required=False)
    


class SimilarFilter(BaseSchema):
    # Catalog swagger.json

    
    data = fields.List(fields.Nested(SimilarItem, required=False), required=False)
    


class VariantFilter(BaseSchema):
    # Catalog swagger.json

    
    data = fields.List(fields.Nested(VariantItem, required=False), required=False)
    


class DetailFilter(BaseSchema):
    # Catalog swagger.json

    
    data = fields.List(fields.Nested(FilterItem, required=False), required=False)
    
    values = fields.Nested(DetailFilterValues, required=False)
    


class DetailFilterValues(BaseSchema):
    # Catalog swagger.json

    
    display_type = fields.List(fields.Nested(DisplayType, required=False), required=False)
    


class DisplayType(BaseSchema):
    # Catalog swagger.json

    
    key = fields.Str(required=False)
    
    display = fields.Str(required=False)
    


class SimilarItem(BaseSchema):
    # Catalog swagger.json

    
    key = fields.Str(required=False)
    
    display = fields.Str(required=False)
    


class VariantItem(BaseSchema):
    # Catalog swagger.json

    
    key = fields.Str(required=False)
    
    display = fields.Str(required=False)
    


class GetCatalogConfigurationDetailsSchemaListing(BaseSchema):
    # Catalog swagger.json

    
    filter = fields.Dict(required=False)
    
    sort = fields.Dict(required=False)
    


class GetCatalogConfigurationMetaData(BaseSchema):
    # Catalog swagger.json

    
    listing = fields.Nested(MetaDataListingResponseSchema, required=False)
    
    product = fields.Nested(GetCatalogConfigurationDetailsProduct, required=False)
    


class GetCollectionDetailNest(BaseSchema):
    # Catalog swagger.json

    
    _schedule = fields.Nested(CollectionSchedule, required=False)
    
    action = fields.Nested(Action, required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    app_id = fields.Str(required=False)
    
    badge = fields.Dict(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    cron = fields.Dict(required=False)
    
    description = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    logo = fields.Nested(Media, required=False)
    
    meta = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
    slug = fields.Str(required=False)
    
    tag = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    


class GetCollectionListingResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    filters = fields.Nested(CollectionListingFilter, required=False)
    
    items = fields.List(fields.Nested(GetCollectionDetailNest, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class GetCompanySchema(BaseSchema):
    # Catalog swagger.json

    
    addresses = fields.List(fields.Nested(GetAddressSchema, required=False), required=False)
    
    business_type = fields.Str(required=False)
    
    company_type = fields.Str(required=False)
    
    created_by = fields.Nested(UserSchema, required=False)
    
    created_on = fields.Str(required=False)
    
    modified_by = fields.Nested(UserSchema, required=False)
    
    modified_on = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    reject_reason = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    verified_by = fields.Nested(UserSchema, required=False)
    
    verified_on = fields.Str(required=False)
    


class ConditionItem(BaseSchema):
    # Catalog swagger.json

    
    key = fields.Str(required=False)
    
    display = fields.Str(required=False)
    


class DataItem(BaseSchema):
    # Catalog swagger.json

    
    key = fields.Str(required=False)
    
    display = fields.Str(required=False)
    
    filter_types = fields.List(fields.Str(required=False), required=False)
    
    compatible_units = fields.List(fields.Str(required=False), required=False)
    


class ValueTypeItem(BaseSchema):
    # Catalog swagger.json

    
    key = fields.Str(required=False)
    
    display = fields.Str(required=False)
    


class SortTypeItem(BaseSchema):
    # Catalog swagger.json

    
    key = fields.Str(required=False)
    
    display = fields.Str(required=False)
    


class GetConfigMetadataResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    page = fields.Nested(Page, required=False)
    
    condition = fields.List(fields.Nested(ConditionItem, required=False), required=False)
    
    data = fields.List(fields.Nested(DataItem, required=False), required=False)
    
    values = fields.Nested(GetConfigMetadataValues, required=False)
    


class GetConfigMetadataValues(BaseSchema):
    # Catalog swagger.json

    
    type = fields.List(fields.Nested(ValueTypeItem, required=False), required=False)
    
    sort = fields.List(fields.Nested(SortTypeItem, required=False), required=False)
    


class AttributeType(BaseSchema):
    # Catalog swagger.json

    
    unit = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
    display_type = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    slug = fields.Str(required=False)
    


class DataType(BaseSchema):
    # Catalog swagger.json

    
    app_id = fields.Str(required=False)
    
    is_default = fields.Boolean(required=False)
    
    priority = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    attributes = fields.List(fields.Nested(AttributeType, required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    slug = fields.Str(required=False)
    
    id = fields.Str(required=False)
    


class ListingValueConfigType(BaseSchema):
    # Catalog swagger.json

    
    sort = fields.Str(required=False)
    
    bucket_points = fields.List(fields.Dict(required=False), required=False)
    
    map = fields.Dict(required=False)
    
    condition = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class SizeLimitConfiguration(BaseSchema):
    # Catalog swagger.json

    
    min = fields.Float(required=False)
    
    max = fields.Float(required=False)
    


class ListingDataType(BaseSchema):
    # Catalog swagger.json

    
    app_id = fields.Str(required=False)
    
    allow_single = fields.Boolean(required=False)
    
    id = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    key = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    is_default = fields.Boolean(required=False)
    
    priority = fields.Int(required=False)
    
    logo = fields.Str(required=False)
    
    value_config = fields.Nested(ListingValueConfigType, required=False)
    
    type = fields.Str(required=False)
    
    display_type = fields.Str(required=False)
    
    size = fields.Nested(SizeLimitConfiguration, required=False)
    


class GetListingConfigResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    data = fields.List(fields.Nested(ListingDataType, required=False), required=False)
    
    page = fields.Nested(PageResponseType, required=False)
    


class GetConfigResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    data = fields.List(fields.Nested(ConfigItem, required=False), required=False)
    
    page = fields.Nested(PageResponseType, required=False)
    


class ConfigItem(BaseSchema):
    # Catalog swagger.json

    
    app_id = fields.Str(required=False)
    
    attributes = fields.List(fields.Nested(AttributeConfig, required=False), required=False)
    
    id = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    is_default = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    
    slug = fields.Str(required=False)
    
    template_slugs = fields.List(fields.Str(required=False), required=False)
    
    seo = fields.Nested(ApplicationItemSEO, required=False)
    


class AttributeConfig(BaseSchema):
    # Catalog swagger.json

    
    display_type = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    key = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    
    slug = fields.Str(required=False)
    


class GetDepartment(BaseSchema):
    # Catalog swagger.json

    
    created_by = fields.Nested(UserSchema, required=False)
    
    created_on = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    item_type = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    modified_by = fields.Nested(UserSchema, required=False)
    
    modified_on = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    synonyms = fields.List(fields.Str(required=False), required=False)
    
    priority_order = fields.Int(required=False)
    
    uid = fields.Int(required=False)
    


class GetInventories(BaseSchema):
    # Catalog swagger.json

    
    brand = fields.Nested(BrandMeta1, required=False)
    
    company = fields.Nested(CompanyMeta1, required=False)
    
    country_of_origin = fields.Str(required=False)
    
    created_by = fields.Nested(UserSchema, required=False)
    
    date_meta = fields.Nested(DateMeta, required=False)
    
    dimension = fields.Nested(InventoryDimensionResponseSchema, required=False)
    
    expiration_date = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    identifier = fields.Nested(Identifier, required=False)
    
    inventory_updated_on = fields.Str(required=False)
    
    is_set = fields.Boolean(required=False)
    
    item_id = fields.Int(required=False)
    
    manufacturer = fields.Nested(InventoryManufacturerResponseSchema, required=False)
    
    modified_by = fields.Nested(UserSchema, required=False)
    
    platforms = fields.Dict(required=False)
    
    price = fields.Nested(PriceArticle, required=False)
    
    quantities = fields.Nested(QuantitiesArticle, required=False)
    
    return_config = fields.Nested(ReturnConfig2, required=False)
    
    seller_identifier = fields.Str(required=False)
    
    size = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    store = fields.Nested(ArticleStoreResponseSchema, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    tax_identifier = fields.Nested(TaxIdentifier, required=False)
    
    total_quantity = fields.Int(required=False)
    
    trace_id = fields.Str(required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    trader = fields.List(fields.Nested(TraderResponseSchema, required=False), required=False)
    
    uid = fields.Str(required=False)
    
    weight = fields.Nested(InventoryWeightResponseSchema, required=False)
    


class InventoryWeightResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    shipping = fields.Float(required=False)
    
    unit = fields.Str(required=False)
    


class TraderResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    address = fields.List(fields.Str(required=False), required=False)
    
    name = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class Identifier(BaseSchema):
    # Catalog swagger.json

    
    primary = fields.Boolean(required=False)
    
    gtin_value = fields.Str(required=False)
    
    gtin_type = fields.Str(required=False)
    


class GetInventoriesResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(GetInventories, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class GetLocationSchema(BaseSchema):
    # Catalog swagger.json

    
    _custom_json = fields.Dict(required=False)
    
    address = fields.Nested(GetAddressSchema, required=False)
    
    store_code = fields.Str(required=False)
    
    company = fields.Nested(GetCompanySchema, required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    created_by = fields.Nested(UserSchema, required=False)
    
    created_on = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    gst_credentials = fields.Nested(InvoiceDetailsSchema, required=False)
    
    integration_type = fields.Nested(LocationIntegrationType, required=False)
    
    manager = fields.Nested(LocationManagerSchema, required=False)
    
    modified_by = fields.Nested(UserSchema, required=False)
    
    modified_on = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    phone_number = fields.Str(required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigSchema, required=False)
    
    stage = fields.Str(required=False)
    
    store_type = fields.Str(required=False)
    
    timing = fields.List(fields.Nested(LocationDayWiseSchema, required=False), required=False)
    
    uid = fields.Int(required=False)
    
    verified_by = fields.Nested(UserSchema, required=False)
    
    verified_on = fields.Str(required=False)
    
    warnings = fields.Dict(required=False)
    
    company_id = fields.Int(required=False)
    


class GetProductBundleCreateResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    created_by = fields.Nested(UserSchema, required=False)
    
    modified_by = fields.Nested(UserSchema, required=False)
    
    choice = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    created_on = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    logo = fields.Str(required=False, allow_none=True)
    
    meta = fields.Dict(required=False)
    
    modified_on = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    page_visibility = fields.List(fields.Str(required=False), required=False)
    
    products = fields.List(fields.Nested(ProductBundleItem, required=False), required=False)
    
    same_store_assignment = fields.Boolean(required=False)
    
    slug = fields.Str(required=False)
    
    allow_remove = fields.Boolean(required=False)
    
    auto_add_to_cart = fields.Boolean(required=False)
    
    auto_select = fields.Boolean(required=False)
    
    prefer_single_shipment = fields.Boolean(required=False)
    
    allow_individual_cancel = fields.Boolean(required=False)
    
    allow_individual_return = fields.Boolean(required=False)
    


class GetProductBundleListingResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(GetProductBundleCreateResponseSchema, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class GetProductBundleResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    choice = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    logo = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    
    page_visibility = fields.List(fields.Str(required=False), required=False)
    
    products = fields.List(fields.Nested(GetProducts, required=False), required=False)
    
    same_store_assignment = fields.Boolean(required=False)
    
    slug = fields.Str(required=False)
    
    allow_remove = fields.Boolean(required=False)
    
    auto_add_to_cart = fields.Boolean(required=False)
    
    auto_select = fields.Boolean(required=False)
    
    prefer_single_shipment = fields.Boolean(required=False)
    
    allow_individual_cancel = fields.Boolean(required=False)
    
    allow_individual_return = fields.Boolean(required=False)
    


class GetProducts(BaseSchema):
    # Catalog swagger.json

    
    max_quantity = fields.Int(required=False)
    
    min_quantity = fields.Int(required=False)
    
    price = fields.Nested(Price, required=False)
    
    product_details = fields.Nested(LimitedProductData, required=False)
    
    product_uid = fields.Int(required=False)
    
    sizes = fields.List(fields.Nested(Size, required=False), required=False)
    


class GetCollectionDetailResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    _custom_json = fields.Dict(required=False)
    
    _locale_language = fields.Dict(required=False)
    
    _schedule = fields.Nested(CollectionSchedule, required=False)
    
    action = fields.Dict(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    app_id = fields.Str(required=False)
    
    badge = fields.Nested(CollectionBadge, required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    cron = fields.Dict(required=False)
    
    description = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    is_visible = fields.Boolean(required=False)
    
    logo = fields.Nested(Media, required=False)
    
    meta = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    
    published = fields.Boolean(required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
    seo = fields.Nested(SeoDetail, required=False)
    
    slug = fields.Str(required=False)
    
    sort_on = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    


class CommonResponseSchemaCollection(BaseSchema):
    # Catalog swagger.json

    
    message = fields.Str(required=False)
    


class GetQueryFiltersResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    filters = fields.List(fields.Nested(CollectionProductFilters, required=False), required=False)
    
    operators = fields.Dict(required=False)
    
    sort_on = fields.List(fields.Nested(CollectionProductSortOn, required=False), required=False)
    


class CollectionProductSortOn(BaseSchema):
    # Catalog swagger.json

    
    is_selected = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    


class CollectionProductFilters(BaseSchema):
    # Catalog swagger.json

    
    key = fields.Nested(ProductFiltersKey, required=False)
    
    values = fields.List(fields.Nested(CollectionProductFiltersValue, required=False), required=False)
    


class CollectionProductFiltersValue(BaseSchema):
    # Catalog swagger.json

    
    display = fields.Str(required=False)
    
    count = fields.Int(required=False)
    
    is_selected = fields.Boolean(required=False)
    
    value = fields.Str(required=False)
    
    logo = fields.Dict(required=False)
    


class GetCollectionItemsResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(ApplicationProductsSchema, required=False), required=False)
    
    sort_on = fields.List(fields.Nested(ProductSortOn, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class CollectionItemSchemaV2(BaseSchema):
    # Catalog swagger.json

    
    action = fields.Str(required=False)
    
    item_id = fields.Int(required=False)
    
    priority = fields.Int(required=False)
    


class CollectionItemUpdateSchema(BaseSchema):
    # Catalog swagger.json

    
    allow_facets = fields.Boolean(required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    items = fields.List(fields.Nested(CollectionItemSchemaV2, required=False), required=False)
    
    query = fields.List(fields.Nested(CollectionQuerySchemaV2, required=False), required=False)
    
    type = fields.Str(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    


class CollectionQuerySchemaV2(BaseSchema):
    # Catalog swagger.json

    
    attribute = fields.Str(required=False)
    
    op = fields.Str(required=False)
    
    value = fields.List(fields.Str(required=False), required=False)
    


class GetSearchConfigurationResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    _id = fields.Str(required=False)
    
    application_id = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    created_by = fields.Nested(UserSchema, required=False)
    
    created_on = fields.Str(required=False)
    
    is_proximity_enabled = fields.Boolean(required=False)
    
    modified_by = fields.Nested(UserSchema, required=False)
    
    modified_on = fields.Str(required=False)
    
    proximity = fields.Int(required=False)
    
    searchable_attributes = fields.List(fields.Nested(SearchableAttribute, required=False), required=False)
    


class GetSearchWordsData(BaseSchema):
    # Catalog swagger.json

    
    query = fields.Dict(required=False)
    
    sort_on = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    app_id = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    result = fields.Dict(required=False)
    
    uid = fields.Str(required=False)
    
    words = fields.List(fields.Str(required=False), required=False)
    


class GetSearchWordsResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(GetSearchWordsData, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class GlobalValidation(BaseSchema):
    # Catalog swagger.json

    
    definitions = fields.Dict(required=False)
    
    description = fields.Str(required=False)
    
    properties = fields.Nested(Properties, required=False)
    
    required = fields.List(fields.Str(required=False), required=False)
    
    title = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class Guide(BaseSchema):
    # Catalog swagger.json

    
    meta = fields.Nested(Meta, required=False)
    


class HSNCodesResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    data = fields.Nested(HSNData, required=False)
    
    message = fields.Str(required=False)
    


class HSNData(BaseSchema):
    # Catalog swagger.json

    
    country_of_origin = fields.List(fields.Str(required=False), required=False)
    
    hsn_code = fields.List(fields.Str(required=False), required=False)
    


class HSNDataInsertV2(BaseSchema):
    # Catalog swagger.json

    
    country_code = fields.Str(required=False)
    
    created_by = fields.Nested(UserInfo, required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    created_on = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    hsn_code = fields.Str(required=False)
    
    hsn_code_id = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    reporting_hsn = fields.Raw(required=False)
    
    id = fields.Str(required=False)
    
    taxes = fields.List(fields.Nested(TaxSlab, required=False), required=False)
    
    type = fields.Str(required=False)
    


class Hierarchy(BaseSchema):
    # Catalog swagger.json

    
    department = fields.Int(required=False)
    
    l1 = fields.Int(required=False)
    
    l2 = fields.Int(required=False)
    


class HsnCodesListingResponseSchemaV2(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(HSNDataInsertV2, required=False), required=False)
    
    page = fields.Nested(PageResponseSchema, required=False)
    


class Image(BaseSchema):
    # Catalog swagger.json

    
    aspect_ratio = fields.Str(required=False)
    
    aspect_ratio_f = fields.Float(required=False)
    
    secure_url = fields.Str(required=False)
    
    url = fields.Str(required=False)
    


class ImageUrls(BaseSchema):
    # Catalog swagger.json

    
    landscape = fields.Nested(BannerImage, required=False)
    
    portrait = fields.Nested(BannerImage, required=False)
    


class InventoryBulkRequestSchema(BaseSchema):
    # Catalog swagger.json

    
    batch_id = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    sizes = fields.List(fields.Nested(InventoryJobPayload, required=False), required=False)
    
    user = fields.Dict(required=False)
    


class InventoryConfig(BaseSchema):
    # Catalog swagger.json

    
    data = fields.List(fields.Nested(FilerList, required=False), required=False)
    
    multivalue = fields.Boolean(required=False)
    


class InventoryCreateRequestSchema(BaseSchema):
    # Catalog swagger.json

    
    data = fields.List(fields.Str(required=False), required=False)
    
    filters = fields.Nested(InventoryExportFilter, required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    


class InventoryExportFilter(BaseSchema):
    # Catalog swagger.json

    
    brand_ids = fields.List(fields.Int(required=False), required=False)
    
    from_date = fields.Str(required=False)
    
    quantity = fields.Nested(InventoryExportQuantityFilter, required=False)
    
    store_ids = fields.List(fields.Int(required=False), required=False)
    
    to_date = fields.Str(required=False)
    


class InventoryExportJobResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(InventoryExportItem, required=False), required=False)
    


class InventoryExportItem(BaseSchema):
    # Catalog swagger.json

    
    status = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    stats = fields.Dict(required=False)
    
    completed_on = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    seller_id = fields.Int(required=False)
    
    task_id = fields.Str(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    created_by = fields.Nested(UserInfo, required=False)
    
    _id = fields.Str(required=False)
    
    url = fields.Str(required=False)
    
    trigger_on = fields.Str(required=False)
    
    brand = fields.List(fields.Int(required=False), required=False)
    
    store = fields.List(fields.Int(required=False), required=False)
    


class InventoryExportJobListFilters(BaseSchema):
    # Catalog swagger.json

    
    brand_ids = fields.List(fields.Int(required=False), required=False)
    
    store_ids = fields.List(fields.Int(required=False), required=False)
    
    brands = fields.List(fields.Str(required=False), required=False)
    
    stores = fields.List(fields.Str(required=False), required=False)
    


class InventoryExportJobListStats(BaseSchema):
    # Catalog swagger.json

    
    success = fields.Int(required=False)
    
    total = fields.Int(required=False)
    


class InventoryExportJobList(BaseSchema):
    # Catalog swagger.json

    
    status = fields.Str(required=False)
    
    completed_on = fields.Str(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    filters = fields.Nested(InventoryExportJobListFilters, required=False)
    
    stats = fields.Nested(InventoryExportJobListStats, required=False)
    
    type = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    seller_id = fields.Int(required=False)
    
    url = fields.Str(required=False)
    
    task_id = fields.Str(required=False)
    
    created_by = fields.Nested(UserInfo, required=False)
    
    id = fields.Str(required=False)
    


class InventoryExportJobListResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(InventoryExportJobList, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class InventoryExportQuantityFilter(BaseSchema):
    # Catalog swagger.json

    
    max = fields.Int(required=False)
    
    min = fields.Int(required=False)
    
    operators = fields.Str(required=False)
    


class ExportPatchRequestSchema(BaseSchema):
    # Catalog swagger.json

    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    status = fields.Str(required=False)
    


class InventoryExportRequestSchema(BaseSchema):
    # Catalog swagger.json

    
    brand = fields.List(fields.Int(required=False), required=False)
    
    store = fields.List(fields.Int(required=False), required=False)
    
    type = fields.Str(required=False)
    


class EditInventoryDataDownloadsResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    url = fields.Str(required=False)
    
    completed_on = fields.Str(required=False)
    
    seller_id = fields.Int(required=False)
    
    task_id = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    status = fields.Str(required=False)
    


class EditInventoryDownloadsResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    data = fields.Nested(EditInventoryDataDownloadsResponseSchema, required=False)
    


class InventoryExportFiltersResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    brand_ids = fields.List(fields.Int(required=False), required=False)
    
    store_ids = fields.List(fields.Int(required=False), required=False)
    


class Stats(BaseSchema):
    # Catalog swagger.json

    
    total = fields.Int(required=False)
    


class InventoryExportResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    created_by = fields.Nested(UserInfo, required=False)
    
    created_on = fields.Str(required=False)
    
    filters = fields.Nested(InventoryExportFiltersResponseSchema, required=False)
    
    modified_on = fields.Str(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    seller_id = fields.Int(required=False)
    
    status = fields.Str(required=False)
    
    task_id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    stats = fields.Nested(Stats, required=False)
    
    _id = fields.Str(required=False)
    
    trigger_on = fields.Str(required=False)
    
    brand = fields.List(fields.Int(required=False), required=False)
    
    store = fields.List(fields.Int(required=False), required=False)
    


class InventoryFailedReason(BaseSchema):
    # Catalog swagger.json

    
    errors = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    reason_code = fields.Int(required=False)
    


class InventoryJobPayload(BaseSchema):
    # Catalog swagger.json

    
    currency = fields.Str(required=False)
    
    expiration_date = fields.Str(required=False)
    
    item_dimensions_unit_of_measure = fields.Str(required=False)
    
    item_weight_unit_of_measure = fields.Str(required=False)
    
    price = fields.Float(required=False)
    
    price_effective = fields.Float(required=False)
    
    price_marked = fields.Float(required=False)
    
    quantity = fields.Int(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    store_code = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    total_quantity = fields.Int(required=False)
    
    trace_id = fields.Str(required=False, allow_none=True)
    


class InventoryPage(BaseSchema):
    # Catalog swagger.json

    
    has_next = fields.Boolean(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    item_total = fields.Int(required=False)
    
    next_id = fields.Str(required=False, allow_none=True)
    
    type = fields.Str(required=False)
    


class InventoryPayload(BaseSchema):
    # Catalog swagger.json

    
    expiration_date = fields.Str(required=False)
    
    price_effective = fields.Float(required=False)
    
    price_marked = fields.Float(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    store_id = fields.Int(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    total_quantity = fields.Int(required=False, allow_none=True)
    
    sellable_quantity = fields.Int(required=False)
    
    trace_id = fields.Str(required=False)
    


class InventoryV2RequestSchema(BaseSchema):
    # Catalog swagger.json

    
    meta = fields.Dict(required=False)
    
    payload = fields.List(fields.Nested(InventoryPayload, required=False), required=False)
    


class InventoryIdentifier(BaseSchema):
    # Catalog swagger.json

    
    gtin_type = fields.Str(required=False)
    
    gtin_value = fields.Str(required=False)
    
    primary = fields.Boolean(required=False)
    


class InventoryGeoLocation(BaseSchema):
    # Catalog swagger.json

    
    type = fields.Str(required=False)
    
    coordinates = fields.List(fields.Float(required=False), required=False)
    


class InventoryMobileNumber(BaseSchema):
    # Catalog swagger.json

    
    number = fields.Str(required=False)
    
    country_code = fields.Int(required=False)
    


class InventoryAddress(BaseSchema):
    # Catalog swagger.json

    
    address1 = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    lat_long = fields.Nested(InventoryGeoLocation, required=False)
    
    country_code = fields.Str(required=False)
    


class InventoryManager(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    mobile_no = fields.Nested(InventoryMobileNumber, required=False)
    


class InventoryStore(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    store_code = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    address = fields.Nested(InventoryAddress, required=False)
    
    manager = fields.Nested(InventoryManager, required=False)
    
    _custom_json = fields.Dict(required=False)
    


class InventoryResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    currency = fields.Str(required=False)
    
    inventory_updated_on = fields.Str(required=False)
    
    item_id = fields.Int(required=False)
    
    price = fields.Float(required=False)
    
    price_effective = fields.Float(required=False)
    
    price_transfer = fields.Float(required=False)
    
    quantity = fields.Int(required=False)
    
    sellable_quantity = fields.Int(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    size = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    expiration_date = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    store = fields.Nested(InventoryStore, required=False)
    
    created_by = fields.Nested(UserInfo, required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    identifiers = fields.List(fields.Nested(InventoryIdentifier, required=False), required=False)
    


class InventoryResponseItem(BaseSchema):
    # Catalog swagger.json

    
    data = fields.Nested(InventoryPayload, required=False)
    
    reason = fields.Nested(InventoryFailedReason, required=False)
    


class InventoryResponsePaginated(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(InventoryResponseSchema, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class ApplicationInventorySellerIdentifierResponsePaginated(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(InventorySellerResponseSchema, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class InventorySellerResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    _custom_json = fields.Dict(required=False)
    
    added_on_store = fields.Str(required=False)
    
    brand = fields.Nested(BrandMeta, required=False)
    
    company = fields.Nested(CompanyMeta, required=False)
    
    country_of_origin = fields.Str(required=False)
    
    created_by = fields.Str(required=False, allow_none=True)
    
    dimension = fields.Nested(DimensionResponseSchema, required=False)
    
    expiration_date = fields.Str(required=False)
    
    fragile = fields.Boolean(required=False)
    
    fynd_article_code = fields.Str(required=False)
    
    fynd_item_code = fields.Str(required=False)
    
    fynd_meta = fields.Dict(required=False)
    
    identifier = fields.Dict(required=False)
    
    is_active = fields.Boolean(required=False)
    
    is_set = fields.Boolean(required=False)
    
    item_id = fields.Int(required=False)
    
    manufacturer = fields.Nested(ManufacturerResponseSchema, required=False)
    
    meta = fields.Dict(required=False, allow_none=True)
    
    modified_by = fields.Str(required=False, allow_none=True)
    
    price = fields.Nested(PriceMeta, required=False)
    
    quantities = fields.Nested(Quantities, required=False)
    
    raw_meta = fields.Dict(required=False)
    
    return_config = fields.Nested(InventoryReturnConfig, required=False)
    
    seller_identifier = fields.Str(required=False)
    
    set = fields.Nested(InventorySet, required=False)
    
    size = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    store = fields.Nested(StoreMeta, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    tax_identifier = fields.Nested(TaxIdentifier, required=False)
    
    total_quantity = fields.Int(required=False)
    
    trace_id = fields.Str(required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    trader = fields.List(fields.Nested(Trader1, required=False), required=False)
    
    uid = fields.Str(required=False)
    
    weight = fields.Nested(WeightResponseSchema, required=False)
    


class InventorySet(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    size_distribution = fields.Nested(SizeDistribution, required=False)
    


class InventoryStockResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Dict(required=False), required=False)
    
    page = fields.Nested(InventoryPage, required=False)
    


class InventoryUpdateResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(InventoryResponseItem, required=False), required=False)
    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class InventoryValidationResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    data = fields.Dict(required=False)
    
    message = fields.Str(required=False)
    


class InvoiceCredSchema(BaseSchema):
    # Catalog swagger.json

    
    enabled = fields.Boolean(required=False)
    
    password = fields.Str(required=False)
    
    username = fields.Str(required=False)
    


class InvoiceDetailsSchema(BaseSchema):
    # Catalog swagger.json

    
    e_invoice = fields.Nested(InvoiceCredSchema, required=False)
    
    e_waybill = fields.Nested(InvoiceCredSchema, required=False)
    


class Items(BaseSchema):
    # Catalog swagger.json

    
    cancelled = fields.Int(required=False)
    
    cancelled_records = fields.List(fields.Str(required=False), required=False)
    
    company_id = fields.Int(required=False)
    
    created_by = fields.Nested(UserCommon, required=False)
    
    created_on = fields.Str(required=False)
    
    failed = fields.Int(required=False)
    
    failed_records = fields.List(fields.Str(required=False), required=False)
    
    file_path = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    modified_by = fields.Nested(UserCommon, required=False)
    
    modified_on = fields.Str(required=False)
    
    retry = fields.Int(required=False)
    
    stage = fields.Str(required=False)
    
    succeed = fields.Int(required=False)
    
    total = fields.Int(required=False)
    
    tracking_url = fields.Str(required=False)
    


class PriceRange(BaseSchema):
    # Catalog swagger.json

    
    min = fields.Float(required=False)
    
    max = fields.Float(required=False)
    


class ProductPriceRangeSchema(BaseSchema):
    # Catalog swagger.json

    
    effective = fields.Nested(PriceRange, required=False)
    
    marked = fields.Nested(PriceRange, required=False)
    
    currency = fields.Str(required=False)
    


class LimitedProductData(BaseSchema):
    # Catalog swagger.json

    
    attributes = fields.Dict(required=False)
    
    country_of_origin = fields.Str(required=False)
    
    identifier = fields.Dict(required=False)
    
    images = fields.List(fields.Str(required=False), required=False)
    
    item_code = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    price = fields.Nested(ProductPriceRangeSchema, required=False)
    
    quantity = fields.Int(required=False)
    
    short_description = fields.Str(required=False)
    
    sizes = fields.List(fields.Str(required=False), required=False)
    
    slug = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    


class ListSizeGuide(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(SizeGuideItem, required=False), required=False)
    
    page = fields.Nested(PageResponseSchema, required=False)
    


class LocationDayWiseSchema(BaseSchema):
    # Catalog swagger.json

    
    closing = fields.Nested(LocationTimingSchema, required=False)
    
    open = fields.Boolean(required=False)
    
    opening = fields.Nested(LocationTimingSchema, required=False)
    
    weekday = fields.Str(required=False)
    


class LocationTimingSchema(BaseSchema):
    # Catalog swagger.json

    
    hour = fields.Int(required=False)
    
    minute = fields.Int(required=False)
    


class LocationIntegrationType(BaseSchema):
    # Catalog swagger.json

    
    inventory = fields.Str(required=False)
    
    order = fields.Str(required=False)
    


class LocationListSchema(BaseSchema):
    # Catalog swagger.json

    
    filters = fields.List(fields.Dict(required=False), required=False)
    
    items = fields.List(fields.Nested(GetLocationSchema, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class LocationManagerSchema(BaseSchema):
    # Catalog swagger.json

    
    email = fields.Str(required=False)
    
    mobile_no = fields.Nested(SellerPhoneNumber, required=False)
    
    name = fields.Str(required=False)
    


class Logo(BaseSchema):
    # Catalog swagger.json

    
    aspect_ratio = fields.Str(required=False)
    
    aspect_ratio_f = fields.Int(required=False)
    
    secure_url = fields.Str(required=False)
    
    url = fields.Str(required=False)
    


class MOQData(BaseSchema):
    # Catalog swagger.json

    
    increment_unit = fields.Int(required=False)
    
    maximum = fields.Int(required=False)
    
    minimum = fields.Int(required=False)
    


class ManufacturerResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    address = fields.Str(required=False)
    
    is_default = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    


class InventoryManufacturerResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    address = fields.Str(required=False)
    
    is_default = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    


class Media(BaseSchema):
    # Catalog swagger.json

    
    meta = fields.Dict(required=False)
    
    type = fields.Str(required=False)
    
    url = fields.Str(required=False)
    
    alt = fields.Str(required=False)
    
    thumbnail = fields.Str(required=False)
    


class Media1(BaseSchema):
    # Catalog swagger.json

    
    landscape = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    portrait = fields.Str(required=False)
    


class DepartmentMedia(BaseSchema):
    # Catalog swagger.json

    
    aspect_ratio = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    url = fields.Str(required=False)
    


class Meta(BaseSchema):
    # Catalog swagger.json

    
    headers = fields.Nested(GuideHeaders, required=False)
    
    values = fields.List(fields.Nested(GuideValues, required=False), required=False)
    
    unit = fields.Str(required=False)
    


class GuideHeaders(BaseSchema):
    # Catalog swagger.json

    
    col_1 = fields.Nested(Header, required=False)
    
    col_2 = fields.Nested(Header, required=False)
    
    col_3 = fields.Nested(Header, required=False)
    
    col_4 = fields.Nested(Header, required=False)
    
    col_5 = fields.Nested(Header, required=False)
    
    col_6 = fields.Nested(Header, required=False)
    
    col_7 = fields.Nested(Header, required=False)
    
    col_8 = fields.Nested(Header, required=False)
    
    col_9 = fields.Nested(Header, required=False)
    
    col_10 = fields.Nested(Header, required=False)
    


class GuideValues(BaseSchema):
    # Catalog swagger.json

    
    col_1 = fields.Str(required=False)
    
    col_2 = fields.Str(required=False)
    
    col_3 = fields.Str(required=False)
    
    col_4 = fields.Str(required=False)
    
    col_5 = fields.Str(required=False)
    
    col_6 = fields.Str(required=False)
    
    col_7 = fields.Str(required=False)
    
    col_8 = fields.Str(required=False)
    
    col_9 = fields.Str(required=False)
    
    col_10 = fields.Str(required=False)
    


class Header(BaseSchema):
    # Catalog swagger.json

    
    value = fields.Str(required=False)
    
    convertable = fields.Boolean(required=False)
    


class MetaDataListingFilterMetaResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    display = fields.Str(required=False)
    
    filter_types = fields.List(fields.Str(required=False), required=False)
    
    key = fields.Str(required=False)
    
    units = fields.List(fields.Dict(required=False), required=False)
    


class MetaDataListingFilterResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    data = fields.List(fields.Nested(MetaDataListingFilterMetaResponseSchema, required=False), required=False)
    


class MetaDataListingResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    filter = fields.Nested(MetaDataListingFilterResponseSchema, required=False)
    
    sort = fields.Nested(MetaDataListingSortResponseSchema, required=False)
    


class MetaDataListingSortMetaResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    display = fields.Str(required=False)
    
    key = fields.Str(required=False)
    


class MetaDataListingSortResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    data = fields.List(fields.Nested(MetaDataListingSortMetaResponseSchema, required=False), required=False)
    


class MetaFields(BaseSchema):
    # Catalog swagger.json

    
    key = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class NetQuantity(BaseSchema):
    # Catalog swagger.json

    
    unit = fields.Str(required=False)
    
    value = fields.Float(required=False)
    


class NetQuantityResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    unit = fields.Str(required=False)
    
    value = fields.Float(required=False)
    


class NextSchedule(BaseSchema):
    # Catalog swagger.json

    
    end = fields.Str(required=False, allow_none=True)
    
    start = fields.Str(required=False, allow_none=True)
    


class OptinCompanyBrandDetailsView(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(CompanyBrandDetail, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class OptinAddress(BaseSchema):
    # Catalog swagger.json

    
    address1 = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    latitude = fields.Float(required=False)
    
    longitude = fields.Float(required=False)
    
    country_code = fields.Str(required=False)
    


class OptinDocument(BaseSchema):
    # Catalog swagger.json

    
    type = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    legal_name = fields.Str(required=False)
    
    verified = fields.Boolean(required=False)
    
    url = fields.Str(required=False)
    


class OptinBusinessCountryInfo(BaseSchema):
    # Catalog swagger.json

    
    country = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    currency = fields.Dict(required=False)
    
    timezone = fields.Str(required=False)
    


class OptinCompanyDetail(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    business_info = fields.Str(required=False)
    
    business_type = fields.Str(required=False)
    
    company_type = fields.Str(required=False)
    
    business_country_info = fields.Nested(OptinBusinessCountryInfo, required=False)
    
    address = fields.Nested(OptinAddress, required=False)
    
    documents = fields.List(fields.Nested(OptinDocument, required=False), required=False)
    
    brands = fields.List(fields.Int(required=False), required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    warnings = fields.Dict(required=False)
    
    stage = fields.Str(required=False)
    


class OptinCompanyMetrics(BaseSchema):
    # Catalog swagger.json

    
    brand = fields.Int(required=False)
    
    company = fields.Str(required=False)
    
    store = fields.Int(required=False)
    


class OptinStoreDetails(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(StoreDetail, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class OwnerAppItemResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    alt_text = fields.Dict(required=False)
    
    is_cod = fields.Boolean(required=False)
    
    is_gift = fields.Boolean(required=False)
    
    moq = fields.Nested(MOQData, required=False)
    
    seo = fields.Nested(SEOData, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    _custom_meta = fields.List(fields.Nested(MetaFields, required=False), required=False)
    


class Page(BaseSchema):
    # Catalog swagger.json

    
    item_total = fields.Int(required=False)
    
    next_id = fields.Str(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    has_next = fields.Boolean(required=False)
    
    current = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    size = fields.Int(required=False)
    
    total = fields.Int(required=False)
    


class PageResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    current = fields.Int(required=False)
    
    has_next = fields.Boolean(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    item_total = fields.Int(required=False)
    
    size = fields.Int(required=False)
    


class PageResponseType(BaseSchema):
    # Catalog swagger.json

    
    current = fields.Int(required=False)
    
    has_next = fields.Boolean(required=False)
    
    next = fields.Int(required=False)
    
    total_count = fields.Int(required=False)
    


class Price(BaseSchema):
    # Catalog swagger.json

    
    currency = fields.Str(required=False)
    
    max_effective = fields.Float(required=False)
    
    max_marked = fields.Float(required=False)
    
    min_effective = fields.Float(required=False)
    
    min_marked = fields.Float(required=False)
    


class ProductListingDetailPrice(BaseSchema):
    # Catalog swagger.json

    
    currency_code = fields.Str(required=False)
    
    currency_symbol = fields.Str(required=False)
    
    max = fields.Float(required=False)
    
    min = fields.Float(required=False)
    


class PriceArticle(BaseSchema):
    # Catalog swagger.json

    
    currency = fields.Str(required=False)
    
    effective = fields.Float(required=False)
    
    marked = fields.Float(required=False)
    
    tp_notes = fields.Dict(required=False)
    
    transfer = fields.Float(required=False)
    


class PriceMeta(BaseSchema):
    # Catalog swagger.json

    
    currency = fields.Str(required=False)
    
    effective = fields.Float(required=False)
    
    marked = fields.Float(required=False)
    
    tp_notes = fields.Dict(required=False)
    
    transfer = fields.Float(required=False)
    
    updated_at = fields.Str(required=False)
    


class ProdcutTemplateCategoriesResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(CategoriesResponseSchema, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class Product(BaseSchema):
    # Catalog swagger.json

    
    _custom_json = fields.Dict(required=False)
    
    all_company_ids = fields.List(fields.Int(required=False), required=False)
    
    all_identifiers = fields.List(fields.Str(required=False), required=False)
    
    all_sizes = fields.List(fields.Dict(required=False), required=False)
    
    attributes = fields.Dict(required=False)
    
    brand = fields.Nested(Brand, required=False)
    
    brand_uid = fields.Int(required=False)
    
    category = fields.Dict(required=False)
    
    category_slug = fields.Str(required=False)
    
    category_uid = fields.Int(required=False)
    
    color = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    country_of_origin = fields.Str(required=False)
    
    created_by = fields.Dict(required=False)
    
    created_on = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    custom_order = fields.Dict(required=False)
    
    departments = fields.List(fields.Int(required=False), required=False)
    
    description = fields.Str(required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    hsn_code = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    image_nature = fields.Str(required=False)
    
    images = fields.List(fields.Nested(Image, required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    is_dependent = fields.Boolean(required=False)
    
    is_expirable = fields.Boolean(required=False)
    
    is_image_less_product = fields.Boolean(required=False)
    
    is_physical = fields.Boolean(required=False)
    
    is_set = fields.Boolean(required=False)
    
    item_code = fields.Str(required=False)
    
    item_type = fields.Str(required=False)
    
    l3_mapping = fields.List(fields.Str(required=False), required=False)
    
    media = fields.List(fields.Nested(Media, required=False), required=False)
    
    modified_by = fields.Dict(required=False)
    
    modified_on = fields.Str(required=False)
    
    moq = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    
    net_quantity = fields.Nested(NetQuantityResponseSchema, required=False)
    
    no_of_boxes = fields.Int(required=False)
    
    pending = fields.Str(required=False)
    
    primary_color = fields.Str(required=False)
    
    product_group_tag = fields.List(fields.Str(required=False), required=False)
    
    product_publish = fields.Nested(ProductPublished, required=False)
    
    return_config = fields.Nested(ReturnConfigResponseSchema, required=False)
    
    short_description = fields.Str(required=False)
    
    size_guide = fields.Str(required=False)
    
    sizes = fields.List(fields.Dict(required=False), required=False)
    
    slug = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    tax_identifier = fields.Nested(TaxIdentifier, required=False)
    
    teaser_tag = fields.Dict(required=False)
    
    template_tag = fields.Str(required=False)
    
    trader = fields.List(fields.Nested(Trader, required=False), required=False)
    
    uid = fields.Int(required=False)
    
    variant_group = fields.Dict(required=False)
    
    variant_media = fields.Dict(required=False)
    
    variants = fields.Dict(required=False)
    
    verified_by = fields.Nested(VerifiedBy, required=False)
    
    verified_on = fields.Str(required=False)
    


class ProductAttributesResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(AttributeMasterSchema, required=False), required=False)
    


class ProductBrand(BaseSchema):
    # Catalog swagger.json

    
    action = fields.Nested(Action, required=False)
    
    logo = fields.Nested(Media, required=False)
    
    name = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    


class ProductBulkAssets(BaseSchema):
    # Catalog swagger.json

    
    batch_id = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    url = fields.Str(required=False)
    
    user = fields.Dict(required=False)
    


class ProductBulkRequestSchema(BaseSchema):
    # Catalog swagger.json

    
    cancelled = fields.Int(required=False)
    
    cancelled_records = fields.List(fields.Dict(required=False), required=False)
    
    company_id = fields.Int(required=False)
    
    created_by = fields.Nested(UserDetail1, required=False)
    
    created_on = fields.Str(required=False)
    
    failed = fields.Int(required=False)
    
    failed_records = fields.List(fields.Dict(required=False), required=False)
    
    file_path = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    modified_by = fields.Nested(UserDetail1, required=False)
    
    modified_on = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    succeed = fields.Int(required=False)
    
    template = fields.Nested(ProductTemplate, required=False)
    
    template_tag = fields.Str(required=False)
    
    total = fields.Int(required=False)
    


class InventoryBulkJob(BaseSchema):
    # Catalog swagger.json

    
    company_id = fields.Int(required=False)
    
    file_path = fields.Str(required=False)
    


class ProductBulkResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    batch_id = fields.Str(required=False)
    


class InventoryBulkResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    batch_id = fields.Str(required=False)
    
    created_by = fields.Nested(UserInfo, required=False)
    
    created_on = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    modified_on = fields.Str(required=False)
    


class ProductBulkRequestSchemaList(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(ProductBulkRequestSchema, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class ProductBundleItem(BaseSchema):
    # Catalog swagger.json

    
    max_quantity = fields.Int(required=False)
    
    min_quantity = fields.Int(required=False)
    
    product_uid = fields.Int(required=False)
    


class ProductBundleRequestSchema(BaseSchema):
    # Catalog swagger.json

    
    choice = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    created_by = fields.Dict(required=False)
    
    created_on = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    logo = fields.Str(required=False, allow_none=True)
    
    meta = fields.Dict(required=False)
    
    modified_by = fields.Dict(required=False)
    
    modified_on = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    page_visibility = fields.List(fields.Str(required=False), required=False)
    
    products = fields.List(fields.Nested(ProductBundleItem, required=False), required=False)
    
    same_store_assignment = fields.Boolean(required=False)
    
    slug = fields.Str(required=False)
    
    auto_add_to_cart = fields.Boolean(required=False)
    
    auto_select = fields.Boolean(required=False)
    
    allow_remove = fields.Boolean(required=False)
    
    prefer_single_shipment = fields.Boolean(required=False)
    
    allow_individual_return = fields.Boolean(required=False)
    
    allow_individual_cancel = fields.Boolean(required=False)
    


class ProductBundleUpdateRequestSchema(BaseSchema):
    # Catalog swagger.json

    
    choice = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    logo = fields.Str(required=False, allow_none=True)
    
    meta = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    
    page_visibility = fields.List(fields.Str(required=False), required=False)
    
    products = fields.List(fields.Nested(ProductBundleItem, required=False), required=False)
    
    same_store_assignment = fields.Boolean(required=False)
    
    slug = fields.Str(required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    modified_on = fields.Str(required=False)
    
    allow_individual_cancel = fields.Boolean(required=False)
    
    allow_individual_return = fields.Boolean(required=False)
    
    allow_remove = fields.Boolean(required=False)
    
    auto_add_to_cart = fields.Boolean(required=False)
    
    auto_select = fields.Boolean(required=False)
    
    prefer_single_shipment = fields.Boolean(required=False)
    


class ProductConfigurationDownloads(BaseSchema):
    # Catalog swagger.json

    
    data = fields.List(fields.Dict(required=False), required=False)
    
    multivalue = fields.Boolean(required=False)
    


class ProductCreateUpdateSizesSchema(BaseSchema):
    # Catalog swagger.json

    
    size = fields.Str(required=False)
    
    price = fields.Float(required=False)
    
    price_effective = fields.Float(required=False)
    
    price_transfer = fields.Float(required=False)
    
    currency = fields.Str(required=False)
    
    item_length = fields.Float(required=False)
    
    item_width = fields.Float(required=False)
    
    item_height = fields.Float(required=False)
    
    item_weight = fields.Float(required=False)
    
    item_dimensions_unit_of_measure = fields.Str(required=False)
    
    item_weight_unit_of_measure = fields.Str(required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    identifiers = fields.List(fields.Nested(GTIN, required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    


class ProductCreateUpdateSchemaV2(BaseSchema):
    # Catalog swagger.json

    
    _custom_json = fields.Dict(required=False)
    
    action = fields.Str(required=False)
    
    attributes = fields.Dict(required=False)
    
    brand_uid = fields.Int(required=False)
    
    bulk_job_id = fields.Str(required=False)
    
    category_slug = fields.Str(required=False)
    
    change_request_id = fields.Str(required=False, allow_none=True)
    
    company_id = fields.Int(required=False)
    
    country_of_origin = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    custom_order = fields.Nested(CustomOrder, required=False)
    
    departments = fields.List(fields.Int(required=False), required=False)
    
    description = fields.Str(required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    is_dependent = fields.Boolean(required=False)
    
    is_image_less_product = fields.Boolean(required=False)
    
    is_set = fields.Boolean(required=False)
    
    item_code = fields.Str(required=False)
    
    item_type = fields.Str(required=False)
    
    media = fields.List(fields.Nested(Media, required=False), required=False)
    
    multi_size = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    net_quantity = fields.Nested(NetQuantity, required=False)
    
    no_of_boxes = fields.Int(required=False)
    
    product_group_tag = fields.List(fields.Str(required=False), required=False)
    
    product_publish = fields.Nested(ProductPublish, required=False)
    
    requester = fields.Str(required=False)
    
    return_config = fields.Nested(ReturnConfig, required=False)
    
    short_description = fields.Str(required=False)
    
    size_guide = fields.Str(required=False)
    
    sizes = fields.List(fields.Dict(required=False), required=False)
    
    slug = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    tax_identifier = fields.Nested(TaxIdentifier, required=False)
    
    teaser_tag = fields.Nested(TeaserTag, required=False)
    
    template_tag = fields.Str(required=False)
    
    trader = fields.List(fields.Nested(Trader, required=False), required=False)
    
    uid = fields.Int(required=False, allow_none=True)
    
    variant_group = fields.Dict(required=False)
    
    variant_media = fields.Dict(required=False)
    
    variants = fields.Dict(required=False)
    


class ProductDetail(BaseSchema):
    # Catalog swagger.json

    
    attributes = fields.Dict(required=False)
    
    brand = fields.Nested(ProductBrand, required=False)
    
    description = fields.Str(required=False)
    
    grouped_attributes = fields.List(fields.Nested(ProductDetailGroupedAttribute, required=False), required=False)
    
    has_variant = fields.Boolean(required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    image_nature = fields.Str(required=False)
    
    item_code = fields.Str(required=False)
    
    item_type = fields.Str(required=False)
    
    medias = fields.List(fields.Nested(Media, required=False), required=False)
    
    name = fields.Str(required=False)
    
    product_online_date = fields.Str(required=False)
    
    promo_meta = fields.Dict(required=False)
    
    rating = fields.Float(required=False)
    
    rating_count = fields.Int(required=False)
    
    short_description = fields.Str(required=False)
    
    similars = fields.List(fields.Str(required=False), required=False)
    
    slug = fields.Str(required=False)
    
    teaser_tag = fields.Dict(required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    country_of_origin = fields.Str(required=False)
    
    categories = fields.List(fields.Nested(ApplicationProductCategoryItem, required=False), required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    no_of_boxes = fields.Int(required=False)
    
    custom_order = fields.Nested(CustomOrder, required=False)
    


class ApplicationProductCategoryItem(BaseSchema):
    # Catalog swagger.json

    
    id = fields.Int(required=False)
    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    logo = fields.Nested(ApplicationProductMedia, required=False)
    
    action = fields.Nested(PageAction, required=False)
    


class ApplicationProductMedia(BaseSchema):
    # Catalog swagger.json

    
    type = fields.Str(required=False)
    
    url = fields.Str(required=False)
    


class ProductDetailAttribute(BaseSchema):
    # Catalog swagger.json

    
    key = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class ProductDetailGroupedAttribute(BaseSchema):
    # Catalog swagger.json

    
    details = fields.List(fields.Nested(ProductDetailAttribute, required=False), required=False)
    
    title = fields.Str(required=False)
    


class PatchProductDownloadsDataResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    created_on = fields.Str(required=False)
    
    created_by = fields.Nested(UserInfo, required=False)
    
    task_id = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    seller_id = fields.Int(required=False)
    
    url = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    completed_on = fields.Str(required=False)
    


class PatchProductDownloadsResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    data = fields.Nested(PatchProductDownloadsDataResponseSchema, required=False)
    


class ProductDownloadFilters(BaseSchema):
    # Catalog swagger.json

    
    brands = fields.List(fields.Str(required=False), required=False)
    
    catalogue_types = fields.List(fields.Str(required=False), required=False)
    
    templates = fields.List(fields.Str(required=False), required=False)
    


class CreateProductDownloadsDataResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    created_on = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    task_id = fields.Str(required=False)
    
    filters = fields.Nested(ProductDownloadFilters, required=False)
    
    created_by = fields.Nested(UserInfo, required=False)
    
    _id = fields.Str(required=False)
    
    notification_emails = fields.List(fields.Dict(required=False), required=False)
    
    modified_on = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    seller_id = fields.Int(required=False)
    
    stats = fields.Nested(Stats, required=False)
    


class CreateProductDownloadsResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    data = fields.Nested(CreateProductDownloadsDataResponseSchema, required=False)
    


class GetProductDownloadsResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    modified_on = fields.Str(required=False)
    
    url = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    completed_on = fields.Str(required=False)
    
    created_by = fields.Nested(UserInfo, required=False)
    
    created_on = fields.Str(required=False)
    
    seller_id = fields.Int(required=False)
    
    task_id = fields.Str(required=False)
    
    id = fields.Str(required=False)
    


class ProductDownloadsResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(ProductTemplateExportResponseSchema, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class ProductFilters(BaseSchema):
    # Catalog swagger.json

    
    key = fields.Nested(ProductFiltersKey, required=False)
    
    values = fields.List(fields.Nested(ProductFiltersValue, required=False), required=False)
    


class ProductFiltersKey(BaseSchema):
    # Catalog swagger.json

    
    display = fields.Str(required=False)
    
    kind = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    operators = fields.List(fields.Str(required=False), required=False)
    


class ProductFiltersValue(BaseSchema):
    # Catalog swagger.json

    
    count = fields.Int(required=False)
    
    currency_code = fields.Str(required=False)
    
    currency_symbol = fields.Str(required=False)
    
    display = fields.Str(required=False)
    
    display_format = fields.Str(required=False)
    
    is_selected = fields.Boolean(required=False)
    
    max = fields.Int(required=False)
    
    min = fields.Int(required=False)
    
    query_format = fields.Str(required=False)
    
    selected_max = fields.Int(required=False)
    
    selected_min = fields.Int(required=False)
    
    value = fields.Dict(required=False)
    


class ApplicationCategoryAction(BaseSchema):
    # Catalog swagger.json

    
    page = fields.Nested(CategoryPageAction, required=False)
    
    type = fields.Str(required=False)
    


class ApplicationCategoryItem(BaseSchema):
    # Catalog swagger.json

    
    _custom_json = fields.Dict(required=False)
    
    action = fields.Nested(ApplicationCategoryAction, required=False)
    
    id = fields.Int(required=False)
    
    logo = fields.Nested(CategoryImage, required=False)
    
    name = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    


class CategoryPageAction(BaseSchema):
    # Catalog swagger.json

    
    query = fields.Nested(CategoryQuery, required=False)
    
    type = fields.Str(required=False)
    


class CategoryQuery(BaseSchema):
    # Catalog swagger.json

    
    category = fields.List(fields.Str(required=False), required=False)
    


class CategoryImage(BaseSchema):
    # Catalog swagger.json

    
    type = fields.Str(required=False)
    
    url = fields.Str(required=False)
    


class PageAction(BaseSchema):
    # Catalog swagger.json

    
    page = fields.Nested(ActionObject, required=False)
    
    type = fields.Str(required=False)
    


class ActionObject(BaseSchema):
    # Catalog swagger.json

    
    type = fields.Str(required=False)
    
    query = fields.Dict(required=False)
    


class ProductListingPrice(BaseSchema):
    # Catalog swagger.json

    
    effective = fields.Nested(Price1, required=False)
    
    marked = fields.Nested(Price1, required=False)
    
    selling = fields.Nested(Price1, required=False)
    


class ProductListingResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(Product, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class ProductListingResponseV2Schema(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(ProductSchemaV2, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class ProductVerificationModel(BaseSchema):
    # Catalog swagger.json

    
    rejected_fields = fields.Dict(required=False)
    
    status = fields.Str(required=False)
    
    brand_uid = fields.Int(required=False)
    
    created_on = fields.Str(required=False)
    
    company_ids = fields.List(fields.Int(required=False), required=False)
    
    item_code = fields.Str(required=False)
    
    remark = fields.Str(required=False)
    
    created_by = fields.Nested(UserInfo, required=False)
    
    modified_on = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    item_id = fields.Int(required=False)
    
    id = fields.Str(required=False)
    


class ProductPublish(BaseSchema):
    # Catalog swagger.json

    
    is_set = fields.Boolean(required=False)
    
    product_online_date = fields.Str(required=False)
    


class ProductPublished(BaseSchema):
    # Catalog swagger.json

    
    is_set = fields.Boolean(required=False)
    
    product_online_date = fields.Int(required=False)
    


class ProductReturnConfigSchema(BaseSchema):
    # Catalog swagger.json

    
    on_same_store = fields.Boolean(required=False)
    
    store_uid = fields.Int(required=False)
    


class ProductReturnConfigBaseSchema(BaseSchema):
    # Catalog swagger.json

    
    returnable = fields.Boolean(required=False)
    
    time = fields.Int(required=False)
    
    unit = fields.Str(required=False)
    


class SizeDetails(BaseSchema):
    # Catalog swagger.json

    
    size = fields.Str(required=False)
    
    store_count = fields.Int(required=False)
    
    sellable_quantity = fields.Int(required=False)
    
    sellable = fields.Boolean(required=False)
    
    size_priority = fields.Int(required=False)
    
    identifiers = fields.List(fields.Nested(Identifier, required=False), required=False)
    
    price = fields.Raw(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    price_transfer = fields.Float(required=False)
    
    track_inventory = fields.Boolean(required=False)
    


class ProductSchemaV2(BaseSchema):
    # Catalog swagger.json

    
    _custom_json = fields.Dict(required=False)
    
    all_company_ids = fields.List(fields.Int(required=False), required=False)
    
    all_identifiers = fields.List(fields.Str(required=False), required=False)
    
    all_sizes = fields.List(fields.Dict(required=False), required=False)
    
    attributes = fields.Dict(required=False)
    
    brand = fields.Nested(Brand, required=False)
    
    brand_uid = fields.Int(required=False)
    
    category = fields.Dict(required=False)
    
    category_slug = fields.Str(required=False)
    
    category_uid = fields.Int(required=False)
    
    color = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    country_of_origin = fields.Str(required=False)
    
    created_by = fields.Dict(required=False)
    
    currency = fields.Str(required=False)
    
    custom_order = fields.Dict(required=False)
    
    departments = fields.List(fields.Int(required=False), required=False)
    
    description = fields.Str(required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    hsn_code = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    image_nature = fields.Str(required=False)
    
    images = fields.List(fields.Nested(Image, required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    is_dependent = fields.Boolean(required=False)
    
    is_expirable = fields.Boolean(required=False)
    
    is_image_less_product = fields.Boolean(required=False)
    
    is_physical = fields.Boolean(required=False)
    
    is_set = fields.Boolean(required=False)
    
    item_code = fields.Str(required=False)
    
    item_type = fields.Str(required=False)
    
    l3_mapping = fields.List(fields.Str(required=False), required=False)
    
    media = fields.List(fields.Nested(Media, required=False), required=False)
    
    modified_by = fields.Dict(required=False)
    
    modified_on = fields.Str(required=False)
    
    moq = fields.Dict(required=False)
    
    multi_size = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    net_quantity = fields.Nested(NetQuantityResponseSchema, required=False)
    
    no_of_boxes = fields.Int(required=False)
    
    pending = fields.Str(required=False)
    
    primary_color = fields.Str(required=False)
    
    product_group_tag = fields.List(fields.Str(required=False), required=False)
    
    product_publish = fields.Nested(ProductPublish, required=False)
    
    return_config = fields.Nested(ReturnConfigResponseSchema, required=False)
    
    short_description = fields.Str(required=False)
    
    size_guide = fields.Str(required=False)
    
    sizes = fields.List(fields.Nested(SizeDetails, required=False), required=False)
    
    slug = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    tax_identifier = fields.Nested(TaxIdentifier, required=False)
    
    teaser_tag = fields.Dict(required=False)
    
    template_tag = fields.Str(required=False)
    
    trader = fields.List(fields.Nested(Trader, required=False), required=False)
    
    uid = fields.Int(required=False)
    
    variant_group = fields.Dict(required=False)
    
    variant_media = fields.Dict(required=False)
    
    variants = fields.Dict(required=False)
    
    verified_by = fields.Nested(VerifiedBy, required=False)
    
    verified_on = fields.Str(required=False)
    


class ProductSize(BaseSchema):
    # Catalog swagger.json

    
    max = fields.Int(required=False)
    
    min = fields.Int(required=False)
    


class ProductSizeDeleteDataResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    company_id = fields.Int(required=False)
    
    item_id = fields.Int(required=False)
    
    size = fields.Str(required=False)
    


class ProductSizeDeleteResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    data = fields.Nested(ProductSizeDeleteDataResponseSchema, required=False)
    
    success = fields.Boolean(required=False)
    


class ProductSortOn(BaseSchema):
    # Catalog swagger.json

    
    is_selected = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class ProductTagsViewResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Str(required=False), required=False)
    


class ProductTemplate(BaseSchema):
    # Catalog swagger.json

    
    attributes = fields.List(fields.Str(required=False), required=False)
    
    categories = fields.List(fields.Str(required=False), required=False)
    
    created_by = fields.Nested(UserInfo, required=False)
    
    created_on = fields.Str(required=False)
    
    departments = fields.List(fields.Str(required=False), required=False)
    
    description = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    is_archived = fields.Boolean(required=False)
    
    is_expirable = fields.Boolean(required=False)
    
    is_physical = fields.Boolean(required=False)
    
    logo = fields.Str(required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    modified_on = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    tag = fields.Str(required=False)
    


class ProductTemplateDownloadsExport(BaseSchema):
    # Catalog swagger.json

    
    filters = fields.Nested(ProductTemplateExportFilterRequestSchema, required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False, allow_none=True)
    


class ProductTemplateExportFilterRequestSchema(BaseSchema):
    # Catalog swagger.json

    
    brands = fields.List(fields.Str(required=False), required=False)
    
    catalogue_types = fields.List(fields.Str(required=False), required=False)
    
    from_date = fields.Str(required=False)
    
    templates = fields.List(fields.Str(required=False), required=False)
    
    to_date = fields.Str(required=False)
    


class ProductTemplateExportResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    trigger_on = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    template_tags = fields.Raw(required=False)
    
    completed_on = fields.Str(required=False)
    
    created_by = fields.Nested(UserInfo, required=False)
    
    filters = fields.Dict(required=False)
    
    modified_on = fields.Str(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    seller_id = fields.Int(required=False)
    
    status = fields.Str(required=False)
    
    task_id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    url = fields.Str(required=False)
    


class ProductVariants(BaseSchema):
    # Catalog swagger.json

    
    brand_uid = fields.Int(required=False)
    
    category_uid = fields.Int(required=False)
    
    item_code = fields.Str(required=False)
    
    media = fields.List(fields.Nested(Media, required=False), required=False)
    
    name = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    


class CompanyVerificationStats(BaseSchema):
    # Catalog swagger.json

    
    verified = fields.Int(required=False)
    
    total = fields.Int(required=False)
    


class CompanyVerificationResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    stats = fields.Nested(CompanyVerificationStats, required=False)
    


class ProductVariantsResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    page = fields.Nested(Page, required=False)
    
    variants = fields.List(fields.Nested(ProductVariants, required=False), required=False)
    


class Properties(BaseSchema):
    # Catalog swagger.json

    
    brand_uid = fields.Dict(required=False)
    
    category_slug = fields.Dict(required=False)
    
    command = fields.Dict(required=False)
    
    country_of_origin = fields.Dict(required=False)
    
    currency = fields.Dict(required=False)
    
    custom_order = fields.Dict(required=False)
    
    description = fields.Dict(required=False)
    
    highlights = fields.Dict(required=False)
    
    hsn_code = fields.Dict(required=False)
    
    is_active = fields.Dict(required=False)
    
    is_dependent = fields.Dict(required=False)
    
    item_code = fields.Dict(required=False)
    
    item_type = fields.Dict(required=False)
    
    media = fields.Dict(required=False)
    
    multi_size = fields.Dict(required=False)
    
    name = fields.Dict(required=False)
    
    no_of_boxes = fields.Dict(required=False)
    
    product_group_tag = fields.Dict(required=False)
    
    product_publish = fields.Dict(required=False)
    
    return_config = fields.Dict(required=False)
    
    short_description = fields.Dict(required=False)
    
    size_guide = fields.Dict(required=False)
    
    sizes = fields.Dict(required=False)
    
    slug = fields.Dict(required=False)
    
    tags = fields.Dict(required=False)
    
    teaser_tag = fields.Dict(required=False)
    
    trader = fields.Dict(required=False)
    
    trader_type = fields.Dict(required=False)
    
    variants = fields.Dict(required=False)
    


class Quantities(BaseSchema):
    # Catalog swagger.json

    
    damaged = fields.Nested(QuantityBase, required=False)
    
    not_available = fields.Nested(QuantityBase, required=False)
    
    order_committed = fields.Nested(QuantityBase, required=False)
    
    sellable = fields.Nested(QuantityBase, required=False)
    


class QuantitiesArticle(BaseSchema):
    # Catalog swagger.json

    
    damaged = fields.Nested(Quantity, required=False)
    
    not_available = fields.Nested(Quantity, required=False)
    
    order_committed = fields.Nested(Quantity, required=False)
    
    sellable = fields.Nested(Quantity, required=False)
    


class Quantity(BaseSchema):
    # Catalog swagger.json

    
    count = fields.Int(required=False)
    


class QuantityBase(BaseSchema):
    # Catalog swagger.json

    
    count = fields.Int(required=False)
    
    updated_at = fields.Str(required=False)
    


class ReturnConfig(BaseSchema):
    # Catalog swagger.json

    
    returnable = fields.Boolean(required=False)
    
    time = fields.Int(required=False)
    
    unit = fields.Str(required=False)
    


class InventoryReturnConfig(BaseSchema):
    # Catalog swagger.json

    
    returnable = fields.Boolean(required=False)
    
    time = fields.Int(required=False)
    
    unit = fields.Str(required=False)
    


class ReturnConfig2(BaseSchema):
    # Catalog swagger.json

    
    returnable = fields.Boolean(required=False)
    
    time = fields.Int(required=False)
    
    unit = fields.Str(required=False)
    


class Sitemap(BaseSchema):
    # Catalog swagger.json

    
    priority = fields.Float(required=False)
    
    frequency = fields.Str(required=False)
    


class PageQuery(BaseSchema):
    # Catalog swagger.json

    
    brand = fields.List(fields.Str(required=False), required=False)
    


class ApplicationCollectionItemSeoPage(BaseSchema):
    # Catalog swagger.json

    
    params = fields.Dict(required=False)
    
    query = fields.Nested(PageQuery, required=False)
    
    type = fields.Str(required=False)
    
    url = fields.Str(required=False)
    


class ApplicationCollectionItemSeoAction(BaseSchema):
    # Catalog swagger.json

    
    type = fields.Str(required=False)
    
    page = fields.Nested(ApplicationCollectionItemSeoPage, required=False)
    


class ApplicationCollectionItemSeoBreadcrumbs(BaseSchema):
    # Catalog swagger.json

    
    url = fields.Str(required=False)
    
    action = fields.List(fields.Nested(ApplicationItemSeoAction, required=False), required=False)
    


class ApplicationItemSeoAction(BaseSchema):
    # Catalog swagger.json

    
    page = fields.Dict(required=False)
    
    type = fields.Str(required=False)
    


class ApplicationItemSeoBreadcrumbs(BaseSchema):
    # Catalog swagger.json

    
    url = fields.Str(required=False)
    
    action = fields.List(fields.Nested(ApplicationItemSeoAction, required=False), required=False)
    


class ApplicationItemSeoMetaTagItem(BaseSchema):
    # Catalog swagger.json

    
    key = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class ApplicationItemSeoMetaTags(BaseSchema):
    # Catalog swagger.json

    
    title = fields.Str(required=False)
    
    items = fields.List(fields.Nested(ApplicationItemSeoMetaTagItem, required=False), required=False)
    


class Metatags(BaseSchema):
    # Catalog swagger.json

    
    title = fields.Str(required=False)
    
    items = fields.List(fields.Nested(ApplicationItemSeoMetaTags, required=False), required=False)
    


class SizePromotionThreshold(BaseSchema):
    # Catalog swagger.json

    
    threshold_type = fields.Str(required=False)
    
    threshold_value = fields.Int(required=False)
    


class SEOData(BaseSchema):
    # Catalog swagger.json

    
    description = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    sitemap = fields.Nested(Sitemap, required=False)
    
    breadcrumbs = fields.List(fields.Nested(ApplicationItemSeoBreadcrumbs, required=False), required=False)
    
    meta_tags = fields.List(fields.Nested(Metatags, required=False), required=False)
    
    canonical_url = fields.Str(required=False)
    


class SearchKeywordResult(BaseSchema):
    # Catalog swagger.json

    
    query = fields.Dict(required=False)
    
    sort_on = fields.Str(required=False)
    


class SearchableAttribute(BaseSchema):
    # Catalog swagger.json

    
    key = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    priority = fields.Float(required=False)
    


class SecondLevelChild(BaseSchema):
    # Catalog swagger.json

    
    _custom_json = fields.Dict(required=False)
    
    action = fields.Nested(Action, required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    childs = fields.List(fields.Nested(ThirdLevelChild, required=False), required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    


class SellerPhoneNumber(BaseSchema):
    # Catalog swagger.json

    
    country_code = fields.Int(required=False)
    
    number = fields.Str(required=False)
    


class CollectionSeoDetail(BaseSchema):
    # Catalog swagger.json

    
    description = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    sitemap = fields.Nested(Sitemap, required=False)
    
    breadcrumbs = fields.List(fields.Nested(ApplicationCollectionItemSeoBreadcrumbs, required=False), required=False)
    
    meta_tags = fields.List(fields.Nested(Metatags, required=False), required=False)
    
    canonical_url = fields.Str(required=False)
    


class SeoDetail(BaseSchema):
    # Catalog swagger.json

    
    description = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    sitemap = fields.Nested(Sitemap, required=False)
    
    breadcrumbs = fields.List(fields.Nested(ApplicationItemSeoBreadcrumbs, required=False), required=False)
    
    meta_tags = fields.List(fields.Nested(Metatags, required=False), required=False)
    
    canonical_url = fields.Str(required=False)
    


class SetSize(BaseSchema):
    # Catalog swagger.json

    
    pieces = fields.Int(required=False)
    
    size = fields.Str(required=False)
    


class SingleCategoryResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    data = fields.Nested(Category, required=False)
    


class VariantTypesResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(VariantTypeItem, required=False), required=False)
    


class VariantTypeItem(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
    type = fields.List(fields.Str(required=False), required=False)
    
    image_config = fields.Dict(required=False, allow_none=True)
    


class SingleProductResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    data = fields.Nested(ProductSchemaV2, required=False)
    


class Size(BaseSchema):
    # Catalog swagger.json

    
    display = fields.Str(required=False)
    
    is_available = fields.Boolean(required=False)
    
    quantity = fields.Int(required=False)
    
    value = fields.Str(required=False)
    


class SizeDistribution(BaseSchema):
    # Catalog swagger.json

    
    sizes = fields.List(fields.Nested(SetSize, required=False), required=False)
    


class SizeGuideItem(BaseSchema):
    # Catalog swagger.json

    
    active = fields.Boolean(required=False)
    
    brand_id = fields.Int(required=False)
    
    company_id = fields.Int(required=False)
    
    created_by = fields.Nested(UserInfo, required=False)
    
    created_on = fields.Str(required=False)
    
    guide = fields.Nested(Guide, required=False)
    
    id = fields.Str(required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    modified_on = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    subtitle = fields.Str(required=False)
    
    tag = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    image = fields.Str(required=False)
    


class SizeGuideResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    active = fields.Boolean(required=False)
    
    brand_id = fields.Int(required=False)
    
    company_id = fields.Int(required=False)
    
    created_by = fields.Nested(UserInfo, required=False)
    
    created_on = fields.Str(required=False)
    
    guide = fields.Dict(required=False)
    
    id = fields.Str(required=False)
    
    image = fields.Str(required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    modified_on = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    subtitle = fields.Str(required=False)
    
    tag = fields.Str(required=False)
    
    title = fields.Str(required=False)
    


class Time(BaseSchema):
    # Catalog swagger.json

    
    hour = fields.Int(required=False)
    
    minute = fields.Int(required=False)
    


class Timing(BaseSchema):
    # Catalog swagger.json

    
    closing = fields.Nested(Time, required=False)
    
    weekday = fields.Str(required=False)
    
    opening = fields.Nested(Time, required=False)
    
    open = fields.Boolean(required=False)
    


class UserSchemaCustom(BaseSchema):
    # Catalog swagger.json

    
    user_id = fields.Str(required=False)
    
    username = fields.Str(required=False)
    


class Manager(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    mobile_no = fields.Nested(MobileNo, required=False)
    


class MobileNo(BaseSchema):
    # Catalog swagger.json

    
    country_code = fields.Int(required=False)
    
    number = fields.Str(required=False)
    


class IntegrationType(BaseSchema):
    # Catalog swagger.json

    
    order = fields.Str(required=False)
    
    inventory = fields.Str(required=False)
    


class Address(BaseSchema):
    # Catalog swagger.json

    
    country_code = fields.Str(required=False)
    
    address1 = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    address2 = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    
    landmark = fields.Str(required=False)
    
    state = fields.Str(required=False)
    


class StoreDetail(BaseSchema):
    # Catalog swagger.json

    
    additional_contacts = fields.List(fields.Dict(required=False), required=False)
    
    company_id = fields.Int(required=False)
    
    created_on = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    store_code = fields.Str(required=False)
    
    store_type = fields.Str(required=False)
    
    timing = fields.List(fields.Nested(Timing, required=False), required=False)
    
    uid = fields.Int(required=False)
    
    stage = fields.Str(required=False)
    
    modified_by = fields.Nested(UserSchemaCustom, required=False)
    
    manager = fields.Nested(Manager, required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    verified_on = fields.Str(required=False)
    
    verified_by = fields.Nested(UserSchemaCustom, required=False)
    
    integration_type = fields.Nested(IntegrationType, required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    address = fields.Nested(Address, required=False)
    
    created_by = fields.Nested(UserSchemaCustom, required=False)
    
    _custom_json = fields.Dict(required=False)
    


class StoreMeta(BaseSchema):
    # Catalog swagger.json

    
    id = fields.Int(required=False)
    


class SuccessResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    success = fields.Boolean(required=False)
    
    uid = fields.Int(required=False)
    


class TaxIdentifier(BaseSchema):
    # Catalog swagger.json

    
    hsn_code = fields.Str(required=False)
    
    hsn_code_id = fields.Str(required=False)
    
    reporting_hsn = fields.Str(required=False)
    


class TaxSlab(BaseSchema):
    # Catalog swagger.json

    
    cess = fields.Float(required=False)
    
    effective_date = fields.Str(required=False)
    
    rate = fields.Float(required=False)
    
    threshold = fields.Float(required=False)
    


class TeaserTag(BaseSchema):
    # Catalog swagger.json

    
    tag = fields.Str(required=False, allow_none=True)
    
    url = fields.Str(required=False, allow_none=True)
    


class TemplateDetails(BaseSchema):
    # Catalog swagger.json

    
    attributes = fields.List(fields.Str(required=False), required=False)
    
    categories = fields.List(fields.Str(required=False), required=False)
    
    departments = fields.List(fields.Str(required=False), required=False)
    
    description = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    is_archived = fields.Boolean(required=False)
    
    is_expirable = fields.Boolean(required=False)
    
    is_physical = fields.Boolean(required=False)
    
    logo = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    tag = fields.Str(required=False)
    


class TemplateGlobalValidationData(BaseSchema):
    # Catalog swagger.json

    
    global_validation = fields.Nested(GlobalValidation, required=False)
    


class TemplateValidationData(BaseSchema):
    # Catalog swagger.json

    
    global_validation = fields.Nested(GlobalValidation, required=False)
    
    template_validation = fields.Dict(required=False)
    


class TemplatesResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(ProductTemplate, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class TemplatesGlobalValidationResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    data = fields.Nested(TemplateGlobalValidationData, required=False)
    


class ThirdLevelChild(BaseSchema):
    # Catalog swagger.json

    
    _custom_json = fields.Dict(required=False)
    
    action = fields.Nested(Action, required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    childs = fields.List(fields.Dict(required=False), required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    


class Trader(BaseSchema):
    # Catalog swagger.json

    
    address = fields.List(fields.Str(required=False), required=False)
    
    name = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class Trader1(BaseSchema):
    # Catalog swagger.json

    
    address = fields.List(fields.Str(required=False), required=False)
    
    name = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class UpdateCollection(BaseSchema):
    # Catalog swagger.json

    
    action = fields.Nested(Action, required=False)
    
    uid = fields.Str(required=False)
    
    app_id = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    _locale_language = fields.Dict(required=False)
    
    _schedule = fields.Nested(CollectionSchedule, required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    badge = fields.Nested(CollectionBadge, required=False)
    
    banners = fields.Nested(CollectionBanner, required=False)
    
    description = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    is_visible = fields.Boolean(required=False)
    
    logo = fields.Nested(CollectionImage, required=False)
    
    meta = fields.Dict(required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    name = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    
    published = fields.Boolean(required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
    seo = fields.Nested(CollectionSeoDetail, required=False)
    
    slug = fields.Str(required=False)
    
    sort_on = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    is_searchable = fields.Boolean(required=False)
    


class UpdateSearchConfigurationRequestSchema(BaseSchema):
    # Catalog swagger.json

    
    application_id = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    created_by = fields.Nested(UserInfo, required=False)
    
    created_on = fields.Str(required=False)
    
    is_proximity_enabled = fields.Boolean(required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    modified_on = fields.Str(required=False)
    
    proximity = fields.Int(required=False)
    
    searchable_attributes = fields.List(fields.Nested(SearchableAttribute, required=False), required=False)
    


class UpdateSearchConfigurationResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    success = fields.Boolean(required=False)
    


class UpdatedResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    items_not_updated = fields.List(fields.Int(required=False), required=False)
    
    message = fields.Str(required=False)
    


class UserCommon(BaseSchema):
    # Catalog swagger.json

    
    company_id = fields.Int(required=False)
    
    user_id = fields.Str(required=False)
    
    username = fields.Str(required=False)
    


class UserDetail(BaseSchema):
    # Catalog swagger.json

    
    contact = fields.Str(required=False)
    
    super_user = fields.Boolean(required=False)
    
    user_id = fields.Str(required=False)
    
    username = fields.Str(required=False)
    


class UserDetail1(BaseSchema):
    # Catalog swagger.json

    
    full_name = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
    username = fields.Str(required=False)
    


class UserInfo(BaseSchema):
    # Catalog swagger.json

    
    email = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
    username = fields.Str(required=False)
    


class UserSchema(BaseSchema):
    # Catalog swagger.json

    
    _id = fields.Str(required=False)
    
    contact = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
    username = fields.Str(required=False)
    


class ValidateIdentifier(BaseSchema):
    # Catalog swagger.json

    
    gtin_type = fields.Str(required=False)
    
    gtin_value = fields.Str(required=False)
    
    primary = fields.Boolean(required=False)
    


class ValidateProduct(BaseSchema):
    # Catalog swagger.json

    
    valid = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class ValidateSizeGuide(BaseSchema):
    # Catalog swagger.json

    
    active = fields.Boolean(required=False)
    
    brand_id = fields.Int(required=False)
    
    company_id = fields.Str(required=False)
    
    created_by = fields.Dict(required=False)
    
    created_on = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    guide = fields.Nested(Guide, required=False)
    
    id = fields.Str(required=False)
    
    image = fields.Str(required=False)
    
    modified_by = fields.Dict(required=False)
    
    modified_on = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    subtitle = fields.Str(required=False)
    
    tag = fields.Str(required=False)
    
    title = fields.Str(required=False)
    


class VerifiedBy(BaseSchema):
    # Catalog swagger.json

    
    user_id = fields.Str(required=False)
    
    username = fields.Str(required=False)
    


class WeightResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    is_default = fields.Boolean(required=False)
    
    shipping = fields.Float(required=False)
    
    unit = fields.Str(required=False)
    


class WeightResponseSchema1(BaseSchema):
    # Catalog swagger.json

    
    shipping = fields.Float(required=False)
    
    unit = fields.Str(required=False)
    


class Marketplaces(BaseSchema):
    # Catalog swagger.json

    
    brand_ids = fields.List(fields.Int(required=False), required=False)
    
    app_id = fields.Str(required=False)
    
    enabled = fields.Boolean(required=False)
    
    created_by = fields.Nested(UserInfo, required=False)
    
    created_on = fields.Str(required=False)
    
    opt_level = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    store_ids = fields.List(fields.Int(required=False), required=False)
    
    modified_on = fields.Str(required=False)
    
    platforms = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    


class GetAllMarketplaces(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(Marketplaces, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class CreateMarketplaceOptinRequestSchema(BaseSchema):
    # Catalog swagger.json

    
    brand_ids = fields.List(fields.Int(required=False), required=False)
    
    company_id = fields.Int(required=False)
    
    enabled = fields.Boolean(required=False)
    
    opt_level = fields.Str(required=False)
    
    platform = fields.Str(required=False)
    
    store_ids = fields.List(fields.Int(required=False), required=False)
    


class UpdateMarketplaceOptinRequestSchema(BaseSchema):
    # Catalog swagger.json

    
    brand_ids = fields.List(fields.Int(required=False), required=False)
    
    company_id = fields.Int(required=False)
    
    enabled = fields.Boolean(required=False)
    
    opt_level = fields.Str(required=False)
    
    platform = fields.Str(required=False)
    
    store_ids = fields.List(fields.Int(required=False), required=False)
    


class CreateMarketplaceOptinResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    store_ids = fields.List(fields.Int(required=False), required=False)
    
    brand_ids = fields.List(fields.Int(required=False), required=False)
    
    company_id = fields.Int(required=False)
    
    opt_level = fields.Str(required=False)
    
    platform = fields.Str(required=False)
    
    enabled = fields.Boolean(required=False)
    
    created_by = fields.Nested(UserInfo, required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    app_id = fields.Str(required=False)
    


class GetProductTemplateSlugItemsSchema(BaseSchema):
    # Catalog swagger.json

    
    attributes = fields.List(fields.Str(required=False), required=False)
    
    departments = fields.List(fields.Str(required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    tag = fields.Str(required=False)
    
    is_physical = fields.Boolean(required=False)
    
    description = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    is_archived = fields.Boolean(required=False)
    
    slug = fields.Str(required=False)
    
    categories = fields.List(fields.Str(required=False), required=False)
    
    is_expirable = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    id = fields.Str(required=False)
    


class GetProductTemplateSlugResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(GetProductTemplateSlugItemsSchema, required=False), required=False)
    


class UpdateMarketplaceOptinResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    brand_ids = fields.List(fields.Int(required=False), required=False)
    
    company_id = fields.Int(required=False)
    
    app_id = fields.Str(required=False)
    
    enabled = fields.Boolean(required=False)
    
    opt_level = fields.Str(required=False)
    
    platform = fields.Str(required=False)
    
    store_ids = fields.List(fields.Int(required=False), required=False)
    
    created_by = fields.Nested(UserInfo, required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    


class AutocompleteRequestSchema(BaseSchema):
    # Catalog swagger.json

    
    query_suggestion = fields.Dict(required=False)
    
    product_suggestion = fields.Dict(required=False)
    
    collection_suggestion = fields.Dict(required=False)
    
    brand_suggestion = fields.Dict(required=False)
    
    category_suggestion = fields.Dict(required=False)
    


class AutocompleteUpsertResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    message = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class AutocompleteErrorResponseSchemaSchema(BaseSchema):
    # Catalog swagger.json

    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class AutocompleteResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    id = fields.Str(required=False)
    
    query_suggestion = fields.Dict(required=False)
    
    product_suggestion = fields.Dict(required=False)
    
    collection_suggestion = fields.Dict(required=False)
    
    brand_suggestion = fields.Dict(required=False)
    
    category_suggestion = fields.Dict(required=False)
    


class ProductListingActionPage(BaseSchema):
    # Catalog swagger.json

    
    type = fields.Str(required=False)
    
    query = fields.Dict(required=False)
    
    params = fields.Dict(required=False)
    


class ProductListingAction(BaseSchema):
    # Catalog swagger.json

    
    type = fields.Str(required=False)
    
    page = fields.Nested(ProductListingActionPage, required=False)
    


class AutocompleteItem(BaseSchema):
    # Catalog swagger.json

    
    logo = fields.Nested(Media, required=False)
    
    display = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    


class AutocompletePreviewResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(AutocompleteItem, required=False), required=False)
    


class CreateAppPriceFactoryRequestSchema(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    factory_type_ids = fields.List(fields.Str(required=False), required=False)
    
    department_ids = fields.List(fields.Int(required=False), required=False)
    
    application_id = fields.Str(required=False)
    
    factory_type = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    currency_symbol = fields.Str(required=False)
    


class CreateAppPriceFactoryResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    factory_type = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    code = fields.Str(required=False)
    
    factory_type_ids = fields.List(fields.Str(required=False), required=False)
    
    currency = fields.Str(required=False)
    
    application_id = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    created_by = fields.Nested(UserInfo, required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    name = fields.Str(required=False)
    
    department_ids = fields.List(fields.Int(required=False), required=False)
    
    modified_on = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    


class AppPriceFactory(BaseSchema):
    # Catalog swagger.json

    
    _id = fields.Str(required=False)
    
    application_id = fields.Str(required=False)
    
    department_ids = fields.List(fields.Int(required=False), required=False)
    
    factory_type = fields.Str(required=False)
    
    factory_type_ids = fields.List(fields.Str(required=False), required=False)
    
    code = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    currency = fields.Str(required=False)
    
    created_by = fields.Nested(UserInfo, required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    


class EditAppPriceFactoryRequestSchema(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    factory_type_ids = fields.List(fields.Str(required=False), required=False)
    
    department_ids = fields.List(fields.Int(required=False), required=False)
    
    application_id = fields.Str(required=False)
    
    factory_type = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    currency_symbol = fields.Str(required=False)
    


class GetAppPriceFactoryResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(AppPriceFactory, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class CreateAppPriceFactoryProduct(BaseSchema):
    # Catalog swagger.json

    
    item_id = fields.Int(required=False)
    
    marked_price = fields.Float(required=False)
    
    selling_price = fields.Float(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    zone = fields.Str(required=False)
    
    action = fields.Str(required=False)
    


class PriceFactorySizes(BaseSchema):
    # Catalog swagger.json

    
    size_name = fields.Str(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    marked_price = fields.Float(required=False)
    
    selling_price = fields.Float(required=False)
    
    currency = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    


class CompanySizes(BaseSchema):
    # Catalog swagger.json

    
    size_name = fields.Str(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    marked_price = fields.Float(required=False)
    
    selling_price = fields.Float(required=False)
    
    currency = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    


class CreateAppPriceFactoryProductItem(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    item_id = fields.Int(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    marked_price = fields.Float(required=False)
    
    selling_price = fields.Float(required=False)
    
    zone = fields.Str(required=False)
    
    command = fields.Str(required=False)
    


class CreatePriceFactoryProductRequestSchema(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(CreateAppPriceFactoryProductItem, required=False), required=False)
    


class CreateAppPriceFactoryProductResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    item_id = fields.Int(required=False)
    
    item_name = fields.Str(required=False)
    
    item_code = fields.Str(required=False)
    
    brand = fields.Str(required=False)
    
    category = fields.Str(required=False)
    
    factory_type_id = fields.List(fields.Str(required=False), required=False)
    
    media = fields.List(fields.Nested(Media, required=False), required=False)
    
    sizes = fields.List(fields.Nested(PriceFactorySizes, required=False), required=False)
    
    company_sizes = fields.List(fields.Nested(CompanySizes, required=False), required=False)
    


class FailedRecordsData(BaseSchema):
    # Catalog swagger.json

    
    item_id = fields.Int(required=False)
    
    error = fields.Str(required=False)
    


class CreatePriceFactoryProductResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    total_records = fields.Int(required=False)
    
    success_records = fields.Int(required=False)
    
    failed_records = fields.Int(required=False)
    
    failed_records_data = fields.List(fields.Nested(FailedRecordsData, required=False), required=False)
    
    stage = fields.Str(required=False)
    


class CreateAppPriceFactoryProductsResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(CreateAppPriceFactoryProductResponseSchema, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class CreateAppPriceFactoryProductBulkJobRequestSchema(BaseSchema):
    # Catalog swagger.json

    
    file_path = fields.Str(required=False)
    
    file_type = fields.Str(required=False)
    
    job_type = fields.Str(required=False)
    


class CreateAppPriceFactoryProductExportJobRequestSchema(BaseSchema):
    # Catalog swagger.json

    
    sample_with_data = fields.Boolean(required=False)
    


class CreateAppPriceFactoryProductExportJobResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    job_type = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    file_type = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    created_by = fields.Nested(UserInfo, required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    success_records = fields.Int(required=False)
    
    application_id = fields.Str(required=False)
    
    total_records = fields.Int(required=False)
    
    factory_id = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    stage = fields.Str(required=False)
    
    failed_records = fields.Int(required=False)
    


class AppPriceFactoryProductExportPollJobResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    id = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    created_on = fields.Str(required=False)
    
    total_records = fields.Int(required=False)
    
    success_records = fields.Int(required=False)
    
    failed_records = fields.Int(required=False)
    
    job_type = fields.Str(required=False)
    


class CreateAppPriceFactoryProductExportJobPollResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(AppPriceFactoryProductExportPollJobResponseSchema, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class CreateAppPriceFactoryProductBulkJobResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    job_id = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    file_type = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    created_by = fields.Nested(UserInfo, required=False)
    
    company_id = fields.Int(required=False)
    
    job_type = fields.Str(required=False)
    
    total_records = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    modified_on = fields.Str(required=False)
    
    application_id = fields.Str(required=False)
    
    factory_id = fields.Str(required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    created_on = fields.Str(required=False)
    
    failed_records = fields.Int(required=False)
    
    file_path = fields.Str(required=False)
    
    success_records = fields.Int(required=False)
    
    _id = fields.Str(required=False)
    


class CreateAppPriceFactoryProductBulkJobValidateResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    job_type = fields.Str(required=False)
    
    file_type = fields.Str(required=False)
    
    file_path = fields.Str(required=False)
    
    job_id = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    created_by = fields.Nested(UserInfo, required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    


class CreateAppPriceFactoryProductBulkJobPollResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    status = fields.Str(required=False)
    
    total_records = fields.Int(required=False)
    
    success_records = fields.Int(required=False)
    
    failed_records = fields.Int(required=False)
    
    error_file = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    created_by = fields.Nested(UserInfo, required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    stage = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    _id = fields.Str(required=False)
    
    error_file_url = fields.Str(required=False, allow_none=True)
    


class SynonymListResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(SynonymResponseSchema, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class SynonymResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    created_on = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    synonyms = fields.List(fields.Str(required=False), required=False)
    
    key = fields.Str(required=False)
    
    app_id = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    


class SynonymListErrorResponseSchemaSchema(BaseSchema):
    # Catalog swagger.json

    
    message = fields.Str(required=False)
    
    error = fields.Str(required=False)
    


class SynonymCreateRequestSchema(BaseSchema):
    # Catalog swagger.json

    
    type = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
    synonyms = fields.List(fields.Str(required=False), required=False)
    


class SynonymCreateResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    status = fields.Boolean(required=False)
    
    _id = fields.Str(required=False)
    
    message = fields.Str(required=False)
    


class SynonymUpdateResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class SynonymCreateErrorSchema(BaseSchema):
    # Catalog swagger.json

    
    message = fields.Str(required=False)
    
    errors = fields.Dict(required=False)
    
    code = fields.Int(required=False)
    


class SynonymDeleteResponseSchemaSchema(BaseSchema):
    # Catalog swagger.json

    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class SynonymUploadRequestSchema(BaseSchema):
    # Catalog swagger.json

    
    tracking_url = fields.Str(required=False)
    
    file_type = fields.Str(required=False)
    
    job_type = fields.Str(required=False)
    


class SynonymUploadResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    job_type = fields.Str(required=False)
    
    file_type = fields.Str(required=False)
    
    tracking_url = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    total_records = fields.Int(required=False)
    
    success_records = fields.Int(required=False)
    
    failed_records = fields.Int(required=False)
    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    id = fields.Str(required=False)
    


class SynonymExportResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    job_type = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    application_id = fields.Str(required=False)
    


class SynonymUploadErrorSchema(BaseSchema):
    # Catalog swagger.json

    
    message = fields.Str(required=False)
    
    errors = fields.Dict(required=False)
    
    code = fields.Int(required=False)
    


class SynonymBulkValidateRequestSchema(BaseSchema):
    # Catalog swagger.json

    
    job_id = fields.Str(required=False)
    
    tracking_url = fields.Str(required=False)
    
    file_type = fields.Str(required=False)
    
    job_type = fields.Str(required=False)
    


class SynonymBulkValidateResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    job_id = fields.Str(required=False)
    
    message = fields.Str(required=False)
    


class SynonymBulkValidateErrorSchema(BaseSchema):
    # Catalog swagger.json

    
    message = fields.Str(required=False)
    
    errors = fields.Dict(required=False)
    
    code = fields.Int(required=False)
    


class SynonymBulkProcessRequestSchema(BaseSchema):
    # Catalog swagger.json

    
    job_id = fields.Str(required=False)
    
    tracking_url = fields.Str(required=False)
    
    file_type = fields.Str(required=False)
    
    job_type = fields.Str(required=False)
    


class SynonymBulkProcessResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    job_id = fields.Str(required=False)
    
    message = fields.Str(required=False)
    


class SynonymBulkProcessErrorSchema(BaseSchema):
    # Catalog swagger.json

    
    message = fields.Str(required=False)
    
    errors = fields.Str(required=False)
    
    code = fields.Int(required=False)
    


class SynonymBulkPollResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    total_records = fields.Int(required=False)
    
    success_records = fields.Int(required=False)
    
    failed_records = fields.Int(required=False)
    
    stage = fields.Str(required=False)
    
    error_url = fields.Str(required=False)
    
    message = fields.Str(required=False)
    


class SynonymBulkPollErrorSchema(BaseSchema):
    # Catalog swagger.json

    
    message = fields.Str(required=False)
    
    error = fields.Str(required=False)
    


class PriceFactoryCreateErrorSchema(BaseSchema):
    # Catalog swagger.json

    
    message = fields.Str(required=False)
    
    error = fields.Dict(required=False)
    
    code = fields.Int(required=False)
    


class PriceGroupedByZone(BaseSchema):
    # Catalog swagger.json

    
    discount = fields.Str(required=False)
    
    store_id = fields.List(fields.Int(required=False), required=False)
    
    seller_id = fields.Int(required=False)
    
    factory_type_id = fields.Str(required=False)
    
    discount_meta = fields.Nested(DiscountMeta, required=False)
    
    price = fields.Nested(ProductListingPrice, required=False)
    


class AppPriceByIdResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    data = fields.List(fields.Nested(PriceGroupedByZone, required=False), required=False)
    


class TemplatesValidationResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    data = fields.Nested(TemplateValidationData, required=False)
    
    template_details = fields.Nested(TemplateDetails, required=False)
    


class ActionPage(BaseSchema):
    # Catalog swagger.json

    
    params = fields.Dict(required=False)
    
    query = fields.Dict(required=False)
    
    url = fields.Str(required=False)
    
    type = fields.Str(required=False, validate=OneOf([val.value for val in PageType.__members__.values()]))
    


class Price1(BaseSchema):
    # Catalog swagger.json

    
    currency_code = fields.Str(required=False, validate=OneOf([val.value for val in CurrencyCodeEnum.__members__.values()]))
    
    currency_symbol = fields.Str(required=False)
    
    max = fields.Float(required=False)
    
    min = fields.Float(required=False)
    


class MultiCategoriesSchema(BaseSchema):
    # Catalog swagger.json

    
    l1 = fields.Int(required=False)
    
    l2 = fields.Int(required=False)
    
    l3 = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    department = fields.Int(required=False)
    


class CustomMeta(BaseSchema):
    # Catalog swagger.json

    
    key = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class ValidationErrors(BaseSchema):
    # Catalog swagger.json

    
    errors = fields.List(fields.Nested(ValidationError, required=False), required=False)
    


class ValidationError(BaseSchema):
    # Catalog swagger.json

    
    message = fields.Str(required=False)
    
    field = fields.Str(required=False)
    


