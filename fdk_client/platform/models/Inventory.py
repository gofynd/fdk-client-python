"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



class DataTresholdDTO(BaseSchema):
    pass


class GenericDTO(BaseSchema):
    pass


class JobConfigDTO(BaseSchema):
    pass


class TaskDTO(BaseSchema):
    pass


class Page(BaseSchema):
    pass


class ResponseEnvelopeString(BaseSchema):
    pass


class AWSS3config(BaseSchema):
    pass


class ArchiveConfig(BaseSchema):
    pass


class Audit(BaseSchema):
    pass


class CatalogMasterConfig(BaseSchema):
    pass


class CompanyConfig(BaseSchema):
    pass


class DBConfig(BaseSchema):
    pass


class DBConnectionProfile(BaseSchema):
    pass


class DBParamConfig(BaseSchema):
    pass


class DefaultHeadersDTO(BaseSchema):
    pass


class DocMappingConfig(BaseSchema):
    pass


class EmailConfig(BaseSchema):
    pass


class FTPConfig(BaseSchema):
    pass


class FileConfig(BaseSchema):
    pass


class GoogleSpreadSheetConfig(BaseSchema):
    pass


class HttpConfig(BaseSchema):
    pass


class JobConfig(BaseSchema):
    pass


class JobConfigRawDTO(BaseSchema):
    pass


class JsonDocConfig(BaseSchema):
    pass


class LocalFileConfig(BaseSchema):
    pass


class MongoDocConfig(BaseSchema):
    pass


class OAuthConfig(BaseSchema):
    pass


class ProcessConfig(BaseSchema):
    pass


class PropBeanConfig(BaseSchema):
    pass


class PropBeanDTO(BaseSchema):
    pass


class ResponseEnvelopeListJobConfigRawDTO(BaseSchema):
    pass


class SFTPConfig(BaseSchema):
    pass


class Send(BaseSchema):
    pass


class StoreConfig(BaseSchema):
    pass


class StoreFilter(BaseSchema):
    pass


class TaskConfig(BaseSchema):
    pass


class TaskParam(BaseSchema):
    pass


class TaskStepConfig(BaseSchema):
    pass


class JobStepsDTO(BaseSchema):
    pass


class ResponseEnvelopeListJobStepsDTO(BaseSchema):
    pass


class ResponseEnvelopeListJobConfigDTO(BaseSchema):
    pass


class ResponseEnvelopeJobConfigDTO(BaseSchema):
    pass


class JobHistoryDto(BaseSchema):
    pass


class JobMetricsDto(BaseSchema):
    pass


class ResponseEnvelopeJobMetricsDto(BaseSchema):
    pass


class JobConfigListDTO(BaseSchema):
    pass


class ResponseEnvelopeListJobConfigListDTO(BaseSchema):
    pass



class DataTresholdDTO(BaseSchema):
    # Inventory swagger.json

    
    min_price = fields.Float(required=False)
    
    safe_stock = fields.Int(required=False)
    
    period_threshold = fields.Int(required=False)
    
    period_threshold_type = fields.Str(required=False)
    
    period_type_list = fields.List(fields.Nested(GenericDTO, required=False), required=False)
    


class GenericDTO(BaseSchema):
    # Inventory swagger.json

    
    text = fields.Str(required=False)
    
    value = fields.Dict(required=False)
    


class JobConfigDTO(BaseSchema):
    # Inventory swagger.json

    
    integration = fields.Str(required=False)
    
    integration_data = fields.Dict(required=False)
    
    company_name = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    task_details = fields.Nested(TaskDTO, required=False)
    
    threshold_details = fields.Nested(DataTresholdDTO, required=False)
    
    job_code = fields.Str(required=False)
    
    alias = fields.Str(required=False)
    


class TaskDTO(BaseSchema):
    # Inventory swagger.json

    
    type = fields.Int(required=False)
    
    group_list = fields.List(fields.Nested(GenericDTO, required=False), required=False)
    


