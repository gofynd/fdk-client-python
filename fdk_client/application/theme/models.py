"""Theme Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..ApplicationModel import BaseSchema


from .enums import *



class AllAvailablePageSchema(BaseSchema):
    pass


class AvailablePageSchema(BaseSchema):
    pass


class AvailablePageSectionMetaAttributes(BaseSchema):
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


class AvailablePageSeo(BaseSchema):
    pass


class AvailablePageSchemaSections(BaseSchema):
    pass


class AvailablePagePredicate(BaseSchema):
    pass


class AvailablePageScreenPredicate(BaseSchema):
    pass


class AvailablePageUserPredicate(BaseSchema):
    pass


class AvailablePageRoutePredicate(BaseSchema):
    pass


class AvailablePageSchedulePredicate(BaseSchema):
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


class CustomConfig(BaseSchema):
    pass


class CustomProps(BaseSchema):
    pass


class GlobalConfig(BaseSchema):
    pass


class GeneralSetting(BaseSchema):
    pass


class AdvanceSetting(BaseSchema):
    pass


class UserAlertsSetting(BaseSchema):
    pass


class ThemeSetting(BaseSchema):
    pass


class TextSetting(BaseSchema):
    pass


class ButtonSetting(BaseSchema):
    pass


class SaleDiscountSetting(BaseSchema):
    pass


class HeaderSetting(BaseSchema):
    pass


class FooterSetting(BaseSchema):
    pass


class OverlayPopupSetting(BaseSchema):
    pass


class DividerStrokeHighlightSetting(BaseSchema):
    pass


class StaticConfig(BaseSchema):
    pass


class StaticProps(BaseSchema):
    pass


class Colors(BaseSchema):
    pass


class AuthConfig(BaseSchema):
    pass


class PaletteConfig(BaseSchema):
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


class AvailablePagePlatformPredicate(BaseSchema):
    pass


class BlitzkriegInternalServerErrorSchema(BaseSchema):
    pass


class BlitzkriegApiErrorSchema(BaseSchema):
    pass


class ActionPage(BaseSchema):
    pass





class AllAvailablePageSchema(BaseSchema):
    # Theme swagger.json

    
    pages = fields.List(fields.Nested(AvailablePageSchema, required=False), required=False)
    


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
    


class AvailablePageSectionMetaAttributes(BaseSchema):
    # Theme swagger.json

    
    attributes = fields.Dict(required=False)
    


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
    


class AvailablePageSeo(BaseSchema):
    # Theme swagger.json

    
    title = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    canonical_url = fields.Str(required=False)
    
    meta_tags = fields.List(fields.Nested(SEOMetaItem, required=False), required=False)
    
    sitemap = fields.Nested(SEOSitemap, required=False)
    
    breadcrumb = fields.List(fields.Nested(SEObreadcrumb, required=False), required=False)
    
    _id = fields.Str(required=False)
    


class AvailablePageSchemaSections(BaseSchema):
    # Theme swagger.json

    
    name = fields.Str(required=False)
    
    label = fields.Str(required=False)
    
    source = fields.Str(required=False)
    
    props = fields.Dict(required=False)
    
    blocks = fields.List(fields.Dict(required=False), required=False)
    
    preset = fields.Dict(required=False)
    
    predicate = fields.Nested(AvailablePagePredicate, required=False)
    


class AvailablePagePredicate(BaseSchema):
    # Theme swagger.json

    
    screen = fields.Nested(AvailablePageScreenPredicate, required=False)
    
    user = fields.Nested(AvailablePageUserPredicate, required=False)
    
    route = fields.Nested(AvailablePageRoutePredicate, required=False)
    
    schedule = fields.Nested(AvailablePageSchedulePredicate, required=False)
    
    platform = fields.Nested(AvailablePagePlatformPredicate, required=False)
    
    zones = fields.List(fields.Str(required=False), required=False)
    


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
    


class AvailablePageSchedulePredicate(BaseSchema):
    # Theme swagger.json

    
    cron = fields.Str(required=False)
    
    start = fields.Str(required=False)
    
    end = fields.Str(required=False)
    


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
    
    page = fields.List(fields.Str(required=False), required=False)
    


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
    


class GlobalConfig(BaseSchema):
    # Theme swagger.json

    
    statics = fields.Nested(StaticConfig, required=False)
    
    custom = fields.Nested(CustomConfig, required=False)
    


class GeneralSetting(BaseSchema):
    # Theme swagger.json

    
    theme = fields.Nested(ThemeSetting, required=False)
    
    text = fields.Nested(TextSetting, required=False)
    
    button = fields.Nested(ButtonSetting, required=False)
    
    sale_discount = fields.Nested(SaleDiscountSetting, required=False)
    
    header = fields.Nested(HeaderSetting, required=False)
    
    footer = fields.Nested(FooterSetting, required=False)
    


class AdvanceSetting(BaseSchema):
    # Theme swagger.json

    
    overlay_popup = fields.Nested(OverlayPopupSetting, required=False)
    
    divider_stroke_highlight = fields.Nested(DividerStrokeHighlightSetting, required=False)
    
    user_alerts = fields.Nested(UserAlertsSetting, required=False)
    


class UserAlertsSetting(BaseSchema):
    # Theme swagger.json

    
    success_background = fields.Str(required=False)
    
    success_text = fields.Str(required=False)
    
    error_background = fields.Str(required=False)
    
    error_text = fields.Str(required=False)
    
    info_background = fields.Str(required=False)
    
    info_text = fields.Str(required=False)
    


class ThemeSetting(BaseSchema):
    # Theme swagger.json

    
    page_background = fields.Str(required=False)
    
    theme_accent = fields.Str(required=False)
    


class TextSetting(BaseSchema):
    # Theme swagger.json

    
    text_heading = fields.Str(required=False)
    
    text_body = fields.Str(required=False)
    
    text_label = fields.Str(required=False)
    
    text_secondary = fields.Str(required=False)
    


class ButtonSetting(BaseSchema):
    # Theme swagger.json

    
    button_primary = fields.Str(required=False)
    
    button_secondary = fields.Str(required=False)
    
    button_link = fields.Str(required=False)
    


class SaleDiscountSetting(BaseSchema):
    # Theme swagger.json

    
    sale_badge_background = fields.Str(required=False)
    
    sale_badge_text = fields.Str(required=False)
    
    sale_discount_text = fields.Str(required=False)
    
    sale_timer = fields.Str(required=False)
    


class HeaderSetting(BaseSchema):
    # Theme swagger.json

    
    header_background = fields.Str(required=False)
    
    header_nav = fields.Str(required=False)
    
    header_icon = fields.Str(required=False)
    


class FooterSetting(BaseSchema):
    # Theme swagger.json

    
    footer_background = fields.Str(required=False)
    
    footer_bottom_background = fields.Str(required=False)
    
    footer_heading_text = fields.Str(required=False)
    
    footer_body_text = fields.Str(required=False)
    
    footer_icon = fields.Str(required=False)
    


class OverlayPopupSetting(BaseSchema):
    # Theme swagger.json

    
    dialog_backgroung = fields.Str(required=False)
    
    overlay = fields.Str(required=False)
    


class DividerStrokeHighlightSetting(BaseSchema):
    # Theme swagger.json

    
    divider_strokes = fields.Str(required=False)
    
    highlight = fields.Str(required=False)
    


class StaticConfig(BaseSchema):
    # Theme swagger.json

    
    props = fields.Nested(StaticProps, required=False)
    


class StaticProps(BaseSchema):
    # Theme swagger.json

    
    colors = fields.Nested(Colors, required=False)
    
    auth = fields.Nested(AuthConfig, required=False)
    
    palette = fields.Nested(PaletteConfig, required=False)
    


class Colors(BaseSchema):
    # Theme swagger.json

    
    primary_color = fields.Str(required=False)
    
    secondary_color = fields.Str(required=False)
    
    accent_color = fields.Str(required=False)
    
    link_color = fields.Str(required=False)
    
    button_secondary_color = fields.Str(required=False)
    
    bg_color = fields.Str(required=False)
    


class AuthConfig(BaseSchema):
    # Theme swagger.json

    
    show_header_auth = fields.Boolean(required=False)
    
    show_footer_auth = fields.Boolean(required=False)
    


class PaletteConfig(BaseSchema):
    # Theme swagger.json

    
    general_setting = fields.Nested(GeneralSetting, required=False)
    
    advance_setting = fields.Nested(AdvanceSetting, required=False)
    


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

    
    links = fields.List(fields.Str(required=False), required=False)
    


class CommonJS(BaseSchema):
    # Theme swagger.json

    
    link = fields.Str(required=False)
    


class CSS(BaseSchema):
    # Theme swagger.json

    
    links = fields.List(fields.Str(required=False), required=False)
    


class SectionItem(BaseSchema):
    # Theme swagger.json

    
    props = fields.List(fields.Dict(required=False), required=False)
    
    blocks = fields.List(fields.Dict(required=False), required=False)
    
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
    


class AvailablePagePlatformPredicate(BaseSchema):
    # Theme swagger.json

    
    ios = fields.Boolean(required=False)
    
    android = fields.Boolean(required=False)
    
    web = fields.Boolean(required=False)
    


class BlitzkriegInternalServerErrorSchema(BaseSchema):
    # Theme swagger.json

    
    message = fields.Str(required=False)
    


class BlitzkriegApiErrorSchema(BaseSchema):
    # Theme swagger.json

    
    message = fields.Str(required=False)
    


class ActionPage(BaseSchema):
    # Theme swagger.json

    
    params = fields.Dict(required=False)
    
    query = fields.Dict(required=False)
    
    url = fields.Str(required=False)
    
    type = fields.Str(required=False, validate=OneOf([val.value for val in PageType.__members__.values()]))
    


