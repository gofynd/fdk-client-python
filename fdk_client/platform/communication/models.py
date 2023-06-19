"""Communication Platform Model"""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




class StatsImported(BaseSchema):
    pass


class StatsProcessedEmail(BaseSchema):
    pass


class StatsProcessedSms(BaseSchema):
    pass


class StatsProcessed(BaseSchema):
    pass


class Stats(BaseSchema):
    pass


class GetStats(BaseSchema):
    pass


class CampaignReq(BaseSchema):
    pass


class RecipientHeaders(BaseSchema):
    pass


class CampaignEmailTemplate(BaseSchema):
    pass


class CampignEmailProvider(BaseSchema):
    pass


class CampaignEmail(BaseSchema):
    pass


class Campaign(BaseSchema):
    pass


class Campaigns(BaseSchema):
    pass


class BadRequestSchema(BaseSchema):
    pass


class NotFound(BaseSchema):
    pass


class BigqueryHeadersReq(BaseSchema):
    pass


class BigqueryHeadersResHeaders(BaseSchema):
    pass


class BigqueryHeadersRes(BaseSchema):
    pass


class GetNRecordsCsvReq(BaseSchema):
    pass


class GetNRecordsCsvResItems(BaseSchema):
    pass


class GetNRecordsCsvRes(BaseSchema):
    pass


class AudienceReq(BaseSchema):
    pass


class Audience(BaseSchema):
    pass


class Audiences(BaseSchema):
    pass


class EmailProviderAdmin(BaseSchema):
    pass


class EmailProvidersAdmin(BaseSchema):
    pass


class EmailProviderReqFrom(BaseSchema):
    pass


class EmailProviderReq(BaseSchema):
    pass


class EmailProvider(BaseSchema):
    pass


class EmailProviders(BaseSchema):
    pass


class DefaultEmailProviders(BaseSchema):
    pass


class DefaultEmailProvidersObjFrom(BaseSchema):
    pass


class EmailTemplateDeleteSuccessRes(BaseSchema):
    pass


class EmailTemplateDeleteFailureRes(BaseSchema):
    pass


class EmailTemplateKeys(BaseSchema):
    pass


class EmailTemplateHeaders(BaseSchema):
    pass


class EmailTemplateReq(BaseSchema):
    pass


class TemplateAndType(BaseSchema):
    pass


class EmailTemplateRes(BaseSchema):
    pass


class EmailTemplate(BaseSchema):
    pass


class SystemEmailTemplate(BaseSchema):
    pass


class EmailTemplates(BaseSchema):
    pass


class SystemEmailTemplates(BaseSchema):
    pass


class PayloadEmailTemplateStructure(BaseSchema):
    pass


class PayloadEmailProviderStructure(BaseSchema):
    pass


class PayloadEmailStructure(BaseSchema):
    pass


class PayloadSmsTemplateStructure(BaseSchema):
    pass


class PayloadSmsProviderStructure(BaseSchema):
    pass


class PayloadSmsStructure(BaseSchema):
    pass


class PayloadStructure(BaseSchema):
    pass


class MetaStructure(BaseSchema):
    pass


class EngineRequest(BaseSchema):
    pass


class EngineResponse(BaseSchema):
    pass


class EventSubscriptionTemplateSms(BaseSchema):
    pass


class EventSubscriptionTemplateEmail(BaseSchema):
    pass


class EventSubscriptionTemplate(BaseSchema):
    pass


class EventSubscription(BaseSchema):
    pass


class EventSubscriptions(BaseSchema):
    pass


class Job(BaseSchema):
    pass


class Jobs(BaseSchema):
    pass


class JobLog(BaseSchema):
    pass


class JobLogs(BaseSchema):
    pass


class TriggerJobResponse(BaseSchema):
    pass


class TriggerJobRequest(BaseSchema):
    pass


class LogEmail(BaseSchema):
    pass


class LogPushnotification(BaseSchema):
    pass


class LogMeta(BaseSchema):
    pass


class Log(BaseSchema):
    pass


class Logs(BaseSchema):
    pass


class SendOtpSmsCommsTemplate(BaseSchema):
    pass


class SendOtpSmsCommsProvider(BaseSchema):
    pass


class SendOtpEmailCommsTemplate(BaseSchema):
    pass


class SendOtpEmailCommsProvider(BaseSchema):
    pass


class SendOtpCommsReqData(BaseSchema):
    pass


class SendOtpCommsReqSms(BaseSchema):
    pass


class SendOtpCommsReqEmail(BaseSchema):
    pass


class SendOtpCommsResSms(BaseSchema):
    pass


class SendOtpCommsResEmail(BaseSchema):
    pass


class SendOtpCommsReq(BaseSchema):
    pass


class SendOtpCommsRes(BaseSchema):
    pass


class VerifyOtpCommsReq(BaseSchema):
    pass


class VerifyOtpCommsSuccessRes(BaseSchema):
    pass


class VerifyOtpCommsErrorRes(BaseSchema):
    pass


class AppProvider(BaseSchema):
    pass


class AppProviderRes(BaseSchema):
    pass


class AppProviderResVoice(BaseSchema):
    pass


class AppProviderResObj(BaseSchema):
    pass


class GlobalProviders(BaseSchema):
    pass


class GlobalProvidersResObj(BaseSchema):
    pass


class AppProviderAdmin(BaseSchema):
    pass


