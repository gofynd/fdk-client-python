"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



class ApplicationAboutResponse(BaseSchema):
    pass


class ApplicationInfo(BaseSchema):
    pass


class CompanyInfo(BaseSchema):
    pass


class OwnerInfo(BaseSchema):
    pass


class AppVersionRequest(BaseSchema):
    pass


class ApplicationVersionRequest(BaseSchema):
    pass


class Device(BaseSchema):
    pass


class OS(BaseSchema):
    pass


class SupportedLanguage(BaseSchema):
    pass


class LanguageResponse(BaseSchema):
    pass


class AppStaffResponse(BaseSchema):
    pass


class AppStaffListResponse(BaseSchema):
    pass


class UpdateDialog(BaseSchema):
    pass


class OrderingStoreSelectRequest(BaseSchema):
    pass


class OrderingStoreSelect(BaseSchema):
    pass


class AppStaff(BaseSchema):
    pass


class AppTokenResponse(BaseSchema):
    pass


class Tokens(BaseSchema):
    pass


class Firebase(BaseSchema):
    pass


class Credentials(BaseSchema):
    pass


class Ios(BaseSchema):
    pass


class Android(BaseSchema):
    pass


class Moengage(BaseSchema):
    pass


class MoengageCredentials(BaseSchema):
    pass


class Segment(BaseSchema):
    pass


class SegmentCredentials(BaseSchema):
    pass


class Gtm(BaseSchema):
    pass


class GtmCredentials(BaseSchema):
    pass


class Freshchat(BaseSchema):
    pass


class FreshchatCredentials(BaseSchema):
    pass


class Safetynet(BaseSchema):
    pass


class SafetynetCredentials(BaseSchema):
    pass


class FyndRewards(BaseSchema):
    pass


class FyndRewardsCredentials(BaseSchema):
    pass


class GoogleMap(BaseSchema):
    pass


class GoogleMapCredentials(BaseSchema):
    pass


class RewardPointsConfig(BaseSchema):
    pass


class Credit(BaseSchema):
    pass


class Debit(BaseSchema):
    pass


class ProductDetailFeature(BaseSchema):
    pass


class LaunchPage(BaseSchema):
    pass


class LandingPageFeature(BaseSchema):
    pass


class RegistrationPageFeature(BaseSchema):
    pass


class AppFeature(BaseSchema):
    pass


class HomePageFeature(BaseSchema):
    pass


class CommonFeature(BaseSchema):
    pass


class CommunicationOptinDialogFeature(BaseSchema):
    pass


class DeploymentStoreSelectionFeature(BaseSchema):
    pass


class ListingPriceFeature(BaseSchema):
    pass


class CurrencyFeature(BaseSchema):
    pass


class RevenueEngineFeature(BaseSchema):
    pass


class FeedbackFeature(BaseSchema):
    pass


class CompareProductsFeature(BaseSchema):
    pass


class CartFeature(BaseSchema):
    pass


class QrFeature(BaseSchema):
    pass


class PcrFeature(BaseSchema):
    pass


class OrderFeature(BaseSchema):
    pass


class AppFeatureRequest(BaseSchema):
    pass


class AppFeatureResponse(BaseSchema):
    pass


class Currency(BaseSchema):
    pass


class Domain(BaseSchema):
    pass


class ApplicationWebsite(BaseSchema):
    pass


class ApplicationCors(BaseSchema):
    pass


class ApplicationAuth(BaseSchema):
    pass


class ApplicationRedirections(BaseSchema):
    pass


class ApplicationMeta(BaseSchema):
    pass


class SecureUrl(BaseSchema):
    pass


class Application(BaseSchema):
    pass


class NotFound(BaseSchema):
    pass


class UnhandledError(BaseSchema):
    pass


class InvalidPayloadRequest(BaseSchema):
    pass


class SuccessMessageResponse(BaseSchema):
    pass


class InventoryBrandRule(BaseSchema):
    pass


class StoreCriteriaRule(BaseSchema):
    pass


class InventoryStoreRule(BaseSchema):
    pass


class InventoryPaymentConfig(BaseSchema):
    pass


class StorePriorityRule(BaseSchema):
    pass


class ArticleAssignmentRule(BaseSchema):
    pass


class InventoryArticleAssignment(BaseSchema):
    pass


class CompanyAboutAddress(BaseSchema):
    pass


class UserEmail(BaseSchema):
    pass


