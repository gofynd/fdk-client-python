"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



class GetActivityStatus(BaseSchema):
    pass


class ActivityHistory(BaseSchema):
    pass


class CanBreakRequestBody(BaseSchema):
    pass


class CanBreakResponse(BaseSchema):
    pass


class FailedOrders(BaseSchema):
    pass


class FailOrder(BaseSchema):
    pass


class MarketplaceOrder(BaseSchema):
    pass


class TotalDiscountsSet(BaseSchema):
    pass


class PresentmentMoney(BaseSchema):
    pass


class ShopMoney(BaseSchema):
    pass


class TotalPriceSet(BaseSchema):
    pass


class TotalPriceSetShopMoney(BaseSchema):
    pass


class TotalPriceSetPresentmentMoney(BaseSchema):
    pass


class TotalTaxSet(BaseSchema):
    pass


class TotalTaxSetShopMoney(BaseSchema):
    pass


class TotalTaxSetPresentmentMoney(BaseSchema):
    pass


class SubtotalPriceSet(BaseSchema):
    pass


class SubtotalPriceSetShopMoney(BaseSchema):
    pass


class SubtotalPriceSetPresentmentMoney(BaseSchema):
    pass


class LineItems(BaseSchema):
    pass


class LineItemsArticle(BaseSchema):
    pass


class Quantities(BaseSchema):
    pass


class NotAvailable(BaseSchema):
    pass


class Sellable(BaseSchema):
    pass


class OrderCommitted(BaseSchema):
    pass


class Damaged(BaseSchema):
    pass


class Manufacturer(BaseSchema):
    pass


class ArticlePrice(BaseSchema):
    pass


class Company(BaseSchema):
    pass


class FailOrderDateMeta(BaseSchema):
    pass


class MarketplaceIdentifiers(BaseSchema):
    pass


class TatacliqLuxury(BaseSchema):
    pass


class Dimension(BaseSchema):
    pass


class Weight(BaseSchema):
    pass


class Store(BaseSchema):
    pass


class ArticleMeta(BaseSchema):
    pass


class ArticleBrand(BaseSchema):
    pass


class LineItemsArticleIdentifier(BaseSchema):
    pass


class PriceSet(BaseSchema):
    pass


class PriceSetShopMoney(BaseSchema):
    pass


class PriceSetPresentmentMoney(BaseSchema):
    pass


class TaxLines(BaseSchema):
    pass


class TaxLinesPriceSet(BaseSchema):
    pass


class TaxLinesPriceSetShopMoney(BaseSchema):
    pass


class TaxLinesPriceSetPresentmentMoney(BaseSchema):
    pass


class TotalDiscountSet(BaseSchema):
    pass


class TotalDiscountSetPresentmentMoney(BaseSchema):
    pass


class TotalDiscountSetShopMoney(BaseSchema):
    pass


class BillingAddress(BaseSchema):
    pass


class TotalShippingPriceSet(BaseSchema):
    pass


class TotalShippingPriceSetShopMoney(BaseSchema):
    pass


class TotalShippingPriceSetPresentmentMoney(BaseSchema):
    pass


class Customer(BaseSchema):
    pass


class DefaultAddress(BaseSchema):
    pass


class TotalLineItemsPriceSet(BaseSchema):
    pass


class TotalLineItemsPriceSetShopMoney(BaseSchema):
    pass


class TotalLineItemsPriceSetPresentmentMoney(BaseSchema):
    pass


class OrderShippingAddress(BaseSchema):
    pass


class OrderListing(BaseSchema):
    pass


class OrderItems(BaseSchema):
    pass


class PlatformOrderUserInfo(BaseSchema):
    pass


class PlatformDeliveryAddress(BaseSchema):
    pass


class Channel(BaseSchema):
    pass


class PlatformApplication(BaseSchema):
    pass


class PlatformShipment(BaseSchema):
    pass


class PlatformShipmentStatus(BaseSchema):
    pass


class Bags(BaseSchema):
    pass


class BagItem(BaseSchema):
    pass


class BagItemAttributes(BaseSchema):
    pass


class ShipmentPrices(BaseSchema):
    pass


class Payments(BaseSchema):
    pass


class Filters(BaseSchema):
    pass


class Stage(BaseSchema):
    pass


class StagesFilters(BaseSchema):
    pass


class Options(BaseSchema):
    pass


class PlatformOrderPage(BaseSchema):
    pass


class AppliedFilters(BaseSchema):
    pass


class OrderDetails(BaseSchema):
    pass


class OrderDetailsItem(BaseSchema):
    pass


class PlatformBreakupValues(BaseSchema):
    pass


class ArticleAssignment(BaseSchema):
    pass


class PlatformShipmentDetails(BaseSchema):
    pass


class PlatformShipmentDetailsStatus(BaseSchema):
    pass


class BagsDetails(BaseSchema):
    pass


class BagFinancialBreakup(BaseSchema):
    pass


class Identifiers(BaseSchema):
    pass


class BagCurrStatus(BaseSchema):
    pass


class BagArticle(BaseSchema):
    pass


class ArticleIdentifiers(BaseSchema):
    pass


class Set(BaseSchema):
    pass


class SetSizeDistribution(BaseSchema):
    pass


class Sizes(BaseSchema):
    pass


class BagArticleReturnConfig(BaseSchema):
    pass


class GstDetails(BaseSchema):
    pass


class BagBreakupValues(BaseSchema):
    pass


class BagCurrentStatus(BaseSchema):
    pass


class BagStateMapper(BaseSchema):
    pass


class BagStatus(BaseSchema):
    pass


class BagStatusBagStateMapper(BaseSchema):
    pass


class BagPrices(BaseSchema):
    pass


class ShipmentBreakupValues(BaseSchema):
    pass


class DpDetails(BaseSchema):
    pass


class ShipmentInvoice(BaseSchema):
    pass


class RtoAddress(BaseSchema):
    pass


class StoreAddressJson(BaseSchema):
    pass


class PlatformFulfillingStore(BaseSchema):
    pass


class FulfillingStoreMeta(BaseSchema):
    pass


class AdditionalContactDetails(BaseSchema):
    pass


class Documents(BaseSchema):
    pass


class Gst(BaseSchema):
    pass


class ProductReturnConfig(BaseSchema):
    pass


class Timing(BaseSchema):
    pass


class Opening(BaseSchema):
    pass


class Closing(BaseSchema):
    pass


class FulfillingStoreStoreAddressJson(BaseSchema):
    pass


class ShipmentGst(BaseSchema):
    pass


class PlatformShipmentDetailsBrand(BaseSchema):
    pass


class Promise(BaseSchema):
    pass


class Timestamp(BaseSchema):
    pass


class ShipmentTrackingDetails(BaseSchema):
    pass


class ItemsPayments(BaseSchema):
    pass


class PlatformOrderDetailsPage(BaseSchema):
    pass


class ShipmentDates(BaseSchema):
    pass


class OrderLanesCount(BaseSchema):
    pass


class StageItem(BaseSchema):
    pass


class UpdateOrderReprocessResponse(BaseSchema):
    pass


class PlatformOrderTrack(BaseSchema):
    pass


class OrderPicklistListing(BaseSchema):
    pass


class Stages(BaseSchema):
    pass


class ItemTotal(BaseSchema):
    pass