class Page(BaseSchema):
    # Inventory swagger.json

    
    type = fields.Str(required=False)
    
    size = fields.Int(required=False)
    
    current = fields.Int(required=False)
    
    has_next = fields.Boolean(required=False)
    
    item_total = fields.Int(required=False)
    
    next_id = fields.Str(required=False)
    
    has_previous = fields.Boolean(required=False)
    


class ResponseEnvelopeString(BaseSchema):
    # Inventory swagger.json

    
    timestamp = fields.Str(required=False)
    
    status = fields.Int(required=False)
    
    error = fields.Str(required=False)
    
    exception = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    total_time_taken_in_millis = fields.Int(required=False)
    
    http_status = fields.Str(required=False)
    
    items = fields.Str(required=False)
    
    payload = fields.Str(required=False)
    
    trace_id = fields.Str(required=False)
    
    page = fields.Nested(Page, required=False)
    


class AWSS3config(BaseSchema):
    # Inventory swagger.json

    
    bucket = fields.Str(required=False)
    
    region = fields.Str(required=False)
    
    dir = fields.Str(required=False)
    
    access_key = fields.Str(required=False)
    
    secret_key = fields.Str(required=False)
    
    local_file_path = fields.Str(required=False)
    
    archive_path = fields.Str(required=False)
    
    archive = fields.Boolean(required=False)
    
    delete = fields.Boolean(required=False)
    
    unzip = fields.Boolean(required=False)
    
    zip_format = fields.Str(required=False)
    
    file_regex = fields.Str(required=False)
    
    archive_config = fields.Nested(ArchiveConfig, required=False)
    


class ArchiveConfig(BaseSchema):
    # Inventory swagger.json

    
    delete = fields.Boolean(required=False)
    
    archive = fields.Boolean(required=False)
    
    archive_dir = fields.Str(required=False)
    


class Audit(BaseSchema):
    # Inventory swagger.json

    
    created_by = fields.Str(required=False)
    
    modified_by = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    


class CatalogMasterConfig(BaseSchema):
    # Inventory swagger.json

    
    source_slug = fields.Str(required=False)
    


class CompanyConfig(BaseSchema):
    # Inventory swagger.json

    
    company_id = fields.Int(required=False)
    
    exclude_steps = fields.List(fields.Int(required=False), required=False)
    
    hidden_closet_keys = fields.List(fields.Str(required=False), required=False)
    
    open_tags = fields.Dict(required=False)
    
    tax_identifiers = fields.List(fields.Str(required=False), required=False)
    
    delete_quantity_threshold = fields.Int(required=False)
    


class DBConfig(BaseSchema):
    # Inventory swagger.json

    
    vendor = fields.Str(required=False)
    
    host = fields.Str(required=False)
    
    port = fields.Int(required=False)
    
    username = fields.Str(required=False)
    
    password = fields.Str(required=False)
    
    dbname = fields.Str(required=False)
    
    query = fields.Str(required=False)
    
    procedure = fields.Boolean(required=False)
    
    driver_class = fields.Str(required=False)
    
    jdbc_url = fields.Str(required=False)
    
    optional_properties = fields.Dict(required=False)
    


class DBConnectionProfile(BaseSchema):
    # Inventory swagger.json

    
    inventory = fields.Str(required=False)
    


class DBParamConfig(BaseSchema):
    # Inventory swagger.json

    
    params = fields.Dict(required=False)
    


class DefaultHeadersDTO(BaseSchema):
    # Inventory swagger.json

    
    store = fields.Nested(PropBeanDTO, required=False)
    
    intf_article_id = fields.Nested(PropBeanDTO, required=False)
    
    price_effective = fields.Nested(PropBeanDTO, required=False)
    
    quantity = fields.Nested(PropBeanDTO, required=False)
    


