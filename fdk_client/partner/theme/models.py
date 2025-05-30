"""Theme Partner Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PartnerModel import BaseSchema


from .enums import *



class AvailablePageSchema(BaseSchema):
    pass


class DraftExtensionSectionRequest(BaseSchema):
    pass


class DraftExtensionSectionResponse(BaseSchema):
    pass


class SectionsResponse(BaseSchema):
    pass


class ExtensionSection(BaseSchema):
    pass


class PropExtension(BaseSchema):
    pass


class AssetsExtension(BaseSchema):
    pass


class PublishExtensionSectionRequest(BaseSchema):
    pass


class ExtensionPreviewRequest(BaseSchema):
    pass


class ExtensionPreviewResponse(BaseSchema):
    pass


class PublishExtensionSectionResponse(BaseSchema):
    pass


class AvailablePageSectionMetaAttributes(BaseSchema):
    pass


class AvailablePageSeo(BaseSchema):
    pass


class SEOMetaItem(BaseSchema):
    pass


class SEOMetaItems(BaseSchema):
    pass


class SEOSitemap(BaseSchema):
    pass


class SEObreadcrumb(BaseSchema):
    pass


class Action(BaseSchema):
    pass


class AvailablePageSchemaSections(BaseSchema):
    pass


class AvailablePageScreenPredicate(BaseSchema):
    pass


class AvailablePageUserPredicate(BaseSchema):
    pass


class AvailablePageRoutePredicate(BaseSchema):
    pass


class AvailablePagePlatformPredicate(BaseSchema):
    pass


class AvailablePageSchedulePredicate(BaseSchema):
    pass


class AvailablePagePredicate(BaseSchema):
    pass


class MarketplaceThemeSchema(BaseSchema):
    pass


class MarketplaceTheme(BaseSchema):
    pass


class PaymentInfo(BaseSchema):
    pass


class ContactInfo(BaseSchema):
    pass


class CatalogSize(BaseSchema):
    pass


class MarketplaceThemeImages(BaseSchema):
    pass


class CarouselItem(BaseSchema):
    pass


class ExploreInfo(BaseSchema):
    pass


class Feature(BaseSchema):
    pass


class FeatureItem(BaseSchema):
    pass


class Highlight(BaseSchema):
    pass


class Variation(BaseSchema):
    pass


class Documentation(BaseSchema):
    pass


class Comments(BaseSchema):
    pass


class ThemeRejectionReasons(BaseSchema):
    pass


class AllAvailablePageSchema(BaseSchema):
    pass


class PaginationSchema(BaseSchema):
    pass


class BlitzkriegApiErrorSchema(BaseSchema):
    pass


class BlitzkriegInternalServerErrorSchema(BaseSchema):
    pass


class ThemesSchema(BaseSchema):
    pass


class Font(BaseSchema):
    pass


class FontVariants(BaseSchema):
    pass


class FontVariant(BaseSchema):
    pass


class Config(BaseSchema):
    pass


class ThemeConfiguration(BaseSchema):
    pass


class OverlayPopup(BaseSchema):
    pass


class DividerStrokeHighlight(BaseSchema):
    pass


class UserAlerts(BaseSchema):
    pass


class OrderTracking(BaseSchema):
    pass


class ThemeConfigListPage(BaseSchema):
    pass


class ThemeConfigListPageSettingsProps(BaseSchema):
    pass


class CustomConfig(BaseSchema):
    pass


class CustomProps(BaseSchema):
    pass


class ThemeMeta(BaseSchema):
    pass


class ThemePayment(BaseSchema):
    pass


class Release(BaseSchema):
    pass


class Images(BaseSchema):
    pass


class Assets(BaseSchema):
    pass


class UMDJs(BaseSchema):
    pass


class CommonJS(BaseSchema):
    pass


class CSS(BaseSchema):
    pass


class SectionItem(BaseSchema):
    pass


class GlobalSchema(BaseSchema):
    pass


class Preset(BaseSchema):
    pass


class Page(BaseSchema):
    pass


class SectionProps(BaseSchema):
    pass


class SectionPreset(BaseSchema):
    pass


class ImagePickerProp(BaseSchema):
    pass


class UrlProp(BaseSchema):
    pass


class BlockProps(BaseSchema):
    pass


class TextProp(BaseSchema):
    pass


class CheckboxProp(BaseSchema):
    pass


class RangeProp(BaseSchema):
    pass


class Section(BaseSchema):
    pass


class Block(BaseSchema):
    pass


class Predicate(BaseSchema):
    pass


class Screen(BaseSchema):
    pass


class ThemeUserSchema(BaseSchema):
    pass


class Route(BaseSchema):
    pass


class UpdateThemeRequestBody(BaseSchema):
    pass


class CreateNewTheme(BaseSchema):
    pass


class ActionPage(BaseSchema):
    pass





class AvailablePageSchema(BaseSchema):
    # Theme swagger.json

    
    value = fields.Str(required=False)
    
    text = fields.Str(required=False)
    
    path = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    sections = fields.List(fields.Nested(AvailablePageSchemaSections, required=False), required=False)
    
    sections_meta = fields.List(fields.Nested(AvailablePageSectionMetaAttributes, required=False), required=False)
    
    theme = fields.Str(required=False)
    
    seo = fields.Nested(AvailablePageSeo, required=False)
    
    props = fields.List(fields.Dict(required=False), required=False)
    
    _id = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    


class DraftExtensionSectionRequest(BaseSchema):
    # Theme swagger.json

    
    extension_id = fields.Str(required=False)
    
    bundle_name = fields.Str(required=False)
    
    organization_id = fields.Str(required=False)
    
    sections = fields.List(fields.Nested(ExtensionSection, required=False), required=False)
    
    assets = fields.Nested(AssetsExtension, required=False)
    
    type = fields.Str(required=False)
    
    status = fields.Str(required=False)
    


class DraftExtensionSectionResponse(BaseSchema):
    # Theme swagger.json

    
    sections = fields.Nested(SectionsResponse, required=False)
    


class SectionsResponse(BaseSchema):
    # Theme swagger.json

    
    acknowledged = fields.Boolean(required=False)
    
    matched_count = fields.Int(required=False)
    
    modified_count = fields.Int(required=False)
    
    upserted_id = fields.Str(required=False)
    
    upserted_count = fields.Int(required=False)
    


class ExtensionSection(BaseSchema):
    # Theme swagger.json

    
    label = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    props = fields.List(fields.Nested(PropExtension, required=False), required=False)
    
    blocks = fields.List(fields.Dict(required=False), required=False)
    


class PropExtension(BaseSchema):
    # Theme swagger.json

    
    id = fields.Str(required=False)
    
    label = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    info = fields.Str(required=False)
    


class AssetsExtension(BaseSchema):
    # Theme swagger.json

    
    js = fields.Str(required=False)
    
    css = fields.Str(required=False)
    


class PublishExtensionSectionRequest(BaseSchema):
    # Theme swagger.json

    
    extension_id = fields.Str(required=False)
    
    bundle_name = fields.Str(required=False)
    
    organization_id = fields.Str(required=False)
    
    sections = fields.List(fields.Nested(ExtensionSection, required=False), required=False)
    
    assets = fields.Nested(AssetsExtension, required=False)
    
    type = fields.Str(required=False)
    
    status = fields.Str(required=False)
    


class ExtensionPreviewRequest(BaseSchema):
    # Theme swagger.json

    
    application_id = fields.Str(required=False)
    
    section_preview_hash = fields.Str(required=False)
    


class ExtensionPreviewResponse(BaseSchema):
    # Theme swagger.json

    
    message = fields.Str(required=False)
    


class PublishExtensionSectionResponse(BaseSchema):
    # Theme swagger.json

    
    sections = fields.Nested(SectionsResponse, required=False)
    


class AvailablePageSectionMetaAttributes(BaseSchema):
    # Theme swagger.json

    
    attributes = fields.Dict(required=False)
    


class AvailablePageSeo(BaseSchema):
    # Theme swagger.json

    
    title = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    meta_tags = fields.List(fields.Nested(SEOMetaItem, required=False), required=False)
    
    sitemap = fields.Nested(SEOSitemap, required=False)
    
    breadcrumb = fields.List(fields.Nested(SEObreadcrumb, required=False), required=False)
    
    _id = fields.Str(required=False)
    


class SEOMetaItem(BaseSchema):
    # Theme swagger.json

    
    title = fields.Str(required=False)
    
    items = fields.List(fields.Nested(SEOMetaItems, required=False), required=False)
    


class SEOMetaItems(BaseSchema):
    # Theme swagger.json

    
    key = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class SEOSitemap(BaseSchema):
    # Theme swagger.json

    
    priority = fields.Float(required=False)
    
    frequency = fields.Str(required=False)
    


class SEObreadcrumb(BaseSchema):
    # Theme swagger.json

    
    url = fields.Str(required=False)
    
    action = fields.Nested(Action, required=False)
    


class Action(BaseSchema):
    # Theme swagger.json

    
    type = fields.Str(required=False)
    
    page = fields.Nested(ActionPage, required=False)
    
    popup = fields.Nested(ActionPage, required=False)
    


class AvailablePageSchemaSections(BaseSchema):
    # Theme swagger.json

    
    name = fields.Str(required=False)
    
    label = fields.Str(required=False)
    
    props = fields.Dict(required=False)
    
    blocks = fields.List(fields.Dict(required=False), required=False)
    
    preset = fields.Dict(required=False)
    
    predicate = fields.Nested(AvailablePagePredicate, required=False)
    
    source = fields.Str(required=False)
    


class AvailablePageScreenPredicate(BaseSchema):
    # Theme swagger.json

    
    mobile = fields.Boolean(required=False)
    
    desktop = fields.Boolean(required=False)
    
    tablet = fields.Boolean(required=False)
    


class AvailablePageUserPredicate(BaseSchema):
    # Theme swagger.json

    
    authenticated = fields.Boolean(required=False)
    
    anonymous = fields.Boolean(required=False)
    


class AvailablePageRoutePredicate(BaseSchema):
    # Theme swagger.json

    
    selected = fields.Str(required=False)
    
    exact_url = fields.Str(required=False)
    
    query = fields.Dict(required=False)
    


class AvailablePagePlatformPredicate(BaseSchema):
    # Theme swagger.json

    
    ios = fields.Boolean(required=False)
    
    android = fields.Boolean(required=False)
    
    web = fields.Boolean(required=False)
    


class AvailablePageSchedulePredicate(BaseSchema):
    # Theme swagger.json

    
    cron = fields.Str(required=False)
    
    start = fields.Str(required=False)
    
    end = fields.Str(required=False)
    


class AvailablePagePredicate(BaseSchema):
    # Theme swagger.json

    
    screen = fields.Nested(AvailablePageScreenPredicate, required=False)
    
    user = fields.Nested(AvailablePageUserPredicate, required=False)
    
    route = fields.Nested(AvailablePageRoutePredicate, required=False)
    
    schedule = fields.Nested(AvailablePageSchedulePredicate, required=False)
    
    platform = fields.Nested(AvailablePagePlatformPredicate, required=False)
    
    zones = fields.List(fields.Str(required=False), required=False)
    


class MarketplaceThemeSchema(BaseSchema):
    # Theme swagger.json

    
    themes = fields.List(fields.Nested(MarketplaceTheme, required=False), required=False)
    
    page = fields.Nested(PaginationSchema, required=False)
    


class MarketplaceTheme(BaseSchema):
    # Theme swagger.json

    
    _id = fields.Str(required=False)
    
    payment = fields.Nested(PaymentInfo, required=False)
    
    contact = fields.Nested(ContactInfo, required=False)
    
    industry = fields.List(fields.Str(required=False), required=False)
    
    is_update = fields.Boolean(required=False)
    
    is_default = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    tagline = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    catalog_size = fields.Nested(CatalogSize, required=False)
    
    images = fields.Nested(MarketplaceThemeImages, required=False)
    
    carousel = fields.List(fields.Nested(CarouselItem, required=False), required=False)
    
    src = fields.Str(required=False)
    
    explore = fields.Nested(ExploreInfo, required=False)
    
    features = fields.List(fields.Nested(Feature, required=False), required=False)
    
    highlights = fields.List(fields.Nested(Highlight, required=False), required=False)
    
    variations = fields.List(fields.Nested(Variation, required=False), required=False)
    
    documentation = fields.Nested(Documentation, required=False)
    
    status = fields.Str(required=False)
    
    step = fields.Int(required=False)
    
    comments = fields.Nested(Comments, required=False)
    
    release = fields.Nested(Release, required=False)
    
    slug = fields.Str(required=False)
    
    organization_id = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    template_theme_id = fields.Str(required=False)
    


class PaymentInfo(BaseSchema):
    # Theme swagger.json

    
    is_paid = fields.Boolean(required=False)
    
    amount = fields.Float(required=False)
    


class ContactInfo(BaseSchema):
    # Theme swagger.json

    
    developer_contact = fields.List(fields.Str(required=False), required=False)
    
    seller_contact = fields.Str(required=False)
    


class CatalogSize(BaseSchema):
    # Theme swagger.json

    
    min = fields.Int(required=False)
    
    max = fields.Int(required=False)
    


class MarketplaceThemeImages(BaseSchema):
    # Theme swagger.json

    
    desktop = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    


class CarouselItem(BaseSchema):
    # Theme swagger.json

    
    desktop = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    


class ExploreInfo(BaseSchema):
    # Theme swagger.json

    
    title = fields.Str(required=False)
    
    description = fields.Str(required=False)
    


class Feature(BaseSchema):
    # Theme swagger.json

    
    category = fields.Str(required=False)
    
    list = fields.List(fields.Nested(FeatureItem, required=False), required=False)
    


class FeatureItem(BaseSchema):
    # Theme swagger.json

    
    label = fields.Str(required=False)
    
    description = fields.Str(required=False)
    


class Highlight(BaseSchema):
    # Theme swagger.json

    
    title = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    image = fields.Str(required=False)
    


class Variation(BaseSchema):
    # Theme swagger.json

    
    name = fields.Str(required=False)
    
    color = fields.Str(required=False)
    
    demo_url = fields.Str(required=False)
    
    images = fields.Nested(MarketplaceThemeImages, required=False)
    


class Documentation(BaseSchema):
    # Theme swagger.json

    
    notes = fields.Str(required=False)
    
    url = fields.Str(required=False)
    


class Comments(BaseSchema):
    # Theme swagger.json

    
    developer_remark = fields.Str(required=False)
    
    reviewer_feedback = fields.Str(required=False)
    


class ThemeRejectionReasons(BaseSchema):
    # Theme swagger.json

    
    _id = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    theme_id = fields.Str(required=False)
    
    organization_id = fields.Str(required=False)
    
    admin_id = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    rejection_reasons = fields.Dict(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    


class AllAvailablePageSchema(BaseSchema):
    # Theme swagger.json

    
    pages = fields.List(fields.Nested(AvailablePageSchema, required=False), required=False)
    


class PaginationSchema(BaseSchema):
    # Theme swagger.json

    
    size = fields.Int(required=False)
    
    item_total = fields.Int(required=False)
    
    has_next = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    
    current = fields.Int(required=False)
    


class BlitzkriegApiErrorSchema(BaseSchema):
    # Theme swagger.json

    
    message = fields.Str(required=False)
    


class BlitzkriegInternalServerErrorSchema(BaseSchema):
    # Theme swagger.json

    
    message = fields.Str(required=False)
    


class ThemesSchema(BaseSchema):
    # Theme swagger.json

    
    font = fields.Nested(Font, required=False)
    
    config = fields.Nested(Config, required=False)
    
    applied = fields.Boolean(required=False)
    
    is_private = fields.Boolean(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    _id = fields.Str(required=False)
    
    application_id = fields.Str(required=False)
    
    marketplace_theme_id = fields.Str(required=False)
    
    meta = fields.Nested(ThemeMeta, required=False)
    
    name = fields.Str(required=False)
    
    template_theme_id = fields.Str(required=False)
    
    version = fields.Str(required=False)
    
    styles = fields.Dict(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    assets = fields.Nested(Assets, required=False)
    
    available_sections = fields.List(fields.Nested(SectionItem, required=False), required=False)
    
    theme_type = fields.Str(required=False)
    
    company_id = fields.Float(required=False)
    
    src = fields.Str(required=False)
    


class Font(BaseSchema):
    # Theme swagger.json

    
    variants = fields.Nested(FontVariants, required=False)
    
    family = fields.Str(required=False)
    


class FontVariants(BaseSchema):
    # Theme swagger.json

    
    light = fields.Nested(FontVariant, required=False)
    
    regular = fields.Nested(FontVariant, required=False)
    
    medium = fields.Nested(FontVariant, required=False)
    
    semi_bold = fields.Nested(FontVariant, required=False)
    
    bold = fields.Nested(FontVariant, required=False)
    


class FontVariant(BaseSchema):
    # Theme swagger.json

    
    name = fields.Str(required=False)
    
    file = fields.Str(required=False)
    


class Config(BaseSchema):
    # Theme swagger.json

    
    current = fields.Str(required=False)
    
    list = fields.List(fields.Nested(ThemeConfiguration, required=False), required=False)
    
    global_schema = fields.Nested(GlobalSchema, required=False)
    
    preset = fields.Nested(Preset, required=False)
    


class ThemeConfiguration(BaseSchema):
    # Theme swagger.json

    
    name = fields.Str(required=False)
    
    global_config = fields.Dict(required=False)
    
    page = fields.List(fields.Nested(ThemeConfigListPage, required=False), required=False)
    


class OverlayPopup(BaseSchema):
    # Theme swagger.json

    
    dialog_backgroung = fields.Str(required=False)
    
    overlay = fields.Str(required=False)
    


class DividerStrokeHighlight(BaseSchema):
    # Theme swagger.json

    
    divider_strokes = fields.Str(required=False)
    
    highlight = fields.Str(required=False)
    


class UserAlerts(BaseSchema):
    # Theme swagger.json

    
    success_background = fields.Str(required=False)
    
    success_text = fields.Str(required=False)
    
    error_background = fields.Str(required=False)
    
    error_text = fields.Str(required=False)
    
    info_background = fields.Str(required=False)
    
    info_text = fields.Str(required=False)
    


class OrderTracking(BaseSchema):
    # Theme swagger.json

    
    show_header = fields.Boolean(required=False)
    
    show_footer = fields.Boolean(required=False)
    


class ThemeConfigListPage(BaseSchema):
    # Theme swagger.json

    
    page = fields.Str(required=False)
    
    settings = fields.Nested(ThemeConfigListPageSettingsProps, required=False)
    


class ThemeConfigListPageSettingsProps(BaseSchema):
    # Theme swagger.json

    
    props = fields.Dict(required=False)
    


class CustomConfig(BaseSchema):
    # Theme swagger.json

    
    props = fields.Nested(CustomProps, required=False)
    


class CustomProps(BaseSchema):
    # Theme swagger.json

    
    header_bg_color = fields.Str(required=False)
    
    header_text_color = fields.Str(required=False)
    
    header_border_color = fields.Str(required=False)
    
    header_icon_color = fields.Str(required=False)
    
    header_cart_notification_bg_color = fields.Str(required=False)
    
    header_cart_notification_text_color = fields.Str(required=False)
    
    header_nav_hover_color = fields.Str(required=False)
    
    button_primary_color = fields.Str(required=False)
    
    button_primary_label_color = fields.Str(required=False)
    
    button_add_to_cart_color = fields.Str(required=False)
    
    button_add_to_cart_label_color = fields.Str(required=False)
    
    button_secondary_color = fields.Str(required=False)
    
    button_secondary_label_color = fields.Str(required=False)
    
    button_tertiary_color = fields.Str(required=False)
    
    button_tertiary_label_color = fields.Str(required=False)
    
    button_tertiary_hover_color = fields.Str(required=False)
    
    button_tertiary_hover_text_color = fields.Str(required=False)
    
    text_heading_link_color = fields.Str(required=False)
    
    text_body_color = fields.Str(required=False)
    
    text_price_color = fields.Str(required=False)
    
    text_sale_price_color = fields.Str(required=False)
    
    text_strikethrough_price_color = fields.Str(required=False)
    
    text_discount_color = fields.Str(required=False)
    
    footer_bg_color = fields.Str(required=False)
    
    footer_text_color = fields.Str(required=False)
    
    footer_border_color = fields.Str(required=False)
    
    footer_nav_hover_color = fields.Str(required=False)
    
    disable_cart = fields.Boolean(required=False)
    
    is_menu_below_logo = fields.Boolean(required=False)
    
    menu_position = fields.Str(required=False)
    


class ThemeMeta(BaseSchema):
    # Theme swagger.json

    
    payment = fields.Nested(ThemePayment, required=False)
    
    description = fields.Str(required=False)
    
    industry = fields.List(fields.Str(required=False), required=False)
    
    release = fields.Nested(Release, required=False)
    
    images = fields.Nested(Images, required=False)
    
    slug = fields.Str(required=False)
    
    name = fields.Str(required=False)
    


class ThemePayment(BaseSchema):
    # Theme swagger.json

    
    is_paid = fields.Boolean(required=False)
    
    amount = fields.Float(required=False)
    


class Release(BaseSchema):
    # Theme swagger.json

    
    notes = fields.Str(required=False)
    
    version = fields.Str(required=False)
    


class Images(BaseSchema):
    # Theme swagger.json

    
    desktop = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    


class Assets(BaseSchema):
    # Theme swagger.json

    
    umd_js = fields.Nested(UMDJs, required=False)
    
    common_js = fields.Nested(CommonJS, required=False)
    
    css = fields.Nested(CSS, required=False)
    


class UMDJs(BaseSchema):
    # Theme swagger.json

    
    link = fields.Str(required=False)
    
    links = fields.List(fields.Str(required=False), required=False)
    


class CommonJS(BaseSchema):
    # Theme swagger.json

    
    link = fields.Str(required=False)
    


class CSS(BaseSchema):
    # Theme swagger.json

    
    link = fields.Str(required=False)
    
    links = fields.List(fields.Str(required=False), required=False)
    


class SectionItem(BaseSchema):
    # Theme swagger.json

    
    props = fields.List(fields.Raw(required=False), required=False)
    
    blocks = fields.List(fields.Raw(required=False), required=False)
    
    name = fields.Str(required=False)
    
    label = fields.Str(required=False)
    


class GlobalSchema(BaseSchema):
    # Theme swagger.json

    
    props = fields.List(fields.Dict(required=False), required=False)
    


class Preset(BaseSchema):
    # Theme swagger.json

    
    pages = fields.List(fields.Nested(Page, required=False), required=False)
    


class Page(BaseSchema):
    # Theme swagger.json

    
    sections = fields.List(fields.Nested(Section, required=False), required=False)
    
    value = fields.Str(required=False)
    


class SectionProps(BaseSchema):
    # Theme swagger.json

    
    title = fields.Nested(TextProp, required=False)
    
    item_margin = fields.Nested(TextProp, required=False)
    
    autoplay = fields.Nested(CheckboxProp, required=False)
    
    slide_interval = fields.Nested(RangeProp, required=False)
    


class SectionPreset(BaseSchema):
    # Theme swagger.json

    
    blocks = fields.List(fields.Nested(Block, required=False), required=False)
    


class ImagePickerProp(BaseSchema):
    # Theme swagger.json

    
    type = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class UrlProp(BaseSchema):
    # Theme swagger.json

    
    type = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class BlockProps(BaseSchema):
    # Theme swagger.json

    
    image = fields.Nested(ImagePickerProp, required=False)
    
    slide_link = fields.Nested(UrlProp, required=False)
    


class TextProp(BaseSchema):
    # Theme swagger.json

    
    value = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class CheckboxProp(BaseSchema):
    # Theme swagger.json

    
    value = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    


class RangeProp(BaseSchema):
    # Theme swagger.json

    
    value = fields.Int(required=False)
    
    type = fields.Str(required=False)
    


class Section(BaseSchema):
    # Theme swagger.json

    
    blocks = fields.List(fields.Nested(Block, required=False), required=False)
    
    predicate = fields.Nested(Predicate, required=False)
    
    name = fields.Str(required=False)
    
    props = fields.Nested(SectionProps, required=False)
    
    preset = fields.Nested(SectionPreset, required=False)
    


class Block(BaseSchema):
    # Theme swagger.json

    
    type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    props = fields.Nested(BlockProps, required=False)
    


class Predicate(BaseSchema):
    # Theme swagger.json

    
    screen = fields.Nested(Screen, required=False)
    
    user = fields.Nested(ThemeUserSchema, required=False)
    
    route = fields.Nested(Route, required=False)
    


class Screen(BaseSchema):
    # Theme swagger.json

    
    mobile = fields.Boolean(required=False)
    
    desktop = fields.Boolean(required=False)
    
    tablet = fields.Boolean(required=False)
    


class ThemeUserSchema(BaseSchema):
    # Theme swagger.json

    
    authenticated = fields.Boolean(required=False)
    
    anonymous = fields.Boolean(required=False)
    


class Route(BaseSchema):
    # Theme swagger.json

    
    selected = fields.Str(required=False)
    
    exact_url = fields.Str(required=False)
    


class UpdateThemeRequestBody(BaseSchema):
    # Theme swagger.json

    
    config = fields.Nested(Config, required=False)
    
    font = fields.Nested(Font, required=False)
    


class CreateNewTheme(BaseSchema):
    # Theme swagger.json

    
    name = fields.Str(required=False)
    
    available_sections = fields.List(fields.Nested(SectionItem, required=False), required=False)
    
    version = fields.Str(required=False)
    
    theme_type = fields.Str(required=False)
    
    list = fields.List(fields.Nested(ThemeConfiguration, required=False), required=False)
    
    global_schema = fields.Nested(GlobalSchema, required=False)
    
    preset = fields.Nested(Preset, required=False)
    
    current = fields.Str(required=False)
    
    pages = fields.List(fields.Nested(Page, required=False), required=False)
    


class ActionPage(BaseSchema):
    # Theme swagger.json

    
    params = fields.Dict(required=False)
    
    query = fields.Dict(required=False)
    
    url = fields.Str(required=False)
    
    type = fields.Str(required=False, validate=OneOf([val.value for val in PageType.__members__.values()]))
    