class GetPingResponse(BaseSchema):
    pass


class GetShipmentAddressResponse(BaseSchema):
    pass


class DataShipmentAddress(BaseSchema):
    pass


class UpdateShipmentAddressRequest(BaseSchema):
    pass


class UpdateShipmentAddressResponse(BaseSchema):
    pass


class ShipmentTrackResponse(BaseSchema):
    pass


class ShipmentTrackResponseBagListItem(BaseSchema):
    pass


class ShipmentTrackResponseBagListItemBreakValues(BaseSchema):
    pass


class ShipmentTrackResponseBagListItemStatuses(BaseSchema):
    pass


class ShipmentTrackResponseBagListItemStatusesProgress(BaseSchema):
    pass


class ShipmentTrackResponseBagListItemStatusesTrack(BaseSchema):
    pass


class ShipmentTrackResponseBagListItemDpDetails(BaseSchema):
    pass


class ShipmentTrackResponseBagListItemsProductImage(BaseSchema):
    pass


class UpdateShipmentStatusResponse(BaseSchema):
    pass


class UpdateShipmentStatusBody(BaseSchema):
    pass


class ShipmentReasonsResponse(BaseSchema):
    pass


class ShipmentResponseReasons(BaseSchema):
    pass


class PlatformShipmentTrack(BaseSchema):
    pass


class Results(BaseSchema):
    pass


class ShipmentUpdateRequest(BaseSchema):
    pass


class ShipmentUpdateResponse(BaseSchema):
    pass


class UpdateProcessShipmenstRequestBody(BaseSchema):
    pass


class UpdateProcessShipmenstRequestResponse(BaseSchema):
    pass


class GetVoiceCallbackResponse(BaseSchema):
    pass


class GetClickToCallResponse(BaseSchema):
    pass


class ApefaceApiError(BaseSchema):
    pass



class GetActivityStatus(BaseSchema):
    # Order swagger.json

    
    activity_history = fields.Nested(ActivityHistory, required=False)
    


class ActivityHistory(BaseSchema):
    # Order swagger.json

    
    createdat = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    user = fields.Str(required=False)
    


class CanBreakRequestBody(BaseSchema):
    # Order swagger.json

    
    shipment_ids = fields.List(fields.Str(required=False), required=False)
    


class CanBreakResponse(BaseSchema):
    # Order swagger.json

    
    status = fields.Boolean(required=False)
    
    valid_actions = fields.Dict(required=False)
    


class FailedOrders(BaseSchema):
    # Order swagger.json

    
    orders = fields.Nested(FailOrder, required=False)
    


class FailOrder(BaseSchema):
    # Order swagger.json

    
    updated_at = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    reason = fields.Str(required=False)
    
    marketplace_order = fields.Nested(MarketplaceOrder, required=False)
    
    marketplace_order_id = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    app_id = fields.Str(required=False)
    
    marketplace = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    