class DocMappingConfig(BaseSchema):
    # Inventory swagger.json

    
    properties = fields.Dict(required=False)
    
    junk_data_threshold_count = fields.Int(required=False)
    
    prop_bean_configs = fields.List(fields.Nested(PropBeanConfig, required=False), required=False)
    
    unwind_field = fields.Str(required=False)
    
    default_headers = fields.Nested(DefaultHeadersDTO, required=False)
    


class EmailConfig(BaseSchema):
    # Inventory swagger.json

    
    recepient = fields.Str(required=False)
    
    host = fields.Str(required=False)
    
    username = fields.Str(required=False)
    
    password = fields.Str(required=False)
    
    unzip = fields.Boolean(required=False)
    
    read_from_content = fields.Boolean(required=False)
    
    filter_based_on_recepients = fields.Boolean(required=False)
    
    pcol = fields.Str(required=False)
    
    subject_line_regex = fields.Str(required=False)
    
    sender_address = fields.Str(required=False)
    
    local_dir = fields.Str(required=False)
    
    folder_name_hierarchies = fields.List(fields.Str(required=False), required=False)
    
    attachment_regex = fields.Str(required=False)
    
    body_content_regex = fields.Str(required=False)
    
    password_protected = fields.Boolean(required=False)
    
    zip_format = fields.Str(required=False)
    
    attachment_mandate = fields.Boolean(required=False)
    
    filter_files_after_extraction = fields.Boolean(required=False)
    
    archive_config = fields.Nested(ArchiveConfig, required=False)
    
    read_all_unread_mails = fields.Boolean(required=False)
    
    content_type = fields.Str(required=False)
    
    downloadable_link = fields.Boolean(required=False)
    
    properties = fields.Dict(required=False)
    


class FTPConfig(BaseSchema):
    # Inventory swagger.json

    
    host = fields.Str(required=False)
    
    port = fields.Int(required=False)
    
    username = fields.Str(required=False)
    
    password = fields.Str(required=False)
    
    unzip = fields.Boolean(required=False)
    
    retries = fields.Int(required=False)
    
    interval = fields.Int(required=False)
    
    local_dir = fields.Str(required=False)
    
    remote_dir = fields.Str(required=False)
    
    zip_file_regex = fields.Str(required=False)
    
    archive_config = fields.Nested(ArchiveConfig, required=False)
    
    file_regex = fields.Str(required=False)
    
    zip_format = fields.Str(required=False)
    
    read_all_files = fields.Boolean(required=False)
    


class FileConfig(BaseSchema):
    # Inventory swagger.json

    
    delimiter = fields.Str(required=False)
    
    charset = fields.Str(required=False)
    
    properties = fields.Dict(required=False)
    
    file_has_header = fields.Boolean(required=False)
    
    header_index = fields.Int(required=False)
    
    header_array = fields.List(fields.Str(required=False), required=False)
    
    data_start_index = fields.Int(required=False)
    
    prop_bean_configs = fields.List(fields.Nested(PropBeanConfig, required=False), required=False)
    
    junk_data_threshold_count = fields.Int(required=False)
    
    file_type = fields.Str(required=False)
    
    line_validity_check = fields.Boolean(required=False)
    
    sheet_names = fields.List(fields.Str(required=False), required=False)
    
    read_all_sheets = fields.Boolean(required=False)
    
    quote_char = fields.Str(required=False)
    
    escape_char = fields.Str(required=False)
    
    default_headers = fields.Nested(DefaultHeadersDTO, required=False)
    


class GoogleSpreadSheetConfig(BaseSchema):
    # Inventory swagger.json

    
    range = fields.Str(required=False)
    
    sheet_id = fields.Str(required=False)
    
    client_secret_location = fields.Str(required=False)
    
    cred_storage_directory = fields.Str(required=False)
    
    local_dir = fields.Str(required=False)
    
    archive_config = fields.Nested(ArchiveConfig, required=False)
    


