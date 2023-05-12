

"""Catalog Platform Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema




    
    
        
        
        
    
    
        
    
    
        
        
    
    
        
        
    
    
        
        
        
        
        
        
    
    
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
    
    
        
    
    
        
        
        
        
        
        
    
    
        
    
    
        
        
        
        
    
    
        
        
    
    
        
        
        
    
    
        
        
        
        
        
        
        
    
    
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
    
    
        
    
    
        
        
        
        
        
    
    
        
    
    
        
        
        
        
    
    
        
        
        
        
        
        
    
    
        
    
    
        
        
    
    
        
        
    
    
        
        
        
        
        
        
        
        
        
        
    
    
        
    
    
        
        
        
        
        
    
    
        
        
        
    
    
        
        
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
    
    
        
        
        
        
        
    
    
        
        
        
        
    
    
        
    
    
        
        
        
    
    
        
        
    
    
        
        
    
    
        
    
    
        
        
        
    
    
        
    
    
        
        
        
    
    
        
        
        
        
        
        
        
    
    
        
        
        
    
    
        
        
        
        
        
        
        
    
    
        
        
        
        
        
        
        
        
        
    
    
        
        
        
        
    
    
        
        
        
    
    
        
    
    
        
        
    
    
        
        
    
    
        
    
    
        
    
    
        
        
        
        
        
    
    
        
    
    
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
    
    
        
        
    
    
        
        
    
    
        
    
    
        
        
        
        
        
    
    
        
        
    
    
        



class CatalogValidator:
    
    
    class getProductBundle(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        q = fields.Str(required=False)
        
        slug = fields.List(fields.Str(required=False), required=False)
         
        
    
    class createProductBundle(BaseSchema):
        
        
        company_id = fields.Str(required=False)
         
        
    
    class getProductBundleDetail(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class updateProductBundle(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class getSizeGuides(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        active = fields.Boolean(required=False)
        
        q = fields.Str(required=False)
        
        tag = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
        
    
    class createSizeGuide(BaseSchema):
        
        
        company_id = fields.Str(required=False)
         
        
    
    class getSizeGuide(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class updateSizeGuide(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class getSellerInsights(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        seller_app_id = fields.Str(required=False)
         
        
    
    class createMarketplaceOptin(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        marketplace = fields.Str(required=False)
         
        
    
    class getMarketplaceOptinDetail(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class getCompanyDetail(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class getCompanyBrandDetail(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        is_active = fields.Boolean(required=False)
        
        q = fields.Boolean(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        marketplace = fields.Str(required=False)
         
        
    
    class getCompanyMetrics(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class getStoreDetail(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        q = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
        
    
    class getGenderAttribute(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        attribute_slug = fields.Str(required=False)
         
        
    
    class listProductTemplateCategories(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        departments = fields.Str(required=False)
        
        item_type = fields.Str(required=False)
         
        
    
    class listDepartmentsData(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        item_type = fields.Str(required=False)
        
        page_size = fields.Int(required=False)
        
        name = fields.Str(required=False)
        
        search = fields.Str(required=False)
        
        is_active = fields.Boolean(required=False)
         
        
    
    class createDepartments(BaseSchema):
        
        
        company_id = fields.Str(required=False)
         
        
    
    class getDepartmentData(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        uid = fields.Str(required=False)
         
        
    
    class updateDepartment(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        uid = fields.Str(required=False)
         
        
    
    class listProductTemplate(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        department = fields.Str(required=False)
         
        
    
    class validateProductTemplate(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        slug = fields.Str(required=False)
         
        
    
    class downloadProductTemplateViews(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        slug = fields.Str(required=False)
         
        
    
    class downloadInventoryTemplateView(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        item_type = fields.Str(required=False)
         
        
    
    class validateProductTemplateSchema(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        item_type = fields.Str(required=False)
         
        
    
    class listHSNCodes(BaseSchema):
        
        
        company_id = fields.Str(required=False)
         
        
    
    class listProductTemplateExportDetails(BaseSchema):
        
        
        company_id = fields.Str(required=False)
         
        
    
    class getProductExportJobs(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        status = fields.Str(required=False)
        
        from_date = fields.Str(required=False)
        
        to_date = fields.Str(required=False)
        
        q = fields.Str(required=False)
         
        
    
    class createProductExportJob(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class listTemplateBrandTypeValues(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        filter = fields.Str(required=False)
        
        template_tag = fields.Str(required=False)
        
        item_type = fields.Str(required=False)
         
        
    
    class listCategories(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        level = fields.Str(required=False)
        
        departments = fields.Str(required=False)
        
        q = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
        
    
    class createCategories(BaseSchema):
        
        
        company_id = fields.Str(required=False)
         
        
    
    class getCategoryData(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        uid = fields.Str(required=False)
         
        
    
    class updateCategory(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        uid = fields.Str(required=False)
         
        
    
    class getProducts(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        brand_ids = fields.List(fields.Int(required=False), required=False)
        
        category_ids = fields.List(fields.Int(required=False), required=False)
        
        item_ids = fields.List(fields.Int(required=False), required=False)
        
        department_ids = fields.List(fields.Int(required=False), required=False)
        
        item_code = fields.List(fields.Str(required=False), required=False)
        
        q = fields.Str(required=False)
        
        tags = fields.List(fields.Str(required=False), required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
        
    
    class createProduct(BaseSchema):
        
        
        company_id = fields.Str(required=False)
         
        
    
    class getVariantsOfProducts(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        item_id = fields.Int(required=False)
        
        variant_type = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
        
    
    class getProductAttributes(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        category = fields.Str(required=False)
        
        filter = fields.Boolean(required=False)
         
        
    
    class getProduct(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        item_id = fields.Int(required=False)
        
        brand_uid = fields.Int(required=False)
        
        item_code = fields.Str(required=False)
         
        
    
    class editProduct(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        item_id = fields.Int(required=False)
         
        
    
    class deleteProduct(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        item_id = fields.Int(required=False)
         
        
    
    class allSizes(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        item_id = fields.Int(required=False)
         
        
    
    class getProductValidation(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class getProductSize(BaseSchema):
        
        
        item_code = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
        
        item_id = fields.Int(required=False)
        
        brand_uid = fields.Int(required=False)
        
        uid = fields.Int(required=False)
         
        
    
    class getProductBulkUploadHistory(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        search = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
        
    
    class createBulkProductUploadJob(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class uploadBulkProducts(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        department = fields.Str(required=False)
        
        product_type = fields.Str(required=False)
         
        
    
    class createProductsInBulk(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        batch_id = fields.Str(required=False)
         
        
    
    class deleteProductBulkJob(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        batch_id = fields.Int(required=False)
         
        
    
    class getProductTags(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class getProductAssetsInBulk(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
        
    
    class createProductAssetsInBulk(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class deleteSize(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        item_id = fields.Int(required=False)
        
        size = fields.Str(required=False)
         
        
    
    class getInventoryBySize(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        item_id = fields.Int(required=False)
        
        size = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        q = fields.Str(required=False)
        
        sellable = fields.Boolean(required=False)
         
        
    
    class addInventory(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        item_id = fields.Int(required=False)
        
        size = fields.Str(required=False)
         
        
    
    class getInventoryBySizeIdentifier(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        item_id = fields.Int(required=False)
        
        size_identifier = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        q = fields.Str(required=False)
        
        location_ids = fields.List(fields.Int(required=False), required=False)
         
        
    
    class getInventories(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        item_id = fields.Str(required=False)
        
        size = fields.Str(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        q = fields.Str(required=False)
        
        sellable = fields.Boolean(required=False)
        
        store_ids = fields.List(fields.Int(required=False), required=False)
        
        size_identifier = fields.Str(required=False)
         
        
    
    class deleteInventory(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        size = fields.Str(required=False)
        
        item_id = fields.Int(required=False)
        
        location_id = fields.Float(required=False)
         
        
    
    class getInventoryBulkUploadHistory(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
         
        
    
    class createBulkInventoryJob(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class createBulkInventory(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        batch_id = fields.Str(required=False)
         
        
    
    class deleteBulkInventoryJob(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        batch_id = fields.Str(required=False)
         
        
    
    class getInventoryExport(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class createInventoryExportJob(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class listInventoryExport(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        status = fields.Str(required=False)
        
        from_date = fields.Str(required=False)
        
        to_date = fields.Str(required=False)
        
        q = fields.Str(required=False)
         
        
    
    class createInventoryExport(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class exportInventoryConfig(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        filter_type = fields.Str(required=False)
         
        
    
    class updateRealtimeInventory(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        item_id = fields.Int(required=False)
        
        seller_identifier = fields.Str(required=False)
         
        
    
    class deleteRealtimeInventory(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        item_id = fields.Int(required=False)
        
        seller_identifier = fields.Str(required=False)
         
        
    
    class updateInventories(BaseSchema):
        
        
        company_id = fields.Int(required=False)
         
        
    
    class getHsnCode(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class updateHsnCode(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class bulkHsnCode(BaseSchema):
        
        
        company_id = fields.Str(required=False)
         
        
    
    class getAllProductHsnCodes(BaseSchema):
        
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        q = fields.Str(required=False)
        
        type = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
         
        
    
    class getSingleProductHSNCode(BaseSchema):
        
        
        reporting_hsn = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
         
        
    
    class getOptimalLocations(BaseSchema):
        
        
        company_id = fields.Str(required=False)
         
        
    
    