class AppProviderAdminObj(BaseSchema):
    pass


class UpdateGlobalProviders(BaseSchema):
    pass


class UpdateGlobalProvidersObj(BaseSchema):
    pass


class AppProviderReq(BaseSchema):
    pass


class PushtokenReq(BaseSchema):
    pass


class PushtokenRes(BaseSchema):
    pass


class SmsProviderAdmin(BaseSchema):
    pass


class SmsProvidersAdmin(BaseSchema):
    pass


class SmsProviderReq(BaseSchema):
    pass


class SmsProvider(BaseSchema):
    pass


class SmsProviders(BaseSchema):
    pass


class DefaultSmsProviders(BaseSchema):
    pass


class SmsTemplateDeleteSuccessRes(BaseSchema):
    pass


class SmsTemplateDeleteFailureRes(BaseSchema):
    pass


class SmsTemplateMessage(BaseSchema):
    pass


class SmsTemplateReq(BaseSchema):
    pass


class SmsTemplateRes(BaseSchema):
    pass


class SmsTemplate(BaseSchema):
    pass


class SystemSmsTemplate(BaseSchema):
    pass


class SmsTemplates(BaseSchema):
    pass


class SystemSmsTemplates(BaseSchema):
    pass


class Notification(BaseSchema):
    pass


class SystemNotificationUser(BaseSchema):
    pass


class SystemNotificationSettings(BaseSchema):
    pass


class SystemNotification(BaseSchema):
    pass


class SystemNotificationsPage(BaseSchema):
    pass


class SystemNotifications(BaseSchema):
    pass


class VoiceProviderReq(BaseSchema):
    pass


class VoiceProvider(BaseSchema):
    pass


class VoiceProviders(BaseSchema):
    pass


class VoiceTemplateDeleteSuccessRes(BaseSchema):
    pass


class VoiceTemplateDeleteFailureRes(BaseSchema):
    pass


class VoiceTemplateMessage(BaseSchema):
    pass


class VoiceTemplateReq(BaseSchema):
    pass


class VoiceTemplateRes(BaseSchema):
    pass


class VoiceTemplate(BaseSchema):
    pass


class SystemVoiceTemplate(BaseSchema):
    pass


class VoiceTemplates(BaseSchema):
    pass


class SystemVoiceTemplates(BaseSchema):
    pass


class Page(BaseSchema):
    pass


class GenericSuccess(BaseSchema):
    pass


class InvalidRangeErrorReqPositive(BaseSchema):
    pass


class InvalidInputRequiredByteOrHexError(BaseSchema):
    pass


class NameValidatorError(BaseSchema):
    pass


class NameValidatorErrorMessage(BaseSchema):
    pass


class ApikeyValidatorError(BaseSchema):
    pass


class ApikeyValidatorErrorMessage(BaseSchema):
    pass


class FeedidValidatorError(BaseSchema):
    pass


class FeedidValidatorErrorMessage(BaseSchema):
    pass


class UsernameValidatorError(BaseSchema):
    pass


class UsernameValidatorErrorMessage(BaseSchema):
    pass


class PasswordValidatorError(BaseSchema):
    pass


class PasswordValidatorErrorMessage(BaseSchema):
    pass


class ValidatorErrorBody(BaseSchema):
    pass


class ValidatorErrorMessageProperties(BaseSchema):
    pass


class CastToStringFail(BaseSchema):
    pass


class InvalidID(BaseSchema):
    pass





class StatsImported(BaseSchema):
    # Communication swagger.json

    
    count = fields.Int(required=False)
    


class StatsProcessedEmail(BaseSchema):
    # Communication swagger.json

    
    success = fields.Int(required=False)
    
    failed = fields.Int(required=False)
    
    suppressed = fields.Int(required=False)
    


class StatsProcessedSms(BaseSchema):
    # Communication swagger.json

    
    success = fields.Int(required=False)
    
    failed = fields.Int(required=False)
    
    suppressed = fields.Int(required=False)
    


class StatsProcessed(BaseSchema):
    # Communication swagger.json

    
    email = fields.Nested(StatsProcessedEmail, required=False)
    
    sms = fields.Nested(StatsProcessedSms, required=False)
    


class Stats(BaseSchema):
    # Communication swagger.json

    
    _id = fields.Str(required=False)
    
    imported = fields.Raw(required=False)
    
    processed = fields.Raw(required=False)
    


class GetStats(BaseSchema):
    # Communication swagger.json

    
    items = fields.List(fields.Nested(Stats, required=False), required=False)
    


