"""Catalog Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf


from ..PlatformModel import BaseSchema



from .enums import *



class DeleteResponse(BaseSchema):
    pass


class ErrorResponse(BaseSchema):
    pass


class Page(BaseSchema):
    pass


class GetSearchWordsData(BaseSchema):
    pass


class GetSearchWordsDetailResponse(BaseSchema):
    pass


class SearchKeywordResult(BaseSchema):
    pass


class CreateSearchKeyword(BaseSchema):
    pass


class GetSearchWordsResponse(BaseSchema):
    pass


class GetAutocompleteWordsData(BaseSchema):
    pass


class GetAutocompleteWordsResponse(BaseSchema):
    pass


class Media(BaseSchema):
    pass


class AutocompletePageAction(BaseSchema):
    pass


class AutocompleteAction(BaseSchema):
    pass


class AutocompleteResult(BaseSchema):
    pass


class CreateAutocompleteKeyword(BaseSchema):
    pass


class CreateAutocompleteWordsResponse(BaseSchema):
    pass


class ProductBundleItem(BaseSchema):
    pass


class GetProductBundleCreateResponse(BaseSchema):
    pass


class GetProductBundleListingResponse(BaseSchema):
    pass


class ProductBundleRequest(BaseSchema):
    pass


class Size(BaseSchema):
    pass


class LimitedProductData(BaseSchema):
    pass


class Price(BaseSchema):
    pass


class GetProducts(BaseSchema):
    pass


class GetProductBundleResponse(BaseSchema):
    pass


class ProductBundleUpdateRequest(BaseSchema):
    pass


class ListSizeGuide(BaseSchema):
    pass


class Meta(BaseSchema):
    pass


class Guide(BaseSchema):
    pass


class ValidateSizeGuide(BaseSchema):
    pass


class SuccessResponse(BaseSchema):
    pass


class SizeGuideResponse(BaseSchema):
    pass


class MOQData(BaseSchema):
    pass


class SEOData(BaseSchema):
    pass


class OwnerAppItemResponse(BaseSchema):
    pass


class MetaFields(BaseSchema):
    pass


class ApplicationItemMOQ(BaseSchema):
    pass


class ApplicationItemSEO(BaseSchema):
    pass


class ApplicationItemMeta(BaseSchema):
    pass


class SuccessResponse1(BaseSchema):
    pass


class GetConfigMetadataResponse(BaseSchema):
    pass


class PageResponseType(BaseSchema):
    pass


class GetConfigResponse(BaseSchema):
    pass


class ConfigErrorResponse(BaseSchema):
    pass


class AttributeDetailsGroup(BaseSchema):
    pass


class AppConfigurationDetail(BaseSchema):
    pass


class ConfigSuccessResponse(BaseSchema):
    pass


class AppConfigurationsSort(BaseSchema):
    pass


class AllowSingleRequest(BaseSchema):
    pass


class DefaultKeyRequest(BaseSchema):
    pass


class MetaDataListingSortMetaResponse(BaseSchema):
    pass


class MetaDataListingSortResponse(BaseSchema):
    pass


class MetaDataListingFilterMetaResponse(BaseSchema):
    pass


class MetaDataListingFilterResponse(BaseSchema):
    pass


class MetaDataListingResponse(BaseSchema):
    pass


class GetCatalogConfigurationDetailsProduct(BaseSchema):
    pass


class GetCatalogConfigurationMetaData(BaseSchema):
    pass


class ConfigurationListingSortConfig(BaseSchema):
    pass


class ConfigurationListingSort(BaseSchema):
    pass


class ConfigurationBucketPoints(BaseSchema):
    pass


class ConfigurationListingFilterValue(BaseSchema):
    pass


class ConfigurationListingFilterConfig(BaseSchema):
    pass


class ConfigurationListingFilter(BaseSchema):
    pass


class ConfigurationListing(BaseSchema):
    pass


class ProductSize(BaseSchema):
    pass


class ConfigurationProductConfig(BaseSchema):
    pass


class ConfigurationProductSimilar(BaseSchema):
    pass


class ConfigurationProductVariantConfig(BaseSchema):
    pass


class ConfigurationProductVariant(BaseSchema):
    pass


class ConfigurationProduct(BaseSchema):
    pass


class AppCatalogConfiguration(BaseSchema):
    pass


class GetAppCatalogConfiguration(BaseSchema):
    pass


class AppConfiguration(BaseSchema):
    pass


class GetCatalogConfigurationDetailsSchemaListing(BaseSchema):
    pass


class EntityConfiguration(BaseSchema):
    pass


class GetAppCatalogEntityConfiguration(BaseSchema):
    pass


class ProductSortOn(BaseSchema):
    pass


class ProductFiltersKey(BaseSchema):
    pass


class ProductFiltersValue(BaseSchema):
    pass


class ProductFilters(BaseSchema):
    pass


class GetCollectionQueryOptionResponse(BaseSchema):
    pass


class CollectionQuery(BaseSchema):
    pass


class BannerImage(BaseSchema):
    pass


class ImageUrls(BaseSchema):
    pass


class Media1(BaseSchema):
    pass


class ActionPage(BaseSchema):
    pass


class Action(BaseSchema):
    pass


class GetCollectionDetailNest(BaseSchema):
    pass


class CollectionListingFilterType(BaseSchema):
    pass


class CollectionListingFilterTag(BaseSchema):
    pass


class CollectionListingFilter(BaseSchema):
    pass


class GetCollectionListingResponse(BaseSchema):
    pass


class SeoDetail(BaseSchema):
    pass


class UserInfo(BaseSchema):
    pass


class NextSchedule(BaseSchema):
    pass


class CollectionSchedule(BaseSchema):
    pass


class CollectionImage(BaseSchema):
    pass


class CollectionBanner(BaseSchema):
    pass


class CollectionBadge(BaseSchema):
    pass


class CreateCollection(BaseSchema):
    pass


class CollectionCreateResponse(BaseSchema):
    pass


class CollectionDetailResponse(BaseSchema):
    pass


class UpdateCollection(BaseSchema):
    pass


class ProductBrand(BaseSchema):
    pass


class Price1(BaseSchema):
    pass


class ProductListingPrice(BaseSchema):
    pass


class ProductDetailAttribute(BaseSchema):
    pass


class ProductDetailGroupedAttribute(BaseSchema):
    pass


class ProductListingDetail(BaseSchema):
    pass


class GetCollectionItemsResponse(BaseSchema):
    pass


class ItemQueryForUserCollection(BaseSchema):
    pass


class CollectionItemRequest(BaseSchema):
    pass


class UpdatedResponse(BaseSchema):
    pass


class CatalogInsightItem(BaseSchema):
    pass


class CatalogInsightBrand(BaseSchema):
    pass


class CatalogInsightResponse(BaseSchema):
    pass


class CrossSellingData(BaseSchema):
    pass


class CrossSellingResponse(BaseSchema):
    pass


class OptInPostRequest(BaseSchema):
    pass


class CompanyOptIn(BaseSchema):
    pass


class GetOptInPlatform(BaseSchema):
    pass


class OptinCompanyDetail(BaseSchema):
    pass


class CompanyBrandDetail(BaseSchema):
    pass


class OptinCompanyBrandDetailsView(BaseSchema):
    pass


class OptinCompanyMetrics(BaseSchema):
    pass


class StoreDetail(BaseSchema):
    pass


class OptinStoreDetails(BaseSchema):
    pass


class AttributeMasterMandatoryDetails(BaseSchema):
    pass


class AttributeMasterMeta(BaseSchema):
    pass


class AttributeMasterDetails(BaseSchema):
    pass


class AttributeMasterFilter(BaseSchema):
    pass


class AttributeSchemaRange(BaseSchema):
    pass


class AttributeMaster(BaseSchema):
    pass


class GenderDetail(BaseSchema):
    pass


class ProductTemplateCategory(BaseSchema):
    pass


class ProdcutTemplateCategoriesResponse(BaseSchema):
    pass


class PTErrorResponse(BaseSchema):
    pass


class UserSerializer(BaseSchema):
    pass


class GetDepartment(BaseSchema):
    pass


class DepartmentsResponse(BaseSchema):
    pass


class DepartmentErrorResponse(BaseSchema):
    pass


class DepartmentCreateUpdate(BaseSchema):
    pass


class DepartmentCreateResponse(BaseSchema):
    pass


class DepartmentCreateErrorResponse(BaseSchema):
    pass


class UserDetail(BaseSchema):
    pass


class DepartmentModel(BaseSchema):
    pass


class ProductTemplate(BaseSchema):
    pass


class TemplatesResponse(BaseSchema):
    pass


class TemplateDetails(BaseSchema):
    pass


class Properties(BaseSchema):
    pass


class GlobalValidation(BaseSchema):
    pass


class TemplateValidationData(BaseSchema):
    pass


class TemplatesValidationResponse(BaseSchema):
    pass


class InventoryValidationResponse(BaseSchema):
    pass


class HSNData(BaseSchema):
    pass


class HSNCodesResponse(BaseSchema):
    pass


class UserInfo1(BaseSchema):
    pass


class ProductTemplateExportResponse(BaseSchema):
    pass


class ProductDownloadsResponse(BaseSchema):
    pass


class ProductTemplateExportFilterRequest(BaseSchema):
    pass


class ProductTemplateDownloadsExport(BaseSchema):
    pass


class ProductPartialExportRequest(BaseSchema):
    pass


class ProductConfigurationDownloads(BaseSchema):
    pass


class Media2(BaseSchema):
    pass


class Hierarchy(BaseSchema):
    pass


class CategoryMappingValues(BaseSchema):
    pass


class CategoryMapping(BaseSchema):
    pass


class Category(BaseSchema):
    pass


class CategoryResponse(BaseSchema):
    pass


class CategoryRequestBody(BaseSchema):
    pass


class CategoryCreateResponse(BaseSchema):
    pass


class SingleCategoryResponse(BaseSchema):
    pass


class CategoryUpdateResponse(BaseSchema):
    pass


class Trader(BaseSchema):
    pass


class VerifiedBy(BaseSchema):
    pass


class Image(BaseSchema):
    pass


class ReturnConfigResponse(BaseSchema):
    pass


class Logo(BaseSchema):
    pass


class Brand(BaseSchema):
    pass


class NetQuantityResponse(BaseSchema):
    pass


class ProductPublish(BaseSchema):
    pass


class ProductSchemaV2(BaseSchema):
    pass


class ProductListingResponseV2(BaseSchema):
    pass


class CustomOrder(BaseSchema):
    pass


class ReturnConfig(BaseSchema):
    pass


class NetQuantity(BaseSchema):
    pass


class TaxIdentifier(BaseSchema):
    pass


class TeaserTag(BaseSchema):
    pass


class ProductPublish1(BaseSchema):
    pass


class ProductCreateUpdateSchemaV2(BaseSchema):
    pass


class ProductVariants(BaseSchema):
    pass


class ProductVariantsResponse(BaseSchema):
    pass


class AttributeMasterSerializer(BaseSchema):
    pass


class ProductAttributesResponse(BaseSchema):
    pass


class SingleProductResponse(BaseSchema):
    pass


class ValidateIdentifier(BaseSchema):
    pass


class AllSizes(BaseSchema):
    pass


class GetAllSizes(BaseSchema):
    pass


class ValidateProduct(BaseSchema):
    pass


class ProductPublished(BaseSchema):
    pass


class Product(BaseSchema):
    pass


class ProductListingResponse(BaseSchema):
    pass


class UserDetail1(BaseSchema):
    pass


class ProductBulkRequest(BaseSchema):
    pass


class ProductBulkRequestList(BaseSchema):
    pass


class BulkJob(BaseSchema):
    pass


class BulkResponse(BaseSchema):
    pass


class BulkProductRequest(BaseSchema):
    pass


class ProductTagsViewResponse(BaseSchema):
    pass


class UserCommon(BaseSchema):
    pass


class Items(BaseSchema):
    pass


class BulkAssetResponse(BaseSchema):
    pass


class ProductBulkAssets(BaseSchema):
    pass


class ProductSizeDeleteDataResponse(BaseSchema):
    pass


class ProductSizeDeleteResponse(BaseSchema):
    pass


class InventoryResponse(BaseSchema):
    pass


class InventoryResponsePaginated(BaseSchema):
    pass


class ItemQuery(BaseSchema):
    pass


class GTIN(BaseSchema):
    pass


class SetSize(BaseSchema):
    pass


class SizeDistribution(BaseSchema):
    pass


class InventorySet(BaseSchema):
    pass


class InvSize(BaseSchema):
    pass


class InventoryRequest(BaseSchema):
    pass


class Trader1(BaseSchema):
    pass


class WeightResponse(BaseSchema):
    pass


class CompanyMeta(BaseSchema):
    pass


class ReturnConfig1(BaseSchema):
    pass


class BrandMeta(BaseSchema):
    pass


class PriceMeta(BaseSchema):
    pass


class StoreMeta(BaseSchema):
    pass


class ManufacturerResponse(BaseSchema):
    pass


class DimensionResponse(BaseSchema):
    pass


class QuantityBase(BaseSchema):
    pass


class Quantities(BaseSchema):
    pass


class InventorySellerResponse(BaseSchema):
    pass


class InventorySellerIdentifierResponsePaginated(BaseSchema):
    pass


class Trader2(BaseSchema):
    pass


class WeightResponse1(BaseSchema):
    pass


class CompanyMeta1(BaseSchema):
    pass


class ReturnConfig2(BaseSchema):
    pass


class BrandMeta1(BaseSchema):
    pass


class PriceArticle(BaseSchema):
    pass


class ArticleStoreResponse(BaseSchema):
    pass


class DateMeta(BaseSchema):
    pass


class ManufacturerResponse1(BaseSchema):
    pass


class DimensionResponse1(BaseSchema):
    pass


class Quantity(BaseSchema):
    pass


class QuantitiesArticle(BaseSchema):
    pass


class GetInventories(BaseSchema):
    pass


class GetInventoriesResponse(BaseSchema):
    pass


class BulkInventoryGetItems(BaseSchema):
    pass


class BulkInventoryGet(BaseSchema):
    pass


class InventoryJobPayload(BaseSchema):
    pass


class InventoryBulkRequest(BaseSchema):
    pass


class InventoryExportQuantityFilter(BaseSchema):
    pass


class InventoryExportAdvanceOption(BaseSchema):
    pass


class InventoryExportJob(BaseSchema):
    pass


class InventoryExportRequest(BaseSchema):
    pass


class InventoryExportResponse(BaseSchema):
    pass


class InventoryJobFilters(BaseSchema):
    pass


class InventoryJobDetailResponse(BaseSchema):
    pass


class InventoryExportJobListResponse(BaseSchema):
    pass


class InventoryExportFilter(BaseSchema):
    pass


class InventoryCreateRequest(BaseSchema):
    pass


class InventoryPartialExportRequest(BaseSchema):
    pass


class InventoryExportCreateFilters(BaseSchema):
    pass


class InventoryExportCreateResponse(BaseSchema):
    pass


class FilerList(BaseSchema):
    pass


class InventoryConfig(BaseSchema):
    pass


class InventoryPayload(BaseSchema):
    pass


class InventoryRequestSchemaV2(BaseSchema):
    pass


class InventoryFailedReason(BaseSchema):
    pass


class InventoryResponseItem(BaseSchema):
    pass


class InventoryUpdateResponse(BaseSchema):
    pass


class HsnCodesObject(BaseSchema):
    pass


class HsnCode(BaseSchema):
    pass


class HsnUpsert(BaseSchema):
    pass


class BulkHsnUpsert(BaseSchema):
    pass


class BulkHsnResponse(BaseSchema):
    pass


class PageResponse(BaseSchema):
    pass


class TaxSlab(BaseSchema):
    pass


class HSNDataInsertV2(BaseSchema):
    pass


class HsnCodesListingResponseSchemaV2(BaseSchema):
    pass


class BrandItem(BaseSchema):
    pass


class BrandListingResponse(BaseSchema):
    pass


class Department(BaseSchema):
    pass


class DepartmentResponse(BaseSchema):
    pass


class DepartmentIdentifier(BaseSchema):
    pass


class ThirdLevelChild(BaseSchema):
    pass


class SecondLevelChild(BaseSchema):
    pass


class Child(BaseSchema):
    pass


class CategoryItems(BaseSchema):
    pass


class DepartmentCategoryTree(BaseSchema):
    pass


class CategoryListingResponse(BaseSchema):
    pass


class ApplicationProductListingResponse(BaseSchema):
    pass


class ProductDetail(BaseSchema):
    pass


class InventoryPage(BaseSchema):
    pass


class InventoryStockResponse(BaseSchema):
    pass


class ArticleQuery(BaseSchema):
    pass


class ArticleAssignment(BaseSchema):
    pass


class AssignStoreArticle(BaseSchema):
    pass


class AssignStore(BaseSchema):
    pass


class ArticleAssignment1(BaseSchema):
    pass


class StoreAssignResponse(BaseSchema):
    pass


class UserSerializer1(BaseSchema):
    pass


class GetAddressSerializer(BaseSchema):
    pass


class UserSerializer2(BaseSchema):
    pass


class GetCompanySerializer(BaseSchema):
    pass


class ProductReturnConfigSerializer(BaseSchema):
    pass


class LocationIntegrationType(BaseSchema):
    pass


class SellerPhoneNumber(BaseSchema):
    pass


class LocationManagerSerializer(BaseSchema):
    pass


class InvoiceCredSerializer(BaseSchema):
    pass


class InvoiceDetailsSerializer(BaseSchema):
    pass


class Document(BaseSchema):
    pass


class LocationTimingSerializer(BaseSchema):
    pass


class LocationDayWiseSerializer(BaseSchema):
    pass


class GetLocationSerializer(BaseSchema):
    pass


class LocationListSerializer(BaseSchema):
    pass


class ApplicationBrandJson(BaseSchema):
    pass


class ApplicationCategoryJson(BaseSchema):
    pass


class ApplicationDepartment(BaseSchema):
    pass


class ApplicationDepartmentListingResponse(BaseSchema):
    pass


class ApplicationDepartmentJson(BaseSchema):
    pass


class ApplicationStoreJson(BaseSchema):
    pass





class DeleteResponse(BaseSchema):
    # Catalog swagger.json

    
    message = fields.Str(required=False)
    


class ErrorResponse(BaseSchema):
    # Catalog swagger.json

    
    message = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    status = fields.Int(required=False)
    
    code = fields.Str(required=False)
    
    error = fields.Str(required=False)
    


class Page(BaseSchema):
    # Catalog swagger.json

    
    item_total = fields.Int(required=False)
    
    next_id = fields.Str(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    has_next = fields.Boolean(required=False)
    
    current = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    size = fields.Int(required=False)
    


class GetSearchWordsData(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Str(required=False)
    
    result = fields.Dict(required=False)
    
    words = fields.List(fields.Str(required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    app_id = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    


class GetSearchWordsDetailResponse(BaseSchema):
    # Catalog swagger.json

    
    page = fields.Nested(Page, required=False)
    
    items = fields.Nested(GetSearchWordsData, required=False)
    


class SearchKeywordResult(BaseSchema):
    # Catalog swagger.json

    
    sort_on = fields.Str(required=False)
    
    query = fields.Dict(required=False)
    


class CreateSearchKeyword(BaseSchema):
    # Catalog swagger.json

    
    result = fields.Nested(SearchKeywordResult, required=False)
    
    words = fields.List(fields.Str(required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    app_id = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    


class GetSearchWordsResponse(BaseSchema):
    # Catalog swagger.json

    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(GetSearchWordsData, required=False), required=False)
    


class GetAutocompleteWordsData(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Str(required=False)
    
    words = fields.List(fields.Str(required=False), required=False)
    
    app_id = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    results = fields.List(fields.Dict(required=False), required=False)
    


class GetAutocompleteWordsResponse(BaseSchema):
    # Catalog swagger.json

    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(GetAutocompleteWordsData, required=False), required=False)
    


class Media(BaseSchema):
    # Catalog swagger.json

    
    aspect_ratio = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    url = fields.Str(required=False)
    


class AutocompletePageAction(BaseSchema):
    # Catalog swagger.json

    
    params = fields.Dict(required=False)
    
    type = fields.Str(required=False)
    
    query = fields.Dict(required=False)
    
    url = fields.Str(required=False)
    


class AutocompleteAction(BaseSchema):
    # Catalog swagger.json

    
    page = fields.Nested(AutocompletePageAction, required=False)
    
    type = fields.Str(required=False)
    


class AutocompleteResult(BaseSchema):
    # Catalog swagger.json

    
    logo = fields.Nested(Media, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    action = fields.Nested(AutocompleteAction, required=False)
    
    display = fields.Str(required=False)
    


class CreateAutocompleteKeyword(BaseSchema):
    # Catalog swagger.json

    
    words = fields.List(fields.Str(required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    app_id = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    results = fields.List(fields.Nested(AutocompleteResult, required=False), required=False)
    


class CreateAutocompleteWordsResponse(BaseSchema):
    # Catalog swagger.json

    
    words = fields.List(fields.Str(required=False), required=False)
    
    results = fields.List(fields.Dict(required=False), required=False)
    
    app_id = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    


class ProductBundleItem(BaseSchema):
    # Catalog swagger.json

    
    product_uid = fields.Int(required=False)
    
    auto_add_to_cart = fields.Boolean(required=False)
    
    auto_select = fields.Boolean(required=False)
    
    max_quantity = fields.Int(required=False)
    
    allow_remove = fields.Boolean(required=False)
    
    min_quantity = fields.Int(required=False)
    


class GetProductBundleCreateResponse(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    products = fields.List(fields.Nested(ProductBundleItem, required=False), required=False)
    
    modified_on = fields.Str(required=False)
    
    same_store_assignment = fields.Boolean(required=False)
    
    meta = fields.Dict(required=False)
    
    page_visibility = fields.List(fields.Str(required=False), required=False)
    
    choice = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    created_by = fields.Dict(required=False)
    
    logo = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    modified_by = fields.Dict(required=False)
    


class GetProductBundleListingResponse(BaseSchema):
    # Catalog swagger.json

    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(GetProductBundleCreateResponse, required=False), required=False)
    


class ProductBundleRequest(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    products = fields.List(fields.Nested(ProductBundleItem, required=False), required=False)
    
    modified_on = fields.Str(required=False)
    
    same_store_assignment = fields.Boolean(required=False)
    
    meta = fields.Dict(required=False)
    
    page_visibility = fields.List(fields.Str(required=False), required=False)
    
    choice = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    created_by = fields.Dict(required=False)
    
    logo = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    modified_by = fields.Dict(required=False)
    


class Size(BaseSchema):
    # Catalog swagger.json

    
    is_available = fields.Boolean(required=False)
    
    quantity = fields.Int(required=False)
    
    value = fields.Str(required=False)
    
    display = fields.Str(required=False)
    


class LimitedProductData(BaseSchema):
    # Catalog swagger.json

    
    identifier = fields.Dict(required=False)
    
    uid = fields.Int(required=False)
    
    short_description = fields.Str(required=False)
    
    sizes = fields.List(fields.Str(required=False), required=False)
    
    name = fields.Str(required=False)
    
    price = fields.Dict(required=False)
    
    slug = fields.Str(required=False)
    
    images = fields.List(fields.Str(required=False), required=False)
    
    country_of_origin = fields.Str(required=False)
    
    attributes = fields.Dict(required=False)
    
    quantity = fields.Int(required=False)
    
    item_code = fields.Str(required=False)
    


class Price(BaseSchema):
    # Catalog swagger.json

    
    min_effective = fields.Float(required=False)
    
    max_effective = fields.Float(required=False)
    
    max_marked = fields.Float(required=False)
    
    currency = fields.Str(required=False)
    
    min_marked = fields.Float(required=False)
    


class GetProducts(BaseSchema):
    # Catalog swagger.json

    
    product_uid = fields.Int(required=False)
    
    sizes = fields.List(fields.Nested(Size, required=False), required=False)
    
    auto_add_to_cart = fields.Boolean(required=False)
    
    product_details = fields.Nested(LimitedProductData, required=False)
    
    auto_select = fields.Boolean(required=False)
    
    allow_remove = fields.Boolean(required=False)
    
    max_quantity = fields.Int(required=False)
    
    min_quantity = fields.Int(required=False)
    
    price = fields.Nested(Price, required=False)
    


class GetProductBundleResponse(BaseSchema):
    # Catalog swagger.json

    
    products = fields.List(fields.Nested(GetProducts, required=False), required=False)
    
    name = fields.Str(required=False)
    
    page_visibility = fields.List(fields.Str(required=False), required=False)
    
    same_store_assignment = fields.Boolean(required=False)
    
    meta = fields.Dict(required=False)
    
    slug = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    choice = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    


class ProductBundleUpdateRequest(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    products = fields.List(fields.Nested(ProductBundleItem, required=False), required=False)
    
    modified_on = fields.Str(required=False)
    
    same_store_assignment = fields.Boolean(required=False)
    
    meta = fields.Dict(required=False)
    
    page_visibility = fields.List(fields.Str(required=False), required=False)
    
    choice = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    logo = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    modified_by = fields.Dict(required=False)
    


class ListSizeGuide(BaseSchema):
    # Catalog swagger.json

    
    page = fields.Dict(required=False)
    
    items = fields.List(fields.Dict(required=False), required=False)
    


class Meta(BaseSchema):
    # Catalog swagger.json

    
    headers = fields.Dict(required=False)
    
    values = fields.List(fields.Dict(required=False), required=False)
    
    unit = fields.Str(required=False)
    


class Guide(BaseSchema):
    # Catalog swagger.json

    
    meta = fields.Nested(Meta, required=False)
    


class ValidateSizeGuide(BaseSchema):
    # Catalog swagger.json

    
    guide = fields.Nested(Guide, required=False)
    
    name = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    subtitle = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    tag = fields.Str(required=False)
    
    image = fields.Str(required=False)
    
    brand_id = fields.Int(required=False)
    
    active = fields.Boolean(required=False)
    
    created_by = fields.Dict(required=False)
    
    description = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    modified_by = fields.Dict(required=False)
    


class SuccessResponse(BaseSchema):
    # Catalog swagger.json

    
    success = fields.Boolean(required=False)
    


class SizeGuideResponse(BaseSchema):
    # Catalog swagger.json

    
    guide = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    subtitle = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    tag = fields.Str(required=False)
    
    brand_id = fields.Int(required=False)
    
    active = fields.Boolean(required=False)
    
    created_by = fields.Dict(required=False)
    
    company_id = fields.Int(required=False)
    
    modified_by = fields.Dict(required=False)
    


class MOQData(BaseSchema):
    # Catalog swagger.json

    
    increment_unit = fields.Int(required=False)
    
    maximum = fields.Int(required=False)
    
    minimum = fields.Int(required=False)
    


class SEOData(BaseSchema):
    # Catalog swagger.json

    
    description = fields.Str(required=False)
    
    title = fields.Str(required=False)
    


class OwnerAppItemResponse(BaseSchema):
    # Catalog swagger.json

    
    is_cod = fields.Boolean(required=False)
    
    alt_text = fields.Dict(required=False)
    
    moq = fields.Nested(MOQData, required=False)
    
    seo = fields.Nested(SEOData, required=False)
    
    is_gift = fields.Boolean(required=False)
    


class MetaFields(BaseSchema):
    # Catalog swagger.json

    
    key = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class ApplicationItemMOQ(BaseSchema):
    # Catalog swagger.json

    
    increment_unit = fields.Int(required=False)
    
    maximum = fields.Int(required=False)
    
    minimum = fields.Int(required=False)
    


class ApplicationItemSEO(BaseSchema):
    # Catalog swagger.json

    
    description = fields.Str(required=False)
    
    title = fields.Str(required=False)
    


class ApplicationItemMeta(BaseSchema):
    # Catalog swagger.json

    
    _custom_meta = fields.List(fields.Nested(MetaFields, required=False), required=False)
    
    is_cod = fields.Boolean(required=False)
    
    alt_text = fields.Dict(required=False)
    
    moq = fields.Nested(ApplicationItemMOQ, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    seo = fields.Nested(ApplicationItemSEO, required=False)
    
    is_gift = fields.Boolean(required=False)
    


class SuccessResponse1(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    success = fields.Boolean(required=False)
    


class GetConfigMetadataResponse(BaseSchema):
    # Catalog swagger.json

    
    values = fields.List(fields.Dict(required=False), required=False)
    
    data = fields.List(fields.Dict(required=False), required=False)
    
    condition = fields.List(fields.Dict(required=False), required=False)
    


class PageResponseType(BaseSchema):
    # Catalog swagger.json

    
    total_count = fields.Int(required=False)
    
    has_next = fields.Boolean(required=False)
    
    current = fields.Int(required=False)
    
    next = fields.Int(required=False)
    


class GetConfigResponse(BaseSchema):
    # Catalog swagger.json

    
    page = fields.Nested(PageResponseType, required=False)
    
    data = fields.List(fields.Dict(required=False), required=False)
    


class ConfigErrorResponse(BaseSchema):
    # Catalog swagger.json

    
    message = fields.Str(required=False)
    


class AttributeDetailsGroup(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    unit = fields.Str(required=False)
    
    display_type = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    logo = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    


class AppConfigurationDetail(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    attributes = fields.List(fields.Nested(AttributeDetailsGroup, required=False), required=False)
    
    template_slugs = fields.List(fields.Str(required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    app_id = fields.Str(required=False)
    
    is_default = fields.Boolean(required=False)
    
    logo = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    


class ConfigSuccessResponse(BaseSchema):
    # Catalog swagger.json

    
    message = fields.Str(required=False)
    


class AppConfigurationsSort(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    default_key = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    app_id = fields.Str(required=False)
    
    is_default = fields.Boolean(required=False)
    
    logo = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    


class AllowSingleRequest(BaseSchema):
    # Catalog swagger.json

    
    allow_single = fields.Boolean(required=False)
    


class DefaultKeyRequest(BaseSchema):
    # Catalog swagger.json

    
    default_key = fields.Str(required=False)
    


class MetaDataListingSortMetaResponse(BaseSchema):
    # Catalog swagger.json

    
    key = fields.Str(required=False)
    
    display = fields.Str(required=False)
    


class MetaDataListingSortResponse(BaseSchema):
    # Catalog swagger.json

    
    data = fields.List(fields.Nested(MetaDataListingSortMetaResponse, required=False), required=False)
    


class MetaDataListingFilterMetaResponse(BaseSchema):
    # Catalog swagger.json

    
    units = fields.List(fields.Dict(required=False), required=False)
    
    key = fields.Str(required=False)
    
    filter_types = fields.List(fields.Str(required=False), required=False)
    
    display = fields.Str(required=False)
    


class MetaDataListingFilterResponse(BaseSchema):
    # Catalog swagger.json

    
    data = fields.List(fields.Nested(MetaDataListingFilterMetaResponse, required=False), required=False)
    


class MetaDataListingResponse(BaseSchema):
    # Catalog swagger.json

    
    sort = fields.Nested(MetaDataListingSortResponse, required=False)
    
    filter = fields.Nested(MetaDataListingFilterResponse, required=False)
    


class GetCatalogConfigurationDetailsProduct(BaseSchema):
    # Catalog swagger.json

    
    compare = fields.Dict(required=False)
    
    similar = fields.Dict(required=False)
    
    variant = fields.Dict(required=False)
    
    detail = fields.Dict(required=False)
    


class GetCatalogConfigurationMetaData(BaseSchema):
    # Catalog swagger.json

    
    listing = fields.Nested(MetaDataListingResponse, required=False)
    
    product = fields.Nested(GetCatalogConfigurationDetailsProduct, required=False)
    


class ConfigurationListingSortConfig(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    logo = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    


class ConfigurationListingSort(BaseSchema):
    # Catalog swagger.json

    
    config = fields.List(fields.Nested(ConfigurationListingSortConfig, required=False), required=False)
    
    default_key = fields.Str(required=False)
    


class ConfigurationBucketPoints(BaseSchema):
    # Catalog swagger.json

    
    display = fields.Str(required=False)
    
    start = fields.Float(required=False)
    
    end = fields.Float(required=False)
    


class ConfigurationListingFilterValue(BaseSchema):
    # Catalog swagger.json

    
    sort = fields.Str(required=False)
    
    map_values = fields.List(fields.Dict(required=False), required=False)
    
    bucket_points = fields.List(fields.Nested(ConfigurationBucketPoints, required=False), required=False)
    
    condition = fields.Str(required=False)
    
    map = fields.Dict(required=False)
    
    value = fields.Str(required=False)
    


class ConfigurationListingFilterConfig(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    value_config = fields.Nested(ConfigurationListingFilterValue, required=False)
    
    key = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    
    display_name = fields.Str(required=False)
    


class ConfigurationListingFilter(BaseSchema):
    # Catalog swagger.json

    
    allow_single = fields.Boolean(required=False)
    
    attribute_config = fields.List(fields.Nested(ConfigurationListingFilterConfig, required=False), required=False)
    


class ConfigurationListing(BaseSchema):
    # Catalog swagger.json

    
    sort = fields.Nested(ConfigurationListingSort, required=False)
    
    filter = fields.Nested(ConfigurationListingFilter, required=False)
    


class ProductSize(BaseSchema):
    # Catalog swagger.json

    
    min = fields.Int(required=False)
    
    max = fields.Int(required=False)
    


class ConfigurationProductConfig(BaseSchema):
    # Catalog swagger.json

    
    subtitle = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    size = fields.Nested(ProductSize, required=False)
    
    key = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    logo = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    


class ConfigurationProductSimilar(BaseSchema):
    # Catalog swagger.json

    
    config = fields.List(fields.Nested(ConfigurationProductConfig, required=False), required=False)
    


class ConfigurationProductVariantConfig(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    display_type = fields.Str(required=False)
    
    size = fields.Nested(ProductSize, required=False)
    
    key = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    logo = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    


class ConfigurationProductVariant(BaseSchema):
    # Catalog swagger.json

    
    config = fields.List(fields.Nested(ConfigurationProductVariantConfig, required=False), required=False)
    


class ConfigurationProduct(BaseSchema):
    # Catalog swagger.json

    
    similar = fields.Nested(ConfigurationProductSimilar, required=False)
    
    variant = fields.Nested(ConfigurationProductVariant, required=False)
    


class AppCatalogConfiguration(BaseSchema):
    # Catalog swagger.json

    
    listing = fields.Nested(ConfigurationListing, required=False)
    
    id = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    config_type = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    config_id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    app_id = fields.Str(required=False)
    
    created_by = fields.Dict(required=False)
    
    product = fields.Nested(ConfigurationProduct, required=False)
    
    modified_by = fields.Dict(required=False)
    


class GetAppCatalogConfiguration(BaseSchema):
    # Catalog swagger.json

    
    data = fields.Nested(AppCatalogConfiguration, required=False)
    
    is_default = fields.Boolean(required=False)
    


class AppConfiguration(BaseSchema):
    # Catalog swagger.json

    
    listing = fields.Nested(ConfigurationListing, required=False)
    
    modified_on = fields.Str(required=False)
    
    config_type = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    config_id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    app_id = fields.Str(required=False)
    
    created_by = fields.Dict(required=False)
    
    product = fields.Nested(ConfigurationProduct, required=False)
    
    modified_by = fields.Dict(required=False)
    


class GetCatalogConfigurationDetailsSchemaListing(BaseSchema):
    # Catalog swagger.json

    
    sort = fields.Dict(required=False)
    
    filter = fields.Dict(required=False)
    


class EntityConfiguration(BaseSchema):
    # Catalog swagger.json

    
    listing = fields.Nested(GetCatalogConfigurationDetailsSchemaListing, required=False)
    
    id = fields.Str(required=False)
    
    config_type = fields.Str(required=False)
    
    config_id = fields.Str(required=False)
    
    app_id = fields.Str(required=False)
    
    product = fields.Nested(GetCatalogConfigurationDetailsProduct, required=False)
    


class GetAppCatalogEntityConfiguration(BaseSchema):
    # Catalog swagger.json

    
    data = fields.Nested(EntityConfiguration, required=False)
    
    is_default = fields.Boolean(required=False)
    


class ProductSortOn(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    is_selected = fields.Boolean(required=False)
    


class ProductFiltersKey(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    operators = fields.List(fields.Str(required=False), required=False)
    
    display = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    kind = fields.Str(required=False)
    


class ProductFiltersValue(BaseSchema):
    # Catalog swagger.json

    
    min = fields.Int(required=False)
    
    is_selected = fields.Boolean(required=False)
    
    max = fields.Int(required=False)
    
    selected_max = fields.Int(required=False)
    
    currency_symbol = fields.Str(required=False)
    
    selected_min = fields.Int(required=False)
    
    count = fields.Int(required=False)
    
    display_format = fields.Str(required=False)
    
    display = fields.Str(required=False)
    
    value = fields.Raw(required=False)
    
    currency_code = fields.Str(required=False)
    
    query_format = fields.Str(required=False)
    


class ProductFilters(BaseSchema):
    # Catalog swagger.json

    
    key = fields.Nested(ProductFiltersKey, required=False)
    
    values = fields.List(fields.Nested(ProductFiltersValue, required=False), required=False)
    


class GetCollectionQueryOptionResponse(BaseSchema):
    # Catalog swagger.json

    
    sort_on = fields.List(fields.Nested(ProductSortOn, required=False), required=False)
    
    operators = fields.Dict(required=False)
    
    filters = fields.List(fields.Nested(ProductFilters, required=False), required=False)
    


class CollectionQuery(BaseSchema):
    # Catalog swagger.json

    
    op = fields.Str(required=False)
    
    attribute = fields.Str(required=False)
    
    value = fields.List(fields.Raw(required=False), required=False)
    


class BannerImage(BaseSchema):
    # Catalog swagger.json

    
    aspect_ratio = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    url = fields.Str(required=False)
    


class ImageUrls(BaseSchema):
    # Catalog swagger.json

    
    landscape = fields.Nested(BannerImage, required=False)
    
    portrait = fields.Nested(BannerImage, required=False)
    


class Media1(BaseSchema):
    # Catalog swagger.json

    
    meta = fields.Dict(required=False)
    
    type = fields.Str(required=False)
    
    url = fields.Str(required=False)
    


class ActionPage(BaseSchema):
    # Catalog swagger.json

    
    params = fields.Dict(required=False)
    
    query = fields.Dict(required=False)
    
    url = fields.Str(required=False)
    
    type = fields.Nested(PageType, required=False)
    


class Action(BaseSchema):
    # Catalog swagger.json

    
    page = fields.Nested(ActionPage, required=False)
    
    popup = fields.Nested(ActionPage, required=False)
    
    type = fields.Str(required=False)
    


class GetCollectionDetailNest(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Str(required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    tag = fields.List(fields.Str(required=False), required=False)
    
    _schedule = fields.Dict(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    cron = fields.Dict(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    type = fields.Str(required=False)
    
    logo = fields.Nested(Media1, required=False)
    
    priority = fields.Int(required=False)
    
    description = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    badge = fields.Dict(required=False)
    
    meta = fields.Dict(required=False)
    
    slug = fields.Str(required=False)
    
    action = fields.Nested(Action, required=False)
    
    is_active = fields.Boolean(required=False)
    
    app_id = fields.Str(required=False)
    


class CollectionListingFilterType(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    is_selected = fields.Boolean(required=False)
    
    display = fields.Str(required=False)
    


class CollectionListingFilterTag(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    is_selected = fields.Boolean(required=False)
    
    display = fields.Str(required=False)
    


class CollectionListingFilter(BaseSchema):
    # Catalog swagger.json

    
    type = fields.List(fields.Nested(CollectionListingFilterType, required=False), required=False)
    
    tags = fields.List(fields.Nested(CollectionListingFilterTag, required=False), required=False)
    


class GetCollectionListingResponse(BaseSchema):
    # Catalog swagger.json

    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(GetCollectionDetailNest, required=False), required=False)
    
    filters = fields.Nested(CollectionListingFilter, required=False)
    


class SeoDetail(BaseSchema):
    # Catalog swagger.json

    
    description = fields.Str(required=False)
    
    title = fields.Str(required=False)
    


class UserInfo(BaseSchema):
    # Catalog swagger.json

    
    username = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    


class NextSchedule(BaseSchema):
    # Catalog swagger.json

    
    start = fields.Str(required=False)
    
    end = fields.Str(required=False)
    


class CollectionSchedule(BaseSchema):
    # Catalog swagger.json

    
    duration = fields.Int(required=False)
    
    next_schedule = fields.List(fields.Nested(NextSchedule, required=False), required=False)
    
    start = fields.Str(required=False)
    
    end = fields.Str(required=False)
    
    cron = fields.Str(required=False)
    


class CollectionImage(BaseSchema):
    # Catalog swagger.json

    
    aspect_ratio = fields.Str(required=False)
    
    url = fields.Str(required=False)
    


class CollectionBanner(BaseSchema):
    # Catalog swagger.json

    
    landscape = fields.Nested(CollectionImage, required=False)
    
    portrait = fields.Nested(CollectionImage, required=False)
    


class CollectionBadge(BaseSchema):
    # Catalog swagger.json

    
    text = fields.Str(required=False)
    
    color = fields.Str(required=False)
    


class CreateCollection(BaseSchema):
    # Catalog swagger.json

    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    seo = fields.Nested(SeoDetail, required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    is_visible = fields.Boolean(required=False)
    
    _schedule = fields.Nested(CollectionSchedule, required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    _locale_language = fields.Dict(required=False)
    
    banners = fields.Nested(CollectionBanner, required=False)
    
    type = fields.Str(required=False)
    
    created_by = fields.Nested(UserInfo, required=False)
    
    logo = fields.Nested(CollectionImage, required=False)
    
    description = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    badge = fields.Nested(CollectionBadge, required=False)
    
    meta = fields.Dict(required=False)
    
    slug = fields.Str(required=False)
    
    sort_on = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    app_id = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    published = fields.Boolean(required=False)
    


class CollectionCreateResponse(BaseSchema):
    # Catalog swagger.json

    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    tag = fields.List(fields.Str(required=False), required=False)
    
    _schedule = fields.Dict(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    cron = fields.Dict(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    type = fields.Str(required=False)
    
    logo = fields.Nested(BannerImage, required=False)
    
    priority = fields.Int(required=False)
    
    description = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    badge = fields.Dict(required=False)
    
    meta = fields.Dict(required=False)
    
    slug = fields.Str(required=False)
    
    sort_on = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    app_id = fields.Str(required=False)
    


class CollectionDetailResponse(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Str(required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    tag = fields.List(fields.Str(required=False), required=False)
    
    _schedule = fields.Dict(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    cron = fields.Dict(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    type = fields.Str(required=False)
    
    logo = fields.Nested(Media1, required=False)
    
    priority = fields.Int(required=False)
    
    description = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    badge = fields.Dict(required=False)
    
    meta = fields.Dict(required=False)
    
    slug = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    app_id = fields.Str(required=False)
    


class UpdateCollection(BaseSchema):
    # Catalog swagger.json

    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    seo = fields.Nested(SeoDetail, required=False)
    
    modified_by = fields.Nested(UserInfo, required=False)
    
    is_visible = fields.Boolean(required=False)
    
    _schedule = fields.Nested(CollectionSchedule, required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    _locale_language = fields.Dict(required=False)
    
    banners = fields.Nested(CollectionBanner, required=False)
    
    type = fields.Str(required=False)
    
    logo = fields.Nested(CollectionImage, required=False)
    
    description = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    badge = fields.Nested(CollectionBadge, required=False)
    
    meta = fields.Dict(required=False)
    
    slug = fields.Str(required=False)
    
    sort_on = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    published = fields.Boolean(required=False)
    


class ProductBrand(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    action = fields.Nested(Action, required=False)
    
    name = fields.Str(required=False)
    
    logo = fields.Nested(Media1, required=False)
    


class Price1(BaseSchema):
    # Catalog swagger.json

    
    currency_symbol = fields.Str(required=False)
    
    currency_code = fields.Str(required=False)
    
    min = fields.Float(required=False)
    
    max = fields.Float(required=False)
    


class ProductListingPrice(BaseSchema):
    # Catalog swagger.json

    
    marked = fields.Nested(Price1, required=False)
    
    effective = fields.Nested(Price1, required=False)
    


class ProductDetailAttribute(BaseSchema):
    # Catalog swagger.json

    
    key = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class ProductDetailGroupedAttribute(BaseSchema):
    # Catalog swagger.json

    
    details = fields.List(fields.Nested(ProductDetailAttribute, required=False), required=False)
    
    title = fields.Str(required=False)
    


class ProductListingDetail(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    similars = fields.List(fields.Str(required=False), required=False)
    
    rating_count = fields.Int(required=False)
    
    medias = fields.List(fields.Nested(Media1, required=False), required=False)
    
    discount = fields.Str(required=False)
    
    image_nature = fields.Str(required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    rating = fields.Float(required=False)
    
    color = fields.Str(required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    brand = fields.Nested(ProductBrand, required=False)
    
    has_variant = fields.Boolean(required=False)
    
    item_code = fields.Str(required=False)
    
    price = fields.Nested(ProductListingPrice, required=False)
    
    promo_meta = fields.Dict(required=False)
    
    type = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    short_description = fields.Str(required=False)
    
    grouped_attributes = fields.List(fields.Nested(ProductDetailGroupedAttribute, required=False), required=False)
    
    name = fields.Str(required=False)
    
    product_online_date = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    teaser_tag = fields.Dict(required=False)
    
    sellable = fields.Boolean(required=False)
    
    attributes = fields.Dict(required=False)
    
    item_type = fields.Str(required=False)
    


class GetCollectionItemsResponse(BaseSchema):
    # Catalog swagger.json

    
    sort_on = fields.List(fields.Nested(ProductSortOn, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(ProductListingDetail, required=False), required=False)
    
    filters = fields.List(fields.Nested(ProductFilters, required=False), required=False)
    


class ItemQueryForUserCollection(BaseSchema):
    # Catalog swagger.json

    
    item_id = fields.Int(required=False)
    
    action = fields.Str(required=False)
    


class CollectionItemRequest(BaseSchema):
    # Catalog swagger.json

    
    item = fields.List(fields.Nested(ItemQueryForUserCollection, required=False), required=False)
    
    type = fields.Str(required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    


class UpdatedResponse(BaseSchema):
    # Catalog swagger.json

    
    message = fields.Str(required=False)
    
    items_not_updated = fields.List(fields.Int(required=False), required=False)
    


class CatalogInsightItem(BaseSchema):
    # Catalog swagger.json

    
    out_of_stock_count = fields.Int(required=False)
    
    sellable_count = fields.Int(required=False)
    
    count = fields.Int(required=False)
    


class CatalogInsightBrand(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    total_articles = fields.Int(required=False)
    
    available_articles = fields.Int(required=False)
    
    article_freshness = fields.Int(required=False)
    
    available_sizes = fields.Int(required=False)
    
    total_sizes = fields.Int(required=False)
    


class CatalogInsightResponse(BaseSchema):
    # Catalog swagger.json

    
    item = fields.Nested(CatalogInsightItem, required=False)
    
    brand_distribution = fields.Nested(CatalogInsightBrand, required=False)
    


class CrossSellingData(BaseSchema):
    # Catalog swagger.json

    
    products = fields.Int(required=False)
    
    articles = fields.Int(required=False)
    


class CrossSellingResponse(BaseSchema):
    # Catalog swagger.json

    
    brand_distribution = fields.Nested(CatalogInsightBrand, required=False)
    
    data = fields.Nested(CrossSellingData, required=False)
    


class OptInPostRequest(BaseSchema):
    # Catalog swagger.json

    
    opt_level = fields.Str(required=False)
    
    enabled = fields.Boolean(required=False)
    
    store_ids = fields.List(fields.Int(required=False), required=False)
    
    brand_ids = fields.List(fields.Int(required=False), required=False)
    
    company_id = fields.Int(required=False)
    
    platform = fields.Str(required=False)
    


class CompanyOptIn(BaseSchema):
    # Catalog swagger.json

    
    opt_level = fields.Str(required=False)
    
    modified_on = fields.Int(required=False)
    
    enabled = fields.Boolean(required=False)
    
    created_on = fields.Int(required=False)
    
    store_ids = fields.List(fields.Int(required=False), required=False)
    
    brand_ids = fields.List(fields.Int(required=False), required=False)
    
    modified_by = fields.Dict(required=False)
    
    created_by = fields.Dict(required=False)
    
    company_id = fields.Int(required=False)
    
    platform = fields.Str(required=False)
    


class GetOptInPlatform(BaseSchema):
    # Catalog swagger.json

    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(CompanyOptIn, required=False), required=False)
    


class OptinCompanyDetail(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    business_type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    company_type = fields.Str(required=False)
    


class CompanyBrandDetail(BaseSchema):
    # Catalog swagger.json

    
    brand_id = fields.Int(required=False)
    
    total_article = fields.Int(required=False)
    
    company_id = fields.Int(required=False)
    
    brand_name = fields.Str(required=False)
    


class OptinCompanyBrandDetailsView(BaseSchema):
    # Catalog swagger.json

    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(CompanyBrandDetail, required=False), required=False)
    


class OptinCompanyMetrics(BaseSchema):
    # Catalog swagger.json

    
    store = fields.Int(required=False)
    
    company = fields.Str(required=False)
    
    brand = fields.Int(required=False)
    


class StoreDetail(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    address = fields.Dict(required=False)
    
    manager = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    store_code = fields.Str(required=False)
    
    documents = fields.List(fields.Dict(required=False), required=False)
    
    store_type = fields.Str(required=False)
    
    timing = fields.Dict(required=False)
    
    additional_contacts = fields.List(fields.Dict(required=False), required=False)
    
    display_name = fields.Str(required=False)
    


class OptinStoreDetails(BaseSchema):
    # Catalog swagger.json

    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(StoreDetail, required=False), required=False)
    


class AttributeMasterMandatoryDetails(BaseSchema):
    # Catalog swagger.json

    
    l3_keys = fields.List(fields.Str(required=False), required=False)
    


class AttributeMasterMeta(BaseSchema):
    # Catalog swagger.json

    
    mandatory_details = fields.Nested(AttributeMasterMandatoryDetails, required=False)
    
    enriched = fields.Boolean(required=False)
    


class AttributeMasterDetails(BaseSchema):
    # Catalog swagger.json

    
    display_type = fields.Str(required=False)
    


class AttributeMasterFilter(BaseSchema):
    # Catalog swagger.json

    
    priority = fields.Int(required=False)
    
    depends_on = fields.List(fields.Str(required=False), required=False)
    
    indexing = fields.Boolean(required=False)
    


class AttributeSchemaRange(BaseSchema):
    # Catalog swagger.json

    
    min = fields.Int(required=False)
    
    max = fields.Int(required=False)
    


class AttributeMaster(BaseSchema):
    # Catalog swagger.json

    
    multi = fields.Boolean(required=False)
    
    allowed_values = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    
    format = fields.Str(required=False)
    
    range = fields.Nested(AttributeSchemaRange, required=False)
    
    mandatory = fields.Boolean(required=False)
    


class GenderDetail(BaseSchema):
    # Catalog swagger.json

    
    enabled_for_end_consumer = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    meta = fields.Nested(AttributeMasterMeta, required=False)
    
    details = fields.Nested(AttributeMasterDetails, required=False)
    
    slug = fields.Str(required=False)
    
    is_nested = fields.Boolean(required=False)
    
    filters = fields.Nested(AttributeMasterFilter, required=False)
    
    departments = fields.List(fields.Str(required=False), required=False)
    
    logo = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    schema = fields.Nested(AttributeMaster, required=False)
    


class ProductTemplateCategory(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    slug_key = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    template_slug = fields.Str(required=False)
    


class ProdcutTemplateCategoriesResponse(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(ProductTemplateCategory, required=False), required=False)
    


class PTErrorResponse(BaseSchema):
    # Catalog swagger.json

    
    message = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    status = fields.Int(required=False)
    
    code = fields.Str(required=False)
    
    errors = fields.Dict(required=False)
    


class UserSerializer(BaseSchema):
    # Catalog swagger.json

    
    _id = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
    username = fields.Str(required=False)
    
    contact = fields.Str(required=False)
    


class GetDepartment(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    page_no = fields.Int(required=False)
    
    modified_on = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    priority_order = fields.Int(required=False)
    
    synonyms = fields.List(fields.Str(required=False), required=False)
    
    search = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    page_size = fields.Int(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    logo = fields.Str(required=False)
    
    item_type = fields.Str(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    


class DepartmentsResponse(BaseSchema):
    # Catalog swagger.json

    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(GetDepartment, required=False), required=False)
    


class DepartmentErrorResponse(BaseSchema):
    # Catalog swagger.json

    
    message = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    status = fields.Int(required=False)
    
    code = fields.Str(required=False)
    
    errors = fields.Dict(required=False)
    


class DepartmentCreateUpdate(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    priority_order = fields.Int(required=False)
    
    slug = fields.Str(required=False)
    
    _cls = fields.Str(required=False)
    
    synonyms = fields.List(fields.Str(required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    logo = fields.Str(required=False)
    
    platforms = fields.Dict(required=False)
    


class DepartmentCreateResponse(BaseSchema):
    # Catalog swagger.json

    
    message = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    


class DepartmentCreateErrorResponse(BaseSchema):
    # Catalog swagger.json

    
    error = fields.Str(required=False)
    


class UserDetail(BaseSchema):
    # Catalog swagger.json

    
    username = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
    contact = fields.Str(required=False)
    
    super_user = fields.Boolean(required=False)
    


class DepartmentModel(BaseSchema):
    # Catalog swagger.json

    
    _id = fields.Raw(required=False)
    
    uid = fields.Int(required=False)
    
    verified_by = fields.Nested(UserDetail, required=False)
    
    name = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    verified_on = fields.Str(required=False)
    
    priority_order = fields.Int(required=False)
    
    _cls = fields.Str(required=False)
    
    synonyms = fields.List(fields.Str(required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    created_by = fields.Nested(UserDetail, required=False)
    
    logo = fields.Str(required=False)
    
    modified_by = fields.Nested(UserDetail, required=False)
    


class ProductTemplate(BaseSchema):
    # Catalog swagger.json

    
    is_physical = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    is_archived = fields.Boolean(required=False)
    
    modified_on = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    tag = fields.Str(required=False)
    
    is_expirable = fields.Boolean(required=False)
    
    departments = fields.List(fields.Str(required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    modified_by = fields.Dict(required=False)
    
    attributes = fields.List(fields.Str(required=False), required=False)
    
    categories = fields.List(fields.Str(required=False), required=False)
    
    logo = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    created_by = fields.Dict(required=False)
    


class TemplatesResponse(BaseSchema):
    # Catalog swagger.json

    
    page = fields.Nested(Page, required=False)
    
    items = fields.Nested(ProductTemplate, required=False)
    


class TemplateDetails(BaseSchema):
    # Catalog swagger.json

    
    is_physical = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    is_archived = fields.Boolean(required=False)
    
    id = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    tag = fields.Str(required=False)
    
    is_expirable = fields.Boolean(required=False)
    
    departments = fields.List(fields.Str(required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    attributes = fields.List(fields.Str(required=False), required=False)
    
    categories = fields.List(fields.Str(required=False), required=False)
    
    logo = fields.Str(required=False)
    
    description = fields.Str(required=False)
    


class Properties(BaseSchema):
    # Catalog swagger.json

    
    trader = fields.Dict(required=False)
    
    custom_order = fields.Dict(required=False)
    
    no_of_boxes = fields.Dict(required=False)
    
    country_of_origin = fields.Dict(required=False)
    
    tags = fields.Dict(required=False)
    
    highlights = fields.Dict(required=False)
    
    media = fields.Dict(required=False)
    
    command = fields.Dict(required=False)
    
    multi_size = fields.Dict(required=False)
    
    return_config = fields.Dict(required=False)
    
    category_slug = fields.Dict(required=False)
    
    item_code = fields.Dict(required=False)
    
    variants = fields.Dict(required=False)
    
    hsn_code = fields.Dict(required=False)
    
    is_dependent = fields.Dict(required=False)
    
    product_group_tag = fields.Dict(required=False)
    
    currency = fields.Dict(required=False)
    
    size_guide = fields.Dict(required=False)
    
    description = fields.Dict(required=False)
    
    short_description = fields.Dict(required=False)
    
    sizes = fields.Dict(required=False)
    
    name = fields.Dict(required=False)
    
    trader_type = fields.Dict(required=False)
    
    brand_uid = fields.Dict(required=False)
    
    slug = fields.Dict(required=False)
    
    teaser_tag = fields.Dict(required=False)
    
    is_active = fields.Dict(required=False)
    
    item_type = fields.Dict(required=False)
    
    product_publish = fields.Dict(required=False)
    


class GlobalValidation(BaseSchema):
    # Catalog swagger.json

    
    title = fields.Str(required=False)
    
    required = fields.List(fields.Str(required=False), required=False)
    
    definitions = fields.Dict(required=False)
    
    description = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    properties = fields.Nested(Properties, required=False)
    


class TemplateValidationData(BaseSchema):
    # Catalog swagger.json

    
    global_validation = fields.Nested(GlobalValidation, required=False)
    
    template_validation = fields.Dict(required=False)
    


class TemplatesValidationResponse(BaseSchema):
    # Catalog swagger.json

    
    template_details = fields.Nested(TemplateDetails, required=False)
    
    data = fields.Nested(TemplateValidationData, required=False)
    


class InventoryValidationResponse(BaseSchema):
    # Catalog swagger.json

    
    message = fields.Str(required=False)
    
    data = fields.Dict(required=False)
    


class HSNData(BaseSchema):
    # Catalog swagger.json

    
    hsn_code = fields.List(fields.Str(required=False), required=False)
    
    country_of_origin = fields.List(fields.Str(required=False), required=False)
    


class HSNCodesResponse(BaseSchema):
    # Catalog swagger.json

    
    message = fields.Str(required=False)
    
    data = fields.Nested(HSNData, required=False)
    


class UserInfo1(BaseSchema):
    # Catalog swagger.json

    
    username = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    


class ProductTemplateExportResponse(BaseSchema):
    # Catalog swagger.json

    
    modified_on = fields.Str(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    status = fields.Str(required=False)
    
    seller_id = fields.Int(required=False)
    
    filters = fields.Dict(required=False)
    
    completed_on = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    created_by = fields.Nested(UserInfo1, required=False)
    
    task_id = fields.Str(required=False)
    
    url = fields.Str(required=False)
    


class ProductDownloadsResponse(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(ProductTemplateExportResponse, required=False), required=False)
    


class ProductTemplateExportFilterRequest(BaseSchema):
    # Catalog swagger.json

    
    templates = fields.List(fields.Str(required=False), required=False)
    
    brands = fields.List(fields.Str(required=False), required=False)
    
    from_date = fields.Str(required=False)
    
    to_date = fields.Str(required=False)
    
    catalogue_types = fields.List(fields.Str(required=False), required=False)
    


class ProductTemplateDownloadsExport(BaseSchema):
    # Catalog swagger.json

    
    type = fields.Str(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    filters = fields.Nested(ProductTemplateExportFilterRequest, required=False)
    


class ProductPartialExportRequest(BaseSchema):
    # Catalog swagger.json

    
    status = fields.Str(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    


class ProductConfigurationDownloads(BaseSchema):
    # Catalog swagger.json

    
    multivalue = fields.Boolean(required=False)
    
    data = fields.List(fields.Dict(required=False), required=False)
    


class Media2(BaseSchema):
    # Catalog swagger.json

    
    logo = fields.Str(required=False)
    
    landscape = fields.Str(required=False)
    
    portrait = fields.Str(required=False)
    


class Hierarchy(BaseSchema):
    # Catalog swagger.json

    
    l2 = fields.Int(required=False)
    
    department = fields.Int(required=False)
    
    l1 = fields.Int(required=False)
    


class CategoryMappingValues(BaseSchema):
    # Catalog swagger.json

    
    catalog_id = fields.Int(required=False)
    
    name = fields.Str(required=False)
    


class CategoryMapping(BaseSchema):
    # Catalog swagger.json

    
    ajio = fields.Nested(CategoryMappingValues, required=False)
    
    facebook = fields.Nested(CategoryMappingValues, required=False)
    
    google = fields.Nested(CategoryMappingValues, required=False)
    


class Category(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    media = fields.Nested(Media2, required=False)
    
    modified_on = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    hierarchy = fields.List(fields.Nested(Hierarchy, required=False), required=False)
    
    created_on = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    level = fields.Int(required=False)
    
    departments = fields.List(fields.Int(required=False), required=False)
    
    synonyms = fields.List(fields.Str(required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    created_by = fields.Dict(required=False)
    
    marketplaces = fields.Nested(CategoryMapping, required=False)
    
    priority = fields.Int(required=False)
    
    modified_by = fields.Dict(required=False)
    


class CategoryResponse(BaseSchema):
    # Catalog swagger.json

    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(Category, required=False), required=False)
    


class CategoryRequestBody(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    media = fields.Nested(Media2, required=False)
    
    hierarchy = fields.List(fields.Nested(Hierarchy, required=False), required=False)
    
    slug = fields.Str(required=False)
    
    level = fields.Int(required=False)
    
    departments = fields.List(fields.Int(required=False), required=False)
    
    synonyms = fields.List(fields.Str(required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    marketplaces = fields.Nested(CategoryMapping, required=False)
    
    priority = fields.Int(required=False)
    


class CategoryCreateResponse(BaseSchema):
    # Catalog swagger.json

    
    message = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    


class SingleCategoryResponse(BaseSchema):
    # Catalog swagger.json

    
    data = fields.Nested(Category, required=False)
    


class CategoryUpdateResponse(BaseSchema):
    # Catalog swagger.json

    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class Trader(BaseSchema):
    # Catalog swagger.json

    
    address = fields.List(fields.Str(required=False), required=False)
    
    name = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class VerifiedBy(BaseSchema):
    # Catalog swagger.json

    
    username = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    


class Image(BaseSchema):
    # Catalog swagger.json

    
    aspect_ratio_f = fields.Float(required=False)
    
    secure_url = fields.Str(required=False)
    
    aspect_ratio = fields.Str(required=False)
    
    url = fields.Str(required=False)
    


class ReturnConfigResponse(BaseSchema):
    # Catalog swagger.json

    
    time = fields.Int(required=False)
    
    unit = fields.Str(required=False)
    
    returnable = fields.Boolean(required=False)
    


class Logo(BaseSchema):
    # Catalog swagger.json

    
    aspect_ratio_f = fields.Int(required=False)
    
    secure_url = fields.Str(required=False)
    
    aspect_ratio = fields.Str(required=False)
    
    url = fields.Str(required=False)
    


class Brand(BaseSchema):
    # Catalog swagger.json

    
    logo = fields.Nested(Logo, required=False)
    
    name = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    


class NetQuantityResponse(BaseSchema):
    # Catalog swagger.json

    
    unit = fields.Str(required=False)
    
    value = fields.Float(required=False)
    


class ProductPublish(BaseSchema):
    # Catalog swagger.json

    
    is_set = fields.Boolean(required=False)
    
    product_online_date = fields.Str(required=False)
    


class ProductSchemaV2(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    trader = fields.List(fields.Nested(Trader, required=False), required=False)
    
    is_image_less_product = fields.Boolean(required=False)
    
    verified_by = fields.Nested(VerifiedBy, required=False)
    
    custom_order = fields.Dict(required=False)
    
    images = fields.List(fields.Nested(Image, required=False), required=False)
    
    primary_color = fields.Str(required=False)
    
    no_of_boxes = fields.Int(required=False)
    
    country_of_origin = fields.Str(required=False)
    
    departments = fields.List(fields.Int(required=False), required=False)
    
    all_company_ids = fields.List(fields.Int(required=False), required=False)
    
    image_nature = fields.Str(required=False)
    
    all_sizes = fields.List(fields.Dict(required=False), required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    category = fields.Dict(required=False)
    
    pending = fields.Str(required=False)
    
    l3_mapping = fields.List(fields.Str(required=False), required=False)
    
    modified_by = fields.Dict(required=False)
    
    is_set = fields.Boolean(required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    media = fields.List(fields.Nested(Media1, required=False), required=False)
    
    created_on = fields.Str(required=False)
    
    variant_media = fields.Dict(required=False)
    
    multi_size = fields.Boolean(required=False)
    
    attributes = fields.Dict(required=False)
    
    moq = fields.Dict(required=False)
    
    color = fields.Str(required=False)
    
    return_config = fields.Nested(ReturnConfigResponse, required=False)
    
    brand = fields.Nested(Brand, required=False)
    
    category_slug = fields.Str(required=False)
    
    item_code = fields.Str(required=False)
    
    variants = fields.Dict(required=False)
    
    id = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    template_tag = fields.Str(required=False)
    
    net_quantity = fields.Nested(NetQuantityResponse, required=False)
    
    hsn_code = fields.Str(required=False)
    
    is_dependent = fields.Boolean(required=False)
    
    variant_group = fields.Dict(required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    category_uid = fields.Int(required=False)
    
    product_group_tag = fields.List(fields.Str(required=False), required=False)
    
    currency = fields.Str(required=False)
    
    is_expirable = fields.Boolean(required=False)
    
    size_guide = fields.Str(required=False)
    
    created_by = fields.Dict(required=False)
    
    description = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    stage = fields.Str(required=False)
    
    short_description = fields.Str(required=False)
    
    sizes = fields.List(fields.Dict(required=False), required=False)
    
    name = fields.Str(required=False)
    
    brand_uid = fields.Int(required=False)
    
    slug = fields.Str(required=False)
    
    verified_on = fields.Str(required=False)
    
    teaser_tag = fields.Dict(required=False)
    
    is_active = fields.Boolean(required=False)
    
    all_identifiers = fields.List(fields.Str(required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    is_physical = fields.Boolean(required=False)
    
    item_type = fields.Str(required=False)
    
    product_publish = fields.Nested(ProductPublish, required=False)
    


class ProductListingResponseV2(BaseSchema):
    # Catalog swagger.json

    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(ProductSchemaV2, required=False), required=False)
    


class CustomOrder(BaseSchema):
    # Catalog swagger.json

    
    is_custom_order = fields.Boolean(required=False)
    
    manufacturing_time = fields.Int(required=False)
    
    manufacturing_time_unit = fields.Str(required=False)
    


class ReturnConfig(BaseSchema):
    # Catalog swagger.json

    
    time = fields.Int(required=False)
    
    unit = fields.Str(required=False)
    
    returnable = fields.Boolean(required=False)
    


class NetQuantity(BaseSchema):
    # Catalog swagger.json

    
    unit = fields.Str(required=False)
    
    value = fields.Float(required=False)
    


class TaxIdentifier(BaseSchema):
    # Catalog swagger.json

    
    hsn_code = fields.Str(required=False)
    
    hsn_code_id = fields.Str(required=False)
    
    reporting_hsn = fields.Str(required=False)
    


class TeaserTag(BaseSchema):
    # Catalog swagger.json

    
    tag = fields.Str(required=False)
    
    url = fields.Str(required=False)
    


class ProductPublish1(BaseSchema):
    # Catalog swagger.json

    
    is_set = fields.Boolean(required=False)
    
    product_online_date = fields.Str(required=False)
    


class ProductCreateUpdateSchemaV2(BaseSchema):
    # Catalog swagger.json

    
    trader = fields.List(fields.Nested(Trader, required=False), required=False)
    
    uid = fields.Int(required=False)
    
    is_image_less_product = fields.Boolean(required=False)
    
    custom_order = fields.Nested(CustomOrder, required=False)
    
    no_of_boxes = fields.Int(required=False)
    
    country_of_origin = fields.Str(required=False)
    
    departments = fields.List(fields.Int(required=False), required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    bulk_job_id = fields.Str(required=False)
    
    is_set = fields.Boolean(required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    media = fields.List(fields.Nested(Media1, required=False), required=False)
    
    variant_media = fields.Dict(required=False)
    
    multi_size = fields.Boolean(required=False)
    
    attributes = fields.Dict(required=False)
    
    return_config = fields.Nested(ReturnConfig, required=False)
    
    category_slug = fields.Str(required=False)
    
    item_code = fields.Str(required=False)
    
    variants = fields.Dict(required=False)
    
    requester = fields.Str(required=False)
    
    template_tag = fields.Str(required=False)
    
    net_quantity = fields.Nested(NetQuantity, required=False)
    
    is_dependent = fields.Boolean(required=False)
    
    variant_group = fields.Dict(required=False)
    
    tax_identifier = fields.Nested(TaxIdentifier, required=False)
    
    product_group_tag = fields.List(fields.Str(required=False), required=False)
    
    currency = fields.Str(required=False)
    
    size_guide = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    short_description = fields.Str(required=False)
    
    sizes = fields.List(fields.Dict(required=False), required=False)
    
    name = fields.Str(required=False)
    
    change_request_id = fields.Raw(required=False)
    
    brand_uid = fields.Int(required=False)
    
    slug = fields.Str(required=False)
    
    action = fields.Str(required=False)
    
    teaser_tag = fields.Nested(TeaserTag, required=False)
    
    is_active = fields.Boolean(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    item_type = fields.Str(required=False)
    
    product_publish = fields.Nested(ProductPublish1, required=False)
    


class ProductVariants(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    media = fields.List(fields.Nested(Media1, required=False), required=False)
    
    brand_uid = fields.Int(required=False)
    
    category_uid = fields.Int(required=False)
    
    item_code = fields.Str(required=False)
    


class ProductVariantsResponse(BaseSchema):
    # Catalog swagger.json

    
    variants = fields.List(fields.Nested(ProductVariants, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class AttributeMasterSerializer(BaseSchema):
    # Catalog swagger.json

    
    filters = fields.Nested(AttributeMasterFilter, required=False)
    
    departments = fields.List(fields.Str(required=False), required=False)
    
    synonyms = fields.Dict(required=False)
    
    raw_key = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    schema = fields.Nested(AttributeMaster, required=False)
    
    modified_by = fields.Dict(required=False)
    
    enabled_for_end_consumer = fields.Boolean(required=False)
    
    created_on = fields.Str(required=False)
    
    is_nested = fields.Boolean(required=False)
    
    unit = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    details = fields.Nested(AttributeMasterDetails, required=False)
    
    created_by = fields.Dict(required=False)
    
    logo = fields.Str(required=False)
    
    suggestion = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    variant = fields.Boolean(required=False)
    


class ProductAttributesResponse(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(AttributeMasterSerializer, required=False), required=False)
    


class SingleProductResponse(BaseSchema):
    # Catalog swagger.json

    
    data = fields.Nested(ProductSchemaV2, required=False)
    


class ValidateIdentifier(BaseSchema):
    # Catalog swagger.json

    
    gtin_value = fields.Str(required=False)
    
    primary = fields.Boolean(required=False)
    
    gtin_type = fields.Str(required=False)
    


class AllSizes(BaseSchema):
    # Catalog swagger.json

    
    identifiers = fields.List(fields.Nested(ValidateIdentifier, required=False), required=False)
    
    item_height = fields.Float(required=False)
    
    item_dimensions_unit_of_measure = fields.Str(required=False)
    
    item_weight_unit_of_measure = fields.Str(required=False)
    
    size = fields.Str(required=False)
    
    item_length = fields.Float(required=False)
    
    item_width = fields.Float(required=False)
    
    item_weight = fields.Float(required=False)
    


class GetAllSizes(BaseSchema):
    # Catalog swagger.json

    
    all_sizes = fields.List(fields.Nested(AllSizes, required=False), required=False)
    


class ValidateProduct(BaseSchema):
    # Catalog swagger.json

    
    valid = fields.Boolean(required=False)
    


class ProductPublished(BaseSchema):
    # Catalog swagger.json

    
    is_set = fields.Boolean(required=False)
    
    product_online_date = fields.Int(required=False)
    


class Product(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    trader = fields.List(fields.Nested(Trader, required=False), required=False)
    
    is_image_less_product = fields.Boolean(required=False)
    
    verified_by = fields.Nested(VerifiedBy, required=False)
    
    custom_order = fields.Dict(required=False)
    
    images = fields.List(fields.Nested(Image, required=False), required=False)
    
    primary_color = fields.Str(required=False)
    
    no_of_boxes = fields.Int(required=False)
    
    country_of_origin = fields.Str(required=False)
    
    departments = fields.List(fields.Int(required=False), required=False)
    
    all_company_ids = fields.List(fields.Int(required=False), required=False)
    
    image_nature = fields.Str(required=False)
    
    all_sizes = fields.List(fields.Dict(required=False), required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    category = fields.Dict(required=False)
    
    pending = fields.Str(required=False)
    
    l3_mapping = fields.List(fields.Str(required=False), required=False)
    
    modified_by = fields.Dict(required=False)
    
    is_set = fields.Boolean(required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    media = fields.List(fields.Nested(Media1, required=False), required=False)
    
    created_on = fields.Str(required=False)
    
    variant_media = fields.Dict(required=False)
    
    multi_size = fields.Boolean(required=False)
    
    attributes = fields.Dict(required=False)
    
    moq = fields.Dict(required=False)
    
    color = fields.Str(required=False)
    
    return_config = fields.Nested(ReturnConfigResponse, required=False)
    
    brand = fields.Nested(Brand, required=False)
    
    category_slug = fields.Str(required=False)
    
    item_code = fields.Str(required=False)
    
    variants = fields.Dict(required=False)
    
    id = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    template_tag = fields.Str(required=False)
    
    net_quantity = fields.Nested(NetQuantityResponse, required=False)
    
    hsn_code = fields.Str(required=False)
    
    is_dependent = fields.Boolean(required=False)
    
    variant_group = fields.Dict(required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    category_uid = fields.Int(required=False)
    
    product_group_tag = fields.List(fields.Str(required=False), required=False)
    
    currency = fields.Str(required=False)
    
    is_expirable = fields.Boolean(required=False)
    
    size_guide = fields.Str(required=False)
    
    created_by = fields.Dict(required=False)
    
    description = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    stage = fields.Str(required=False)
    
    short_description = fields.Str(required=False)
    
    sizes = fields.List(fields.Dict(required=False), required=False)
    
    name = fields.Str(required=False)
    
    brand_uid = fields.Int(required=False)
    
    slug = fields.Str(required=False)
    
    verified_on = fields.Str(required=False)
    
    teaser_tag = fields.Dict(required=False)
    
    is_active = fields.Boolean(required=False)
    
    all_identifiers = fields.List(fields.Str(required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    is_physical = fields.Boolean(required=False)
    
    item_type = fields.Str(required=False)
    
    product_publish = fields.Nested(ProductPublished, required=False)
    


class ProductListingResponse(BaseSchema):
    # Catalog swagger.json

    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(Product, required=False), required=False)
    


class UserDetail1(BaseSchema):
    # Catalog swagger.json

    
    username = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
    full_name = fields.Str(required=False)
    


class ProductBulkRequest(BaseSchema):
    # Catalog swagger.json

    
    stage = fields.Str(required=False)
    
    cancelled_records = fields.List(fields.Str(required=False), required=False)
    
    modified_on = fields.Str(required=False)
    
    template_tag = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    total = fields.Int(required=False)
    
    file_path = fields.Str(required=False)
    
    failed = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    cancelled = fields.Int(required=False)
    
    template = fields.Nested(ProductTemplate, required=False)
    
    created_by = fields.Nested(UserDetail1, required=False)
    
    succeed = fields.Int(required=False)
    
    company_id = fields.Int(required=False)
    
    failed_records = fields.List(fields.Str(required=False), required=False)
    
    modified_by = fields.Nested(UserDetail1, required=False)
    


class ProductBulkRequestList(BaseSchema):
    # Catalog swagger.json

    
    page = fields.Nested(Page, required=False)
    
    items = fields.Nested(ProductBulkRequest, required=False)
    


class BulkJob(BaseSchema):
    # Catalog swagger.json

    
    stage = fields.Str(required=False)
    
    cancelled_records = fields.List(fields.Dict(required=False), required=False)
    
    modified_on = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    template_tag = fields.Str(required=False)
    
    total = fields.Int(required=False)
    
    custom_template_tag = fields.Str(required=False)
    
    file_path = fields.Str(required=False)
    
    cancelled = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    failed = fields.Int(required=False)
    
    tracking_url = fields.Str(required=False)
    
    created_by = fields.Nested(UserInfo1, required=False)
    
    succeed = fields.Int(required=False)
    
    company_id = fields.Int(required=False)
    
    failed_records = fields.List(fields.Dict(required=False), required=False)
    
    modified_by = fields.Nested(UserInfo1, required=False)
    


class BulkResponse(BaseSchema):
    # Catalog swagger.json

    
    modified_on = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    batch_id = fields.Str(required=False)
    
    created_by = fields.Nested(UserInfo1, required=False)
    
    modified_by = fields.Nested(UserInfo1, required=False)
    


class BulkProductRequest(BaseSchema):
    # Catalog swagger.json

    
    template_tag = fields.Str(required=False)
    
    batch_id = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    data = fields.List(fields.Dict(required=False), required=False)
    


class ProductTagsViewResponse(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Str(required=False), required=False)
    


class UserCommon(BaseSchema):
    # Catalog swagger.json

    
    username = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    


class Items(BaseSchema):
    # Catalog swagger.json

    
    stage = fields.Str(required=False)
    
    cancelled_records = fields.List(fields.Str(required=False), required=False)
    
    id = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    total = fields.Int(required=False)
    
    file_path = fields.Str(required=False)
    
    failed = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    retry = fields.Int(required=False)
    
    cancelled = fields.Int(required=False)
    
    tracking_url = fields.Str(required=False)
    
    created_by = fields.Nested(UserCommon, required=False)
    
    succeed = fields.Int(required=False)
    
    company_id = fields.Int(required=False)
    
    failed_records = fields.List(fields.Str(required=False), required=False)
    
    modified_by = fields.Nested(UserCommon, required=False)
    


class BulkAssetResponse(BaseSchema):
    # Catalog swagger.json

    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(Items, required=False), required=False)
    


class ProductBulkAssets(BaseSchema):
    # Catalog swagger.json

    
    user = fields.Dict(required=False)
    
    company_id = fields.Int(required=False)
    
    url = fields.Str(required=False)
    


class ProductSizeDeleteDataResponse(BaseSchema):
    # Catalog swagger.json

    
    item_id = fields.Int(required=False)
    
    company_id = fields.Int(required=False)
    
    size = fields.Str(required=False)
    


class ProductSizeDeleteResponse(BaseSchema):
    # Catalog swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.Nested(ProductSizeDeleteDataResponse, required=False)
    


class InventoryResponse(BaseSchema):
    # Catalog swagger.json

    
    identifiers = fields.Dict(required=False)
    
    uid = fields.Str(required=False)
    
    store = fields.Dict(required=False)
    
    sellable_quantity = fields.Int(required=False)
    
    price_effective = fields.Float(required=False)
    
    price_transfer = fields.Float(required=False)
    
    size = fields.Str(required=False)
    
    inventory_updated_on = fields.Str(required=False)
    
    item_id = fields.Int(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    price = fields.Float(required=False)
    


class InventoryResponsePaginated(BaseSchema):
    # Catalog swagger.json

    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(InventoryResponse, required=False), required=False)
    


class ItemQuery(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    item_code = fields.Str(required=False)
    
    brand_uid = fields.Int(required=False)
    


class GTIN(BaseSchema):
    # Catalog swagger.json

    
    gtin_value = fields.Str(required=False)
    
    primary = fields.Boolean(required=False)
    
    gtin_type = fields.Str(required=False)
    


class SetSize(BaseSchema):
    # Catalog swagger.json

    
    pieces = fields.Int(required=False)
    
    size = fields.Str(required=False)
    


class SizeDistribution(BaseSchema):
    # Catalog swagger.json

    
    sizes = fields.List(fields.Nested(SetSize, required=False), required=False)
    


class InventorySet(BaseSchema):
    # Catalog swagger.json

    
    quantity = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    size_distribution = fields.Nested(SizeDistribution, required=False)
    


class InvSize(BaseSchema):
    # Catalog swagger.json

    
    item_height = fields.Float(required=False)
    
    is_set = fields.Boolean(required=False)
    
    identifiers = fields.List(fields.Nested(GTIN, required=False), required=False)
    
    item_dimensions_unit_of_measure = fields.Str(required=False)
    
    expiration_date = fields.Str(required=False)
    
    price_effective = fields.Float(required=False)
    
    item_weight_unit_of_measure = fields.Str(required=False)
    
    set = fields.Nested(InventorySet, required=False)
    
    price_transfer = fields.Float(required=False)
    
    size = fields.Str(required=False)
    
    store_code = fields.Str(required=False)
    
    item_length = fields.Float(required=False)
    
    item_width = fields.Float(required=False)
    
    item_weight = fields.Float(required=False)
    
    currency = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    price = fields.Float(required=False)
    


class InventoryRequest(BaseSchema):
    # Catalog swagger.json

    
    item = fields.Nested(ItemQuery, required=False)
    
    sizes = fields.List(fields.Nested(InvSize, required=False), required=False)
    
    company_id = fields.Int(required=False)
    


class Trader1(BaseSchema):
    # Catalog swagger.json

    
    address = fields.List(fields.Str(required=False), required=False)
    
    name = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class WeightResponse(BaseSchema):
    # Catalog swagger.json

    
    shipping = fields.Float(required=False)
    
    unit = fields.Str(required=False)
    
    is_default = fields.Boolean(required=False)
    


class CompanyMeta(BaseSchema):
    # Catalog swagger.json

    
    id = fields.Int(required=False)
    


class ReturnConfig1(BaseSchema):
    # Catalog swagger.json

    
    time = fields.Int(required=False)
    
    unit = fields.Str(required=False)
    
    returnable = fields.Boolean(required=False)
    


class BrandMeta(BaseSchema):
    # Catalog swagger.json

    
    id = fields.Int(required=False)
    
    name = fields.Str(required=False)
    


class PriceMeta(BaseSchema):
    # Catalog swagger.json

    
    marked = fields.Float(required=False)
    
    updated_at = fields.Str(required=False)
    
    transfer = fields.Float(required=False)
    
    tp_notes = fields.Dict(required=False)
    
    currency = fields.Str(required=False)
    
    effective = fields.Float(required=False)
    


class StoreMeta(BaseSchema):
    # Catalog swagger.json

    
    id = fields.Int(required=False)
    


class ManufacturerResponse(BaseSchema):
    # Catalog swagger.json

    
    address = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    is_default = fields.Boolean(required=False)
    


class DimensionResponse(BaseSchema):
    # Catalog swagger.json

    
    height = fields.Float(required=False)
    
    unit = fields.Str(required=False)
    
    width = fields.Float(required=False)
    
    is_default = fields.Boolean(required=False)
    
    length = fields.Float(required=False)
    


class QuantityBase(BaseSchema):
    # Catalog swagger.json

    
    updated_at = fields.Str(required=False)
    
    count = fields.Int(required=False)
    


class Quantities(BaseSchema):
    # Catalog swagger.json

    
    order_committed = fields.Nested(QuantityBase, required=False)
    
    not_available = fields.Nested(QuantityBase, required=False)
    
    sellable = fields.Nested(QuantityBase, required=False)
    
    damaged = fields.Nested(QuantityBase, required=False)
    


class InventorySellerResponse(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Str(required=False)
    
    trader = fields.List(fields.Nested(Trader1, required=False), required=False)
    
    country_of_origin = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    identifier = fields.Dict(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    fynd_item_code = fields.Str(required=False)
    
    is_set = fields.Boolean(required=False)
    
    weight = fields.Nested(WeightResponse, required=False)
    
    set = fields.Nested(InventorySet, required=False)
    
    company = fields.Nested(CompanyMeta, required=False)
    
    size = fields.Str(required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    raw_meta = fields.Dict(required=False)
    
    return_config = fields.Nested(ReturnConfig1, required=False)
    
    trace_id = fields.Str(required=False)
    
    brand = fields.Nested(BrandMeta, required=False)
    
    price = fields.Nested(PriceMeta, required=False)
    
    fynd_article_code = fields.Str(required=False)
    
    store = fields.Nested(StoreMeta, required=False)
    
    fynd_meta = fields.Dict(required=False)
    
    fragile = fields.Boolean(required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    added_on_store = fields.Str(required=False)
    
    item_id = fields.Int(required=False)
    
    manufacturer = fields.Nested(ManufacturerResponse, required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    stage = fields.Str(required=False)
    
    total_quantity = fields.Int(required=False)
    
    meta = fields.Dict(required=False)
    
    expiration_date = fields.Str(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    dimension = fields.Nested(DimensionResponse, required=False)
    
    quantities = fields.Nested(Quantities, required=False)
    


class InventorySellerIdentifierResponsePaginated(BaseSchema):
    # Catalog swagger.json

    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(InventorySellerResponse, required=False), required=False)
    


class Trader2(BaseSchema):
    # Catalog swagger.json

    
    address = fields.List(fields.Str(required=False), required=False)
    
    name = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class WeightResponse1(BaseSchema):
    # Catalog swagger.json

    
    shipping = fields.Float(required=False)
    
    unit = fields.Str(required=False)
    


class CompanyMeta1(BaseSchema):
    # Catalog swagger.json

    
    id = fields.Int(required=False)
    


class ReturnConfig2(BaseSchema):
    # Catalog swagger.json

    
    time = fields.Int(required=False)
    
    unit = fields.Str(required=False)
    
    returnable = fields.Boolean(required=False)
    


class BrandMeta1(BaseSchema):
    # Catalog swagger.json

    
    id = fields.Int(required=False)
    
    name = fields.Str(required=False)
    


class PriceArticle(BaseSchema):
    # Catalog swagger.json

    
    marked = fields.Float(required=False)
    
    transfer = fields.Float(required=False)
    
    tp_notes = fields.Dict(required=False)
    
    currency = fields.Str(required=False)
    
    effective = fields.Float(required=False)
    


class ArticleStoreResponse(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    store_type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    store_code = fields.Str(required=False)
    


class DateMeta(BaseSchema):
    # Catalog swagger.json

    
    created_on = fields.Str(required=False)
    
    inventory_updated_on = fields.Str(required=False)
    
    added_on_store = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    


class ManufacturerResponse1(BaseSchema):
    # Catalog swagger.json

    
    address = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    is_default = fields.Boolean(required=False)
    


class DimensionResponse1(BaseSchema):
    # Catalog swagger.json

    
    length = fields.Float(required=False)
    
    height = fields.Float(required=False)
    
    unit = fields.Str(required=False)
    
    width = fields.Float(required=False)
    


class Quantity(BaseSchema):
    # Catalog swagger.json

    
    count = fields.Int(required=False)
    


class QuantitiesArticle(BaseSchema):
    # Catalog swagger.json

    
    order_committed = fields.Nested(Quantity, required=False)
    
    not_available = fields.Nested(Quantity, required=False)
    
    sellable = fields.Nested(Quantity, required=False)
    
    damaged = fields.Nested(Quantity, required=False)
    


class GetInventories(BaseSchema):
    # Catalog swagger.json

    
    trader = fields.List(fields.Nested(Trader2, required=False), required=False)
    
    uid = fields.Str(required=False)
    
    country_of_origin = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    identifier = fields.Dict(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    is_set = fields.Boolean(required=False)
    
    weight = fields.Nested(WeightResponse1, required=False)
    
    company = fields.Nested(CompanyMeta1, required=False)
    
    size = fields.Str(required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    return_config = fields.Nested(ReturnConfig2, required=False)
    
    trace_id = fields.Str(required=False)
    
    brand = fields.Nested(BrandMeta1, required=False)
    
    price = fields.Nested(PriceArticle, required=False)
    
    store = fields.Nested(ArticleStoreResponse, required=False)
    
    id = fields.Str(required=False)
    
    date_meta = fields.Nested(DateMeta, required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    inventory_updated_on = fields.Str(required=False)
    
    item_id = fields.Int(required=False)
    
    manufacturer = fields.Nested(ManufacturerResponse1, required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    stage = fields.Str(required=False)
    
    total_quantity = fields.Int(required=False)
    
    expiration_date = fields.Str(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    dimension = fields.Nested(DimensionResponse1, required=False)
    
    platforms = fields.Dict(required=False)
    
    quantities = fields.Nested(QuantitiesArticle, required=False)
    


class GetInventoriesResponse(BaseSchema):
    # Catalog swagger.json

    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(GetInventories, required=False), required=False)
    


class BulkInventoryGetItems(BaseSchema):
    # Catalog swagger.json

    
    stage = fields.Str(required=False)
    
    cancelled_records = fields.List(fields.Str(required=False), required=False)
    
    id = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    total = fields.Int(required=False)
    
    file_path = fields.Str(required=False)
    
    cancelled = fields.Int(required=False)
    
    failed = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    created_by = fields.Dict(required=False)
    
    succeed = fields.Int(required=False)
    
    company_id = fields.Int(required=False)
    
    failed_records = fields.List(fields.Str(required=False), required=False)
    
    modified_by = fields.Dict(required=False)
    


class BulkInventoryGet(BaseSchema):
    # Catalog swagger.json

    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(BulkInventoryGetItems, required=False), required=False)
    


class InventoryJobPayload(BaseSchema):
    # Catalog swagger.json

    
    item_dimensions_unit_of_measure = fields.Str(required=False)
    
    total_quantity = fields.Int(required=False)
    
    expiration_date = fields.Str(required=False)
    
    price_effective = fields.Float(required=False)
    
    item_weight_unit_of_measure = fields.Str(required=False)
    
    store_code = fields.Str(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    price_marked = fields.Float(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    currency = fields.Str(required=False)
    
    trace_id = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    price = fields.Float(required=False)
    


class InventoryBulkRequest(BaseSchema):
    # Catalog swagger.json

    
    user = fields.Dict(required=False)
    
    sizes = fields.List(fields.Nested(InventoryJobPayload, required=False), required=False)
    
    company_id = fields.Int(required=False)
    
    batch_id = fields.Str(required=False)
    


class InventoryExportQuantityFilter(BaseSchema):
    # Catalog swagger.json

    
    operators = fields.Str(required=False)
    
    min = fields.Int(required=False)
    
    max = fields.Int(required=False)
    


class InventoryExportAdvanceOption(BaseSchema):
    # Catalog swagger.json

    
    to_date = fields.Str(required=False)
    
    store_ids = fields.List(fields.Int(required=False), required=False)
    
    from_date = fields.Str(required=False)
    
    brand_ids = fields.List(fields.Int(required=False), required=False)
    
    quantity = fields.Nested(InventoryExportQuantityFilter, required=False)
    


class InventoryExportJob(BaseSchema):
    # Catalog swagger.json

    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    status = fields.Str(required=False)
    
    seller_id = fields.Int(required=False)
    
    filters = fields.Nested(InventoryExportAdvanceOption, required=False)
    
    completed_on = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    task_id = fields.Str(required=False)
    
    url = fields.Str(required=False)
    


class InventoryExportRequest(BaseSchema):
    # Catalog swagger.json

    
    store = fields.List(fields.Int(required=False), required=False)
    
    type = fields.Str(required=False)
    
    brand = fields.List(fields.Int(required=False), required=False)
    


class InventoryExportResponse(BaseSchema):
    # Catalog swagger.json

    
    modified_on = fields.Str(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    created_on = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    seller_id = fields.Int(required=False)
    
    filters = fields.Dict(required=False)
    
    type = fields.Str(required=False)
    
    created_by = fields.Str(required=False)
    
    task_id = fields.Str(required=False)
    


class InventoryJobFilters(BaseSchema):
    # Catalog swagger.json

    
    brands = fields.List(fields.Str(required=False), required=False)
    
    to_date = fields.Str(required=False)
    
    from_date = fields.Str(required=False)
    
    stores = fields.List(fields.Str(required=False), required=False)
    
    quantity = fields.Nested(InventoryExportQuantityFilter, required=False)
    


class InventoryJobDetailResponse(BaseSchema):
    # Catalog swagger.json

    
    id = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    created_on = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    seller_id = fields.Int(required=False)
    
    filters = fields.Nested(InventoryJobFilters, required=False)
    
    completed_on = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    cancelled_on = fields.Str(required=False)
    
    created_by = fields.Nested(UserDetail, required=False)
    
    cancelled_by = fields.Nested(UserDetail, required=False)
    
    task_id = fields.Str(required=False)
    
    url = fields.Str(required=False)
    


class InventoryExportJobListResponse(BaseSchema):
    # Catalog swagger.json

    
    items = fields.Nested(InventoryJobDetailResponse, required=False)
    


class InventoryExportFilter(BaseSchema):
    # Catalog swagger.json

    
    to_date = fields.Str(required=False)
    
    store_ids = fields.List(fields.Int(required=False), required=False)
    
    from_date = fields.Str(required=False)
    
    brand_ids = fields.List(fields.Int(required=False), required=False)
    
    quantity = fields.Nested(InventoryExportQuantityFilter, required=False)
    


class InventoryCreateRequest(BaseSchema):
    # Catalog swagger.json

    
    data = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    filters = fields.Nested(InventoryExportFilter, required=False)
    


class InventoryPartialExportRequest(BaseSchema):
    # Catalog swagger.json

    
    status = fields.Str(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    


class InventoryExportCreateFilters(BaseSchema):
    # Catalog swagger.json

    
    to_date = fields.Str(required=False)
    
    store_ids = fields.List(fields.Int(required=False), required=False)
    
    from_date = fields.Str(required=False)
    
    brand_ids = fields.List(fields.Int(required=False), required=False)
    
    quantity = fields.Nested(InventoryExportQuantityFilter, required=False)
    


class InventoryExportCreateResponse(BaseSchema):
    # Catalog swagger.json

    
    id = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    created_on = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    seller_id = fields.Int(required=False)
    
    filters = fields.Nested(InventoryExportCreateFilters, required=False)
    
    completed_on = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    cancelled_on = fields.Str(required=False)
    
    created_by = fields.Nested(UserDetail, required=False)
    
    cancelled_by = fields.Nested(UserDetail, required=False)
    
    task_id = fields.Str(required=False)
    
    url = fields.Str(required=False)
    


class FilerList(BaseSchema):
    # Catalog swagger.json

    
    value = fields.Str(required=False)
    
    display = fields.Str(required=False)
    


class InventoryConfig(BaseSchema):
    # Catalog swagger.json

    
    multivalues = fields.Boolean(required=False)
    
    data = fields.List(fields.Nested(FilerList, required=False), required=False)
    


class InventoryPayload(BaseSchema):
    # Catalog swagger.json

    
    total_quantity = fields.Int(required=False)
    
    expiration_date = fields.Str(required=False)
    
    price_effective = fields.Float(required=False)
    
    store_id = fields.Int(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    price_marked = fields.Float(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    trace_id = fields.Str(required=False)
    


class InventoryRequestSchemaV2(BaseSchema):
    # Catalog swagger.json

    
    meta = fields.Dict(required=False)
    
    payload = fields.List(fields.Nested(InventoryPayload, required=False), required=False)
    
    company_id = fields.Int(required=False)
    


class InventoryFailedReason(BaseSchema):
    # Catalog swagger.json

    
    message = fields.Str(required=False)
    
    errors = fields.Str(required=False)
    


class InventoryResponseItem(BaseSchema):
    # Catalog swagger.json

    
    data = fields.Nested(InventoryPayload, required=False)
    
    reason = fields.Nested(InventoryFailedReason, required=False)
    


class InventoryUpdateResponse(BaseSchema):
    # Catalog swagger.json

    
    message = fields.Str(required=False)
    
    items = fields.List(fields.Nested(InventoryResponseItem, required=False), required=False)
    


class HsnCodesObject(BaseSchema):
    # Catalog swagger.json

    
    tax_on_mrp = fields.Boolean(required=False)
    
    id = fields.Str(required=False)
    
    threshold1 = fields.Float(required=False)
    
    modified_on = fields.Str(required=False)
    
    threshold2 = fields.Float(required=False)
    
    hsn_code = fields.Str(required=False)
    
    tax1 = fields.Float(required=False)
    
    tax2 = fields.Float(required=False)
    
    hs2_code = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    tax_on_esp = fields.Boolean(required=False)
    


class HsnCode(BaseSchema):
    # Catalog swagger.json

    
    data = fields.Nested(HsnCodesObject, required=False)
    


class HsnUpsert(BaseSchema):
    # Catalog swagger.json

    
    tax_on_mrp = fields.Boolean(required=False)
    
    uid = fields.Int(required=False)
    
    threshold1 = fields.Float(required=False)
    
    threshold2 = fields.Float(required=False)
    
    hsn_code = fields.Str(required=False)
    
    tax1 = fields.Float(required=False)
    
    tax2 = fields.Float(required=False)
    
    is_active = fields.Boolean(required=False)
    
    hs2_code = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    tax_on_esp = fields.Boolean(required=False)
    


class BulkHsnUpsert(BaseSchema):
    # Catalog swagger.json

    
    data = fields.List(fields.Nested(HsnUpsert, required=False), required=False)
    


class BulkHsnResponse(BaseSchema):
    # Catalog swagger.json

    
    success = fields.Boolean(required=False)
    


class PageResponse(BaseSchema):
    # Catalog swagger.json

    
    has_next = fields.Boolean(required=False)
    
    size = fields.Int(required=False)
    
    current = fields.Str(required=False)
    
    item_total = fields.Int(required=False)
    
    has_previous = fields.Boolean(required=False)
    


class TaxSlab(BaseSchema):
    # Catalog swagger.json

    
    threshold = fields.Float(required=False)
    
    rate = fields.Float(required=False)
    
    cess = fields.Float(required=False)
    
    effective_date = fields.Str(required=False)
    


class HSNDataInsertV2(BaseSchema):
    # Catalog swagger.json

    
    country_code = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    hsn_code = fields.Str(required=False)
    
    taxes = fields.List(fields.Nested(TaxSlab, required=False), required=False)
    
    type = fields.Str(required=False)
    
    created_by = fields.Dict(required=False)
    
    description = fields.Str(required=False)
    
    hsn_code_id = fields.Str(required=False)
    
    reporting_hsn = fields.Str(required=False)
    
    modified_by = fields.Dict(required=False)
    


class HsnCodesListingResponseSchemaV2(BaseSchema):
    # Catalog swagger.json

    
    page = fields.Nested(PageResponse, required=False)
    
    items = fields.List(fields.Nested(HSNDataInsertV2, required=False), required=False)
    


class BrandItem(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    discount = fields.Str(required=False)
    
    action = fields.Nested(Action, required=False)
    
    departments = fields.List(fields.Str(required=False), required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    logo = fields.Nested(Media, required=False)
    


class BrandListingResponse(BaseSchema):
    # Catalog swagger.json

    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(BrandItem, required=False), required=False)
    


class Department(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    priority_order = fields.Int(required=False)
    
    slug = fields.Str(required=False)
    
    logo = fields.Nested(Media, required=False)
    


class DepartmentResponse(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(Department, required=False), required=False)
    


class DepartmentIdentifier(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    slug = fields.Str(required=False)
    


class ThirdLevelChild(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    childs = fields.List(fields.Dict(required=False), required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    action = fields.Nested(Action, required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    _custom_json = fields.Dict(required=False)
    


class SecondLevelChild(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    childs = fields.List(fields.Nested(ThirdLevelChild, required=False), required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    action = fields.Nested(Action, required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    _custom_json = fields.Dict(required=False)
    


class Child(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    childs = fields.List(fields.Nested(SecondLevelChild, required=False), required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    action = fields.Nested(Action, required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    _custom_json = fields.Dict(required=False)
    


class CategoryItems(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    childs = fields.List(fields.Nested(Child, required=False), required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    action = fields.Nested(Action, required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    


class DepartmentCategoryTree(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(CategoryItems, required=False), required=False)
    
    department = fields.Str(required=False)
    


class CategoryListingResponse(BaseSchema):
    # Catalog swagger.json

    
    departments = fields.List(fields.Nested(DepartmentIdentifier, required=False), required=False)
    
    data = fields.List(fields.Nested(DepartmentCategoryTree, required=False), required=False)
    


class ApplicationProductListingResponse(BaseSchema):
    # Catalog swagger.json

    
    page = fields.Nested(Page, required=False)
    
    filters = fields.List(fields.Nested(ProductFilters, required=False), required=False)
    
    sort_on = fields.List(fields.Nested(ProductSortOn, required=False), required=False)
    
    operators = fields.Dict(required=False)
    
    items = fields.List(fields.Nested(ProductListingDetail, required=False), required=False)
    


class ProductDetail(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    similars = fields.List(fields.Str(required=False), required=False)
    
    rating_count = fields.Int(required=False)
    
    medias = fields.List(fields.Nested(Media1, required=False), required=False)
    
    image_nature = fields.Str(required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    rating = fields.Float(required=False)
    
    color = fields.Str(required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    brand = fields.Nested(ProductBrand, required=False)
    
    has_variant = fields.Boolean(required=False)
    
    item_code = fields.Str(required=False)
    
    promo_meta = fields.Dict(required=False)
    
    type = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    short_description = fields.Str(required=False)
    
    grouped_attributes = fields.List(fields.Nested(ProductDetailGroupedAttribute, required=False), required=False)
    
    name = fields.Str(required=False)
    
    product_online_date = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    teaser_tag = fields.Dict(required=False)
    
    attributes = fields.Dict(required=False)
    
    item_type = fields.Str(required=False)
    


class InventoryPage(BaseSchema):
    # Catalog swagger.json

    
    has_next = fields.Boolean(required=False)
    
    item_total = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    next_id = fields.Str(required=False)
    


class InventoryStockResponse(BaseSchema):
    # Catalog swagger.json

    
    page = fields.Nested(InventoryPage, required=False)
    
    items = fields.List(fields.Dict(required=False), required=False)
    


class ArticleQuery(BaseSchema):
    # Catalog swagger.json

    
    item_id = fields.Int(required=False)
    
    ignored_stores = fields.List(fields.Int(required=False), required=False)
    
    size = fields.Str(required=False)
    


class ArticleAssignment(BaseSchema):
    # Catalog swagger.json

    
    strategy = fields.Str(required=False)
    
    level = fields.Str(required=False)
    


class AssignStoreArticle(BaseSchema):
    # Catalog swagger.json

    
    meta = fields.Dict(required=False)
    
    query = fields.Nested(ArticleQuery, required=False)
    
    article_assignment = fields.Nested(ArticleAssignment, required=False)
    
    quantity = fields.Int(required=False)
    
    group_id = fields.Str(required=False)
    


class AssignStore(BaseSchema):
    # Catalog swagger.json

    
    pincode = fields.Str(required=False)
    
    channel_type = fields.Str(required=False)
    
    channel_identifier = fields.Str(required=False)
    
    store_ids = fields.List(fields.Int(required=False), required=False)
    
    app_id = fields.Str(required=False)
    
    articles = fields.List(fields.Nested(AssignStoreArticle, required=False), required=False)
    
    company_id = fields.Int(required=False)
    


class ArticleAssignment1(BaseSchema):
    # Catalog swagger.json

    
    strategy = fields.Str(required=False)
    
    level = fields.Str(required=False)
    


class StoreAssignResponse(BaseSchema):
    # Catalog swagger.json

    
    _id = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    status = fields.Boolean(required=False)
    
    price_effective = fields.Int(required=False)
    
    group_id = fields.Str(required=False)
    
    store_id = fields.Int(required=False)
    
    size = fields.Str(required=False)
    
    article_assignment = fields.Nested(ArticleAssignment1, required=False)
    
    item_id = fields.Int(required=False)
    
    price_marked = fields.Int(required=False)
    
    strategy_wise_listing = fields.List(fields.Dict(required=False), required=False)
    
    index = fields.Int(required=False)
    
    quantity = fields.Int(required=False)
    
    company_id = fields.Int(required=False)
    
    s_city = fields.Str(required=False)
    
    store_pincode = fields.Int(required=False)
    


class UserSerializer1(BaseSchema):
    # Catalog swagger.json

    
    username = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
    contact = fields.Str(required=False)
    


class GetAddressSerializer(BaseSchema):
    # Catalog swagger.json

    
    address2 = fields.Str(required=False)
    
    pincode = fields.Int(required=False)
    
    country_code = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    latitude = fields.Float(required=False)
    
    longitude = fields.Float(required=False)
    
    landmark = fields.Str(required=False)
    
    address1 = fields.Str(required=False)
    
    address_type = fields.Str(required=False)
    


class UserSerializer2(BaseSchema):
    # Catalog swagger.json

    
    username = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
    contact = fields.Str(required=False)
    


class GetCompanySerializer(BaseSchema):
    # Catalog swagger.json

    
    stage = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    business_type = fields.Str(required=False)
    
    addresses = fields.List(fields.Nested(GetAddressSerializer, required=False), required=False)
    
    verified_by = fields.Nested(UserSerializer2, required=False)
    
    name = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    company_type = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    verified_on = fields.Str(required=False)
    
    reject_reason = fields.Str(required=False)
    
    created_by = fields.Nested(UserSerializer2, required=False)
    
    modified_by = fields.Nested(UserSerializer2, required=False)
    


class ProductReturnConfigSerializer(BaseSchema):
    # Catalog swagger.json

    
    store_uid = fields.Int(required=False)
    
    on_same_store = fields.Boolean(required=False)
    


class LocationIntegrationType(BaseSchema):
    # Catalog swagger.json

    
    inventory = fields.Str(required=False)
    
    order = fields.Str(required=False)
    


class SellerPhoneNumber(BaseSchema):
    # Catalog swagger.json

    
    number = fields.Str(required=False)
    
    country_code = fields.Int(required=False)
    


class LocationManagerSerializer(BaseSchema):
    # Catalog swagger.json

    
    email = fields.Str(required=False)
    
    mobile_no = fields.Nested(SellerPhoneNumber, required=False)
    
    name = fields.Str(required=False)
    


class InvoiceCredSerializer(BaseSchema):
    # Catalog swagger.json

    
    username = fields.Str(required=False)
    
    password = fields.Str(required=False)
    
    enabled = fields.Boolean(required=False)
    


class InvoiceDetailsSerializer(BaseSchema):
    # Catalog swagger.json

    
    e_invoice = fields.Nested(InvoiceCredSerializer, required=False)
    
    e_waybill = fields.Nested(InvoiceCredSerializer, required=False)
    


class Document(BaseSchema):
    # Catalog swagger.json

    
    legal_name = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    verified = fields.Boolean(required=False)
    
    url = fields.Str(required=False)
    


class LocationTimingSerializer(BaseSchema):
    # Catalog swagger.json

    
    minute = fields.Int(required=False)
    
    hour = fields.Int(required=False)
    


class LocationDayWiseSerializer(BaseSchema):
    # Catalog swagger.json

    
    weekday = fields.Str(required=False)
    
    closing = fields.Nested(LocationTimingSerializer, required=False)
    
    open = fields.Boolean(required=False)
    
    opening = fields.Nested(LocationTimingSerializer, required=False)
    


class GetLocationSerializer(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    verified_by = fields.Nested(UserSerializer1, required=False)
    
    phone_number = fields.Str(required=False)
    
    modified_by = fields.Nested(UserSerializer1, required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    created_on = fields.Str(required=False)
    
    company = fields.Nested(GetCompanySerializer, required=False)
    
    product_return_config = fields.Nested(ProductReturnConfigSerializer, required=False)
    
    store_type = fields.Str(required=False)
    
    address = fields.Nested(GetAddressSerializer, required=False)
    
    modified_on = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    warnings = fields.Dict(required=False)
    
    created_by = fields.Nested(UserSerializer1, required=False)
    
    integration_type = fields.Nested(LocationIntegrationType, required=False)
    
    display_name = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    manager = fields.Nested(LocationManagerSerializer, required=False)
    
    gst_credentials = fields.Nested(InvoiceDetailsSerializer, required=False)
    
    name = fields.Str(required=False)
    
    verified_on = fields.Str(required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    timing = fields.List(fields.Nested(LocationDayWiseSerializer, required=False), required=False)
    


class LocationListSerializer(BaseSchema):
    # Catalog swagger.json

    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(GetLocationSerializer, required=False), required=False)
    


class ApplicationBrandJson(BaseSchema):
    # Catalog swagger.json

    
    _custom_json = fields.Dict(required=False)
    


class ApplicationCategoryJson(BaseSchema):
    # Catalog swagger.json

    
    _custom_json = fields.Dict(required=False)
    


class ApplicationDepartment(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    app_id = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    logo = fields.Str(required=False)
    


class ApplicationDepartmentListingResponse(BaseSchema):
    # Catalog swagger.json

    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(ApplicationDepartment, required=False), required=False)
    


class ApplicationDepartmentJson(BaseSchema):
    # Catalog swagger.json

    
    _custom_json = fields.Dict(required=False)
    


class ApplicationStoreJson(BaseSchema):
    # Catalog swagger.json

    
    _custom_json = fields.Dict(required=False)
    