class UserPhoneNumber(BaseSchema):
    pass


class Page(BaseSchema):
    pass


class ApplicationInformation(BaseSchema):
    pass


class InformationAddress(BaseSchema):
    pass


class InformationPhone(BaseSchema):
    pass


class InformationSupport(BaseSchema):
    pass


class SocialLinks(BaseSchema):
    pass


class FacebookLink(BaseSchema):
    pass


class InstagramLink(BaseSchema):
    pass


class TwitterLink(BaseSchema):
    pass


class PinterestLink(BaseSchema):
    pass


class GooglePlusLink(BaseSchema):
    pass


class YoutubeLink(BaseSchema):
    pass


class LinkedInLink(BaseSchema):
    pass


class VimeoLink(BaseSchema):
    pass


class BlogLink(BaseSchema):
    pass


class Links(BaseSchema):
    pass


class BusinessHighlights(BaseSchema):
    pass


class ApplicationDetail(BaseSchema):
    pass


class CurrenciesResponse(BaseSchema):
    pass


class DefaultCurrency(BaseSchema):
    pass


class AppCurrencyResponse(BaseSchema):
    pass


class StoreLatLong(BaseSchema):
    pass


class OptedStoreAddress(BaseSchema):
    pass


class OrderingStore(BaseSchema):
    pass


class OrderingStores(BaseSchema):
    pass


class OrderingStoresResponse(BaseSchema):
    pass



class ApplicationAboutResponse(BaseSchema):
    # Configuration swagger.json

    
    application_info = fields.Nested(ApplicationInfo, required=False)
    
    company_info = fields.Nested(CompanyInfo, required=False)
    
    owner_info = fields.Nested(OwnerInfo, required=False)
    


class ApplicationInfo(BaseSchema):
    # Configuration swagger.json

    
    _id = fields.Str(required=False)
    
    domain = fields.Nested(Domain, required=False)
    
    website = fields.Nested(ApplicationWebsite, required=False)
    
    cors = fields.Nested(ApplicationCors, required=False)
    
    description = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    meta = fields.Nested(ApplicationMeta, required=False)
    
    token = fields.Str(required=False)
    
    secret = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    banner = fields.Nested(SecureUrl, required=False)
    
    logo = fields.Nested(SecureUrl, required=False)
    
    is_active = fields.Boolean(required=False)
    


class CompanyInfo(BaseSchema):
    # Configuration swagger.json

    
    _id = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    created_on = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    addresses = fields.List(fields.Nested(CompanyAboutAddress, required=False), required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    


class OwnerInfo(BaseSchema):
    # Configuration swagger.json

    
    _id = fields.Str(required=False)
    
    emails = fields.List(fields.Nested(UserEmail, required=False), required=False)
    
    phone_numbers = fields.List(fields.Nested(UserPhoneNumber, required=False), required=False)
    
    first_name = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    
    profile_pic = fields.Str(required=False)
    


class AppVersionRequest(BaseSchema):
    # Configuration swagger.json

    
    application = fields.Nested(ApplicationVersionRequest, required=False)
    
    device = fields.Nested(Device, required=False)
    
    locale = fields.Str(required=False)
    
    timezone = fields.Str(required=False)
    


class ApplicationVersionRequest(BaseSchema):
    # Configuration swagger.json

    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    namespace = fields.Str(required=False)
    
    token = fields.Str(required=False)
    
    version = fields.Str(required=False)
    


class Device(BaseSchema):
    # Configuration swagger.json

    
    build = fields.Int(required=False)
    
    model = fields.Str(required=False)
    
    os = fields.Nested(OS, required=False)
    


class OS(BaseSchema):
    # Configuration swagger.json

    
    name = fields.Str(required=False)
    
    version = fields.Str(required=False)
    


class SupportedLanguage(BaseSchema):
    # Configuration swagger.json

    
    name = fields.Str(required=False)
    
    code = fields.Str(required=False)
    


class LanguageResponse(BaseSchema):
    # Configuration swagger.json

    
    items = fields.List(fields.Nested(SupportedLanguage, required=False), required=False)
    


class AppStaffResponse(BaseSchema):
    # Configuration swagger.json

    
    staff_users = fields.List(fields.Nested(AppStaff, required=False), required=False)
    


class AppStaffListResponse(BaseSchema):
    # Configuration swagger.json

    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(AppStaff, required=False), required=False)
    