class MarketplaceOrder(BaseSchema):
    # Order swagger.json

    
    order_status_url = fields.Str(required=False)
    
    admin_graphql_api_id = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    test = fields.Boolean(required=False)
    
    note = fields.Str(required=False)
    
    total_price = fields.Str(required=False)
    
    app_id = fields.Int(required=False)
    
    total_discounts_set = fields.Nested(TotalDiscountsSet, required=False)
    
    total_price_set = fields.Nested(TotalPriceSet, required=False)
    
    total_tax_set = fields.Nested(TotalTaxSet, required=False)
    
    gateway = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    subtotal_price_set = fields.Nested(SubtotalPriceSet, required=False)
    
    number = fields.Int(required=False)
    
    buyer_accepts_marketing = fields.Boolean(required=False)
    
    contact_email = fields.Str(required=False)
    
    token = fields.Str(required=False)
    
    source_name = fields.Str(required=False)
    
    payment_gateway_names = fields.List(fields.Raw(required=False), required=False)
    
    presentment_currency = fields.Str(required=False)
    
    subtotal_price = fields.Str(required=False)
    
    processed_at = fields.Str(required=False)
    
    order_number = fields.Int(required=False)
    
    total_tip_received = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    confirmed = fields.Boolean(required=False)
    
    currency = fields.Str(required=False)
    
    total_line_items_price = fields.Str(required=False)
    
    line_items = fields.Nested(LineItems, required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    total_weight = fields.Int(required=False)
    
    billing_address = fields.Nested(BillingAddress, required=False)
    
    total_shipping_price_set = fields.Nested(TotalShippingPriceSet, required=False)
    
    customer = fields.Nested(Customer, required=False)
    
    total_discounts = fields.Str(required=False)
    
    total_line_items_price_set = fields.Nested(TotalLineItemsPriceSet, required=False)
    
    tags = fields.Str(required=False)
    
    total_price_usd = fields.Str(required=False)
    
    user_id = fields.Int(required=False)
    
    total_tax = fields.Str(required=False)
    
    processing_method = fields.Str(required=False)
    
    shipping_address = fields.Nested(OrderShippingAddress, required=False)
    
    taxes_included = fields.Boolean(required=False)
    
    financial_status = fields.Str(required=False)
    


class TotalDiscountsSet(BaseSchema):
    # Order swagger.json

    
    presentment_money = fields.Nested(PresentmentMoney, required=False)
    
    shop_money = fields.Nested(ShopMoney, required=False)
    


class PresentmentMoney(BaseSchema):
    # Order swagger.json

    
    amount = fields.Str(required=False)
    
    currency_code = fields.Str(required=False)
    


class ShopMoney(BaseSchema):
    # Order swagger.json

    
    amount = fields.Str(required=False)
    
    currency_code = fields.Str(required=False)
    


class TotalPriceSet(BaseSchema):
    # Order swagger.json

    
    shop_money = fields.Nested(TotalPriceSetShopMoney, required=False)
    
    presentment_money = fields.Nested(TotalPriceSetPresentmentMoney, required=False)
    


class TotalPriceSetShopMoney(BaseSchema):
    # Order swagger.json

    
    amount = fields.Str(required=False)
    
    currency_code = fields.Str(required=False)
    


class TotalPriceSetPresentmentMoney(BaseSchema):
    # Order swagger.json

    
    amount = fields.Str(required=False)
    
    currency_code = fields.Str(required=False)
    


class TotalTaxSet(BaseSchema):
    # Order swagger.json

    
    shop_money = fields.Nested(TotalTaxSetShopMoney, required=False)
    
    presentment_money = fields.Nested(TotalTaxSetPresentmentMoney, required=False)
    


class TotalTaxSetShopMoney(BaseSchema):
    # Order swagger.json

    
    amount = fields.Str(required=False)
    
    currency_code = fields.Str(required=False)
    


class TotalTaxSetPresentmentMoney(BaseSchema):
    # Order swagger.json

    
    amount = fields.Str(required=False)
    
    currency_code = fields.Str(required=False)
    


class SubtotalPriceSet(BaseSchema):
    # Order swagger.json

    
    shop_money = fields.Nested(SubtotalPriceSetShopMoney, required=False)
    
    presentment_money = fields.Nested(SubtotalPriceSetPresentmentMoney, required=False)
    


class SubtotalPriceSetShopMoney(BaseSchema):
    # Order swagger.json

    
    amount = fields.Str(required=False)
    
    currency_code = fields.Str(required=False)
    


class SubtotalPriceSetPresentmentMoney(BaseSchema):
    # Order swagger.json

    
    amount = fields.Str(required=False)
    
    currency_code = fields.Str(required=False)
    


class LineItems(BaseSchema):
    # Order swagger.json

    
    sku = fields.Str(required=False)
    
    fulfillable_quantity = fields.Int(required=False)
    
    grams = fields.Int(required=False)
    
    total_discount = fields.Str(required=False)
    
    article = fields.Nested(LineItemsArticle, required=False)
    
    title = fields.Str(required=False)
    
    variant_inventory_management = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    variant_id = fields.Int(required=False)
    
    variant_title = fields.Str(required=False)
    
    product_exists = fields.Boolean(required=False)
    
    price = fields.Str(required=False)
    
    admin_graphql_api_id = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    vendor = fields.Str(required=False)
    
    fulfillment_service = fields.Str(required=False)
    
    taxable = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    product_id = fields.Int(required=False)
    
    price_set = fields.Nested(PriceSet, required=False)
    
    tax_lines = fields.Nested(TaxLines, required=False)
    
    requires_shipping = fields.Boolean(required=False)
    
    gift_card = fields.Boolean(required=False)
    
    total_discount_set = fields.Nested(TotalDiscountSet, required=False)
    


class LineItemsArticle(BaseSchema):
    # Order swagger.json

    
    quantities = fields.Nested(Quantities, required=False)
    
    old_article_uid = fields.Str(required=False)
    
    total_quantity = fields.Int(required=False)
    
    manufacturer = fields.Nested(Manufacturer, required=False)
    
    price = fields.Nested(ArticlePrice, required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    company = fields.Nested(Company, required=False)
    
    is_active = fields.Boolean(required=False)
    
    date_meta = fields.Nested(FailOrderDateMeta, required=False)
    
    fragile = fields.Boolean(required=False)
    
    marketplace_identifiers = fields.Nested(MarketplaceIdentifiers, required=False)
    
    size = fields.Str(required=False)
    
    is_set = fields.Boolean(required=False)
    
    dimension = fields.Nested(Dimension, required=False)
    
    weight = fields.Nested(Weight, required=False)
    
    store = fields.Nested(Store, required=False)
    
    meta = fields.Nested(ArticleMeta, required=False)
    
    uid = fields.Str(required=False)
    
    brand = fields.Nested(ArticleBrand, required=False)
    
    item_id = fields.Int(required=False)
    
    fynd_article_code = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    identifier = fields.Nested(LineItemsArticleIdentifier, required=False)
    
    seller_identifier = fields.Str(required=False)
    
    fynd_item_code = fields.Str(required=False)
    
    country_of_origin = fields.Str(required=False)
    


class Quantities(BaseSchema):
    # Order swagger.json

    
    not_available = fields.Nested(NotAvailable, required=False)
    
    sellable = fields.Nested(Sellable, required=False)
    
    order_committed = fields.Nested(OrderCommitted, required=False)
    
    damaged = fields.Nested(Damaged, required=False)
    


class NotAvailable(BaseSchema):
    # Order swagger.json

    
    count = fields.Int(required=False)
    
    updated_at = fields.Str(required=False)
    


class Sellable(BaseSchema):
    # Order swagger.json

    
    count = fields.Int(required=False)
    
    updated_at = fields.Str(required=False)
    


class OrderCommitted(BaseSchema):
    # Order swagger.json

    
    count = fields.Int(required=False)
    
    updated_at = fields.Str(required=False)
    


class Damaged(BaseSchema):
    # Order swagger.json

    
    updated_at = fields.Str(required=False)
    
    count = fields.Int(required=False)
    


class Manufacturer(BaseSchema):
    # Order swagger.json

    
    is_default = fields.Boolean(required=False)
    
    address = fields.Str(required=False)
    
    name = fields.Str(required=False)
    


class ArticlePrice(BaseSchema):
    # Order swagger.json

    
    marked = fields.Int(required=False)
    
    currency = fields.Str(required=False)
    
    effective = fields.Int(required=False)
    
    transfer = fields.Int(required=False)
    


class Company(BaseSchema):
    # Order swagger.json

    
    id = fields.Int(required=False)
    
    company_type = fields.Str(required=False)
    
    business_type = fields.Str(required=False)
    
    company_name = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    pan_no = fields.Str(required=False)
    
    return_allowed = fields.Boolean(required=False)
    
    meta = fields.Str(required=False)
    
    exchange_allowed = fields.Boolean(required=False)
    
    agreement_start_date = fields.Str(required=False)
    
    exchange_within_days = fields.Int(required=False)
    
    payment_procesing_charge = fields.Int(required=False)
    
    fynd_a_fit_available = fields.Boolean(required=False)
    
    modified_on = fields.Str(required=False)
    
    return_within_days = fields.Int(required=False)
    


class FailOrderDateMeta(BaseSchema):
    # Order swagger.json

    
    added_on_store = fields.Str(required=False)
    
    inventory_updated_on = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    


class MarketplaceIdentifiers(BaseSchema):
    # Order swagger.json

    
    tatacliq_luxury = fields.Nested(TatacliqLuxury, required=False)
    


class TatacliqLuxury(BaseSchema):
    # Order swagger.json

    
    sku = fields.Str(required=False)
    


class Dimension(BaseSchema):
    # Order swagger.json

    
    height = fields.Int(required=False)
    
    width = fields.Int(required=False)
    
    unit = fields.Str(required=False)
    
    length = fields.Int(required=False)
    
    is_default = fields.Boolean(required=False)
    


class Weight(BaseSchema):
    # Order swagger.json

    
    is_default = fields.Boolean(required=False)
    
    unit = fields.Str(required=False)
    
    shipping = fields.Int(required=False)
    


class Store(BaseSchema):
    # Order swagger.json

    
    id = fields.Int(required=False)
    


class ArticleMeta(BaseSchema):
    # Order swagger.json

    
    service = fields.Str(required=False)
    


class ArticleBrand(BaseSchema):
    # Order swagger.json

    
    name = fields.Str(required=False)
    
    id = fields.Int(required=False)
    


class LineItemsArticleIdentifier(BaseSchema):
    # Order swagger.json

    
    sku_code = fields.Str(required=False)
    


class PriceSet(BaseSchema):
    # Order swagger.json

    
    shop_money = fields.Nested(PriceSetShopMoney, required=False)
    
    presentment_money = fields.Nested(PriceSetPresentmentMoney, required=False)
    


class PriceSetShopMoney(BaseSchema):
    # Order swagger.json

    
    amount = fields.Str(required=False)
    
    currency_code = fields.Str(required=False)
    


class PriceSetPresentmentMoney(BaseSchema):
    # Order swagger.json

    
    amount = fields.Str(required=False)
    
    currency_code = fields.Str(required=False)
    


class TaxLines(BaseSchema):
    # Order swagger.json

    
    title = fields.Str(required=False)
    
    price = fields.Str(required=False)
    
    rate = fields.Int(required=False)
    
    price_set = fields.Nested(TaxLinesPriceSet, required=False)
    


class TaxLinesPriceSet(BaseSchema):
    # Order swagger.json

    
    shop_money = fields.Nested(TaxLinesPriceSetShopMoney, required=False)
    
    presentment_money = fields.Nested(TaxLinesPriceSetPresentmentMoney, required=False)
    


class TaxLinesPriceSetShopMoney(BaseSchema):
    # Order swagger.json

    
    amount = fields.Str(required=False)
    
    currency_code = fields.Str(required=False)
    


class TaxLinesPriceSetPresentmentMoney(BaseSchema):
    # Order swagger.json

    
    currency_code = fields.Str(required=False)
    
    amount = fields.Str(required=False)
    


class TotalDiscountSet(BaseSchema):
    # Order swagger.json

    
    presentment_money = fields.Nested(TotalDiscountSetPresentmentMoney, required=False)
    
    shop_money = fields.Nested(TotalDiscountSetShopMoney, required=False)
    


class TotalDiscountSetPresentmentMoney(BaseSchema):
    # Order swagger.json

    
    amount = fields.Str(required=False)
    
    currency_code = fields.Str(required=False)
    


class TotalDiscountSetShopMoney(BaseSchema):
    # Order swagger.json

    
    amount = fields.Str(required=False)
    
    currency_code = fields.Str(required=False)
    


class BillingAddress(BaseSchema):
    # Order swagger.json

    
    address1 = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    zip = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    
    address2 = fields.Str(required=False)
    
    latitude = fields.Float(required=False)
    
    longitude = fields.Float(required=False)
    
    province_code = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    
    company = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    first_name = fields.Str(required=False)
    
    province = fields.Str(required=False)
    


class TotalShippingPriceSet(BaseSchema):
    # Order swagger.json

    
    shop_money = fields.Nested(TotalShippingPriceSetShopMoney, required=False)
    
    presentment_money = fields.Nested(TotalShippingPriceSetPresentmentMoney, required=False)
    


class TotalShippingPriceSetShopMoney(BaseSchema):
    # Order swagger.json

    
    amount = fields.Str(required=False)
    
    currency_code = fields.Str(required=False)
    


class TotalShippingPriceSetPresentmentMoney(BaseSchema):
    # Order swagger.json

    
    amount = fields.Str(required=False)
    
    currency_code = fields.Str(required=False)
    


class Customer(BaseSchema):
    # Order swagger.json

    
    created_at = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    last_name = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    last_order_id = fields.Int(required=False)
    
    note = fields.Str(required=False)
    
    verified_email = fields.Boolean(required=False)
    
    phone = fields.Str(required=False)
    
    accepts_marketing = fields.Boolean(required=False)
    
    first_name = fields.Str(required=False)
    
    tags = fields.Str(required=False)
    
    last_order_name = fields.Str(required=False)
    
    orders_count = fields.Int(required=False)
    
    total_spent = fields.Str(required=False)
    
    tax_exempt = fields.Boolean(required=False)
    
    currency = fields.Str(required=False)
    
    accepts_marketing_updated_at = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    admin_graphql_api_id = fields.Str(required=False)
    
    default_address = fields.Nested(DefaultAddress, required=False)
    


class DefaultAddress(BaseSchema):
    # Order swagger.json

    
    last_name = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    province_code = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    is_default = fields.Boolean(required=False)
    
    id = fields.Int(required=False)
    
    customer_id = fields.Int(required=False)
    
    first_name = fields.Str(required=False)
    
    address1 = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    
    country_name = fields.Str(required=False)
    
    company = fields.Str(required=False)
    
    address2 = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    province = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    zip = fields.Str(required=False)
    


class TotalLineItemsPriceSet(BaseSchema):
    # Order swagger.json

    
    shop_money = fields.Nested(TotalLineItemsPriceSetShopMoney, required=False)
    
    presentment_money = fields.Nested(TotalLineItemsPriceSetPresentmentMoney, required=False)
    


class TotalLineItemsPriceSetShopMoney(BaseSchema):
    # Order swagger.json

    
    amount = fields.Str(required=False)
    
    currency_code = fields.Str(required=False)
    


class TotalLineItemsPriceSetPresentmentMoney(BaseSchema):
    # Order swagger.json

    
    amount = fields.Str(required=False)
    
    currency_code = fields.Str(required=False)
    


class OrderShippingAddress(BaseSchema):
    # Order swagger.json

    
    address1 = fields.Str(required=False)
    
    zip = fields.Str(required=False)
    
    address2 = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    
    province_code = fields.Str(required=False)
    
    first_name = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    
    province = fields.Str(required=False)
    
    latitude = fields.Float(required=False)
    
    longitude = fields.Float(required=False)
    
    city = fields.Str(required=False)
    
    company = fields.Str(required=False)
    
    name = fields.Str(required=False)
    


class OrderListing(BaseSchema):
    # Order swagger.json

    
    items = fields.List(fields.Nested(OrderItems, required=False), required=False)
    
    filters = fields.Nested(Filters, required=False)
    
    next_order_status = fields.Dict(required=False)
    
    page = fields.Nested(PlatformOrderPage, required=False)
    
    applied_filters = fields.Nested(AppliedFilters, required=False)
    


class OrderItems(BaseSchema):
    # Order swagger.json

    
    user = fields.Nested(PlatformOrderUserInfo, required=False)
    
    delivery_address = fields.Nested(PlatformDeliveryAddress, required=False)
    
    channel = fields.Nested(Channel, required=False)
    
    id = fields.Str(required=False)
    
    application = fields.Nested(PlatformApplication, required=False)
    
    shipments = fields.Nested(PlatformShipment, required=False)
    
    created_at = fields.Str(required=False)
    
    total_shipments_in_order = fields.Int(required=False)
    


class PlatformOrderUserInfo(BaseSchema):
    # Order swagger.json

    
    mobile = fields.Str(required=False)
    
    first_name = fields.Str(required=False)
    
    gender = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    
    is_anonymous_user = fields.Boolean(required=False)
    
    uid = fields.Int(required=False)
    
    avis_user_id = fields.Str(required=False)
    


class PlatformDeliveryAddress(BaseSchema):
    # Order swagger.json

    
    area = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    version = fields.Str(required=False)
    
    address1 = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    landmark = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    address = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    
    latitude = fields.Float(required=False)
    
    longitude = fields.Float(required=False)
    
    address_type = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    
    address2 = fields.Str(required=False)
    
    contact_person = fields.Str(required=False)
    
    address_category = fields.Str(required=False)
    


class Channel(BaseSchema):
    # Order swagger.json

    
    name = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    


class PlatformApplication(BaseSchema):
    # Order swagger.json

    
    id = fields.Str(required=False)
    


class PlatformShipment(BaseSchema):
    # Order swagger.json

    
    status = fields.Nested(PlatformShipmentStatus, required=False)
    
    bags = fields.Nested(Bags, required=False)
    
    prices = fields.Nested(ShipmentPrices, required=False)
    
    id = fields.Str(required=False)
    
    gst = fields.Nested(ShipmentGst, required=False)
    
    priority = fields.Float(required=False)
    
    priority_text = fields.Str(required=False)
    
    lock_status = fields.Boolean(required=False)
    
    ordering_channel = fields.Str(required=False)
    
    total_shipment_bags = fields.Int(required=False)
    


class PlatformShipmentStatus(BaseSchema):
    # Order swagger.json

    
    id = fields.Int(required=False)
    
    bag_list = fields.List(fields.Int(required=False), required=False)
    
    created_at = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    progress = fields.Int(required=False)
    
    shipment_id = fields.Str(required=False)
    
    current_shipment_status = fields.Str(required=False)
    
    color_code = fields.Str(required=False)
    


class Bags(BaseSchema):
    # Order swagger.json

    
    item = fields.Nested(BagItem, required=False)
    
    id = fields.Int(required=False)
    


class BagItem(BaseSchema):
    # Order swagger.json

    
    id = fields.Int(required=False)
    
    size = fields.Str(required=False)
    
    slug_key = fields.Str(required=False)
    
    can_return = fields.Boolean(required=False)
    
    brand_id = fields.Int(required=False)
    
    l2_category = fields.List(fields.Str(required=False), required=False)
    
    name = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    attributes = fields.Nested(BagItemAttributes, required=False)
    
    l3_category_name = fields.Str(required=False)
    
    l3_category = fields.Int(required=False)
    
    l1_category = fields.List(fields.Str(required=False), required=False)
    
    image = fields.List(fields.Str(required=False), required=False)
    
    brand = fields.Str(required=False)
    
    last_updated_at = fields.Str(required=False)
    


class BagItemAttributes(BaseSchema):
    # Order swagger.json

    
    item_code = fields.Str(required=False)
    
    brand_name = fields.Str(required=False)
    
    country_of_origin = fields.Str(required=False)
    


class ShipmentPrices(BaseSchema):
    # Order swagger.json

    
    refund_amount = fields.Float(required=False)
    
    cashback_applied = fields.Float(required=False)
    
    transfer_price = fields.Float(required=False)
    
    coupon_value = fields.Float(required=False)
    
    amount_paid = fields.Float(required=False)
    
    delivery_charge = fields.Float(required=False)
    
    coupon_effective_discount = fields.Float(required=False)
    
    cod_charges = fields.Float(required=False)
    
    refund_credit = fields.Float(required=False)
    
    added_to_fynd_cash = fields.Boolean(required=False)
    
    gst_tax_percentage = fields.Float(required=False)
    
    price_marked = fields.Float(required=False)
    
    price_effective = fields.Float(required=False)
    
    discount = fields.Float(required=False)
    
    promotion_effective_discount = fields.Float(required=False)
    
    amount_paid_roundoff = fields.Float(required=False)
    
    fynd_credits = fields.Float(required=False)
    
    brand_calculated_amount = fields.Float(required=False)
    
    cashback = fields.Float(required=False)
    
    value_of_good = fields.Float(required=False)
    


class Payments(BaseSchema):
    # Order swagger.json

    
    is_active = fields.Boolean(required=False)
    
    display_name = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    source = fields.Str(required=False)
    
    source_nickname = fields.Str(required=False)
    
    display_priority = fields.Int(required=False)
    
    id = fields.Int(required=False)
    
    mode = fields.Str(required=False)
    
    payment_identifier = fields.Str(required=False)
    


class Filters(BaseSchema):
    # Order swagger.json

    
    stage = fields.Nested(Stage, required=False)
    
    stages = fields.Nested(Stages, required=False)
    


class Stage(BaseSchema):
    # Order swagger.json

    
    text = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    is_default = fields.Boolean(required=False)
    
    filters = fields.Nested(StagesFilters, required=False)
    


class StagesFilters(BaseSchema):
    # Order swagger.json

    
    text = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    options = fields.Nested(Options, required=False)
    


class Options(BaseSchema):
    # Order swagger.json

    
    text = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class PlatformOrderPage(BaseSchema):
    # Order swagger.json

    
    next = fields.Str(required=False)
    
    previous = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    size = fields.Int(required=False)
    
    current = fields.Int(required=False)
    
    has_next = fields.Boolean(required=False)
    
    total = fields.Int(required=False)
    
    item_total = fields.Nested(ItemTotal, required=False)
    


class AppliedFilters(BaseSchema):
    # Order swagger.json

    
    stage = fields.Str(required=False)
    
    stores = fields.List(fields.Str(required=False), required=False)
    
    deployment_stores = fields.List(fields.Str(required=False), required=False)
    
    dp = fields.List(fields.Int(required=False), required=False)
    
    from_date = fields.Str(required=False)
    
    to_date = fields.Str(required=False)
    


class OrderDetails(BaseSchema):
    # Order swagger.json

    
    items = fields.List(fields.Nested(OrderPicklistListing, required=False), required=False)
    
    page = fields.Nested(PlatformOrderPage, required=False)
    
    filters = fields.Nested(Filters, required=False)
    
    next_order_status = fields.Dict(required=False)
    
    applied_filters = fields.Nested(AppliedFilters, required=False)
    


class OrderDetailsItem(BaseSchema):
    # Order swagger.json

    
    user = fields.Nested(PlatformOrderUserInfo, required=False)
    
    delivery_address = fields.Nested(PlatformDeliveryAddress, required=False)
    
    channel = fields.Nested(Channel, required=False)
    
    fyndstore_emp = fields.Dict(required=False)
    
    ordering_store = fields.Dict(required=False)
    
    breakup_values = fields.Nested(PlatformBreakupValues, required=False)
    
    id = fields.Str(required=False)
    
    application = fields.Nested(PlatformApplication, required=False)
    
    shipments = fields.Nested(PlatformShipmentDetails, required=False)
    
    created_at = fields.Str(required=False)
    
    total_shipments_in_order = fields.Int(required=False)
    
    payments = fields.Nested(ItemsPayments, required=False)
    
    payment_methods = fields.Dict(required=False)
    


class PlatformBreakupValues(BaseSchema):
    # Order swagger.json

    
    display = fields.Str(required=False)
    
    value = fields.Float(required=False)
    
    name = fields.Str(required=False)
    


class ArticleAssignment(BaseSchema):
    # Order swagger.json

    
    strategy = fields.Str(required=False)
    
    level = fields.Str(required=False)
    


class PlatformShipmentDetails(BaseSchema):
    # Order swagger.json

    
    status = fields.Nested(PlatformShipmentDetailsStatus, required=False)
    
    bags = fields.Nested(BagsDetails, required=False)
    
    prices = fields.Nested(ShipmentPrices, required=False)
    
    breakup_values = fields.Nested(ShipmentBreakupValues, required=False)
    
    id = fields.Str(required=False)
    
    dp_details = fields.Nested(DpDetails, required=False)
    
    payment_methods = fields.Dict(required=False)
    
    invoice = fields.Nested(ShipmentInvoice, required=False)
    
    fulfilling_store = fields.Nested(PlatformFulfillingStore, required=False)
    
    payments = fields.Nested(Payments, required=False)
    
    gst = fields.Nested(ShipmentGst, required=False)
    
    company = fields.Nested(Company, required=False)
    
    brand = fields.Nested(PlatformShipmentDetailsBrand, required=False)
    
    coupon = fields.Dict(required=False)
    
    order_source = fields.Str(required=False)
    
    is_not_fynd_source = fields.Boolean(required=False)
    
    can_break = fields.Dict(required=False)
    
    comment = fields.Str(required=False)
    
    promise = fields.Nested(Promise, required=False)
    
    tracking_details = fields.Nested(ShipmentTrackingDetails, required=False)
    
    is_fynd_coupon = fields.Boolean(required=False)
    
    order_type = fields.Str(required=False)
    
    total_shipment_bags = fields.Int(required=False)
    
    pod = fields.Dict(required=False)
    
    lock_status = fields.Boolean(required=False)
    
    priority = fields.Float(required=False)
    
    priority_text = fields.Str(required=False)
    
    ordering_channel = fields.Str(required=False)
    
    credit_note_id = fields.Str(required=False)
    
    auto_trigger_dp_assignment = fields.Boolean(required=False)
    
    packaging_type = fields.Str(required=False)
    
    dates = fields.Nested(ShipmentDates, required=False)
    


class PlatformShipmentDetailsStatus(BaseSchema):
    # Order swagger.json

    
    id = fields.Int(required=False)
    
    bag_list = fields.List(fields.Int(required=False), required=False)
    
    created_at = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    progress = fields.Int(required=False)
    
    shipment_id = fields.Str(required=False)
    
    current_shipment_status = fields.Str(required=False)
    
    color_code = fields.Str(required=False)
    


class BagsDetails(BaseSchema):
    # Order swagger.json

    
    financial_breakup = fields.List(fields.Nested(BagFinancialBreakup, required=False), required=False)
    
    status = fields.Nested(BagCurrStatus, required=False)
    
    item = fields.Nested(BagItem, required=False)
    
    article = fields.Nested(BagArticle, required=False)
    
    id = fields.Int(required=False)
    
    prices = fields.Nested(BagPrices, required=False)
    
    gst_details = fields.Nested(GstDetails, required=False)
    
    breakup_values = fields.Nested(BagBreakupValues, required=False)
    
    update_time = fields.Int(required=False)
    
    current_status = fields.Nested(BagCurrentStatus, required=False)
    
    bag_status = fields.Nested(BagStatus, required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    can_return = fields.Boolean(required=False)
    
    payment_methods = fields.Dict(required=False)
    


class BagFinancialBreakup(BaseSchema):
    # Order swagger.json

    
    value_of_good = fields.Float(required=False)
    
    hsn_code = fields.Str(required=False)
    
    price_effective = fields.Float(required=False)
    
    cod_charges = fields.Float(required=False)
    
    gst_fee = fields.Float(required=False)
    
    fynd_credits = fields.Float(required=False)
    
    refund_amount = fields.Float(required=False)
    
    cashback_applied = fields.Float(required=False)
    
    transfer_price = fields.Float(required=False)
    
    amount_paid_roundoff = fields.Float(required=False)
    
    coupon_value = fields.Float(required=False)
    
    amount_paid = fields.Float(required=False)
    
    gst_tax_percentage = fields.Float(required=False)
    
    size = fields.Str(required=False)
    
    total_units = fields.Int(required=False)
    
    discount = fields.Float(required=False)
    
    coupon_effective_discount = fields.Float(required=False)
    
    cashback = fields.Float(required=False)
    
    promotion_effective_discount = fields.Float(required=False)
    
    gst_tag = fields.Str(required=False)
    
    delivery_charge = fields.Float(required=False)
    
    refund_credit = fields.Float(required=False)
    
    price_marked = fields.Float(required=False)
    
    identifiers = fields.Nested(Identifiers, required=False)
    
    item_name = fields.Str(required=False)
    
    added_to_fynd_cash = fields.Boolean(required=False)
    
    brand_calculated_amount = fields.Float(required=False)
    


class Identifiers(BaseSchema):
    # Order swagger.json

    
    ean = fields.Str(required=False)
    


class BagCurrStatus(BaseSchema):
    # Order swagger.json

    
    enable_tracking = fields.Boolean(required=False)
    
    is_customer_return_allowed = fields.Boolean(required=False)
    
    is_active = fields.Boolean(required=False)
    
    is_returnable = fields.Boolean(required=False)
    
    can_be_cancelled = fields.Boolean(required=False)
    


class BagArticle(BaseSchema):
    # Order swagger.json

    
    identifiers = fields.Nested(ArticleIdentifiers, required=False)
    
    esp_modified = fields.Boolean(required=False)
    
    is_set = fields.Boolean(required=False)
    
    size = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    set = fields.Nested(Set, required=False)
    
    seller_identifier = fields.Str(required=False)
    
    return_config = fields.Nested(BagArticleReturnConfig, required=False)
    
    _id = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    child_details = fields.Dict(required=False)
    


class ArticleIdentifiers(BaseSchema):
    # Order swagger.json

    
    ean = fields.Str(required=False)
    


class Set(BaseSchema):
    # Order swagger.json

    
    quantity = fields.Int(required=False)
    
    size_distribution = fields.Nested(SetSizeDistribution, required=False)
    


class SetSizeDistribution(BaseSchema):
    # Order swagger.json

    
    sizes = fields.Nested(Sizes, required=False)
    


class Sizes(BaseSchema):
    # Order swagger.json

    
    size = fields.Str(required=False)
    
    pieces = fields.Int(required=False)
    


class BagArticleReturnConfig(BaseSchema):
    # Order swagger.json

    
    time = fields.Int(required=False)
    
    unit = fields.Str(required=False)
    
    returnable = fields.Boolean(required=False)
    


class GstDetails(BaseSchema):
    # Order swagger.json

    
    brand_calculated_amount = fields.Float(required=False)
    
    gst_fee = fields.Float(required=False)
    
    gst_tag = fields.Str(required=False)
    
    hsn_code = fields.Str(required=False)
    
    value_of_good = fields.Float(required=False)
    
    gst_tax_percentage = fields.Float(required=False)
    
    is_default_hsn_code = fields.Boolean(required=False)
    


class BagBreakupValues(BaseSchema):
    # Order swagger.json

    
    name = fields.Str(required=False)
    
    display = fields.Str(required=False)
    
    value = fields.Float(required=False)
    


class BagCurrentStatus(BaseSchema):
    # Order swagger.json

    
    updated_at = fields.Str(required=False)
    
    bag_state_mapper = fields.Nested(BagStateMapper, required=False)
    
    status = fields.Str(required=False)
    
    state_type = fields.Str(required=False)
    


class BagStateMapper(BaseSchema):
    # Order swagger.json

    
    app_state_name = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    display_name = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    app_display_name = fields.Str(required=False)
    


class BagStatus(BaseSchema):
    # Order swagger.json

    
    status = fields.Str(required=False)
    
    state_type = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    bag_state_mapper = fields.Nested(BagStatusBagStateMapper, required=False)
    


class BagStatusBagStateMapper(BaseSchema):
    # Order swagger.json

    
    is_active = fields.Boolean(required=False)
    
    display_name = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    app_display_name = fields.Str(required=False)
    
    app_state_name = fields.Str(required=False)
    


class BagPrices(BaseSchema):
    # Order swagger.json

    
    cashback = fields.Float(required=False)
    
    refund_credit = fields.Float(required=False)
    
    coupon_value = fields.Float(required=False)
    
    delivery_charge = fields.Float(required=False)
    
    fynd_credits = fields.Float(required=False)
    
    price_marked = fields.Float(required=False)
    
    cashback_applied = fields.Float(required=False)
    
    value_of_good = fields.Float(required=False)
    
    amount_paid_roundoff = fields.Float(required=False)
    
    amount_paid = fields.Float(required=False)
    
    cod_charges = fields.Float(required=False)
    
    price_effective = fields.Float(required=False)
    
    refund_amount = fields.Float(required=False)
    
    discount = fields.Float(required=False)
    


class ShipmentBreakupValues(BaseSchema):
    # Order swagger.json

    
    name = fields.Str(required=False)
    
    display = fields.Str(required=False)
    
    value = fields.Float(required=False)
    


class DpDetails(BaseSchema):
    # Order swagger.json

    
    gst_tag = fields.Str(required=False)
    


class ShipmentInvoice(BaseSchema):
    # Order swagger.json

    
    payment_type = fields.Str(required=False)
    
    updated_date = fields.Str(required=False)
    
    invoice_url = fields.Str(required=False)
    
    label_url = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
    amount_to_collect = fields.Float(required=False)
    
    rto_address = fields.Nested(RtoAddress, required=False)
    


class RtoAddress(BaseSchema):
    # Order swagger.json

    
    name = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    phone = fields.Str(required=False)
    
    location_type = fields.Str(required=False)
    
    store_address_json = fields.Nested(StoreAddressJson, required=False)
    
    code = fields.Str(required=False)
    
    address1 = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    contact_person = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    store_email = fields.Str(required=False)
    
    address2 = fields.Str(required=False)
    


class StoreAddressJson(BaseSchema):
    # Order swagger.json

    
    country = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    area = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    address_type = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    
    address1 = fields.Str(required=False)
    
    address2 = fields.Str(required=False)
    
    latitude = fields.Float(required=False)
    
    longitude = fields.Float(required=False)
    
    email = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    contact_person = fields.Str(required=False)
    
    address_category = fields.Str(required=False)
    
    version = fields.Str(required=False)
    
    landmark = fields.Str(required=False)
    


class PlatformFulfillingStore(BaseSchema):
    # Order swagger.json

    
    packaging_material_count = fields.Int(required=False)
    
    location_type = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    meta = fields.Nested(FulfillingStoreMeta, required=False)
    
    name = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    address1 = fields.Str(required=False)
    
    store_email = fields.Str(required=False)
    
    is_archived = fields.Boolean(required=False)
    
    state = fields.Str(required=False)
    
    address2 = fields.Str(required=False)
    
    contact_person = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    
    is_enabled_for_recon = fields.Boolean(required=False)
    
    fulfillment_channel = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    pincode = fields.Str(required=False)
    
    brand_store_tags = fields.List(fields.Str(required=False), required=False)
    
    company_id = fields.Int(required=False)
    
    store_address_json = fields.Nested(FulfillingStoreStoreAddressJson, required=False)
    
    updated_at = fields.Str(required=False)
    
    login_username = fields.Str(required=False)
    
    country = fields.Str(required=False)
    


class FulfillingStoreMeta(BaseSchema):
    # Order swagger.json

    
    additional_contact_details = fields.Nested(AdditionalContactDetails, required=False)
    
    documents = fields.Nested(Documents, required=False)
    
    gst_number = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    product_return_config = fields.Nested(ProductReturnConfig, required=False)
    
    allow_dp_assignment_from_fynd = fields.Boolean(required=False)
    
    stage = fields.Str(required=False)
    
    timing = fields.Nested(Timing, required=False)
    


class AdditionalContactDetails(BaseSchema):
    # Order swagger.json

    
    number = fields.List(fields.Str(required=False), required=False)
    


class Documents(BaseSchema):
    # Order swagger.json

    
    gst = fields.Nested(Gst, required=False)
    


class Gst(BaseSchema):
    # Order swagger.json

    
    legal_name = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    verified = fields.Boolean(required=False)
    


class ProductReturnConfig(BaseSchema):
    # Order swagger.json

    
    on_same_store = fields.Boolean(required=False)
    


class Timing(BaseSchema):
    # Order swagger.json

    
    opening = fields.Nested(Opening, required=False)
    
    weekday = fields.Str(required=False)
    
    open = fields.Boolean(required=False)
    
    closing = fields.Nested(Closing, required=False)
    


class Opening(BaseSchema):
    # Order swagger.json

    
    minute = fields.Int(required=False)
    
    hour = fields.Int(required=False)
    


class Closing(BaseSchema):
    # Order swagger.json

    
    hour = fields.Int(required=False)
    
    minute = fields.Int(required=False)
    


class FulfillingStoreStoreAddressJson(BaseSchema):
    # Order swagger.json

    
    address2 = fields.Str(required=False)
    
    area = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    contact_person = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    
    version = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    address_type = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    address1 = fields.Str(required=False)
    
    landmark = fields.Str(required=False)
    
    latitude = fields.Float(required=False)
    
    longitude = fields.Float(required=False)
    
    updated_at = fields.Str(required=False)
    
    address_category = fields.Str(required=False)
    


class ShipmentGst(BaseSchema):
    # Order swagger.json

    
    brand_calculated_amount = fields.Float(required=False)
    
    value_of_good = fields.Float(required=False)
    
    gst_fee = fields.Float(required=False)
    


class PlatformShipmentDetailsBrand(BaseSchema):
    # Order swagger.json

    
    credit_note_allowed = fields.Boolean(required=False)
    
    brand_name = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    is_virtual_invoice = fields.Boolean(required=False)
    
    created_on = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    


class Promise(BaseSchema):
    # Order swagger.json

    
    timestamp = fields.Nested(Timestamp, required=False)
    


class Timestamp(BaseSchema):
    # Order swagger.json

    
    min = fields.Str(required=False)
    
    max = fields.Str(required=False)
    


class ShipmentTrackingDetails(BaseSchema):
    # Order swagger.json

    
    status = fields.Str(required=False)
    
    time = fields.Str(required=False)
    
    is_passed = fields.Boolean(required=False)
    
    is_current = fields.Boolean(required=False)
    


class ItemsPayments(BaseSchema):
    # Order swagger.json

    
    display_priority = fields.Int(required=False)
    
    id = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    display_name = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    payment_identifier = fields.Str(required=False)
    
    source_nickname = fields.Str(required=False)
    
    mode = fields.Str(required=False)
    
    source = fields.Str(required=False)
    


class PlatformOrderDetailsPage(BaseSchema):
    # Order swagger.json

    
    next = fields.Str(required=False)
    
    previous = fields.Str(required=False)
    


class ShipmentDates(BaseSchema):
    # Order swagger.json

    
    due_date = fields.Str(required=False)
    


class OrderLanesCount(BaseSchema):
    # Order swagger.json

    
    stages = fields.List(fields.Nested(StageItem, required=False), required=False)
    


class StageItem(BaseSchema):
    # Order swagger.json

    
    count = fields.Int(required=False)
    
    text = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class UpdateOrderReprocessResponse(BaseSchema):
    # Order swagger.json

    
    status = fields.Str(required=False)
    


class PlatformOrderTrack(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    request_id = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    resend_timer = fields.Int(required=False)
    
    resend_token = fields.Str(required=False)
    


class OrderPicklistListing(BaseSchema):
    # Order swagger.json

    
    user = fields.Nested(PlatformOrderUserInfo, required=False)
    
    delivery_address = fields.Nested(PlatformDeliveryAddress, required=False)
    
    channel = fields.Nested(Channel, required=False)
    
    fyndstore_emp = fields.Dict(required=False)
    
    ordering_store = fields.Dict(required=False)
    
    breakup_values = fields.Nested(PlatformBreakupValues, required=False)
    
    id = fields.Str(required=False)
    
    application = fields.Nested(PlatformApplication, required=False)
    
    shipments = fields.Nested(PlatformShipmentDetails, required=False)
    
    created_at = fields.Str(required=False)
    
    total_shipments_in_order = fields.Int(required=False)
    
    payments = fields.Nested(ItemsPayments, required=False)
    
    payment_methods = fields.Dict(required=False)
    


class Stages(BaseSchema):
    # Order swagger.json

    
    text = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    is_default = fields.Boolean(required=False)
    
    filters = fields.Nested(StagesFilters, required=False)
    


class ItemTotal(BaseSchema):
    # Order swagger.json

    
    new = fields.Int(required=False)
    
    processing = fields.Int(required=False)
    
    returns = fields.Int(required=False)
    
    all = fields.Int(required=False)
    


class GetPingResponse(BaseSchema):
    # Order swagger.json

    
    ping = fields.Str(required=False)
    


class GetShipmentAddressResponse(BaseSchema):
    # Order swagger.json

    
    message = fields.Str(required=False)
    
    data = fields.Nested(DataShipmentAddress, required=False)
    
    success = fields.Boolean(required=False)
    


class DataShipmentAddress(BaseSchema):
    # Order swagger.json

    
    city = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    
    area = fields.Str(required=False)
    
    address = fields.Str(required=False)
    
    landmark = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    address_type = fields.Str(required=False)
    
    address_category = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    name = fields.Str(required=False)
    


class UpdateShipmentAddressRequest(BaseSchema):
    # Order swagger.json

    
    email = fields.Str(required=False)
    
    address = fields.Str(required=False)
    
    pincode = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    address_type = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    
    area = fields.Str(required=False)
    
    landmark = fields.Str(required=False)
    
    city = fields.Str(required=False)
    


class UpdateShipmentAddressResponse(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class ShipmentTrackResponse(BaseSchema):
    # Order swagger.json

    
    bag_list = fields.List(fields.Nested(ShipmentTrackResponseBagListItem, required=False), required=False)
    
    message = fields.Str(required=False)
    
    order_value = fields.Int(required=False)
    


class ShipmentTrackResponseBagListItem(BaseSchema):
    # Order swagger.json

    
    enable_tracking = fields.Boolean(required=False)
    
    price = fields.Str(required=False)
    
    time_slot = fields.Str(required=False)
    
    product_name = fields.Str(required=False)
    
    can_return = fields.Boolean(required=False)
    
    order_date = fields.Str(required=False)
    
    is_try_at_home = fields.Boolean(required=False)
    
    breakup_values = fields.List(fields.Nested(ShipmentTrackResponseBagListItemBreakValues, required=False), required=False)
    
    statuses = fields.List(fields.Nested(ShipmentTrackResponseBagListItemStatuses, required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    bag_id = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    size = fields.Str(required=False)
    
    payment_mode_source = fields.Str(required=False)
    
    dp_details = fields.Nested(ShipmentTrackResponseBagListItemDpDetails, required=False)
    
    product_id = fields.Int(required=False)
    
    product_image = fields.Nested(ShipmentTrackResponseBagListItemsProductImage, required=False)
    
    brand_name = fields.Str(required=False)
    
    price_marked = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    payment_mode = fields.Str(required=False)
    
    fynd_cash_msg = fields.Str(required=False)
    
    delivery_address = fields.Str(required=False)
    


class ShipmentTrackResponseBagListItemBreakValues(BaseSchema):
    # Order swagger.json

    
    name = fields.Str(required=False)
    
    display = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class ShipmentTrackResponseBagListItemStatuses(BaseSchema):
    # Order swagger.json

    
    nps_rating = fields.Int(required=False)
    
    nps_string = fields.Str(required=False)
    
    progress_status = fields.List(fields.Nested(ShipmentTrackResponseBagListItemStatusesProgress, required=False), required=False)
    
    flow_type = fields.Str(required=False)
    
    status_progress = fields.Int(required=False)
    
    is_nps_done = fields.Boolean(required=False)
    
    header_message = fields.Str(required=False)
    
    is_delayed = fields.Str(required=False)
    
    tracking_list = fields.List(fields.Nested(ShipmentTrackResponseBagListItemStatusesTrack, required=False), required=False)
    


class ShipmentTrackResponseBagListItemStatusesProgress(BaseSchema):
    # Order swagger.json

    
    title = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    state = fields.Boolean(required=False)
    


class ShipmentTrackResponseBagListItemStatusesTrack(BaseSchema):
    # Order swagger.json

    
    status = fields.Str(required=False)
    
    time = fields.Str(required=False)
    
    is_passed = fields.Boolean(required=False)
    
    is_current = fields.Boolean(required=False)
    


class ShipmentTrackResponseBagListItemDpDetails(BaseSchema):
    # Order swagger.json

    
    tracking_no = fields.Str(required=False)
    
    courier = fields.Str(required=False)
    


class ShipmentTrackResponseBagListItemsProductImage(BaseSchema):
    # Order swagger.json

    
    aspect_ratio = fields.Str(required=False)
    
    url = fields.Str(required=False)
    


class UpdateShipmentStatusResponse(BaseSchema):
    # Order swagger.json

    
    shipments = fields.Dict(required=False)
    
    error_shipments = fields.List(fields.Raw(required=False), required=False)
    


class UpdateShipmentStatusBody(BaseSchema):
    # Order swagger.json

    
    shipments = fields.Dict(required=False)
    
    force_transition = fields.Boolean(required=False)
    
    task = fields.Boolean(required=False)
    


class ShipmentReasonsResponse(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    reasons = fields.List(fields.Nested(ShipmentResponseReasons, required=False), required=False)
    


class ShipmentResponseReasons(BaseSchema):
    # Order swagger.json

    
    reason_id = fields.Float(required=False)
    
    reason = fields.Str(required=False)
    


class PlatformShipmentTrack(BaseSchema):
    # Order swagger.json

    
    results = fields.Nested(Results, required=False)
    


class Results(BaseSchema):
    # Order swagger.json

    
    awb = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    last_location_recieved_at = fields.Str(required=False)
    
    reason = fields.Str(required=False)
    
    shipment_type = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    updated_time = fields.Str(required=False)
    
    account_name = fields.Str(required=False)
    


class ShipmentUpdateRequest(BaseSchema):
    # Order swagger.json

    
    bags = fields.List(fields.Str(required=False), required=False)
    
    reason = fields.Dict(required=False)
    
    comments = fields.Str(required=False)
    
    action = fields.Str(required=False)
    


class ShipmentUpdateResponse(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class UpdateProcessShipmenstRequestBody(BaseSchema):
    # Order swagger.json

    
    shipment_ids = fields.List(fields.Str(required=False), required=False)
    
    expected_status = fields.Str(required=False)
    


class UpdateProcessShipmenstRequestResponse(BaseSchema):
    # Order swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class GetVoiceCallbackResponse(BaseSchema):
    # Order swagger.json

    
    message = fields.Str(required=False)
    


class GetClickToCallResponse(BaseSchema):
    # Order swagger.json

    
    message = fields.Str(required=False)
    


class ApefaceApiError(BaseSchema):
    # Order swagger.json

    
    message = fields.Str(required=False)
    