class HttpConfig(BaseSchema):
    # Inventory swagger.json

    
    hosturl = fields.Str(required=False)
    
    username = fields.Str(required=False)
    
    password = fields.Str(required=False)
    
    request_params = fields.Dict(required=False)
    
    http_method = fields.Str(required=False)
    
    request_payload = fields.Str(required=False)
    
    local_path = fields.Str(required=False)
    
    archive_config = fields.Nested(ArchiveConfig, required=False)
    


class JobConfig(BaseSchema):
    # Inventory swagger.json

    
    _id = fields.Int(required=False)
    
    job_code = fields.Str(required=False)
    
    task_type = fields.Str(required=False)
    
    sync_delay = fields.Int(required=False)
    
    cron_expression = fields.Str(required=False)
    
    store_filter = fields.Nested(StoreFilter, required=False)
    
    process_config = fields.Nested(ProcessConfig, required=False)
    
    store_config = fields.List(fields.Nested(StoreConfig, required=False), required=False)
    
    properties = fields.Dict(required=False)
    
    immediate_first_run = fields.Boolean(required=False)
    
    disable = fields.Boolean(required=False)
    
    dependent_job_codes = fields.List(fields.Str(required=False), required=False)
    
    company_config = fields.List(fields.Nested(CompanyConfig, required=False), required=False)
    
    company_ids = fields.List(fields.Int(required=False), required=False)
    
    tax_identifiers = fields.List(fields.Str(required=False), required=False)
    
    priority = fields.Str(required=False)
    
    period_threshold = fields.Int(required=False)
    
    period_threshold_type = fields.Str(required=False)
    
    db_connection_profile = fields.Nested(DBConnectionProfile, required=False)
    
    params = fields.Dict(required=False)
    
    open_tags = fields.Dict(required=False)
    
    delete_quantity_threshold = fields.Int(required=False)
    
    catalog_master_config = fields.Nested(CatalogMasterConfig, required=False)
    
    aggregator_types = fields.List(fields.Str(required=False), required=False)
    
    integration_type = fields.Str(required=False)
    
    min_price = fields.Float(required=False)
    
    audit = fields.Nested(Audit, required=False)
    
    version = fields.Int(required=False)
    
    alias = fields.Str(required=False)
    


class JobConfigRawDTO(BaseSchema):
    # Inventory swagger.json

    
    integration = fields.Str(required=False)
    
    company_name = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    data = fields.Nested(JobConfig, required=False)
    


class JsonDocConfig(BaseSchema):
    # Inventory swagger.json

    
    prop_bean_configs = fields.List(fields.Nested(PropBeanConfig, required=False), required=False)
    


class LocalFileConfig(BaseSchema):
    # Inventory swagger.json

    
    retries = fields.Int(required=False)
    
    interval = fields.Int(required=False)
    
    local_dir = fields.Str(required=False)
    
    working_dir = fields.Str(required=False)
    
    unzip = fields.Boolean(required=False)
    
    zip_file_regex = fields.Str(required=False)
    
    file_regex = fields.Str(required=False)
    
    zip_format = fields.Str(required=False)
    
    archive_config = fields.Nested(ArchiveConfig, required=False)
    
    read_all_files = fields.Boolean(required=False)
    


class MongoDocConfig(BaseSchema):
    # Inventory swagger.json

    
    collection_name = fields.Str(required=False)
    
    find_query = fields.Dict(required=False)
    
    projection_query = fields.Dict(required=False)
    
    prop_bean_configs = fields.List(fields.Nested(PropBeanConfig, required=False), required=False)
    
    aggregate_pipeline = fields.List(fields.Dict(required=False), required=False)
    
    skip_save = fields.Boolean(required=False)
    


class OAuthConfig(BaseSchema):
    # Inventory swagger.json

    
    limit = fields.Int(required=False)
    
    pages = fields.Int(required=False)
    
    interval = fields.Int(required=False)
    
    consumer_key = fields.Str(required=False)
    
    consumer_secret = fields.Str(required=False)
    
    token = fields.Str(required=False)
    
    token_secret = fields.Str(required=False)
    
    rest_url = fields.Str(required=False)
    
    rest_base_url = fields.Str(required=False)
    
    function_name = fields.Str(required=False)
    


