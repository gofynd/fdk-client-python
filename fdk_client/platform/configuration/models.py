"""Configuration Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




class ApplicationInventory(BaseSchema):
    pass


class AppInventoryConfig(BaseSchema):
    pass


class InventoryBrand(BaseSchema):
    pass


class InventoryStore(BaseSchema):
    pass


class AppStoreRules(BaseSchema):
    pass


class InventoryCategory(BaseSchema):
    pass


class InventoryPrice(BaseSchema):
    pass


class InventoryDiscount(BaseSchema):
    pass


class AuthenticationConfig(BaseSchema):
    pass


class ArticleAssignmentConfig(BaseSchema):
    pass


class ArticleAssignmentRules(BaseSchema):
    pass


class StorePriority(BaseSchema):
    pass


class AppCartConfig(BaseSchema):
    pass


class DeliveryCharges(BaseSchema):
    pass


class Charges(BaseSchema):
    pass


class AppPaymentConfig(BaseSchema):
    pass


class CallbackUrl(BaseSchema):
    pass


class Methods(BaseSchema):
    pass


class PaymentModeConfig(BaseSchema):
    pass


class PaymentSelectionLock(BaseSchema):
    pass


class AppOrderConfig(BaseSchema):
    pass


class AppLogisticsConfig(BaseSchema):
    pass


class LoyaltyPointsConfig(BaseSchema):
    pass


class AppInventoryPartialUpdate(BaseSchema):
    pass


class BrandCompanyInfo(BaseSchema):
    pass


class CompanyByBrandsRequest(BaseSchema):
    pass


class CompanyByBrandsResponse(BaseSchema):
    pass


class StoreByBrandsRequest(BaseSchema):
    pass


class StoreByBrandsResponse(BaseSchema):
    pass


class BrandStoreInfo(BaseSchema):
    pass


class CompanyBrandInfo(BaseSchema):
    pass


class BrandsByCompanyResponse(BaseSchema):
    pass


class PanCardConfig(BaseSchema):
    pass


class CommunicationConfig(BaseSchema):
    pass


class CommsConfig(BaseSchema):
    pass


class CreateApplicationRequest(BaseSchema):
    pass


class CreateAppResponse(BaseSchema):
    pass


class ApplicationsResponse(BaseSchema):
    pass


class MobileAppConfiguration(BaseSchema):
    pass


class LandingImage(BaseSchema):
    pass


class SplashImage(BaseSchema):
    pass


class MobileAppConfigRequest(BaseSchema):
    pass


class BuildVersionHistory(BaseSchema):
    pass


class BuildVersion(BaseSchema):
    pass


class AppSupportedCurrency(BaseSchema):
    pass


class DefaultCurrency(BaseSchema):
    pass


class CurrencyConfig(BaseSchema):
    pass


class DomainAdd(BaseSchema):
    pass


class DomainAddRequest(BaseSchema):
    pass


class DomainsResponse(BaseSchema):
    pass


class UpdateDomain(BaseSchema):
    pass


class UpdateDomainTypeRequest(BaseSchema):
    pass


class DomainStatusRequest(BaseSchema):
    pass


class DomainStatus(BaseSchema):
    pass


class DomainStatusResponse(BaseSchema):
    pass


class DomainSuggestionsRequest(BaseSchema):
    pass


class DomainSuggestion(BaseSchema):
    pass


class DomainSuggestionsResponse(BaseSchema):
    pass


class GetIntegrationsOptInsResponse(BaseSchema):
    pass


class IntegrationOptIn(BaseSchema):
    pass


class Validators(BaseSchema):
    pass


class CompanyValidator(BaseSchema):
    pass


class JsonSchema(BaseSchema):
    pass


class StoreValidator(BaseSchema):
    pass


class InventoryValidator(BaseSchema):
    pass


class OrderValidator(BaseSchema):
    pass


class IntegrationMeta(BaseSchema):
    pass


class Integration(BaseSchema):
    pass


class IntegrationConfigResponse(BaseSchema):
    pass


class IntegrationLevel(BaseSchema):
    pass


class UpdateIntegrationLevelRequest(BaseSchema):
    pass


class OptedStoreIntegration(BaseSchema):
    pass


class OtherEntity(BaseSchema):
    pass


class LastPatch(BaseSchema):
    pass


class OtherEntityData(BaseSchema):
    pass


class App(BaseSchema):
    pass


class AppInventory(BaseSchema):
    pass


class AppDomain(BaseSchema):
    pass


class CompaniesResponse(BaseSchema):
    pass


class AppInventoryCompanies(BaseSchema):
    pass


class StoresResponse(BaseSchema):
    pass


class AppInventoryStores(BaseSchema):
    pass


class FilterOrderingStoreRequest(BaseSchema):
    pass


class DeploymentMeta(BaseSchema):
    pass


class OrderingStoreConfig(BaseSchema):
    pass


class OtherSellerCompany(BaseSchema):
    pass


class OtherSellerApplication(BaseSchema):
    pass


class OtherSellerApplications(BaseSchema):
    pass


class OptedApplicationResponse(BaseSchema):
    pass


class OptedCompany(BaseSchema):
    pass


class OptedInventory(BaseSchema):
    pass


class OptType(BaseSchema):
    pass


class OptedStore(BaseSchema):
    pass


class OptOutInventory(BaseSchema):
    pass


class TokenResponse(BaseSchema):
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





class ApplicationInventory(BaseSchema):
    # Configuration swagger.json

    
    inventory = fields.Nested(AppInventoryConfig, required=False)
    
    authentication = fields.Nested(AuthenticationConfig, required=False)
    
    article_assignment = fields.Nested(ArticleAssignmentConfig, required=False)
    
    reward_points = fields.Nested(RewardPointsConfig, required=False)
    
    cart = fields.Nested(AppCartConfig, required=False)
    
    payment = fields.Nested(AppPaymentConfig, required=False)
    
    order = fields.Nested(AppOrderConfig, required=False)
    
    logistics = fields.Nested(AppLogisticsConfig, required=False)
    
    business = fields.Str(required=False)
    
    comms_enabled = fields.Boolean(required=False)
    
    communication = fields.Nested(CommunicationConfig, required=False)
    
    platforms = fields.List(fields.Str(required=False), required=False)
    
    _id = fields.Str(required=False)
    
    loyalty_points = fields.Nested(LoyaltyPointsConfig, required=False)
    
    app = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    modified_by = fields.Str(required=False)
    


class AppInventoryConfig(BaseSchema):
    # Configuration swagger.json

    
    brand = fields.Nested(InventoryBrand, required=False)
    
    store = fields.Nested(InventoryStore, required=False)
    
    category = fields.Nested(InventoryCategory, required=False)
    
    price = fields.Nested(InventoryPrice, required=False)
    
    discount = fields.Nested(InventoryDiscount, required=False)
    
    out_of_stock = fields.Boolean(required=False)
    
    only_verified_products = fields.Boolean(required=False)
    
    franchise_enabled = fields.Boolean(required=False)
    
    exclude_category = fields.List(fields.Raw(required=False), required=False)
    
    image = fields.List(fields.Str(required=False), required=False)
    
    company_store = fields.List(fields.Raw(required=False), required=False)
    


class InventoryBrand(BaseSchema):
    # Configuration swagger.json

    
    criteria = fields.Str(required=False)
    
    brands = fields.List(fields.Raw(required=False), required=False)
    


class InventoryStore(BaseSchema):
    # Configuration swagger.json

    
    criteria = fields.Str(required=False)
    
    stores = fields.List(fields.Raw(required=False), required=False)
    
    rules = fields.Nested(AppStoreRules, required=False)
    


class AppStoreRules(BaseSchema):
    # Configuration swagger.json

    
    companies = fields.List(fields.Int(required=False), required=False)
    
    brands = fields.List(fields.Raw(required=False), required=False)
    


class InventoryCategory(BaseSchema):
    # Configuration swagger.json

    
    criteria = fields.Str(required=False)
    
    categories = fields.List(fields.Raw(required=False), required=False)
    


class InventoryPrice(BaseSchema):
    # Configuration swagger.json

    
    min = fields.Float(required=False)
    
    max = fields.Float(required=False)
    


class InventoryDiscount(BaseSchema):
    # Configuration swagger.json

    
    min = fields.Float(required=False)
    
    max = fields.Float(required=False)
    


class AuthenticationConfig(BaseSchema):
    # Configuration swagger.json

    
    required = fields.Boolean(required=False)
    
    provider = fields.Str(required=False)
    


class ArticleAssignmentConfig(BaseSchema):
    # Configuration swagger.json

    
    rules = fields.Nested(ArticleAssignmentRules, required=False)
    
    post_order_reassignment = fields.Boolean(required=False)
    


class ArticleAssignmentRules(BaseSchema):
    # Configuration swagger.json

    
    store_priority = fields.Nested(StorePriority, required=False)
    


class StorePriority(BaseSchema):
    # Configuration swagger.json

    
    enabled = fields.Boolean(required=False)
    
    storetype_order = fields.List(fields.Raw(required=False), required=False)
    


class AppCartConfig(BaseSchema):
    # Configuration swagger.json

    
    delivery_charges = fields.Nested(DeliveryCharges, required=False)
    
    enabled = fields.Boolean(required=False)
    
    max_cart_items = fields.Int(required=False)
    
    min_cart_value = fields.Float(required=False)
    
    bulk_coupons = fields.Boolean(required=False)
    
    revenue_engine_coupon = fields.Boolean(required=False)
    
    empty_cart = fields.Boolean(required=False)
    
    pan_card = fields.Nested(PanCardConfig, required=False)
    


class DeliveryCharges(BaseSchema):
    # Configuration swagger.json

    
    enabled = fields.Boolean(required=False)
    
    charges = fields.Nested(Charges, required=False)
    


class Charges(BaseSchema):
    # Configuration swagger.json

    
    threshold = fields.Float(required=False)
    
    charges = fields.Float(required=False)
    


class AppPaymentConfig(BaseSchema):
    # Configuration swagger.json

    
    callback_url = fields.Nested(CallbackUrl, required=False)
    
    methods = fields.Nested(Methods, required=False)
    
    payment_selection_lock = fields.Nested(PaymentSelectionLock, required=False)
    
    mode_of_payment = fields.Str(required=False)
    
    source = fields.Str(required=False)
    
    enabled = fields.Boolean(required=False)
    
    cod_amount_limit = fields.Float(required=False)
    
    cod_charges = fields.Float(required=False)
    


class CallbackUrl(BaseSchema):
    # Configuration swagger.json

    
    app = fields.Str(required=False)
    
    web = fields.Str(required=False)
    


class Methods(BaseSchema):
    # Configuration swagger.json

    
    pl = fields.Nested(PaymentModeConfig, required=False)
    
    card = fields.Nested(PaymentModeConfig, required=False)
    
    nb = fields.Nested(PaymentModeConfig, required=False)
    
    wl = fields.Nested(PaymentModeConfig, required=False)
    
    ps = fields.Nested(PaymentModeConfig, required=False)
    
    upi = fields.Nested(PaymentModeConfig, required=False)
    
    qr = fields.Nested(PaymentModeConfig, required=False)
    
    cod = fields.Nested(PaymentModeConfig, required=False)
    
    pp = fields.Nested(PaymentModeConfig, required=False)
    
    jp = fields.Nested(PaymentModeConfig, required=False)
    
    pac = fields.Nested(PaymentModeConfig, required=False)
    
    fc = fields.Nested(PaymentModeConfig, required=False)
    
    jiopp = fields.Nested(PaymentModeConfig, required=False)
    
    stripepg = fields.Nested(PaymentModeConfig, required=False)
    
    juspaypg = fields.Nested(PaymentModeConfig, required=False)
    
    payubizpg = fields.Nested(PaymentModeConfig, required=False)
    
    payumoneypg = fields.Nested(PaymentModeConfig, required=False)
    
    rupifipg = fields.Nested(PaymentModeConfig, required=False)
    
    simpl = fields.Nested(PaymentModeConfig, required=False)
    


class PaymentModeConfig(BaseSchema):
    # Configuration swagger.json

    
    enabled = fields.Boolean(required=False)
    


class PaymentSelectionLock(BaseSchema):
    # Configuration swagger.json

    
    enabled = fields.Boolean(required=False)
    
    default_options = fields.Str(required=False)
    
    payment_identifier = fields.Str(required=False)
    


class AppOrderConfig(BaseSchema):
    # Configuration swagger.json

    
    enabled = fields.Boolean(required=False)
    
    force_reassignment = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class AppLogisticsConfig(BaseSchema):
    # Configuration swagger.json

    
    logistics_by_seller = fields.Boolean(required=False)
    
    serviceability_check = fields.Boolean(required=False)
    
    same_day_delivery = fields.Boolean(required=False)
    
    dp_assignment = fields.Boolean(required=False)
    


class LoyaltyPointsConfig(BaseSchema):
    # Configuration swagger.json

    
    enabled = fields.Boolean(required=False)
    
    auto_apply = fields.Boolean(required=False)
    


class AppInventoryPartialUpdate(BaseSchema):
    # Configuration swagger.json

    
    reward_points = fields.Nested(RewardPointsConfig, required=False)
    
    cart = fields.Nested(AppCartConfig, required=False)
    
    payment = fields.Nested(AppPaymentConfig, required=False)
    
    loyalty_points = fields.Nested(LoyaltyPointsConfig, required=False)
    
    comms_enabled = fields.Boolean(required=False)
    
    communication = fields.Nested(CommunicationConfig, required=False)
    


class BrandCompanyInfo(BaseSchema):
    # Configuration swagger.json

    
    company_name = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    


class CompanyByBrandsRequest(BaseSchema):
    # Configuration swagger.json

    
    brands = fields.Int(required=False)
    
    search_text = fields.Str(required=False)
    


class CompanyByBrandsResponse(BaseSchema):
    # Configuration swagger.json

    
    items = fields.List(fields.Nested(BrandCompanyInfo, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class StoreByBrandsRequest(BaseSchema):
    # Configuration swagger.json

    
    company_id = fields.Int(required=False)
    
    brands = fields.Int(required=False)
    
    search_text = fields.Str(required=False)
    


class StoreByBrandsResponse(BaseSchema):
    # Configuration swagger.json

    
    items = fields.List(fields.Nested(BrandStoreInfo, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class BrandStoreInfo(BaseSchema):
    # Configuration swagger.json

    
    store_name = fields.Str(required=False)
    
    store_id = fields.Int(required=False)
    
    store_type = fields.Str(required=False)
    
    store_code = fields.Str(required=False)
    
    store_address = fields.Nested(OptedStoreAddress, required=False)
    
    company = fields.Nested(OptedCompany, required=False)
    


class CompanyBrandInfo(BaseSchema):
    # Configuration swagger.json

    
    name = fields.Str(required=False)
    
    value = fields.Int(required=False)
    
    brand_logo_url = fields.Str(required=False)
    
    brand_banner_url = fields.Str(required=False)
    
    brand_banner_portrait_url = fields.Str(required=False)
    


class BrandsByCompanyResponse(BaseSchema):
    # Configuration swagger.json

    
    brands = fields.Nested(CompanyBrandInfo, required=False)
    


class PanCardConfig(BaseSchema):
    # Configuration swagger.json

    
    enabled = fields.Boolean(required=False)
    
    threshold_amount = fields.Float(required=False)
    


class CommunicationConfig(BaseSchema):
    # Configuration swagger.json

    
    email = fields.Nested(CommsConfig, required=False)
    
    sms = fields.Nested(CommsConfig, required=False)
    
    voice = fields.Nested(CommsConfig, required=False)
    


class CommsConfig(BaseSchema):
    # Configuration swagger.json

    
    enabled = fields.Boolean(required=False)
    


class CreateApplicationRequest(BaseSchema):
    # Configuration swagger.json

    
    app = fields.Nested(App, required=False)
    
    configuration = fields.Nested(AppInventory, required=False)
    
    domain = fields.Nested(AppDomain, required=False)
    


class CreateAppResponse(BaseSchema):
    # Configuration swagger.json

    
    app = fields.Nested(Application, required=False)
    
    configuration = fields.Nested(ApplicationInventory, required=False)
    


class ApplicationsResponse(BaseSchema):
    # Configuration swagger.json

    
    items = fields.List(fields.Nested(Application, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class MobileAppConfiguration(BaseSchema):
    # Configuration swagger.json

    
    is_active = fields.Boolean(required=False)
    
    _id = fields.Str(required=False)
    
    app_name = fields.Str(required=False)
    
    landing_image = fields.Nested(LandingImage, required=False)
    
    splash_image = fields.Nested(SplashImage, required=False)
    
    application = fields.Str(required=False)
    
    platform_type = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    
    package_name = fields.Str(required=False)
    


class LandingImage(BaseSchema):
    # Configuration swagger.json

    
    aspect_ratio = fields.Str(required=False)
    
    secure_url = fields.Str(required=False)
    


class SplashImage(BaseSchema):
    # Configuration swagger.json

    
    aspect_ratio = fields.Str(required=False)
    
    secure_url = fields.Str(required=False)
    


class MobileAppConfigRequest(BaseSchema):
    # Configuration swagger.json

    
    app_name = fields.Str(required=False)
    
    landing_image = fields.Nested(LandingImage, required=False)
    
    splash_image = fields.Nested(SplashImage, required=False)
    
    is_active = fields.Boolean(required=False)
    


class BuildVersionHistory(BaseSchema):
    # Configuration swagger.json

    
    versions = fields.Nested(BuildVersion, required=False)
    
    latest_available_version_name = fields.Str(required=False)
    


class BuildVersion(BaseSchema):
    # Configuration swagger.json

    
    _id = fields.Str(required=False)
    
    application = fields.Str(required=False)
    
    platform_type = fields.Str(required=False)
    
    build_status = fields.Str(required=False)
    
    version_name = fields.Str(required=False)
    
    version_code = fields.Int(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    


class AppSupportedCurrency(BaseSchema):
    # Configuration swagger.json

    
    _id = fields.Str(required=False)
    
    supported_currency = fields.List(fields.Str(required=False), required=False)
    
    application = fields.Str(required=False)
    
    default_currency = fields.Nested(DefaultCurrency, required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    


class DefaultCurrency(BaseSchema):
    # Configuration swagger.json

    
    ref = fields.Str(required=False)
    
    code = fields.Str(required=False)
    


class CurrencyConfig(BaseSchema):
    # Configuration swagger.json

    
    _id = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    decimal_digits = fields.Int(required=False)
    
    symbol = fields.Str(required=False)
    


class DomainAdd(BaseSchema):
    # Configuration swagger.json

    
    name = fields.Str(required=False)
    


class DomainAddRequest(BaseSchema):
    # Configuration swagger.json

    
    domain = fields.Nested(DomainAdd, required=False)
    


class DomainsResponse(BaseSchema):
    # Configuration swagger.json

    
    domains = fields.List(fields.Nested(Domain, required=False), required=False)
    


class UpdateDomain(BaseSchema):
    # Configuration swagger.json

    
    _id = fields.Str(required=False)
    


class UpdateDomainTypeRequest(BaseSchema):
    # Configuration swagger.json

    
    domain = fields.Nested(UpdateDomain, required=False)
    
    action = fields.Str(required=False)
    


class DomainStatusRequest(BaseSchema):
    # Configuration swagger.json

    
    domain_url = fields.Str(required=False)
    


class DomainStatus(BaseSchema):
    # Configuration swagger.json

    
    display = fields.Str(required=False)
    
    status = fields.Boolean(required=False)
    


class DomainStatusResponse(BaseSchema):
    # Configuration swagger.json

    
    connected = fields.Boolean(required=False)
    
    status = fields.List(fields.Nested(DomainStatus, required=False), required=False)
    


class DomainSuggestionsRequest(BaseSchema):
    # Configuration swagger.json

    
    domain_url = fields.Str(required=False)
    
    custom = fields.Boolean(required=False)
    


class DomainSuggestion(BaseSchema):
    # Configuration swagger.json

    
    name = fields.Str(required=False)
    
    unsupported = fields.Boolean(required=False)
    
    is_available = fields.Boolean(required=False)
    
    price = fields.Float(required=False)
    
    currency = fields.Str(required=False)
    


class DomainSuggestionsResponse(BaseSchema):
    # Configuration swagger.json

    
    domains = fields.List(fields.Nested(DomainSuggestion, required=False), required=False)
    


class GetIntegrationsOptInsResponse(BaseSchema):
    # Configuration swagger.json

    
    items = fields.List(fields.Nested(IntegrationOptIn, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class IntegrationOptIn(BaseSchema):
    # Configuration swagger.json

    
    validators = fields.Nested(Validators, required=False)
    
    description = fields.Str(required=False)
    
    description_html = fields.Str(required=False)
    
    constants = fields.Str(required=False)
    
    companies = fields.List(fields.Dict(required=False), required=False)
    
    support = fields.List(fields.Str(required=False), required=False)
    
    _id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    meta = fields.List(fields.Nested(IntegrationMeta, required=False), required=False)
    
    icon = fields.Str(required=False)
    
    owner = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    token = fields.Str(required=False)
    
    secret = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    


class Validators(BaseSchema):
    # Configuration swagger.json

    
    company = fields.Nested(CompanyValidator, required=False)
    
    store = fields.Nested(StoreValidator, required=False)
    
    inventory = fields.Nested(InventoryValidator, required=False)
    
    order = fields.Nested(OrderValidator, required=False)
    


class CompanyValidator(BaseSchema):
    # Configuration swagger.json

    
    json_schema = fields.List(fields.Nested(JsonSchema, required=False), required=False)
    
    browser_script = fields.Str(required=False)
    


class JsonSchema(BaseSchema):
    # Configuration swagger.json

    
    display = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    tooltip = fields.Str(required=False)
    


class StoreValidator(BaseSchema):
    # Configuration swagger.json

    
    json_schema = fields.List(fields.Nested(JsonSchema, required=False), required=False)
    
    browser_script = fields.Str(required=False)
    


class InventoryValidator(BaseSchema):
    # Configuration swagger.json

    
    json_schema = fields.List(fields.Nested(JsonSchema, required=False), required=False)
    
    browser_script = fields.Str(required=False)
    


class OrderValidator(BaseSchema):
    # Configuration swagger.json

    
    json_schema = fields.List(fields.Nested(JsonSchema, required=False), required=False)
    
    browser_script = fields.Str(required=False)
    


class IntegrationMeta(BaseSchema):
    # Configuration swagger.json

    
    is_public = fields.Boolean(required=False)
    
    _id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class Integration(BaseSchema):
    # Configuration swagger.json

    
    validators = fields.Nested(Validators, required=False)
    
    description = fields.Str(required=False)
    
    description_html = fields.Str(required=False)
    
    constants = fields.Dict(required=False)
    
    companies = fields.List(fields.Dict(required=False), required=False)
    
    support = fields.List(fields.Str(required=False), required=False)
    
    _id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    meta = fields.List(fields.Nested(IntegrationMeta, required=False), required=False)
    
    icon = fields.Str(required=False)
    
    owner = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    token = fields.Str(required=False)
    
    secret = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    


class IntegrationConfigResponse(BaseSchema):
    # Configuration swagger.json

    
    items = fields.List(fields.Nested(IntegrationLevel, required=False), required=False)
    


class IntegrationLevel(BaseSchema):
    # Configuration swagger.json

    
    opted = fields.Boolean(required=False)
    
    permissions = fields.List(fields.Dict(required=False), required=False)
    
    last_patch = fields.List(fields.Nested(LastPatch, required=False), required=False)
    
    _id = fields.Str(required=False)
    
    integration = fields.Str(required=False)
    
    level = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    meta = fields.List(fields.Nested(IntegrationMeta, required=False), required=False)
    
    token = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    
    data = fields.Dict(required=False)
    


class UpdateIntegrationLevelRequest(BaseSchema):
    # Configuration swagger.json

    
    items = fields.List(fields.Nested(IntegrationLevel, required=False), required=False)
    


class OptedStoreIntegration(BaseSchema):
    # Configuration swagger.json

    
    other_opted = fields.Boolean(required=False)
    
    other_integration = fields.Nested(IntegrationOptIn, required=False)
    
    other_entity = fields.Nested(OtherEntity, required=False)
    


class OtherEntity(BaseSchema):
    # Configuration swagger.json

    
    opted = fields.Boolean(required=False)
    
    permissions = fields.List(fields.Str(required=False), required=False)
    
    last_patch = fields.List(fields.Nested(LastPatch, required=False), required=False)
    
    _id = fields.Str(required=False)
    
    integration = fields.Str(required=False)
    
    level = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    data = fields.Nested(OtherEntityData, required=False)
    
    meta = fields.List(fields.Dict(required=False), required=False)
    
    token = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    


class LastPatch(BaseSchema):
    # Configuration swagger.json

    
    op = fields.Str(required=False)
    
    path = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class OtherEntityData(BaseSchema):
    # Configuration swagger.json

    
    article_identifier = fields.Str(required=False)
    


class App(BaseSchema):
    # Configuration swagger.json

    
    company_id = fields.Str(required=False)
    
    channel_type = fields.Str(required=False)
    
    auth = fields.Nested(ApplicationAuth, required=False)
    
    name = fields.Str(required=False)
    
    desc = fields.Str(required=False)
    


class AppInventory(BaseSchema):
    # Configuration swagger.json

    
    brand = fields.Nested(InventoryBrandRule, required=False)
    
    store = fields.Nested(InventoryStoreRule, required=False)
    
    image = fields.List(fields.Str(required=False), required=False)
    
    franchise_enabled = fields.Boolean(required=False)
    
    out_of_stock = fields.Boolean(required=False)
    
    only_verified_products = fields.Boolean(required=False)
    
    payment = fields.Nested(InventoryPaymentConfig, required=False)
    
    article_assignment = fields.Nested(InventoryArticleAssignment, required=False)
    


class AppDomain(BaseSchema):
    # Configuration swagger.json

    
    name = fields.Str(required=False)
    


class CompaniesResponse(BaseSchema):
    # Configuration swagger.json

    
    items = fields.Nested(AppInventoryCompanies, required=False)
    
    page = fields.Nested(Page, required=False)
    


class AppInventoryCompanies(BaseSchema):
    # Configuration swagger.json

    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    company_type = fields.Str(required=False)
    


class StoresResponse(BaseSchema):
    # Configuration swagger.json

    
    items = fields.Nested(AppInventoryStores, required=False)
    
    page = fields.Nested(Page, required=False)
    


class AppInventoryStores(BaseSchema):
    # Configuration swagger.json

    
    _id = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    store_type = fields.Str(required=False)
    
    store_code = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    


class FilterOrderingStoreRequest(BaseSchema):
    # Configuration swagger.json

    
    all_stores = fields.Boolean(required=False)
    
    deployed_stores = fields.List(fields.Int(required=False), required=False)
    
    q = fields.Str(required=False)
    
    only_deployed = fields.Boolean(required=False)
    


class DeploymentMeta(BaseSchema):
    # Configuration swagger.json

    
    deployed_stores = fields.List(fields.Int(required=False), required=False)
    
    all_stores = fields.Boolean(required=False)
    
    enabled = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    app = fields.Str(required=False)
    


class OrderingStoreConfig(BaseSchema):
    # Configuration swagger.json

    
    deployment_meta = fields.Nested(DeploymentMeta, required=False)
    


class OtherSellerCompany(BaseSchema):
    # Configuration swagger.json

    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    


class OtherSellerApplication(BaseSchema):
    # Configuration swagger.json

    
    name = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    domain = fields.Str(required=False)
    
    company = fields.Nested(OtherSellerCompany, required=False)
    
    opt_type = fields.Str(required=False)
    


class OtherSellerApplications(BaseSchema):
    # Configuration swagger.json

    
    items = fields.List(fields.Nested(OtherSellerApplication, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class OptedApplicationResponse(BaseSchema):
    # Configuration swagger.json

    
    name = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    domain = fields.Str(required=False)
    
    company = fields.Nested(OptedCompany, required=False)
    
    opted_inventory = fields.Nested(OptedInventory, required=False)
    
    opt_out_inventory = fields.Nested(OptOutInventory, required=False)
    


class OptedCompany(BaseSchema):
    # Configuration swagger.json

    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    


class OptedInventory(BaseSchema):
    # Configuration swagger.json

    
    opt_type = fields.Nested(OptType, required=False)
    
    items = fields.Raw(required=False)
    


class OptType(BaseSchema):
    # Configuration swagger.json

    
    key = fields.Str(required=False)
    
    display = fields.Str(required=False)
    


class OptedStore(BaseSchema):
    # Configuration swagger.json

    
    name = fields.Str(required=False)
    
    store_code = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    address = fields.Nested(OptedStoreAddress, required=False)
    
    display_name = fields.Str(required=False)
    
    store_type = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    


class OptOutInventory(BaseSchema):
    # Configuration swagger.json

    
    store = fields.List(fields.Int(required=False), required=False)
    
    company = fields.List(fields.Int(required=False), required=False)
    


class TokenResponse(BaseSchema):
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
    
    slug = fields.Str(required=False)
    


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

    
    item_total = fields.Int(required=False)
    
    next_id = fields.Str(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    has_next = fields.Boolean(required=False)
    
    current = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    size = fields.Int(required=False)
    


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
    
    phone = fields.List(fields.Nested(InformationPhone, required=False), required=False)
    
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
    
    slug = fields.Str(required=False)
    


class CurrenciesResponse(BaseSchema):
    # Configuration swagger.json

    
    items = fields.List(fields.Nested(Currency, required=False), required=False)
    


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
    


