"""Content Application Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..ApplicationModel import BaseSchema


from .enums import *



class ApplicationLegal(BaseSchema):
    pass


class ApplicationLegalFAQ(BaseSchema):
    pass


class SeoComponent(BaseSchema):
    pass


class SeoSchema(BaseSchema):
    pass


class CustomMetaTag(BaseSchema):
    pass


class Detail(BaseSchema):
    pass


class SeoSchemaComponent(BaseSchema):
    pass


class SEOSchemaMarkupTemplate(BaseSchema):
    pass


class ScheduleSchema(BaseSchema):
    pass


class NextSchedule(BaseSchema):
    pass


class AnnouncementSchema(BaseSchema):
    pass


class ScheduleStartSchema(BaseSchema):
    pass


class BlogGetResponseSchema(BaseSchema):
    pass


class BlogFilters(BaseSchema):
    pass


class ResourceContent(BaseSchema):
    pass


class Asset(BaseSchema):
    pass


class Author(BaseSchema):
    pass


class BlogSchema(BaseSchema):
    pass


class SEO(BaseSchema):
    pass


class SEOImage(BaseSchema):
    pass


class SEOMetaItem(BaseSchema):
    pass


class SEOMetaItems(BaseSchema):
    pass


class SEOSitemap(BaseSchema):
    pass


class SEObreadcrumb(BaseSchema):
    pass


class DefaultSitemapIndividualConfig(BaseSchema):
    pass


class DefaultSitemapConfig(BaseSchema):
    pass


class SitemapConfig(BaseSchema):
    pass


class SitemapConfigurationList(BaseSchema):
    pass


class DateMeta(BaseSchema):
    pass


class LocaleLanguage(BaseSchema):
    pass


class Language(BaseSchema):
    pass


class Action(BaseSchema):
    pass


class NavigationReference(BaseSchema):
    pass


class AnnouncementsResponseSchema(BaseSchema):
    pass


class FaqResponseSchema(BaseSchema):
    pass


class DataLoaderSchema(BaseSchema):
    pass


class DataLoaderSourceSchema(BaseSchema):
    pass


class DataLoadersSchema(BaseSchema):
    pass


class ContentAPIError(BaseSchema):
    pass


class CategorySchema(BaseSchema):
    pass


class ChildrenSchema(BaseSchema):
    pass


class FAQCategorySchema(BaseSchema):
    pass


class FaqSchema(BaseSchema):
    pass


class GetFaqSchema(BaseSchema):
    pass


class GetFaqCategoriesSchema(BaseSchema):
    pass


class GetFaqCategoryBySlugSchema(BaseSchema):
    pass


class Page(BaseSchema):
    pass


class LandingPageSchema(BaseSchema):
    pass


class NavigationGetResponseSchema(BaseSchema):
    pass


class Orientation(BaseSchema):
    pass


class NavigationSchema(BaseSchema):
    pass


class PageGetResponseSchema(BaseSchema):
    pass


class PageSchema(BaseSchema):
    pass


class SanitizedContent(BaseSchema):
    pass


class CreatedBySchema(BaseSchema):
    pass


class Support(BaseSchema):
    pass


class PhoneProperties(BaseSchema):
    pass


class PhoneSchema(BaseSchema):
    pass


class EmailProperties(BaseSchema):
    pass


class EmailSchema(BaseSchema):
    pass


class ContactSchema(BaseSchema):
    pass


class TagsSchema(BaseSchema):
    pass


class TagSchema(BaseSchema):
    pass


class TagSourceSchema(BaseSchema):
    pass


class WellKnownResponseSchema(BaseSchema):
    pass


class CustomObjectListItemDefinationSchema(BaseSchema):
    pass


class CustomObjectFieldSchema(BaseSchema):
    pass


class CustomObjectByIdSchema(BaseSchema):
    pass


class CustomFieldSchema(BaseSchema):
    pass


class CustomFieldsResponseByResourceIdSchema(BaseSchema):
    pass


class ActionPage(BaseSchema):
    pass





class ApplicationLegal(BaseSchema):
    # Content swagger.json

    
    application = fields.Str(required=False)
    
    tnc = fields.Str(required=False)
    
    policy = fields.Str(required=False)
    
    shipping = fields.Str(required=False)
    
    returns = fields.Str(required=False)
    
    faq = fields.List(fields.Nested(ApplicationLegalFAQ, required=False), required=False)
    
    _id = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    __v = fields.Float(required=False)
    


class ApplicationLegalFAQ(BaseSchema):
    # Content swagger.json

    
    question = fields.Str(required=False)
    
    answer = fields.Str(required=False)
    


class SeoComponent(BaseSchema):
    # Content swagger.json

    
    seo = fields.Nested(SeoSchema, required=False)
    


class SeoSchema(BaseSchema):
    # Content swagger.json

    
    app = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    robots_txt = fields.Str(required=False)
    
    sitemap_enabled = fields.Boolean(required=False)
    
    additional_sitemap = fields.Str(required=False)
    
    sitemap = fields.Nested(SEOSitemap, required=False)
    
    cannonical_enabled = fields.Boolean(required=False)
    
    custom_meta_tags = fields.List(fields.Nested(CustomMetaTag, required=False), required=False)
    
    details = fields.Nested(Detail, required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    __v = fields.Float(required=False)
    


class CustomMetaTag(BaseSchema):
    # Content swagger.json

    
    name = fields.Str(required=False)
    
    content = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    


class Detail(BaseSchema):
    # Content swagger.json

    
    title = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    image_url = fields.Str(required=False)
    


class SeoSchemaComponent(BaseSchema):
    # Content swagger.json

    
    items = fields.List(fields.Nested(SEOSchemaMarkupTemplate, required=False), required=False)
    


class SEOSchemaMarkupTemplate(BaseSchema):
    # Content swagger.json

    
    _id = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    page_type = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    schema = fields.Str(required=False)
    
    target_json = fields.Dict(required=False)
    
    active = fields.Boolean(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    application = fields.Str(required=False)
    
    __v = fields.Float(required=False)
    


class ScheduleSchema(BaseSchema):
    # Content swagger.json

    
    cron = fields.Str(required=False)
    
    start = fields.Str(required=False)
    
    end = fields.Str(required=False)
    
    duration = fields.Float(required=False)
    
    next_schedule = fields.List(fields.Nested(NextSchedule, required=False), required=False)
    


class NextSchedule(BaseSchema):
    # Content swagger.json

    
    start = fields.Str(required=False)
    
    end = fields.Str(required=False)
    


class AnnouncementSchema(BaseSchema):
    # Content swagger.json

    
    announcement = fields.Str(required=False)
    
    schedule = fields.Nested(ScheduleStartSchema, required=False)
    


class ScheduleStartSchema(BaseSchema):
    # Content swagger.json

    
    start = fields.Str(required=False)
    
    end = fields.Str(required=False)
    


class BlogGetResponseSchema(BaseSchema):
    # Content swagger.json

    
    items = fields.List(fields.Nested(BlogSchema, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
    filters = fields.Nested(BlogFilters, required=False)
    


class BlogFilters(BaseSchema):
    # Content swagger.json

    
    tags = fields.List(fields.Str(required=False), required=False)
    


class ResourceContent(BaseSchema):
    # Content swagger.json

    
    type = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class Asset(BaseSchema):
    # Content swagger.json

    
    aspect_ratio = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    secure_url = fields.Str(required=False)
    


class Author(BaseSchema):
    # Content swagger.json

    
    designation = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    


class BlogSchema(BaseSchema):
    # Content swagger.json

    
    _id = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    application = fields.Str(required=False)
    
    archived = fields.Boolean(required=False)
    
    author = fields.Nested(Author, required=False)
    
    content = fields.List(fields.Nested(ResourceContent, required=False), required=False)
    
    feature_image = fields.Nested(Asset, required=False)
    
    published = fields.Boolean(required=False)
    
    reading_time = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    publish_date = fields.Str(required=False)
    
    seo = fields.Nested(SEO, required=False)
    
    title = fields.Str(required=False)
    
    date_meta = fields.Nested(DateMeta, required=False)
    
    summary = fields.Str(required=False)
    
    status = fields.Str(required=False)
    


class SEO(BaseSchema):
    # Content swagger.json

    
    description = fields.Str(required=False)
    
    image = fields.Nested(SEOImage, required=False)
    
    title = fields.Str(required=False)
    
    meta_tags = fields.List(fields.Nested(SEOMetaItem, required=False), required=False)
    
    sitemap = fields.Nested(SEOSitemap, required=False)
    
    breadcrumbs = fields.List(fields.Nested(SEObreadcrumb, required=False), required=False)
    
    canonical_url = fields.Str(required=False)
    


class SEOImage(BaseSchema):
    # Content swagger.json

    
    url = fields.Str(required=False)
    


class SEOMetaItem(BaseSchema):
    # Content swagger.json

    
    title = fields.Str(required=False)
    
    items = fields.List(fields.Nested(SEOMetaItems, required=False), required=False)
    


class SEOMetaItems(BaseSchema):
    # Content swagger.json

    
    key = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class SEOSitemap(BaseSchema):
    # Content swagger.json

    
    priority = fields.Float(required=False)
    
    frequency = fields.Str(required=False)
    


class SEObreadcrumb(BaseSchema):
    # Content swagger.json

    
    url = fields.Str(required=False)
    
    action = fields.Nested(Action, required=False)
    


class DefaultSitemapIndividualConfig(BaseSchema):
    # Content swagger.json

    
    enabled = fields.Boolean(required=False)
    


class DefaultSitemapConfig(BaseSchema):
    # Content swagger.json

    
    root = fields.Nested(DefaultSitemapIndividualConfig, required=False)
    
    brand = fields.Nested(DefaultSitemapIndividualConfig, required=False)
    
    collections = fields.Nested(DefaultSitemapIndividualConfig, required=False)
    
    category_l1 = fields.Nested(DefaultSitemapIndividualConfig, required=False)
    
    category_l2 = fields.Nested(DefaultSitemapIndividualConfig, required=False)
    
    category_l3 = fields.Nested(DefaultSitemapIndividualConfig, required=False)
    
    pages = fields.Nested(DefaultSitemapIndividualConfig, required=False)
    
    blog = fields.Nested(DefaultSitemapIndividualConfig, required=False)
    
    section = fields.Nested(DefaultSitemapIndividualConfig, required=False)
    
    faq = fields.Nested(DefaultSitemapIndividualConfig, required=False)
    
    sitemap = fields.Nested(DefaultSitemapIndividualConfig, required=False)
    


class SitemapConfig(BaseSchema):
    # Content swagger.json

    
    name = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    sitemap = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    


class SitemapConfigurationList(BaseSchema):
    # Content swagger.json

    
    items = fields.List(fields.Nested(SitemapConfig, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class DateMeta(BaseSchema):
    # Content swagger.json

    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    


class LocaleLanguage(BaseSchema):
    # Content swagger.json

    
    hi = fields.Nested(Language, required=False)
    
    ar = fields.Nested(Language, required=False)
    
    en_us = fields.Nested(Language, required=False)
    


class Language(BaseSchema):
    # Content swagger.json

    
    display = fields.Str(required=False)
    


class Action(BaseSchema):
    # Content swagger.json

    
    type = fields.Str(required=False)
    
    page = fields.Nested(ActionPage, required=False)
    
    popup = fields.Nested(ActionPage, required=False)
    


class NavigationReference(BaseSchema):
    # Content swagger.json

    
    acl = fields.List(fields.Str(required=False), required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    _locale_language = fields.Nested(LocaleLanguage, required=False)
    
    image = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    action = fields.Nested(Action, required=False)
    
    active = fields.Boolean(required=False)
    
    display = fields.Str(required=False)
    
    sort_order = fields.Int(required=False)
    
    sub_navigation = fields.List(fields.Nested(lambda: NavigationReference(exclude=('sub_navigation')), required=False), required=False)
    


class AnnouncementsResponseSchema(BaseSchema):
    # Content swagger.json

    
    announcements = fields.Dict(required=False)
    
    refresh_rate = fields.Int(required=False)
    
    refresh_pages = fields.List(fields.Str(required=False), required=False)
    


class FaqResponseSchema(BaseSchema):
    # Content swagger.json

    
    faqs = fields.List(fields.Nested(FaqSchema, required=False), required=False)
    


class DataLoaderSchema(BaseSchema):
    # Content swagger.json

    
    name = fields.Str(required=False)
    
    service = fields.Str(required=False)
    
    operation_id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    is_selected = fields.Boolean(required=False)
    
    created_at = fields.Str(required=False)
    
    modified_at = fields.Str(required=False)
    
    company = fields.Str(required=False)
    
    application = fields.Str(required=False)
    
    url = fields.Str(required=False)
    
    content = fields.Str(required=False)
    
    __source = fields.Nested(DataLoaderSourceSchema, required=False)
    
    _id = fields.Str(required=False)
    


class DataLoaderSourceSchema(BaseSchema):
    # Content swagger.json

    
    type = fields.Str(required=False)
    
    id = fields.Str(required=False)
    


class DataLoadersSchema(BaseSchema):
    # Content swagger.json

    
    items = fields.List(fields.Nested(DataLoaderSchema, required=False), required=False)
    


class ContentAPIError(BaseSchema):
    # Content swagger.json

    
    message = fields.Str(required=False)
    
    status = fields.Float(required=False)
    
    code = fields.Str(required=False)
    
    exception = fields.Str(required=False)
    
    info = fields.Str(required=False)
    
    request_id = fields.Str(required=False)
    
    stack_trace = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    


class CategorySchema(BaseSchema):
    # Content swagger.json

    
    index = fields.Int(required=False)
    
    title = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    children = fields.List(fields.Str(required=False), required=False)
    
    _id = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    application = fields.Str(required=False)
    
    icon_url = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    __v = fields.Float(required=False)
    


class ChildrenSchema(BaseSchema):
    # Content swagger.json

    
    question = fields.Str(required=False)
    
    answer = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    application = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    


class FAQCategorySchema(BaseSchema):
    # Content swagger.json

    
    index = fields.Int(required=False)
    
    title = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    children = fields.List(fields.Nested(ChildrenSchema, required=False), required=False)
    
    _id = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    application = fields.Str(required=False)
    
    icon_url = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    __v = fields.Float(required=False)
    


class FaqSchema(BaseSchema):
    # Content swagger.json

    
    slug = fields.Str(required=False)
    
    application = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    question = fields.Str(required=False)
    
    answer = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    __v = fields.Float(required=False)
    


class GetFaqSchema(BaseSchema):
    # Content swagger.json

    
    faqs = fields.List(fields.Nested(FaqSchema, required=False), required=False)
    


class GetFaqCategoriesSchema(BaseSchema):
    # Content swagger.json

    
    categories = fields.List(fields.Nested(CategorySchema, required=False), required=False)
    


class GetFaqCategoryBySlugSchema(BaseSchema):
    # Content swagger.json

    
    category = fields.Nested(FAQCategorySchema, required=False)
    


class Page(BaseSchema):
    # Content swagger.json

    
    item_total = fields.Int(required=False)
    
    next_id = fields.Str(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    has_next = fields.Boolean(required=False)
    
    current = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    size = fields.Int(required=False)
    
    total = fields.Int(required=False)
    


class LandingPageSchema(BaseSchema):
    # Content swagger.json

    
    slug = fields.Str(required=False)
    
    action = fields.Nested(Action, required=False)
    
    platform = fields.List(fields.Str(required=False), required=False)
    
    created_by = fields.Nested(CreatedBySchema, required=False)
    
    date_meta = fields.Nested(DateMeta, required=False)
    
    _id = fields.Str(required=False)
    
    application = fields.Str(required=False)
    
    archived = fields.Boolean(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    __v = fields.Float(required=False)
    


class NavigationGetResponseSchema(BaseSchema):
    # Content swagger.json

    
    items = fields.List(fields.Nested(NavigationSchema, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class Orientation(BaseSchema):
    # Content swagger.json

    
    portrait = fields.List(fields.Str(required=False), required=False)
    
    landscape = fields.List(fields.Str(required=False), required=False)
    


class NavigationSchema(BaseSchema):
    # Content swagger.json

    
    _id = fields.Str(required=False)
    
    application = fields.Str(required=False)
    
    archived = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    platform = fields.List(fields.Str(required=False), required=False)
    
    created_by = fields.Nested(CreatedBySchema, required=False)
    
    date_meta = fields.Nested(DateMeta, required=False)
    
    orientation = fields.Nested(Orientation, required=False)
    
    version = fields.Float(required=False)
    
    navigation = fields.List(fields.Nested(NavigationReference, required=False), required=False)
    
    __v = fields.Float(required=False)
    


class PageGetResponseSchema(BaseSchema):
    # Content swagger.json

    
    items = fields.List(fields.Nested(PageSchema, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class PageSchema(BaseSchema):
    # Content swagger.json

    
    _id = fields.Str(required=False)
    
    application = fields.Str(required=False)
    
    component_ids = fields.List(fields.Str(required=False), required=False)
    
    content = fields.List(fields.Dict(required=False), required=False)
    
    content_path = fields.Str(required=False)
    
    created_by = fields.Nested(CreatedBySchema, required=False)
    
    date_meta = fields.Nested(DateMeta, required=False)
    
    description = fields.Str(required=False)
    
    feature_image = fields.Nested(Asset, required=False)
    
    page_meta = fields.List(fields.Dict(required=False), required=False)
    
    _schedule = fields.Nested(ScheduleSchema, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    orientation = fields.Str(required=False)
    
    platform = fields.Str(required=False)
    
    published = fields.Boolean(required=False)
    
    slug = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    title = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    seo = fields.Nested(SEO, required=False)
    
    visibility = fields.Dict(required=False)
    
    archived = fields.Boolean(required=False)
    
    __v = fields.Float(required=False)
    
    sanitized_content = fields.List(fields.Nested(SanitizedContent, required=False), required=False)
    


class SanitizedContent(BaseSchema):
    # Content swagger.json

    
    type = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class CreatedBySchema(BaseSchema):
    # Content swagger.json

    
    id = fields.Str(required=False)
    


class Support(BaseSchema):
    # Content swagger.json

    
    created = fields.Boolean(required=False)
    
    _id = fields.Str(required=False)
    
    application = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    contact = fields.Nested(ContactSchema, required=False)
    


class PhoneProperties(BaseSchema):
    # Content swagger.json

    
    key = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    number = fields.Str(required=False)
    
    phone_type = fields.Str(required=False)
    


class PhoneSchema(BaseSchema):
    # Content swagger.json

    
    active = fields.Boolean(required=False)
    
    phone = fields.List(fields.Nested(PhoneProperties, required=False), required=False)
    


class EmailProperties(BaseSchema):
    # Content swagger.json

    
    key = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class EmailSchema(BaseSchema):
    # Content swagger.json

    
    active = fields.Boolean(required=False)
    
    email = fields.List(fields.Nested(EmailProperties, required=False), required=False)
    


class ContactSchema(BaseSchema):
    # Content swagger.json

    
    phone = fields.Nested(PhoneSchema, required=False)
    
    email = fields.Nested(EmailSchema, required=False)
    


class TagsSchema(BaseSchema):
    # Content swagger.json

    
    application = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    company = fields.Str(required=False)
    
    tags = fields.List(fields.Nested(TagSchema, required=False), required=False)
    
    __v = fields.Float(required=False)
    


class TagSchema(BaseSchema):
    # Content swagger.json

    
    name = fields.Str(required=False)
    
    url = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    sub_type = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    position = fields.Str(required=False)
    
    attributes = fields.Dict(required=False)
    
    content = fields.Str(required=False)
    
    compatible_engines = fields.List(fields.Str(required=False), required=False)
    
    pages = fields.List(fields.Dict(required=False), required=False)
    
    __source = fields.Nested(TagSourceSchema, required=False)
    


class TagSourceSchema(BaseSchema):
    # Content swagger.json

    
    type = fields.Str(required=False)
    
    id = fields.Str(required=False)
    


class WellKnownResponseSchema(BaseSchema):
    # Content swagger.json

    
    _id = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    application_id = fields.Str(required=False)
    
    content = fields.Str(required=False)
    
    content_type = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    


class CustomObjectListItemDefinationSchema(BaseSchema):
    # Content swagger.json

    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class CustomObjectFieldSchema(BaseSchema):
    # Content swagger.json

    
    _id = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    definition_id = fields.Str(required=False)
    


class CustomObjectByIdSchema(BaseSchema):
    # Content swagger.json

    
    id = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    definition = fields.Nested(CustomObjectListItemDefinationSchema, required=False)
    
    references = fields.List(fields.Raw(required=False), required=False)
    
    fields = fields.List(fields.Nested(CustomObjectFieldSchema, required=False), required=False)
    


class CustomFieldSchema(BaseSchema):
    # Content swagger.json

    
    _id = fields.Str(required=False)
    
    namespace = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    resource = fields.Str(required=False)
    
    resource_id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    multi_value = fields.Boolean(required=False)
    
    company_id = fields.Str(required=False)
    
    application_id = fields.Str(required=False)
    
    definition_id = fields.Str(required=False)
    
    has_invalid_values = fields.Boolean(required=False)
    
    invalid_value_errors = fields.List(fields.Raw(required=False), required=False)
    
    is_deleted = fields.Boolean(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    


class CustomFieldsResponseByResourceIdSchema(BaseSchema):
    # Content swagger.json

    
    items = fields.List(fields.Nested(CustomFieldSchema, required=False), required=False)
    


class ActionPage(BaseSchema):
    # Content swagger.json

    
    params = fields.Dict(required=False)
    
    query = fields.Dict(required=False)
    
    url = fields.Str(required=False)
    
    type = fields.Str(required=False, validate=OneOf([val.value for val in PageType.__members__.values()]))
    