class ProcessConfig(BaseSchema):
    # Inventory swagger.json

    
    db_config = fields.Nested(DBConfig, required=False)
    
    db_param_config = fields.Nested(DBParamConfig, required=False)
    
    sftp_config = fields.Nested(SFTPConfig, required=False)
    
    aws_s3_config = fields.Nested(AWSS3config, required=False)
    
    mongo_doc_config = fields.Nested(MongoDocConfig, required=False)
    
    ftp_config = fields.Nested(FTPConfig, required=False)
    
    email_config = fields.Nested(EmailConfig, required=False)
    
    file_config = fields.Nested(FileConfig, required=False)
    
    json_doc_config = fields.Nested(JsonDocConfig, required=False)
    
    doc_mapping_config = fields.Nested(DocMappingConfig, required=False)
    
    task_step_config = fields.Nested(TaskStepConfig, required=False)
    
    http_config = fields.Nested(HttpConfig, required=False)
    
    local_file_config = fields.Nested(LocalFileConfig, required=False)
    
    oauth_config = fields.Nested(OAuthConfig, required=False)
    
    google_spreadsheet_config = fields.Nested(GoogleSpreadSheetConfig, required=False)
    


class PropBeanConfig(BaseSchema):
    # Inventory swagger.json

    
    required = fields.Boolean(required=False)
    
    optional = fields.Boolean(required=False)
    
    send = fields.Nested(Send, required=False)
    
    validations = fields.List(fields.Dict(required=False), required=False)
    
    values = fields.List(fields.Str(required=False), required=False)
    
    include = fields.Boolean(required=False)
    
    source_field = fields.Str(required=False)
    
    source_fields = fields.List(fields.Str(required=False), required=False)
    
    destination_field = fields.Str(required=False)
    
    data_type = fields.Str(required=False)
    
    default_value = fields.Dict(required=False)
    
    const_value = fields.Dict(required=False)
    
    concat_str = fields.Str(required=False)
    
    function_name = fields.Str(required=False)
    
    transformer_name = fields.Str(required=False)
    
    all_param_function_name = fields.Str(required=False)
    
    sub_separator = fields.Str(required=False)
    
    index_field = fields.Str(required=False)
    
    ignore_if_not_exists = fields.Boolean(required=False)
    
    identifier_type = fields.Str(required=False)
    
    projection_query = fields.Dict(required=False)
    
    enrich_from_master = fields.Boolean(required=False)
    


class PropBeanDTO(BaseSchema):
    # Inventory swagger.json

    
    required = fields.Boolean(required=False)
    
    optional = fields.Boolean(required=False)
    
    include = fields.Boolean(required=False)
    
    source_field = fields.Str(required=False)
    
    source_fields = fields.List(fields.Str(required=False), required=False)
    
    destination_field = fields.Str(required=False)
    
    data_type = fields.Str(required=False)
    
    default_value = fields.Dict(required=False)
    
    const_value = fields.Dict(required=False)
    
    concat_str = fields.Str(required=False)
    
    function_name = fields.Str(required=False)
    
    transformer_name = fields.Str(required=False)
    
    all_param_function_name = fields.Str(required=False)
    
    sub_separator = fields.Str(required=False)
    
    index_field = fields.Str(required=False)
    
    ignore_if_not_exists = fields.Boolean(required=False)
    
    identifier_type = fields.Str(required=False)
    
    projection_query = fields.Dict(required=False)
    
    enrich_from_master = fields.Boolean(required=False)
    


