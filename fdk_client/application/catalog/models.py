"""Catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..ApplicationModel import BaseSchema




class ProductDetailCustomOrder(BaseSchema):
    pass


class Meta(BaseSchema):
    pass


class Media(BaseSchema):
    pass


class QueryParams(BaseSchema):
    pass


class Params(BaseSchema):
    pass


class ProductListingActionPage(BaseSchema):
    pass


class ProductListingAction(BaseSchema):
    pass


class ProductBrand(BaseSchema):
    pass


class ProductDepartment(BaseSchema):
    pass


class ProductCategoryMap(BaseSchema):
    pass


class NetQuantity(BaseSchema):
    pass


class CustomMetaFields(BaseSchema):
    pass


class ApplicationItemSeoAction(BaseSchema):
    pass


class ApplicationItemSeoBreadcrumbs(BaseSchema):
    pass


class ApplicationItemSeoMetaTagItem(BaseSchema):
    pass


class ApplicationItemSEO(BaseSchema):
    pass


class ApplicationItemSeoSitemap(BaseSchema):
    pass


class ApplicationItemSeoMetaTags(BaseSchema):
    pass


class ProductDetailAttribute(BaseSchema):
    pass


class ProductDetailGroupedAttribute(BaseSchema):
    pass


class ApplicationItemMOQ(BaseSchema):
    pass


class Price(BaseSchema):
    pass


class ProductListingPrice(BaseSchema):
    pass


class ProductSizesPrice(BaseSchema):
    pass


class ProductCompareDetail(BaseSchema):
    pass


class ProductDetail(BaseSchema):
    pass


class NotServiceableError(BaseSchema):
    pass


class ErrorResponseSchema(BaseSchema):
    pass


class Dimension(BaseSchema):
    pass


class Weight(BaseSchema):
    pass


class DiscountMeta(BaseSchema):
    pass


class ProductSize(BaseSchema):
    pass


class SizeChartValues(BaseSchema):
    pass


class ColumnHeader(BaseSchema):
    pass


class ColumnHeaders(BaseSchema):
    pass


class SizeChart(BaseSchema):
    pass


class ProductSizeStores(BaseSchema):
    pass


class ProductSizes(BaseSchema):
    pass


class MOQ(BaseSchema):
    pass


class AttributeDetail(BaseSchema):
    pass


class AttributeMetadata(BaseSchema):
    pass


class ProductsComparisonResponseSchema(BaseSchema):
    pass


class ProductCompareResponseSchema(BaseSchema):
    pass


class ProductFrequentlyComparedSimilarResponseSchema(BaseSchema):
    pass


class ProductVariantItemResponseSchema(BaseSchema):
    pass


class ProductVariantResponseSchema(BaseSchema):
    pass


class ProductVariantsResponseSchema(BaseSchema):
    pass


class StoreDetail(BaseSchema):
    pass


class ProductStockPrice(BaseSchema):
    pass


class CompanyDetail(BaseSchema):
    pass


class Seller(BaseSchema):
    pass


class ArticleIdentifier(BaseSchema):
    pass


class ProductStockStatusItem(BaseSchema):
    pass


class ProductStockStatusResponseSchema(BaseSchema):
    pass


class Page(BaseSchema):
    pass


class ProductStockPolling(BaseSchema):
    pass


class ProductVariantListingResponseSchema(BaseSchema):
    pass


class ProductListingDetail(BaseSchema):
    pass


class ProductFiltersValue(BaseSchema):
    pass


class ProductFiltersKey(BaseSchema):
    pass


class ProductFilters(BaseSchema):
    pass


class ProductSortOn(BaseSchema):
    pass


class ProductListingResponseSchema(BaseSchema):
    pass


class ImageUrls(BaseSchema):
    pass


class BrandItem(BaseSchema):
    pass


class BrandListingResponseSchema(BaseSchema):
    pass


class BrandDetailResponseSchema(BaseSchema):
    pass


class CategoryBanner(BaseSchema):
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


class DepartmentIdentifier(BaseSchema):
    pass


class CategoryListingResponseSchema(BaseSchema):
    pass


class CategoryMetaResponseSchema(BaseSchema):
    pass


class HomeListingResponseSchema(BaseSchema):
    pass


class Department(BaseSchema):
    pass


class DepartmentResponseSchema(BaseSchema):
    pass


class AutocompleteItem(BaseSchema):
    pass


class AutoCompleteResponseSchema(BaseSchema):
    pass


class CollectionQuery(BaseSchema):
    pass


class NextSchedule(BaseSchema):
    pass


class Schedule(BaseSchema):
    pass


class GetCollectionDetailNest(BaseSchema):
    pass


class CollectionListingFilterTag(BaseSchema):
    pass


class CollectionListingFilterType(BaseSchema):
    pass


class CollectionListingFilter(BaseSchema):
    pass


class GetCollectionListingResponseSchema(BaseSchema):
    pass


class CollectionDetailResponseSchema(BaseSchema):
    pass


class GetFollowListingResponseSchema(BaseSchema):
    pass


class FollowPostResponseSchema(BaseSchema):
    pass


class FollowerCountResponseSchema(BaseSchema):
    pass


class FollowIdsData(BaseSchema):
    pass


class FollowIdsResponseSchema(BaseSchema):
    pass


class LatLong(BaseSchema):
    pass


class Store(BaseSchema):
    pass


class ContactDetails(BaseSchema):
    pass


class StoreListingResponseSchema(BaseSchema):
    pass


class StoreDepartments(BaseSchema):
    pass


class AppStoreDepartment(BaseSchema):
    pass


class CompanyStore(BaseSchema):
    pass


class SellerPhoneNumber(BaseSchema):
    pass


class StoreManagerSchema(BaseSchema):
    pass


class StoreAddressSchema(BaseSchema):
    pass


class AppStore(BaseSchema):
    pass


class ProductReturnConfig(BaseSchema):
    pass


class OrderProcessingTime(BaseSchema):
    pass


class OrderTiming(BaseSchema):
    pass


class GSTCredentials(BaseSchema):
    pass


class EnabledStatus(BaseSchema):
    pass


class ApplicationStoreFilterListing(BaseSchema):
    pass


class ModifiedBy(BaseSchema):
    pass


class ApplicationStoreListing(BaseSchema):
    pass


class Time(BaseSchema):
    pass


class StoreTiming(BaseSchema):
    pass


class StoreDetails(BaseSchema):
    pass


class UserDetail(BaseSchema):
    pass


class Size(BaseSchema):
    pass


class ProductGroupPrice(BaseSchema):
    pass


class ProductDetails(BaseSchema):
    pass


class ProductInGroup(BaseSchema):
    pass


class ProductGroupingModel(BaseSchema):
    pass


class ProductBundle(BaseSchema):
    pass


class StoreV3(BaseSchema):
    pass


class ArticleAssignmentV3(BaseSchema):
    pass


class StrategyWiseListingSchemaV3(BaseSchema):
    pass


class DetailsSchemaV3(BaseSchema):
    pass


class SellerGroupAttributes(BaseSchema):
    pass


class ReturnConfigSchemaV3(BaseSchema):
    pass


class ProductSetDistributionSizeV3(BaseSchema):
    pass


class ProductSetDistributionV3(BaseSchema):
    pass


class ProductSetV3(BaseSchema):
    pass


class ProductStockPriceV3(BaseSchema):
    pass


class ProductStockUnitPriceV3(BaseSchema):
    pass


class MarketPlaceSttributesSchemaV3(BaseSchema):
    pass


class SellerV3(BaseSchema):
    pass


class PromiseSchema(BaseSchema):
    pass


class ProductSizePriceResponseV4(BaseSchema):
    pass


class ProductSizeSellerFilterSchemaV4(BaseSchema):
    pass


class ProductSizeSellersResponseV4(BaseSchema):
    pass


class ProductSizePriceV1RequestSchema(BaseSchema):
    pass


class ProductSizePriceV1RequestBody(BaseSchema):
    pass


class ProductSizePriceResponseV1(BaseSchema):
    pass


class Identifier(BaseSchema):
    pass





class ProductDetailCustomOrder(BaseSchema):
    # Catalog swagger.json

    
    manufacturing_time = fields.Int(required=False)
    
    manufacturing_time_unit = fields.Str(required=False)
    
    is_custom_order = fields.Boolean(required=False)
    


class Meta(BaseSchema):
    # Catalog swagger.json

    
    source = fields.Str(required=False)
    


class Media(BaseSchema):
    # Catalog swagger.json

    
    url = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    meta = fields.Nested(Meta, required=False)
    
    alt = fields.Str(required=False)
    


class QueryParams(BaseSchema):
    # Catalog swagger.json

    
    category = fields.List(fields.Str(required=False), required=False)
    
    brand = fields.List(fields.Str(required=False), required=False)
    
    department = fields.List(fields.Str(required=False), required=False)
    


class Params(BaseSchema):
    # Catalog swagger.json

    
    slug = fields.List(fields.Str(required=False), required=False)
    


class ProductListingActionPage(BaseSchema):
    # Catalog swagger.json

    
    type = fields.Str(required=False)
    
    query = fields.Nested(QueryParams, required=False)
    
    params = fields.Nested(Params, required=False)
    


class ProductListingAction(BaseSchema):
    # Catalog swagger.json

    
    type = fields.Str(required=False)
    
    page = fields.Nested(ProductListingActionPage, required=False)
    


class ProductBrand(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    logo = fields.Nested(Media, required=False)
    
    description = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    _custom_json = fields.Dict(required=False)
    


class ProductDepartment(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    logo = fields.Nested(Media, required=False)
    
    slug = fields.Str(required=False)
    
    name = fields.Str(required=False)
    


class ProductCategoryMap(BaseSchema):
    # Catalog swagger.json

    
    l1 = fields.Nested(ProductBrand, required=False)
    
    l2 = fields.Nested(ProductBrand, required=False)
    
    l3 = fields.Nested(ProductBrand, required=False)
    


class NetQuantity(BaseSchema):
    # Catalog swagger.json

    
    unit = fields.Str(required=False)
    
    value = fields.Float(required=False)
    


class CustomMetaFields(BaseSchema):
    # Catalog swagger.json

    
    value = fields.Str(required=False)
    
    key = fields.Str(required=False)
    


class ApplicationItemSeoAction(BaseSchema):
    # Catalog swagger.json

    
    page = fields.Dict(required=False)
    
    type = fields.Str(required=False)
    


class ApplicationItemSeoBreadcrumbs(BaseSchema):
    # Catalog swagger.json

    
    url = fields.Str(required=False)
    
    action = fields.Nested(ApplicationItemSeoAction, required=False)
    


class ApplicationItemSeoMetaTagItem(BaseSchema):
    # Catalog swagger.json

    
    key = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class ApplicationItemSEO(BaseSchema):
    # Catalog swagger.json

    
    description = fields.Str(required=False)
    
    sitemap = fields.Nested(ApplicationItemSeoSitemap, required=False)
    
    breadcrumbs = fields.List(fields.Nested(ApplicationItemSeoBreadcrumbs, required=False), required=False)
    
    meta_tags = fields.List(fields.Nested(ApplicationItemSeoMetaTags, required=False), required=False)
    
    canonical_url = fields.Str(required=False)
    


class ApplicationItemSeoSitemap(BaseSchema):
    # Catalog swagger.json

    
    priority = fields.Float(required=False)
    
    frequency = fields.Str(required=False)
    


class ApplicationItemSeoMetaTags(BaseSchema):
    # Catalog swagger.json

    
    title = fields.Str(required=False)
    
    items = fields.List(fields.Nested(ApplicationItemSeoMetaTagItem, required=False), required=False)
    


class ProductDetailAttribute(BaseSchema):
    # Catalog swagger.json

    
    value = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    key = fields.Str(required=False)
    


class ProductDetailGroupedAttribute(BaseSchema):
    # Catalog swagger.json

    
    title = fields.Str(required=False)
    
    details = fields.List(fields.Nested(ProductDetailAttribute, required=False), required=False)
    


class ApplicationItemMOQ(BaseSchema):
    # Catalog swagger.json

    
    minimum = fields.Int(required=False)
    
    maximum = fields.Int(required=False)
    
    increment_unit = fields.Int(required=False)
    


class Price(BaseSchema):
    # Catalog swagger.json

    
    min = fields.Float(required=False)
    
    currency_symbol = fields.Str(required=False)
    
    currency_code = fields.Str(required=False)
    
    max = fields.Float(required=False)
    


class ProductListingPrice(BaseSchema):
    # Catalog swagger.json

    
    effective = fields.Nested(Price, required=False)
    
    marked = fields.Nested(Price, required=False)
    
    selling = fields.Nested(Price, required=False)
    


class ProductSizesPrice(BaseSchema):
    # Catalog swagger.json

    
    effective = fields.Nested(Price, required=False)
    
    marked = fields.Nested(Price, required=False)
    
    selling = fields.Nested(Price, required=False)
    


class ProductCompareDetail(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    custom_order = fields.Nested(ProductDetailCustomOrder, required=False)
    
    net_quantity = fields.Nested(NetQuantity, required=False)
    
    rating_count = fields.Int(required=False)
    
    template_tag = fields.Str(required=False)
    
    sellable = fields.Boolean(required=False)
    
    _custom_meta = fields.List(fields.Nested(CustomMetaFields, required=False), required=False)
    
    similars = fields.List(fields.Str(required=False), required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    seo = fields.Nested(ApplicationItemSEO, required=False)
    
    image_nature = fields.Str(required=False)
    
    has_variant = fields.Boolean(required=False)
    
    item_type = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    grouped_attributes = fields.List(fields.Nested(ProductDetailGroupedAttribute, required=False), required=False)
    
    medias = fields.List(fields.Nested(Media, required=False), required=False)
    
    type = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    item_code = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    moq = fields.Nested(ApplicationItemMOQ, required=False)
    
    short_description = fields.Str(required=False)
    
    categories = fields.List(fields.Nested(ProductBrand, required=False), required=False)
    
    attributes = fields.Dict(required=False)
    
    discount = fields.Str(required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    slug = fields.Str(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    rating = fields.Float(required=False)
    
    is_dependent = fields.Boolean(required=False)
    
    product_group_tag = fields.List(fields.Str(required=False), required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    price = fields.Nested(ProductListingPrice, required=False)
    
    brand = fields.Nested(ProductBrand, required=False)
    
    department = fields.Nested(ProductDepartment, required=False)
    
    teaser_tag = fields.Str(required=False)
    
    country_of_origin = fields.Str(required=False)
    


class ProductDetail(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    sizes = fields.List(fields.Str(required=False), required=False)
    
    identifiers = fields.List(fields.Str(required=False), required=False)
    
    is_tryout = fields.Boolean(required=False)
    
    channel = fields.Str(required=False)
    
    discount_meta = fields.Nested(DiscountMeta, required=False)
    
    variants = fields.List(fields.Nested(ProductVariantResponseSchema, required=False), required=False)
    
    custom_order = fields.Nested(ProductDetailCustomOrder, required=False)
    
    category_map = fields.Nested(ProductCategoryMap, required=False)
    
    net_quantity = fields.Nested(NetQuantity, required=False)
    
    rating_count = fields.Int(required=False)
    
    _custom_meta = fields.List(fields.Nested(CustomMetaFields, required=False), required=False)
    
    similars = fields.List(fields.Str(required=False), required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    seo = fields.Nested(ApplicationItemSEO, required=False)
    
    image_nature = fields.Str(required=False)
    
    has_variant = fields.Boolean(required=False)
    
    item_type = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    grouped_attributes = fields.List(fields.Nested(ProductDetailGroupedAttribute, required=False), required=False)
    
    medias = fields.List(fields.Nested(Media, required=False), required=False)
    
    color = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    product_online_date = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    item_code = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    moq = fields.Nested(ApplicationItemMOQ, required=False)
    
    short_description = fields.Str(required=False)
    
    categories = fields.List(fields.Nested(ProductBrand, required=False), required=False)
    
    attributes = fields.Dict(required=False)
    
    discount = fields.Str(required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    slug = fields.Str(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    rating = fields.Float(required=False)
    
    is_dependent = fields.Boolean(required=False)
    
    product_group_tag = fields.List(fields.Str(required=False), required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    price = fields.Nested(ProductListingPrice, required=False)
    
    brand = fields.Nested(ProductBrand, required=False)
    
    department = fields.Nested(ProductDepartment, required=False)
    
    teaser_tag = fields.Str(required=False)
    
    promo_meta = fields.Dict(required=False)
    
    no_of_boxes = fields.Int(required=False)
    
    template_tag = fields.Str(required=False)
    
    sellable = fields.Boolean(required=False)
    
    country_of_origin = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    


class NotServiceableError(BaseSchema):
    # Catalog swagger.json

    
    message = fields.Str(required=False)
    
    is_serviceable = fields.Boolean(required=False)
    


class ErrorResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    error = fields.Str(required=False)
    
    errors = fields.Dict(required=False)
    
    code = fields.Int(required=False)
    
    message = fields.Str(required=False)
    


class Dimension(BaseSchema):
    # Catalog swagger.json

    
    unit = fields.Str(required=False)
    
    height = fields.Float(required=False)
    
    length = fields.Float(required=False)
    
    width = fields.Float(required=False)
    
    is_default = fields.Boolean(required=False)
    


class Weight(BaseSchema):
    # Catalog swagger.json

    
    unit = fields.Str(required=False)
    
    shipping = fields.Float(required=False)
    
    is_default = fields.Boolean(required=False)
    


class DiscountMeta(BaseSchema):
    # Catalog swagger.json

    
    timer = fields.Boolean(required=False)
    
    start_timer_in_minutes = fields.Float(required=False)
    
    start = fields.Str(required=False)
    
    end = fields.Str(required=False)
    


class ProductSize(BaseSchema):
    # Catalog swagger.json

    
    quantity = fields.Int(required=False)
    
    dimension = fields.Nested(Dimension, required=False)
    
    weight = fields.Nested(Weight, required=False)
    
    is_available = fields.Boolean(required=False)
    
    seller_identifiers = fields.List(fields.Str(required=False), required=False)
    
    value = fields.Str(required=False)
    
    display = fields.Str(required=False)
    
    set = fields.Nested(ProductSetV3, required=False)
    


class SizeChartValues(BaseSchema):
    # Catalog swagger.json

    
    col_3 = fields.Str(required=False)
    
    col_6 = fields.Str(required=False)
    
    col_2 = fields.Str(required=False)
    
    col_4 = fields.Str(required=False)
    
    col_1 = fields.Str(required=False)
    
    col_5 = fields.Str(required=False)
    


class ColumnHeader(BaseSchema):
    # Catalog swagger.json

    
    convertable = fields.Boolean(required=False)
    
    value = fields.Str(required=False)
    


class ColumnHeaders(BaseSchema):
    # Catalog swagger.json

    
    col_3 = fields.Nested(ColumnHeader, required=False)
    
    col_6 = fields.Nested(ColumnHeader, required=False)
    
    col_2 = fields.Nested(ColumnHeader, required=False)
    
    col_4 = fields.Nested(ColumnHeader, required=False)
    
    col_1 = fields.Nested(ColumnHeader, required=False)
    
    col_5 = fields.Nested(ColumnHeader, required=False)
    


class SizeChart(BaseSchema):
    # Catalog swagger.json

    
    unit = fields.Str(required=False)
    
    image = fields.Str(required=False)
    
    size_tip = fields.Str(required=False)
    
    sizes = fields.List(fields.Nested(SizeChartValues, required=False), required=False)
    
    description = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    headers = fields.Nested(ColumnHeaders, required=False)
    


class ProductSizeStores(BaseSchema):
    # Catalog swagger.json

    
    count = fields.Int(required=False)
    


class ProductSizes(BaseSchema):
    # Catalog swagger.json

    
    sizes = fields.List(fields.Nested(ProductSize, required=False), required=False)
    
    price = fields.Nested(ProductSizesPrice, required=False)
    
    price_per_piece = fields.Nested(ProductSizesPrice, required=False)
    
    size_chart = fields.Nested(SizeChart, required=False)
    
    sellable = fields.Boolean(required=False)
    
    multi_size = fields.Boolean(required=False)
    
    discount = fields.Str(required=False)
    
    stores = fields.Nested(ProductSizeStores, required=False)
    
    discount_meta = fields.Nested(DiscountMeta, required=False)
    
    moq = fields.Nested(MOQ, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    custom_order = fields.Dict(required=False)
    
    no_of_boxes = fields.Int(required=False)
    
    teaser_tag = fields.Dict(required=False)
    


class MOQ(BaseSchema):
    # Catalog swagger.json

    
    maximum = fields.Int(required=False)
    
    minimum = fields.Int(required=False)
    
    increment_unit = fields.Int(required=False)
    


class AttributeDetail(BaseSchema):
    # Catalog swagger.json

    
    logo = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    display = fields.Str(required=False)
    
    key = fields.Str(required=False)
    


class AttributeMetadata(BaseSchema):
    # Catalog swagger.json

    
    title = fields.Str(required=False)
    
    details = fields.List(fields.Nested(AttributeDetail, required=False), required=False)
    


class ProductsComparisonResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(ProductCompareDetail, required=False), required=False)
    
    attributes_metadata = fields.List(fields.Nested(AttributeMetadata, required=False), required=False)
    


class ProductCompareResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    title = fields.Str(required=False)
    
    items = fields.List(fields.Nested(ProductDetail, required=False), required=False)
    
    attributes_metadata = fields.List(fields.Nested(AttributeMetadata, required=False), required=False)
    
    subtitle = fields.Str(required=False)
    


class ProductFrequentlyComparedSimilarResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    similars = fields.Nested(ProductCompareResponseSchema, required=False)
    


class ProductVariantItemResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    color_name = fields.Str(required=False)
    
    color = fields.Str(required=False)
    
    medias = fields.List(fields.Nested(Media, required=False), required=False)
    
    is_available = fields.Boolean(required=False)
    
    _custom_meta = fields.List(fields.Nested(CustomMetaFields, required=False), required=False)
    
    name = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    


class ProductVariantResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    display_type = fields.Str(required=False)
    
    header = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    group_id = fields.Str(required=False)
    
    items = fields.List(fields.Nested(ProductVariantItemResponseSchema, required=False), required=False)
    
    key = fields.Str(required=False)
    


class ProductVariantsResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    variants = fields.List(fields.Nested(ProductVariantResponseSchema, required=False), required=False)
    


class StoreDetail(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    code = fields.Str(required=False)
    


class ProductStockPrice(BaseSchema):
    # Catalog swagger.json

    
    effective = fields.Float(required=False)
    
    currency = fields.Str(required=False)
    
    marked = fields.Float(required=False)
    


class CompanyDetail(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    id = fields.Int(required=False)
    


class Seller(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    count = fields.Int(required=False)
    


class ArticleIdentifier(BaseSchema):
    # Catalog swagger.json

    
    ean = fields.Str(required=False)
    
    alu = fields.Str(required=False)
    
    upc = fields.Str(required=False)
    
    sku_code = fields.Str(required=False)
    


class ProductStockStatusItem(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    brand = fields.Nested(BrandItem, required=False)
    
    seller_identifier = fields.Str(required=False)
    
    price_effective = fields.Float(required=False)
    
    price_selling = fields.Float(required=False)
    
    price_marked = fields.Float(required=False)
    
    discount_meta = fields.Nested(DiscountMeta, required=False)
    
    discount_applied = fields.Dict(required=False)
    
    store = fields.Nested(StoreDetail, required=False)
    
    size = fields.Str(required=False)
    
    identifier = fields.Nested(ArticleIdentifier, required=False)
    
    price = fields.Nested(ProductStockPrice, required=False)
    
    item_id = fields.Int(required=False)
    
    company = fields.Nested(CompanyDetail, required=False)
    
    company_id = fields.Int(required=False)
    
    brand_id = fields.Int(required=False)
    
    store_id = fields.Int(required=False)
    
    seller = fields.Nested(Seller, required=False)
    
    currency = fields.Str(required=False)
    


class ProductStockStatusResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(ProductStockStatusItem, required=False), required=False)
    


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
    


class ProductStockPolling(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(ProductStockStatusItem, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class ProductVariantListingResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    header = fields.Str(required=False)
    
    items = fields.List(fields.Nested(ProductVariantItemResponseSchema, required=False), required=False)
    
    total = fields.Int(required=False)
    
    key = fields.Str(required=False)
    
    display_type = fields.Str(required=False)
    


class ProductListingDetail(BaseSchema):
    # Catalog swagger.json

    
    discount_meta = fields.Nested(DiscountMeta, required=False)
    
    uid = fields.Int(required=False)
    
    custom_order = fields.Nested(ProductDetailCustomOrder, required=False)
    
    sizes = fields.List(fields.Str(required=False), required=False)
    
    category_map = fields.Nested(ProductCategoryMap, required=False)
    
    net_quantity = fields.Nested(NetQuantity, required=False)
    
    rating_count = fields.Int(required=False)
    
    _custom_meta = fields.List(fields.Nested(CustomMetaFields, required=False), required=False)
    
    similars = fields.List(fields.Str(required=False), required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    seo = fields.Nested(ApplicationItemSEO, required=False)
    
    image_nature = fields.Str(required=False)
    
    has_variant = fields.Boolean(required=False)
    
    item_type = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    grouped_attributes = fields.List(fields.Nested(ProductDetailGroupedAttribute, required=False), required=False)
    
    medias = fields.List(fields.Nested(Media, required=False), required=False)
    
    color = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    product_online_date = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    item_code = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    moq = fields.Nested(ApplicationItemMOQ, required=False)
    
    short_description = fields.Str(required=False)
    
    categories = fields.List(fields.Nested(ProductBrand, required=False), required=False)
    
    sellable = fields.Boolean(required=False)
    
    attributes = fields.Dict(required=False)
    
    variants = fields.List(fields.Nested(ProductVariantListingResponseSchema, required=False), required=False)
    
    discount = fields.Str(required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    identifiers = fields.List(fields.Str(required=False), required=False)
    
    slug = fields.Str(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    rating = fields.Float(required=False)
    
    is_dependent = fields.Boolean(required=False)
    
    product_group_tag = fields.List(fields.Str(required=False), required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    price = fields.Nested(ProductListingPrice, required=False)
    
    brand = fields.Nested(ProductBrand, required=False)
    
    teaser_tag = fields.Str(required=False)
    
    country_of_origin = fields.Str(required=False)
    
    is_tryout = fields.Boolean(required=False)
    
    channel = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    


class ProductFiltersValue(BaseSchema):
    # Catalog swagger.json

    
    min = fields.Int(required=False)
    
    display_format = fields.Str(required=False)
    
    selected_max = fields.Int(required=False)
    
    value = fields.Str(required=False)
    
    query_format = fields.Str(required=False)
    
    currency_symbol = fields.Str(required=False)
    
    selected_min = fields.Int(required=False)
    
    currency_code = fields.Str(required=False)
    
    is_selected = fields.Boolean(required=False)
    
    display = fields.Str(required=False)
    
    count = fields.Int(required=False)
    
    max = fields.Int(required=False)
    
    logo = fields.Nested(Media, required=False)
    


class ProductFiltersKey(BaseSchema):
    # Catalog swagger.json

    
    logo = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    kind = fields.Str(required=False)
    
    display = fields.Str(required=False)
    


class ProductFilters(BaseSchema):
    # Catalog swagger.json

    
    values = fields.List(fields.Nested(ProductFiltersValue, required=False), required=False)
    
    key = fields.Nested(ProductFiltersKey, required=False)
    


class ProductSortOn(BaseSchema):
    # Catalog swagger.json

    
    logo = fields.Str(required=False)
    
    is_selected = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    display = fields.Str(required=False)
    


class ProductListingResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(ProductListingDetail, required=False), required=False)
    
    filters = fields.List(fields.Nested(ProductFilters, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
    sort_on = fields.List(fields.Nested(ProductSortOn, required=False), required=False)
    


class ImageUrls(BaseSchema):
    # Catalog swagger.json

    
    portrait = fields.Nested(Media, required=False)
    
    landscape = fields.Nested(Media, required=False)
    


class BrandItem(BaseSchema):
    # Catalog swagger.json

    
    id = fields.Int(required=False)
    
    uid = fields.Int(required=False)
    
    logo = fields.Nested(Media, required=False)
    
    seo = fields.Nested(ApplicationItemSEO, required=False)
    
    description = fields.Str(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    departments = fields.List(fields.Str(required=False), required=False)
    
    discount = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    


class BrandListingResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(BrandItem, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class BrandDetailResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    logo = fields.Nested(Media, required=False)
    
    uid = fields.Int(required=False)
    
    description = fields.Str(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    slug = fields.Str(required=False)
    
    _app = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    
    seo = fields.Nested(ApplicationItemSEO, required=False)
    


class CategoryBanner(BaseSchema):
    # Catalog swagger.json

    
    portrait = fields.Nested(Media, required=False)
    
    landscape = fields.Nested(Media, required=False)
    


class ThirdLevelChild(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    childs = fields.List(fields.Dict(required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    priority = fields.Int(required=False)
    


class SecondLevelChild(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    childs = fields.List(fields.Nested(ThirdLevelChild, required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    priority = fields.Int(required=False)
    


class Child(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    childs = fields.List(fields.Nested(SecondLevelChild, required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    priority = fields.Int(required=False)
    


class CategoryItems(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    banners = fields.Nested(CategoryBanner, required=False)
    
    childs = fields.List(fields.Nested(Child, required=False), required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    priority = fields.Int(required=False)
    
    _custom_json = fields.Dict(required=False)
    


class DepartmentCategoryTree(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(CategoryItems, required=False), required=False)
    
    department = fields.Str(required=False)
    


class DepartmentIdentifier(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    slug = fields.Str(required=False)
    


class CategoryListingResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    data = fields.List(fields.Nested(DepartmentCategoryTree, required=False), required=False)
    
    departments = fields.List(fields.Nested(DepartmentIdentifier, required=False), required=False)
    


class CategoryMetaResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    logo = fields.Nested(Media, required=False)
    
    uid = fields.Int(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    
    _app = fields.Dict(required=False)
    


class HomeListingResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(ProductListingDetail, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
    message = fields.Str(required=False)
    
    sort_on = fields.Str(required=False)
    


class Department(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    logo = fields.Nested(Media, required=False)
    
    priority_order = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    


class DepartmentResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(Department, required=False), required=False)
    


class AutocompleteItem(BaseSchema):
    # Catalog swagger.json

    
    logo = fields.Nested(Media, required=False)
    
    display = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    


class AutoCompleteResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(AutocompleteItem, required=False), required=False)
    


class CollectionQuery(BaseSchema):
    # Catalog swagger.json

    
    op = fields.Str(required=False)
    
    value = fields.List(fields.Str(required=False), required=False)
    
    attribute = fields.Str(required=False)
    


class NextSchedule(BaseSchema):
    # Catalog swagger.json

    
    start = fields.Str(required=False, allow_none=True)
    
    end = fields.Str(required=False, allow_none=True)
    


class Schedule(BaseSchema):
    # Catalog swagger.json

    
    cron = fields.Str(required=False)
    
    next_schedule = fields.List(fields.Nested(NextSchedule, required=False), required=False)
    
    duration = fields.Int(required=False)
    
    start = fields.Str(required=False, allow_none=True)
    
    end = fields.Str(required=False, allow_none=True)
    
    metadata = fields.Dict(required=False)
    


class GetCollectionDetailNest(BaseSchema):
    # Catalog swagger.json

    
    is_active = fields.Boolean(required=False)
    
    uid = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    sort_on = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    cron = fields.Dict(required=False)
    
    _schedule = fields.Nested(Schedule, required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
    description = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    badge = fields.Dict(required=False)
    
    slug = fields.Str(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    logo = fields.Nested(Media, required=False)
    
    priority = fields.Int(required=False)
    
    tag = fields.List(fields.Str(required=False), required=False)
    
    app_id = fields.Str(required=False)
    
    published = fields.Boolean(required=False)
    
    _locale_language = fields.Dict(required=False)
    
    seo = fields.Dict(required=False)
    
    is_visible = fields.Boolean(required=False)
    
    modified_on = fields.Str(required=False)
    


class CollectionListingFilterTag(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    is_selected = fields.Boolean(required=False)
    
    display = fields.Str(required=False)
    


class CollectionListingFilterType(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    is_selected = fields.Boolean(required=False)
    
    display = fields.Str(required=False)
    


class CollectionListingFilter(BaseSchema):
    # Catalog swagger.json

    
    tags = fields.List(fields.Nested(CollectionListingFilterTag, required=False), required=False)
    
    type = fields.List(fields.Nested(CollectionListingFilterType, required=False), required=False)
    


class GetCollectionListingResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(GetCollectionDetailNest, required=False), required=False)
    
    filters = fields.Nested(CollectionListingFilter, required=False)
    
    page = fields.Nested(Page, required=False)
    


class CollectionDetailResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Str(required=False)
    
    published = fields.Boolean(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    _locale_language = fields.Dict(required=False)
    
    seo = fields.Dict(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    is_active = fields.Boolean(required=False)
    
    sort_on = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    cron = fields.Dict(required=False)
    
    _schedule = fields.Nested(Schedule, required=False)
    
    modified_on = fields.Str(required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
    description = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    badge = fields.Dict(required=False)
    
    slug = fields.Str(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    logo = fields.Nested(Media, required=False)
    
    priority = fields.Int(required=False)
    
    tag = fields.List(fields.Str(required=False), required=False)
    
    app_id = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    is_visible = fields.Boolean(required=False)
    


class GetFollowListingResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(ProductListingDetail, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class FollowPostResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    message = fields.Str(required=False)
    
    id = fields.Str(required=False)
    


class FollowerCountResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    count = fields.Int(required=False)
    


class FollowIdsData(BaseSchema):
    # Catalog swagger.json

    
    products = fields.List(fields.Int(required=False), required=False)
    
    collections = fields.List(fields.Int(required=False), required=False)
    
    brands = fields.List(fields.Int(required=False), required=False)
    


class FollowIdsResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    data = fields.Nested(FollowIdsData, required=False)
    


class LatLong(BaseSchema):
    # Catalog swagger.json

    
    coordinates = fields.List(fields.Float(required=False), required=False)
    
    type = fields.Str(required=False)
    


class Store(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    store_email = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    address = fields.Str(required=False)
    
    store_code = fields.Str(required=False)
    
    lat_long = fields.Nested(LatLong, required=False)
    
    name = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    manager_contact = fields.Str(required=False)
    
    contacts = fields.List(fields.Nested(ContactDetails, required=False), required=False)
    


class ContactDetails(BaseSchema):
    # Catalog swagger.json

    
    number = fields.Str(required=False)
    
    country_code = fields.Int(required=False)
    


class StoreListingResponseSchema(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(Store, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class StoreDepartments(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    logo = fields.Dict(required=False)
    
    priority_order = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    


class AppStoreDepartment(BaseSchema):
    # Catalog swagger.json

    
    priority_order = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    logo = fields.Nested(Media, required=False)
    
    uid = fields.Int(required=False)
    
    slug = fields.Str(required=False)
    


class CompanyStore(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    company_type = fields.Str(required=False)
    
    business_type = fields.Str(required=False)
    


class SellerPhoneNumber(BaseSchema):
    # Catalog swagger.json

    
    country_code = fields.Int(required=False)
    
    number = fields.Str(required=False)
    


class StoreManagerSchema(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    mobile_no = fields.Nested(SellerPhoneNumber, required=False)
    


class StoreAddressSchema(BaseSchema):
    # Catalog swagger.json

    
    latitude = fields.Float(required=False)
    
    state = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    landmark = fields.Str(required=False)
    
    address1 = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    longitude = fields.Float(required=False)
    
    address2 = fields.Str(required=False)
    
    lat_long = fields.Nested(LatLong, required=False)
    
    country_code = fields.Str(required=False)
    
    address_meta = fields.Dict(required=False)
    


class AppStore(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    departments = fields.List(fields.Nested(AppStoreDepartment, required=False), required=False)
    
    company = fields.Nested(CompanyStore, required=False)
    
    manager = fields.Nested(StoreManagerSchema, required=False)
    
    store_code = fields.Str(required=False)
    
    address = fields.Nested(StoreAddressSchema, required=False)
    
    name = fields.Str(required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    additional_contacts = fields.List(fields.Nested(ContactDetails, required=False), required=False)
    
    company_id = fields.Int(required=False)
    
    display_name = fields.Str(required=False)
    
    store_type = fields.Str(required=False)
    
    auto_invoice = fields.Boolean(required=False)
    
    credit_note = fields.Boolean(required=False)
    
    stage = fields.Str(required=False)
    
    gst_credentials = fields.Nested(GSTCredentials, required=False)
    
    product_return_config = fields.Nested(ProductReturnConfig, required=False)
    
    avg_order_processing_time = fields.Nested(OrderProcessingTime, required=False)
    
    bulk_shipment = fields.Boolean(required=False)
    
    default_order_acceptance_timing = fields.Boolean(required=False)
    
    order_acceptance_timing = fields.List(fields.Nested(OrderTiming, required=False), required=False)
    
    auto_assign_courier_partner = fields.Boolean(required=False)
    


class ProductReturnConfig(BaseSchema):
    # Catalog swagger.json

    
    on_same_store = fields.Boolean(required=False)
    


class OrderProcessingTime(BaseSchema):
    # Catalog swagger.json

    
    duration = fields.Int(required=False)
    
    duration_type = fields.Str(required=False)
    


class OrderTiming(BaseSchema):
    # Catalog swagger.json

    
    weekday = fields.Str(required=False)
    
    opening = fields.Nested(Time, required=False)
    
    closing = fields.Nested(Time, required=False)
    
    open = fields.Boolean(required=False)
    


class GSTCredentials(BaseSchema):
    # Catalog swagger.json

    
    e_invoice = fields.Nested(EnabledStatus, required=False)
    
    e_waybill = fields.Nested(EnabledStatus, required=False)
    


class EnabledStatus(BaseSchema):
    # Catalog swagger.json

    
    enabled = fields.Boolean(required=False)
    


class ApplicationStoreFilterListing(BaseSchema):
    # Catalog swagger.json

    
    slug = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    priority_order = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    modified_by = fields.Nested(ModifiedBy, required=False)
    
    modified_on = fields.Str(required=False)
    


class ModifiedBy(BaseSchema):
    # Catalog swagger.json

    
    user_id = fields.Str(required=False)
    
    username = fields.Str(required=False)
    


class ApplicationStoreListing(BaseSchema):
    # Catalog swagger.json

    
    filters = fields.List(fields.Nested(ApplicationStoreFilterListing, required=False), required=False)
    
    items = fields.List(fields.Nested(AppStore, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class Time(BaseSchema):
    # Catalog swagger.json

    
    hour = fields.Int(required=False)
    
    minute = fields.Int(required=False)
    


class StoreTiming(BaseSchema):
    # Catalog swagger.json

    
    open = fields.Boolean(required=False)
    
    closing = fields.Nested(Time, required=False)
    
    weekday = fields.Str(required=False)
    
    opening = fields.Nested(Time, required=False)
    


class StoreDetails(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    departments = fields.List(fields.Nested(StoreDepartments, required=False), required=False)
    
    company = fields.Nested(CompanyStore, required=False)
    
    manager = fields.Nested(StoreManagerSchema, required=False)
    
    store_code = fields.Str(required=False)
    
    timing = fields.List(fields.Nested(StoreTiming, required=False), required=False)
    
    address = fields.Nested(StoreAddressSchema, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    additional_contacts = fields.List(fields.Nested(ContactDetails, required=False), required=False)
    
    company_id = fields.Int(required=False)
    
    display_name = fields.Str(required=False)
    
    store_type = fields.Str(required=False)
    
    auto_invoice = fields.Boolean(required=False)
    
    credit_note = fields.Boolean(required=False)
    
    stage = fields.Str(required=False)
    
    gst_credentials = fields.Nested(GSTCredentials, required=False)
    
    product_return_config = fields.Nested(ProductReturnConfig, required=False)
    
    avg_order_processing_time = fields.Nested(OrderProcessingTime, required=False)
    
    bulk_shipment = fields.Boolean(required=False)
    
    default_order_acceptance_timing = fields.Boolean(required=False)
    
    order_acceptance_timing = fields.List(fields.Nested(OrderTiming, required=False), required=False)
    
    auto_assign_courier_partner = fields.Boolean(required=False)
    


class UserDetail(BaseSchema):
    # Catalog swagger.json

    
    super_user = fields.Boolean(required=False)
    
    contact = fields.Str(required=False)
    
    username = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    


class Size(BaseSchema):
    # Catalog swagger.json

    
    quantity = fields.Int(required=False)
    
    value = fields.Str(required=False)
    
    display = fields.Str(required=False)
    
    is_available = fields.Boolean(required=False)
    


class ProductGroupPrice(BaseSchema):
    # Catalog swagger.json

    
    effective = fields.Float(required=False)
    
    marked = fields.Float(required=False)
    
    selling = fields.Float(required=False)
    
    currency = fields.Str(required=False)
    


class ProductDetails(BaseSchema):
    # Catalog swagger.json

    
    template_tag = fields.Str(required=False)
    
    rating_count = fields.Int(required=False)
    
    image_nature = fields.Str(required=False)
    
    has_variant = fields.Boolean(required=False)
    
    description = fields.Str(required=False)
    
    out_of_stock = fields.Boolean(required=False)
    
    hsn_code = fields.Int(required=False)
    
    grouped_attributes = fields.Dict(required=False)
    
    item_code = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    country_of_origin = fields.Str(required=False)
    
    short_description = fields.Str(required=False)
    
    media = fields.List(fields.Dict(required=False), required=False)
    
    attributes = fields.Dict(required=False)
    
    is_set = fields.Boolean(required=False)
    
    images = fields.List(fields.Str(required=False), required=False)
    
    slug = fields.Str(required=False)
    
    rating = fields.Float(required=False)
    
    identifier = fields.Nested(Identifier, required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    
    brand_uid = fields.Int(required=False)
    


class ProductInGroup(BaseSchema):
    # Catalog swagger.json

    
    max_quantity = fields.Int(required=False)
    
    sizes = fields.List(fields.Nested(Size, required=False), required=False)
    
    price = fields.Nested(ProductGroupPrice, required=False)
    
    product_details = fields.Dict(required=False)
    
    min_quantity = fields.Int(required=False)
    
    allow_remove = fields.Boolean(required=False)
    
    product_uid = fields.Int(required=False)
    


class ProductGroupingModel(BaseSchema):
    # Catalog swagger.json

    
    logo = fields.Str(required=False, allow_none=True)
    
    is_active = fields.Boolean(required=False)
    
    meta = fields.Dict(required=False)
    
    verified_by = fields.Dict(required=False)
    
    created_on = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    page_visibility = fields.List(fields.Str(required=False), required=False)
    
    modified_on = fields.Str(required=False)
    
    created_by = fields.Dict(required=False)
    
    modified_by = fields.Dict(required=False)
    
    products = fields.List(fields.Nested(ProductInGroup, required=False), required=False)
    
    allow_remove = fields.Boolean(required=False)
    
    auto_add_to_cart = fields.Boolean(required=False)
    
    auto_select = fields.Boolean(required=False)
    
    allow_individual_cancel = fields.Boolean(required=False)
    
    allow_individual_return = fields.Boolean(required=False)
    
    prefer_single_shipment = fields.Boolean(required=False)
    
    same_store_assignment = fields.Boolean(required=False)
    
    _id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    choice = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    verified_on = fields.Str(required=False)
    


class ProductBundle(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(ProductGroupingModel, required=False), required=False)
    


class StoreV3(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    count = fields.Int(required=False)
    


class ArticleAssignmentV3(BaseSchema):
    # Catalog swagger.json

    
    strategy = fields.Str(required=False)
    
    level = fields.Str(required=False)
    


class StrategyWiseListingSchemaV3(BaseSchema):
    # Catalog swagger.json

    
    distance = fields.Int(required=False)
    
    pincode = fields.Str(required=False)
    
    tat = fields.Int(required=False)
    
    quantity = fields.Int(required=False)
    


class DetailsSchemaV3(BaseSchema):
    # Catalog swagger.json

    
    value = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    key = fields.Str(required=False)
    


class SellerGroupAttributes(BaseSchema):
    # Catalog swagger.json

    
    title = fields.Str(required=False)
    
    details = fields.List(fields.Nested(DetailsSchemaV3, required=False), required=False)
    


class ReturnConfigSchemaV3(BaseSchema):
    # Catalog swagger.json

    
    unit = fields.Str(required=False)
    
    returnable = fields.Boolean(required=False)
    
    time = fields.Int(required=False)
    


class ProductSetDistributionSizeV3(BaseSchema):
    # Catalog swagger.json

    
    pieces = fields.Int(required=False)
    
    size = fields.Str(required=False)
    


class ProductSetDistributionV3(BaseSchema):
    # Catalog swagger.json

    
    sizes = fields.List(fields.Nested(ProductSetDistributionSizeV3, required=False), required=False)
    


class ProductSetV3(BaseSchema):
    # Catalog swagger.json

    
    quantity = fields.Int(required=False)
    
    size_distribution = fields.Nested(ProductSetDistributionV3, required=False)
    


class ProductStockPriceV3(BaseSchema):
    # Catalog swagger.json

    
    effective = fields.Float(required=False)
    
    currency_code = fields.Str(required=False)
    
    currency_symbol = fields.Str(required=False)
    
    marked = fields.Float(required=False)
    
    selling = fields.Float(required=False)
    


class ProductStockUnitPriceV3(BaseSchema):
    # Catalog swagger.json

    
    unit = fields.Str(required=False)
    
    currency_symbol = fields.Str(required=False)
    
    currency_code = fields.Str(required=False)
    
    price = fields.Float(required=False)
    


class MarketPlaceSttributesSchemaV3(BaseSchema):
    # Catalog swagger.json

    
    title = fields.Str(required=False)
    
    details = fields.List(fields.Nested(DetailsSchemaV3, required=False), required=False)
    


class SellerV3(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    count = fields.Int(required=False)
    


class PromiseSchema(BaseSchema):
    # Catalog swagger.json

    
    min = fields.Str(required=False)
    
    max = fields.Str(required=False)
    


class ProductSizePriceResponseV4(BaseSchema):
    # Catalog swagger.json

    
    store = fields.Nested(StoreV3, required=False)
    
    article_assignment = fields.Nested(ArticleAssignmentV3, required=False)
    
    is_cod = fields.Boolean(required=False)
    
    strategy_wise_listing = fields.List(fields.Nested(StrategyWiseListingSchemaV3, required=False), required=False)
    
    quantity = fields.Int(required=False)
    
    item_type = fields.Str(required=False)
    
    grouped_attributes = fields.List(fields.Nested(SellerGroupAttributes, required=False), required=False)
    
    return_config = fields.Nested(ReturnConfigSchemaV3, required=False)
    
    article_id = fields.Str(required=False)
    
    is_gift = fields.Boolean(required=False)
    
    set = fields.Nested(ProductSetV3, required=False)
    
    price_per_piece = fields.Nested(ProductStockPriceV3, required=False)
    
    discount_meta = fields.Nested(DiscountMeta, required=False)
    
    discount = fields.Str(required=False)
    
    long_lat = fields.List(fields.Float(required=False), required=False)
    
    price = fields.Nested(ProductStockPriceV3, required=False)
    
    price_per_unit = fields.Nested(ProductStockUnitPriceV3, required=False)
    
    pincode = fields.Str(required=False)
    
    trader = fields.List(fields.Str(required=False), required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    is_serviceable = fields.Boolean(required=False)
    
    marketplace_attributes = fields.List(fields.Nested(MarketPlaceSttributesSchemaV3, required=False), required=False)
    
    seller = fields.Nested(SellerV3, required=False)
    
    delivery_promise = fields.Nested(PromiseSchema, required=False)
    
    product_name = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    error = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    size = fields.Str(required=False)
    


class ProductSizeSellerFilterSchemaV4(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    is_selected = fields.Boolean(required=False)
    
    value = fields.Str(required=False)
    


class ProductSizeSellersResponseV4(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(ProductSizePriceResponseV4, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
    sort_on = fields.List(fields.Nested(ProductSizeSellerFilterSchemaV4, required=False), required=False)
    


class ProductSizePriceV1RequestSchema(BaseSchema):
    # Catalog swagger.json

    
    seller_id = fields.Int(required=False)
    
    store_id = fields.Int(required=False)
    
    moq = fields.Int(required=False)
    
    pincode = fields.Str(required=False)
    
    items = fields.List(fields.Nested(ProductSizePriceV1RequestBody, required=False), required=False)
    


class ProductSizePriceV1RequestBody(BaseSchema):
    # Catalog swagger.json

    
    slug = fields.Str(required=False)
    
    size = fields.Str(required=False)
    
    parent_slug = fields.Str(required=False)
    
    product_grouping_id = fields.Str(required=False)
    


class ProductSizePriceResponseV1(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(ProductSizePriceResponseV4, required=False), required=False)
    


class Identifier(BaseSchema):
    # Catalog swagger.json

    
    ean = fields.Str(required=False)
    
    sku_code = fields.Str(required=False)
    
    alu = fields.Str(required=False)
    
    upc = fields.Str(required=False)
    
    isbn = fields.Str(required=False)
    