class UpdateDialog(BaseSchema):
    # Configuration swagger.json

    
    type = fields.Str(required=False)
    
    interval = fields.Int(required=False)
    


class OrderingStoreSelectRequest(BaseSchema):
    # Configuration swagger.json

    
    ordering_store = fields.Nested(OrderingStoreSelect, required=False)
    


class OrderingStoreSelect(BaseSchema):
    # Configuration swagger.json

    
    uid = fields.Int(required=False)
    


class AppStaff(BaseSchema):
    # Configuration swagger.json

    
    _id = fields.Str(required=False)
    
    order_incent = fields.Boolean(required=False)
    
    stores = fields.List(fields.Int(required=False), required=False)
    
    application = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    user = fields.Str(required=False)
    
    employee_code = fields.Str(required=False)
    
    first_name = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    
    profile_pic_url = fields.Str(required=False)
    


class AppTokenResponse(BaseSchema):
    # Configuration swagger.json

    
    tokens = fields.Nested(Tokens, required=False)
    
    _id = fields.Str(required=False)
    
    application = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    


class Tokens(BaseSchema):
    # Configuration swagger.json

    
    firebase = fields.Nested(Firebase, required=False)
    
    moengage = fields.Nested(Moengage, required=False)
    
    segment = fields.Nested(Segment, required=False)
    
    gtm = fields.Nested(Gtm, required=False)
    
    freshchat = fields.Nested(Freshchat, required=False)
    
    safetynet = fields.Nested(Safetynet, required=False)
    
    fynd_rewards = fields.Nested(FyndRewards, required=False)
    
    google_map = fields.Nested(GoogleMap, required=False)
    


class Firebase(BaseSchema):
    # Configuration swagger.json

    
    credentials = fields.Nested(Credentials, required=False)
    
    enabled = fields.Boolean(required=False)
    


class Credentials(BaseSchema):
    # Configuration swagger.json

    
    ios = fields.Nested(Ios, required=False)
    
    android = fields.Nested(Android, required=False)
    
    project_id = fields.Str(required=False)
    
    gcm_sender_id = fields.Str(required=False)
    
    application_id = fields.Str(required=False)
    
    api_key = fields.Str(required=False)
    


class Ios(BaseSchema):
    # Configuration swagger.json

    
    application_id = fields.Str(required=False)
    
    api_key = fields.Str(required=False)
    


class Android(BaseSchema):
    # Configuration swagger.json

    
    application_id = fields.Str(required=False)
    
    api_key = fields.Str(required=False)
    


class Moengage(BaseSchema):
    # Configuration swagger.json

    
    credentials = fields.Nested(MoengageCredentials, required=False)
    
    enabled = fields.Boolean(required=False)
    


class MoengageCredentials(BaseSchema):
    # Configuration swagger.json

    
    app_id = fields.Str(required=False)
    


class Segment(BaseSchema):
    # Configuration swagger.json

    
    credentials = fields.Nested(SegmentCredentials, required=False)
    
    enabled = fields.Boolean(required=False)
    


class SegmentCredentials(BaseSchema):
    # Configuration swagger.json

    
    write_key = fields.Str(required=False)
    


class Gtm(BaseSchema):
    # Configuration swagger.json

    
    credentials = fields.Nested(GtmCredentials, required=False)
    
    enabled = fields.Boolean(required=False)
    


class GtmCredentials(BaseSchema):
    # Configuration swagger.json

    
    api_key = fields.Str(required=False)
    


class Freshchat(BaseSchema):
    # Configuration swagger.json

    
    credentials = fields.Nested(FreshchatCredentials, required=False)
    
    enabled = fields.Boolean(required=False)
    


class FreshchatCredentials(BaseSchema):
    # Configuration swagger.json

    
    app_id = fields.Str(required=False)
    
    app_key = fields.Str(required=False)
    
    web_token = fields.Str(required=False)
    


class Safetynet(BaseSchema):
    # Configuration swagger.json

    
    credentials = fields.Nested(SafetynetCredentials, required=False)
    
    enabled = fields.Boolean(required=False)
    


class SafetynetCredentials(BaseSchema):
    # Configuration swagger.json

    
    api_key = fields.Str(required=False)
    


class FyndRewards(BaseSchema):
    # Configuration swagger.json

    
    credentials = fields.Nested(FyndRewardsCredentials, required=False)
    


class FyndRewardsCredentials(BaseSchema):
    # Configuration swagger.json

    
    public_key = fields.Str(required=False)
    