class ResponseEnvelopeListJobConfigRawDTO(BaseSchema):
    # Inventory swagger.json

    
    timestamp = fields.Str(required=False)
    
    status = fields.Int(required=False)
    
    error = fields.Str(required=False)
    
    exception = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    total_time_taken_in_millis = fields.Int(required=False)
    
    http_status = fields.Str(required=False)
    
    items = fields.List(fields.Nested(JobConfigRawDTO, required=False), required=False)
    
    payload = fields.List(fields.Nested(JobConfigRawDTO, required=False), required=False)
    
    trace_id = fields.Str(required=False)
    
    page = fields.Nested(Page, required=False)
    


class SFTPConfig(BaseSchema):
    # Inventory swagger.json

    
    host = fields.Str(required=False)
    
    port = fields.Int(required=False)
    
    username = fields.Str(required=False)
    
    password = fields.Str(required=False)
    
    unzip = fields.Boolean(required=False)
    
    retries = fields.Int(required=False)
    
    interval = fields.Int(required=False)
    
    private_key_path = fields.Str(required=False)
    
    strict_host_key_checking = fields.Boolean(required=False)
    
    local_dir = fields.Str(required=False)
    
    remote_dir = fields.Str(required=False)
    
    password_protected = fields.Boolean(required=False)
    
    zip_file_regex = fields.Str(required=False)
    
    file_regex = fields.Str(required=False)
    
    zip_format = fields.Str(required=False)
    
    archive_config = fields.Nested(ArchiveConfig, required=False)
    
    read_all_files = fields.Boolean(required=False)
    


class Send(BaseSchema):
    # Inventory swagger.json

    
    raw = fields.Boolean(required=False)
    
    processed = fields.Boolean(required=False)
    


class StoreConfig(BaseSchema):
    # Inventory swagger.json

    
    job_code = fields.Str(required=False)
    
    storeid = fields.Str(required=False)
    
    store_alias = fields.Str(required=False)
    
    store_file_regex = fields.Str(required=False)
    
    store_file_name = fields.Str(required=False)
    
    process_config = fields.Nested(ProcessConfig, required=False)
    
    properties = fields.Dict(required=False)
    


class StoreFilter(BaseSchema):
    # Inventory swagger.json

    
    include_tags = fields.List(fields.Str(required=False), required=False)
    
    exclude_tags = fields.List(fields.Str(required=False), required=False)
    
    query = fields.Dict(required=False)
    


class TaskConfig(BaseSchema):
    # Inventory swagger.json

    
    name = fields.Str(required=False)
    
    task_config_id = fields.Int(required=False)
    
    task_params = fields.List(fields.Nested(TaskParam, required=False), required=False)
    


class TaskParam(BaseSchema):
    # Inventory swagger.json

    
    name = fields.Str(required=False)
    
    value = fields.Dict(required=False)
    


class TaskStepConfig(BaseSchema):
    # Inventory swagger.json

    
    task_configs = fields.List(fields.Nested(TaskConfig, required=False), required=False)
    
    task_config_ids = fields.List(fields.Int(required=False), required=False)
    
    task_config_group_ids = fields.List(fields.Int(required=False), required=False)
    


class JobStepsDTO(BaseSchema):
    # Inventory swagger.json

    
    step_name = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    step_execution_time = fields.Int(required=False)
    
    start_count = fields.Int(required=False)
    
    end_count = fields.Int(required=False)
    
    deleted_count = fields.Int(required=False)
    
    processed_start_time = fields.Str(required=False)
    
    processed_at = fields.Str(required=False)
    


class ResponseEnvelopeListJobStepsDTO(BaseSchema):
    # Inventory swagger.json

    
    timestamp = fields.Str(required=False)
    
    status = fields.Int(required=False)
    
    error = fields.Str(required=False)
    
    exception = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    total_time_taken_in_millis = fields.Int(required=False)
    
    http_status = fields.Str(required=False)
    
    items = fields.List(fields.Nested(JobStepsDTO, required=False), required=False)
    
    payload = fields.List(fields.Nested(JobStepsDTO, required=False), required=False)
    
    trace_id = fields.Str(required=False)
    
    page = fields.Nested(Page, required=False)
    


