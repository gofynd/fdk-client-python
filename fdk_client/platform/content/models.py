"""Content Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema


from .enums import *



class GenerateSEOContent(BaseSchema):
    pass


class GeneratedSEOContent(BaseSchema):
    pass


class ApplicationLegal(BaseSchema):
    pass


class ApplicationLegalFAQ(BaseSchema):
    pass


class PathMappingSchema(BaseSchema):
    pass


class PathSourceSchema(BaseSchema):
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


class SEOSchemaMarkupTemplateRequestBody(BaseSchema):
    pass


class AnnouncementPageSchema(BaseSchema):
    pass


class EditorMeta(BaseSchema):
    pass


class AnnouncementAuthorSchema(BaseSchema):
    pass


class AdminAnnouncementSchema(BaseSchema):
    pass


class DefaultSchemaComponent(BaseSchema):
    pass


class DefaultSEOSchemaMarkupTemplate(BaseSchema):
    pass


class ScheduleSchema(BaseSchema):
    pass


class NextSchedule(BaseSchema):
    pass


class BlogGetResponse(BaseSchema):
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


class DateMeta(BaseSchema):
    pass


class BlogRequest(BaseSchema):
    pass


class GetAnnouncementListSchema(BaseSchema):
    pass


class CreateAnnouncementSchema(BaseSchema):
    pass


class DataLoaderResponseSchema(BaseSchema):
    pass


class DataLoaderResetResponseSchema(BaseSchema):
    pass


class LocaleLanguage(BaseSchema):
    pass


class Language(BaseSchema):
    pass


class Action(BaseSchema):
    pass


class ActionPage(BaseSchema):
    pass


class NavigationReference(BaseSchema):
    pass


class ConfigurationSchema(BaseSchema):
    pass


class SlideshowMedia(BaseSchema):
    pass


class UpdateHandpickedSchema(BaseSchema):
    pass


class HandpickedTagSchema(BaseSchema):
    pass


class RemoveHandpickedSchema(BaseSchema):
    pass


class CreateTagSchema(BaseSchema):
    pass


class CreateTagRequestSchema(BaseSchema):
    pass


class DataLoaderSchema(BaseSchema):
    pass


class DataLoaderSourceSchema(BaseSchema):
    pass


class DataLoadersSchema(BaseSchema):
    pass


class TagDeleteSuccessResponse(BaseSchema):
    pass


class ContentAPIError(BaseSchema):
    pass


class CommonError(BaseSchema):
    pass


class CategorySchema(BaseSchema):
    pass


class ChildrenSchema(BaseSchema):
    pass


class CategoryRequestSchema(BaseSchema):
    pass


class FAQCategorySchema(BaseSchema):
    pass


class FaqSchema(BaseSchema):
    pass


class FAQ(BaseSchema):
    pass


class CreateFaqResponseSchema(BaseSchema):
    pass


class CreateFaqSchema(BaseSchema):
    pass


class GetFaqSchema(BaseSchema):
    pass


class UpdateFaqCategoryRequestSchema(BaseSchema):
    pass


class CreateFaqCategoryRequestSchema(BaseSchema):
    pass


class CreateFaqCategorySchema(BaseSchema):
    pass


class GetFaqCategoriesSchema(BaseSchema):
    pass


class GetFaqCategoryBySlugSchema(BaseSchema):
    pass


class Page(BaseSchema):
    pass


class LandingPageGetResponse(BaseSchema):
    pass


class LandingPageSchema(BaseSchema):
    pass


class DefaultNavigationResponse(BaseSchema):
    pass


class NavigationGetResponse(BaseSchema):
    pass


class Orientation(BaseSchema):
    pass


class NavigationSchema(BaseSchema):
    pass


class NavigationRequest(BaseSchema):
    pass


class PageGetResponse(BaseSchema):
    pass


class PageSpec(BaseSchema):
    pass


class PageSpecParam(BaseSchema):
    pass


class PageSpecItem(BaseSchema):
    pass


class PageSchema(BaseSchema):
    pass


class CreatedBySchema(BaseSchema):
    pass


class PageRequest(BaseSchema):
    pass


class CronSchedule(BaseSchema):
    pass


class PagePublishRequest(BaseSchema):
    pass


class PageMetaSchema(BaseSchema):
    pass


class SlideshowGetResponse(BaseSchema):
    pass


class SlideshowSchema(BaseSchema):
    pass


class SlideshowRequest(BaseSchema):
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


class ResourcesSchema(BaseSchema):
    pass


class ResourceSchema(BaseSchema):
    pass


class FieldValidations(BaseSchema):
    pass


class FieldDefinitionSchema(BaseSchema):
    pass


class CustomFieldDefinitionsSchema(BaseSchema):
    pass


class CustomFieldDefinitionRequestSchema(BaseSchema):
    pass


class CustomObjectCustomFieldDefinitions(BaseSchema):
    pass


class CustomObjectDefinitionUpdateRequestSchema(BaseSchema):
    pass


class CustomFieldDefinitionDetailResSchema(BaseSchema):
    pass


class CustomDataDeleteSchema(BaseSchema):
    pass


class CustomFieldValue(BaseSchema):
    pass


class CustomFieldSchema(BaseSchema):
    pass


class CustomFieldsResponseSchema(BaseSchema):
    pass


class CustomFieldsResponseByResourceIdSchema(BaseSchema):
    pass


class CustomField(BaseSchema):
    pass


class CustomFieldRequestSchema(BaseSchema):
    pass


class CustomObjectSchema(BaseSchema):
    pass


class CustomObjectDefinitionRequestSchema(BaseSchema):
    pass


class CustomObjectCustomFieldDefinitionResSchema(BaseSchema):
    pass


class CustomObjectDefinitionSchema(BaseSchema):
    pass


class CustomObjectDefinitionDeleteResponseSchema(BaseSchema):
    pass


class CustomObjectEntryBulkUploadResponse(BaseSchema):
    pass


class CustomObjectListItemDefinationSchema(BaseSchema):
    pass


class CustomObjectListItemSchema(BaseSchema):
    pass


class CustomObjectsSchema(BaseSchema):
    pass


class CustomObjectFieldSchema(BaseSchema):
    pass


class CustomObjectByIdSchema(BaseSchema):
    pass


class CustomObjectBulkEntryInitiateDownload(BaseSchema):
    pass


class CustomObjectMetaSchema(BaseSchema):
    pass


class CustomObjectJobSchema(BaseSchema):
    pass


class CustomObjectBulkEntry(BaseSchema):
    pass


class CustomFieldTypeSchema(BaseSchema):
    pass


class SupportedValidationsMetaExampleSchema(BaseSchema):
    pass


class SupportedValidationsMetaSchema(BaseSchema):
    pass


class SupportedValidationsSchema(BaseSchema):
    pass


class StringSingleLine(BaseSchema):
    pass


class StringMultiLine(BaseSchema):
    pass


class Dropdown(BaseSchema):
    pass


class Integer(BaseSchema):
    pass


class FloatType(BaseSchema):
    pass


class BooleanType(BaseSchema):
    pass


class Date(BaseSchema):
    pass


class Datetime(BaseSchema):
    pass


class Json(BaseSchema):
    pass


class File(BaseSchema):
    pass


class Url(BaseSchema):
    pass


class Metaobject(BaseSchema):
    pass


class Product(BaseSchema):
    pass


class CustomObjectEntry(BaseSchema):
    pass


class CustomObjectDefinitionsSchema(BaseSchema):
    pass


class CustomObjectEntryFieldSchema(BaseSchema):
    pass


class CustomObjectRequestSchema(BaseSchema):
    pass


class CustomObjectBulkSchema(BaseSchema):
    pass





class GenerateSEOContent(BaseSchema):
    # Content swagger.json

    
    text = fields.Str(required=False)
    
    existing_text = fields.Str(required=False)
    
    keywords = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    


class GeneratedSEOContent(BaseSchema):
    # Content swagger.json

    
    title = fields.Str(required=False)
    
    description = fields.Str(required=False)
    


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
    


class ApplicationLegalFAQ(BaseSchema):
    # Content swagger.json

    
    question = fields.Str(required=False)
    
    answer = fields.Str(required=False)
    


class PathMappingSchema(BaseSchema):
    # Content swagger.json

    
    application = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    redirect_from = fields.Str(required=False)
    
    redirect_to = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    __source = fields.Nested(PathSourceSchema, required=False)
    


class PathSourceSchema(BaseSchema):
    # Content swagger.json

    
    type = fields.Str(required=False)
    
    id = fields.Str(required=False)
    


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
    
    cannonical_enabled = fields.Boolean(required=False)
    
    custom_meta_tags = fields.List(fields.Nested(CustomMetaTag, required=False), required=False)
    
    details = fields.Nested(Detail, required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    


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
    
    page = fields.Nested(Page, required=False)
    


class SEOSchemaMarkupTemplate(BaseSchema):
    # Content swagger.json

    
    id = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    page_type = fields.Str(required=False)
    
    schema = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    active = fields.Boolean(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    application = fields.Str(required=False)
    
    target_json = fields.Dict(required=False)
    


class SEOSchemaMarkupTemplateRequestBody(BaseSchema):
    # Content swagger.json

    
    title = fields.Str(required=False)
    
    page_type = fields.Str(required=False)
    
    schema = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    target_json = fields.Dict(required=False)
    
    active = fields.Boolean(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    


class AnnouncementPageSchema(BaseSchema):
    # Content swagger.json

    
    page_slug = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class EditorMeta(BaseSchema):
    # Content swagger.json

    
    foreground_color = fields.Str(required=False)
    
    background_color = fields.Str(required=False)
    
    content_type = fields.Str(required=False)
    
    content = fields.Str(required=False)
    


class AnnouncementAuthorSchema(BaseSchema):
    # Content swagger.json

    
    created_by = fields.Str(required=False)
    
    modified_by = fields.Str(required=False)
    


class AdminAnnouncementSchema(BaseSchema):
    # Content swagger.json

    
    _id = fields.Str(required=False)
    
    platforms = fields.List(fields.Str(required=False), required=False)
    
    title = fields.Str(required=False)
    
    announcement = fields.Str(required=False)
    
    pages = fields.List(fields.Nested(AnnouncementPageSchema, required=False), required=False)
    
    editor_meta = fields.Nested(EditorMeta, required=False)
    
    author = fields.Nested(AnnouncementAuthorSchema, required=False)
    
    created_at = fields.Str(required=False)
    
    app = fields.Str(required=False)
    
    modified_at = fields.Str(required=False)
    
    _schedule = fields.Nested(ScheduleSchema, required=False)
    


class DefaultSchemaComponent(BaseSchema):
    # Content swagger.json

    
    items = fields.List(fields.Nested(DefaultSEOSchemaMarkupTemplate, required=False), required=False)
    


class DefaultSEOSchemaMarkupTemplate(BaseSchema):
    # Content swagger.json

    
    page_type = fields.Str(required=False)
    
    schema = fields.Str(required=False)
    
    target_json = fields.Dict(required=False)
    


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
    


class BlogGetResponse(BaseSchema):
    # Content swagger.json

    
    items = fields.List(fields.Nested(BlogSchema, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


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
    
    seo = fields.Nested(SEO, required=False)
    
    _schedule = fields.Nested(CronSchedule, required=False)
    
    title = fields.Str(required=False)
    
    date_meta = fields.Nested(DateMeta, required=False)
    


class SEO(BaseSchema):
    # Content swagger.json

    
    description = fields.Str(required=False)
    
    image = fields.Nested(SEOImage, required=False)
    
    title = fields.Str(required=False)
    
    meta_tags = fields.List(fields.Nested(SEOMetaItem, required=False), required=False)
    
    sitemap = fields.Nested(SEOSitemap, required=False)
    
    breadcrumb = fields.List(fields.Nested(SEObreadcrumb, required=False), required=False)
    
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
    


class DateMeta(BaseSchema):
    # Content swagger.json

    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    


class BlogRequest(BaseSchema):
    # Content swagger.json

    
    application = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    author = fields.Nested(Author, required=False)
    
    content = fields.List(fields.Nested(ResourceContent, required=False), required=False)
    
    feature_image = fields.Nested(Asset, required=False)
    
    published = fields.Boolean(required=False)
    
    reading_time = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    title = fields.Str(required=False)
    
    seo = fields.Nested(SEO, required=False)
    
    _schedule = fields.Nested(CronSchedule, required=False)
    


class GetAnnouncementListSchema(BaseSchema):
    # Content swagger.json

    
    items = fields.List(fields.Nested(AdminAnnouncementSchema, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class CreateAnnouncementSchema(BaseSchema):
    # Content swagger.json

    
    message = fields.Str(required=False)
    
    data = fields.Nested(AdminAnnouncementSchema, required=False)
    


class DataLoaderResponseSchema(BaseSchema):
    # Content swagger.json

    
    application = fields.Str(required=False)
    
    company = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    service = fields.Str(required=False)
    
    operation_id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    url = fields.Str(required=False)
    
    content = fields.Str(required=False)
    
    __source = fields.Nested(DataLoaderSourceSchema, required=False)
    


class DataLoaderResetResponseSchema(BaseSchema):
    # Content swagger.json

    
    reset = fields.Boolean(required=False)
    


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

    
    page = fields.Nested(ActionPage, required=False)
    
    popup = fields.Nested(ActionPage, required=False)
    
    type = fields.Str(required=False)
    


class ActionPage(BaseSchema):
    # Content swagger.json

    
    params = fields.Dict(required=False)
    
    query = fields.Dict(required=False)
    
    url = fields.Str(required=False)
    
    type = fields.Str(required=False, validate=OneOf([val.value for val in PageType.__members__.values()]))
    


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
    


class ConfigurationSchema(BaseSchema):
    # Content swagger.json

    
    sleep_time = fields.Int(required=False)
    
    start_on_launch = fields.Boolean(required=False)
    
    duration = fields.Int(required=False)
    
    slide_direction = fields.Str(required=False)
    


class SlideshowMedia(BaseSchema):
    # Content swagger.json

    
    type = fields.Str(required=False)
    
    url = fields.Str(required=False)
    
    bg_color = fields.Str(required=False)
    
    duration = fields.Int(required=False)
    
    auto_decide_duration = fields.Boolean(required=False)
    
    action = fields.Nested(Action, required=False)
    


class UpdateHandpickedSchema(BaseSchema):
    # Content swagger.json

    
    tag = fields.Nested(HandpickedTagSchema, required=False)
    


class HandpickedTagSchema(BaseSchema):
    # Content swagger.json

    
    position = fields.Str(required=False)
    
    attributes = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    
    url = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    sub_type = fields.Str(required=False)
    
    content = fields.Str(required=False)
    


class RemoveHandpickedSchema(BaseSchema):
    # Content swagger.json

    
    tags = fields.List(fields.Str(required=False), required=False)
    


class CreateTagSchema(BaseSchema):
    # Content swagger.json

    
    name = fields.Str(required=False)
    
    sub_type = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    url = fields.Str(required=False)
    
    position = fields.Str(required=False)
    
    attributes = fields.Dict(required=False)
    
    pages = fields.List(fields.Dict(required=False), required=False)
    
    content = fields.Str(required=False)
    


class CreateTagRequestSchema(BaseSchema):
    # Content swagger.json

    
    tags = fields.List(fields.Nested(CreateTagSchema, required=False), required=False)
    


class DataLoaderSchema(BaseSchema):
    # Content swagger.json

    
    name = fields.Str(required=False)
    
    service = fields.Str(required=False)
    
    operation_id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
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
    


class TagDeleteSuccessResponse(BaseSchema):
    # Content swagger.json

    
    success = fields.Boolean(required=False)
    


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
    


class CommonError(BaseSchema):
    # Content swagger.json

    
    message = fields.Str(required=False)
    


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
    


class ChildrenSchema(BaseSchema):
    # Content swagger.json

    
    question = fields.Str(required=False)
    
    answer = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    application = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    


class CategoryRequestSchema(BaseSchema):
    # Content swagger.json

    
    slug = fields.Str(required=False)
    
    title = fields.Str(required=False)
    


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
    


class FaqSchema(BaseSchema):
    # Content swagger.json

    
    slug = fields.Str(required=False)
    
    application = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    question = fields.Str(required=False)
    
    answer = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    


class FAQ(BaseSchema):
    # Content swagger.json

    
    slug = fields.Str(required=False)
    
    question = fields.Str(required=False)
    
    answer = fields.Str(required=False)
    


class CreateFaqResponseSchema(BaseSchema):
    # Content swagger.json

    
    faq = fields.Nested(FaqSchema, required=False)
    


class CreateFaqSchema(BaseSchema):
    # Content swagger.json

    
    faq = fields.Nested(FAQ, required=False)
    


class GetFaqSchema(BaseSchema):
    # Content swagger.json

    
    faqs = fields.List(fields.Nested(FaqSchema, required=False), required=False)
    


class UpdateFaqCategoryRequestSchema(BaseSchema):
    # Content swagger.json

    
    category = fields.Nested(CategorySchema, required=False)
    


class CreateFaqCategoryRequestSchema(BaseSchema):
    # Content swagger.json

    
    category = fields.Nested(CategoryRequestSchema, required=False)
    


class CreateFaqCategorySchema(BaseSchema):
    # Content swagger.json

    
    category = fields.Nested(CategorySchema, required=False)
    


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
    


class LandingPageGetResponse(BaseSchema):
    # Content swagger.json

    
    items = fields.List(fields.Nested(LandingPageSchema, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


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
    


class DefaultNavigationResponse(BaseSchema):
    # Content swagger.json

    
    items = fields.List(fields.Nested(NavigationSchema, required=False), required=False)
    


class NavigationGetResponse(BaseSchema):
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
    


class NavigationRequest(BaseSchema):
    # Content swagger.json

    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    platform = fields.List(fields.Str(required=False), required=False)
    
    orientation = fields.Nested(Orientation, required=False)
    
    navigation = fields.List(fields.Nested(NavigationReference, required=False), required=False)
    


class PageGetResponse(BaseSchema):
    # Content swagger.json

    
    items = fields.List(fields.Nested(PageSchema, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class PageSpec(BaseSchema):
    # Content swagger.json

    
    specifications = fields.List(fields.Nested(PageSpecItem, required=False), required=False)
    


class PageSpecParam(BaseSchema):
    # Content swagger.json

    
    key = fields.Str(required=False)
    
    required = fields.Boolean(required=False)
    


class PageSpecItem(BaseSchema):
    # Content swagger.json

    
    page_type = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    params = fields.List(fields.Nested(PageSpecParam, required=False), required=False)
    
    query = fields.List(fields.Nested(PageSpecParam, required=False), required=False)
    


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
    


class CreatedBySchema(BaseSchema):
    # Content swagger.json

    
    id = fields.Str(required=False)
    


class PageRequest(BaseSchema):
    # Content swagger.json

    
    _schedule = fields.Nested(CronSchedule, required=False)
    
    application = fields.Str(required=False)
    
    author = fields.Nested(Author, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    orientation = fields.Str(required=False)
    
    content = fields.List(fields.Dict(required=False), required=False)
    
    feature_image = fields.Nested(Asset, required=False)
    
    published = fields.Boolean(required=False)
    
    reading_time = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    seo = fields.Nested(SEO, required=False)
    
    title = fields.Str(required=False)
    


class CronSchedule(BaseSchema):
    # Content swagger.json

    
    cron = fields.Str(required=False)
    
    start = fields.Str(required=False)
    
    end = fields.Str(required=False)
    
    duration = fields.Float(required=False)
    


class PagePublishRequest(BaseSchema):
    # Content swagger.json

    
    publish = fields.Boolean(required=False)
    


class PageMetaSchema(BaseSchema):
    # Content swagger.json

    
    system_pages = fields.List(fields.Nested(NavigationSchema, required=False), required=False)
    
    custom_pages = fields.List(fields.Nested(PageSchema, required=False), required=False)
    
    application_id = fields.Str(required=False)
    


class SlideshowGetResponse(BaseSchema):
    # Content swagger.json

    
    items = fields.List(fields.Nested(SlideshowSchema, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class SlideshowSchema(BaseSchema):
    # Content swagger.json

    
    _id = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    date_meta = fields.Nested(DateMeta, required=False)
    
    application = fields.Str(required=False)
    
    platform = fields.Str(required=False)
    
    configuration = fields.Nested(ConfigurationSchema, required=False)
    
    media = fields.List(fields.Nested(SlideshowMedia, required=False), required=False)
    
    active = fields.Boolean(required=False)
    
    archived = fields.Boolean(required=False)
    
    _custom_json = fields.Dict(required=False)
    


class SlideshowRequest(BaseSchema):
    # Content swagger.json

    
    slug = fields.Str(required=False)
    
    platform = fields.Str(required=False)
    
    configuration = fields.Nested(ConfigurationSchema, required=False)
    
    media = fields.Nested(SlideshowMedia, required=False)
    
    active = fields.Boolean(required=False)
    


class Support(BaseSchema):
    # Content swagger.json

    
    created = fields.Boolean(required=False)
    
    _id = fields.Str(required=False)
    
    config_type = fields.Str(required=False)
    
    application = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    contact = fields.Nested(ContactSchema, required=False)
    


class PhoneProperties(BaseSchema):
    # Content swagger.json

    
    key = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    number = fields.Str(required=False)
    


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
    
    tags = fields.List(fields.Nested(TagSchema, required=False), required=False)
    


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
    
    pages = fields.List(fields.Dict(required=False), required=False)
    
    __source = fields.Nested(TagSourceSchema, required=False)
    


class TagSourceSchema(BaseSchema):
    # Content swagger.json

    
    type = fields.Str(required=False)
    
    id = fields.Str(required=False)
    


class ResourcesSchema(BaseSchema):
    # Content swagger.json

    
    resources = fields.List(fields.Nested(ResourceSchema, required=False), required=False)
    


class ResourceSchema(BaseSchema):
    # Content swagger.json

    
    name = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
    definitions_count = fields.Float(required=False)
    


class FieldValidations(BaseSchema):
    # Content swagger.json

    
    name = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    value = fields.Raw(required=False)
    


class FieldDefinitionSchema(BaseSchema):
    # Content swagger.json

    
    _id = fields.Str(required=False)
    
    creator = fields.Str(required=False)
    
    resource = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    namespace = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    multi_value = fields.Boolean(required=False)
    
    validations = fields.List(fields.Nested(FieldValidations, required=False), required=False)
    
    company_id = fields.Str(required=False)
    
    created_by = fields.Str(required=False)
    
    updated_by = fields.Str(required=False)
    
    required = fields.Boolean(required=False)
    
    is_deleted = fields.Boolean(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    type_name = fields.Str(required=False)
    
    invalid_fields_count = fields.Int(required=False)
    


class CustomFieldDefinitionsSchema(BaseSchema):
    # Content swagger.json

    
    items = fields.List(fields.Nested(FieldDefinitionSchema, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class CustomFieldDefinitionRequestSchema(BaseSchema):
    # Content swagger.json

    
    resource = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
    namespace = fields.Str(required=False)
    
    multi_value = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    validations = fields.List(fields.Nested(FieldValidations, required=False), required=False)
    


class CustomObjectCustomFieldDefinitions(BaseSchema):
    # Content swagger.json

    
    id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    multi_value = fields.Boolean(required=False)
    
    required = fields.Boolean(required=False)
    
    key = fields.Str(required=False)
    
    validations = fields.List(fields.Nested(FieldValidations, required=False), required=False)
    
    action = fields.Str(required=False)
    


class CustomObjectDefinitionUpdateRequestSchema(BaseSchema):
    # Content swagger.json

    
    type = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    display_name_key = fields.Str(required=False)
    
    field_definitions = fields.List(fields.Nested(CustomObjectCustomFieldDefinitions, required=False), required=False)
    


class CustomFieldDefinitionDetailResSchema(BaseSchema):
    # Content swagger.json

    
    creator = fields.Str(required=False)
    
    resource = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    namespace = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    multi_value = fields.Boolean(required=False)
    
    company_id = fields.Str(required=False)
    
    application_id = fields.Str(required=False)
    
    created_by = fields.Str(required=False)
    
    updated_by = fields.Str(required=False)
    
    required = fields.Boolean(required=False)
    
    is_deleted = fields.Boolean(required=False)
    
    _id = fields.Str(required=False)
    
    validations = fields.List(fields.Raw(required=False), required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    


class CustomDataDeleteSchema(BaseSchema):
    # Content swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class CustomFieldValue(BaseSchema):
    # Content swagger.json

    
    value = fields.Raw(required=False)
    


class CustomFieldSchema(BaseSchema):
    # Content swagger.json

    
    _id = fields.Str(required=False)
    
    namespace = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
    resource = fields.Str(required=False)
    
    creator = fields.Str(required=False)
    
    value = fields.List(fields.Nested(CustomFieldValue, required=False), required=False)
    
    resource_id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    multi_value = fields.Boolean(required=False)
    
    company_id = fields.Str(required=False)
    
    definition_id = fields.Str(required=False)
    
    has_invalid_values = fields.Boolean(required=False)
    
    invalid_value_errors = fields.List(fields.Raw(required=False), required=False)
    
    created_by = fields.Str(required=False)
    
    is_deleted = fields.Boolean(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    


class CustomFieldsResponseSchema(BaseSchema):
    # Content swagger.json

    
    items = fields.List(fields.Nested(CustomFieldSchema, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class CustomFieldsResponseByResourceIdSchema(BaseSchema):
    # Content swagger.json

    
    items = fields.List(fields.Nested(CustomFieldSchema, required=False), required=False)
    


class CustomField(BaseSchema):
    # Content swagger.json

    
    value = fields.List(fields.Raw(required=False), required=False)
    
    definition_id = fields.Str(required=False)
    


class CustomFieldRequestSchema(BaseSchema):
    # Content swagger.json

    
    fields = fields.List(fields.Nested(CustomField, required=False), required=False)
    


class CustomObjectSchema(BaseSchema):
    # Content swagger.json

    
    _id = fields.Str(required=False)
    
    creator = fields.Str(required=False)
    
    company_id = fields.Str(required=False)
    
    application_id = fields.Str(required=False)
    
    created_by = fields.Str(required=False)
    
    updated_by = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    definition_id = fields.Str(required=False)
    
    fields = fields.List(fields.Nested(CustomFieldSchema, required=False), required=False)
    


class CustomObjectDefinitionRequestSchema(BaseSchema):
    # Content swagger.json

    
    type = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    display_name_key = fields.Str(required=False)
    
    field_definitions = fields.List(fields.Nested(CustomObjectCustomFieldDefinitions, required=False), required=False)
    


class CustomObjectCustomFieldDefinitionResSchema(BaseSchema):
    # Content swagger.json

    
    creator = fields.Str(required=False)
    
    resource = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    namespace = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    multi_value = fields.Boolean(required=False)
    
    validations = fields.List(fields.Nested(FieldValidations, required=False), required=False)
    
    company_id = fields.Str(required=False)
    
    created_by = fields.Str(required=False)
    
    metaobject_definition_id = fields.Str(required=False)
    
    required = fields.Boolean(required=False)
    
    is_deleted = fields.Boolean(required=False)
    
    _id = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    


class CustomObjectDefinitionSchema(BaseSchema):
    # Content swagger.json

    
    _id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    display_name_key = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    creator = fields.Str(required=False)
    
    created_by = fields.Str(required=False)
    
    updated_by = fields.Str(required=False)
    
    field_definitions = fields.List(fields.Nested(CustomObjectCustomFieldDefinitionResSchema, required=False), required=False)
    


class CustomObjectDefinitionDeleteResponseSchema(BaseSchema):
    # Content swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class CustomObjectEntryBulkUploadResponse(BaseSchema):
    # Content swagger.json

    
    url = fields.Str(required=False)
    
    total_records = fields.Int(required=False)
    


class CustomObjectListItemDefinationSchema(BaseSchema):
    # Content swagger.json

    
    _id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class CustomObjectListItemSchema(BaseSchema):
    # Content swagger.json

    
    _id = fields.Str(required=False)
    
    definition_id = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    definition = fields.Nested(CustomObjectListItemDefinationSchema, required=False)
    
    references = fields.Int(required=False)
    


class CustomObjectsSchema(BaseSchema):
    # Content swagger.json

    
    items = fields.List(fields.Nested(CustomObjectListItemSchema, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class CustomObjectFieldSchema(BaseSchema):
    # Content swagger.json

    
    _id = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
    value = fields.List(fields.Raw(required=False), required=False)
    
    type = fields.Str(required=False)
    
    definition_id = fields.Str(required=False)
    


class CustomObjectByIdSchema(BaseSchema):
    # Content swagger.json

    
    _id = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    definition = fields.Nested(CustomObjectListItemDefinationSchema, required=False)
    
    references = fields.List(fields.Raw(required=False), required=False)
    
    fields = fields.List(fields.Nested(CustomObjectFieldSchema, required=False), required=False)
    


class CustomObjectBulkEntryInitiateDownload(BaseSchema):
    # Content swagger.json

    
    message = fields.Str(required=False)
    
    task_id = fields.Str(required=False)
    


class CustomObjectMetaSchema(BaseSchema):
    # Content swagger.json

    
    mo_total_count = fields.Int(required=False)
    
    mo_success_count = fields.Int(required=False)
    
    mo_error_count = fields.Int(required=False)
    
    mo_defintion_type = fields.Str(required=False)
    


class CustomObjectJobSchema(BaseSchema):
    # Content swagger.json

    
    _id = fields.Str(required=False)
    
    jobs = fields.List(fields.Str(required=False), required=False)
    
    finished_jobs = fields.List(fields.Str(required=False), required=False)
    
    error_jobs = fields.List(fields.Str(required=False), required=False)
    
    errors_occured = fields.List(fields.Str(required=False), required=False)
    
    company_id = fields.Str(required=False)
    
    creator = fields.Str(required=False)
    
    url = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    action_type = fields.Str(required=False)
    
    entity = fields.Str(required=False)
    
    error_url = fields.Str(required=False)
    
    finished_count = fields.Int(required=False)
    
    error_count = fields.Int(required=False)
    
    success_count = fields.Int(required=False)
    
    total_jobs = fields.Int(required=False)
    
    meta = fields.Nested(CustomObjectMetaSchema, required=False)
    
    created_by = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    


class CustomObjectBulkEntry(BaseSchema):
    # Content swagger.json

    
    items = fields.List(fields.Nested(CustomObjectJobSchema, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class CustomFieldTypeSchema(BaseSchema):
    # Content swagger.json

    
    string_single_line = fields.Nested(StringSingleLine, required=False)
    
    string_multi_line = fields.Nested(StringMultiLine, required=False)
    
    dropdown = fields.Nested(Dropdown, required=False)
    
    integer = fields.Nested(Integer, required=False)
    
    float_type = fields.Nested(FloatType, required=False)
    
    boolean_type = fields.Nested(BooleanType, required=False)
    
    date = fields.Nested(Date, required=False)
    
    datetime = fields.Nested(Datetime, required=False)
    
    json = fields.Nested(Json, required=False)
    
    file = fields.Nested(File, required=False)
    
    url = fields.Nested(Url, required=False)
    
    metaobject = fields.Nested(Metaobject, required=False)
    
    product = fields.Nested(Product, required=False)
    


class SupportedValidationsMetaExampleSchema(BaseSchema):
    # Content swagger.json

    
    name = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class SupportedValidationsMetaSchema(BaseSchema):
    # Content swagger.json

    
    examples = fields.List(fields.Nested(SupportedValidationsMetaExampleSchema, required=False), required=False)
    


class SupportedValidationsSchema(BaseSchema):
    # Content swagger.json

    
    name = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    display = fields.Str(required=False)
    
    required = fields.Boolean(required=False)
    
    meta = fields.Nested(SupportedValidationsMetaSchema, required=False)
    


class StringSingleLine(BaseSchema):
    # Content swagger.json

    
    name = fields.Str(required=False)
    
    list_enabled = fields.Boolean(required=False)
    
    category = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    supported_validations = fields.List(fields.Nested(SupportedValidationsSchema, required=False), required=False)
    


class StringMultiLine(BaseSchema):
    # Content swagger.json

    
    name = fields.Str(required=False)
    
    list_enabled = fields.Boolean(required=False)
    
    category = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    supported_validations = fields.List(fields.Nested(SupportedValidationsSchema, required=False), required=False)
    


class Dropdown(BaseSchema):
    # Content swagger.json

    
    name = fields.Str(required=False)
    
    list_enabled = fields.Boolean(required=False)
    
    category = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    supported_validations = fields.List(fields.Nested(SupportedValidationsSchema, required=False), required=False)
    


class Integer(BaseSchema):
    # Content swagger.json

    
    name = fields.Str(required=False)
    
    list_enabled = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    
    category = fields.Str(required=False)
    
    supported_validations = fields.List(fields.Nested(SupportedValidationsSchema, required=False), required=False)
    


class FloatType(BaseSchema):
    # Content swagger.json

    
    name = fields.Str(required=False)
    
    list_enabled = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    
    category = fields.Str(required=False)
    
    supported_validations = fields.List(fields.Nested(SupportedValidationsSchema, required=False), required=False)
    


class BooleanType(BaseSchema):
    # Content swagger.json

    
    name = fields.Str(required=False)
    
    category = fields.Str(required=False)
    
    list_enabled = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    
    supported_validations = fields.List(fields.Nested(SupportedValidationsSchema, required=False), required=False)
    


class Date(BaseSchema):
    # Content swagger.json

    
    name = fields.Str(required=False)
    
    list_enabled = fields.Boolean(required=False)
    
    category = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    supported_validations = fields.List(fields.Nested(SupportedValidationsSchema, required=False), required=False)
    


class Datetime(BaseSchema):
    # Content swagger.json

    
    name = fields.Str(required=False)
    
    category = fields.Str(required=False)
    
    list_enabled = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    
    supported_validations = fields.List(fields.Nested(SupportedValidationsSchema, required=False), required=False)
    


class Json(BaseSchema):
    # Content swagger.json

    
    name = fields.Str(required=False)
    
    list_enabled = fields.Boolean(required=False)
    
    category = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    supported_validations = fields.List(fields.Nested(SupportedValidationsSchema, required=False), required=False)
    


class File(BaseSchema):
    # Content swagger.json

    
    name = fields.Str(required=False)
    
    category = fields.Str(required=False)
    
    list_enabled = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    
    supported_validations = fields.List(fields.Nested(SupportedValidationsSchema, required=False), required=False)
    


class Url(BaseSchema):
    # Content swagger.json

    
    name = fields.Str(required=False)
    
    list_enabled = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    
    supported_validations = fields.List(fields.Nested(SupportedValidationsSchema, required=False), required=False)
    


class Metaobject(BaseSchema):
    # Content swagger.json

    
    name = fields.Str(required=False)
    
    list_enabled = fields.Boolean(required=False)
    
    category = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    supported_validations = fields.List(fields.Nested(SupportedValidationsSchema, required=False), required=False)
    


class Product(BaseSchema):
    # Content swagger.json

    
    name = fields.Str(required=False)
    
    list_enabled = fields.Boolean(required=False)
    
    category = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    supported_validations = fields.List(fields.Nested(SupportedValidationsSchema, required=False), required=False)
    


class CustomObjectEntry(BaseSchema):
    # Content swagger.json

    
    _id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    entries_count = fields.Int(required=False)
    
    fields_count = fields.Int(required=False)
    


class CustomObjectDefinitionsSchema(BaseSchema):
    # Content swagger.json

    
    items = fields.List(fields.Nested(CustomObjectEntry, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class CustomObjectEntryFieldSchema(BaseSchema):
    # Content swagger.json

    
    definition_id = fields.Str(required=False)
    
    value = fields.List(fields.Raw(required=False), required=False)
    


class CustomObjectRequestSchema(BaseSchema):
    # Content swagger.json

    
    status = fields.Str(required=False)
    
    definition_id = fields.Str(required=False)
    
    fields = fields.List(fields.Nested(CustomObjectEntryFieldSchema, required=False), required=False)
    


class CustomObjectBulkSchema(BaseSchema):
    # Content swagger.json

    
    url = fields.Str(required=False)
    
    total_records = fields.Int(required=False)
    


