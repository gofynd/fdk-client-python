"""Theme Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




class ThemeReq(BaseSchema):
    pass


class ThemeSchema(BaseSchema):
    pass


class MarketplaceThemeId(BaseSchema):
    pass


class ThemeMeta(BaseSchema):
    pass


class ThemePayment(BaseSchema):
    pass


class ThemeImages(BaseSchema):
    pass


class AvailablePageSchema(BaseSchema):
    pass


class AvailablePageSectionMetaAttributes(BaseSchema):
    pass


class AvailablePageSeo(BaseSchema):
    pass


class AvailablePageSchemaSections(BaseSchema):
    pass


class AvailablePageScreenPredicate(BaseSchema):
    pass


class AvailablePageUserPredicate(BaseSchema):
    pass


class AvailablePageRoutePredicate(BaseSchema):
    pass


class AvailablePagePredicate(BaseSchema):
    pass


class MarketplaceThemeResponse(BaseSchema):
    pass


class MarketplaceThemeResponseBody(BaseSchema):
    pass


class MarketplaceTheme(BaseSchema):
    pass


class PaymentInfo(BaseSchema):
    pass


class ContactInfo(BaseSchema):
    pass


class CatalogSize(BaseSchema):
    pass


class Images(BaseSchema):
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


class Release(BaseSchema):
    pass


class AllAvailablePageSchema(BaseSchema):
    pass


class PaginationSchema(BaseSchema):
    pass


class ThemesListingResponseSchema(BaseSchema):
    pass


class AddThemeRequestSchema(BaseSchema):
    pass


class UpgradableThemeSchema(BaseSchema):
    pass


class FontsSchema(BaseSchema):
    pass


class BlitzkriegApiErrorSchema(BaseSchema):
    pass


class BlitzkriegNotFoundSchema(BaseSchema):
    pass


class BlitzkriegInternalServerErrorSchema(BaseSchema):
    pass


class FontsSchemaItems(BaseSchema):
    pass


class FontsSchemaItemsFiles(BaseSchema):
    pass


class ThemesSchema(BaseSchema):
    pass


class availableSectionSchema(BaseSchema):
    pass


class Information(BaseSchema):
    pass


class Src(BaseSchema):
    pass


class AssetsSchema(BaseSchema):
    pass


class UmdJs(BaseSchema):
    pass


class CommonJs(BaseSchema):
    pass


class Css(BaseSchema):
    pass


class Sections(BaseSchema):
    pass


class Config(BaseSchema):
    pass


class Preset(BaseSchema):
    pass


class GlobalSchema(BaseSchema):
    pass


class ListSchemaItem(BaseSchema):
    pass


class Colors(BaseSchema):
    pass


class Custom(BaseSchema):
    pass


class ConfigPage(BaseSchema):
    pass


class Font(BaseSchema):
    pass


class Variants(BaseSchema):
    pass


class Medium(BaseSchema):
    pass


class SemiBold(BaseSchema):
    pass


class Bold(BaseSchema):
    pass


class Light(BaseSchema):
    pass


class Regular(BaseSchema):
    pass


class Blocks(BaseSchema):
    pass


class GlobalSchemaProps(BaseSchema):
    pass


class BlocksProps(BaseSchema):
    pass


class ApplyThemeRequestV2(BaseSchema):
    pass


class ApplyThemeResponseV2(BaseSchema):
    pass


class AllThemesApplicationResponseV2(BaseSchema):
    pass


class UpdateThemeNameRequestBodyV2(BaseSchema):
    pass


class UpdateThemeRequestBodyV2(BaseSchema):
    pass


class FontV2(BaseSchema):
    pass


class FontVariantsV2(BaseSchema):
    pass


class FontVariantV2(BaseSchema):
    pass


class ConfigV2(BaseSchema):
    pass


class ConfigurationV2(BaseSchema):
    pass


class GlobalConfigV2(BaseSchema):
    pass


class StaticConfigV2(BaseSchema):
    pass


class AuthConfigV2(BaseSchema):
    pass


class PaletteConfigV2(BaseSchema):
    pass


class CustomConfigV2(BaseSchema):
    pass


class MetaV2(BaseSchema):
    pass


class PaymentV2(BaseSchema):
    pass


class ReleaseV2(BaseSchema):
    pass


class ImagesV2(BaseSchema):
    pass


class StaticPropsV2(BaseSchema):
    pass


class ColorsV2(BaseSchema):
    pass


class GeneralSettingV2(BaseSchema):
    pass


class AdvanceSettingV2(BaseSchema):
    pass


class ThemeSettingV2(BaseSchema):
    pass


class TextSettingV2(BaseSchema):
    pass


class ButtonSettingV2(BaseSchema):
    pass


class SaleDiscountSettingV2(BaseSchema):
    pass


class HeaderSettingV2(BaseSchema):
    pass


class FooterSettingV2(BaseSchema):
    pass


class OverlayPopupSettingV2(BaseSchema):
    pass


class DividerStrokeHighlightSettingV2(BaseSchema):
    pass


class UserAlertsSettingV2(BaseSchema):
    pass


class CustomPropsV2(BaseSchema):
    pass


class GlobalSchemaV2(BaseSchema):
    pass


class PropV2(BaseSchema):
    pass


class AssetsV2(BaseSchema):
    pass


class UMDJs(BaseSchema):
    pass


class CommonJS(BaseSchema):
    pass


class CSS(BaseSchema):
    pass


class SectionItem(BaseSchema):
    pass


class PresetV2(BaseSchema):
    pass


class PageV2(BaseSchema):
    pass


class SectionV2(BaseSchema):
    pass


class BlockV2(BaseSchema):
    pass


class PredicateV2(BaseSchema):
    pass


class ScreenV2(BaseSchema):
    pass


class UserV2(BaseSchema):
    pass


class RouteV2(BaseSchema):
    pass


class SectionPropsV2(BaseSchema):
    pass


class SectionPresetV2(BaseSchema):
    pass


class BlockPropsV2(BaseSchema):
    pass


class TextPropV2(BaseSchema):
    pass


class CheckboxPropV2(BaseSchema):
    pass


class RangePropV2(BaseSchema):
    pass


class ImagePickerPropV2(BaseSchema):
    pass


class UrlPropV2(BaseSchema):
    pass





class ThemeReq(BaseSchema):
    # Theme swagger.json

    
    marketplace_theme_id = fields.Str(required=False)
    


class ThemeSchema(BaseSchema):
    # Theme swagger.json

    
    _id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    marketplace_theme_id = fields.Nested(MarketplaceThemeId, required=False)
    
    company_id = fields.Int(required=False)
    
    meta = fields.Nested(ThemeMeta, required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    


class MarketplaceThemeId(BaseSchema):
    # Theme swagger.json

    
    _id = fields.Str(required=False)
    
    is_default = fields.Boolean(required=False)
    


class ThemeMeta(BaseSchema):
    # Theme swagger.json

    
    payment = fields.Nested(ThemePayment, required=False)
    
    industry = fields.List(fields.Str(required=False), required=False)
    
    description = fields.Str(required=False)
    
    images = fields.Nested(ThemeImages, required=False)
    
    slug = fields.Str(required=False)
    


class ThemePayment(BaseSchema):
    # Theme swagger.json

    
    is_paid = fields.Boolean(required=False)
    
    amount = fields.Float(required=False)
    


class ThemeImages(BaseSchema):
    # Theme swagger.json

    
    desktop = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    


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
    


class AvailablePageSeo(BaseSchema):
    # Theme swagger.json

    
    title = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    


class AvailablePageSchemaSections(BaseSchema):
    # Theme swagger.json

    
    name = fields.Str(required=False)
    
    label = fields.Str(required=False)
    
    props = fields.Dict(required=False)
    
    blocks = fields.List(fields.Dict(required=False), required=False)
    
    preset = fields.Dict(required=False)
    
    predicate = fields.Nested(AvailablePagePredicate, required=False)
    


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
    


class AvailablePagePredicate(BaseSchema):
    # Theme swagger.json

    
    screen = fields.Nested(AvailablePageScreenPredicate, required=False)
    
    user = fields.Nested(AvailablePageUserPredicate, required=False)
    
    route = fields.Nested(AvailablePageRoutePredicate, required=False)
    


class MarketplaceThemeResponse(BaseSchema):
    # Theme swagger.json

    
    status = fields.Int(required=False)
    
    body = fields.Nested(MarketplaceThemeResponseBody, required=False)
    


class MarketplaceThemeResponseBody(BaseSchema):
    # Theme swagger.json

    
    items = fields.List(fields.Nested(MarketplaceTheme, required=False), required=False)
    
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
    
    images = fields.Nested(Images, required=False)
    
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
    


class Images(BaseSchema):
    # Theme swagger.json

    
    desktop = fields.List(fields.Str(required=False), required=False)
    
    mobile = fields.Str(required=False)
    
    android = fields.List(fields.Str(required=False), required=False)
    
    ios = fields.List(fields.Str(required=False), required=False)
    
    thumbnail = fields.List(fields.Str(required=False), required=False)
    


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
    
    images = fields.Nested(Images, required=False)
    


class Documentation(BaseSchema):
    # Theme swagger.json

    
    notes = fields.Str(required=False)
    
    url = fields.Str(required=False)
    


class Comments(BaseSchema):
    # Theme swagger.json

    
    developer_remark = fields.Str(required=False)
    
    reviewer_feedback = fields.Str(required=False)
    


class Release(BaseSchema):
    # Theme swagger.json

    
    version = fields.Str(required=False)
    
    notes = fields.Str(required=False)
    


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
    


class ThemesListingResponseSchema(BaseSchema):
    # Theme swagger.json

    
    items = fields.List(fields.Nested(ThemesSchema, required=False), required=False)
    
    page = fields.Nested(PaginationSchema, required=False)
    


class AddThemeRequestSchema(BaseSchema):
    # Theme swagger.json

    
    theme_id = fields.Str(required=False)
    


class UpgradableThemeSchema(BaseSchema):
    # Theme swagger.json

    
    parent_theme = fields.Str(required=False)
    
    applied_theme = fields.Str(required=False)
    
    upgrade = fields.Boolean(required=False)
    


class FontsSchema(BaseSchema):
    # Theme swagger.json

    
    items = fields.Nested(FontsSchemaItems, required=False)
    
    kind = fields.Str(required=False)
    


class BlitzkriegApiErrorSchema(BaseSchema):
    # Theme swagger.json

    
    message = fields.Str(required=False)
    


class BlitzkriegNotFoundSchema(BaseSchema):
    # Theme swagger.json

    
    message = fields.Str(required=False)
    


class BlitzkriegInternalServerErrorSchema(BaseSchema):
    # Theme swagger.json

    
    message = fields.Str(required=False)
    


class FontsSchemaItems(BaseSchema):
    # Theme swagger.json

    
    family = fields.Str(required=False)
    
    variants = fields.List(fields.Str(required=False), required=False)
    
    subsets = fields.List(fields.Str(required=False), required=False)
    
    version = fields.Str(required=False)
    
    last_modified = fields.Str(required=False)
    
    files = fields.Nested(FontsSchemaItemsFiles, required=False)
    
    category = fields.Str(required=False)
    
    kind = fields.Str(required=False)
    


class FontsSchemaItemsFiles(BaseSchema):
    # Theme swagger.json

    
    regular = fields.Str(required=False)
    
    italic = fields.Str(required=False)
    
    bold = fields.Str(required=False)
    


class ThemesSchema(BaseSchema):
    # Theme swagger.json

    
    application = fields.Str(required=False)
    
    applied = fields.Boolean(required=False)
    
    customized = fields.Boolean(required=False)
    
    published = fields.Boolean(required=False)
    
    archived = fields.Boolean(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    version = fields.Str(required=False)
    
    parent_theme_version = fields.Str(required=False)
    
    parent_theme = fields.Str(required=False)
    
    information = fields.Nested(Information, required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    src = fields.Nested(Src, required=False)
    
    assets = fields.Nested(AssetsSchema, required=False)
    
    available_sections = fields.List(fields.Nested(availableSectionSchema, required=False), required=False)
    
    styles = fields.Dict(required=False)
    
    config = fields.Nested(Config, required=False)
    
    font = fields.Nested(Font, required=False)
    
    _id = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    
    colors = fields.Nested(Colors, required=False)
    


class availableSectionSchema(BaseSchema):
    # Theme swagger.json

    
    blocks = fields.List(fields.Nested(Blocks, required=False), required=False)
    
    name = fields.Str(required=False)
    
    label = fields.Str(required=False)
    
    props = fields.List(fields.Nested(BlocksProps, required=False), required=False)
    


class Information(BaseSchema):
    # Theme swagger.json

    
    images = fields.Nested(Images, required=False)
    
    features = fields.List(fields.Str(required=False), required=False)
    
    name = fields.Str(required=False)
    
    description = fields.Str(required=False)
    


class Src(BaseSchema):
    # Theme swagger.json

    
    link = fields.Str(required=False)
    


class AssetsSchema(BaseSchema):
    # Theme swagger.json

    
    umd_js = fields.Nested(UmdJs, required=False)
    
    common_js = fields.Nested(CommonJs, required=False)
    
    css = fields.Nested(Css, required=False)
    


class UmdJs(BaseSchema):
    # Theme swagger.json

    
    link = fields.Str(required=False)
    
    links = fields.List(fields.Str(required=False), required=False)
    


class CommonJs(BaseSchema):
    # Theme swagger.json

    
    link = fields.Str(required=False)
    


class Css(BaseSchema):
    # Theme swagger.json

    
    link = fields.Str(required=False)
    
    links = fields.List(fields.Str(required=False), required=False)
    


class Sections(BaseSchema):
    # Theme swagger.json

    
    attributes = fields.Str(required=False)
    


class Config(BaseSchema):
    # Theme swagger.json

    
    preset = fields.Nested(Preset, required=False)
    
    global_schema = fields.Nested(GlobalSchema, required=False)
    
    current = fields.Str(required=False)
    
    list = fields.List(fields.Nested(ListSchemaItem, required=False), required=False)
    


class Preset(BaseSchema):
    # Theme swagger.json

    
    pages = fields.List(fields.Nested(AvailablePageSchema, required=False), required=False)
    


class GlobalSchema(BaseSchema):
    # Theme swagger.json

    
    props = fields.List(fields.Nested(GlobalSchemaProps, required=False), required=False)
    


class ListSchemaItem(BaseSchema):
    # Theme swagger.json

    
    global_config = fields.Dict(required=False)
    
    page = fields.List(fields.Nested(ConfigPage, required=False), required=False)
    
    name = fields.Str(required=False)
    


class Colors(BaseSchema):
    # Theme swagger.json

    
    bg_color = fields.Str(required=False)
    
    primary_color = fields.Str(required=False)
    
    secondary_color = fields.Str(required=False)
    
    accent_color = fields.Str(required=False)
    
    link_color = fields.Str(required=False)
    
    button_secondary_color = fields.Str(required=False)
    


class Custom(BaseSchema):
    # Theme swagger.json

    
    props = fields.Dict(required=False)
    


class ConfigPage(BaseSchema):
    # Theme swagger.json

    
    settings = fields.Dict(required=False)
    
    page = fields.Str(required=False)
    


class Font(BaseSchema):
    # Theme swagger.json

    
    family = fields.Str(required=False)
    
    variants = fields.Nested(Variants, required=False)
    


class Variants(BaseSchema):
    # Theme swagger.json

    
    medium = fields.Nested(Medium, required=False)
    
    semi_bold = fields.Nested(SemiBold, required=False)
    
    bold = fields.Nested(Bold, required=False)
    
    light = fields.Nested(Light, required=False)
    
    regular = fields.Nested(Regular, required=False)
    


class Medium(BaseSchema):
    # Theme swagger.json

    
    name = fields.Str(required=False)
    
    file = fields.Str(required=False)
    


class SemiBold(BaseSchema):
    # Theme swagger.json

    
    name = fields.Str(required=False)
    
    file = fields.Str(required=False)
    


class Bold(BaseSchema):
    # Theme swagger.json

    
    name = fields.Str(required=False)
    
    file = fields.Str(required=False)
    


class Light(BaseSchema):
    # Theme swagger.json

    
    name = fields.Str(required=False)
    
    file = fields.Str(required=False)
    


class Regular(BaseSchema):
    # Theme swagger.json

    
    name = fields.Str(required=False)
    
    file = fields.Str(required=False)
    


class Blocks(BaseSchema):
    # Theme swagger.json

    
    type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    props = fields.List(fields.Nested(BlocksProps, required=False), required=False)
    


class GlobalSchemaProps(BaseSchema):
    # Theme swagger.json

    
    id = fields.Str(required=False)
    
    label = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    category = fields.Str(required=False)
    


class BlocksProps(BaseSchema):
    # Theme swagger.json

    
    id = fields.Str(required=False)
    
    label = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class ApplyThemeRequestV2(BaseSchema):
    # Theme swagger.json

    
    marketplace_theme_id = fields.Str(required=False)
    


class ApplyThemeResponseV2(BaseSchema):
    # Theme swagger.json

    
    font = fields.Nested(FontV2, required=False)
    
    config = fields.Nested(ConfigV2, required=False)
    
    applied = fields.Boolean(required=False)
    
    is_private = fields.Boolean(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    _id = fields.Str(required=False)
    
    application_id = fields.Str(required=False)
    
    marketplace_theme_id = fields.Str(required=False)
    
    meta = fields.Nested(MetaV2, required=False)
    
    name = fields.Str(required=False)
    
    template_theme_id = fields.Str(required=False)
    
    version = fields.Str(required=False)
    
    styles = fields.Dict(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    


class AllThemesApplicationResponseV2(BaseSchema):
    # Theme swagger.json

    
    font = fields.Nested(FontV2, required=False)
    
    config = fields.Nested(ConfigV2, required=False)
    
    applied = fields.Boolean(required=False)
    
    is_private = fields.Boolean(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    _id = fields.Str(required=False)
    
    application_id = fields.Str(required=False)
    
    marketplace_theme_id = fields.Str(required=False)
    
    meta = fields.Nested(MetaV2, required=False)
    
    name = fields.Str(required=False)
    
    template_theme_id = fields.Str(required=False)
    
    version = fields.Str(required=False)
    
    styles = fields.Dict(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    assets = fields.Nested(AssetsV2, required=False)
    
    available_sections = fields.List(fields.Nested(SectionItem, required=False), required=False)
    


class UpdateThemeNameRequestBodyV2(BaseSchema):
    # Theme swagger.json

    
    name = fields.Str(required=False)
    


class UpdateThemeRequestBodyV2(BaseSchema):
    # Theme swagger.json

    
    config = fields.Nested(ConfigV2, required=False)
    
    font = fields.Nested(FontV2, required=False)
    


class FontV2(BaseSchema):
    # Theme swagger.json

    
    variants = fields.Nested(FontVariantsV2, required=False)
    
    family = fields.Str(required=False)
    


class FontVariantsV2(BaseSchema):
    # Theme swagger.json

    
    light = fields.Nested(FontVariantV2, required=False)
    
    regular = fields.Nested(FontVariantV2, required=False)
    
    medium = fields.Nested(FontVariantV2, required=False)
    
    semi_bold = fields.Nested(FontVariantV2, required=False)
    
    bold = fields.Nested(FontVariantV2, required=False)
    


class FontVariantV2(BaseSchema):
    # Theme swagger.json

    
    name = fields.Str(required=False)
    
    file = fields.Str(required=False)
    


class ConfigV2(BaseSchema):
    # Theme swagger.json

    
    current = fields.Str(required=False)
    
    list = fields.List(fields.Nested(ConfigurationV2, required=False), required=False)
    
    global_schema = fields.Nested(GlobalSchemaV2, required=False)
    
    preset = fields.Nested(PresetV2, required=False)
    


class ConfigurationV2(BaseSchema):
    # Theme swagger.json

    
    name = fields.Str(required=False)
    
    global_config = fields.Nested(GlobalConfigV2, required=False)
    
    custom = fields.Nested(CustomConfigV2, required=False)
    
    page = fields.List(fields.Str(required=False), required=False)
    


class GlobalConfigV2(BaseSchema):
    # Theme swagger.json

    
    statics = fields.Nested(StaticConfigV2, required=False)
    
    auth = fields.Nested(AuthConfigV2, required=False)
    
    palette = fields.Nested(PaletteConfigV2, required=False)
    


class StaticConfigV2(BaseSchema):
    # Theme swagger.json

    
    props = fields.Nested(StaticPropsV2, required=False)
    


class AuthConfigV2(BaseSchema):
    # Theme swagger.json

    
    show_header_auth = fields.Boolean(required=False)
    
    show_footer_auth = fields.Boolean(required=False)
    


class PaletteConfigV2(BaseSchema):
    # Theme swagger.json

    
    general_setting = fields.Nested(GeneralSettingV2, required=False)
    
    advance_setting = fields.Nested(AdvanceSettingV2, required=False)
    


class CustomConfigV2(BaseSchema):
    # Theme swagger.json

    
    props = fields.Nested(CustomPropsV2, required=False)
    


class MetaV2(BaseSchema):
    # Theme swagger.json

    
    payment = fields.Nested(PaymentV2, required=False)
    
    description = fields.Str(required=False)
    
    industry = fields.List(fields.Str(required=False), required=False)
    
    release = fields.Nested(ReleaseV2, required=False)
    
    images = fields.Nested(ImagesV2, required=False)
    
    slug = fields.Str(required=False)
    
    name = fields.Str(required=False)
    


class PaymentV2(BaseSchema):
    # Theme swagger.json

    
    is_paid = fields.Boolean(required=False)
    
    amount = fields.Float(required=False)
    


class ReleaseV2(BaseSchema):
    # Theme swagger.json

    
    notes = fields.Str(required=False)
    
    version = fields.Str(required=False)
    


class ImagesV2(BaseSchema):
    # Theme swagger.json

    
    desktop = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    


class StaticPropsV2(BaseSchema):
    # Theme swagger.json

    
    colors = fields.Nested(ColorsV2, required=False)
    
    auth = fields.Nested(AuthConfigV2, required=False)
    


class ColorsV2(BaseSchema):
    # Theme swagger.json

    
    primary_color = fields.Str(required=False)
    
    secondary_color = fields.Str(required=False)
    
    accent_color = fields.Str(required=False)
    
    link_color = fields.Str(required=False)
    
    button_secondary_color = fields.Str(required=False)
    
    bg_color = fields.Str(required=False)
    


class GeneralSettingV2(BaseSchema):
    # Theme swagger.json

    
    theme = fields.Nested(ThemeSettingV2, required=False)
    
    text = fields.Nested(TextSettingV2, required=False)
    
    button = fields.Nested(ButtonSettingV2, required=False)
    
    sale_discount = fields.Nested(SaleDiscountSettingV2, required=False)
    
    header = fields.Nested(HeaderSettingV2, required=False)
    
    footer = fields.Nested(FooterSettingV2, required=False)
    


class AdvanceSettingV2(BaseSchema):
    # Theme swagger.json

    
    overlay_popup = fields.Nested(OverlayPopupSettingV2, required=False)
    
    divider_stroke_highlight = fields.Nested(DividerStrokeHighlightSettingV2, required=False)
    
    user_alerts = fields.Nested(UserAlertsSettingV2, required=False)
    


class ThemeSettingV2(BaseSchema):
    # Theme swagger.json

    
    page_background = fields.Str(required=False)
    
    theme_accent = fields.Str(required=False)
    


class TextSettingV2(BaseSchema):
    # Theme swagger.json

    
    text_heading = fields.Str(required=False)
    
    text_body = fields.Str(required=False)
    
    text_label = fields.Str(required=False)
    
    text_secondary = fields.Str(required=False)
    


class ButtonSettingV2(BaseSchema):
    # Theme swagger.json

    
    button_primary = fields.Str(required=False)
    
    button_secondary = fields.Str(required=False)
    
    button_link = fields.Str(required=False)
    


class SaleDiscountSettingV2(BaseSchema):
    # Theme swagger.json

    
    sale_badge_background = fields.Str(required=False)
    
    sale_badge_text = fields.Str(required=False)
    
    sale_discount_text = fields.Str(required=False)
    
    sale_timer = fields.Str(required=False)
    


class HeaderSettingV2(BaseSchema):
    # Theme swagger.json

    
    header_background = fields.Str(required=False)
    
    header_nav = fields.Str(required=False)
    
    header_icon = fields.Str(required=False)
    


class FooterSettingV2(BaseSchema):
    # Theme swagger.json

    
    footer_background = fields.Str(required=False)
    
    footer_bottom_background = fields.Str(required=False)
    
    footer_heading_text = fields.Str(required=False)
    
    footer_body_text = fields.Str(required=False)
    
    footer_icon = fields.Str(required=False)
    


class OverlayPopupSettingV2(BaseSchema):
    # Theme swagger.json

    
    dialog_backgroung = fields.Str(required=False)
    
    overlay = fields.Str(required=False)
    


class DividerStrokeHighlightSettingV2(BaseSchema):
    # Theme swagger.json

    
    divider_strokes = fields.Str(required=False)
    
    highlight = fields.Str(required=False)
    


class UserAlertsSettingV2(BaseSchema):
    # Theme swagger.json

    
    success_background = fields.Str(required=False)
    
    success_text = fields.Str(required=False)
    
    error_background = fields.Str(required=False)
    
    error_text = fields.Str(required=False)
    
    info_background = fields.Str(required=False)
    
    info_text = fields.Str(required=False)
    


class CustomPropsV2(BaseSchema):
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
    


class GlobalSchemaV2(BaseSchema):
    # Theme swagger.json

    
    props = fields.List(fields.Nested(PropV2, required=False), required=False)
    


class PropV2(BaseSchema):
    # Theme swagger.json

    
    type = fields.Str(required=False)
    
    category = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    label = fields.Str(required=False)
    
    info = fields.Str(required=False)
    


class AssetsV2(BaseSchema):
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

    
    props = fields.List(fields.Raw(required=False), required=False)
    
    blocks = fields.List(fields.Raw(required=False), required=False)
    
    name = fields.Str(required=False)
    
    label = fields.Str(required=False)
    


class PresetV2(BaseSchema):
    # Theme swagger.json

    
    pages = fields.List(fields.Nested(PageV2, required=False), required=False)
    


class PageV2(BaseSchema):
    # Theme swagger.json

    
    sections = fields.List(fields.Nested(SectionV2, required=False), required=False)
    
    value = fields.Str(required=False)
    


class SectionV2(BaseSchema):
    # Theme swagger.json

    
    blocks = fields.List(fields.Nested(BlockV2, required=False), required=False)
    
    predicate = fields.Nested(PredicateV2, required=False)
    
    name = fields.Str(required=False)
    
    props = fields.Nested(SectionPropsV2, required=False)
    
    preset = fields.Nested(SectionPresetV2, required=False)
    


class BlockV2(BaseSchema):
    # Theme swagger.json

    
    type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    props = fields.Nested(BlockPropsV2, required=False)
    


class PredicateV2(BaseSchema):
    # Theme swagger.json

    
    screen = fields.Nested(ScreenV2, required=False)
    
    user = fields.Nested(UserV2, required=False)
    
    route = fields.Nested(RouteV2, required=False)
    


class ScreenV2(BaseSchema):
    # Theme swagger.json

    
    mobile = fields.Boolean(required=False)
    
    desktop = fields.Boolean(required=False)
    
    tablet = fields.Boolean(required=False)
    


class UserV2(BaseSchema):
    # Theme swagger.json

    
    authenticated = fields.Boolean(required=False)
    
    anonymous = fields.Boolean(required=False)
    


class RouteV2(BaseSchema):
    # Theme swagger.json

    
    selected = fields.Str(required=False)
    
    exact_url = fields.Str(required=False)
    


class SectionPropsV2(BaseSchema):
    # Theme swagger.json

    
    title = fields.Nested(TextPropV2, required=False)
    
    item_margin = fields.Nested(TextPropV2, required=False)
    
    autoplay = fields.Nested(CheckboxPropV2, required=False)
    
    slide_interval = fields.Nested(RangePropV2, required=False)
    


class SectionPresetV2(BaseSchema):
    # Theme swagger.json

    
    blocks = fields.List(fields.Nested(BlockV2, required=False), required=False)
    


class BlockPropsV2(BaseSchema):
    # Theme swagger.json

    
    image = fields.Nested(ImagePickerPropV2, required=False)
    
    slide_link = fields.Nested(UrlPropV2, required=False)
    


class TextPropV2(BaseSchema):
    # Theme swagger.json

    
    value = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class CheckboxPropV2(BaseSchema):
    # Theme swagger.json

    
    value = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    


class RangePropV2(BaseSchema):
    # Theme swagger.json

    
    value = fields.Int(required=False)
    
    type = fields.Str(required=False)
    


class ImagePickerPropV2(BaseSchema):
    # Theme swagger.json

    
    type = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class UrlPropV2(BaseSchema):
    # Theme swagger.json

    
    type = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