class ResponseEnvelopeListJobConfigDTO(BaseSchema):
    # Inventory swagger.json

    
    timestamp = fields.Str(required=False)
    
    status = fields.Int(required=False)
    
    error = fields.Str(required=False)
    
    exception = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    total_time_taken_in_millis = fields.Int(required=False)
    
    http_status = fields.Str(required=False)
    
    items = fields.List(fields.Nested(JobConfigDTO, required=False), required=False)
    
    payload = fields.List(fields.Nested(JobConfigDTO, required=False), required=False)
    
    trace_id = fields.Str(required=False)
    
    page = fields.Nested(Page, required=False)
    


class ResponseEnvelopeJobConfigDTO(BaseSchema):
    # Inventory swagger.json

    
    timestamp = fields.Str(required=False)
    
    status = fields.Int(required=False)
    
    error = fields.Str(required=False)
    
    exception = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    total_time_taken_in_millis = fields.Int(required=False)
    
    http_status = fields.Str(required=False)
    
    items = fields.Nested(JobConfigDTO, required=False)
    
    payload = fields.Nested(JobConfigDTO, required=False)
    
    trace_id = fields.Str(required=False)
    
    page = fields.Nested(Page, required=False)
    


class JobHistoryDto(BaseSchema):
    # Inventory swagger.json

    
    total_added_count = fields.Int(required=False)
    
    total_updated_count = fields.Int(required=False)
    
    total_suppressed_count = fields.Int(required=False)
    
    total_initial_count = fields.Int(required=False)
    
    job_id = fields.Int(required=False)
    
    status = fields.Str(required=False)
    
    job_code = fields.Str(required=False)
    
    processed_on = fields.Str(required=False)
    
    filename = fields.List(fields.Str(required=False), required=False)
    
    error_type = fields.Str(required=False)
    
    message = fields.Str(required=False)
    


class JobMetricsDto(BaseSchema):
    # Inventory swagger.json

    
    job_code = fields.Str(required=False)
    
    is_run_more_than_usual = fields.Str(required=False)
    
    job_history = fields.List(fields.Nested(JobHistoryDto, required=False), required=False)
    
    total_success_count = fields.Int(required=False)
    
    total_failure_count = fields.Int(required=False)
    
    total_warning_count = fields.Int(required=False)
    
    total_suppressed_count = fields.Int(required=False)
    
    total_job_runs = fields.Int(required=False)
    


class ResponseEnvelopeJobMetricsDto(BaseSchema):
    # Inventory swagger.json

    
    timestamp = fields.Str(required=False)
    
    status = fields.Int(required=False)
    
    error = fields.Str(required=False)
    
    exception = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    total_time_taken_in_millis = fields.Int(required=False)
    
    http_status = fields.Str(required=False)
    
    items = fields.Nested(JobMetricsDto, required=False)
    
    payload = fields.Nested(JobMetricsDto, required=False)
    
    trace_id = fields.Str(required=False)
    
    page = fields.Nested(Page, required=False)
    


class JobConfigListDTO(BaseSchema):
    # Inventory swagger.json

    
    code = fields.Str(required=False)
    
    alias = fields.Str(required=False)
    
    modified_by = fields.Str(required=False)
    
    created_by = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    active = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    


class ResponseEnvelopeListJobConfigListDTO(BaseSchema):
    # Inventory swagger.json

    
    timestamp = fields.Str(required=False)
    
    status = fields.Int(required=False)
    
    error = fields.Str(required=False)
    
    exception = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    total_time_taken_in_millis = fields.Int(required=False)
    
    http_status = fields.Str(required=False)
    
    items = fields.List(fields.Nested(JobConfigListDTO, required=False), required=False)
    
    payload = fields.List(fields.Nested(JobConfigListDTO, required=False), required=False)
    
    trace_id = fields.Str(required=False)
    
    page = fields.Nested(Page, required=False)
    


