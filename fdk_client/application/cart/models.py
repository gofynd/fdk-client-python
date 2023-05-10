"""Cart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..ApplicationModel import BaseSchema




class RawBreakupSchema(BaseSchema):
    pass


class DisplayBreakupSchema(BaseSchema):
    pass


class CouponBreakupSchema(BaseSchema):
    pass


class LoyaltyPoints(BaseSchema):
    pass


class CartBreakupSchema(BaseSchema):
    pass


class PromiseFormatted(BaseSchema):
    pass


class PromiseTimestamp(BaseSchema):
    pass


class ShipmentPromise(BaseSchema):
    pass


class CartCurrencySchema(BaseSchema):
    pass


class BuyRulesSchema(BaseSchema):
    pass


class DiscountRulesAppSchema(BaseSchema):
    pass


class Ownership(BaseSchema):
    pass


class FreeGiftItemSchema(BaseSchema):
    pass


class AppliedFreeArticlesSchema(BaseSchema):
    pass


class AppliedPromotion(BaseSchema):
    pass


class PaymentSelectionLock(BaseSchema):
    pass


class CartProductIdentifer(BaseSchema):
    pass


class BaseInfo(BaseSchema):
    pass


class BasePriceSchema(BaseSchema):
    pass


class ArticlePriceInfo(BaseSchema):
    pass


class ProductArticle(BaseSchema):
    pass


class ProductPrice(BaseSchema):
    pass


class ProductPriceInfo(BaseSchema):
    pass


class ProductAvailabilitySize(BaseSchema):
    pass


class ProductAvailability(BaseSchema):
    pass


class ActionQuery(BaseSchema):
    pass


class ProductAction(BaseSchema):
    pass


class Tags(BaseSchema):
    pass


class ProductImage(BaseSchema):
    pass


class NetQuantity(BaseSchema):
    pass


class CategoryInfo(BaseSchema):
    pass


class CartProduct(BaseSchema):
    pass


class CouponDetails(BaseSchema):
    pass


class PromoMeta(BaseSchema):
    pass


class CartProductInfo(BaseSchema):
    pass


class CartDetailResponse(BaseSchema):
    pass


class AddProductCart(BaseSchema):
    pass


class AddCartRequest(BaseSchema):
    pass


class AddCartDetailResponse(BaseSchema):
    pass


class UpdateProductCart(BaseSchema):
    pass


class UpdateCartRequest(BaseSchema):
    pass


class UpdateCartDetailResponse(BaseSchema):
    pass


class DeleteCartDetailResponse(BaseSchema):
    pass


class CartItemCountResponse(BaseSchema):
    pass


class PageCouponSchema(BaseSchema):
    pass


class Coupon(BaseSchema):
    pass


class GetCouponResponse(BaseSchema):
    pass


class ApplyCouponRequest(BaseSchema):
    pass


class OfferPrice(BaseSchema):
    pass


class OfferItemSchema(BaseSchema):
    pass


class OfferSellerSchema(BaseSchema):
    pass


class BulkPriceOfferSchema(BaseSchema):
    pass


class BulkPriceResponse(BaseSchema):
    pass


class RewardPointRequestSchema(BaseSchema):
    pass


class GeoLocation(BaseSchema):
    pass


class Address(BaseSchema):
    pass


class GetAddressesResponse(BaseSchema):
    pass


class SaveAddressResponse(BaseSchema):
    pass


class UpdateAddressResponse(BaseSchema):
    pass


class DeleteAddressResponse(BaseSchema):
    pass


class SelectCartAddressRequest(BaseSchema):
    pass


class UpdateCartPaymentRequest(BaseSchema):
    pass


class CouponValidity(BaseSchema):
    pass


class PaymentCouponValidateSchema(BaseSchema):
    pass


class ShipmentResponse(BaseSchema):
    pass


class CartShipmentsResponse(BaseSchema):
    pass


class StaffCheckoutSchema(BaseSchema):
    pass


class CartCheckoutCustomMetaSchema(BaseSchema):
    pass


class CartCheckoutDetailRequest(BaseSchema):
    pass


class CheckCartSchema(BaseSchema):
    pass


class CartCheckoutResponseSchema(BaseSchema):
    pass


class GiftDetailSchema(BaseSchema):
    pass


class ArticleGiftDetailSchema(BaseSchema):
    pass


class CartMetaRequest(BaseSchema):
    pass


class CartMetaResponse(BaseSchema):
    pass


class CartMetaMissingResponse(BaseSchema):
    pass


class GetShareCartLinkRequest(BaseSchema):
    pass


class GetShareCartLinkResponse(BaseSchema):
    pass


class SharedCartDetails(BaseSchema):
    pass


class SharedCart(BaseSchema):
    pass


class SharedCartResponse(BaseSchema):
    pass


class FreeGiftItemsSchema(BaseSchema):
    pass


class PromotionOffer(BaseSchema):
    pass


class PromotionOffersResponse(BaseSchema):
    pass


class OperationErrorResponse(BaseSchema):
    pass


class CurrencyInfoSchema(BaseSchema):
    pass


class LadderPrice(BaseSchema):
    pass


class LadderOfferItemSchema(BaseSchema):
    pass


class LadderPriceOffer(BaseSchema):
    pass


class LadderPriceOffers(BaseSchema):
    pass


class PaymentMetaSchema(BaseSchema):
    pass


class PaymentMethodSchema(BaseSchema):
    pass


class CartCheckoutDetailV2Request(BaseSchema):
    pass





class RawBreakupSchema(BaseSchema):
    # Cart swagger.json

    
    convenience_fee = fields.Float(required=False)
    
    vog = fields.Float(required=False)
    
    subtotal = fields.Float(required=False)
    
    you_saved = fields.Float(required=False)
    
    gift_card = fields.Float(required=False)
    
    total = fields.Float(required=False)
    
    discount = fields.Float(required=False)
    
    coupon = fields.Float(required=False)
    
    cod_charge = fields.Float(required=False)
    
    mrp_total = fields.Float(required=False)
    
    delivery_charge = fields.Float(required=False)
    
    gst_charges = fields.Float(required=False)
    
    fynd_cash = fields.Float(required=False)
    


class DisplayBreakupSchema(BaseSchema):
    # Cart swagger.json

    
    currency_code = fields.Str(required=False)
    
    display = fields.Str(required=False)
    
    currency_symbol = fields.Str(required=False)
    
    message = fields.List(fields.Str(required=False), required=False)
    
    value = fields.Float(required=False)
    
    key = fields.Str(required=False)
    


class CouponBreakupSchema(BaseSchema):
    # Cart swagger.json

    
    description = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    coupon_value = fields.Float(required=False)
    
    sub_title = fields.Str(required=False)
    
    is_applied = fields.Boolean(required=False)
    
    coupon_type = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    minimum_cart_value = fields.Float(required=False)
    
    value = fields.Float(required=False)
    
    max_discount_value = fields.Float(required=False)
    
    type = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    


class LoyaltyPoints(BaseSchema):
    # Cart swagger.json

    
    description = fields.Str(required=False)
    
    applicable = fields.Float(required=False)
    
    total = fields.Float(required=False)
    
    is_applied = fields.Boolean(required=False)
    


class CartBreakupSchema(BaseSchema):
    # Cart swagger.json

    
    raw = fields.Nested(RawBreakupSchema, required=False)
    
    display = fields.List(fields.Nested(DisplayBreakupSchema, required=False), required=False)
    
    coupon = fields.Nested(CouponBreakupSchema, required=False)
    
    loyalty_points = fields.Nested(LoyaltyPoints, required=False)
    


class PromiseFormatted(BaseSchema):
    # Cart swagger.json

    
    min = fields.Str(required=False)
    
    max = fields.Str(required=False)
    


class PromiseTimestamp(BaseSchema):
    # Cart swagger.json

    
    min = fields.Float(required=False)
    
    max = fields.Float(required=False)
    


class ShipmentPromise(BaseSchema):
    # Cart swagger.json

    
    formatted = fields.Nested(PromiseFormatted, required=False)
    
    timestamp = fields.Nested(PromiseTimestamp, required=False)
    


class CartCurrencySchema(BaseSchema):
    # Cart swagger.json

    
    symbol = fields.Str(required=False)
    
    code = fields.Str(required=False)
    


class BuyRulesSchema(BaseSchema):
    # Cart swagger.json

    
    cart_conditions = fields.Dict(required=False)
    
    item_criteria = fields.Dict(required=False)
    


class DiscountRulesAppSchema(BaseSchema):
    # Cart swagger.json

    
    offer = fields.Dict(required=False)
    
    item_criteria = fields.Dict(required=False)
    
    matched_buy_rules = fields.List(fields.Str(required=False), required=False)
    
    raw_offer = fields.Dict(required=False)
    


class Ownership(BaseSchema):
    # Cart swagger.json

    
    payable_category = fields.Str(required=False)
    
    payable_by = fields.Str(required=False)
    


class FreeGiftItemSchema(BaseSchema):
    # Cart swagger.json

    
    item_id = fields.Int(required=False)
    
    item_price_details = fields.Dict(required=False)
    
    item_name = fields.Str(required=False)
    
    item_slug = fields.Str(required=False)
    
    item_images_url = fields.List(fields.Str(required=False), required=False)
    
    item_brand_name = fields.Str(required=False)
    


class AppliedFreeArticlesSchema(BaseSchema):
    # Cart swagger.json

    
    free_gift_item_details = fields.Nested(FreeGiftItemSchema, required=False)
    
    article_id = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    parent_item_identifier = fields.Str(required=False)
    


class AppliedPromotion(BaseSchema):
    # Cart swagger.json

    
    mrp_promotion = fields.Boolean(required=False)
    
    promotion_name = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
    offer_text = fields.Str(required=False)
    
    buy_rules = fields.List(fields.Nested(BuyRulesSchema, required=False), required=False)
    
    discount_rules = fields.List(fields.Nested(DiscountRulesAppSchema, required=False), required=False)
    
    promotion_group = fields.Str(required=False)
    
    article_quantity = fields.Int(required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    promotion_type = fields.Str(required=False)
    
    promo_id = fields.Str(required=False)
    
    applied_free_articles = fields.List(fields.Nested(AppliedFreeArticlesSchema, required=False), required=False)
    


class PaymentSelectionLock(BaseSchema):
    # Cart swagger.json

    
    enabled = fields.Boolean(required=False)
    
    default_options = fields.Str(required=False)
    
    payment_identifier = fields.Str(required=False)
    


class CartProductIdentifer(BaseSchema):
    # Cart swagger.json

    
    identifier = fields.Str(required=False)
    


class BaseInfo(BaseSchema):
    # Cart swagger.json

    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    


class BasePriceSchema(BaseSchema):
    # Cart swagger.json

    
    currency_code = fields.Str(required=False)
    
    currency_symbol = fields.Str(required=False)
    
    effective = fields.Float(required=False)
    
    marked = fields.Float(required=False)
    


class ArticlePriceInfo(BaseSchema):
    # Cart swagger.json

    
    base = fields.Nested(BasePriceSchema, required=False)
    
    converted = fields.Nested(BasePriceSchema, required=False)
    


class ProductArticle(BaseSchema):
    # Cart swagger.json

    
    parent_item_identifiers = fields.Dict(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    extra_meta = fields.Dict(required=False)
    
    cart_item_meta = fields.Dict(required=False)
    
    identifier = fields.Dict(required=False)
    
    is_gift_visible = fields.Boolean(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    gift_card = fields.Dict(required=False)
    
    size = fields.Str(required=False)
    
    product_group_tags = fields.List(fields.Str(required=False), required=False)
    
    seller = fields.Nested(BaseInfo, required=False)
    
    quantity = fields.Int(required=False)
    
    price = fields.Nested(ArticlePriceInfo, required=False)
    
    type = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    store = fields.Nested(BaseInfo, required=False)
    


class ProductPrice(BaseSchema):
    # Cart swagger.json

    
    currency_code = fields.Str(required=False)
    
    add_on = fields.Float(required=False)
    
    selling = fields.Float(required=False)
    
    currency_symbol = fields.Str(required=False)
    
    effective = fields.Float(required=False)
    
    marked = fields.Float(required=False)
    


class ProductPriceInfo(BaseSchema):
    # Cart swagger.json

    
    base = fields.Nested(ProductPrice, required=False)
    
    converted = fields.Nested(ProductPrice, required=False)
    


class ProductAvailabilitySize(BaseSchema):
    # Cart swagger.json

    
    display = fields.Str(required=False)
    
    is_available = fields.Boolean(required=False)
    
    value = fields.Str(required=False)
    


class ProductAvailability(BaseSchema):
    # Cart swagger.json

    
    out_of_stock = fields.Boolean(required=False)
    
    deliverable = fields.Boolean(required=False)
    
    sizes = fields.List(fields.Str(required=False), required=False)
    
    other_store_quantity = fields.Int(required=False)
    
    is_valid = fields.Boolean(required=False)
    
    available_sizes = fields.List(fields.Nested(ProductAvailabilitySize, required=False), required=False)
    


class ActionQuery(BaseSchema):
    # Cart swagger.json

    
    product_slug = fields.List(fields.Str(required=False), required=False)
    


class ProductAction(BaseSchema):
    # Cart swagger.json

    
    query = fields.Nested(ActionQuery, required=False)
    
    url = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class Tags(BaseSchema):
    # Cart swagger.json

    
    tags = fields.Dict(required=False)
    


class ProductImage(BaseSchema):
    # Cart swagger.json

    
    url = fields.Str(required=False)
    
    secure_url = fields.Str(required=False)
    
    aspect_ratio = fields.Str(required=False)
    


class NetQuantity(BaseSchema):
    # Cart swagger.json

    
    unit = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class CategoryInfo(BaseSchema):
    # Cart swagger.json

    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    


class CartProduct(BaseSchema):
    # Cart swagger.json

    
    action = fields.Nested(ProductAction, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    teaser_tag = fields.Nested(Tags, required=False)
    
    images = fields.List(fields.Nested(ProductImage, required=False), required=False)
    
    net_quantity = fields.Nested(NetQuantity, required=False)
    
    categories = fields.List(fields.Nested(CategoryInfo, required=False), required=False)
    
    brand = fields.Nested(BaseInfo, required=False)
    
    item_code = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    


class CouponDetails(BaseSchema):
    # Cart swagger.json

    
    discount_single_quantity = fields.Float(required=False)
    
    discount_total_quantity = fields.Float(required=False)
    
    code = fields.Str(required=False)
    


class PromoMeta(BaseSchema):
    # Cart swagger.json

    
    message = fields.Str(required=False)
    


class CartProductInfo(BaseSchema):
    # Cart swagger.json

    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    promotions_applied = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    
    is_set = fields.Boolean(required=False)
    
    bulk_offer = fields.Dict(required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    
    coupon_message = fields.Str(required=False)
    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    
    product = fields.Nested(CartProduct, required=False)
    
    custom_order = fields.Dict(required=False)
    
    coupon = fields.Nested(CouponDetails, required=False)
    
    message = fields.Str(required=False)
    
    moq = fields.Dict(required=False)
    
    discount = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    key = fields.Str(required=False)
    
    price = fields.Nested(ProductPriceInfo, required=False)
    


class CartDetailResponse(BaseSchema):
    # Cart swagger.json

    
    id = fields.Str(required=False)
    
    comment = fields.Str(required=False)
    
    breakup_values = fields.Nested(CartBreakupSchema, required=False)
    
    pan_no = fields.Str(required=False)
    
    is_valid = fields.Boolean(required=False)
    
    restrict_checkout = fields.Boolean(required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    buy_now = fields.Boolean(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    gstin = fields.Str(required=False)
    
    currency = fields.Nested(CartCurrencySchema, required=False)
    
    message = fields.Str(required=False)
    
    last_modified = fields.Str(required=False)
    
    delivery_charge_info = fields.Str(required=False)
    
    applied_promo_details = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    coupon_text = fields.Str(required=False)
    
    pan_config = fields.Dict(required=False)
    
    payment_selection_lock = fields.Nested(PaymentSelectionLock, required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    


class AddProductCart(BaseSchema):
    # Cart swagger.json

    
    parent_item_identifiers = fields.List(fields.Dict(required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    extra_meta = fields.Dict(required=False)
    
    item_size = fields.Str(required=False)
    
    item_id = fields.Int(required=False)
    
    article_assignment = fields.Dict(required=False)
    
    display = fields.Str(required=False)
    
    article_id = fields.Str(required=False)
    
    product_group_tags = fields.List(fields.Str(required=False), required=False)
    
    quantity = fields.Int(required=False)
    
    store_id = fields.Int(required=False)
    
    pos = fields.Boolean(required=False)
    
    seller_id = fields.Int(required=False)
    


class AddCartRequest(BaseSchema):
    # Cart swagger.json

    
    new_cart = fields.Boolean(required=False)
    
    items = fields.List(fields.Nested(AddProductCart, required=False), required=False)
    


class AddCartDetailResponse(BaseSchema):
    # Cart swagger.json

    
    message = fields.Str(required=False)
    
    cart = fields.Nested(CartDetailResponse, required=False)
    
    success = fields.Boolean(required=False)
    
    partial = fields.Boolean(required=False)
    


class UpdateProductCart(BaseSchema):
    # Cart swagger.json

    
    parent_item_identifiers = fields.Dict(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    extra_meta = fields.Dict(required=False)
    
    item_size = fields.Str(required=False)
    
    item_id = fields.Int(required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    article_id = fields.Str(required=False)
    
    item_index = fields.Int(required=False)
    
    quantity = fields.Int(required=False)
    


class UpdateCartRequest(BaseSchema):
    # Cart swagger.json

    
    operation = fields.Str(required=False)
    
    items = fields.List(fields.Nested(UpdateProductCart, required=False), required=False)
    


class UpdateCartDetailResponse(BaseSchema):
    # Cart swagger.json

    
    message = fields.Str(required=False)
    
    cart = fields.Nested(CartDetailResponse, required=False)
    
    success = fields.Boolean(required=False)
    


class DeleteCartDetailResponse(BaseSchema):
    # Cart swagger.json

    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class CartItemCountResponse(BaseSchema):
    # Cart swagger.json

    
    user_cart_items_count = fields.Int(required=False)
    


class PageCouponSchema(BaseSchema):
    # Cart swagger.json

    
    total = fields.Int(required=False)
    
    current = fields.Int(required=False)
    
    total_item_count = fields.Int(required=False)
    
    has_next = fields.Boolean(required=False)
    
    has_previous = fields.Boolean(required=False)
    


class Coupon(BaseSchema):
    # Cart swagger.json

    
    description = fields.Str(required=False)
    
    is_applicable = fields.Boolean(required=False)
    
    coupon_value = fields.Float(required=False)
    
    title = fields.Str(required=False)
    
    sub_title = fields.Str(required=False)
    
    is_applied = fields.Boolean(required=False)
    
    coupon_type = fields.Str(required=False)
    
    coupon_code = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    minimum_cart_value = fields.Float(required=False)
    
    expires_on = fields.Str(required=False)
    
    max_discount_value = fields.Float(required=False)
    


class GetCouponResponse(BaseSchema):
    # Cart swagger.json

    
    page = fields.Nested(PageCouponSchema, required=False)
    
    available_coupon_list = fields.List(fields.Nested(Coupon, required=False), required=False)
    


class ApplyCouponRequest(BaseSchema):
    # Cart swagger.json

    
    coupon_code = fields.Str(required=False)
    


class OfferPrice(BaseSchema):
    # Cart swagger.json

    
    currency_code = fields.Str(required=False)
    
    currency_symbol = fields.Str(required=False)
    
    effective = fields.Int(required=False)
    
    marked = fields.Int(required=False)
    
    bulk_effective = fields.Float(required=False)
    


class OfferItemSchema(BaseSchema):
    # Cart swagger.json

    
    auto_applied = fields.Boolean(required=False)
    
    total = fields.Float(required=False)
    
    quantity = fields.Int(required=False)
    
    margin = fields.Int(required=False)
    
    best = fields.Boolean(required=False)
    
    price = fields.Nested(OfferPrice, required=False)
    
    type = fields.Str(required=False)
    


class OfferSellerSchema(BaseSchema):
    # Cart swagger.json

    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    


class BulkPriceOfferSchema(BaseSchema):
    # Cart swagger.json

    
    offers = fields.List(fields.Nested(OfferItemSchema, required=False), required=False)
    
    seller = fields.Nested(OfferSellerSchema, required=False)
    


class BulkPriceResponse(BaseSchema):
    # Cart swagger.json

    
    data = fields.List(fields.Nested(BulkPriceOfferSchema, required=False), required=False)
    


class RewardPointRequestSchema(BaseSchema):
    # Cart swagger.json

    
    points = fields.Boolean(required=False)
    


class GeoLocation(BaseSchema):
    # Cart swagger.json

    
    latitude = fields.Float(required=False)
    
    longitude = fields.Float(required=False)
    


class Address(BaseSchema):
    # Cart swagger.json

    
    id = fields.Str(required=False)
    
    area_code_slug = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    address_type = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    google_map_point = fields.Dict(required=False)
    
    is_active = fields.Boolean(required=False)
    
    is_default_address = fields.Boolean(required=False)
    
    meta = fields.Dict(required=False)
    
    geo_location = fields.Nested(GeoLocation, required=False)
    
    country_iso_code = fields.Str(required=False)
    
    address = fields.Str(required=False)
    
    landmark = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    created_by_user_id = fields.Str(required=False)
    
    country_phone_code = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    country = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    area_code = fields.Str(required=False)
    
    area = fields.Str(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    name = fields.Str(required=False)
    


class GetAddressesResponse(BaseSchema):
    # Cart swagger.json

    
    pii_masking = fields.Boolean(required=False)
    
    address = fields.List(fields.Nested(Address, required=False), required=False)
    


class SaveAddressResponse(BaseSchema):
    # Cart swagger.json

    
    id = fields.Str(required=False)
    
    is_default_address = fields.Boolean(required=False)
    
    success = fields.Boolean(required=False)
    


class UpdateAddressResponse(BaseSchema):
    # Cart swagger.json

    
    is_default_address = fields.Boolean(required=False)
    
    id = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    is_updated = fields.Boolean(required=False)
    


class DeleteAddressResponse(BaseSchema):
    # Cart swagger.json

    
    id = fields.Str(required=False)
    
    is_deleted = fields.Boolean(required=False)
    


class SelectCartAddressRequest(BaseSchema):
    # Cart swagger.json

    
    id = fields.Str(required=False)
    
    cart_id = fields.Str(required=False)
    
    billing_address_id = fields.Str(required=False)
    


class UpdateCartPaymentRequest(BaseSchema):
    # Cart swagger.json

    
    aggregator_name = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
    payment_identifier = fields.Str(required=False)
    
    merchant_code = fields.Str(required=False)
    
    address_id = fields.Str(required=False)
    


class CouponValidity(BaseSchema):
    # Cart swagger.json

    
    valid = fields.Boolean(required=False)
    
    code = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    discount = fields.Float(required=False)
    
    display_message_en = fields.Str(required=False)
    


class PaymentCouponValidateSchema(BaseSchema):
    # Cart swagger.json

    
    message = fields.Str(required=False)
    
    coupon_validity = fields.Nested(CouponValidity, required=False)
    
    success = fields.Boolean(required=False)
    


class ShipmentResponse(BaseSchema):
    # Cart swagger.json

    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    dp_id = fields.Str(required=False)
    
    fulfillment_type = fields.Str(required=False)
    
    order_type = fields.Str(required=False)
    
    fulfillment_id = fields.Int(required=False)
    
    box_type = fields.Str(required=False)
    
    shipments = fields.Int(required=False)
    
    promise = fields.Nested(ShipmentPromise, required=False)
    
    shipment_type = fields.Str(required=False)
    
    dp_options = fields.Dict(required=False)
    


class CartShipmentsResponse(BaseSchema):
    # Cart swagger.json

    
    gstin = fields.Str(required=False)
    
    payment_selection_lock = fields.Nested(PaymentSelectionLock, required=False)
    
    currency = fields.Nested(CartCurrencySchema, required=False)
    
    id = fields.Str(required=False)
    
    comment = fields.Str(required=False)
    
    cart_id = fields.Int(required=False)
    
    breakup_values = fields.Nested(CartBreakupSchema, required=False)
    
    message = fields.Str(required=False)
    
    shipments = fields.List(fields.Nested(ShipmentResponse, required=False), required=False)
    
    is_valid = fields.Boolean(required=False)
    
    uid = fields.Str(required=False)
    
    last_modified = fields.Str(required=False)
    
    restrict_checkout = fields.Boolean(required=False)
    
    delivery_charge_info = fields.Str(required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    coupon_text = fields.Str(required=False)
    
    buy_now = fields.Boolean(required=False)
    
    error = fields.Boolean(required=False)
    
    checkout_mode = fields.Str(required=False)
    


class StaffCheckoutSchema(BaseSchema):
    # Cart swagger.json

    
    first_name = fields.Str(required=False)
    
    user = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    
    employee_code = fields.Str(required=False)
    


class CartCheckoutCustomMetaSchema(BaseSchema):
    # Cart swagger.json

    
    key = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class CartCheckoutDetailRequest(BaseSchema):
    # Cart swagger.json

    
    aggregator = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    payment_auto_confirm = fields.Boolean(required=False)
    
    extra_meta = fields.Dict(required=False)
    
    meta = fields.Dict(required=False)
    
    payment_mode = fields.Str(required=False)
    
    callback_url = fields.Str(required=False)
    
    billing_address = fields.Dict(required=False)
    
    staff = fields.Nested(StaffCheckoutSchema, required=False)
    
    order_type = fields.Str(required=False)
    
    payment_identifier = fields.Str(required=False)
    
    ordering_store = fields.Int(required=False)
    
    delivery_address = fields.Dict(required=False)
    
    payment_params = fields.Dict(required=False)
    
    billing_address_id = fields.Str(required=False)
    
    custom_meta = fields.List(fields.Nested(CartCheckoutCustomMetaSchema, required=False), required=False)
    
    merchant_code = fields.Str(required=False)
    
    address_id = fields.Str(required=False)
    


class CheckCartSchema(BaseSchema):
    # Cart swagger.json

    
    cod_available = fields.Boolean(required=False)
    
    id = fields.Str(required=False)
    
    comment = fields.Str(required=False)
    
    cod_message = fields.Str(required=False)
    
    breakup_values = fields.Nested(CartBreakupSchema, required=False)
    
    store_code = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    delivery_charge_order_value = fields.Int(required=False)
    
    success = fields.Boolean(required=False)
    
    is_valid = fields.Boolean(required=False)
    
    restrict_checkout = fields.Boolean(required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    buy_now = fields.Boolean(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    store_emps = fields.List(fields.Dict(required=False), required=False)
    
    gstin = fields.Str(required=False)
    
    currency = fields.Nested(CartCurrencySchema, required=False)
    
    cart_id = fields.Int(required=False)
    
    delivery_charges = fields.Int(required=False)
    
    error_message = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    cod_charges = fields.Int(required=False)
    
    last_modified = fields.Str(required=False)
    
    delivery_charge_info = fields.Str(required=False)
    
    coupon_text = fields.Str(required=False)
    
    user_type = fields.Str(required=False)
    
    payment_selection_lock = fields.Nested(PaymentSelectionLock, required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    


class CartCheckoutResponseSchema(BaseSchema):
    # Cart swagger.json

    
    payment_confirm_url = fields.Str(required=False)
    
    data = fields.Dict(required=False)
    
    callback_url = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    app_intercept_url = fields.Str(required=False)
    
    cart = fields.Nested(CheckCartSchema, required=False)
    


class GiftDetailSchema(BaseSchema):
    # Cart swagger.json

    
    is_gift_applied = fields.Boolean(required=False)
    
    gift_message = fields.Str(required=False)
    


class ArticleGiftDetailSchema(BaseSchema):
    # Cart swagger.json

    
    article_id = fields.Nested(GiftDetailSchema, required=False)
    


class CartMetaRequest(BaseSchema):
    # Cart swagger.json

    
    gstin = fields.Str(required=False)
    
    comment = fields.Str(required=False)
    
    pick_up_customer_details = fields.Dict(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    gift_details = fields.Nested(ArticleGiftDetailSchema, required=False)
    


class CartMetaResponse(BaseSchema):
    # Cart swagger.json

    
    message = fields.Str(required=False)
    


class CartMetaMissingResponse(BaseSchema):
    # Cart swagger.json

    
    errors = fields.List(fields.Str(required=False), required=False)
    


class GetShareCartLinkRequest(BaseSchema):
    # Cart swagger.json

    
    id = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    


class GetShareCartLinkResponse(BaseSchema):
    # Cart swagger.json

    
    share_url = fields.Str(required=False)
    
    token = fields.Str(required=False)
    


class SharedCartDetails(BaseSchema):
    # Cart swagger.json

    
    source = fields.Dict(required=False)
    
    meta = fields.Dict(required=False)
    
    token = fields.Str(required=False)
    
    user = fields.Dict(required=False)
    
    created_on = fields.Str(required=False)
    


class SharedCart(BaseSchema):
    # Cart swagger.json

    
    id = fields.Str(required=False)
    
    comment = fields.Str(required=False)
    
    breakup_values = fields.Nested(CartBreakupSchema, required=False)
    
    shared_cart_details = fields.Nested(SharedCartDetails, required=False)
    
    is_valid = fields.Boolean(required=False)
    
    restrict_checkout = fields.Boolean(required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    buy_now = fields.Boolean(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    gstin = fields.Str(required=False)
    
    currency = fields.Nested(CartCurrencySchema, required=False)
    
    cart_id = fields.Int(required=False)
    
    message = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    last_modified = fields.Str(required=False)
    
    delivery_charge_info = fields.Str(required=False)
    
    coupon_text = fields.Str(required=False)
    
    payment_selection_lock = fields.Nested(PaymentSelectionLock, required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    


class SharedCartResponse(BaseSchema):
    # Cart swagger.json

    
    cart = fields.Nested(SharedCart, required=False)
    
    error = fields.Str(required=False)
    


class FreeGiftItemsSchema(BaseSchema):
    # Cart swagger.json

    
    item_id = fields.Int(required=False)
    
    item_price_details = fields.Dict(required=False)
    
    item_name = fields.Str(required=False)
    
    item_slug = fields.Str(required=False)
    
    item_images_url = fields.List(fields.Str(required=False), required=False)
    
    item_brand_name = fields.Str(required=False)
    


class PromotionOffer(BaseSchema):
    # Cart swagger.json

    
    description = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    free_gift_items = fields.List(fields.Nested(FreeGiftItemsSchema, required=False), required=False)
    
    offer_text = fields.Str(required=False)
    
    buy_rules = fields.Dict(required=False)
    
    valid_till = fields.Str(required=False)
    
    discount_rules = fields.List(fields.Dict(required=False), required=False)
    
    promotion_group = fields.Str(required=False)
    


class PromotionOffersResponse(BaseSchema):
    # Cart swagger.json

    
    available_promotions = fields.List(fields.Nested(PromotionOffer, required=False), required=False)
    


class OperationErrorResponse(BaseSchema):
    # Cart swagger.json

    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class CurrencyInfoSchema(BaseSchema):
    # Cart swagger.json

    
    symbol = fields.Str(required=False)
    
    code = fields.Str(required=False)
    


class LadderPrice(BaseSchema):
    # Cart swagger.json

    
    currency_code = fields.Str(required=False)
    
    currency_symbol = fields.Str(required=False)
    
    effective = fields.Int(required=False)
    
    marked = fields.Int(required=False)
    
    offer_price = fields.Float(required=False)
    


class LadderOfferItemSchema(BaseSchema):
    # Cart swagger.json

    
    margin = fields.Int(required=False)
    
    min_quantity = fields.Int(required=False)
    
    price = fields.Nested(LadderPrice, required=False)
    
    type = fields.Str(required=False)
    
    max_quantity = fields.Int(required=False)
    


class LadderPriceOffer(BaseSchema):
    # Cart swagger.json

    
    description = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    offer_prices = fields.List(fields.Nested(LadderOfferItemSchema, required=False), required=False)
    
    free_gift_items = fields.List(fields.Nested(FreeGiftItemsSchema, required=False), required=False)
    
    offer_text = fields.Str(required=False)
    
    buy_rules = fields.Dict(required=False)
    
    valid_till = fields.Str(required=False)
    
    discount_rules = fields.List(fields.Dict(required=False), required=False)
    
    promotion_group = fields.Str(required=False)
    
    calculate_on = fields.Str(required=False)
    


class LadderPriceOffers(BaseSchema):
    # Cart swagger.json

    
    currency = fields.Nested(CurrencyInfoSchema, required=False)
    
    available_offers = fields.List(fields.Nested(LadderPriceOffer, required=False), required=False)
    


class PaymentMetaSchema(BaseSchema):
    # Cart swagger.json

    
    merchant_code = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    payment_identifier = fields.Str(required=False)
    
    payment_gateway = fields.Str(required=False)
    


class PaymentMethodSchema(BaseSchema):
    # Cart swagger.json

    
    payment_meta = fields.Nested(PaymentMetaSchema, required=False)
    
    amount = fields.Float(required=False)
    
    payment = fields.Str(required=False)
    
    mode = fields.Str(required=False)
    
    name = fields.Str(required=False)
    


class CartCheckoutDetailV2Request(BaseSchema):
    # Cart swagger.json

    
    id = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
    billing_address = fields.Dict(required=False)
    
    meta = fields.Dict(required=False)
    
    delivery_address = fields.Dict(required=False)
    
    payment_methods = fields.List(fields.Nested(PaymentMethodSchema, required=False), required=False)
    
    cart_id = fields.Str(required=False)
    
    callback_url = fields.Str(required=False)
    
    order_type = fields.Str(required=False)
    
    staff = fields.Nested(StaffCheckoutSchema, required=False)
    
    ordering_store = fields.Int(required=False)
    
    aggregator = fields.Str(required=False)
    
    extra_meta = fields.Dict(required=False)
    
    payment_auto_confirm = fields.Boolean(required=False)
    
    payment_identifier = fields.Str(required=False)
    
    custom_meta = fields.Dict(required=False)
    
    payment_params = fields.Dict(required=False)
    
    billing_address_id = fields.Str(required=False)
    
    merchant_code = fields.Str(required=False)
    
    address_id = fields.Str(required=False)
    