class GoogleMap(BaseSchema):
    # Configuration swagger.json

    
    credentials = fields.Nested(GoogleMapCredentials, required=False)
    


class GoogleMapCredentials(BaseSchema):
    # Configuration swagger.json

    
    api_key = fields.Str(required=False)
    


class RewardPointsConfig(BaseSchema):
    # Configuration swagger.json

    
    credit = fields.Nested(Credit, required=False)
    
    debit = fields.Nested(Debit, required=False)
    


class Credit(BaseSchema):
    # Configuration swagger.json

    
    enabled = fields.Boolean(required=False)
    


class Debit(BaseSchema):
    # Configuration swagger.json

    
    enabled = fields.Boolean(required=False)
    
    auto_apply = fields.Boolean(required=False)
    
    strategy_channel = fields.Str(required=False)
    


class ProductDetailFeature(BaseSchema):
    # Configuration swagger.json

    
    similar = fields.List(fields.Str(required=False), required=False)
    
    seller_selection = fields.Boolean(required=False)
    
    update_product_meta = fields.Boolean(required=False)
    
    request_product = fields.Boolean(required=False)
    


class LaunchPage(BaseSchema):
    # Configuration swagger.json

    
    page_type = fields.Str(required=False)
    
    params = fields.Dict(required=False)
    
    query = fields.Dict(required=False)
    


class LandingPageFeature(BaseSchema):
    # Configuration swagger.json

    
    launch_page = fields.Nested(LaunchPage, required=False)
    
    continue_as_guest = fields.Boolean(required=False)
    
    login_btn_text = fields.Str(required=False)
    
    show_domain_textbox = fields.Boolean(required=False)
    
    show_register_btn = fields.Boolean(required=False)
    


class RegistrationPageFeature(BaseSchema):
    # Configuration swagger.json

    
    ask_store_address = fields.Boolean(required=False)
    


class AppFeature(BaseSchema):
    # Configuration swagger.json

    
    product_detail = fields.Nested(ProductDetailFeature, required=False)
    
    landing_page = fields.Nested(LandingPageFeature, required=False)
    
    registration_page = fields.Nested(RegistrationPageFeature, required=False)
    
    home_page = fields.Nested(HomePageFeature, required=False)
    
    common = fields.Nested(CommonFeature, required=False)
    
    cart = fields.Nested(CartFeature, required=False)
    
    qr = fields.Nested(QrFeature, required=False)
    
    pcr = fields.Nested(PcrFeature, required=False)
    
    order = fields.Nested(OrderFeature, required=False)
    
    _id = fields.Str(required=False)
    
    app = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    


class HomePageFeature(BaseSchema):
    # Configuration swagger.json

    
    order_processing = fields.Boolean(required=False)
    


class CommonFeature(BaseSchema):
    # Configuration swagger.json

    
    communication_optin_dialog = fields.Nested(CommunicationOptinDialogFeature, required=False)
    
    deployment_store_selection = fields.Nested(DeploymentStoreSelectionFeature, required=False)
    
    listing_price = fields.Nested(ListingPriceFeature, required=False)
    
    currency = fields.Nested(CurrencyFeature, required=False)
    
    revenue_engine = fields.Nested(RevenueEngineFeature, required=False)
    
    feedback = fields.Nested(FeedbackFeature, required=False)
    
    compare_products = fields.Nested(CompareProductsFeature, required=False)
    
    reward_points = fields.Nested(RewardPointsConfig, required=False)
    


class CommunicationOptinDialogFeature(BaseSchema):
    # Configuration swagger.json

    
    visibility = fields.Boolean(required=False)
    


class DeploymentStoreSelectionFeature(BaseSchema):
    # Configuration swagger.json

    
    enabled = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    


class ListingPriceFeature(BaseSchema):
    # Configuration swagger.json

    
    value = fields.Str(required=False)
    
    sort = fields.Str(required=False)
    


class CurrencyFeature(BaseSchema):
    # Configuration swagger.json

    
    value = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    
    default_currency = fields.Str(required=False)
    


class RevenueEngineFeature(BaseSchema):
    # Configuration swagger.json

    
    enabled = fields.Boolean(required=False)
    


class FeedbackFeature(BaseSchema):
    # Configuration swagger.json

    
    enabled = fields.Boolean(required=False)
    


class CompareProductsFeature(BaseSchema):
    # Configuration swagger.json

    
    enabled = fields.Boolean(required=False)
    


