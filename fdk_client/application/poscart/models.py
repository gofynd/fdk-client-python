"""PosCart Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..ApplicationModel import BaseSchema




class PaymentSelectionLock(BaseSchema):
    pass


class DisplayBreakupSchema(BaseSchema):
    pass


class RawBreakupSchema(BaseSchema):
    pass


class CouponBreakupSchema(BaseSchema):
    pass


class LoyaltyPoints(BaseSchema):
    pass


class CartBreakupSchema(BaseSchema):
    pass


class ProductPrice(BaseSchema):
    pass


class ProductPriceInfo(BaseSchema):
    pass


class FreeGiftItemSchema(BaseSchema):
    pass


class AppliedFreeArticlesSchema(BaseSchema):
    pass


class Ownership(BaseSchema):
    pass


class BuyRulesSchema(BaseSchema):
    pass


class DiscountRulesAppSchema(BaseSchema):
    pass


class AppliedPromotion(BaseSchema):
    pass


class BaseInfo(BaseSchema):
    pass


class BasePriceSchema(BaseSchema):
    pass


class ArticlePriceInfo(BaseSchema):
    pass


class ProductArticle(BaseSchema):
    pass


class PromoMeta(BaseSchema):
    pass


class ProductAvailabilitySize(BaseSchema):
    pass


class ProductAvailability(BaseSchema):
    pass


class CartProductIdentifer(BaseSchema):
    pass


class PromiseTimestamp(BaseSchema):
    pass


class PromiseFormatted(BaseSchema):
    pass


class ShipmentPromise(BaseSchema):
    pass


class CategoryInfo(BaseSchema):
    pass


class ActionQuery(BaseSchema):
    pass


class ProductAction(BaseSchema):
    pass


class NetQuantity(BaseSchema):
    pass


class ProductImage(BaseSchema):
    pass


class CartProduct(BaseSchema):
    pass


class CartProductInfo(BaseSchema):
    pass


class CartCurrencySchema(BaseSchema):
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


class CartItemCountResponse(BaseSchema):
    pass


class Coupon(BaseSchema):
    pass


class PageCouponSchema(BaseSchema):
    pass


class GetCouponResponse(BaseSchema):
    pass


class ApplyCouponRequest(BaseSchema):
    pass


class OfferSellerSchema(BaseSchema):
    pass


class OfferPrice(BaseSchema):
    pass


class OfferItemSchema(BaseSchema):
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


class UpdateCartShipmentItem(BaseSchema):
    pass


class UpdateCartShipmentRequest(BaseSchema):
    pass


class StaffCheckoutSchema(BaseSchema):
    pass


class FilesSchema(BaseSchema):
    pass


class CartCheckoutCustomMetaSchema(BaseSchema):
    pass


class CartPosCheckoutDetailRequest(BaseSchema):
    pass


class CheckCartSchema(BaseSchema):
    pass


class CartCheckoutResponseSchema(BaseSchema):
    pass


class CartMetaRequest(BaseSchema):
    pass


class CartMetaResponse(BaseSchema):
    pass


class CartMetaMissingResponse(BaseSchema):
    pass


class CartDeliveryModesResponse(BaseSchema):
    pass


class PickupStoreDetail(BaseSchema):
    pass


class StoreDetailsResponse(BaseSchema):
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





class PaymentSelectionLock(BaseSchema):
    # PosCart swagger.json

    
    default_options = fields.Str(required=False)
    
    payment_identifier = fields.Str(required=False)
    
    enabled = fields.Boolean(required=False)
    


class DisplayBreakupSchema(BaseSchema):
    # PosCart swagger.json

    
    message = fields.List(fields.Str(required=False), required=False)
    
    currency_code = fields.Str(required=False)
    
    currency_symbol = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
    value = fields.Float(required=False)
    
    display = fields.Str(required=False)
    


class RawBreakupSchema(BaseSchema):
    # PosCart swagger.json

    
    fynd_cash = fields.Float(required=False)
    
    you_saved = fields.Float(required=False)
    
    subtotal = fields.Float(required=False)
    
    discount = fields.Float(required=False)
    
    gst_charges = fields.Float(required=False)
    
    vog = fields.Float(required=False)
    
    delivery_charge = fields.Float(required=False)
    
    mrp_total = fields.Float(required=False)
    
    coupon = fields.Float(required=False)
    
    total = fields.Float(required=False)
    
    cod_charge = fields.Float(required=False)
    
    convenience_fee = fields.Float(required=False)
    


class CouponBreakupSchema(BaseSchema):
    # PosCart swagger.json

    
    sub_title = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    is_applied = fields.Boolean(required=False)
    
    code = fields.Str(required=False)
    
    coupon_type = fields.Str(required=False)
    
    value = fields.Float(required=False)
    
    max_discount_value = fields.Float(required=False)
    
    title = fields.Str(required=False)
    
    minimum_cart_value = fields.Float(required=False)
    
    coupon_value = fields.Float(required=False)
    


class LoyaltyPoints(BaseSchema):
    # PosCart swagger.json

    
    total = fields.Float(required=False)
    
    is_applied = fields.Boolean(required=False)
    
    applicable = fields.Float(required=False)
    
    description = fields.Str(required=False)
    


class CartBreakupSchema(BaseSchema):
    # PosCart swagger.json

    
    display = fields.List(fields.Nested(DisplayBreakupSchema, required=False), required=False)
    
    raw = fields.Nested(RawBreakupSchema, required=False)
    
    coupon = fields.Nested(CouponBreakupSchema, required=False)
    
    loyalty_points = fields.Nested(LoyaltyPoints, required=False)
    


class ProductPrice(BaseSchema):
    # PosCart swagger.json

    
    effective = fields.Float(required=False)
    
    marked = fields.Float(required=False)
    
    selling = fields.Float(required=False)
    
    currency_code = fields.Str(required=False)
    
    add_on = fields.Float(required=False)
    
    currency_symbol = fields.Str(required=False)
    


class ProductPriceInfo(BaseSchema):
    # PosCart swagger.json

    
    converted = fields.Nested(ProductPrice, required=False)
    
    base = fields.Nested(ProductPrice, required=False)
    


class FreeGiftItemSchema(BaseSchema):
    # PosCart swagger.json

    
    item_images_url = fields.List(fields.Str(required=False), required=False)
    
    item_price_details = fields.Dict(required=False)
    
    item_id = fields.Int(required=False)
    
    item_slug = fields.Str(required=False)
    
    item_brand_name = fields.Str(required=False)
    
    item_name = fields.Str(required=False)
    


class AppliedFreeArticlesSchema(BaseSchema):
    # PosCart swagger.json

    
    parent_item_identifier = fields.Str(required=False)
    
    article_id = fields.Str(required=False)
    
    free_gift_item_details = fields.Nested(FreeGiftItemSchema, required=False)
    
    quantity = fields.Int(required=False)
    


class Ownership(BaseSchema):
    # PosCart swagger.json

    
    payable_by = fields.Str(required=False)
    
    payable_category = fields.Str(required=False)
    


class BuyRulesSchema(BaseSchema):
    # PosCart swagger.json

    
    cart_conditions = fields.Dict(required=False)
    
    item_criteria = fields.Dict(required=False)
    


class DiscountRulesAppSchema(BaseSchema):
    # PosCart swagger.json

    
    matched_buy_rules = fields.List(fields.Str(required=False), required=False)
    
    offer = fields.Dict(required=False)
    
    item_criteria = fields.Dict(required=False)
    
    raw_offer = fields.Dict(required=False)
    


class AppliedPromotion(BaseSchema):
    # PosCart swagger.json

    
    applied_free_articles = fields.List(fields.Nested(AppliedFreeArticlesSchema, required=False), required=False)
    
    ownership = fields.Nested(Ownership, required=False)
    
    promotion_group = fields.Str(required=False)
    
    offer_text = fields.Str(required=False)
    
    promotion_type = fields.Str(required=False)
    
    promo_id = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
    buy_rules = fields.List(fields.Nested(BuyRulesSchema, required=False), required=False)
    
    promotion_name = fields.Str(required=False)
    
    article_quantity = fields.Int(required=False)
    
    discount_rules = fields.List(fields.Nested(DiscountRulesAppSchema, required=False), required=False)
    
    mrp_promotion = fields.Boolean(required=False)
    


class BaseInfo(BaseSchema):
    # PosCart swagger.json

    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    


class BasePriceSchema(BaseSchema):
    # PosCart swagger.json

    
    effective = fields.Float(required=False)
    
    marked = fields.Float(required=False)
    
    currency_code = fields.Str(required=False)
    
    currency_symbol = fields.Str(required=False)
    


class ArticlePriceInfo(BaseSchema):
    # PosCart swagger.json

    
    converted = fields.Nested(BasePriceSchema, required=False)
    
    base = fields.Nested(BasePriceSchema, required=False)
    


class ProductArticle(BaseSchema):
    # PosCart swagger.json

    
    extra_meta = fields.Dict(required=False)
    
    type = fields.Str(required=False)
    
    seller = fields.Nested(BaseInfo, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    product_group_tags = fields.List(fields.Str(required=False), required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    
    uid = fields.Str(required=False)
    
    store = fields.Nested(BaseInfo, required=False)
    
    size = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    price = fields.Nested(ArticlePriceInfo, required=False)
    


class PromoMeta(BaseSchema):
    # PosCart swagger.json

    
    message = fields.Str(required=False)
    


class ProductAvailabilitySize(BaseSchema):
    # PosCart swagger.json

    
    is_available = fields.Boolean(required=False)
    
    display = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class ProductAvailability(BaseSchema):
    # PosCart swagger.json

    
    deliverable = fields.Boolean(required=False)
    
    sizes = fields.List(fields.Str(required=False), required=False)
    
    out_of_stock = fields.Boolean(required=False)
    
    other_store_quantity = fields.Int(required=False)
    
    is_valid = fields.Boolean(required=False)
    
    available_sizes = fields.List(fields.Nested(ProductAvailabilitySize, required=False), required=False)
    


class CartProductIdentifer(BaseSchema):
    # PosCart swagger.json

    
    identifier = fields.Str(required=False)
    


class PromiseTimestamp(BaseSchema):
    # PosCart swagger.json

    
    min = fields.Float(required=False)
    
    max = fields.Float(required=False)
    


class PromiseFormatted(BaseSchema):
    # PosCart swagger.json

    
    min = fields.Str(required=False)
    
    max = fields.Str(required=False)
    


class ShipmentPromise(BaseSchema):
    # PosCart swagger.json

    
    timestamp = fields.Nested(PromiseTimestamp, required=False)
    
    formatted = fields.Nested(PromiseFormatted, required=False)
    


class CategoryInfo(BaseSchema):
    # PosCart swagger.json

    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    


class ActionQuery(BaseSchema):
    # PosCart swagger.json

    
    product_slug = fields.List(fields.Str(required=False), required=False)
    


class ProductAction(BaseSchema):
    # PosCart swagger.json

    
    type = fields.Str(required=False)
    
    query = fields.Nested(ActionQuery, required=False)
    
    url = fields.Str(required=False)
    


class NetQuantity(BaseSchema):
    # PosCart swagger.json

    
    unit = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class ProductImage(BaseSchema):
    # PosCart swagger.json

    
    aspect_ratio = fields.Str(required=False)
    
    secure_url = fields.Str(required=False)
    
    url = fields.Str(required=False)
    


class CartProduct(BaseSchema):
    # PosCart swagger.json

    
    brand = fields.Nested(BaseInfo, required=False)
    
    item_code = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    categories = fields.List(fields.Nested(CategoryInfo, required=False), required=False)
    
    type = fields.Str(required=False)
    
    action = fields.Nested(ProductAction, required=False)
    
    uid = fields.Int(required=False)
    
    net_quantity = fields.Nested(NetQuantity, required=False)
    
    images = fields.List(fields.Nested(ProductImage, required=False), required=False)
    
    slug = fields.Str(required=False)
    


class CartProductInfo(BaseSchema):
    # PosCart swagger.json

    
    bulk_offer = fields.Dict(required=False)
    
    message = fields.Str(required=False)
    
    moq = fields.Dict(required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    custom_order = fields.Dict(required=False)
    
    coupon_message = fields.Str(required=False)
    
    promotions_applied = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    product = fields.Nested(CartProduct, required=False)
    
    discount = fields.Str(required=False)
    
    is_set = fields.Boolean(required=False)
    
    key = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    


class CartCurrencySchema(BaseSchema):
    # PosCart swagger.json

    
    symbol = fields.Str(required=False)
    
    code = fields.Str(required=False)
    


class CartDetailResponse(BaseSchema):
    # PosCart swagger.json

    
    comment = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    coupon_text = fields.Str(required=False)
    
    delivery_charge_info = fields.Str(required=False)
    
    payment_selection_lock = fields.Nested(PaymentSelectionLock, required=False)
    
    breakup_values = fields.Nested(CartBreakupSchema, required=False)
    
    id = fields.Str(required=False)
    
    is_valid = fields.Boolean(required=False)
    
    buy_now = fields.Boolean(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    pan_config = fields.Dict(required=False)
    
    gstin = fields.Str(required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    currency = fields.Nested(CartCurrencySchema, required=False)
    
    last_modified = fields.Str(required=False)
    
    pan_no = fields.Str(required=False)
    
    applied_promo_details = fields.List(fields.Nested(AppliedPromotion, required=False), required=False)
    
    restrict_checkout = fields.Boolean(required=False)
    


class AddProductCart(BaseSchema):
    # PosCart swagger.json

    
    item_size = fields.Str(required=False)
    
    seller_id = fields.Int(required=False)
    
    extra_meta = fields.Dict(required=False)
    
    item_id = fields.Int(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    product_group_tags = fields.List(fields.Str(required=False), required=False)
    
    parent_item_identifiers = fields.List(fields.Dict(required=False), required=False)
    
    article_id = fields.Str(required=False)
    
    store_id = fields.Int(required=False)
    
    quantity = fields.Int(required=False)
    
    article_assignment = fields.Dict(required=False)
    
    display = fields.Str(required=False)
    
    pos = fields.Boolean(required=False)
    


class AddCartRequest(BaseSchema):
    # PosCart swagger.json

    
    new_cart = fields.Boolean(required=False)
    
    items = fields.List(fields.Nested(AddProductCart, required=False), required=False)
    


class AddCartDetailResponse(BaseSchema):
    # PosCart swagger.json

    
    cart = fields.Nested(CartDetailResponse, required=False)
    
    message = fields.Str(required=False)
    
    partial = fields.Boolean(required=False)
    
    success = fields.Boolean(required=False)
    


class UpdateProductCart(BaseSchema):
    # PosCart swagger.json

    
    item_size = fields.Str(required=False)
    
    extra_meta = fields.Dict(required=False)
    
    item_id = fields.Int(required=False)
    
    item_index = fields.Int(required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    article_id = fields.Str(required=False)
    
    parent_item_identifiers = fields.Dict(required=False)
    
    quantity = fields.Int(required=False)
    


class UpdateCartRequest(BaseSchema):
    # PosCart swagger.json

    
    operation = fields.Str(required=False)
    
    items = fields.List(fields.Nested(UpdateProductCart, required=False), required=False)
    


class UpdateCartDetailResponse(BaseSchema):
    # PosCart swagger.json

    
    cart = fields.Nested(CartDetailResponse, required=False)
    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    


class CartItemCountResponse(BaseSchema):
    # PosCart swagger.json

    
    user_cart_items_count = fields.Int(required=False)
    


class Coupon(BaseSchema):
    # PosCart swagger.json

    
    expires_on = fields.Str(required=False)
    
    sub_title = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    is_applicable = fields.Boolean(required=False)
    
    is_applied = fields.Boolean(required=False)
    
    coupon_type = fields.Str(required=False)
    
    coupon_code = fields.Str(required=False)
    
    max_discount_value = fields.Float(required=False)
    
    title = fields.Str(required=False)
    
    minimum_cart_value = fields.Float(required=False)
    
    coupon_value = fields.Float(required=False)
    


class PageCouponSchema(BaseSchema):
    # PosCart swagger.json

    
    total_item_count = fields.Int(required=False)
    
    current = fields.Int(required=False)
    
    has_next = fields.Boolean(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    total = fields.Int(required=False)
    


class GetCouponResponse(BaseSchema):
    # PosCart swagger.json

    
    available_coupon_list = fields.List(fields.Nested(Coupon, required=False), required=False)
    
    page = fields.Nested(PageCouponSchema, required=False)
    


class ApplyCouponRequest(BaseSchema):
    # PosCart swagger.json

    
    coupon_code = fields.Str(required=False)
    


class OfferSellerSchema(BaseSchema):
    # PosCart swagger.json

    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    


class OfferPrice(BaseSchema):
    # PosCart swagger.json

    
    effective = fields.Int(required=False)
    
    marked = fields.Int(required=False)
    
    currency_code = fields.Str(required=False)
    
    bulk_effective = fields.Float(required=False)
    
    currency_symbol = fields.Str(required=False)
    


class OfferItemSchema(BaseSchema):
    # PosCart swagger.json

    
    margin = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    best = fields.Boolean(required=False)
    
    quantity = fields.Int(required=False)
    
    total = fields.Float(required=False)
    
    price = fields.Nested(OfferPrice, required=False)
    
    auto_applied = fields.Boolean(required=False)
    


class BulkPriceOfferSchema(BaseSchema):
    # PosCart swagger.json

    
    seller = fields.Nested(OfferSellerSchema, required=False)
    
    offers = fields.List(fields.Nested(OfferItemSchema, required=False), required=False)
    


class BulkPriceResponse(BaseSchema):
    # PosCart swagger.json

    
    data = fields.List(fields.Nested(BulkPriceOfferSchema, required=False), required=False)
    


class RewardPointRequestSchema(BaseSchema):
    # PosCart swagger.json

    
    points = fields.Boolean(required=False)
    


class GeoLocation(BaseSchema):
    # PosCart swagger.json

    
    latitude = fields.Float(required=False)
    
    longitude = fields.Float(required=False)
    


class Address(BaseSchema):
    # PosCart swagger.json

    
    country_phone_code = fields.Str(required=False)
    
    area_code = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    area = fields.Str(required=False)
    
    address_type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    landmark = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
    country_iso_code = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    google_map_point = fields.Dict(required=False)
    
    country_code = fields.Str(required=False)
    
    geo_location = fields.Nested(GeoLocation, required=False)
    
    checkout_mode = fields.Str(required=False)
    
    area_code_slug = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    is_default_address = fields.Boolean(required=False)
    
    created_by_user_id = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    address = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    


class GetAddressesResponse(BaseSchema):
    # PosCart swagger.json

    
    pii_masking = fields.Boolean(required=False)
    
    address = fields.List(fields.Nested(Address, required=False), required=False)
    


class SaveAddressResponse(BaseSchema):
    # PosCart swagger.json

    
    id = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    is_default_address = fields.Boolean(required=False)
    


class UpdateAddressResponse(BaseSchema):
    # PosCart swagger.json

    
    id = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    is_default_address = fields.Boolean(required=False)
    
    is_updated = fields.Boolean(required=False)
    


class DeleteAddressResponse(BaseSchema):
    # PosCart swagger.json

    
    id = fields.Str(required=False)
    
    is_deleted = fields.Boolean(required=False)
    


class SelectCartAddressRequest(BaseSchema):
    # PosCart swagger.json

    
    billing_address_id = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    cart_id = fields.Str(required=False)
    


class UpdateCartPaymentRequest(BaseSchema):
    # PosCart swagger.json

    
    aggregator_name = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    merchant_code = fields.Str(required=False)
    
    payment_identifier = fields.Str(required=False)
    
    address_id = fields.Str(required=False)
    


class CouponValidity(BaseSchema):
    # PosCart swagger.json

    
    discount = fields.Float(required=False)
    
    display_message_en = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    valid = fields.Boolean(required=False)
    
    title = fields.Str(required=False)
    


class PaymentCouponValidateSchema(BaseSchema):
    # PosCart swagger.json

    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    coupon_validity = fields.Nested(CouponValidity, required=False)
    


class ShipmentResponse(BaseSchema):
    # PosCart swagger.json

    
    dp_options = fields.Dict(required=False)
    
    box_type = fields.Str(required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    fulfillment_type = fields.Str(required=False)
    
    dp_id = fields.Str(required=False)
    
    shipment_type = fields.Str(required=False)
    
    fulfillment_id = fields.Int(required=False)
    
    shipments = fields.Int(required=False)
    
    order_type = fields.Str(required=False)
    
    promise = fields.Nested(ShipmentPromise, required=False)
    


class CartShipmentsResponse(BaseSchema):
    # PosCart swagger.json

    
    comment = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    coupon_text = fields.Str(required=False)
    
    restrict_checkout = fields.Boolean(required=False)
    
    delivery_charge_info = fields.Str(required=False)
    
    shipments = fields.List(fields.Nested(ShipmentResponse, required=False), required=False)
    
    payment_selection_lock = fields.Nested(PaymentSelectionLock, required=False)
    
    gstin = fields.Str(required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    breakup_values = fields.Nested(CartBreakupSchema, required=False)
    
    currency = fields.Nested(CartCurrencySchema, required=False)
    
    last_modified = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    cart_id = fields.Int(required=False)
    
    error = fields.Boolean(required=False)
    
    uid = fields.Str(required=False)
    
    is_valid = fields.Boolean(required=False)
    
    buy_now = fields.Boolean(required=False)
    
    checkout_mode = fields.Str(required=False)
    


class UpdateCartShipmentItem(BaseSchema):
    # PosCart swagger.json

    
    shipment_type = fields.Str(required=False)
    
    article_uid = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    


class UpdateCartShipmentRequest(BaseSchema):
    # PosCart swagger.json

    
    shipments = fields.List(fields.Nested(UpdateCartShipmentItem, required=False), required=False)
    


class StaffCheckoutSchema(BaseSchema):
    # PosCart swagger.json

    
    _id = fields.Str(required=False)
    
    first_name = fields.Str(required=False)
    
    employee_code = fields.Str(required=False)
    
    user = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    


class FilesSchema(BaseSchema):
    # PosCart swagger.json

    
    key = fields.Str(required=False)
    
    values = fields.List(fields.Str(required=False), required=False)
    


class CartCheckoutCustomMetaSchema(BaseSchema):
    # PosCart swagger.json

    
    key = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class CartPosCheckoutDetailRequest(BaseSchema):
    # PosCart swagger.json

    
    billing_address = fields.Dict(required=False)
    
    payment_mode = fields.Str(required=False)
    
    callback_url = fields.Str(required=False)
    
    order_type = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    staff = fields.Nested(StaffCheckoutSchema, required=False)
    
    extra_meta = fields.Dict(required=False)
    
    files = fields.List(fields.Nested(FilesSchema, required=False), required=False)
    
    ordering_store = fields.Int(required=False)
    
    payment_params = fields.Dict(required=False)
    
    payment_identifier = fields.Str(required=False)
    
    custom_meta = fields.List(fields.Nested(CartCheckoutCustomMetaSchema, required=False), required=False)
    
    address_id = fields.Str(required=False)
    
    billing_address_id = fields.Str(required=False)
    
    aggregator = fields.Str(required=False)
    
    merchant_code = fields.Str(required=False)
    
    delivery_address = fields.Dict(required=False)
    
    pick_at_store_uid = fields.Int(required=False)
    
    pos = fields.Boolean(required=False)
    
    payment_auto_confirm = fields.Boolean(required=False)
    


class CheckCartSchema(BaseSchema):
    # PosCart swagger.json

    
    order_id = fields.Str(required=False)
    
    comment = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    coupon_text = fields.Str(required=False)
    
    delivery_charge_info = fields.Str(required=False)
    
    payment_selection_lock = fields.Nested(PaymentSelectionLock, required=False)
    
    breakup_values = fields.Nested(CartBreakupSchema, required=False)
    
    store_code = fields.Str(required=False)
    
    delivery_charges = fields.Int(required=False)
    
    error_message = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    is_valid = fields.Boolean(required=False)
    
    buy_now = fields.Boolean(required=False)
    
    delivery_charge_order_value = fields.Int(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    store_emps = fields.List(fields.Dict(required=False), required=False)
    
    cod_charges = fields.Int(required=False)
    
    gstin = fields.Str(required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    currency = fields.Nested(CartCurrencySchema, required=False)
    
    last_modified = fields.Str(required=False)
    
    cod_message = fields.Str(required=False)
    
    cart_id = fields.Int(required=False)
    
    user_type = fields.Str(required=False)
    
    cod_available = fields.Boolean(required=False)
    
    uid = fields.Str(required=False)
    
    restrict_checkout = fields.Boolean(required=False)
    


class CartCheckoutResponseSchema(BaseSchema):
    # PosCart swagger.json

    
    order_id = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    callback_url = fields.Str(required=False)
    
    payment_confirm_url = fields.Str(required=False)
    
    data = fields.Dict(required=False)
    
    app_intercept_url = fields.Str(required=False)
    
    cart = fields.Nested(CheckCartSchema, required=False)
    
    success = fields.Boolean(required=False)
    


class CartMetaRequest(BaseSchema):
    # PosCart swagger.json

    
    pick_up_customer_details = fields.Dict(required=False)
    
    comment = fields.Str(required=False)
    
    gstin = fields.Str(required=False)
    
    checkout_mode = fields.Str(required=False)
    


class CartMetaResponse(BaseSchema):
    # PosCart swagger.json

    
    message = fields.Str(required=False)
    


class CartMetaMissingResponse(BaseSchema):
    # PosCart swagger.json

    
    errors = fields.List(fields.Str(required=False), required=False)
    


class CartDeliveryModesResponse(BaseSchema):
    # PosCart swagger.json

    
    pickup_stores = fields.List(fields.Int(required=False), required=False)
    
    available_modes = fields.List(fields.Str(required=False), required=False)
    


class PickupStoreDetail(BaseSchema):
    # PosCart swagger.json

    
    country = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    address = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    landmark = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    store_code = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    state = fields.Str(required=False)
    
    area_code = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    area = fields.Str(required=False)
    
    address_type = fields.Str(required=False)
    
    area_code_slug = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    
    pincode = fields.Int(required=False)
    


class StoreDetailsResponse(BaseSchema):
    # PosCart swagger.json

    
    items = fields.List(fields.Nested(PickupStoreDetail, required=False), required=False)
    


class GetShareCartLinkRequest(BaseSchema):
    # PosCart swagger.json

    
    id = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    


class GetShareCartLinkResponse(BaseSchema):
    # PosCart swagger.json

    
    share_url = fields.Str(required=False)
    
    token = fields.Str(required=False)
    


class SharedCartDetails(BaseSchema):
    # PosCart swagger.json

    
    source = fields.Dict(required=False)
    
    meta = fields.Dict(required=False)
    
    token = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    user = fields.Dict(required=False)
    


class SharedCart(BaseSchema):
    # PosCart swagger.json

    
    comment = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    coupon_text = fields.Str(required=False)
    
    delivery_charge_info = fields.Str(required=False)
    
    payment_selection_lock = fields.Nested(PaymentSelectionLock, required=False)
    
    shared_cart_details = fields.Nested(SharedCartDetails, required=False)
    
    breakup_values = fields.Nested(CartBreakupSchema, required=False)
    
    id = fields.Str(required=False)
    
    is_valid = fields.Boolean(required=False)
    
    buy_now = fields.Boolean(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    
    gstin = fields.Str(required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    currency = fields.Nested(CartCurrencySchema, required=False)
    
    last_modified = fields.Str(required=False)
    
    cart_id = fields.Int(required=False)
    
    uid = fields.Str(required=False)
    
    restrict_checkout = fields.Boolean(required=False)
    


class SharedCartResponse(BaseSchema):
    # PosCart swagger.json

    
    cart = fields.Nested(SharedCart, required=False)
    
    error = fields.Str(required=False)
    


