

"""Catalog Platform Application Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema



    
    
        
        
        
    
    
        
        
        
        
        
    
    
        
        
        
    
    
        
        
        
        
        
        
        
    
    
        
        
        
    
    
        
        
        
        
        
        
    
    
        
        
        
    
    
        
        
    
    
        
        
        
        
        
        
        
        
        
    
    
        
        
        
        
        
        
        
        
    
    
        
        
        
    
    
        
        
    
    
        
        
        
        
        
        
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
        
        
        
        
        
        
        
        
        
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
        
        
        
        
        
        
        
    
    
        
        
        
    
    
        
        
        
        
        
        
        
        
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
        
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
        
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
    
    
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
        
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
    
    
        
        
    
    
        
        
        
    
    
        
        
        
        
        
        
        
    
    
        
        
        
    
    
        
        
        
        
        
        
        
    
    
        
        
        
        
    
    
        
        
        
        
    
    
        
        
        
        
    
    
        
        
        
        
    
    
        
        
        
        
    
    
        
        
    
    
        
        
    
    
        
        
        
    
    
        
        
        
        
        
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
        
    
    
        
        
        
    
    
        
        
        
        
    
    
        
        
    
    
        
        
        
        
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
        
        
        
        
        
    
    
        
        
        
    
    
        
        
        
        
    
    
        
        
        
        
    
    
        
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
        
        
        
    
    
        
        
        
        
        
    
    
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
    
    
        
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
        
    
    
        
        
        
        
        
        

class CatalogValidator:
    
    
    class getCatalogInsights(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        brand = fields.Str(required=False)
         
        
    
    class getApplicationBrandListing(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        q = fields.Str(required=False)
         
        
    
    class updateAppBrand(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        brand_uid = fields.Int(required=False)
         
        
    
    class getApplicationBrands(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        department = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        q = fields.Str(required=False)
        
        brand_id = fields.List(fields.Int(required=False), required=False)
         
        
    
    class getCategories(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        department = fields.Str(required=False)
         
        
    
    class getApplicationCategoryListing(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        department_id = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        q = fields.Str(required=False)
         
        
    
    class updateAppCategory(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        category_uid = fields.Int(required=False)
         
        
    
    class createCollection(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getAllCollections(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        q = fields.Str(required=False)
        
        schedule_status = fields.Str(required=False)
        
        type = fields.Str(required=False)
        
        tag = fields.List(fields.Str(required=False), required=False)
        
        is_active = fields.Boolean(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
        
    
    class getApplicationFilterValues(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        filter_key = fields.Str(required=False)
        
        c = fields.Str(required=False)
        
        collection_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        q = fields.Str(required=False)
         
        
    
    class getApplicationFilterKeys(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        c = fields.Str(required=False)
         
        
    
    class getQueryFilters(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getCollectionItems(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
        
        sort_on = fields.Str(required=False)
        
        page_size = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
        
        is_pinned = fields.Boolean(required=False)
        
        q = fields.Str(required=False)
        
        is_excluded = fields.Boolean(required=False)
         
        
    
    class clearCollectionItemsPriority(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class addCollectionItems(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class getCollectionDetail(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        slug = fields.Str(required=False)
         
        
    
    class updateCollection(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class deleteCollection(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class getApplicationDepartmentListing(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        q = fields.Str(required=False)
         
        
    
    class updateAppDepartment(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        department_uid = fields.Int(required=False)
         
        
    
    class getConfigurationsFilterMetadata(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        filter = fields.Str(required=False)
         
        
    
    class getDepartments(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getAppInventory(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        item_ids = fields.List(fields.Int(required=False), required=False)
        
        store_ids = fields.List(fields.Int(required=False), required=False)
        
        brand_ids = fields.List(fields.Int(required=False), required=False)
        
        seller_identifiers = fields.List(fields.Str(required=False), required=False)
        
        timestamp = fields.Str(required=False)
        
        page_size = fields.Int(required=False)
        
        page_id = fields.Str(required=False)
        
        qty_gt = fields.Int(required=False)
        
        qty_lt = fields.Int(required=False)
        
        qty_type = fields.Str(required=False)
        
        from_date = fields.Str(required=False)
        
        to_date = fields.Str(required=False)
         
        
    
    class getAppLocations(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        store_type = fields.Str(required=False)
        
        uid = fields.List(fields.Int(required=False), required=False)
        
        q = fields.Str(required=False)
        
        stage = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        tags = fields.List(fields.Str(required=False), required=False)
        
        store_types = fields.List(fields.Str(required=False), required=False)
        
        company_uids = fields.List(fields.Int(required=False), required=False)
         
        
    
    class getConfigurations(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class createConfigurationProductListing(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getCatalogConfiguration(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getConfigurationByType(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        type = fields.Str(required=False)
         
        
    
    class createConfigurationByType(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        type = fields.Str(required=False)
         
        
    
    class getAppProduct(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        item_id = fields.Int(required=False)
         
        
    
    class updateAppProduct(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        item_id = fields.Int(required=False)
         
        
    
    class getAppicationProducts(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        q = fields.Str(required=False)
        
        f = fields.Str(required=False)
        
        c = fields.Str(required=False)
        
        filters = fields.Boolean(required=False)
        
        is_dependent = fields.Boolean(required=False)
        
        sort_on = fields.Str(required=False)
        
        page_id = fields.Str(required=False)
        
        page_size = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
        
        page_type = fields.Str(required=False)
        
        item_ids = fields.List(fields.Str(required=False), required=False)
         
        
    
    class getDiscountedInventoryBySizeIdentifier(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        item_id = fields.Int(required=False)
        
        size_identifier = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        location_ids = fields.List(fields.Int(required=False), required=False)
         
        
    
    class getProductDetailBySlug(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        slug = fields.Str(required=False)
         
        
    
    class getAppProducts(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        brand_ids = fields.List(fields.Int(required=False), required=False)
        
        category_ids = fields.List(fields.Int(required=False), required=False)
        
        department_ids = fields.List(fields.Int(required=False), required=False)
        
        tags = fields.List(fields.Str(required=False), required=False)
        
        item_ids = fields.List(fields.Int(required=False), required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        q = fields.Str(required=False)
         
        
    
    class getAppReturnConfiguration(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class createAppReturnConfiguration(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class updateAppReturnConfiguration(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class deleteAppCategoryReturnConfiguration(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getAppCategoryReturnConfig(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        q = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
        
    
    class createAppCategoryReturnConfiguration(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class updateAppCategoryReturnConfiguration(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class createCustomAutocompleteRule(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getAutocompleteConfig(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        q = fields.Str(required=False)
        
        is_active = fields.Boolean(required=False)
         
        
    
    class getAutocompleteKeywordDetail(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class updateAutocompleteKeyword(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class deleteAutocompleteKeyword(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class createSearchRerank(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getSearchRerank(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getSearchRerankDetail(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class updateSearchRerankConfiguration(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class deleteSearchRerankConfiguration(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class createSearchConfiguration(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getSearchConfiguration(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class updateSearchConfiguration(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class deleteSearchConfiguration(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class createCustomKeyword(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getAllSearchKeyword(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        q = fields.Str(required=False)
        
        is_active = fields.Boolean(required=False)
         
        
    
    class getSearchKeywords(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class updateSearchKeywords(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class deleteSearchKeywords(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class updateAppLocation(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        store_uid = fields.Int(required=False)
         
        
    
    class updateAllowSingle(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class updateDefaultSort(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class createListingConfiguration(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        config_type = fields.Str(required=False)
         
        
    
    class getListingConfigurations(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        config_type = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        search = fields.Str(required=False)
        
        uids = fields.List(fields.Int(required=False), required=False)
         
        
    
    class createGroupConfiguration(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        config_type = fields.Str(required=False)
         
        
    
    class getGroupConfigurations(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        config_type = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        search = fields.Str(required=False)
        
        template_slug = fields.Str(required=False)
         
        
    
    class updateGroupConfiguration(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        config_type = fields.Str(required=False)
        
        group_slug = fields.Str(required=False)
         
        
    
    class deleteGroupConfiguration(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        config_type = fields.Str(required=False)
        
        group_slug = fields.Str(required=False)
         
        
    
    class updateListingConfiguration(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        config_type = fields.Str(required=False)
        
        config_id = fields.Str(required=False)
         
        
    
    class deleteListingConfiguration(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        config_type = fields.Str(required=False)
        
        config_id = fields.Str(required=False)
         
        
    
    class getConfigurationMetadata(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        config_type = fields.Str(required=False)
        
        template_slug = fields.Str(required=False)
         
        
    
    class createAutocompleteSettings(BaseSchema):
        
        
        application_id = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
         
        
    
    class getAutocompleteSettings(BaseSchema):
        
        
        application_id = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
         
        
    
    class updateAutocompleteSettings(BaseSchema):
        
        
        application_id = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class getAutocompletePreview(BaseSchema):
        
        
        application_id = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
        
        q = fields.Str(required=False)
        
        category_suggestion = fields.Int(required=False)
        
        brand_suggestion = fields.Int(required=False)
        
        collection_suggestion = fields.Int(required=False)
        
        product_suggestion = fields.Int(required=False)
        
        query_suggestion = fields.Int(required=False)
         
        
    
    class createMerchandisingRulePinAction(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        merchandising_rule_id = fields.Str(required=False)
         
        
    
    class updateMerchandisingRulePinAction(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        merchandising_rule_id = fields.Str(required=False)
         
        
    
    class getMerchandisingRulePinAction(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        merchandising_rule_id = fields.Str(required=False)
         
        
    
    class createMerchandisingRuleHideAction(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        merchandising_rule_id = fields.Str(required=False)
         
        
    
    class updateMerchandisingRuleHideAction(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        merchandising_rule_id = fields.Str(required=False)
         
        
    
    class getMerchandisingRuleHideAction(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        merchandising_rule_id = fields.Str(required=False)
         
        
    
    class createMerchandisingRuleBoostAction(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        merchandising_rule_id = fields.Str(required=False)
         
        
    
    class updateMerchandisingRuleBoostAction(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        merchandising_rule_id = fields.Str(required=False)
         
        
    
    class getMerchandisingRuleBoostAction(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        merchandising_rule_id = fields.Str(required=False)
         
        
    
    class createMerchandisingRuleBuryAction(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        merchandising_rule_id = fields.Str(required=False)
         
        
    
    class updateMerchandisingRuleBuryAction(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        merchandising_rule_id = fields.Str(required=False)
         
        
    
    class getMerchandisingRuleBuryAction(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        merchandising_rule_id = fields.Str(required=False)
         
        
    
    class createMerchandisingRuleQuery(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getMerchandisingQuery(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        merchandising_rule_id = fields.Str(required=False)
         
        
    
    class updateMerchandisingRuleQuery(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        merchandising_rule_id = fields.Str(required=False)
         
        
    
    class saveMerchandisingRules(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        merchandising_rule_id = fields.Str(required=False)
         
        
    
    class deleteMerchandisingRule(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        merchandising_rule_id = fields.Str(required=False)
         
        
    
    class getMerchandisingRules(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        page_id = fields.Str(required=False)
        
        page_size = fields.Int(required=False)
         
        
    
    class deleteMerchandisingRulesPreview(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        merchandising_rule_id = fields.Str(required=False)
         
        
    
    class getLivePreview(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        merchandising_rule_id = fields.Str(required=False)
        
        search_keyword = fields.Str(required=False)
         
        
    
    class createAppPriceFactory(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getAppPriceFactories(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        is_active = fields.Boolean(required=False)
        
        factory_type_id = fields.Str(required=False)
        
        code = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
        
    
    class getAppPriceFactory(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class editAppPriceFactory(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class addProductsInPriceFactoryByZoneId(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class getProductsInPriceFactoryByZoneId(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
        
        zone_id = fields.Str(required=False)
        
        item_id = fields.Float(required=False)
        
        q = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
        
    
    class createProductPriceFactoryBulkJob(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class pollProductPriceFactoryBulkJob(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
        
        job_id = fields.Str(required=False)
         
        
    
    class validateProductPriceFactoryBulkJob(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
        
        job_id = fields.Str(required=False)
         
        
    
    class processProductPriceFactoryBulkJob(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
        
        job_id = fields.Str(required=False)
         
        
    
    class exportProductsInPriceFactory(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class pollPriceFactoryJobs(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class getAppProductPrices(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        item_ids = fields.List(fields.Int(required=False), required=False)
        
        factory_type_ids = fields.List(fields.Str(required=False), required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
        
    
    class getSynonyms(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
        
        name = fields.Str(required=False)
        
        type = fields.Str(required=False)
         
        
    
    class createSynonyms(BaseSchema):
        
        
        application_id = fields.Int(required=False)
        
        company_id = fields.Int(required=False)
         
        
    
    class updateSynonyms(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class deleteSynonym(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class exportSynonyms(BaseSchema):
        
        
        application_id = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
         
        
    
    class sampleBulkSynonymsFile(BaseSchema):
        
        
        type = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
         
        
    
    class uploadSynonyms(BaseSchema):
        
        
        application_id = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
         
        
    
    class validateBulkSynonyms(BaseSchema):
        
        
        application_id = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
         
        
    
    class processBulkSynonyms(BaseSchema):
        
        
        application_id = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
         
        
    
    class pollBulkSynonyms(BaseSchema):
        
        
        application_id = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class getAppPriceById(BaseSchema):
        
        
        application_id = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
        
        item_id = fields.Int(required=False)
        
        store_ids = fields.List(fields.Int(required=False), required=False)
        
        factory_type_ids = fields.List(fields.Str(required=False), required=False)
        
        seller_id = fields.Int(required=False)
         
        
    
    

