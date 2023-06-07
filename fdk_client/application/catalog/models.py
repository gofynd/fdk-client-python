"""Catalog Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..ApplicationModel import BaseSchema




class ProductListingActionPage(BaseSchema):
    pass


class ProductListingAction(BaseSchema):
    pass


class Price(BaseSchema):
    pass


class ProductListingPrice(BaseSchema):
    pass


class ApplicationItemSEO(BaseSchema):
    pass


class Meta(BaseSchema):
    pass


class Media(BaseSchema):
    pass


class ProductBrand(BaseSchema):
    pass


class NetQuantity(BaseSchema):
    pass


class ProductCategoryMap(BaseSchema):
    pass


class ApplicationItemMOQ(BaseSchema):
    pass


class CustomMetaFields(BaseSchema):
    pass


class ProductDetailAttribute(BaseSchema):
    pass


class ProductDetailGroupedAttribute(BaseSchema):
    pass


class ProductDetail(BaseSchema):
    pass


class ErrorResponse(BaseSchema):
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


class Weight(BaseSchema):
    pass


class Dimension(BaseSchema):
    pass


class ProductSize(BaseSchema):
    pass


class ProductSizes(BaseSchema):
    pass


class AttributeDetail(BaseSchema):
    pass


class AttributeMetadata(BaseSchema):
    pass


class ProductsComparisonResponse(BaseSchema):
    pass


class ProductCompareResponse(BaseSchema):
    pass


class ProductFrequentlyComparedSimilarResponse(BaseSchema):
    pass


class ProductVariantItemResponse(BaseSchema):
    pass


class ProductVariantResponse(BaseSchema):
    pass


class ProductVariantsResponse(BaseSchema):
    pass


class StoreDetail(BaseSchema):
    pass


class ProductStockPrice(BaseSchema):
    pass


class Seller(BaseSchema):
    pass


class CompanyDetail(BaseSchema):
    pass


class ProductStockStatusItem(BaseSchema):
    pass


class ProductStockStatusResponse(BaseSchema):
    pass


class Page(BaseSchema):
    pass


class ProductStockPolling(BaseSchema):
    pass


class ProductFiltersKey(BaseSchema):
    pass


class ProductFiltersValue(BaseSchema):
    pass


class ProductFilters(BaseSchema):
    pass


class ProductSortOn(BaseSchema):
    pass


class ProductVariantListingResponse(BaseSchema):
    pass


class ProductListingDetail(BaseSchema):
    pass


class ProductListingResponse(BaseSchema):
    pass


class ImageUrls(BaseSchema):
    pass


class BrandItem(BaseSchema):
    pass


class BrandListingResponse(BaseSchema):
    pass


class BrandDetailResponse(BaseSchema):
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


class CategoryListingResponse(BaseSchema):
    pass


class CategoryMetaResponse(BaseSchema):
    pass


class HomeListingResponse(BaseSchema):
    pass


class Department(BaseSchema):
    pass


class DepartmentResponse(BaseSchema):
    pass


class AutocompleteItem(BaseSchema):
    pass


class AutoCompleteResponse(BaseSchema):
    pass


class CollectionListingFilterTag(BaseSchema):
    pass


class CollectionListingFilterType(BaseSchema):
    pass


class CollectionListingFilter(BaseSchema):
    pass


class CollectionQuery(BaseSchema):
    pass


class GetCollectionDetailNest(BaseSchema):
    pass


class GetCollectionListingResponse(BaseSchema):
    pass


class CollectionDetailResponse(BaseSchema):
    pass


class GetFollowListingResponse(BaseSchema):
    pass


class FollowPostResponse(BaseSchema):
    pass


class FollowerCountResponse(BaseSchema):
    pass


class FollowIdsData(BaseSchema):
    pass


class FollowIdsResponse(BaseSchema):
    pass


class LatLong(BaseSchema):
    pass


class Store(BaseSchema):
    pass


class StoreListingResponse(BaseSchema):
    pass


class SellerPhoneNumber(BaseSchema):
    pass


class StoreAddressSerializer(BaseSchema):
    pass


class StoreManagerSerializer(BaseSchema):
    pass


class StoreDepartments(BaseSchema):
    pass


class CompanyStore(BaseSchema):
    pass


class AppStore(BaseSchema):
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


class ProductStockPriceV3(BaseSchema):
    pass


class StoreV3(BaseSchema):
    pass


class DetailsSchemaV3(BaseSchema):
    pass


class MarketPlaceSttributesSchemaV3(BaseSchema):
    pass


class ReturnConfigSchemaV3(BaseSchema):
    pass


class SellerV3(BaseSchema):
    pass


class StrategyWiseListingSchemaV3(BaseSchema):
    pass


class ArticleAssignmentV3(BaseSchema):
    pass


class ProductSetDistributionSizeV3(BaseSchema):
    pass


class ProductSetDistributionV3(BaseSchema):
    pass


class ProductSetV3(BaseSchema):
    pass


class SellerGroupAttributes(BaseSchema):
    pass


class ProductStockUnitPriceV3(BaseSchema):
    pass


class ProductSizePriceResponseV3(BaseSchema):
    pass


class ProductSizeSellerFilterSchemaV3(BaseSchema):
    pass


class ProductSizeSellersResponseV3(BaseSchema):
    pass





class ProductListingActionPage(BaseSchema):
    # Catalog swagger.json

    
    type = fields.Str(required=False)
    
    params = fields.Dict(required=False)
    
    query = fields.Dict(required=False)
    


class ProductListingAction(BaseSchema):
    # Catalog swagger.json

    
    type = fields.Str(required=False)
    
    page = fields.Nested(ProductListingActionPage, required=False)
    


class Price(BaseSchema):
    # Catalog swagger.json

    
    currency_code = fields.Str(required=False)
    
    min = fields.Float(required=False)
    
    currency_symbol = fields.Str(required=False)
    
    max = fields.Float(required=False)
    


class ProductListingPrice(BaseSchema):
    # Catalog swagger.json

    
    effective = fields.Nested(Price, required=False)
    
    marked = fields.Nested(Price, required=False)
    


class ApplicationItemSEO(BaseSchema):
    # Catalog swagger.json

    
    description = fields.Raw(required=False)
    
    title = fields.Raw(required=False)
    


class Meta(BaseSchema):
    # Catalog swagger.json

    
    source = fields.Str(required=False)
    


class Media(BaseSchema):
    # Catalog swagger.json

    
    url = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    alt = fields.Str(required=False)
    
    meta = fields.Nested(Meta, required=False)
    


class ProductBrand(BaseSchema):
    # Catalog swagger.json

    
    description = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    logo = fields.Nested(Media, required=False)
    
    uid = fields.Int(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    


class NetQuantity(BaseSchema):
    # Catalog swagger.json

    
    value = fields.Float(required=False)
    
    unit = fields.Raw(required=False)
    


class ProductCategoryMap(BaseSchema):
    # Catalog swagger.json

    
    l3 = fields.Nested(ProductBrand, required=False)
    
    l2 = fields.Nested(ProductBrand, required=False)
    
    l1 = fields.Nested(ProductBrand, required=False)
    


class ApplicationItemMOQ(BaseSchema):
    # Catalog swagger.json

    
    maximum = fields.Int(required=False)
    
    increment_unit = fields.Int(required=False)
    
    minimum = fields.Int(required=False)
    


class CustomMetaFields(BaseSchema):
    # Catalog swagger.json

    
    value = fields.Str(required=False)
    
    key = fields.Str(required=False)
    


class ProductDetailAttribute(BaseSchema):
    # Catalog swagger.json

    
    type = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    key = fields.Str(required=False)
    


class ProductDetailGroupedAttribute(BaseSchema):
    # Catalog swagger.json

    
    details = fields.List(fields.Nested(ProductDetailAttribute, required=False), required=False)
    
    title = fields.Str(required=False)
    


class ProductDetail(BaseSchema):
    # Catalog swagger.json

    
    type = fields.Str(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    product_online_date = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    price = fields.Nested(ProductListingPrice, required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    is_dependent = fields.Boolean(required=False)
    
    seo = fields.Nested(ApplicationItemSEO, required=False)
    
    color = fields.Str(required=False)
    
    teaser_tag = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    brand = fields.Nested(ProductBrand, required=False)
    
    discount = fields.Str(required=False)
    
    net_quantity = fields.Nested(NetQuantity, required=False)
    
    category_map = fields.Nested(ProductCategoryMap, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    similars = fields.List(fields.Str(required=False), required=False)
    
    image_nature = fields.Str(required=False)
    
    attributes = fields.Dict(required=False)
    
    rating = fields.Float(required=False)
    
    description = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    medias = fields.List(fields.Nested(Media, required=False), required=False)
    
    moq = fields.Nested(ApplicationItemMOQ, required=False)
    
    item_type = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    has_variant = fields.Boolean(required=False)
    
    categories = fields.List(fields.Nested(ProductBrand, required=False), required=False)
    
    item_code = fields.Str(required=False)
    
    _custom_meta = fields.List(fields.Nested(CustomMetaFields, required=False), required=False)
    
    grouped_attributes = fields.List(fields.Nested(ProductDetailGroupedAttribute, required=False), required=False)
    
    short_description = fields.Str(required=False)
    
    rating_count = fields.Int(required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    


class ErrorResponse(BaseSchema):
    # Catalog swagger.json

    
    error = fields.Str(required=False)
    


class SizeChartValues(BaseSchema):
    # Catalog swagger.json

    
    col_3 = fields.Str(required=False)
    
    col_1 = fields.Str(required=False)
    
    col_6 = fields.Str(required=False)
    
    col_5 = fields.Str(required=False)
    
    col_2 = fields.Str(required=False)
    
    col_4 = fields.Str(required=False)
    


class ColumnHeader(BaseSchema):
    # Catalog swagger.json

    
    convertable = fields.Boolean(required=False)
    
    value = fields.Str(required=False)
    


class ColumnHeaders(BaseSchema):
    # Catalog swagger.json

    
    col_3 = fields.Nested(ColumnHeader, required=False)
    
    col_1 = fields.Nested(ColumnHeader, required=False)
    
    col_6 = fields.Nested(ColumnHeader, required=False)
    
    col_5 = fields.Nested(ColumnHeader, required=False)
    
    col_2 = fields.Nested(ColumnHeader, required=False)
    
    col_4 = fields.Nested(ColumnHeader, required=False)
    


class SizeChart(BaseSchema):
    # Catalog swagger.json

    
    unit = fields.Str(required=False)
    
    sizes = fields.List(fields.Nested(SizeChartValues, required=False), required=False)
    
    description = fields.Str(required=False)
    
    image = fields.Str(required=False)
    
    size_tip = fields.Str(required=False)
    
    headers = fields.Nested(ColumnHeaders, required=False)
    
    title = fields.Str(required=False)
    


class ProductSizeStores(BaseSchema):
    # Catalog swagger.json

    
    count = fields.Int(required=False)
    


class Weight(BaseSchema):
    # Catalog swagger.json

    
    is_default = fields.Boolean(required=False)
    
    unit = fields.Str(required=False)
    
    shipping = fields.Float(required=False)
    


class Dimension(BaseSchema):
    # Catalog swagger.json

    
    height = fields.Float(required=False)
    
    unit = fields.Str(required=False)
    
    width = fields.Float(required=False)
    
    is_default = fields.Boolean(required=False)
    
    length = fields.Float(required=False)
    


class ProductSize(BaseSchema):
    # Catalog swagger.json

    
    value = fields.Str(required=False)
    
    seller_identifiers = fields.List(fields.Str(required=False), required=False)
    
    weight = fields.Nested(Weight, required=False)
    
    display = fields.Str(required=False)
    
    is_available = fields.Boolean(required=False)
    
    dimension = fields.Nested(Dimension, required=False)
    
    quantity = fields.Int(required=False)
    


class ProductSizes(BaseSchema):
    # Catalog swagger.json

    
    size_chart = fields.Nested(SizeChart, required=False)
    
    stores = fields.Nested(ProductSizeStores, required=False)
    
    sizes = fields.List(fields.Nested(ProductSize, required=False), required=False)
    
    price = fields.Nested(ProductListingPrice, required=False)
    
    discount = fields.Str(required=False)
    
    multi_size = fields.Boolean(required=False)
    
    sellable = fields.Boolean(required=False)
    


class AttributeDetail(BaseSchema):
    # Catalog swagger.json

    
    display = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    description = fields.Str(required=False)
    


class AttributeMetadata(BaseSchema):
    # Catalog swagger.json

    
    details = fields.List(fields.Nested(AttributeDetail, required=False), required=False)
    
    title = fields.Str(required=False)
    


class ProductsComparisonResponse(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(ProductDetail, required=False), required=False)
    
    attributes_metadata = fields.List(fields.Nested(AttributeMetadata, required=False), required=False)
    


class ProductCompareResponse(BaseSchema):
    # Catalog swagger.json

    
    attributes_metadata = fields.List(fields.Nested(AttributeMetadata, required=False), required=False)
    
    items = fields.List(fields.Nested(ProductDetail, required=False), required=False)
    
    subtitle = fields.Str(required=False)
    
    title = fields.Str(required=False)
    


class ProductFrequentlyComparedSimilarResponse(BaseSchema):
    # Catalog swagger.json

    
    similars = fields.Nested(ProductCompareResponse, required=False)
    


class ProductVariantItemResponse(BaseSchema):
    # Catalog swagger.json

    
    value = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    color = fields.Str(required=False)
    
    color_name = fields.Str(required=False)
    
    is_available = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    _custom_meta = fields.List(fields.Nested(CustomMetaFields, required=False), required=False)
    
    uid = fields.Int(required=False)
    
    medias = fields.List(fields.Nested(Media, required=False), required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    


class ProductVariantResponse(BaseSchema):
    # Catalog swagger.json

    
    key = fields.Str(required=False)
    
    items = fields.List(fields.Nested(ProductVariantItemResponse, required=False), required=False)
    
    header = fields.Str(required=False)
    
    display_type = fields.Str(required=False)
    


class ProductVariantsResponse(BaseSchema):
    # Catalog swagger.json

    
    variants = fields.List(fields.Nested(ProductVariantResponse, required=False), required=False)
    


class StoreDetail(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    id = fields.Int(required=False)
    


class ProductStockPrice(BaseSchema):
    # Catalog swagger.json

    
    currency = fields.Str(required=False)
    
    effective = fields.Float(required=False)
    
    marked = fields.Float(required=False)
    


class Seller(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    count = fields.Int(required=False)
    
    uid = fields.Int(required=False)
    


class CompanyDetail(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    id = fields.Int(required=False)
    


class ProductStockStatusItem(BaseSchema):
    # Catalog swagger.json

    
    item_id = fields.Int(required=False)
    
    identifier = fields.Dict(required=False)
    
    size = fields.Str(required=False)
    
    store = fields.Nested(StoreDetail, required=False)
    
    uid = fields.Str(required=False)
    
    price = fields.Nested(ProductStockPrice, required=False)
    
    seller = fields.Nested(Seller, required=False)
    
    company = fields.Nested(CompanyDetail, required=False)
    
    quantity = fields.Int(required=False)
    


class ProductStockStatusResponse(BaseSchema):
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
    


class ProductStockPolling(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(ProductStockStatusItem, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class ProductFiltersKey(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    display = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    kind = fields.Str(required=False)
    


class ProductFiltersValue(BaseSchema):
    # Catalog swagger.json

    
    value = fields.Str(required=False)
    
    currency_symbol = fields.Str(required=False)
    
    is_selected = fields.Boolean(required=False)
    
    currency_code = fields.Str(required=False)
    
    display = fields.Str(required=False)
    
    min = fields.Int(required=False)
    
    selected_min = fields.Int(required=False)
    
    count = fields.Int(required=False)
    
    selected_max = fields.Int(required=False)
    
    display_format = fields.Str(required=False)
    
    max = fields.Int(required=False)
    
    query_format = fields.Str(required=False)
    


class ProductFilters(BaseSchema):
    # Catalog swagger.json

    
    key = fields.Nested(ProductFiltersKey, required=False)
    
    values = fields.List(fields.Nested(ProductFiltersValue, required=False), required=False)
    


class ProductSortOn(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    is_selected = fields.Boolean(required=False)
    


class ProductVariantListingResponse(BaseSchema):
    # Catalog swagger.json

    
    key = fields.Str(required=False)
    
    header = fields.Str(required=False)
    
    total = fields.Int(required=False)
    
    display_type = fields.Str(required=False)
    
    items = fields.List(fields.Nested(ProductVariantItemResponse, required=False), required=False)
    


class ProductListingDetail(BaseSchema):
    # Catalog swagger.json

    
    type = fields.Str(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    product_online_date = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    price = fields.Nested(ProductListingPrice, required=False)
    
    variants = fields.List(fields.Nested(ProductVariantListingResponse, required=False), required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    is_dependent = fields.Boolean(required=False)
    
    seo = fields.Nested(ApplicationItemSEO, required=False)
    
    color = fields.Str(required=False)
    
    teaser_tag = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    brand = fields.Nested(ProductBrand, required=False)
    
    discount = fields.Str(required=False)
    
    net_quantity = fields.Nested(NetQuantity, required=False)
    
    category_map = fields.Nested(ProductCategoryMap, required=False)
    
    sellable = fields.Boolean(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    similars = fields.List(fields.Str(required=False), required=False)
    
    image_nature = fields.Str(required=False)
    
    attributes = fields.Dict(required=False)
    
    sizes = fields.List(fields.Str(required=False), required=False)
    
    rating = fields.Float(required=False)
    
    description = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    medias = fields.List(fields.Nested(Media, required=False), required=False)
    
    moq = fields.Nested(ApplicationItemMOQ, required=False)
    
    item_type = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    has_variant = fields.Boolean(required=False)
    
    identifiers = fields.List(fields.Str(required=False), required=False)
    
    categories = fields.List(fields.Nested(ProductBrand, required=False), required=False)
    
    item_code = fields.Str(required=False)
    
    _custom_meta = fields.List(fields.Nested(CustomMetaFields, required=False), required=False)
    
    grouped_attributes = fields.List(fields.Nested(ProductDetailGroupedAttribute, required=False), required=False)
    
    short_description = fields.Str(required=False)
    
    rating_count = fields.Int(required=False)
    
    highlights = fields.List(fields.Str(required=False), required=False)
    


class ProductListingResponse(BaseSchema):
    # Catalog swagger.json

    
    filters = fields.List(fields.Nested(ProductFilters, required=False), required=False)
    
    sort_on = fields.List(fields.Nested(ProductSortOn, required=False), required=False)
    
    items = fields.List(fields.Nested(ProductListingDetail, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class ImageUrls(BaseSchema):
    # Catalog swagger.json

    
    portrait = fields.Nested(Media, required=False)
    
    landscape = fields.Nested(Media, required=False)
    


class BrandItem(BaseSchema):
    # Catalog swagger.json

    
    slug = fields.Str(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    description = fields.Str(required=False)
    
    departments = fields.List(fields.Str(required=False), required=False)
    
    name = fields.Str(required=False)
    
    logo = fields.Nested(Media, required=False)
    
    uid = fields.Int(required=False)
    
    discount = fields.Str(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    


class BrandListingResponse(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(BrandItem, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class BrandDetailResponse(BaseSchema):
    # Catalog swagger.json

    
    _custom_json = fields.Dict(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    description = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    logo = fields.Nested(Media, required=False)
    
    uid = fields.Int(required=False)
    


class CategoryBanner(BaseSchema):
    # Catalog swagger.json

    
    portrait = fields.Nested(Media, required=False)
    
    landscape = fields.Nested(Media, required=False)
    


class ThirdLevelChild(BaseSchema):
    # Catalog swagger.json

    
    _custom_json = fields.Dict(required=False)
    
    slug = fields.Str(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    name = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    childs = fields.List(fields.Dict(required=False), required=False)
    


class SecondLevelChild(BaseSchema):
    # Catalog swagger.json

    
    _custom_json = fields.Dict(required=False)
    
    slug = fields.Str(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    name = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    childs = fields.List(fields.Nested(ThirdLevelChild, required=False), required=False)
    


class Child(BaseSchema):
    # Catalog swagger.json

    
    _custom_json = fields.Dict(required=False)
    
    slug = fields.Str(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    name = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    childs = fields.List(fields.Nested(SecondLevelChild, required=False), required=False)
    


class CategoryItems(BaseSchema):
    # Catalog swagger.json

    
    slug = fields.Str(required=False)
    
    banners = fields.Nested(CategoryBanner, required=False)
    
    name = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    childs = fields.List(fields.Nested(Child, required=False), required=False)
    


class DepartmentCategoryTree(BaseSchema):
    # Catalog swagger.json

    
    department = fields.Str(required=False)
    
    items = fields.List(fields.Nested(CategoryItems, required=False), required=False)
    


class DepartmentIdentifier(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    slug = fields.Str(required=False)
    


class CategoryListingResponse(BaseSchema):
    # Catalog swagger.json

    
    data = fields.List(fields.Nested(DepartmentCategoryTree, required=False), required=False)
    
    departments = fields.List(fields.Nested(DepartmentIdentifier, required=False), required=False)
    


class CategoryMetaResponse(BaseSchema):
    # Catalog swagger.json

    
    _custom_json = fields.Dict(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    name = fields.Str(required=False)
    
    logo = fields.Nested(Media, required=False)
    
    uid = fields.Int(required=False)
    


class HomeListingResponse(BaseSchema):
    # Catalog swagger.json

    
    message = fields.Str(required=False)
    
    items = fields.List(fields.Nested(ProductListingDetail, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class Department(BaseSchema):
    # Catalog swagger.json

    
    slug = fields.Str(required=False)
    
    priority_order = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    logo = fields.Nested(Media, required=False)
    
    uid = fields.Int(required=False)
    


class DepartmentResponse(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(Department, required=False), required=False)
    


class AutocompleteItem(BaseSchema):
    # Catalog swagger.json

    
    _custom_json = fields.Dict(required=False)
    
    type = fields.Str(required=False)
    
    display = fields.Str(required=False)
    
    logo = fields.Nested(Media, required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    


class AutoCompleteResponse(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(AutocompleteItem, required=False), required=False)
    


class CollectionListingFilterTag(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    display = fields.Str(required=False)
    
    is_selected = fields.Boolean(required=False)
    


class CollectionListingFilterType(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    display = fields.Str(required=False)
    
    is_selected = fields.Boolean(required=False)
    


class CollectionListingFilter(BaseSchema):
    # Catalog swagger.json

    
    tags = fields.List(fields.Nested(CollectionListingFilterTag, required=False), required=False)
    
    type = fields.List(fields.Nested(CollectionListingFilterType, required=False), required=False)
    


class CollectionQuery(BaseSchema):
    # Catalog swagger.json

    
    value = fields.List(fields.Raw(required=False), required=False)
    
    op = fields.Str(required=False)
    
    attribute = fields.Str(required=False)
    


class GetCollectionDetailNest(BaseSchema):
    # Catalog swagger.json

    
    type = fields.Str(required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    priority = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    badge = fields.Dict(required=False)
    
    sort_on = fields.Str(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    _schedule = fields.Dict(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    uid = fields.Str(required=False)
    
    cron = fields.Dict(required=False)
    
    app_id = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    description = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    slug = fields.Str(required=False)
    
    tag = fields.List(fields.Str(required=False), required=False)
    
    logo = fields.Nested(Media, required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    


class GetCollectionListingResponse(BaseSchema):
    # Catalog swagger.json

    
    filters = fields.Nested(CollectionListingFilter, required=False)
    
    items = fields.List(fields.Nested(GetCollectionDetailNest, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class CollectionDetailResponse(BaseSchema):
    # Catalog swagger.json

    
    type = fields.Str(required=False)
    
    query = fields.List(fields.Nested(CollectionQuery, required=False), required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    priority = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    badge = fields.Dict(required=False)
    
    sort_on = fields.Str(required=False)
    
    visible_facets_keys = fields.List(fields.Str(required=False), required=False)
    
    _schedule = fields.Dict(required=False)
    
    allow_facets = fields.Boolean(required=False)
    
    cron = fields.Dict(required=False)
    
    app_id = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    allow_sort = fields.Boolean(required=False)
    
    description = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    slug = fields.Str(required=False)
    
    tag = fields.List(fields.Str(required=False), required=False)
    
    logo = fields.Nested(Media, required=False)
    


class GetFollowListingResponse(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(ProductListingDetail, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class FollowPostResponse(BaseSchema):
    # Catalog swagger.json

    
    message = fields.Str(required=False)
    
    id = fields.Str(required=False)
    


class FollowerCountResponse(BaseSchema):
    # Catalog swagger.json

    
    count = fields.Int(required=False)
    


class FollowIdsData(BaseSchema):
    # Catalog swagger.json

    
    products = fields.List(fields.Int(required=False), required=False)
    
    brands = fields.List(fields.Int(required=False), required=False)
    
    collections = fields.List(fields.Int(required=False), required=False)
    


class FollowIdsResponse(BaseSchema):
    # Catalog swagger.json

    
    data = fields.Nested(FollowIdsData, required=False)
    


class LatLong(BaseSchema):
    # Catalog swagger.json

    
    type = fields.Str(required=False)
    
    coordinates = fields.List(fields.Float(required=False), required=False)
    


class Store(BaseSchema):
    # Catalog swagger.json

    
    store_code = fields.Str(required=False)
    
    address = fields.Str(required=False)
    
    store_email = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    pincode = fields.Int(required=False)
    
    uid = fields.Int(required=False)
    
    state = fields.Str(required=False)
    
    lat_long = fields.Nested(LatLong, required=False)
    
    city = fields.Str(required=False)
    


class StoreListingResponse(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(Store, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class SellerPhoneNumber(BaseSchema):
    # Catalog swagger.json

    
    number = fields.Str(required=False)
    
    country_code = fields.Int(required=False)
    


class StoreAddressSerializer(BaseSchema):
    # Catalog swagger.json

    
    latitude = fields.Float(required=False)
    
    country = fields.Str(required=False)
    
    longitude = fields.Float(required=False)
    
    address2 = fields.Str(required=False)
    
    pincode = fields.Int(required=False)
    
    landmark = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    address1 = fields.Str(required=False)
    
    city = fields.Str(required=False)
    


class StoreManagerSerializer(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    mobile_no = fields.Nested(SellerPhoneNumber, required=False)
    


class StoreDepartments(BaseSchema):
    # Catalog swagger.json

    
    slug = fields.Str(required=False)
    
    priority_order = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    logo = fields.Dict(required=False)
    
    uid = fields.Int(required=False)
    


class CompanyStore(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    business_type = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    company_type = fields.Str(required=False)
    


class AppStore(BaseSchema):
    # Catalog swagger.json

    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    store_code = fields.Str(required=False)
    
    address = fields.Nested(StoreAddressSerializer, required=False)
    
    manager = fields.Nested(StoreManagerSerializer, required=False)
    
    departments = fields.List(fields.Nested(StoreDepartments, required=False), required=False)
    
    name = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    company = fields.Nested(CompanyStore, required=False)
    


class ApplicationStoreListing(BaseSchema):
    # Catalog swagger.json

    
    filters = fields.List(fields.Dict(required=False), required=False)
    
    items = fields.List(fields.Nested(AppStore, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class Time(BaseSchema):
    # Catalog swagger.json

    
    minute = fields.Int(required=False)
    
    hour = fields.Int(required=False)
    


class StoreTiming(BaseSchema):
    # Catalog swagger.json

    
    closing = fields.Nested(Time, required=False)
    
    opening = fields.Nested(Time, required=False)
    
    weekday = fields.Str(required=False)
    
    open = fields.Boolean(required=False)
    


class StoreDetails(BaseSchema):
    # Catalog swagger.json

    
    contact_numbers = fields.List(fields.Nested(SellerPhoneNumber, required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    timing = fields.List(fields.Nested(StoreTiming, required=False), required=False)
    
    store_code = fields.Str(required=False)
    
    address = fields.Nested(StoreAddressSerializer, required=False)
    
    manager = fields.Nested(StoreManagerSerializer, required=False)
    
    departments = fields.List(fields.Nested(StoreDepartments, required=False), required=False)
    
    name = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    company = fields.Nested(CompanyStore, required=False)
    


class UserDetail(BaseSchema):
    # Catalog swagger.json

    
    username = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
    super_user = fields.Boolean(required=False)
    
    contact = fields.Str(required=False)
    


class Size(BaseSchema):
    # Catalog swagger.json

    
    value = fields.Raw(required=False)
    
    display = fields.Raw(required=False)
    
    is_available = fields.Boolean(required=False)
    
    quantity = fields.Int(required=False)
    


class ProductGroupPrice(BaseSchema):
    # Catalog swagger.json

    
    currency = fields.Raw(required=False)
    
    max_marked = fields.Float(required=False)
    
    min_effective = fields.Float(required=False)
    
    min_marked = fields.Float(required=False)
    
    max_effective = fields.Float(required=False)
    


class ProductDetails(BaseSchema):
    # Catalog swagger.json

    
    out_of_stock = fields.Boolean(required=False)
    
    identifier = fields.Dict(required=False)
    
    name = fields.Raw(required=False)
    
    rating_count = fields.Int(required=False)
    
    template_tag = fields.Raw(required=False)
    
    media = fields.List(fields.Dict(required=False), required=False)
    
    image_nature = fields.Raw(required=False)
    
    hsn_code = fields.Int(required=False)
    
    attributes = fields.Dict(required=False)
    
    country_of_origin = fields.Raw(required=False)
    
    description = fields.Raw(required=False)
    
    rating = fields.Float(required=False)
    
    images = fields.List(fields.Raw(required=False), required=False)
    
    is_set = fields.Boolean(required=False)
    
    has_variant = fields.Boolean(required=False)
    
    slug = fields.Raw(required=False)
    
    item_code = fields.Raw(required=False)
    
    grouped_attributes = fields.Dict(required=False)
    
    short_description = fields.Raw(required=False)
    
    brand_uid = fields.Int(required=False)
    
    highlights = fields.List(fields.Raw(required=False), required=False)
    


class ProductInGroup(BaseSchema):
    # Catalog swagger.json

    
    auto_add_to_cart = fields.Boolean(required=False)
    
    max_quantity = fields.Int(required=False)
    
    min_quantity = fields.Int(required=False)
    
    sizes = fields.List(fields.Nested(Size, required=False), required=False)
    
    auto_select = fields.Boolean(required=False)
    
    price = fields.Nested(ProductGroupPrice, required=False)
    
    allow_remove = fields.Boolean(required=False)
    
    product_uid = fields.Int(required=False)
    
    product_details = fields.Nested(ProductDetails, required=False)
    


class ProductGroupingModel(BaseSchema):
    # Catalog swagger.json

    
    is_active = fields.Boolean(required=False)
    
    created_on = fields.Str(required=False)
    
    slug = fields.Raw(required=False)
    
    created_by = fields.Nested(UserDetail, required=False)
    
    company_id = fields.Int(required=False)
    
    modified_on = fields.Str(required=False)
    
    verified_by = fields.Nested(UserDetail, required=False)
    
    name = fields.Raw(required=False)
    
    page_visibility = fields.List(fields.Raw(required=False), required=False)
    
    _id = fields.Raw(required=False)
    
    modified_by = fields.Nested(UserDetail, required=False)
    
    logo = fields.Raw(required=False)
    
    meta = fields.Dict(required=False)
    
    same_store_assignment = fields.Boolean(required=False)
    
    products = fields.List(fields.Nested(ProductInGroup, required=False), required=False)
    
    choice = fields.Raw(required=False)
    
    verified_on = fields.Str(required=False)
    


class ProductBundle(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(ProductGroupingModel, required=False), required=False)
    


class ProductStockPriceV3(BaseSchema):
    # Catalog swagger.json

    
    currency = fields.Str(required=False)
    
    effective = fields.Float(required=False)
    
    marked = fields.Float(required=False)
    


class StoreV3(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    count = fields.Int(required=False)
    
    uid = fields.Int(required=False)
    


class DetailsSchemaV3(BaseSchema):
    # Catalog swagger.json

    
    type = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    key = fields.Str(required=False)
    


class MarketPlaceSttributesSchemaV3(BaseSchema):
    # Catalog swagger.json

    
    details = fields.List(fields.Nested(DetailsSchemaV3, required=False), required=False)
    
    title = fields.Str(required=False)
    


class ReturnConfigSchemaV3(BaseSchema):
    # Catalog swagger.json

    
    returnable = fields.Boolean(required=False)
    
    unit = fields.Str(required=False)
    
    time = fields.Int(required=False)
    


class SellerV3(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    count = fields.Int(required=False)
    
    uid = fields.Int(required=False)
    


class StrategyWiseListingSchemaV3(BaseSchema):
    # Catalog swagger.json

    
    tat = fields.Int(required=False)
    
    pincode = fields.Int(required=False)
    
    distance = fields.Int(required=False)
    
    quantity = fields.Int(required=False)
    


class ArticleAssignmentV3(BaseSchema):
    # Catalog swagger.json

    
    level = fields.Str(required=False)
    
    strategy = fields.Str(required=False)
    


class ProductSetDistributionSizeV3(BaseSchema):
    # Catalog swagger.json

    
    size = fields.Str(required=False)
    
    pieces = fields.Int(required=False)
    


class ProductSetDistributionV3(BaseSchema):
    # Catalog swagger.json

    
    sizes = fields.List(fields.Nested(ProductSetDistributionSizeV3, required=False), required=False)
    


class ProductSetV3(BaseSchema):
    # Catalog swagger.json

    
    quantity = fields.Int(required=False)
    
    size_distribution = fields.Nested(ProductSetDistributionV3, required=False)
    


class SellerGroupAttributes(BaseSchema):
    # Catalog swagger.json

    
    details = fields.List(fields.Nested(DetailsSchemaV3, required=False), required=False)
    
    title = fields.Str(required=False)
    


class ProductStockUnitPriceV3(BaseSchema):
    # Catalog swagger.json

    
    unit = fields.Str(required=False)
    
    price = fields.Float(required=False)
    
    currency_symbol = fields.Str(required=False)
    
    currency_code = fields.Str(required=False)
    


class ProductSizePriceResponseV3(BaseSchema):
    # Catalog swagger.json

    
    is_cod = fields.Boolean(required=False)
    
    price = fields.Nested(ProductStockPriceV3, required=False)
    
    store = fields.Nested(StoreV3, required=False)
    
    marketplace_attributes = fields.List(fields.Nested(MarketPlaceSttributesSchemaV3, required=False), required=False)
    
    is_gift = fields.Boolean(required=False)
    
    price_per_piece = fields.Nested(ProductStockPriceV3, required=False)
    
    special_badge = fields.Str(required=False)
    
    return_config = fields.Nested(ReturnConfigSchemaV3, required=False)
    
    seller = fields.Nested(SellerV3, required=False)
    
    discount = fields.Str(required=False)
    
    article_id = fields.Str(required=False)
    
    seller_count = fields.Int(required=False)
    
    long_lat = fields.List(fields.Float(required=False), required=False)
    
    strategy_wise_listing = fields.List(fields.Nested(StrategyWiseListingSchemaV3, required=False), required=False)
    
    pincode = fields.Int(required=False)
    
    article_assignment = fields.Nested(ArticleAssignmentV3, required=False)
    
    quantity = fields.Int(required=False)
    
    item_type = fields.Str(required=False)
    
    set = fields.Nested(ProductSetV3, required=False)
    
    grouped_attributes = fields.List(fields.Nested(SellerGroupAttributes, required=False), required=False)
    
    price_per_unit = fields.Nested(ProductStockUnitPriceV3, required=False)
    


class ProductSizeSellerFilterSchemaV3(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    is_selected = fields.Boolean(required=False)
    


class ProductSizeSellersResponseV3(BaseSchema):
    # Catalog swagger.json

    
    sort_on = fields.List(fields.Nested(ProductSizeSellerFilterSchemaV3, required=False), required=False)
    
    items = fields.List(fields.Nested(ProductSizePriceResponseV3, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