class CartFeature(BaseSchema):
    # Configuration swagger.json

    
    gst_input = fields.Boolean(required=False)
    
    staff_selection = fields.Boolean(required=False)
    
    placing_for_customer = fields.Boolean(required=False)
    
    google_map = fields.Boolean(required=False)
    
    revenue_engine_coupon = fields.Boolean(required=False)
    


class QrFeature(BaseSchema):
    # Configuration swagger.json

    
    application = fields.Boolean(required=False)
    
    products = fields.Boolean(required=False)
    
    collections = fields.Boolean(required=False)
    


class PcrFeature(BaseSchema):
    # Configuration swagger.json

    
    staff_selection = fields.Boolean(required=False)
    


class OrderFeature(BaseSchema):
    # Configuration swagger.json

    
    buy_again = fields.Boolean(required=False)
    


class AppFeatureRequest(BaseSchema):
    # Configuration swagger.json

    
    feature = fields.Nested(AppFeature, required=False)
    


class AppFeatureResponse(BaseSchema):
    # Configuration swagger.json

    
    feature = fields.Nested(AppFeature, required=False)
    


class Currency(BaseSchema):
    # Configuration swagger.json

    
    _id = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    decimal_digits = fields.Int(required=False)
    
    symbol = fields.Str(required=False)
    


class Domain(BaseSchema):
    # Configuration swagger.json

    
    verified = fields.Boolean(required=False)
    
    is_primary = fields.Boolean(required=False)
    
    is_shortlink = fields.Boolean(required=False)
    
    _id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    is_predefined = fields.Boolean(required=False)
    


class ApplicationWebsite(BaseSchema):
    # Configuration swagger.json

    
    enabled = fields.Boolean(required=False)
    
    basepath = fields.Str(required=False)
    


class ApplicationCors(BaseSchema):
    # Configuration swagger.json

    
    domains = fields.List(fields.Str(required=False), required=False)
    


class ApplicationAuth(BaseSchema):
    # Configuration swagger.json

    
    enabled = fields.Boolean(required=False)
    


class ApplicationRedirections(BaseSchema):
    # Configuration swagger.json

    
    redirect_from = fields.Str(required=False)
    
    redirect_to = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class ApplicationMeta(BaseSchema):
    # Configuration swagger.json

    
    name = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class SecureUrl(BaseSchema):
    # Configuration swagger.json

    
    secure_url = fields.Str(required=False)
    