class CampaignReq(BaseSchema):
    # Communication swagger.json

    
    description = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    headers = fields.List(fields.Str(required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    file_url = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    records_count = fields.Int(required=False)
    
    application = fields.Str(required=False)
    


class RecipientHeaders(BaseSchema):
    # Communication swagger.json

    
    email = fields.Str(required=False)
    


class CampaignEmailTemplate(BaseSchema):
    # Communication swagger.json

    
    key = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class CampignEmailProvider(BaseSchema):
    # Communication swagger.json

    
    _id = fields.Str(required=False)
    
    from_name = fields.Str(required=False)
    
    from_email = fields.Str(required=False)
    


class CampaignEmail(BaseSchema):
    # Communication swagger.json

    
    template = fields.Nested(CampaignEmailTemplate, required=False)
    
    provider = fields.Nested(CampignEmailProvider, required=False)
    


class Campaign(BaseSchema):
    # Communication swagger.json

    
    recipient_headers = fields.Nested(RecipientHeaders, required=False)
    
    email = fields.Nested(CampaignEmail, required=False)
    
    description = fields.Str(required=False)
    
    tags = fields.List(fields.Raw(required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    _id = fields.Str(required=False)
    
    datasource = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    application = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    


class Campaigns(BaseSchema):
    # Communication swagger.json

    
    items = fields.List(fields.Nested(Campaign, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class BadRequestSchema(BaseSchema):
    # Communication swagger.json

    
    status = fields.Str(required=False)
    
    message = fields.Str(required=False)
    


class NotFound(BaseSchema):
    # Communication swagger.json

    
    message = fields.Str(required=False)
    


class BigqueryHeadersReq(BaseSchema):
    # Communication swagger.json

    
    query = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class BigqueryHeadersResHeaders(BaseSchema):
    # Communication swagger.json

    
    name = fields.Str(required=False)
    
    type = fields.Str(required=False)
    


class BigqueryHeadersRes(BaseSchema):
    # Communication swagger.json

    
    headers = fields.List(fields.Nested(BigqueryHeadersResHeaders, required=False), required=False)
    


class GetNRecordsCsvReq(BaseSchema):
    # Communication swagger.json

    
    url = fields.Str(required=False)
    
    header = fields.Boolean(required=False)
    
    count = fields.Int(required=False)
    


class GetNRecordsCsvResItems(BaseSchema):
    # Communication swagger.json

    
    phone_number = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    firstname = fields.Str(required=False)
    
    lastname = fields.Str(required=False)
    
    orderid = fields.Str(required=False)
    


class GetNRecordsCsvRes(BaseSchema):
    # Communication swagger.json

    
    items = fields.List(fields.Nested(GetNRecordsCsvResItems, required=False), required=False)
    


class AudienceReq(BaseSchema):
    # Communication swagger.json

    
    description = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    headers = fields.List(fields.Str(required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    file_url = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    records_count = fields.Int(required=False)
    
    application = fields.Str(required=False)
    


class Audience(BaseSchema):
    # Communication swagger.json

    
    description = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    headers = fields.List(fields.Str(required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    _id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    file_url = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    records_count = fields.Int(required=False)
    
    application = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    


class Audiences(BaseSchema):
    # Communication swagger.json

    
    items = fields.List(fields.Nested(Audience, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class EmailProviderAdmin(BaseSchema):
    # Communication swagger.json

    
    type = fields.Str(required=False)
    
    provider = fields.Str(required=False)
    
    from_address = fields.List(fields.Nested(EmailProviderReqFrom, required=False), required=False)
    
    _id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    api_key = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    


class EmailProvidersAdmin(BaseSchema):
    # Communication swagger.json

    
    items = fields.List(fields.Nested(EmailProvider, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class EmailProviderReqFrom(BaseSchema):
    # Communication swagger.json

    
    name = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    is_default = fields.Boolean(required=False)
    


class EmailProviderReq(BaseSchema):
    # Communication swagger.json

    
    name = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    api_key = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    provider = fields.Str(required=False)
    
    from_address = fields.List(fields.Nested(EmailProviderReqFrom, required=False), required=False)
    


class EmailProvider(BaseSchema):
    # Communication swagger.json

    
    type = fields.Str(required=False)
    
    provider = fields.Str(required=False)
    
    from_address = fields.List(fields.Nested(EmailProviderReqFrom, required=False), required=False)
    
    _id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    api_key = fields.Str(required=False)
    
    application = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    


class EmailProviders(BaseSchema):
    # Communication swagger.json

    
    items = fields.List(fields.Nested(EmailProvider, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class DefaultEmailProviders(BaseSchema):
    # Communication swagger.json

    
    _id = fields.Str(required=False)
    
    from_address = fields.List(fields.Nested(DefaultEmailProvidersObjFrom, required=False), required=False)
    
    name = fields.Str(required=False)
    
    is_default = fields.Boolean(required=False)
    


class DefaultEmailProvidersObjFrom(BaseSchema):
    # Communication swagger.json

    
    name = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    is_default = fields.Boolean(required=False)
    


class EmailTemplateDeleteSuccessRes(BaseSchema):
    # Communication swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class EmailTemplateDeleteFailureRes(BaseSchema):
    # Communication swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class EmailTemplateKeys(BaseSchema):
    # Communication swagger.json

    
    to = fields.Str(required=False)
    
    cc = fields.Str(required=False)
    
    bcc = fields.Str(required=False)
    


class EmailTemplateHeaders(BaseSchema):
    # Communication swagger.json

    
    key = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class EmailTemplateReq(BaseSchema):
    # Communication swagger.json

    
    name = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    keys = fields.Nested(EmailTemplateKeys, required=False)
    
    static_to = fields.List(fields.Str(required=False), required=False)
    
    static_cc = fields.List(fields.Str(required=False), required=False)
    
    static_bcc = fields.List(fields.Str(required=False), required=False)
    
    reply_to = fields.Str(required=False)
    
    headers = fields.List(fields.Nested(EmailTemplateHeaders, required=False), required=False)
    
    subject = fields.Nested(TemplateAndType, required=False)
    
    html = fields.Nested(TemplateAndType, required=False)
    
    text = fields.Nested(TemplateAndType, required=False)
    
    attachments = fields.List(fields.Raw(required=False), required=False)
    
    priority = fields.Str(required=False)
    


class TemplateAndType(BaseSchema):
    # Communication swagger.json

    
    template_type = fields.Str(required=False)
    
    template = fields.Str(required=False)
    


class EmailTemplateRes(BaseSchema):
    # Communication swagger.json

    
    is_system = fields.Boolean(required=False)
    
    is_internal = fields.Boolean(required=False)
    
    description = fields.Str(required=False)
    
    static_to = fields.List(fields.Str(required=False), required=False)
    
    static_cc = fields.List(fields.Str(required=False), required=False)
    
    static_bcc = fields.List(fields.Str(required=False), required=False)
    
    tags = fields.List(fields.Raw(required=False), required=False)
    
    priority = fields.Str(required=False)
    
    published = fields.Boolean(required=False)
    
    _id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    keys = fields.Nested(EmailTemplateKeys, required=False)
    
    reply_to = fields.Str(required=False)
    
    headers = fields.List(fields.Nested(EmailTemplateHeaders, required=False), required=False)
    
    subject = fields.Nested(TemplateAndType, required=False)
    
    html = fields.Nested(TemplateAndType, required=False)
    
    text = fields.Nested(TemplateAndType, required=False)
    
    attachments = fields.List(fields.Raw(required=False), required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    


class EmailTemplate(BaseSchema):
    # Communication swagger.json

    
    is_system = fields.Boolean(required=False)
    
    is_internal = fields.Boolean(required=False)
    
    description = fields.Str(required=False)
    
    static_to = fields.List(fields.Raw(required=False), required=False)
    
    static_cc = fields.List(fields.Raw(required=False), required=False)
    
    static_bcc = fields.List(fields.Raw(required=False), required=False)
    
    tags = fields.List(fields.Raw(required=False), required=False)
    
    priority = fields.Str(required=False)
    
    published = fields.Boolean(required=False)
    
    _id = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    from_name = fields.Str(required=False)
    
    subject = fields.Nested(TemplateAndType, required=False)
    
    html = fields.Nested(TemplateAndType, required=False)
    
    text = fields.Nested(TemplateAndType, required=False)
    
    headers = fields.List(fields.Raw(required=False), required=False)
    
    attachments = fields.List(fields.Raw(required=False), required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    


class SystemEmailTemplate(BaseSchema):
    # Communication swagger.json

    
    is_system = fields.Boolean(required=False)
    
    is_internal = fields.Boolean(required=False)
    
    description = fields.Str(required=False)
    
    static_to = fields.List(fields.Raw(required=False), required=False)
    
    static_cc = fields.List(fields.Raw(required=False), required=False)
    
    static_bcc = fields.List(fields.Raw(required=False), required=False)
    
    tags = fields.List(fields.Raw(required=False), required=False)
    
    priority = fields.Str(required=False)
    
    published = fields.Boolean(required=False)
    
    _id = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    from_name = fields.Str(required=False)
    
    subject = fields.Nested(TemplateAndType, required=False)
    
    html = fields.Nested(TemplateAndType, required=False)
    
    text = fields.Nested(TemplateAndType, required=False)
    
    headers = fields.List(fields.Raw(required=False), required=False)
    
    attachments = fields.List(fields.Raw(required=False), required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    


class EmailTemplates(BaseSchema):
    # Communication swagger.json

    
    items = fields.List(fields.Nested(EmailTemplate, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class SystemEmailTemplates(BaseSchema):
    # Communication swagger.json

    
    items = fields.List(fields.Nested(SystemEmailTemplate, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class PayloadEmailTemplateStructure(BaseSchema):
    # Communication swagger.json

    
    key = fields.Str(required=False)
    
    value = fields.Raw(required=False)
    


class PayloadEmailProviderStructure(BaseSchema):
    # Communication swagger.json

    
    _id = fields.Str(required=False)
    


class PayloadEmailStructure(BaseSchema):
    # Communication swagger.json

    
    template = fields.Nested(PayloadEmailTemplateStructure, required=False)
    
    provider = fields.Nested(PayloadEmailProviderStructure, required=False)
    


class PayloadSmsTemplateStructure(BaseSchema):
    # Communication swagger.json

    
    key = fields.Str(required=False)
    
    value = fields.Raw(required=False)
    


class PayloadSmsProviderStructure(BaseSchema):
    # Communication swagger.json

    
    _id = fields.Str(required=False)
    


class PayloadSmsStructure(BaseSchema):
    # Communication swagger.json

    
    template = fields.Nested(PayloadSmsTemplateStructure, required=False)
    
    provider = fields.Nested(PayloadSmsProviderStructure, required=False)
    


class PayloadStructure(BaseSchema):
    # Communication swagger.json

    
    data = fields.List(fields.Dict(required=False), required=False)
    
    email = fields.Nested(PayloadEmailStructure, required=False)
    
    sms = fields.Nested(PayloadSmsStructure, required=False)
    
    application = fields.Str(required=False)
    


class MetaStructure(BaseSchema):
    # Communication swagger.json

    
    job_type = fields.Str(required=False)
    
    action = fields.Str(required=False)
    
    trace = fields.Str(required=False)
    
    timestamp = fields.Str(required=False)
    


class EngineRequest(BaseSchema):
    # Communication swagger.json

    
    payload = fields.Nested(PayloadStructure, required=False)
    
    meta = fields.Nested(MetaStructure, required=False)
    


class EngineResponse(BaseSchema):
    # Communication swagger.json

    
    success = fields.Boolean(required=False)
    


class EventSubscriptionTemplateSms(BaseSchema):
    # Communication swagger.json

    
    subscribed = fields.Boolean(required=False)
    
    template = fields.Str(required=False)
    


class EventSubscriptionTemplateEmail(BaseSchema):
    # Communication swagger.json

    
    subscribed = fields.Boolean(required=False)
    
    template = fields.Str(required=False)
    


class EventSubscriptionTemplate(BaseSchema):
    # Communication swagger.json

    
    sms = fields.Nested(EventSubscriptionTemplateSms, required=False)
    
    email = fields.Nested(EventSubscriptionTemplateEmail, required=False)
    


class EventSubscription(BaseSchema):
    # Communication swagger.json

    
    template = fields.Nested(EventSubscriptionTemplate, required=False)
    
    is_default = fields.Boolean(required=False)
    
    _id = fields.Str(required=False)
    
    application = fields.Str(required=False)
    
    event = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    


class EventSubscriptions(BaseSchema):
    # Communication swagger.json

    
    items = fields.List(fields.Nested(EventSubscription, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class Job(BaseSchema):
    # Communication swagger.json

    
    completed = fields.Boolean(required=False)
    
    is_active = fields.Boolean(required=False)
    
    _id = fields.Str(required=False)
    
    campaign = fields.Str(required=False)
    
    application = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    


class Jobs(BaseSchema):
    # Communication swagger.json

    
    items = fields.List(fields.Nested(Job, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class JobLog(BaseSchema):
    # Communication swagger.json

    
    imported = fields.Raw(required=False)
    
    processed = fields.Raw(required=False)
    
    _id = fields.Str(required=False)
    
    job = fields.Str(required=False)
    
    campaign = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    


class JobLogs(BaseSchema):
    # Communication swagger.json

    
    items = fields.List(fields.Nested(JobLog, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class TriggerJobResponse(BaseSchema):
    # Communication swagger.json

    
    status = fields.Int(required=False)
    


class TriggerJobRequest(BaseSchema):
    # Communication swagger.json

    
    job_id = fields.Str(required=False)
    


class LogEmail(BaseSchema):
    # Communication swagger.json

    
    template = fields.Str(required=False)
    


class LogPushnotification(BaseSchema):
    # Communication swagger.json

    
    pushtokens = fields.List(fields.Str(required=False), required=False)
    


class LogMeta(BaseSchema):
    # Communication swagger.json

    
    type = fields.Str(required=False)
    
    identifier = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
    offset = fields.Str(required=False)
    
    partition = fields.Str(required=False)
    
    topic = fields.Str(required=False)
    


class Log(BaseSchema):
    # Communication swagger.json

    
    email = fields.Nested(LogEmail, required=False)
    
    pushnotification = fields.Nested(LogPushnotification, required=False)
    
    meta = fields.Nested(LogMeta, required=False)
    
    _id = fields.Str(required=False)
    
    application = fields.Str(required=False)
    
    service = fields.Str(required=False)
    
    step = fields.Str(required=False)
    
    source = fields.Str(required=False)
    
    channel_type = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    data = fields.Raw(required=False)
    
    expire_at = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    


class Logs(BaseSchema):
    # Communication swagger.json

    
    items = fields.List(fields.Nested(Log, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class SendOtpSmsCommsTemplate(BaseSchema):
    # Communication swagger.json

    
    key = fields.Str(required=False)
    
    value = fields.Raw(required=False)
    


class SendOtpSmsCommsProvider(BaseSchema):
    # Communication swagger.json

    
    slug = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    


class SendOtpEmailCommsTemplate(BaseSchema):
    # Communication swagger.json

    
    key = fields.Str(required=False)
    
    value = fields.Raw(required=False)
    


class SendOtpEmailCommsProvider(BaseSchema):
    # Communication swagger.json

    
    slug = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    


class SendOtpCommsReqData(BaseSchema):
    # Communication swagger.json

    
    send_same_otp_to_channel = fields.Boolean(required=False)
    
    mobile = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    to = fields.Str(required=False)
    


class SendOtpCommsReqSms(BaseSchema):
    # Communication swagger.json

    
    otp_length = fields.Int(required=False)
    
    expiry = fields.Int(required=False)
    
    template = fields.Nested(SendOtpSmsCommsTemplate, required=False)
    
    provider = fields.Nested(SendOtpSmsCommsProvider, required=False)
    


class SendOtpCommsReqEmail(BaseSchema):
    # Communication swagger.json

    
    otp_length = fields.Int(required=False)
    
    expiry = fields.Int(required=False)
    
    template = fields.Nested(SendOtpEmailCommsTemplate, required=False)
    
    provider = fields.Nested(SendOtpEmailCommsProvider, required=False)
    


class SendOtpCommsResSms(BaseSchema):
    # Communication swagger.json

    
    success = fields.Boolean(required=False)
    
    request_id = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    resend_timer = fields.Int(required=False)
    


class SendOtpCommsResEmail(BaseSchema):
    # Communication swagger.json

    
    success = fields.Boolean(required=False)
    
    request_id = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    to = fields.Str(required=False)
    
    resend_timer = fields.Int(required=False)
    


class SendOtpCommsReq(BaseSchema):
    # Communication swagger.json

    
    data = fields.Nested(SendOtpCommsReqData, required=False)
    
    sms = fields.Nested(SendOtpCommsReqSms, required=False)
    
    email = fields.Nested(SendOtpCommsReqEmail, required=False)
    


class SendOtpCommsRes(BaseSchema):
    # Communication swagger.json

    
    sms = fields.Nested(SendOtpCommsResSms, required=False)
    
    email = fields.Nested(SendOtpCommsResEmail, required=False)
    


class VerifyOtpCommsReq(BaseSchema):
    # Communication swagger.json

    
    request_id = fields.Str(required=False)
    
    otp = fields.Str(required=False)
    


class VerifyOtpCommsSuccessRes(BaseSchema):
    # Communication swagger.json

    
    success = fields.Boolean(required=False)
    
    mobile = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    message = fields.Str(required=False)
    


class VerifyOtpCommsErrorRes(BaseSchema):
    # Communication swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class AppProvider(BaseSchema):
    # Communication swagger.json

    
    email = fields.Nested(AppProviderRes, required=False)
    
    sms = fields.Nested(AppProviderRes, required=False)
    
    voice = fields.Nested(AppProviderResVoice, required=False)
    
    _id = fields.Str(required=False)
    
    application = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    


class AppProviderRes(BaseSchema):
    # Communication swagger.json

    
    transaction = fields.Nested(AppProviderResObj, required=False)
    
    promotional = fields.Nested(AppProviderResObj, required=False)
    
    otp = fields.Nested(AppProviderResObj, required=False)
    


class AppProviderResVoice(BaseSchema):
    # Communication swagger.json

    
    transaction = fields.Nested(AppProviderResObj, required=False)
    
    otp = fields.Nested(AppProviderResObj, required=False)
    


class AppProviderResObj(BaseSchema):
    # Communication swagger.json

    
    provider = fields.Str(required=False)
    


class GlobalProviders(BaseSchema):
    # Communication swagger.json

    
    email = fields.List(fields.Nested(GlobalProvidersResObj, required=False), required=False)
    
    sms = fields.List(fields.Nested(GlobalProvidersResObj, required=False), required=False)
    
    voice = fields.List(fields.Nested(GlobalProvidersResObj, required=False), required=False)
    


class GlobalProvidersResObj(BaseSchema):
    # Communication swagger.json

    
    _id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    


class AppProviderAdmin(BaseSchema):
    # Communication swagger.json

    
    email = fields.Nested(AppProviderAdminObj, required=False)
    
    sms = fields.Nested(AppProviderAdminObj, required=False)
    
    voice = fields.Nested(AppProviderAdminObj, required=False)
    


class AppProviderAdminObj(BaseSchema):
    # Communication swagger.json

    
    transaction = fields.Nested(AppProviderResObj, required=False)
    
    otp = fields.Nested(AppProviderResObj, required=False)
    


class UpdateGlobalProviders(BaseSchema):
    # Communication swagger.json

    
    email = fields.Nested(UpdateGlobalProvidersObj, required=False)
    
    sms = fields.Nested(UpdateGlobalProvidersObj, required=False)
    
    voice = fields.Nested(UpdateGlobalProvidersObj, required=False)
    
    _id = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    


class UpdateGlobalProvidersObj(BaseSchema):
    # Communication swagger.json

    
    default_provider = fields.Str(required=False)
    
    otp_provider = fields.Str(required=False)
    


class AppProviderReq(BaseSchema):
    # Communication swagger.json

    
    email = fields.Nested(AppProviderRes, required=False)
    
    sms = fields.Nested(AppProviderRes, required=False)
    
    voice = fields.Nested(AppProviderResVoice, required=False)
    


class PushtokenReq(BaseSchema):
    # Communication swagger.json

    
    action = fields.Str(required=False)
    
    bundle_identifier = fields.Str(required=False)
    
    push_token = fields.Str(required=False)
    
    unique_device_id = fields.Str(required=False)
    


class PushtokenRes(BaseSchema):
    # Communication swagger.json

    
    _id = fields.Str(required=False)
    
    bundle_identifier = fields.Str(required=False)
    
    push_token = fields.Str(required=False)
    
    unique_device_id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    platform = fields.Str(required=False)
    
    application_id = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    expired_at = fields.Str(required=False)
    


class SmsProviderAdmin(BaseSchema):
    # Communication swagger.json

    
    rpt = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    provider = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    entity_id = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    sender = fields.Str(required=False)
    
    username = fields.Str(required=False)
    
    authkey = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    


class SmsProvidersAdmin(BaseSchema):
    # Communication swagger.json

    
    items = fields.List(fields.Nested(SmsProviderAdmin, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class SmsProviderReq(BaseSchema):
    # Communication swagger.json

    
    name = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    sender = fields.Str(required=False)
    
    username = fields.Str(required=False)
    
    authkey = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    provider = fields.Str(required=False)
    


class SmsProvider(BaseSchema):
    # Communication swagger.json

    
    rpt = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    provider = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    entity_id = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    sender = fields.Str(required=False)
    
    username = fields.Str(required=False)
    
    authkey = fields.Str(required=False)
    
    application = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    


class SmsProviders(BaseSchema):
    # Communication swagger.json

    
    items = fields.List(fields.Nested(SmsProvider, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class DefaultSmsProviders(BaseSchema):
    # Communication swagger.json

    
    _id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    is_default = fields.Boolean(required=False)
    


class SmsTemplateDeleteSuccessRes(BaseSchema):
    # Communication swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class SmsTemplateDeleteFailureRes(BaseSchema):
    # Communication swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class SmsTemplateMessage(BaseSchema):
    # Communication swagger.json

    
    template_type = fields.Str(required=False)
    
    template = fields.Str(required=False)
    


class SmsTemplateReq(BaseSchema):
    # Communication swagger.json

    
    name = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    message = fields.Nested(SmsTemplateMessage, required=False)
    
    template_variables = fields.Raw(required=False)
    
    attachments = fields.List(fields.Raw(required=False), required=False)
    
    priority = fields.Str(required=False)
    


class SmsTemplateRes(BaseSchema):
    # Communication swagger.json

    
    is_system = fields.Boolean(required=False)
    
    is_internal = fields.Boolean(required=False)
    
    description = fields.Str(required=False)
    
    tags = fields.List(fields.Raw(required=False), required=False)
    
    priority = fields.Str(required=False)
    
    published = fields.Boolean(required=False)
    
    _id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    message = fields.Nested(SmsTemplateMessage, required=False)
    
    template_variables = fields.Raw(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    


class SmsTemplate(BaseSchema):
    # Communication swagger.json

    
    is_system = fields.Boolean(required=False)
    
    is_internal = fields.Boolean(required=False)
    
    description = fields.Str(required=False)
    
    priority = fields.Str(required=False)
    
    tags = fields.List(fields.Raw(required=False), required=False)
    
    published = fields.Boolean(required=False)
    
    _id = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    message = fields.Nested(SmsTemplateMessage, required=False)
    
    template_variables = fields.Raw(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    


class SystemSmsTemplate(BaseSchema):
    # Communication swagger.json

    
    is_system = fields.Boolean(required=False)
    
    is_internal = fields.Boolean(required=False)
    
    description = fields.Str(required=False)
    
    tags = fields.List(fields.Raw(required=False), required=False)
    
    priority = fields.Str(required=False)
    
    published = fields.Boolean(required=False)
    
    _id = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    message = fields.Nested(SmsTemplateMessage, required=False)
    
    template_variables = fields.Raw(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    


class SmsTemplates(BaseSchema):
    # Communication swagger.json

    
    items = fields.List(fields.Nested(SmsTemplate, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class SystemSmsTemplates(BaseSchema):
    # Communication swagger.json

    
    items = fields.List(fields.Nested(SystemSmsTemplate, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class Notification(BaseSchema):
    # Communication swagger.json

    
    title = fields.Str(required=False)
    
    body = fields.Str(required=False)
    
    subtitle = fields.Str(required=False)
    
    icon = fields.Str(required=False)
    
    deeplink = fields.Str(required=False)
    
    click_action = fields.Str(required=False)
    


class SystemNotificationUser(BaseSchema):
    # Communication swagger.json

    
    type = fields.Str(required=False)
    
    value = fields.Str(required=False)
    


class SystemNotificationSettings(BaseSchema):
    # Communication swagger.json

    
    sound = fields.Boolean(required=False)
    
    priority = fields.Str(required=False)
    
    time_to_live = fields.Str(required=False)
    


class SystemNotification(BaseSchema):
    # Communication swagger.json

    
    notification = fields.Nested(Notification, required=False)
    
    user = fields.Nested(SystemNotificationUser, required=False)
    
    settings = fields.Nested(SystemNotificationUser, required=False)
    
    _id = fields.Str(required=False)
    
    group = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    


class SystemNotificationsPage(BaseSchema):
    # Communication swagger.json

    
    type = fields.Str(required=False)
    
    current = fields.Int(required=False)
    
    size = fields.Int(required=False)
    
    item_total = fields.Int(required=False)
    
    has_next = fields.Boolean(required=False)
    


class SystemNotifications(BaseSchema):
    # Communication swagger.json

    
    items = fields.List(fields.Nested(SystemNotification, required=False), required=False)
    
    last_read_anchor = fields.Int(required=False)
    
    page = fields.Nested(Page, required=False)
    


class VoiceProviderReq(BaseSchema):
    # Communication swagger.json

    
    name = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    sender = fields.Str(required=False)
    
    username = fields.Str(required=False)
    
    authkey = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    provider = fields.Str(required=False)
    


class VoiceProvider(BaseSchema):
    # Communication swagger.json

    
    _id = fields.Str(required=False)
    
    application = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    provider = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    __v = fields.Float(required=False)
    
    discriminator = fields.Str(required=False)
    
    username = fields.Str(required=False)
    
    password = fields.Str(required=False)
    
    caller_id = fields.Str(required=False)
    
    applet_url = fields.Str(required=False)
    
    whitelisted_ip = fields.List(fields.Str(required=False), required=False)
    


class VoiceProviders(BaseSchema):
    # Communication swagger.json

    
    items = fields.List(fields.Nested(VoiceProvider, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class VoiceTemplateDeleteSuccessRes(BaseSchema):
    # Communication swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class VoiceTemplateDeleteFailureRes(BaseSchema):
    # Communication swagger.json

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    


class VoiceTemplateMessage(BaseSchema):
    # Communication swagger.json

    
    template_type = fields.Str(required=False)
    
    template = fields.Str(required=False)
    


class VoiceTemplateReq(BaseSchema):
    # Communication swagger.json

    
    name = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    message = fields.Nested(VoiceTemplateMessage, required=False)
    
    template_variables = fields.Raw(required=False)
    
    attachments = fields.List(fields.Raw(required=False), required=False)
    
    priority = fields.Str(required=False)
    


class VoiceTemplateRes(BaseSchema):
    # Communication swagger.json

    
    is_system = fields.Boolean(required=False)
    
    is_internal = fields.Boolean(required=False)
    
    description = fields.Str(required=False)
    
    tags = fields.List(fields.Raw(required=False), required=False)
    
    priority = fields.Str(required=False)
    
    published = fields.Boolean(required=False)
    
    _id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    message = fields.Nested(VoiceTemplateMessage, required=False)
    
    template_variables = fields.Raw(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    


class VoiceTemplate(BaseSchema):
    # Communication swagger.json

    
    is_system = fields.Boolean(required=False)
    
    is_internal = fields.Boolean(required=False)
    
    description = fields.Str(required=False)
    
    priority = fields.Str(required=False)
    
    tags = fields.List(fields.Raw(required=False), required=False)
    
    published = fields.Boolean(required=False)
    
    _id = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    message = fields.Nested(VoiceTemplateMessage, required=False)
    
    template_variables = fields.Raw(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    


class SystemVoiceTemplate(BaseSchema):
    # Communication swagger.json

    
    is_system = fields.Boolean(required=False)
    
    is_internal = fields.Boolean(required=False)
    
    description = fields.Str(required=False)
    
    tags = fields.List(fields.Raw(required=False), required=False)
    
    priority = fields.Str(required=False)
    
    published = fields.Boolean(required=False)
    
    _id = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    message = fields.Nested(VoiceTemplateMessage, required=False)
    
    template_variables = fields.Raw(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    


class VoiceTemplates(BaseSchema):
    # Communication swagger.json

    
    items = fields.List(fields.Nested(VoiceTemplate, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class SystemVoiceTemplates(BaseSchema):
    # Communication swagger.json

    
    items = fields.List(fields.Nested(SystemVoiceTemplate, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    


class Page(BaseSchema):
    # Communication swagger.json

    
    item_total = fields.Int(required=False)
    
    next_id = fields.Str(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    has_next = fields.Boolean(required=False)
    
    current = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    size = fields.Int(required=False)
    


class GenericSuccess(BaseSchema):
    # Communication swagger.json

    
    success = fields.Boolean(required=False)
    


class InvalidRangeErrorReqPositive(BaseSchema):
    # Communication swagger.json

    
    message = fields.Str(required=False)
    
    code = fields.Int(required=False)
    
    sentry = fields.Str(required=False)
    


class InvalidInputRequiredByteOrHexError(BaseSchema):
    # Communication swagger.json

    
    message = fields.Str(required=False)
    
    sentry = fields.Str(required=False)
    


class NameValidatorError(BaseSchema):
    # Communication swagger.json

    
    message = fields.Nested(NameValidatorErrorMessage, required=False)
    
    sentry = fields.Str(required=False)
    


class NameValidatorErrorMessage(BaseSchema):
    # Communication swagger.json

    
    name = fields.Nested(ValidatorErrorBody, required=False)
    


class ApikeyValidatorError(BaseSchema):
    # Communication swagger.json

    
    message = fields.Nested(ApikeyValidatorErrorMessage, required=False)
    
    sentry = fields.Str(required=False)
    


class ApikeyValidatorErrorMessage(BaseSchema):
    # Communication swagger.json

    
    api_key = fields.Nested(ValidatorErrorBody, required=False)
    


class FeedidValidatorError(BaseSchema):
    # Communication swagger.json

    
    message = fields.Nested(FeedidValidatorErrorMessage, required=False)
    
    sentry = fields.Str(required=False)
    


class FeedidValidatorErrorMessage(BaseSchema):
    # Communication swagger.json

    
    feedid = fields.Nested(ValidatorErrorBody, required=False)
    


class UsernameValidatorError(BaseSchema):
    # Communication swagger.json

    
    message = fields.Nested(UsernameValidatorErrorMessage, required=False)
    
    sentry = fields.Str(required=False)
    


class UsernameValidatorErrorMessage(BaseSchema):
    # Communication swagger.json

    
    username = fields.Nested(ValidatorErrorBody, required=False)
    


class PasswordValidatorError(BaseSchema):
    # Communication swagger.json

    
    message = fields.Nested(PasswordValidatorErrorMessage, required=False)
    
    sentry = fields.Str(required=False)
    


class PasswordValidatorErrorMessage(BaseSchema):
    # Communication swagger.json

    
    password = fields.Nested(ValidatorErrorBody, required=False)
    


class ValidatorErrorBody(BaseSchema):
    # Communication swagger.json

    
    name = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    properties = fields.Nested(ValidatorErrorMessageProperties, required=False)
    
    kind = fields.Str(required=False)
    
    path = fields.Str(required=False)
    


class ValidatorErrorMessageProperties(BaseSchema):
    # Communication swagger.json

    
    message = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    path = fields.Str(required=False)
    


class CastToStringFail(BaseSchema):
    # Communication swagger.json

    
    message = fields.Str(required=False)
    
    sentry = fields.Str(required=False)
    


class InvalidID(BaseSchema):
    # Communication swagger.json

    
    message = fields.Str(required=False)
    
    sentry = fields.Str(required=False)
    


