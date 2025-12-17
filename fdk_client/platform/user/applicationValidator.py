

"""User Platform Application Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf

from ..PlatformModel import BaseSchema



    
    
        
        
        
        
        
    
    
        
        
        
        
    
    
        
        
        
    
    
        
        
    
    
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
    
    
        
        
        
        
        
    
    
        
        
        
    
    
        
        
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
    
    
        
        
        
        
        
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
        
    
    
        
        
        
        
    
    
        
        
        
        
    
    
        
        
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
        
    
    
        
        
    
    
        
        
        
        
        
        
        
        
        
    
    
        
        
    
    
        
        
        
        
        
        
        
        
        
    
    
        
        
        
    
    
        
        

class UserValidator:
    
    
    class getCustomers(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        q = fields.Str(required=False)
        
        page_size = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
         
        
    
    class searchUsers(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        q = fields.Str(required=False)
        
        query = fields.List(fields.Str(required=False), required=False)
         
        
    
    class createUser(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        verified = fields.Boolean(required=False)
         
        
    
    class blockOrUnblockUsers(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class unDeleteUser(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getUserTimeline(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        user_id = fields.Str(required=False)
         
        
    
    class updateUser(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        user_id = fields.Str(required=False)
         
        
    
    class createUserSession(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class deleteSession(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
        
        session_id = fields.Str(required=False)
        
        reason = fields.Str(required=False)
         
        
    
    class getActiveSessions(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
        
    
    class deleteActiveSessions(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        id = fields.Str(required=False)
        
        reason = fields.Str(required=False)
         
        
    
    class archiveUser(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getPlatformConfig(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class updatePlatformConfig(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class createUserGroup(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getUserGroups(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        page_no = fields.Str(required=False)
        
        page_size = fields.Str(required=False)
        
        name = fields.Str(required=False)
        
        type = fields.Str(required=False)
        
        status = fields.Str(required=False)
        
        group_uid = fields.Int(required=False)
         
        
    
    class updateUserGroup(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        group_id = fields.Str(required=False)
         
        
    
    class getUserGroupById(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        group_id = fields.Str(required=False)
         
        
    
    class updateUserGroupPartially(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        group_id = fields.Str(required=False)
         
        
    
    class deleteUserGroup(BaseSchema):
        
        
        company_id = fields.Int(required=False)
        
        application_id = fields.Str(required=False)
        
        group_id = fields.Str(required=False)
         
        
    
    class createUserAttributeDefinition(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getUserAttributeDefinitions(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        excluding_ids = fields.Str(required=False)
        
        slug = fields.Str(required=False)
        
        type = fields.Str(required=False)
        
        customer_editable = fields.Boolean(required=False)
        
        encrypted = fields.Boolean(required=False)
        
        pinned = fields.Boolean(required=False)
        
        pin_order = fields.Int(required=False)
        
        is_locked = fields.Boolean(required=False)
        
        name = fields.Str(required=False)
        
        page_size = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
         
        
    
    class updateUserAttributeDefinition(BaseSchema):
        
        
        attribute_def_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        company_id = fields.Str(required=False)
         
        
    
    class deleteUserAttributeDefinitionById(BaseSchema):
        
        
        attribute_def_id = fields.Str(required=False)
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class getUserAttributeDefinitionById(BaseSchema):
        
        
        attribute_def_id = fields.Str(required=False)
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    class updateUserAttribute(BaseSchema):
        
        
        attribute_def_id = fields.Str(required=False)
        
        user_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        company_id = fields.Str(required=False)
         
        
    
    class getUserAttribute(BaseSchema):
        
        
        attribute_def_id = fields.Str(required=False)
        
        user_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        company_id = fields.Str(required=False)
         
        
    
    class deleteUserAttribute(BaseSchema):
        
        
        attribute_def_id = fields.Str(required=False)
        
        user_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        company_id = fields.Str(required=False)
         
        
    
    class getUserAttributesForUser(BaseSchema):
        
        
        user_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        company_id = fields.Str(required=False)
        
        page_size = fields.Int(required=False)
        
        page_no = fields.Int(required=False)
         
        
    
    class updateUserAttributes(BaseSchema):
        
        
        user_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
         
        
    
    class deleteUserAttributesInBulk(BaseSchema):
        
        
        user_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        company_id = fields.Int(required=False)
         
        
    
    class getUserAttributeById(BaseSchema):
        
        
        attribute_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        company_id = fields.Str(required=False)
         
        
    
    class bulkImportStoreFrontUsers(BaseSchema):
        
        
        application_id = fields.Str(required=False)
        
        company_id = fields.Str(required=False)
         
        
    
    class getBulkImportUsersList(BaseSchema):
        
        
        application_id = fields.Str(required=False)
        
        company_id = fields.Str(required=False)
        
        page_no = fields.Str(required=False)
        
        page_size = fields.Str(required=False)
        
        search = fields.Str(required=False)
        
        start_date = fields.Str(required=False)
        
        end_date = fields.Str(required=False)
        
        status = fields.Str(required=False)
        
        file_format = fields.Str(required=False)
         
        
    
    class createBulkExportUsers(BaseSchema):
        
        
        application_id = fields.Str(required=False)
        
        company_id = fields.Str(required=False)
         
        
    
    class getBulkExportUsersList(BaseSchema):
        
        
        application_id = fields.Str(required=False)
        
        company_id = fields.Str(required=False)
        
        page_no = fields.Str(required=False)
        
        page_size = fields.Str(required=False)
        
        file_format = fields.Str(required=False)
        
        search = fields.Str(required=False)
        
        start_date = fields.Str(required=False)
        
        end_date = fields.Str(required=False)
        
        status = fields.Str(required=False)
         
        
    
    class getUsersJobByJobId(BaseSchema):
        
        
        application_id = fields.Str(required=False)
        
        company_id = fields.Str(required=False)
        
        job_id = fields.Str(required=False)
         
        
    
    class filterUsersByAttributes(BaseSchema):
        
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
        
    
    