class Application(BaseSchema):
    # Configuration swagger.json

    
    website = fields.Nested(ApplicationWebsite, required=False)
    
    cors = fields.Nested(ApplicationCors, required=False)
    
    auth = fields.Nested(ApplicationAuth, required=False)
    
    description = fields.Str(required=False)
    
    channel_type = fields.Str(required=False)
    
    cache_ttl = fields.Int(required=False)
    
    is_internal = fields.Boolean(required=False)
    
    is_active = fields.Boolean(required=False)
    
    _id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    owner = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    token = fields.Str(required=False)
    
    redirections = fields.List(fields.Nested(ApplicationRedirections, required=False), required=False)
    
    meta = fields.List(fields.Nested(ApplicationMeta, required=False), required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    
    banner = fields.Nested(SecureUrl, required=False)
    
    logo = fields.Nested(SecureUrl, required=False)
    
    favicon = fields.Nested(SecureUrl, required=False)
    
    domains = fields.List(fields.Nested(Domain, required=False), required=False)
    
    app_type = fields.Str(required=False)
    
    mobile_logo = fields.Nested(SecureUrl, required=False)
    
    domain = fields.Nested(Domain, required=False)
    


class NotFound(BaseSchema):
    # Configuration swagger.json

    
    message = fields.Str(required=False)
    


class UnhandledError(BaseSchema):
    # Configuration swagger.json

    
    message = fields.Str(required=False)
    


class InvalidPayloadRequest(BaseSchema):
    # Configuration swagger.json

    
    message = fields.Str(required=False)
    


class SuccessMessageResponse(BaseSchema):
    # Configuration swagger.json

    
    message = fields.Str(required=False)
    


class InventoryBrandRule(BaseSchema):
    # Configuration swagger.json

    
    criteria = fields.Str(required=False)
    
    brands = fields.List(fields.Int(required=False), required=False)
    


class StoreCriteriaRule(BaseSchema):
    # Configuration swagger.json

    
    companies = fields.List(fields.Int(required=False), required=False)
    
    brands = fields.List(fields.Int(required=False), required=False)
    


class InventoryStoreRule(BaseSchema):
    # Configuration swagger.json

    
    criteria = fields.Str(required=False)
    
    rules = fields.List(fields.Nested(StoreCriteriaRule, required=False), required=False)
    
    stores = fields.List(fields.Int(required=False), required=False)
    


class InventoryPaymentConfig(BaseSchema):
    # Configuration swagger.json

    
    mode_of_payment = fields.Str(required=False)
    
    source = fields.Str(required=False)
    


class StorePriorityRule(BaseSchema):
    # Configuration swagger.json

    
    enabled = fields.Boolean(required=False)
    
    storetype_order = fields.List(fields.Str(required=False), required=False)
    


class ArticleAssignmentRule(BaseSchema):
    # Configuration swagger.json

    
    store_priority = fields.Nested(StorePriorityRule, required=False)
    


class InventoryArticleAssignment(BaseSchema):
    # Configuration swagger.json

    
    post_order_reassignment = fields.Boolean(required=False)
    
    rules = fields.Nested(ArticleAssignmentRule, required=False)
    


class CompanyAboutAddress(BaseSchema):
    # Configuration swagger.json

    
    pincode = fields.Int(required=False)
    
    address1 = fields.Str(required=False)
    
    address2 = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    address_type = fields.Str(required=False)
    


class UserEmail(BaseSchema):
    # Configuration swagger.json

    
    active = fields.Boolean(required=False)
    
    primary = fields.Boolean(required=False)
    
    verified = fields.Boolean(required=False)
    
    email = fields.Str(required=False)
    


class UserPhoneNumber(BaseSchema):
    # Configuration swagger.json

    
    active = fields.Boolean(required=False)
    
    primary = fields.Boolean(required=False)
    
    verified = fields.Boolean(required=False)
    
    country_code = fields.Int(required=False)
    
    phone = fields.Str(required=False)
    


class Page(BaseSchema):
    # Configuration swagger.json

    
    type = fields.Str(required=False)
    
    size = fields.Int(required=False)
    
    current = fields.Int(required=False)
    
    has_next = fields.Boolean(required=False)
    
    item_total = fields.Int(required=False)
    
    next_id = fields.Str(required=False)
    
    has_previous = fields.Boolean(required=False)
    


class ApplicationInformation(BaseSchema):
    # Configuration swagger.json

    
    address = fields.Nested(InformationAddress, required=False)
    
    support = fields.Nested(InformationSupport, required=False)
    
    social_links = fields.Nested(SocialLinks, required=False)
    
    links = fields.Nested(Links, required=False)
    
    copyright_text = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    business_highlights = fields.Nested(BusinessHighlights, required=False)
    
    application = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    


class InformationAddress(BaseSchema):
    # Configuration swagger.json

    
    loc = fields.Str(required=False)
    
    address_line = fields.List(fields.Str(required=False), required=False)
    
    phone = fields.Nested(InformationPhone, required=False)
    
    city = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    pincode = fields.Int(required=False)
    


class InformationPhone(BaseSchema):
    # Configuration swagger.json

    
    code = fields.Str(required=False)
    
    number = fields.Str(required=False)
    


class InformationSupport(BaseSchema):
    # Configuration swagger.json

    
    phone = fields.List(fields.Str(required=False), required=False)
    
    email = fields.List(fields.Str(required=False), required=False)
    
    timing = fields.Str(required=False)
    


class SocialLinks(BaseSchema):
    # Configuration swagger.json

    
    facebook = fields.Nested(FacebookLink, required=False)
    
    instagram = fields.Nested(InstagramLink, required=False)
    
    twitter = fields.Nested(TwitterLink, required=False)
    
    pinterest = fields.Nested(PinterestLink, required=False)
    
    google_plus = fields.Nested(GooglePlusLink, required=False)
    
    youtube = fields.Nested(YoutubeLink, required=False)
    
    linked_in = fields.Nested(LinkedInLink, required=False)
    
    vimeo = fields.Nested(VimeoLink, required=False)
    
    blog_link = fields.Nested(BlogLink, required=False)
    


class FacebookLink(BaseSchema):
    # Configuration swagger.json

    
    title = fields.Str(required=False)
    
    icon = fields.Str(required=False)
    
    link = fields.Str(required=False)
    


class InstagramLink(BaseSchema):
    # Configuration swagger.json

    
    title = fields.Str(required=False)
    
    icon = fields.Str(required=False)
    
    link = fields.Str(required=False)
    


class TwitterLink(BaseSchema):
    # Configuration swagger.json

    
    title = fields.Str(required=False)
    
    icon = fields.Str(required=False)
    
    link = fields.Str(required=False)
    


class PinterestLink(BaseSchema):
    # Configuration swagger.json

    
    title = fields.Str(required=False)
    
    icon = fields.Str(required=False)
    
    link = fields.Str(required=False)
    


class GooglePlusLink(BaseSchema):
    # Configuration swagger.json

    
    title = fields.Str(required=False)
    
    icon = fields.Str(required=False)
    
    link = fields.Str(required=False)
    


class YoutubeLink(BaseSchema):
    # Configuration swagger.json

    
    title = fields.Str(required=False)
    
    icon = fields.Str(required=False)
    
    link = fields.Str(required=False)
    


class LinkedInLink(BaseSchema):
    # Configuration swagger.json

    
    title = fields.Str(required=False)
    
    icon = fields.Str(required=False)
    
    link = fields.Str(required=False)
    


class VimeoLink(BaseSchema):
    # Configuration swagger.json

    
    title = fields.Str(required=False)
    
    icon = fields.Str(required=False)
    
    link = fields.Str(required=False)
    


class BlogLink(BaseSchema):
    # Configuration swagger.json

    
    title = fields.Str(required=False)
    
    icon = fields.Str(required=False)
    
    link = fields.Str(required=False)
    


class Links(BaseSchema):
    # Configuration swagger.json

    
    title = fields.Str(required=False)
    
    link = fields.Str(required=False)
    


class BusinessHighlights(BaseSchema):
    # Configuration swagger.json

    
    _id = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    icon = fields.Str(required=False)
    
    sub_title = fields.Str(required=False)
    


class ApplicationDetail(BaseSchema):
    # Configuration swagger.json

    
    name = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    logo = fields.Nested(SecureUrl, required=False)
    
    mobile_logo = fields.Nested(SecureUrl, required=False)
    
    favicon = fields.Nested(SecureUrl, required=False)
    
    banner = fields.Nested(SecureUrl, required=False)
    
    domain = fields.Nested(Domain, required=False)
    
    domains = fields.List(fields.Nested(Domain, required=False), required=False)
    
    _id = fields.Str(required=False)
    


class CurrenciesResponse(BaseSchema):
    # Configuration swagger.json

    
    items = fields.List(fields.Nested(Currency, required=False), required=False)
    


class DefaultCurrency(BaseSchema):
    # Configuration swagger.json

    
    ref = fields.Str(required=False)
    
    code = fields.Str(required=False)
    


class AppCurrencyResponse(BaseSchema):
    # Configuration swagger.json

    
    application = fields.Str(required=False)
    
    default_currency = fields.Nested(DefaultCurrency, required=False)
    
    supported_currency = fields.List(fields.Nested(Currency, required=False), required=False)
    


class StoreLatLong(BaseSchema):
    # Configuration swagger.json

    
    type = fields.Str(required=False)
    
    coordinates = fields.List(fields.Float(required=False), required=False)
    


class OptedStoreAddress(BaseSchema):
    # Configuration swagger.json

    
    state = fields.Str(required=False)
    
    address1 = fields.Str(required=False)
    
    lat_long = fields.Nested(StoreLatLong, required=False)
    
    address2 = fields.Str(required=False)
    
    pincode = fields.Int(required=False)
    
    country = fields.Str(required=False)
    
    city = fields.Str(required=False)
    


class OrderingStore(BaseSchema):
    # Configuration swagger.json

    
    address = fields.Nested(OptedStoreAddress, required=False)
    
    _id = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    store_type = fields.Str(required=False)
    
    store_code = fields.Str(required=False)
    
    pincode = fields.Int(required=False)
    
    code = fields.Str(required=False)
    


class OrderingStores(BaseSchema):
    # Configuration swagger.json

    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(OrderingStore, required=False), required=False)
    
    deployed_stores = fields.List(fields.Int(required=False), required=False)
    
    all_stores = fields.Boolean(required=False)
    
    enabled = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    app = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    


class OrderingStoresResponse(BaseSchema):
    # Configuration swagger.json

    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(OrderingStore, required=False), required=False)
    


