



##### [Back to Platform docs](./README.md)

## Communication Methods
Manages email, sms, push notifications sent to users

Default
* [getAppProviders](#getappproviders)
* [updateAppProviders](#updateappproviders)
* [getGlobalProviders](#getglobalproviders)
* [getEmailProviders](#getemailproviders)
* [createEmailProvider](#createemailprovider)
* [getEmailProviderById](#getemailproviderbyid)
* [updateEmailProviderById](#updateemailproviderbyid)
* [deleteEmailProviderById](#deleteemailproviderbyid)
* [getSmsProviders](#getsmsproviders)
* [createSmsProvider](#createsmsprovider)
* [getDefaultSmsProviders](#getdefaultsmsproviders)
* [getSmsProviderById](#getsmsproviderbyid)
* [updateSmsProviderById](#updatesmsproviderbyid)
* [deleteSmsProviderById](#deletesmsproviderbyid)
* [getCampaigns](#getcampaigns)
* [createCampaign](#createcampaign)
* [getCampaignById](#getcampaignbyid)
* [updateCampaignById](#updatecampaignbyid)
* [getStatsOfCampaignById](#getstatsofcampaignbyid)
* [getBigQueryRowCountById](#getbigqueryrowcountbyid)
* [createBigQueryRowCount](#createbigqueryrowcount)
* [getBigQueryHeadersById](#getbigqueryheadersbyid)
* [createBigQueryNCount](#createbigqueryncount)
* [createBigQueryHeaders](#createbigqueryheaders)
* [getSystemAudiences](#getsystemaudiences)
* [getAudiences](#getaudiences)
* [createAudience](#createaudience)
* [getAudienceById](#getaudiencebyid)
* [updateAudienceById](#updateaudiencebyid)
* [deleteAudienceById](#deleteaudiencebyid)
* [getDummyDatasources](#getdummydatasources)
* [getDummyDatasourcesMeta](#getdummydatasourcesmeta)
* [getNSampleRecordsFromCsvByGet](#getnsamplerecordsfromcsvbyget)
* [getNSampleRecordsFromCsv](#getnsamplerecordsfromcsv)
* [getEmailTemplates](#getemailtemplates)
* [createEmailTemplate](#createemailtemplate)
* [getSystemEmailTemplates](#getsystememailtemplates)
* [getEmailTemplateById](#getemailtemplatebyid)
* [updateEmailTemplateById](#updateemailtemplatebyid)
* [deleteEmailTemplateById](#deleteemailtemplatebyid)
* [getSubscribedEmailTemplates](#getsubscribedemailtemplates)
* [getSmsTemplates](#getsmstemplates)
* [createSmsTemplate](#createsmstemplate)
* [getSystemSmsTemplates](#getsystemsmstemplates)
* [getSmsTemplateById](#getsmstemplatebyid)
* [updateSmsTemplateById](#updatesmstemplatebyid)
* [deleteSmsTemplateById](#deletesmstemplatebyid)
* [getSubscribedSmsTemplates](#getsubscribedsmstemplates)
* [sendCommunicationSynchronously](#sendcommunicationsynchronously)
* [sendCommunicationAsynchronously](#sendcommunicationasynchronously)
* [getEventSubscriptions](#geteventsubscriptions)
* [createEventSubscriptions](#createeventsubscriptions)
* [getEventSubscriptionsById](#geteventsubscriptionsbyid)
* [editEventSubscriptions](#editeventsubscriptions)
* [deleteEventSubscriptionsById](#deleteeventsubscriptionsbyid)
* [createEventSubscriptionsByBulk](#createeventsubscriptionsbybulk)
* [getGlobalVariables](#getglobalvariables)
* [postGlobalVariables](#postglobalvariables)
* [getJobs](#getjobs)
* [createJobs](#createjobs)
* [triggerCampaignJob](#triggercampaignjob)
* [getJobLogs](#getjoblogs)
* [getCommunicationLogs](#getcommunicationlogs)
* [getSystemNotifications](#getsystemnotifications)
* [sendOtp](#sendotp)
* [verfiyOtp](#verfiyotp)
* [getOtpConfiguration](#getotpconfiguration)
* [updateOtpConfiguration](#updateotpconfiguration)




## Methods with example and description



### getAppProviders
Get app providers




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.getAppProviders()
    # use result
except Exception as e:
    print(e)
```






Using this API will return a list of application providers.

*Returned Response:*




[AppProvider](#AppProvider)

Success




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {
    "email": {
      "transaction": {
        "provider": "5f0408cec0c2a2175a1c16f6"
      },
      "promotional": {
        "provider": "6385ed1ebf50a6c9a61d58d5"
      },
      "otp": {
        "provider": "5f0408cec0c2a2175a1c16f6"
      }
    },
    "sms": {
      "transaction": {
        "provider": "63db8c68975237fff4f2133e"
      },
      "promotional": {
        "provider": "63db8c68975237fff4f2133e"
      },
      "otp": {
        "provider": "63db8c68975237fff4f21346"
      }
    },
    "voice": {
      "transaction": {
        "provider": "643cf4098bb1fc2c1d67f089"
      },
      "otp": {
        "provider": "643cf4098bb1fc2c1d67f089"
      }
    },
    "_id": "63e20ce7648381edb6de45ff",
    "application": "637b6355dc65337da9b5c951",
    "created_at": "2023-02-07T08:33:43.169Z",
    "updated_at": "2023-05-30T07:16:39.161Z",
    "__v": 0
  }
}
```
</details>

</details>









---


### updateAppProviders
update app providers




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.updateAppProviders(body=body)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- |
| body | [AppProviderReq](#AppProviderReq) | yes | Request body |


Using this API will update the application providers.

*Returned Response:*




[AppProvider](#AppProvider)

Success




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {
    "email": {
      "transaction": {
        "provider": "5f0408cec0c2a2175a1c16f6"
      },
      "promotional": {
        "provider": "6385ed1ebf50a6c9a61d58d5"
      },
      "otp": {
        "provider": "5f0408cec0c2a2175a1c16f6"
      }
    },
    "sms": {
      "transaction": {
        "provider": "63db8c68975237fff4f2133e"
      },
      "promotional": {
        "provider": "63db8c68975237fff4f2133e"
      },
      "otp": {
        "provider": "63db8c68975237fff4f21346"
      }
    },
    "voice": {
      "transaction": {
        "provider": "643cf4098bb1fc2c1d67f089"
      },
      "otp": {
        "provider": "643cf4098bb1fc2c1d67f089"
      }
    },
    "_id": "63e20ce7648381edb6de45ff",
    "application": "637b6355dc65337da9b5c951",
    "created_at": "2023-02-07T08:33:43.169Z",
    "updated_at": "2023-05-30T07:16:39.161Z",
    "__v": 0
  }
}
```
</details>

</details>









---


### getGlobalProviders
Get global providers




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.getGlobalProviders()
    # use result
except Exception as e:
    print(e)
```






Using this API, will retrieve a list of global providers.

*Returned Response:*




[GlobalProviders](#GlobalProviders)

Success




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {
    "email": [
      {
        "_id": "5f0408cec0c2a2175a1c16f6",
        "name": "Fynd-falconide"
      }
    ],
    "sms": [
      {
        "_id": "63db8c68975237fff4f2133e",
        "name": "Fynd Transactional - timesinternet"
      },
      {
        "_id": "63db8c68975237fff4f21346",
        "name": "Fynd OTP - timesinternet"
      }
    ],
    "voice": [
      {
        "_id": "643cf4098bb1fc2c1d67f089",
        "name": "Fynd-exotel"
      }
    ]
  }
}
```
</details>

</details>









---


### getEmailProviders
Get email providers




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.getEmailProviders(pageNo=pageNo, pageSize=pageSize, sort=sort, query=query)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| pageNo | Int? | no | Current page no |   
| pageSize | Int? | no | Current request items count |   
| sort | HashMap<String,Any>? | no | To sort based on created_at |   
| query | HashMap<String,Any>? | no | To search based on plain text |  



Get email providers

*Returned Response:*




[EmailProviders](#EmailProviders)

Success




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {
    "items": [
      {
        "type": "application",
        "provider": "falconide",
        "from_address": [
          {
            "is_default": true,
            "name": "abc",
            "email": "abc@test.com"
          }
        ],
        "_id": "5fd9fd44c474a7e3d5d376d6",
        "name": "test falconide",
        "description": "test",
        "api_key": "testtttt",
        "application": "000000000000000000000004",
        "created_at": "2020-12-16T12:27:48.051Z",
        "updated_at": "2020-12-16T12:27:48.051Z",
        "slug": "test-falconide-application-falconide-ZTD-D7wbB",
        "__v": 0
      }
    ],
    "page": {
      "type": "number",
      "current": 1,
      "size": 10,
      "item_total": 1,
      "has_next": false
    }
  }
}
```
</details>

</details>









---


### createEmailProvider
Create email provider




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.createEmailProvider(body=body)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- |
| body | [EmailProviderReq](#EmailProviderReq) | yes | Request body |


Create email provider

*Returned Response:*




[EmailProvider](#EmailProvider)

Success




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {
    "type": "application",
    "provider": "falconide",
    "from_address": [
      {
        "is_default": true,
        "name": "abc",
        "email": "abc@test.com"
      }
    ],
    "_id": "5fd9fd44c474a7e3d5d376d6",
    "name": "test falconide",
    "description": "test",
    "api_key": "testtttt",
    "application": "000000000000000000000004",
    "created_at": "2020-12-16T12:27:48.051Z",
    "updated_at": "2020-12-16T12:27:48.051Z",
    "slug": "test-falconide-application-falconide-ZTD-D7wbB",
    "__v": 0
  }
}
```
</details>

</details>









---


### getEmailProviderById
Get email provider by id




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.getEmailProviderById(id=id)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| id | String | yes | Email provider id |  



Get email provider by id

*Returned Response:*




[EmailProvider](#EmailProvider)

Success




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {
    "type": "application",
    "provider": "falconide",
    "from_address": [
      {
        "is_default": true,
        "name": "abc",
        "email": "abc@test.com"
      }
    ],
    "_id": "5fd9fd44c474a7e3d5d376d6",
    "name": "test falconide",
    "description": "test",
    "api_key": "testtttt",
    "application": "000000000000000000000004",
    "created_at": "2020-12-16T12:27:48.051Z",
    "updated_at": "2020-12-16T12:27:48.051Z",
    "slug": "test-falconide-application-falconide-ZTD-D7wbB",
    "__v": 0
  }
}
```
</details>

</details>









---


### updateEmailProviderById
Update email provider by id




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.updateEmailProviderById(id=id, body=body)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| id | String | yes | Email provider id |  
| body | [EmailProviderReq](#EmailProviderReq) | yes | Request body |


Update email provider by id

*Returned Response:*




[EmailProvider](#EmailProvider)

Success




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {
    "type": "application",
    "provider": "falconide",
    "from_address": [
      {
        "is_default": true,
        "name": "abc",
        "email": "abc@test.com"
      }
    ],
    "_id": "5fd9fd44c474a7e3d5d376d6",
    "name": "test falconide",
    "description": "test",
    "api_key": "testtttt",
    "application": "000000000000000000000004",
    "created_at": "2020-12-16T12:27:48.051Z",
    "updated_at": "2020-12-16T12:27:48.051Z",
    "slug": "test-falconide-application-falconide-ZTD-D7wbB",
    "__v": 0
  }
}
```
</details>

</details>









---


### deleteEmailProviderById
Delete email provider by id




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.deleteEmailProviderById(id=id)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| id | String | yes | Email provider id |  



Delete email provider by id

*Returned Response:*




[GenericDelete](#GenericDelete)

Refer `GenericDelete` schema for more details.




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {
    "message": "Deletion Successfull",
    "acknowledged": true,
    "affected": 1,
    "operation": "TEMP-ST-DEL:ID"
  }
}
```
</details>

</details>









---


### getSmsProviders
Get sms providers




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.getSmsProviders(pageNo=pageNo, pageSize=pageSize, sort=sort, query=query)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| pageNo | Int? | no | Current page no |   
| pageSize | Int? | no | Current request items count |   
| sort | HashMap<String,Any>? | no | To sort based on created_at |   
| query | HashMap<String,Any>? | no | To search based on plain text |  



Get sms providers

*Returned Response:*




[HashMap<String,Any>](#HashMap<String,Any>)

Success




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {
    "items": [
      {
        "rpt": 1,
        "type": "application",
        "provider": "telspiel",
        "_id": "5fd9fd07c474a7710dd376d5",
        "name": "test telspiel",
        "description": "test",
        "sender": "test",
        "username": "test",
        "authkey": "test",
        "application": "000000000000000000000004",
        "created_at": "2020-12-16T12:26:47.794Z",
        "updated_at": "2020-12-16T12:26:47.794Z",
        "slug": "test-telspiel-application-telspiel-p9UY1r7nG",
        "__v": 0
      }
    ],
    "page": {
      "type": "number",
      "current": 1,
      "size": 1,
      "item_total": 1,
      "has_next": false
    }
  }
}
```
</details>

</details>









---


### createSmsProvider
Create sms provider




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.createSmsProvider(body=body)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- |
| body | [SmsProviderReq](#SmsProviderReq) | yes | Request body |


Create sms provider

*Returned Response:*




[HashMap<String,Any>](#HashMap<String,Any>)

Success




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {
    "rpt": 1,
    "type": "application",
    "provider": "telspiel",
    "_id": "5fd9fd07c474a7710dd376d5",
    "name": "test telspiel",
    "description": "test",
    "sender": "test",
    "username": "test",
    "authkey": "test",
    "application": "000000000000000000000004",
    "created_at": "2020-12-16T12:26:47.794Z",
    "updated_at": "2020-12-16T12:26:47.794Z",
    "slug": "test-telspiel-application-telspiel-p9UY1r7nG",
    "__v": 0
  }
}
```
</details>

</details>









---


### getDefaultSmsProviders
Get default sms providers




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.getDefaultSmsProviders()
    # use result
except Exception as e:
    print(e)
```






Get default sms providers

*Returned Response:*




[ArrayList<DefaultSmsProviders>](#ArrayList<DefaultSmsProviders>)

Successful retrieval of the default SMS providers list




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": [
    {
      "_id": "63db8c68975237fff4f2133e",
      "name": "Fynd timesinternet",
      "is_default": true
    }
  ]
}
```
</details>

</details>









---


### getSmsProviderById
Get sms provider by id




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.getSmsProviderById(id=id)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| id | String | yes | Sms provider id |  



Get sms provider by id

*Returned Response:*




[HashMap<String,Any>](#HashMap<String,Any>)

Success




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {
    "rpt": 1,
    "type": "application",
    "provider": "telspiel",
    "_id": "5fd9fd07c474a7710dd376d5",
    "name": "test telspiel",
    "description": "test",
    "sender": "test",
    "username": "test",
    "authkey": "test",
    "application": "000000000000000000000004",
    "created_at": "2020-12-16T12:26:47.794Z",
    "updated_at": "2020-12-16T12:26:47.794Z",
    "slug": "test-telspiel-application-telspiel-p9UY1r7nG",
    "__v": 0
  }
}
```
</details>

</details>









---


### updateSmsProviderById
Update sms provider by id




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.updateSmsProviderById(id=id, body=body)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| id | String | yes | Sms provider id |  
| body | [SmsProviderReq](#SmsProviderReq) | yes | Request body |


Update sms provider by id

*Returned Response:*




[HashMap<String,Any>](#HashMap<String,Any>)

Success




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {
    "rpt": 1,
    "type": "application",
    "provider": "telspiel",
    "_id": "5fd9fd07c474a7710dd376d5",
    "name": "test telspiel",
    "description": "test",
    "sender": "test",
    "username": "test",
    "authkey": "test",
    "application": "000000000000000000000004",
    "created_at": "2020-12-16T12:26:47.794Z",
    "updated_at": "2020-12-16T12:26:47.794Z",
    "slug": "test-telspiel-application-telspiel-p9UY1r7nG",
    "__v": 0
  }
}
```
</details>

</details>









---


### deleteSmsProviderById
Delete sms provider by id




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.deleteSmsProviderById(id=id)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| id | String | yes | Sms provider id |  



Delete sms provider by id

*Returned Response:*




[GenericDelete](#GenericDelete)

Refer `GenericDelete` schema for more details.




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {
    "message": "Deletion Successfull",
    "acknowledged": true,
    "affected": 1,
    "operation": "TEMP-ST-DEL:ID"
  }
}
```
</details>

</details>









---


### getCampaigns
Get campaigns




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.getCampaigns(query=query, pageNo=pageNo, pageSize=pageSize, sort=sort)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| query | HashMap<String,Any>? | no | To search based on plain text |   
| pageNo | Int? | no | Current page no |   
| pageSize | Int? | no | Current request items count |   
| sort | HashMap<String,Any>? | no | To sort based on created_at |  



Get campaigns

*Returned Response:*




[Campaigns](#Campaigns)

Success




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {
    "items": [
      {
        "recipient_headers": {
          "email": "email"
        },
        "email": {
          "template": {
            "key": "_id",
            "value": "5fb6757a09fd90ca91917a60"
          },
          "provider": {
            "_id": "5e560652b5eb4b1f13b4d601",
            "from_name": "Fynd",
            "from_email": "hey@gofynd.com"
          }
        },
        "description": "",
        "tags": [],
        "is_active": true,
        "_id": "6009a1ea1f6a61d88e80a867",
        "datasource": "6009a1be1f6a61a13180a866",
        "type": "email",
        "name": "testing bq email",
        "application": "000000000000000000000004",
        "created_at": "2021-01-21T15:46:50.357Z",
        "updated_at": "2021-01-21T15:46:50.357Z",
        "slug": "testing-bq-email-vPyAd1YB1",
        "__v": 0
      },
      {
        "recipient_headers": {
          "sms": "phone_number"
        },
        "sms": {
          "template": {
            "key": "_id",
            "value": "5fb675d009fd903196917a61"
          },
          "provider": {
            "_id": "5e560652b5eb4b06f3b4d5ff"
          }
        },
        "description": "",
        "tags": [],
        "is_active": true,
        "_id": "600981561f6a612c6080a85e",
        "datasource": "600981461f6a614b2c80a85d",
        "type": "sms",
        "name": "test",
        "application": "000000000000000000000004",
        "created_at": "2021-01-21T13:27:50.848Z",
        "updated_at": "2021-01-21T13:27:50.848Z",
        "slug": "test-ipLO3c8Jh",
        "__v": 0
      }
    ],
    "page": {
      "type": "number",
      "current": 1,
      "size": 2,
      "item_total": 2,
      "has_next": false
    }
  }
}
```
</details>

</details>









---


### createCampaign
Create campaign




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.createCampaign(body=body)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- |
| body | [CampaignReq](#CampaignReq) | yes | Request body |


Create campaign

*Returned Response:*




[Campaign](#Campaign)

Success




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {
    "recipient_headers": {
      "email": "email"
    },
    "email": {
      "template": {
        "key": "_id",
        "value": "5fb6757a09fd90ca91917a60"
      },
      "provider": {
        "_id": "5e560652b5eb4b1f13b4d601",
        "from_name": "Fynd",
        "from_email": "hey@gofynd.com"
      }
    },
    "description": "",
    "tags": [],
    "is_active": true,
    "_id": "6009a1ea1f6a61d88e80a867",
    "datasource": "6009a1be1f6a61a13180a866",
    "type": "email",
    "name": "testing bq email",
    "application": "000000000000000000000004",
    "created_at": "2021-01-21T15:46:50.357Z",
    "updated_at": "2021-01-21T15:46:50.357Z",
    "slug": "testing-bq-email-vPyAd1YB1",
    "__v": 0
  }
}
```
</details>

</details>









---


### getCampaignById
Get campaign by id




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.getCampaignById(id=id)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| id | String | yes | Campaign id |  



Get campaign by id

*Returned Response:*




[Campaign](#Campaign)

Success




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {
    "recipient_headers": {
      "email": "email"
    },
    "email": {
      "template": {
        "key": "_id",
        "value": "5fb6757a09fd90ca91917a60"
      },
      "provider": {
        "_id": "5e560652b5eb4b1f13b4d601",
        "from_name": "Fynd",
        "from_email": "hey@gofynd.com"
      }
    },
    "description": "",
    "tags": [],
    "is_active": true,
    "_id": "6009a1ea1f6a61d88e80a867",
    "datasource": "6009a1be1f6a61a13180a866",
    "type": "email",
    "name": "testing bq email",
    "application": "000000000000000000000004",
    "created_at": "2021-01-21T15:46:50.357Z",
    "updated_at": "2021-01-21T15:46:50.357Z",
    "slug": "testing-bq-email-vPyAd1YB1",
    "__v": 0
  }
}
```
</details>

</details>









---


### updateCampaignById
Update campaign by id




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.updateCampaignById(id=id, body=body)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| id | String | yes | Campaign id |  
| body | [CampaignReq](#CampaignReq) | yes | Request body |


Update campaign by id

*Returned Response:*




[Campaign](#Campaign)

Success




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {
    "recipient_headers": {
      "email": "email"
    },
    "email": {
      "template": {
        "key": "_id",
        "value": "5fb6757a09fd90ca91917a60"
      },
      "provider": {
        "_id": "5e560652b5eb4b1f13b4d601",
        "from_name": "Fynd",
        "from_email": "hey@gofynd.com"
      }
    },
    "description": "",
    "tags": [],
    "is_active": true,
    "_id": "6009a1ea1f6a61d88e80a867",
    "datasource": "6009a1be1f6a61a13180a866",
    "type": "email",
    "name": "testing bq email",
    "application": "000000000000000000000004",
    "created_at": "2021-01-21T15:46:50.357Z",
    "updated_at": "2021-01-21T15:46:50.357Z",
    "slug": "testing-bq-email-vPyAd1YB1",
    "__v": 0
  }
}
```
</details>

</details>









---


### getStatsOfCampaignById
Get stats of campaign by id




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.getStatsOfCampaignById(id=id)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| id | String | yes | Campaign id |  



Get stats of campaign by id

*Returned Response:*




[GetStats](#GetStats)

Success




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {
    "items": [
      {
        "_id": "6009a1ea1f6a61d88e80a867",
        "imported": {
          "count": 2
        },
        "processed": {
          "email": {
            "success": 2,
            "failed": 0,
            "suppressed": 0
          },
          "sms": {
            "success": 0,
            "failed": 0,
            "suppressed": 0
          }
        }
      }
    ]
  }
}
```
</details>

</details>









---


### getBigQueryRowCountById
Get big query row count by id




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.getBigQueryRowCountById(id=id)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| id | String | yes | Audience id |  



Get big query row count by id

*Returned Response:*




[HashMap<String,Any>](#HashMap<String,Any>)

Success




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {}
}
```
</details>

</details>









---


### createBigQueryRowCount
Create big query row count




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.createBigQueryRowCount()
    # use result
except Exception as e:
    print(e)
```






Create big query row count

*Returned Response:*




[HashMap<String,Any>](#HashMap<String,Any>)

Success




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {}
}
```
</details>

</details>









---


### getBigQueryHeadersById
Get big query headers by id




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.getBigQueryHeadersById(id=id)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| id | String | yes | Audience id |  



Get big query headers by id

*Returned Response:*




[HashMap<String,Any>](#HashMap<String,Any>)

Success




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {}
}
```
</details>

</details>









---


### createBigQueryNCount
Create big query n count




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.createBigQueryNCount()
    # use result
except Exception as e:
    print(e)
```






Create big query n count

*Returned Response:*




[HashMap<String,Any>](#HashMap<String,Any>)

Success




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {}
}
```
</details>

</details>









---


### createBigQueryHeaders
Create big query headers




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.createBigQueryHeaders()
    # use result
except Exception as e:
    print(e)
```






Create big query headers

*Returned Response:*




[HashMap<String,Any>](#HashMap<String,Any>)

Success




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {}
}
```
</details>

</details>









---


### getSystemAudiences
Get system audiences




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.getSystemAudiences()
    # use result
except Exception as e:
    print(e)
```






Get system audiences

*Returned Response:*




[HashMap<String,Any>](#HashMap<String,Any>)

Success




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {}
}
```
</details>

</details>









---


### getAudiences
Get audiences




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.getAudiences(pageNo=pageNo, pageSize=pageSize, sort=sort, query=query)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| pageNo | Int? | no | Current page no |   
| pageSize | Int? | no | Current request items count |   
| sort | HashMap<String,Any>? | no | To sort based on created_at |   
| query | HashMap<String,Any>? | no | To search based on plain text |  



Audience is used to import CSV files containing emails, phone numbers, and other variables in order to populate email/SMS templates for bulk delivery via a Campaign. Use this API to get audiences.

*Returned Response:*




[Audiences](#Audiences)

Success




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {
    "items": [
      {
        "_id": "64ad30a15efbc5f85fb549d8",
        "application": "64802b8bd4dc759bcc1fef86",
        "name": "dummy ds",
        "description": "desc",
        "records_count": 1,
        "type": "raw_csv",
        "tags": [
          "tag1",
          "tag2"
        ],
        "headers": [
          "phone",
          "mail"
        ],
        "file_url": "https://cdn.pixelbin.io/v2/falling-surf-7c8bb8/fyndnp/wrkr/x5/application/64802b8bd4dc759bcc1fef86/datasources/ODKRR6aBQ-jsonviewer.csv",
        "is_active": true,
        "created_at": "2023-07-11T10:36:17.340Z",
        "updated_at": "2023-07-11T10:36:17.340Z",
        "slug": "dummy-1-5JrNGM8LA",
        "__v": 0
      }
    ],
    "page": {
      "type": "number",
      "current": 1,
      "size": 1,
      "item_total": 1,
      "has_next": false
    }
  }
}
```
</details>

</details>









---


### createAudience
Create audience




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.createAudience(body=body)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- |
| body | [AudienceReq](#AudienceReq) | yes | Request body |


Audience is used to import CSV files containing emails, phone numbers, and other variables in order to populate email/SMS templates for bulk delivery via a Campaign. Use this API to create audience.

*Returned Response:*




[Audience](#Audience)

Refer `Audience` schema for more details.




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {
    "_id": "64ad30a15efbc5f85fb549d8",
    "application": "64802b8bd4dc759bcc1fef86",
    "name": "dummy ds",
    "description": "desc",
    "records_count": 1,
    "type": "raw_csv",
    "tags": [
      "tag1",
      "tag2"
    ],
    "headers": [
      "phone",
      "mail"
    ],
    "file_url": "https://cdn.pixelbin.io/v2/falling-surf-7c8bb8/fyndnp/wrkr/x5/application/64802b8bd4dc759bcc1fef86/datasources/ODKRR6aBQ-jsonviewer.csv",
    "is_active": true,
    "created_at": "2023-07-11T10:36:17.340Z",
    "updated_at": "2023-07-11T10:36:17.340Z",
    "slug": "dummy-1-5JrNGM8LA",
    "__v": 0
  }
}
```
</details>

</details>









---


### getAudienceById
Get audience by id




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.getAudienceById(id=id)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| id | String | yes | Audience id |  



Audience is used to import CSV files containing emails, phone numbers, and other variables in order to populate email/SMS templates for bulk delivery via a Campaign. Use this API to get audiences by Id.

*Returned Response:*




[Audience](#Audience)

Refer `Audience` schema for more details.




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {
    "_id": "64ad30a15efbc5f85fb549d8",
    "application": "64802b8bd4dc759bcc1fef86",
    "name": "dummy ds",
    "description": "desc",
    "records_count": 1,
    "type": "raw_csv",
    "tags": [
      "tag1",
      "tag2"
    ],
    "headers": [
      "phone",
      "mail"
    ],
    "file_url": "https://cdn.pixelbin.io/v2/falling-surf-7c8bb8/fyndnp/wrkr/x5/application/64802b8bd4dc759bcc1fef86/datasources/ODKRR6aBQ-jsonviewer.csv",
    "is_active": true,
    "created_at": "2023-07-11T10:36:17.340Z",
    "updated_at": "2023-07-11T10:36:17.340Z",
    "slug": "dummy-1-5JrNGM8LA",
    "__v": 0
  }
}
```
</details>

</details>









---


### updateAudienceById
Update audience by id




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.updateAudienceById(id=id, body=body)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| id | String | yes | Audience id |  
| body | [AudienceReq](#AudienceReq) | yes | Request body |


Audience is used to import CSV files containing emails, phone numbers, and other variables in order to populate email/SMS templates for bulk delivery via a Campaign. Use this API to update audience by id.

*Returned Response:*




[Audience](#Audience)

Refer `Audience` schema for more details.




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {
    "_id": "64ad30a15efbc5f85fb549d8",
    "application": "64802b8bd4dc759bcc1fef86",
    "name": "dummy ds",
    "description": "desc",
    "records_count": 1,
    "type": "raw_csv",
    "tags": [
      "tag1",
      "tag2"
    ],
    "headers": [
      "phone",
      "mail"
    ],
    "file_url": "https://cdn.pixelbin.io/v2/falling-surf-7c8bb8/fyndnp/wrkr/x5/application/64802b8bd4dc759bcc1fef86/datasources/ODKRR6aBQ-jsonviewer.csv",
    "is_active": true,
    "created_at": "2023-07-11T10:36:17.340Z",
    "updated_at": "2023-07-11T10:36:17.340Z",
    "slug": "dummy-1-5JrNGM8LA",
    "__v": 0
  }
}
```
</details>

</details>









---


### deleteAudienceById
Delete audience by id




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.deleteAudienceById(id=id, body=body)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| id | String | yes | Audience id |  
| body | [AudienceReq](#AudienceReq) | yes | Request body |


Audience is used to import CSV files containing emails, phone numbers, and other variables in order to populate email/SMS templates for bulk delivery via a Campaign. Use this API to delete audience by id.

*Returned Response:*




[Audience](#Audience)

Refer `Audience` schema for more details.




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {
    "_id": "64ad30a15efbc5f85fb549d8",
    "application": "64802b8bd4dc759bcc1fef86",
    "name": "dummy ds",
    "description": "desc",
    "records_count": 1,
    "type": "raw_csv",
    "tags": [
      "tag1",
      "tag2"
    ],
    "headers": [
      "phone",
      "mail"
    ],
    "file_url": "https://cdn.pixelbin.io/v2/falling-surf-7c8bb8/fyndnp/wrkr/x5/application/64802b8bd4dc759bcc1fef86/datasources/ODKRR6aBQ-jsonviewer.csv",
    "is_active": true,
    "created_at": "2023-07-11T10:36:17.340Z",
    "updated_at": "2023-07-11T10:36:17.340Z",
    "slug": "dummy-1-5JrNGM8LA",
    "__v": 0
  }
}
```
</details>

</details>









---


### getDummyDatasources
Get dummy data sources




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.getDummyDatasources()
    # use result
except Exception as e:
    print(e)
```






Audience is used to import CSV files containing emails, phone numbers, and other variables in order to populate email/SMS templates for bulk delivery via a Campaign. Use this API to get dummy data sources.

*Returned Response:*




[ArrayList<DummyDatasources>](#ArrayList<DummyDatasources>)

Refer `DummyDatasources` schema for more details.




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": [
    {
      "id": 1,
      "name": "Data source 1"
    },
    {
      "id": 2,
      "name": "Data source 2"
    }
  ]
}
```
</details>

</details>









---


### getDummyDatasourcesMeta
Get dummy data sources meta




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.getDummyDatasourcesMeta(id=id)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| id | Int | yes | Dummy datasources meta ID |  



Audience is used to import CSV files containing emails, phone numbers, and other variables in order to populate email/SMS templates for bulk delivery via a Campaign. Use this API to get dummy data sources meta.

*Returned Response:*




[DummyDatasourcesMeta](#DummyDatasourcesMeta)

Refer `DummyDatasourcesMeta` schema for more details.




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {
    "id": 2,
    "data": {
      "b": 2
    }
  }
}
```
</details>

</details>









---


### getNSampleRecordsFromCsvByGet
Get n sample records from csv




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.getNSampleRecordsFromCsvByGet()
    # use result
except Exception as e:
    print(e)
```






Audience is used to import CSV files containing emails, phone numbers, and other variables in order to populate email/SMS templates for bulk delivery via a Campaign. Use this API to get n sample records from csv.

*Returned Response:*




[GetNRecordsCsvRes](#GetNRecordsCsvRes)

Refer `GetNRecordsCsvRes` schema for more details.




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {
    "items": [
      {
        "phone_number": "1234567890",
        "email": "abcxyz@gofynd.com",
        "firstname": "Abc",
        "lastname": "Xyz",
        "orderid": "1"
      }
    ]
  }
}
```
</details>

</details>









---


### getNSampleRecordsFromCsv
Get n sample records from csv




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.getNSampleRecordsFromCsv(body=body)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- |
| body | [GetNRecordsCsvReq](#GetNRecordsCsvReq) | yes | Request body |


Audience is used to import CSV files containing emails, phone numbers, and other variables in order to populate email/SMS templates for bulk delivery via a Campaign. Use this API to get n sample records from csv

*Returned Response:*




[GetNRecordsCsvRes](#GetNRecordsCsvRes)

Refer `GetNRecordsCsvRes` schema for more details.




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {
    "items": [
      {
        "phone_number": "1234567890",
        "email": "abcxyz@gofynd.com",
        "firstname": "Abc",
        "lastname": "Xyz",
        "orderid": "1"
      }
    ]
  }
}
```
</details>

</details>









---


### getEmailTemplates
Get email templates




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.getEmailTemplates(pageNo=pageNo, pageSize=pageSize, sort=sort, query=query)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| pageNo | Int? | no | Current page no |   
| pageSize | Int? | no | Current request items count |   
| sort | HashMap<String,Any>? | no | To sort based on created_at |   
| query | HashMap<String,Any>? | no | To search based on plain text |  



Email templates are predefined formats linked to various events for delivering messages to users. Use this API to get all email templates.

*Returned Response:*




[EmailTemplates](#EmailTemplates)

Refer `EmailTemplates` schema for more details.




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {
    "items": [
      {
        "application": "637b6355dc65337da9b5c951",
        "is_system": false,
        "is_internal": false,
        "name": "title",
        "description": "desc",
        "editor_type": "bee",
        "editor_meta": "",
        "static_to": [],
        "static_cc": [
          "abc@abc.com"
        ],
        "static_bcc": [
          "abc@abc.com"
        ],
        "reply_to": "abc@abc.com",
        "tags": [
          "tag"
        ],
        "subject": {
          "template_type": "nunjucks",
          "template": "subject"
        },
        "html": {
          "template_type": "nunjucks",
          "template": ""
        },
        "url_shorten": {
          "enabled": false
        },
        "priority": "low",
        "template_variables": {
          "hello": "world"
        },
        "published": true,
        "category": "website",
        "_id": "649fca8fe89b403f490f9c55",
        "headers": [],
        "attachments": [],
        "created_at": "2023-07-01T06:41:19.360Z",
        "updated_at": "2023-07-01T06:41:19.360Z",
        "slug": "title-W9qbdl8AJ",
        "__v": 0,
        "from_name": "Fynd",
        "text": {
          "template_type": "nunjucks",
          "template": "subject"
        }
      }
    ],
    "page": {
      "type": "number",
      "current": 1,
      "size": 1,
      "item_total": 66,
      "has_next": true
    }
  }
}
```
</details>

</details>









---


### createEmailTemplate
Create email template




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.createEmailTemplate(body=body)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- |
| body | [EmailTemplateReq](#EmailTemplateReq) | yes | Request body |


Email templates are predefined formats linked to various events for delivering messages to users. Use this API to create an email template.

*Returned Response:*




[EmailTemplate](#EmailTemplate)

Refer `EmailTemplate` schema for more details.




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {
    "application": "637b6355dc65337da9b5c951",
    "is_system": false,
    "is_internal": false,
    "name": "title",
    "description": "desc",
    "editor_type": "bee",
    "editor_meta": "",
    "static_to": [],
    "static_cc": [
      "abc@abc.com"
    ],
    "static_bcc": [
      "abc@abc.com"
    ],
    "reply_to": "abc@abc.com",
    "tags": [
      "tag"
    ],
    "subject": {
      "template_type": "nunjucks",
      "template": "subject"
    },
    "html": {
      "template_type": "nunjucks",
      "template": ""
    },
    "url_shorten": {
      "enabled": false
    },
    "priority": "low",
    "template_variables": {
      "hello": "world"
    },
    "published": true,
    "category": "website",
    "_id": "649fca8fe89b403f490f9c55",
    "headers": [],
    "attachments": [],
    "created_at": "2023-07-01T06:41:19.360Z",
    "updated_at": "2023-07-01T06:41:19.360Z",
    "slug": "title-W9qbdl8AJ",
    "__v": 0,
    "from_name": "Fynd",
    "text": {
      "template_type": "nunjucks",
      "template": "subject"
    }
  }
}
```
</details>

</details>









---


### getSystemEmailTemplates
Get system email templates




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.getSystemEmailTemplates()
    # use result
except Exception as e:
    print(e)
```






Email templates are predefined formats linked to various events for delivering messages to users. Use this API to get all system email templates.

*Returned Response:*




[SystemEmailTemplates](#SystemEmailTemplates)

Refer `SystemEmailTemplates` schema for more details.




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {
    "url_shorten": {
      "enabled": true
    },
    "_id": "646b73e7e10612283cfd977f",
    "is_system": true,
    "is_internal": false,
    "name": "Online order confirmed",
    "slug": "bag_confirmed-email",
    "description": "Use this email template for notifying the customers, that their order is Confirmed.",
    "static_to": [],
    "static_cc": [],
    "static_bcc": [],
    "tags": [],
    "subject": {
      "template_type": "nunjucks",
      "template": "{{ email_subject }}"
    },
    "html": {
      "template_type": "nunjucks",
      "template": ""
    },
    "text": {
      "template_type": "nunjucks",
      "template": ""
    },
    "priority": "high",
    "template_variables": {},
    "published": true,
    "category": "website",
    "headers": [],
    "attachments": [],
    "created_at": "2023-05-22T13:53:43.468Z",
    "updated_at": "2023-05-22T13:53:43.468Z",
    "__v": 0
  }
}
```
</details>

</details>









---


### getEmailTemplateById
Get email template by id




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.getEmailTemplateById(id=id)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| id | String | yes | Email template id |  



Email templates are predefined formats linked to various events for delivering messages to users. Use this API to get an email template by id.

*Returned Response:*




[EmailTemplate](#EmailTemplate)

Refer `EmailTemplate` schema for more details.




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {
    "application": "637b6355dc65337da9b5c951",
    "is_system": false,
    "is_internal": false,
    "name": "title",
    "description": "desc",
    "editor_type": "bee",
    "editor_meta": "",
    "static_to": [],
    "static_cc": [
      "abc@abc.com"
    ],
    "static_bcc": [
      "abc@abc.com"
    ],
    "reply_to": "abc@abc.com",
    "tags": [
      "tag"
    ],
    "subject": {
      "template_type": "nunjucks",
      "template": "subject"
    },
    "html": {
      "template_type": "nunjucks",
      "template": ""
    },
    "url_shorten": {
      "enabled": false
    },
    "priority": "low",
    "template_variables": {
      "hello": "world"
    },
    "published": true,
    "category": "website",
    "_id": "649fca8fe89b403f490f9c55",
    "headers": [],
    "attachments": [],
    "created_at": "2023-07-01T06:41:19.360Z",
    "updated_at": "2023-07-01T06:41:19.360Z",
    "slug": "title-W9qbdl8AJ",
    "__v": 0,
    "from_name": "Fynd",
    "text": {
      "template_type": "nunjucks",
      "template": "subject"
    }
  }
}
```
</details>

</details>









---


### updateEmailTemplateById
Update email template by id




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.updateEmailTemplateById(id=id, body=body)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| id | String | yes | Email template id |  
| body | [EmailTemplateReq](#EmailTemplateReq) | yes | Request body |


Email templates are predefined formats linked to various events for delivering messages to users. Use this API to update an email template by id.

*Returned Response:*




[EmailTemplate](#EmailTemplate)

Refer `EmailTemplate` schema for more details.




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {
    "application": "637b6355dc65337da9b5c951",
    "is_system": false,
    "is_internal": false,
    "name": "title",
    "description": "desc",
    "editor_type": "bee",
    "editor_meta": "",
    "static_to": [],
    "static_cc": [
      "abc@abc.com"
    ],
    "static_bcc": [
      "abc@abc.com"
    ],
    "reply_to": "abc@abc.com",
    "tags": [
      "tag"
    ],
    "subject": {
      "template_type": "nunjucks",
      "template": "subject"
    },
    "html": {
      "template_type": "nunjucks",
      "template": ""
    },
    "url_shorten": {
      "enabled": false
    },
    "priority": "low",
    "template_variables": {
      "hello": "world"
    },
    "published": true,
    "category": "website",
    "_id": "649fca8fe89b403f490f9c55",
    "headers": [],
    "attachments": [],
    "created_at": "2023-07-01T06:41:19.360Z",
    "updated_at": "2023-07-01T06:41:19.360Z",
    "slug": "title-W9qbdl8AJ",
    "__v": 0,
    "from_name": "Fynd",
    "text": {
      "template_type": "nunjucks",
      "template": "subject"
    }
  }
}
```
</details>

</details>









---


### deleteEmailTemplateById
Delete email template by id




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.deleteEmailTemplateById(id=id)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| id | String | yes | Email template id |  



Email templates are predefined formats linked to various events for delivering messages to users. Use this API to delete an email template by id.

*Returned Response:*




[GenericDelete](#GenericDelete)

Refer `GenericDelete` schema for more details.




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {
    "message": "Deletion Successfull",
    "acknowledged": true,
    "affected": 1,
    "operation": "TEMP-ST-DEL:ID"
  }
}
```
</details>

</details>









---


### getSubscribedEmailTemplates
Get subscribed email templates




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.getSubscribedEmailTemplates(pageNo=pageNo, pageSize=pageSize, query=query)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| pageNo | Int? | no | Current page no |   
| pageSize | Int? | no | Current request items count |   
| query | HashMap<String,Any>? | no | To search based on plain text |  



Email templates are predefined formats linked to various events for delivering messages to users. Use this API to get all subscribed email templates.

*Returned Response:*




[EmailTemplates](#EmailTemplates)

Refer `EmailTemplates` schema for more details.




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {
    "items": [
      {
        "application": "637b6355dc65337da9b5c951",
        "is_system": false,
        "is_internal": false,
        "name": "title",
        "description": "desc",
        "editor_type": "bee",
        "editor_meta": "",
        "static_to": [],
        "static_cc": [
          "abc@abc.com"
        ],
        "static_bcc": [
          "abc@abc.com"
        ],
        "reply_to": "abc@abc.com",
        "tags": [
          "tag"
        ],
        "subject": {
          "template_type": "nunjucks",
          "template": "subject"
        },
        "html": {
          "template_type": "nunjucks",
          "template": ""
        },
        "url_shorten": {
          "enabled": false
        },
        "priority": "low",
        "template_variables": {
          "hello": "world"
        },
        "published": true,
        "category": "website",
        "_id": "649fca8fe89b403f490f9c55",
        "headers": [],
        "attachments": [],
        "created_at": "2023-07-01T06:41:19.360Z",
        "updated_at": "2023-07-01T06:41:19.360Z",
        "slug": "title-W9qbdl8AJ",
        "__v": 0,
        "from_name": "Fynd",
        "text": {
          "template_type": "nunjucks",
          "template": "subject"
        }
      }
    ],
    "page": {
      "type": "number",
      "current": 1,
      "size": 1,
      "item_total": 66,
      "has_next": true
    }
  }
}
```
</details>

</details>









---


### getSmsTemplates
Get sms templates




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.getSmsTemplates(pageNo=pageNo, pageSize=pageSize, sort=sort, query=query)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| pageNo | Int? | no | Current page no |   
| pageSize | Int? | no | Current request items count |   
| sort | HashMap<String,Any>? | no | To sort based on created_at |   
| query | HashMap<String,Any>? | no | To search based on plain text |  



SMS templates are predefined message formats linked to various events for delivering messages to users. Use this API to get all sms templates.

*Returned Response:*




[SmsTemplates](#SmsTemplates)

Refer `SmsTemplates` schema for more details.




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {
    "items": [
      {
        "url_shorten": {
          "enabled": false
        },
        "_id": "649968feca21d7edd0595b35",
        "application": "637b6355dc65337da9b5c951",
        "is_system": false,
        "is_internal": false,
        "meta": {
          "type": "cloned",
          "template": "61963d42ce3af81bde44a67d",
          "is_system": true
        },
        "name": "TD sms templates",
        "description": "description",
        "message": {
          "template_type": "nunjucks",
          "template": "This is a test message"
        },
        "priority": "low",
        "tags": [
          "tag1",
          "tag2"
        ],
        "template_variables": {
          "hello": "world"
        },
        "template_id": "1234567891234567890123",
        "published": true,
        "category": "website",
        "created_at": "2023-06-26T10:31:26.212Z",
        "updated_at": "2023-06-26T10:31:26.212Z",
        "slug": "TD-sms-templates-KwtzEUcpn",
        "__v": 0
      }
    ],
    "page": {
      "type": "number",
      "current": 1,
      "size": 10,
      "item_total": 17,
      "has_next": true
    }
  }
}
```
</details>

</details>









---


### createSmsTemplate
Create sms template




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.createSmsTemplate(body=body)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- |
| body | [SmsTemplateReq](#SmsTemplateReq) | yes | Request body |


SMS templates are predefined message formats linked to various events for delivering messages to users. Use this API to create an sms template.

*Returned Response:*




[SmsTemplate](#SmsTemplate)

Refer `SmsTemplate` schema for more details.




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {
    "url_shorten": {
      "enabled": false
    },
    "_id": "649968feca21d7edd0595b35",
    "application": "637b6355dc65337da9b5c951",
    "is_system": false,
    "is_internal": false,
    "meta": {
      "type": "cloned",
      "template": "61963d42ce3af81bde44a67d",
      "is_system": true
    },
    "name": "TD sms templates",
    "description": "description",
    "message": {
      "template_type": "nunjucks",
      "template": "This is a test message"
    },
    "priority": "low",
    "tags": [
      "tag1",
      "tag2"
    ],
    "template_variables": {
      "hello": "world"
    },
    "template_id": "1234567891234567890123",
    "published": true,
    "category": "website",
    "created_at": "2023-06-26T10:31:26.212Z",
    "updated_at": "2023-06-26T10:31:26.212Z",
    "slug": "TD-sms-templates-KwtzEUcpn",
    "__v": 0
  }
}
```
</details>

</details>









---


### getSystemSmsTemplates
Get system sms templates




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.getSystemSmsTemplates()
    # use result
except Exception as e:
    print(e)
```






SMS templates are predefined message formats linked to various events for delivering messages to users. Use this API to get all system sms templates.

*Returned Response:*




[ArrayList<SystemSmsTemplates>](#ArrayList<SystemSmsTemplates>)

Refer `SystemSmsTemplates` schema for more details.




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": [
    {
      "url_shorten": {
        "enabled": false
      },
      "_id": "646b73e7e10612283cfd9773",
      "is_system": true,
      "is_internal": false,
      "name": "Order Arrived at Store",
      "description": "Use this SMS template, for notifying the customers, that their requested order has arrived at the store.",
      "slug": "arrived_at_store-sms",
      "message": {
        "template_type": "nunjucks",
        "template": "Delivered. Your shipment for {{ articles }} with {{ orderID }} has been delivered today at {{ delivered_at }}. You can collect it from store on or before {{ collection_date }}. Notification via Fynd"
      },
      "priority": "low",
      "tags": [],
      "template_variables": {
        "email": "care@fynd.com",
        "orderID": "Order ID FY5E53AFAA091115C235",
        "brand": "SAPPER",
        "name": "Alwira Sheikh",
        "tracking_url": "http://go.fyndi.ng/track-order",
        "articles": "Blue Solid Slim Fit Trackpants (28)",
        "contact": 8767087087,
        "ordering_channel": "ECOMM",
        "delivered_at": "GT_Store, Vashi",
        "collection_date": "Fri, Nov 15",
        "credits": 0,
        "slot": "By 9:00 PM",
        "datetime": "Feb 28",
        "cashback": 0,
        "ref_application": {
          "support_email": "care@fynd.com",
          "app_information": {
            "additional_data": {
              "address_line": "Kurar village,Malad",
              "city_pincode": "Mumbai - 400097",
              "contactUs": "https://uniket-testing.addsale.link/contact-us",
              "domain": "uniket-testing.addsale.link",
              "privacyPolicy": "https://fynd.freshdesk.com/support/solutions/articles/33000214398-privacy-policy"
            }
          },
          "domain": {
            "name": "https://fynd.com"
          },
          "logo": {
            "secure_url": "https://res.cloudinary.com/dwzm9bysq/image/upload/v1587981831/production/system/pointblank/fynd_logo_square_vunk4f.png"
          }
        }
      },
      "template_id": "1007569169965694807",
      "published": true,
      "category": "website",
      "created_at": "2023-05-22T13:53:43.439Z",
      "updated_at": "2023-05-22T13:53:43.439Z",
      "__v": 0
    }
  ]
}
```
</details>

</details>









---


### getSmsTemplateById
Get sms template by id




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.getSmsTemplateById(id=id)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| id | String | yes | Sms template id |  



SMS templates are predefined message formats linked to various events for delivering messages to users. Use this API to get an sms template by ID.

*Returned Response:*




[SmsTemplate](#SmsTemplate)

Refer `SmsTemplate` schema for more details.




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {
    "url_shorten": {
      "enabled": false
    },
    "_id": "649968feca21d7edd0595b35",
    "application": "637b6355dc65337da9b5c951",
    "is_system": false,
    "is_internal": false,
    "meta": {
      "type": "cloned",
      "template": "61963d42ce3af81bde44a67d",
      "is_system": true
    },
    "name": "TD sms templates",
    "description": "description",
    "message": {
      "template_type": "nunjucks",
      "template": "This is a test message"
    },
    "priority": "low",
    "tags": [
      "tag1",
      "tag2"
    ],
    "template_variables": {
      "hello": "world"
    },
    "template_id": "1234567891234567890123",
    "published": true,
    "category": "website",
    "created_at": "2023-06-26T10:31:26.212Z",
    "updated_at": "2023-06-26T10:31:26.212Z",
    "slug": "TD-sms-templates-KwtzEUcpn",
    "__v": 0
  }
}
```
</details>

</details>









---


### updateSmsTemplateById
Update sms template by id




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.updateSmsTemplateById(id=id, body=body)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| id | String | yes | Sms template id |  
| body | [SmsTemplateReq](#SmsTemplateReq) | yes | Request body |


SMS templates are predefined message formats linked to various events for delivering messages to users. Use this API to update an sms template by ID.

*Returned Response:*




[SmsTemplate](#SmsTemplate)

Refer `SmsTemplate` schema for more details.




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {
    "url_shorten": {
      "enabled": false
    },
    "_id": "649968feca21d7edd0595b35",
    "application": "637b6355dc65337da9b5c951",
    "is_system": false,
    "is_internal": false,
    "meta": {
      "type": "cloned",
      "template": "61963d42ce3af81bde44a67d",
      "is_system": true
    },
    "name": "TD sms templates",
    "description": "description",
    "message": {
      "template_type": "nunjucks",
      "template": "This is a test message"
    },
    "priority": "low",
    "tags": [
      "tag1",
      "tag2"
    ],
    "template_variables": {
      "hello": "world"
    },
    "template_id": "1234567891234567890123",
    "published": true,
    "category": "website",
    "created_at": "2023-06-26T10:31:26.212Z",
    "updated_at": "2023-06-26T10:31:26.212Z",
    "slug": "TD-sms-templates-KwtzEUcpn",
    "__v": 0
  }
}
```
</details>

</details>









---


### deleteSmsTemplateById
Delete sms template by id




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.deleteSmsTemplateById(id=id)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| id | String | yes | Sms template id |  



SMS templates are predefined message formats linked to various events for delivering messages to users. Use this API to delete an sms template by ID.

*Returned Response:*




[GenericDelete](#GenericDelete)

Refer `GenericDelete` schema for more details.




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {
    "message": "Deletion Successfull",
    "acknowledged": true,
    "affected": 1,
    "operation": "TEMP-ST-DEL:ID"
  }
}
```
</details>

</details>









---


### getSubscribedSmsTemplates
Get subscribed sms templates




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.getSubscribedSmsTemplates(pageNo=pageNo, pageSize=pageSize, query=query)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| pageNo | Int? | no | Current page no |   
| pageSize | Int? | no | Current request items count |   
| query | HashMap<String,Any>? | no | To search based on plain text |  



SMS templates are predefined message formats linked to various events for delivering messages to users. Use this API to get all subscribed sms templates.

*Returned Response:*




[SmsTemplates](#SmsTemplates)

Refer `SmsTemplates` schema for more details.




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {
    "items": [
      {
        "url_shorten": {
          "enabled": false
        },
        "_id": "649968feca21d7edd0595b35",
        "application": "637b6355dc65337da9b5c951",
        "is_system": false,
        "is_internal": false,
        "meta": {
          "type": "cloned",
          "template": "61963d42ce3af81bde44a67d",
          "is_system": true
        },
        "name": "TD sms templates",
        "description": "description",
        "message": {
          "template_type": "nunjucks",
          "template": "This is a test message"
        },
        "priority": "low",
        "tags": [
          "tag1",
          "tag2"
        ],
        "template_variables": {
          "hello": "world"
        },
        "template_id": "1234567891234567890123",
        "published": true,
        "category": "website",
        "created_at": "2023-06-26T10:31:26.212Z",
        "updated_at": "2023-06-26T10:31:26.212Z",
        "slug": "TD-sms-templates-KwtzEUcpn",
        "__v": 0
      }
    ],
    "page": {
      "type": "number",
      "current": 1,
      "size": 10,
      "item_total": 17,
      "has_next": true
    }
  }
}
```
</details>

</details>









---


### sendCommunicationSynchronously
Send email or sms synchronously




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.sendCommunicationSynchronously(body=body)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- |
| body | [EngineRequest](#EngineRequest) | yes | Request body |


Send email or sms synchronously

*Returned Response:*




[EngineResponse](#EngineResponse)

Success




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {
    "success": true
  }
}
```
</details>

</details>









---


### sendCommunicationAsynchronously
Send email or sms asynchronously




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.sendCommunicationAsynchronously(body=body)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- |
| body | [EngineRequest](#EngineRequest) | yes | Request body |


Send email or sms asynchronously

*Returned Response:*




[EngineResponse](#EngineResponse)

Success




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {
    "success": true
  }
}
```
</details>

</details>









---


### getEventSubscriptions
Get event subscriptions




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.getEventSubscriptions(pageNo=pageNo, pageSize=pageSize, populate=populate)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| pageNo | Int? | no | Current page no |   
| pageSize | Int? | no | Current request items count |   
| populate | String? | no | Populate Fields |  



Get event subscriptions

*Returned Response:*




[EventSubscriptions](#EventSubscriptions)

Success




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {
    "items": [
      {
        "template": {
          "sms": {
            "subscribed": true,
            "template": "null"
          },
          "email": {
            "subscribed": true,
            "template": "5e5653c1d503e0038407fc16"
          }
        },
        "is_default": true,
        "_id": "5e56598f2bfda9050ccaa8e8",
        "application": "000000000000000000000004",
        "event": "5e5653c1d503e0038407fc10",
        "slug": "reset-password-event",
        "created_at": "2020-02-26T11:42:08.164Z",
        "updated_at": "2021-03-03T09:00:47.871Z",
        "__v": 0
      },
      {
        "template": {
          "sms": {
            "subscribed": true,
            "template": "null"
          },
          "email": {
            "subscribed": true,
            "template": "5e5653c1d503e0038407fc17"
          }
        },
        "is_default": true,
        "_id": "5e56598f2bfda9050ccaa911",
        "application": "000000000000000000000004",
        "event": "5e5653c1d503e0038407fc11",
        "slug": "invite-email-event",
        "created_at": "2020-02-26T11:42:08.174Z",
        "updated_at": "2021-03-03T09:00:47.871Z",
        "__v": 0
      },
      {
        "template": {
          "sms": {
            "subscribed": true,
            "template": "null"
          },
          "email": {
            "subscribed": true,
            "template": "5e5653c1d503e0038407fc14"
          }
        },
        "is_default": true,
        "_id": "5e56598f2bfda9050ccaa8f2",
        "application": "000000000000000000000004",
        "event": "5e5653c1d503e0038407fc12",
        "slug": "verify-email-event",
        "created_at": "2020-02-26T11:42:08.172Z",
        "updated_at": "2021-03-03T09:00:47.953Z",
        "__v": 0
      },
      {
        "template": {
          "sms": {
            "subscribed": true,
            "template": "null"
          },
          "email": {
            "subscribed": true,
            "template": "5e5653c1d503e0038407fc15"
          }
        },
        "is_default": true,
        "_id": "5e56598f2bfda9050ccaa8fd",
        "application": "000000000000000000000004",
        "event": "5e5653c1d503e0038407fc13",
        "slug": "verify-otp-event",
        "created_at": "2020-02-26T11:42:08.172Z",
        "updated_at": "2021-03-03T09:00:47.953Z",
        "__v": 0
      },
      {
        "template": {
          "sms": {
            "subscribed": true,
            "template": "5e565a10343582051d211d1c"
          },
          "email": {
            "subscribed": true,
            "template": "5e565a10343582051d211d1b"
          }
        },
        "is_default": true,
        "_id": "5e565a16343582051d211d68",
        "application": "000000000000000000000004",
        "event": "5e565a10343582051d211d1d",
        "slug": "cancelled_customer-event",
        "created_at": "2020-02-26T11:44:22.246Z",
        "updated_at": "2021-03-03T09:00:47.953Z",
        "__v": 0
      },
      {
        "template": {
          "sms": {
            "subscribed": true,
            "template": "5e565a10343582051d211d1f"
          },
          "email": {
            "subscribed": true,
            "template": "5e565a10343582051d211d1e"
          }
        },
        "is_default": true,
        "_id": "5e565a16343582051d211d6c",
        "application": "000000000000000000000004",
        "event": "5e565a11343582051d211d20",
        "slug": "cancelled_fynd-event",
        "created_at": "2020-02-26T11:44:22.314Z",
        "updated_at": "2021-03-03T09:00:47.953Z",
        "__v": 0
      },
      {
        "template": {
          "sms": {
            "subscribed": true,
            "template": "5e565a11343582051d211d22"
          },
          "email": {
            "subscribed": true,
            "template": "5e565a11343582051d211d21"
          }
        },
        "is_default": true,
        "_id": "5e565a16343582051d211d65",
        "application": "000000000000000000000004",
        "event": "5e565a11343582051d211d23",
        "slug": "delivery_done-event",
        "created_at": "2020-02-26T11:44:22.246Z",
        "updated_at": "2021-03-03T09:00:47.972Z",
        "__v": 0
      },
      {
        "template": {
          "sms": {
            "subscribed": true,
            "template": "5e565a11343582051d211d25"
          },
          "email": {
            "subscribed": true,
            "template": "5e565a11343582051d211d24"
          }
        },
        "is_default": true,
        "_id": "5e565a16343582051d211d61",
        "application": "000000000000000000000004",
        "event": "5e565a11343582051d211d26",
        "slug": "out_for_delivery-event",
        "created_at": "2020-02-26T11:44:22.171Z",
        "updated_at": "2021-03-03T09:00:47.972Z",
        "__v": 0
      },
      {
        "template": {
          "sms": {
            "subscribed": true,
            "template": "5e565a12343582051d211d28"
          },
          "email": {
            "subscribed": true,
            "template": "5e565a11343582051d211d27"
          }
        },
        "is_default": true,
        "_id": "5e565a16343582051d211d62",
        "application": "000000000000000000000004",
        "event": "5e565a12343582051d211d29",
        "slug": "out_for_pickup-event",
        "created_at": "2020-02-26T11:44:22.171Z",
        "updated_at": "2021-03-03T09:00:47.972Z",
        "__v": 0
      },
      {
        "template": {
          "sms": {
            "subscribed": true,
            "template": "5e565a12343582051d211d2b"
          },
          "email": {
            "subscribed": true,
            "template": "5e565a12343582051d211d2a"
          }
        },
        "is_default": true,
        "_id": "5e565a16343582051d211d69",
        "application": "000000000000000000000004",
        "event": "5e565a12343582051d211d2c",
        "slug": "placed-event",
        "created_at": "2020-02-26T11:44:22.246Z",
        "updated_at": "2021-03-03T09:00:47.953Z",
        "__v": 0
      },
      {
        "template": {
          "sms": {
            "subscribed": true,
            "template": "5e565a12343582051d211d2e"
          },
          "email": {
            "subscribed": true,
            "template": "5e565a12343582051d211d2d"
          }
        },
        "is_default": true,
        "_id": "5e565a16343582051d211d66",
        "application": "000000000000000000000004",
        "event": "5e565a12343582051d211d2f",
        "slug": "refund_completed-event",
        "created_at": "2020-02-26T11:44:22.246Z",
        "updated_at": "2021-03-03T09:00:48.052Z",
        "__v": 0
      },
      {
        "template": {
          "sms": {
            "subscribed": true,
            "template": "5e565a13343582051d211d31"
          },
          "email": {
            "subscribed": true,
            "template": "5e565a12343582051d211d30"
          }
        },
        "is_default": true,
        "_id": "5e565a16343582051d211d64",
        "application": "000000000000000000000004",
        "event": "5e565a13343582051d211d32",
        "slug": "refund_initiated-event",
        "created_at": "2020-02-26T11:44:22.246Z",
        "updated_at": "2021-03-03T09:00:47.972Z",
        "__v": 0
      },
      {
        "template": {
          "sms": {
            "subscribed": true,
            "template": "5e565a13343582051d211d34"
          },
          "email": {
            "subscribed": true,
            "template": "5e565a13343582051d211d33"
          }
        },
        "is_default": true,
        "_id": "5e565a16343582051d211d6d",
        "application": "000000000000000000000004",
        "event": "5e565a13343582051d211d35",
        "slug": "rejected_by_customer-event",
        "created_at": "2020-02-26T11:44:22.314Z",
        "updated_at": "2021-03-03T09:00:47.972Z",
        "__v": 0
      },
      {
        "template": {
          "sms": {
            "subscribed": true,
            "template": "5e565a13343582051d211d37"
          },
          "email": {
            "subscribed": true,
            "template": "5e565a13343582051d211d36"
          }
        },
        "is_default": true,
        "_id": "5e565a16343582051d211d63",
        "application": "000000000000000000000004",
        "event": "5e565a13343582051d211d38",
        "slug": "return_accepted-event",
        "created_at": "2020-02-26T11:44:22.178Z",
        "updated_at": "2021-03-03T09:00:48.052Z",
        "__v": 0
      },
      {
        "template": {
          "sms": {
            "subscribed": true,
            "template": "5e565a14343582051d211d3a"
          },
          "email": {
            "subscribed": true,
            "template": "5e565a13343582051d211d39"
          }
        },
        "is_default": true,
        "_id": "5e565a16343582051d211d6a",
        "application": "000000000000000000000004",
        "event": "5e565a14343582051d211d3b",
        "slug": "return_bag_picked_by_dp-event",
        "created_at": "2020-02-26T11:44:22.246Z",
        "updated_at": "2021-03-03T09:00:48.052Z",
        "__v": 0
      },
      {
        "template": {
          "sms": {
            "subscribed": true,
            "template": "5e565a14343582051d211d3d"
          },
          "email": {
            "subscribed": true,
            "template": "5e565a14343582051d211d3c"
          }
        },
        "is_default": true,
        "_id": "5e565a16343582051d211d67",
        "application": "000000000000000000000004",
        "event": "5e565a14343582051d211d3e",
        "slug": "return_initiated-event",
        "created_at": "2020-02-26T11:44:22.246Z",
        "updated_at": "2021-03-03T09:00:48.052Z",
        "__v": 0
      },
      {
        "template": {
          "sms": {
            "subscribed": true,
            "template": "5e565a14343582051d211d40"
          },
          "email": {
            "subscribed": true,
            "template": "5e565a14343582051d211d3f"
          }
        },
        "is_default": true,
        "_id": "5e565a16343582051d211d6b",
        "application": "000000000000000000000004",
        "event": "5e565a14343582051d211d41",
        "slug": "return_not_accepted-event",
        "created_at": "2020-02-26T11:44:22.314Z",
        "updated_at": "2021-03-03T09:00:48.052Z",
        "__v": 0
      },
      {
        "template": {
          "sms": {
            "subscribed": true,
            "template": "5e565a15343582051d211d43"
          },
          "email": {
            "subscribed": true,
            "template": "5e565a15343582051d211d42"
          }
        },
        "is_default": true,
        "_id": "5e565a16343582051d211d6e",
        "application": "000000000000000000000004",
        "event": "5e565a15343582051d211d44",
        "slug": "return_request_cancelled-event",
        "created_at": "2020-02-26T11:44:22.314Z",
        "updated_at": "2021-03-03T09:00:48.052Z",
        "__v": 0
      },
      {
        "template": {
          "sms": {
            "subscribed": true,
            "template": "5e6a4b6d610dbf44166e74ba"
          },
          "email": {
            "subscribed": true,
            "template": "null"
          }
        },
        "is_default": true,
        "_id": "5e6a4b6e610dbf6b2a6e74c4",
        "application": "000000000000000000000004",
        "event": "5e6a4b6d610dbf3b146e74bb",
        "slug": "handed_over_to_customer-event",
        "created_at": "2020-03-12T14:47:10.453Z",
        "updated_at": "2021-03-03T09:00:48.141Z",
        "__v": 0
      },
      {
        "template": {
          "sms": {
            "subscribed": true,
            "template": "5e6a4b6d610dbf01326e74b6"
          },
          "email": {
            "subscribed": true,
            "template": "null"
          }
        },
        "is_default": true,
        "_id": "5e6a4b6e610dbf907e6e74c2",
        "application": "000000000000000000000004",
        "event": "5e6a4b6d610dbf454e6e74b7",
        "slug": "arrived_at_store-event",
        "created_at": "2020-03-12T14:47:10.453Z",
        "updated_at": "2021-03-03T09:00:48.052Z",
        "__v": 0
      },
      {
        "template": {
          "sms": {
            "subscribed": true,
            "template": "5e6a4b6d610dbf69b16e74b8"
          },
          "email": {
            "subscribed": true,
            "template": "null"
          }
        },
        "is_default": true,
        "_id": "5e6a4b6e610dbf28086e74c3",
        "application": "000000000000000000000004",
        "event": "5e6a4b6d610dbf91c76e74b9",
        "slug": "bag_packed-event",
        "created_at": "2020-03-12T14:47:10.453Z",
        "updated_at": "2021-03-03T09:00:48.052Z",
        "__v": 0
      },
      {
        "template": {
          "sms": {
            "subscribed": true,
            "template": "null"
          },
          "email": {
            "subscribed": true,
            "template": "5ed72116ccc0c408fbb5a404"
          }
        },
        "is_default": true,
        "_id": "5ed72117ccc0c48f29b5a408",
        "application": "000000000000000000000004",
        "event": "5ed72116ccc0c4e240b5a405",
        "slug": "order-review-reminder-event",
        "created_at": "2020-06-03T04:03:35.394Z",
        "updated_at": "2021-03-03T09:00:48.052Z",
        "__v": 0
      },
      {
        "template": {
          "sms": {
            "subscribed": true,
            "template": "5f633b15b490eaf13f494bf4"
          },
          "email": {
            "subscribed": true,
            "template": "null"
          }
        },
        "is_default": true,
        "_id": "5f633b16b490ea31eb494bfd",
        "application": "000000000000000000000004",
        "event": "5f633b15b490ea3c9b494bf5",
        "slug": "referral-code-applied-to-referrer",
        "created_at": "2020-09-17T10:31:50.204Z",
        "updated_at": "2021-03-03T09:00:48.141Z",
        "__v": 0
      },
      {
        "template": {
          "sms": {
            "subscribed": true,
            "template": "5f633b15b490ea465b494bf2"
          },
          "email": {
            "subscribed": true,
            "template": "null"
          }
        },
        "is_default": true,
        "_id": "5f633b16b490eada59494bfc",
        "application": "000000000000000000000004",
        "event": "5f633b15b490ea40dd494bf3",
        "slug": "referral-code-applied-to-referred-friend",
        "created_at": "2020-09-17T10:31:50.204Z",
        "updated_at": "2021-03-03T09:00:48.141Z",
        "__v": 0
      },
      {
        "template": {
          "sms": {
            "subscribed": true,
            "template": "5fe2e7da09c5fc047172e830"
          },
          "email": {
            "subscribed": true,
            "template": "null"
          }
        },
        "is_default": true,
        "_id": "5fe2e7dc09c5fc657372e841",
        "application": "000000000000000000000004",
        "event": "5fe2e7da09c5fc3da372e831",
        "slug": "return_dp_out_for_pickup-event",
        "created_at": "2020-12-23T06:46:52.214Z",
        "updated_at": "2021-03-03T09:00:48.141Z",
        "__v": 0
      },
      {
        "template": {
          "sms": {
            "subscribed": true,
            "template": "5fe2e7da09c5fcef0a72e82b"
          },
          "email": {
            "subscribed": true,
            "template": "5ff841fd864df30915c416e9"
          }
        },
        "is_default": true,
        "_id": "600951fb0e9745637d2e5081",
        "application": "000000000000000000000004",
        "event": "5fe2e7da09c5fc524f72e82c",
        "slug": "delivery_attempt_failed-event",
        "created_at": "2021-01-21T10:05:47.315Z",
        "updated_at": "2021-03-03T09:00:48.141Z",
        "__v": 0
      },
      {
        "template": {
          "sms": {
            "subscribed": true,
            "template": "5fe2e7da09c5fc6c5272e82e"
          },
          "email": {
            "subscribed": true,
            "template": "5fe2e7da09c5fc7fee72e82d"
          }
        },
        "is_default": true,
        "_id": "5fe2e7dc09c5fc10fe72e840",
        "application": "000000000000000000000004",
        "event": "5fe2e7da09c5fc611c72e82f",
        "slug": "return_bag_picked-event",
        "created_at": "2020-12-23T06:46:52.214Z",
        "updated_at": "2021-03-03T09:00:48.141Z",
        "__v": 0
      },
      {
        "template": {
          "sms": {
            "subscribed": true,
            "template": "5fe2e7da09c5fc4cde72e829"
          },
          "email": {
            "subscribed": true,
            "template": "null"
          }
        },
        "is_default": true,
        "_id": "5fe2e7dc09c5fcf4fc72e83e",
        "application": "000000000000000000000004",
        "event": "5fe2e7da09c5fc72d272e82a",
        "slug": "bag_picked-event",
        "created_at": "2020-12-23T06:46:52.214Z",
        "updated_at": "2021-03-03T09:00:48.141Z",
        "__v": 0
      }
    ],
    "page": {
      "type": "number",
      "current": 1,
      "size": 200,
      "item_total": 28,
      "has_next": false
    }
  }
}
```
</details>

</details>









---


### createEventSubscriptions
Create event subscriptions




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.createEventSubscriptions(body=body)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- |
| body | [SubscriptionsObject](#SubscriptionsObject) | yes | Request body |


Create event subscriptions

*Returned Response:*




[EventSubscriptionsBulkUpdateResponse](#EventSubscriptionsBulkUpdateResponse)

Success




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": [
    {
      "template": {
        "sms": {
          "subscribed": true,
          "template": "65252a7f2b235b3b7a75e4be"
        },
        "email": {
          "subscribed": true,
          "template": "65252a196fcb371a2d6aa418"
        },
        "pushnotification": {
          "subscribed": false
        }
      },
      "_id": "64b2ddb856dd97a75c452f2d",
      "application": "64b2ddb6cb99a609e12a9bea",
      "event": "64aec4c6c987e14691600e2b",
      "slug": "invite-event",
      "category": "website",
      "created_at": "2023-07-15T17:56:08.601Z",
      "updated_at": "2023-10-10T10:50:28.781Z"
    }
  ]
}
```
</details>

</details>









---


### getEventSubscriptionsById
Get event subscriptions by id




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.getEventSubscriptionsById(id=id, populate=populate)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| id | String | yes | Event subscription id |   
| populate | String? | no | Populate Fields |  



Get event subscriptions by id

*Returned Response:*




[EventSubscription](#EventSubscription)

Success




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {
    "template": {
      "sms": {
        "subscribed": true,
        "template": "64aec4c4c987e14691600d1a"
      },
      "email": {
        "subscribed": true,
        "template": "64aec4c4c987e14691600d1a"
      },
      "pushnotification": {
        "subscribed": false
      }
    },
    "_id": "64b2ddb756dd97a75c452ee6",
    "application": "64b2ddb6cb99a609e12a9bea",
    "event": "64aec4c4c987e14691600d1d",
    "slug": "arriving_early_out_for_delivery-event",
    "category": "website",
    "created_at": "2023-07-15T17:56:07.926Z",
    "updated_at": "2023-10-07T09:41:32.836Z",
    "__v": 0
  }
}
```
</details>

</details>









---


### editEventSubscriptions
Create event subscriptions




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.editEventSubscriptions(id=id, body=body)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| id | String | yes | Event subscription id |  
| body | [SubscriptionsObject](#SubscriptionsObject) | yes | Request body |


Create event subscriptions

*Returned Response:*




[EventSubscriptionsBulkUpdateResponse](#EventSubscriptionsBulkUpdateResponse)

Success




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": [
    {
      "template": {
        "sms": {
          "subscribed": true,
          "template": "65252a7f2b235b3b7a75e4be"
        },
        "email": {
          "subscribed": true,
          "template": "65252a196fcb371a2d6aa418"
        },
        "pushnotification": {
          "subscribed": false
        }
      },
      "_id": "64b2ddb856dd97a75c452f2d",
      "application": "64b2ddb6cb99a609e12a9bea",
      "event": "64aec4c6c987e14691600e2b",
      "slug": "invite-event",
      "category": "website",
      "created_at": "2023-07-15T17:56:08.601Z",
      "updated_at": "2023-10-10T10:50:28.781Z"
    }
  ]
}
```
</details>

</details>









---


### deleteEventSubscriptionsById
Create event subscriptions




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.deleteEventSubscriptionsById(id=id)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| id | String | yes | Event subscription id |  



Create event subscriptions

*Returned Response:*




[GenericDelete](#GenericDelete)

Refer `GenericDelete` schema for more details.




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {
    "message": "Deletion Successfull",
    "acknowledged": true,
    "affected": 1,
    "operation": "TEMP-ST-DEL:ID"
  }
}
```
</details>

</details>









---


### createEventSubscriptionsByBulk
Create event subscriptions by bulk




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.createEventSubscriptionsByBulk(body=body)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- |
| body | [EventSubscriptionsBulkUpdateRequest](#EventSubscriptionsBulkUpdateRequest) | yes | Request body |


Create event subscriptions by bulk

*Returned Response:*




[ArrayList<EventSubscriptionsBulkUpdateResponse>](#ArrayList<EventSubscriptionsBulkUpdateResponse>)

Success




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": [
    {
      "template": {
        "sms": {
          "subscribed": true,
          "template": "65252a7f2b235b3b7a75e4be"
        },
        "email": {
          "subscribed": true,
          "template": "65252a196fcb371a2d6aa418"
        },
        "pushnotification": {
          "subscribed": false
        }
      },
      "_id": "64b2ddb856dd97a75c452f2d",
      "application": "64b2ddb6cb99a609e12a9bea",
      "event": "64aec4c6c987e14691600e2b",
      "slug": "invite-event",
      "category": "website",
      "created_at": "2023-07-15T17:56:08.601Z",
      "updated_at": "2023-10-10T10:50:28.781Z"
    }
  ]
}
```
</details>

</details>









---


### getGlobalVariables
get global variables




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.getGlobalVariables()
    # use result
except Exception as e:
    print(e)
```






get global variables

*Returned Response:*




[GlobalVariablesGetResponse](#GlobalVariablesGetResponse)

Refer `GlobalVariablesGetResponse` schema for more details.




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {
    "read_only": {
      "app.address.address_line": [],
      "app.shipping_policy": "",
      "app.returns_policy": "",
      "app.terms_policy": "",
      "app.copyright_text": null,
      "app.address_line": "",
      "app.city_pincode": "",
      "app.logo_url": null,
      "app.support_email": null,
      "app.support_mobile": null,
      "app.contact_us": "",
      "app.domain": "",
      "app.privacy_policy": "https://fynd.freshdesk.com/support/solutions/articles/33000214398-privacy-policy"
    },
    "editable": {
      "service_country": "uzbekistan",
      "service_name": "fynd",
      "service_platform": "fynd platform"
    }
  }
}
```
</details>

</details>









---


### postGlobalVariables
post global variables




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.postGlobalVariables(body=body)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- |
| body | [GlobalVariablesReq](#GlobalVariablesReq) | yes | Request body |


psot global variables

*Returned Response:*




[GlobalVariablesPostResponse](#GlobalVariablesPostResponse)

Refer `GlobalVariablesPostResponse` schema for more details.




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {
    "_id": "64a2be215cc595c57fa0e40a",
    "category": "website",
    "application": "637b6355dc65337da9b5c951",
    "global_variables": {
      "service_country": "uzbekistan",
      "service_name": "fynd-plato",
      "service_platform": "fynd platform"
    },
    "created_at": "2023-07-03T12:25:05.819Z"
  }
}
```
</details>

</details>









---


### getJobs
Get jobs




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.getJobs(pageNo=pageNo, pageSize=pageSize, sort=sort, query=query)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| pageNo | Int? | no | Current page no |   
| pageSize | Int? | no | Current request items count |   
| sort | HashMap<String,Any>? | no | To sort based on created_at |   
| query | HashMap<String,Any>? | no | To search based on plain text |  



Get jobs

*Returned Response:*




[Jobs](#Jobs)

Success




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {
    "items": [
      {
        "completed": true,
        "is_active": false,
        "_id": "6044be260c92a7be0624f1cf",
        "campaign": "6044be1e0c92a7026924f1ce",
        "application": "000000000000000000000001",
        "created_at": "2021-03-07T11:51:02.234Z",
        "updated_at": "2021-03-07T12:12:36.587Z",
        "__v": 0
      }
    ],
    "page": {
      "type": "number",
      "current": 1,
      "size": 50,
      "item_total": 1,
      "has_next": false
    }
  }
}
```
</details>

</details>









---


### createJobs
Create jobs




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.createJobs(body=body)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- |
| body | [CreateJobsReq](#CreateJobsReq) | yes | Request body |


Create jobs

*Returned Response:*




[CreateJobsRes](#CreateJobsRes)

Success




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {
    "application": "000000000000000000000004",
    "campaign": "656c9cad5638b4af9e2329af",
    "completed": true,
    "is_active": true,
    "_id": "5fd9fd44c474a7e3d5d376d6",
    "created_at": "2020-12-16T12:27:48.051Z",
    "updated_at": "2020-12-16T12:27:48.051Z",
    "__v": 0
  }
}
```
</details>

</details>









---


### triggerCampaignJob
Trigger campaign job




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.triggerCampaignJob(body=body)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- |
| body | [TriggerJobRequest](#TriggerJobRequest) | yes | Request body |


Trigger campaign job

*Returned Response:*




[TriggerJobResponse](#TriggerJobResponse)

Success




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {
    "status": 200
  }
}
```
</details>

</details>









---


### getJobLogs
Get job logs




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.getJobLogs(pageNo=pageNo, pageSize=pageSize, sort=sort, query=query)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| pageNo | Int? | no | Current page no |   
| pageSize | Int? | no | Current request items count |   
| sort | HashMap<String,Any>? | no | To sort based on created_at |   
| query | HashMap<String,Any>? | no | To search based on plain text |  



Get job logs

*Returned Response:*




[JobLogs](#JobLogs)

Success




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {
    "items": [
      {
        "imported": {
          "count": 61135
        },
        "processed": {
          "email": {
            "success": 0,
            "failed": 0,
            "suppressed": 0
          },
          "sms": {
            "success": 61313,
            "failed": 85,
            "suppressed": 87
          }
        },
        "_id": "6044be30bc5f4b79aae7b29f",
        "job": "6044be260c92a7be0624f1cf",
        "campaign": "6044be1e0c92a7026924f1ce",
        "created_at": "2021-03-07T11:51:12.778Z",
        "updated_at": "2021-03-07T12:14:11.475Z",
        "__v": 0
      }
    ],
    "page": {
      "type": "number",
      "current": 1,
      "size": 50,
      "item_total": 1,
      "has_next": false
    }
  }
}
```
</details>

</details>









---


### getCommunicationLogs
Get communication logs




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.getCommunicationLogs(pageId=pageId, pageSize=pageSize, sort=sort, query=query)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| pageId | String? | no | Current page no |   
| pageSize | Int? | no | Current request items count |   
| sort | HashMap<String,Any>? | no | To sort based on _id |   
| query | HashMap<String,Any>? | no |  |  



Get communication logs

*Returned Response:*




[Logs](#Logs)

Success




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {
    "items": [
      {
        "sms": {
          "phone_number": "1234567890",
          "country_code": "+91",
          "template": "603e00649014219f87943213",
          "provider": "5f8ee2234d70f7c5624f0413"
        },
        "pushnotification": {
          "pushtokens": []
        },
        "meta": {
          "type": "job",
          "job": "603e021f171b19ee5a4324f4",
          "campaign": "603e0217171b19556e4324f3",
          "identifier": "pointblank.00395d65-c0a9-f9dc-0c46-5d65c0aa0c46"
        },
        "_id": "603e02300b9f817e1592fcbd",
        "application": "000000000000000000000004",
        "service": "sms-consumer",
        "step": "MSG_SENT",
        "status": "success",
        "pod": "fynd-core-pointblank-smslow-cnsmr-dply-d6dbf9d7f-b6h2f",
        "expire_at": "2021-04-01T09:15:28.526Z",
        "created_at": "2021-03-02T09:15:28.527Z"
      }
    ],
    "page": {
      "type": "cursor",
      "next_id": "null",
      "has_previous": false,
      "has_next": false
    }
  }
}
```
</details>

</details>









---


### getSystemNotifications
Get system notifications




```python
try:
    result = await platformClient.communication.getSystemNotifications(pageNo=pageNo, pageSize=pageSize)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| pageNo | Int? | no |  |   
| pageSize | Int? | no |  |  



Get system notifications

*Returned Response:*




[SystemNotifications](#SystemNotifications)

Success




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {
    "items": [
      {
        "notification": {
          "title": "Xyz Company is verified!",
          "body": "",
          "subtitle": "",
          "icon": "icon.png",
          "deeplink": "",
          "click_action": ""
        },
        "user": {
          "type": "company",
          "value": "1"
        },
        "settings": {
          "sound": true,
          "priority": "normal",
          "time_to_live": "60"
        },
        "_id": "60619f167dbd13ff0722f6dd",
        "group": "fynd-platform",
        "created_at": "2021-03-29T09:34:14.182Z"
      }
    ],
    "last_read_anchor": 1616748860,
    "page": {
      "type": "number",
      "current": 1,
      "size": 1,
      "item_total": 1,
      "has_next": false
    }
  }
}
```
</details>

</details>









---


### sendOtp
Send OTP using email and sms




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.sendOtp(body=body)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- |
| body | [SendOtpCommsReq](#SendOtpCommsReq) | yes | Request body |


Send OTP Comms via email and sms

*Returned Response:*




[SendOtpCommsRes](#SendOtpCommsRes)

Success




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {
    "sms": {
      "success": true,
      "request_id": "c8d1bd63d56a2d368aae9dbd4e7d8326",
      "message": "OTP sent",
      "mobile": "9096686804",
      "country_code": "91",
      "resend_timer": 30
    },
    "email": {
      "success": true,
      "request_id": "1cc79c911923971580d903039ea9ee05",
      "message": "OTP sent",
      "to": "parvezshaikh@gofynd.com",
      "resend_timer": 30
    }
  }
}
```
</details>

</details>









---


### verfiyOtp
Verify OTP sent via email and sms




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.verfiyOtp(body=body)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- |
| body | [VerifyOtpCommsReq](#VerifyOtpCommsReq) | yes | Request body |


Verify OTP sent via email and sms

*Returned Response:*




[VerifyOtpCommsSuccessRes](#VerifyOtpCommsSuccessRes)

Success




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {
    "success": true,
    "mobile": "9096686804",
    "country_code": "91",
    "message": "OTP verified"
  }
}
```
</details>

</details>









---


### getOtpConfiguration
Get otp-configuration, if not present in db then return default settings




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.getOtpConfiguration()
    # use result
except Exception as e:
    print(e)
```






Get otp-configuration

*Returned Response:*




[OtpConfiguration](#OtpConfiguration)

Success




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {
    "type": "numeric",
    "otp_length": 4,
    "expiry": {
      "type": "new",
      "duration": {
        "time": 5,
        "denomination": "min"
      }
    },
    "application_id": "6399ba6924ab1bacf0131492",
    "company_id": "1"
  }
}
```
</details>

</details>









---


### updateOtpConfiguration
Update/insert otp configurations




```python
try:
    result = await platformClient.application("<APPLICATION_ID>").communication.updateOtpConfiguration()
    # use result
except Exception as e:
    print(e)
```






Update otp-configuration

*Returned Response:*




[OtpConfiguration](#OtpConfiguration)

Success




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; default</i></summary>

```json
{
  "value": {
    "type": "numeric",
    "otp_length": 4,
    "expiry": {
      "type": "new",
      "duration": {
        "time": 5,
        "denomination": "min"
      }
    },
    "application_id": "6399ba6924ab1bacf0131492",
    "company_id": "1"
  }
}
```
</details>

</details>









---




### Schemas

 
 
 #### [EventSubscriptionsBulkUpdateRequest](#EventSubscriptionsBulkUpdateRequest)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | subscriptions | ArrayList<[SubscriptionsObject](#SubscriptionsObject)>? |  yes  |  |

---


 
 
 #### [EventSubscriptionsBulkUpdateResponse](#EventSubscriptionsBulkUpdateResponse)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | template | [EventSubscriptionTemplate](#EventSubscriptionTemplate)? |  yes  |  |
 | id | String? |  yes  |  |
 | application | String? |  yes  |  |
 | event | String? |  yes  |  |
 | slug | String? |  yes  |  |
 | category | String? |  yes  |  |
 | createdAt | String? |  yes  |  |
 | updatedAt | String? |  yes  |  |
 | v | Int? |  yes  |  |

---


 
 
 #### [SubscriptionsObject](#SubscriptionsObject)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | id | String? |  yes  | Subscription ID |
 | template | [TemplateObject](#TemplateObject)? |  yes  |  |

---


 
 
 #### [TemplateObject](#TemplateObject)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | sms | [CommunicationTemplate](#CommunicationTemplate)? |  yes  |  |
 | email | [CommunicationTemplate](#CommunicationTemplate)? |  yes  |  |
 | pushnotification | [CommunicationTemplate](#CommunicationTemplate)? |  yes  |  |

---


 
 
 #### [CommunicationTemplate](#CommunicationTemplate)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | subscribed | Boolean? |  yes  | Whether the user is subscribed or not |
 | template | String? |  yes  | Template ID |

---


 
 
 #### [AppProvider](#AppProvider)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | email | [AppProviderRes](#AppProviderRes)? |  yes  |  |
 | sms | [AppProviderRes](#AppProviderRes)? |  yes  |  |
 | voice | [AppProviderResVoice](#AppProviderResVoice)? |  yes  |  |
 | id | String? |  yes  |  |
 | application | String? |  yes  |  |
 | createdAt | String? |  yes  |  |
 | updatedAt | String? |  yes  |  |
 | v | Int? |  yes  |  |

---


 
 
 #### [AppProviderRes](#AppProviderRes)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | transaction | [AppProviderResObj](#AppProviderResObj)? |  yes  |  |
 | promotional | [AppProviderResObj](#AppProviderResObj)? |  yes  |  |
 | otp | [AppProviderResObj](#AppProviderResObj)? |  yes  |  |

---


 
 
 #### [AppProviderResVoice](#AppProviderResVoice)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | transaction | [AppProviderResObj](#AppProviderResObj)? |  yes  |  |
 | otp | [AppProviderResObj](#AppProviderResObj)? |  yes  |  |

---


 
 
 #### [AppProviderResObj](#AppProviderResObj)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | provider | String? |  yes  |  |

---


 
 
 #### [GlobalProviders](#GlobalProviders)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | email | ArrayList<[GlobalProvidersResObj](#GlobalProvidersResObj)>? |  yes  |  |
 | sms | ArrayList<[GlobalProvidersResObj](#GlobalProvidersResObj)>? |  yes  |  |
 | voice | ArrayList<[GlobalProvidersResObj](#GlobalProvidersResObj)>? |  yes  |  |

---


 
 
 #### [GlobalProvidersResObj](#GlobalProvidersResObj)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | id | String? |  yes  |  |
 | name | String? |  yes  |  |

---


 
 
 #### [AppProviderReq](#AppProviderReq)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | email | [AppProviderRes](#AppProviderRes)? |  yes  |  |
 | sms | [AppProviderRes](#AppProviderRes)? |  yes  |  |
 | voice | [AppProviderResVoice](#AppProviderResVoice)? |  yes  |  |

---


 
 
 #### [StatsImported](#StatsImported)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | count | Int? |  yes  |  |

---


 
 
 #### [StatsProcessedEmail](#StatsProcessedEmail)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | success | Int? |  yes  |  |
 | failed | Int? |  yes  |  |
 | suppressed | Int? |  yes  |  |

---


 
 
 #### [StatsProcessedSms](#StatsProcessedSms)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | success | Int? |  yes  |  |
 | failed | Int? |  yes  |  |
 | suppressed | Int? |  yes  |  |

---


 
 
 #### [StatsProcessed](#StatsProcessed)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | email | [StatsProcessedEmail](#StatsProcessedEmail)? |  yes  |  |
 | sms | [StatsProcessedSms](#StatsProcessedSms)? |  yes  |  |

---


 
 
 #### [Stats](#Stats)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | id | String? |  yes  |  |
 | imported | Any? |  yes  |  |
 | processed | Any? |  yes  |  |

---


 
 
 #### [GetStats](#GetStats)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | items | ArrayList<[Stats](#Stats)>? |  yes  |  |

---


 
 
 #### [CampaignReq](#CampaignReq)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | description | String? |  yes  |  |
 | tags | ArrayList<String>? |  yes  |  |
 | headers | ArrayList<String>? |  yes  |  |
 | isActive | Boolean? |  yes  |  |
 | name | String? |  yes  |  |
 | fileUrl | String? |  yes  |  |
 | type | String? |  yes  |  |
 | recordsCount | Int? |  yes  |  |
 | application | String? |  yes  |  |

---


 
 
 #### [RecipientHeaders](#RecipientHeaders)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | email | String? |  yes  |  |

---


 
 
 #### [CampaignEmailTemplate](#CampaignEmailTemplate)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | key | String? |  yes  |  |
 | value | String? |  yes  |  |

---


 
 
 #### [CampignEmailProvider](#CampignEmailProvider)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | id | String? |  yes  |  |
 | fromName | String? |  yes  |  |
 | fromEmail | String? |  yes  |  |

---


 
 
 #### [CampaignEmail](#CampaignEmail)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | template | [CampaignEmailTemplate](#CampaignEmailTemplate)? |  yes  |  |
 | provider | [CampignEmailProvider](#CampignEmailProvider)? |  yes  |  |

---


 
 
 #### [Campaign](#Campaign)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | recipientHeaders | [RecipientHeaders](#RecipientHeaders)? |  yes  |  |
 | email | [CampaignEmail](#CampaignEmail)? |  yes  |  |
 | description | String? |  yes  |  |
 | tags | ArrayList<Any>? |  yes  |  |
 | isActive | Boolean? |  yes  |  |
 | id | String? |  yes  |  |
 | datasource | String? |  yes  |  |
 | type | String? |  yes  |  |
 | name | String? |  yes  |  |
 | application | String? |  yes  |  |
 | createdAt | String? |  yes  |  |
 | updatedAt | String? |  yes  |  |
 | slug | String? |  yes  |  |
 | v | Int? |  yes  |  |

---


 
 
 #### [Campaigns](#Campaigns)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | items | ArrayList<[Campaign](#Campaign)>? |  yes  |  |
 | page | [Page](#Page)? |  yes  |  |

---


 
 
 #### [BadRequestSchema](#BadRequestSchema)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | status | String? |  yes  | Response status. |
 | message | String? |  yes  | Failure message. |

---


 
 
 #### [NotFound](#NotFound)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | message | String? |  yes  | Failure message. |

---


 
 
 #### [AudienceReq](#AudienceReq)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | name | String? |  yes  |  |
 | description | String? |  yes  |  |
 | tags | ArrayList<String>? |  yes  |  |
 | fileUrl | String? |  yes  |  |
 | type | String? |  yes  |  |
 | recordsCount | Int? |  yes  |  |
 | headers | ArrayList<String>? |  yes  |  |

---


 
 
 #### [Audience](#Audience)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | id | String? |  yes  |  |
 | application | String? |  yes  |  |
 | name | String? |  yes  |  |
 | description | String? |  yes  |  |
 | recordsCount | Int? |  yes  |  |
 | type | String? |  yes  |  |
 | tags | ArrayList<String>? |  yes  |  |
 | headers | ArrayList<String>? |  yes  |  |
 | fileUrl | String? |  yes  |  |
 | isActive | Boolean? |  yes  |  |
 | createdAt | String? |  yes  |  |
 | updatedAt | String? |  yes  |  |
 | slug | String? |  yes  |  |
 | v | Int? |  yes  |  |

---


 
 
 #### [Audiences](#Audiences)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | items | ArrayList<[Audience](#Audience)>? |  yes  |  |
 | page | [Page](#Page)? |  yes  |  |

---


 
 
 #### [GetNRecordsCsvReq](#GetNRecordsCsvReq)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | url | String? |  yes  |  |
 | header | Boolean? |  yes  |  |
 | count | Int? |  yes  |  |

---


 
 
 #### [GetNRecordsCsvResItems](#GetNRecordsCsvResItems)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | phoneNumber | String? |  yes  |  |
 | email | String? |  yes  |  |
 | firstname | String? |  yes  |  |
 | lastname | String? |  yes  |  |
 | orderid | String? |  yes  |  |

---


 
 
 #### [GetNRecordsCsvRes](#GetNRecordsCsvRes)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | items | ArrayList<[GetNRecordsCsvResItems](#GetNRecordsCsvResItems)>? |  yes  |  |

---


 
 
 #### [DummyDatasources](#DummyDatasources)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | id | Int? |  yes  |  |
 | name | String? |  yes  |  |

---


 
 
 #### [DummyDatasourcesMeta](#DummyDatasourcesMeta)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | id | Int? |  yes  |  |
 | data | [DummyDatasourcesMetaObj](#DummyDatasourcesMetaObj)? |  yes  |  |

---


 
 
 #### [DummyDatasourcesMetaObj](#DummyDatasourcesMetaObj)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | b | Int? |  yes  |  |

---


 
 
 #### [EmailProviderReqFrom](#EmailProviderReqFrom)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | name | String? |  yes  |  |
 | email | String? |  yes  |  |
 | isDefault | Boolean? |  yes  |  |

---


 
 
 #### [EmailProviderReq](#EmailProviderReq)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | name | String? |  yes  |  |
 | description | String? |  yes  |  |
 | apiKey | String? |  yes  |  |
 | type | String? |  yes  |  |
 | provider | String? |  yes  |  |
 | fromAddress | ArrayList<[EmailProviderReqFrom](#EmailProviderReqFrom)>? |  yes  |  |

---


 
 
 #### [EmailProvider](#EmailProvider)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | type | String? |  yes  |  |
 | provider | String? |  yes  |  |
 | fromAddress | ArrayList<[EmailProviderReqFrom](#EmailProviderReqFrom)>? |  yes  |  |
 | id | String? |  yes  |  |
 | name | String? |  yes  |  |
 | description | String? |  yes  |  |
 | apiKey | String? |  yes  |  |
 | application | String? |  yes  |  |
 | createdAt | String? |  yes  |  |
 | updatedAt | String? |  yes  |  |
 | slug | String? |  yes  |  |
 | v | Int? |  yes  |  |

---


 
 
 #### [EmailProviders](#EmailProviders)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | items | ArrayList<[EmailProvider](#EmailProvider)>? |  yes  |  |
 | page | [Page](#Page)? |  yes  |  |

---


 
 
 #### [EmailTemplateKeys](#EmailTemplateKeys)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | to | String? |  yes  |  |
 | cc | String? |  yes  |  |
 | bcc | String? |  yes  |  |

---


 
 
 #### [EmailTemplateHeaders](#EmailTemplateHeaders)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | key | String? |  yes  |  |
 | value | String? |  yes  |  |

---


 
 
 #### [EmailTemplateReq](#EmailTemplateReq)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | name | String |  no  |  |
 | description | String? |  yes  |  |
 | fromName | String? |  yes  |  |
 | staticTo | ArrayList<String>? |  yes  |  |
 | staticCc | ArrayList<String>? |  yes  |  |
 | staticBcc | ArrayList<String>? |  yes  |  |
 | replyTo | String? |  yes  |  |
 | priority | String? |  yes  |  |
 | tags | ArrayList<String>? |  yes  |  |
 | templateVariables | HashMap<String,Any>? |  yes  |  |
 | published | Boolean? |  yes  |  |
 | subject | [TemplateAndType](#TemplateAndType)? |  yes  |  |
 | html | [TemplateAndType](#TemplateAndType)? |  yes  |  |
 | editorType | String? |  yes  |  |
 | editorMeta | String? |  yes  |  |
 | attachments | ArrayList<Int>? |  yes  |  |
 | headers | ArrayList<[EmailTemplateHeaders](#EmailTemplateHeaders)>? |  yes  |  |
 | keys | [EmailTemplateKeys](#EmailTemplateKeys)? |  yes  |  |
 | text | [TemplateAndType](#TemplateAndType)? |  yes  |  |

---


 
 
 #### [TemplateAndType](#TemplateAndType)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | templateType | String? |  yes  |  |
 | template | String? |  yes  |  |

---


 
 
 #### [EmailTemplate](#EmailTemplate)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | application | String? |  yes  |  |
 | isSystem | Boolean? |  yes  |  |
 | isInternal | Boolean? |  yes  |  |
 | name | String? |  yes  |  |
 | description | String? |  yes  |  |
 | editorType | String? |  yes  |  |
 | editorMeta | String? |  yes  |  |
 | staticTo | ArrayList<String>? |  yes  |  |
 | staticCc | ArrayList<String>? |  yes  |  |
 | staticBcc | ArrayList<String>? |  yes  |  |
 | replyTo | String? |  yes  |  |
 | tags | ArrayList<String>? |  yes  |  |
 | subject | [TemplateAndType](#TemplateAndType)? |  yes  |  |
 | html | [TemplateAndType](#TemplateAndType)? |  yes  |  |
 | urlShorten | [EnabledObj](#EnabledObj)? |  yes  |  |
 | priority | String? |  yes  |  |
 | templateVariables | HashMap<String,Any>? |  yes  |  |
 | published | Boolean? |  yes  |  |
 | category | String? |  yes  |  |
 | id | String? |  yes  |  |
 | headers | ArrayList<[EmailTemplateHeaders](#EmailTemplateHeaders)>? |  yes  |  |
 | attachments | ArrayList<Int>? |  yes  |  |
 | createdAt | String? |  yes  |  |
 | updatedAt | String? |  yes  |  |
 | slug | String? |  yes  |  |
 | v | Int? |  yes  |  |
 | fromName | String? |  yes  |  |
 | text | [TemplateAndType](#TemplateAndType)? |  yes  |  |

---


 
 
 #### [SystemEmailTemplate](#SystemEmailTemplate)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | isSystem | Boolean? |  yes  |  |
 | isInternal | Boolean? |  yes  |  |
 | name | String? |  yes  |  |
 | description | String? |  yes  |  |
 | staticTo | ArrayList<String>? |  yes  |  |
 | staticCc | ArrayList<String>? |  yes  |  |
 | staticBcc | ArrayList<String>? |  yes  |  |
 | tags | ArrayList<String>? |  yes  |  |
 | subject | [TemplateAndType](#TemplateAndType)? |  yes  |  |
 | html | [TemplateAndType](#TemplateAndType)? |  yes  |  |
 | urlShorten | [EnabledObj](#EnabledObj)? |  yes  |  |
 | priority | String? |  yes  |  |
 | templateVariables | HashMap<String,Any>? |  yes  |  |
 | published | Boolean? |  yes  |  |
 | category | String? |  yes  |  |
 | id | String? |  yes  |  |
 | headers | ArrayList<[EmailTemplateHeaders](#EmailTemplateHeaders)>? |  yes  |  |
 | attachments | ArrayList<Int>? |  yes  |  |
 | createdAt | String? |  yes  |  |
 | updatedAt | String? |  yes  |  |
 | slug | String? |  yes  |  |
 | v | Int? |  yes  |  |
 | text | [TemplateAndType](#TemplateAndType)? |  yes  |  |

---


 
 
 #### [EmailTemplates](#EmailTemplates)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | items | ArrayList<[EmailTemplate](#EmailTemplate)>? |  yes  |  |
 | page | [Page](#Page)? |  yes  |  |

---


 
 
 #### [SystemEmailTemplates](#SystemEmailTemplates)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | items | ArrayList<[SystemEmailTemplate](#SystemEmailTemplate)>? |  yes  |  |

---


 
 
 #### [PayloadEmailTemplateStructure](#PayloadEmailTemplateStructure)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | key | String? |  yes  |  |
 | value | Any? |  yes  |  |

---


 
 
 #### [PayloadEmailProviderStructure](#PayloadEmailProviderStructure)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | id | String? |  yes  |  |

---


 
 
 #### [PayloadEmailStructure](#PayloadEmailStructure)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | template | [PayloadEmailTemplateStructure](#PayloadEmailTemplateStructure)? |  yes  |  |
 | provider | [PayloadEmailProviderStructure](#PayloadEmailProviderStructure)? |  yes  |  |

---


 
 
 #### [PayloadSmsTemplateStructure](#PayloadSmsTemplateStructure)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | key | String? |  yes  |  |
 | value | Any? |  yes  |  |

---


 
 
 #### [PayloadSmsProviderStructure](#PayloadSmsProviderStructure)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | id | String? |  yes  |  |

---


 
 
 #### [PayloadSmsStructure](#PayloadSmsStructure)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | template | [PayloadSmsTemplateStructure](#PayloadSmsTemplateStructure)? |  yes  |  |
 | provider | [PayloadSmsProviderStructure](#PayloadSmsProviderStructure)? |  yes  |  |

---


 
 
 #### [PayloadStructure](#PayloadStructure)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | data | ArrayList<HashMap<String,Any>>? |  yes  |  |
 | email | [PayloadEmailStructure](#PayloadEmailStructure)? |  yes  |  |
 | sms | [PayloadSmsStructure](#PayloadSmsStructure)? |  yes  |  |
 | application | String? |  yes  |  |

---


 
 
 #### [MetaStructure](#MetaStructure)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | jobType | String? |  yes  |  |
 | action | String? |  yes  |  |
 | trace | String? |  yes  |  |
 | timestamp | String? |  yes  |  |

---


 
 
 #### [EngineRequest](#EngineRequest)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | payload | [PayloadStructure](#PayloadStructure)? |  yes  |  |
 | meta | [MetaStructure](#MetaStructure)? |  yes  |  |

---


 
 
 #### [EngineResponse](#EngineResponse)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | success | Boolean? |  yes  |  |

---


 
 
 #### [EventSubscriptionTemplateSms](#EventSubscriptionTemplateSms)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | subscribed | Boolean? |  yes  |  |
 | template | String? |  yes  |  |

---


 
 
 #### [EventSubscriptionTemplateEmail](#EventSubscriptionTemplateEmail)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | subscribed | Boolean? |  yes  |  |
 | template | String? |  yes  |  |

---


 
 
 #### [EventSubscriptionTemplate](#EventSubscriptionTemplate)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | sms | [EventSubscriptionTemplateSms](#EventSubscriptionTemplateSms)? |  yes  |  |
 | email | [EventSubscriptionTemplateEmail](#EventSubscriptionTemplateEmail)? |  yes  |  |

---


 
 
 #### [EventSubscription](#EventSubscription)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | template | [EventSubscriptionTemplate](#EventSubscriptionTemplate)? |  yes  |  |
 | isDefault | Boolean? |  yes  |  |
 | id | String? |  yes  |  |
 | application | String? |  yes  |  |
 | event | String? |  yes  |  |
 | slug | String? |  yes  |  |
 | createdAt | String? |  yes  |  |
 | updatedAt | String? |  yes  |  |
 | v | Int? |  yes  |  |

---


 
 
 #### [EventSubscriptions](#EventSubscriptions)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | items | ArrayList<[EventSubscription](#EventSubscription)>? |  yes  |  |
 | page | [Page](#Page)? |  yes  |  |

---


 
 
 #### [TriggerJobResponse](#TriggerJobResponse)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | status | Int? |  yes  |  |

---


 
 
 #### [TriggerJobRequest](#TriggerJobRequest)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | jobId | String? |  yes  |  |

---


 
 
 #### [GlobalVariablesGetResponse](#GlobalVariablesGetResponse)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | readOnly | HashMap<String,Any>? |  yes  |  |
 | editable | HashMap<String,Any>? |  yes  |  |

---


 
 
 #### [GlobalVariablesPostResponse](#GlobalVariablesPostResponse)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | id | String? |  yes  |  |
 | category | String? |  yes  |  |
 | application | String? |  yes  |  |
 | globalVariables | HashMap<String,Any>? |  yes  |  |
 | createdAt | String? |  yes  |  |

---


 
 
 #### [GlobalVariablesReq](#GlobalVariablesReq)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | globalVariables | HashMap<String,Any>? |  yes  |  |

---


 
 
 #### [Job](#Job)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | completed | Boolean? |  yes  |  |
 | isActive | Boolean? |  yes  |  |
 | id | String? |  yes  |  |
 | campaign | String? |  yes  |  |
 | application | String? |  yes  |  |
 | createdAt | String? |  yes  |  |
 | updatedAt | String? |  yes  |  |
 | v | Int? |  yes  |  |

---


 
 
 #### [Jobs](#Jobs)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | items | ArrayList<[Job](#Job)>? |  yes  |  |
 | page | [Page](#Page)? |  yes  |  |

---


 
 
 #### [CreateJobsRes](#CreateJobsRes)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | application | String? |  yes  |  |
 | campaign | String? |  yes  |  |
 | completed | Boolean? |  yes  |  |
 | isActive | Boolean? |  yes  |  |
 | id | String? |  yes  |  |
 | createdAt | String? |  yes  |  |
 | updatedAt | String? |  yes  |  |
 | v | Int? |  yes  |  |

---


 
 
 #### [CreateJobsReq](#CreateJobsReq)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | campaign | String? |  yes  |  |

---


 
 
 #### [JobLog](#JobLog)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | imported | Any? |  yes  |  |
 | processed | Any? |  yes  |  |
 | id | String? |  yes  |  |
 | job | String? |  yes  |  |
 | campaign | String? |  yes  |  |
 | createdAt | String? |  yes  |  |
 | updatedAt | String? |  yes  |  |
 | v | Int? |  yes  |  |

---


 
 
 #### [JobLogs](#JobLogs)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | items | ArrayList<[JobLog](#JobLog)>? |  yes  |  |
 | page | [Page](#Page)? |  yes  |  |

---


 
 
 #### [LogEmail](#LogEmail)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | template | String? |  yes  |  |

---


 
 
 #### [LogPushnotification](#LogPushnotification)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | pushtokens | ArrayList<String>? |  yes  |  |

---


 
 
 #### [LogMeta](#LogMeta)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | type | String? |  yes  |  |
 | identifier | String? |  yes  |  |
 | key | String? |  yes  |  |
 | offset | String? |  yes  |  |
 | partition | String? |  yes  |  |
 | topic | String? |  yes  |  |

---


 
 
 #### [Log](#Log)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | email | [LogEmail](#LogEmail)? |  yes  |  |
 | pushnotification | [LogPushnotification](#LogPushnotification)? |  yes  |  |
 | meta | [LogMeta](#LogMeta)? |  yes  |  |
 | id | String? |  yes  |  |
 | application | String? |  yes  |  |
 | service | String? |  yes  |  |
 | step | String? |  yes  |  |
 | status | String? |  yes  |  |
 | data | Any? |  yes  |  |
 | expireAt | String? |  yes  |  |
 | createdAt | String? |  yes  |  |

---


 
 
 #### [Logs](#Logs)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | items | ArrayList<[Log](#Log)>? |  yes  |  |
 | page | [Page](#Page)? |  yes  |  |

---


 
 
 #### [SendOtpSmsCommsTemplate](#SendOtpSmsCommsTemplate)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | key | String? |  yes  |  |
 | value | Any? |  yes  |  |

---


 
 
 #### [SendOtpSmsCommsProvider](#SendOtpSmsCommsProvider)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | slug | String? |  yes  |  |
 | id | String? |  yes  |  |

---


 
 
 #### [SendOtpEmailCommsProvider](#SendOtpEmailCommsProvider)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | slug | String? |  yes  |  |
 | id | String? |  yes  |  |

---


 
 
 #### [SendOtpEmailCommsTemplate](#SendOtpEmailCommsTemplate)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | key | String? |  yes  |  |
 | value | Any? |  yes  |  |

---


 
 
 #### [SendOtpCommsReqData](#SendOtpCommsReqData)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | sendSameOtpToChannel | Boolean? |  yes  |  |
 | mobile | String? |  yes  |  |
 | countryCode | String? |  yes  |  |
 | to | String? |  yes  |  |

---


 
 
 #### [SendOtpCommsReqSms](#SendOtpCommsReqSms)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | otpLength | Int? |  yes  |  |
 | expiry | Int? |  yes  |  |
 | template | [SendOtpSmsCommsTemplate](#SendOtpSmsCommsTemplate)? |  yes  |  |
 | provider | [SendOtpSmsCommsProvider](#SendOtpSmsCommsProvider)? |  yes  |  |

---


 
 
 #### [SendOtpCommsReqEmail](#SendOtpCommsReqEmail)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | otpLength | Int? |  yes  |  |
 | expiry | Int? |  yes  |  |
 | template | [SendOtpEmailCommsTemplate](#SendOtpEmailCommsTemplate)? |  yes  |  |
 | provider | [SendOtpEmailCommsProvider](#SendOtpEmailCommsProvider)? |  yes  |  |

---


 
 
 #### [SendOtpCommsResSms](#SendOtpCommsResSms)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | success | Boolean? |  yes  |  |
 | requestId | String? |  yes  |  |
 | message | String? |  yes  |  |
 | mobile | String? |  yes  |  |
 | countryCode | String? |  yes  |  |
 | resendTimer | Int? |  yes  |  |

---


 
 
 #### [SendOtpCommsResEmail](#SendOtpCommsResEmail)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | success | Boolean? |  yes  |  |
 | requestId | String? |  yes  |  |
 | message | String? |  yes  |  |
 | to | String? |  yes  |  |
 | resendTimer | Int? |  yes  |  |

---


 
 
 #### [SendOtpCommsReq](#SendOtpCommsReq)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | data | [SendOtpCommsReqData](#SendOtpCommsReqData)? |  yes  |  |
 | sms | [SendOtpCommsReqSms](#SendOtpCommsReqSms)? |  yes  |  |
 | email | [SendOtpCommsReqEmail](#SendOtpCommsReqEmail)? |  yes  |  |

---


 
 
 #### [SendOtpCommsRes](#SendOtpCommsRes)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | sms | [SendOtpCommsResSms](#SendOtpCommsResSms)? |  yes  |  |
 | email | [SendOtpCommsResEmail](#SendOtpCommsResEmail)? |  yes  |  |

---


 
 
 #### [VerifyOtpCommsReq](#VerifyOtpCommsReq)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | requestId | String? |  yes  |  |
 | otp | String? |  yes  |  |

---


 
 
 #### [VerifyOtpCommsSuccessRes](#VerifyOtpCommsSuccessRes)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | success | Boolean? |  yes  |  |
 | mobile | String? |  yes  |  |
 | countryCode | String? |  yes  |  |
 | message | String? |  yes  |  |

---


 
 
 #### [VerifyOtpCommsErrorRes](#VerifyOtpCommsErrorRes)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | success | Boolean? |  yes  |  |
 | message | String? |  yes  |  |

---


 
 
 #### [SmsProviderReq](#SmsProviderReq)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | name | String? |  yes  |  |
 | description | String? |  yes  |  |
 | sender | String? |  yes  |  |
 | username | String? |  yes  |  |
 | authkey | String? |  yes  |  |
 | type | String? |  yes  |  |
 | provider | String? |  yes  |  |
 | password | String? |  yes  | The password for the test. |
 | senderid | String? |  yes  | The sender ID for the test. |
 | feedid | String? |  yes  | The feed ID for the test. |
 | entityid | String? |  yes  | The entity ID for the test. |
 | overrideDnd | Boolean? |  yes  | Whether to override Do Not Disturb. |
 | host | String? |  yes  | The host for the test. |
 | port | Int? |  yes  | The port for the test. |
 | entityId | String? |  yes  | The entity ID for the test. |
 | apikey | String? |  yes  | The apikey for the test. |
 | versionId | Int? |  yes  | The version ID for the test. |
 | senderId | String? |  yes  | The sender ID for the test. |
 | apiKey | String? |  yes  | The api_key for the test. |

---


 
 
 #### [SmsProvider](#SmsProvider)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | rpt | Int? |  yes  |  |
 | type | String? |  yes  |  |
 | provider | String? |  yes  |  |
 | id | String? |  yes  |  |
 | name | String? |  yes  |  |
 | description | String? |  yes  |  |
 | sender | String? |  yes  |  |
 | username | String? |  yes  |  |
 | authkey | String? |  yes  |  |
 | application | String? |  yes  |  |
 | createdAt | String? |  yes  |  |
 | updatedAt | String? |  yes  |  |
 | slug | String? |  yes  |  |
 | v | Int? |  yes  |  |

---


 
 
 #### [SmsProviders](#SmsProviders)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | items | ArrayList<[SmsProvider](#SmsProvider)>? |  yes  |  |
 | page | [Page](#Page)? |  yes  |  |

---


 
 
 #### [DefaultSmsProviders](#DefaultSmsProviders)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | id | String? |  yes  |  |
 | name | String? |  yes  |  |
 | isDefault | Boolean? |  yes  |  |

---


 
 
 #### [SmsTemplateMessage](#SmsTemplateMessage)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | templateType | String? |  yes  |  |
 | template | String? |  yes  |  |

---


 
 
 #### [SmsTemplates](#SmsTemplates)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | items | ArrayList<[SmsTemplate](#SmsTemplate)>? |  yes  |  |
 | page | [Page](#Page)? |  yes  |  |

---


 
 
 #### [SmsTemplate](#SmsTemplate)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | urlShorten | [EnabledObj](#EnabledObj)? |  yes  |  |
 | id | String? |  yes  |  |
 | application | String? |  yes  |  |
 | isSystem | Boolean? |  yes  |  |
 | isInternal | Boolean? |  yes  |  |
 | meta | [metaObj](#metaObj)? |  yes  |  |
 | name | String? |  yes  |  |
 | description | String? |  yes  |  |
 | message | [SmsTemplateMessage](#SmsTemplateMessage)? |  yes  |  |
 | priority | String? |  yes  |  |
 | tags | ArrayList<String>? |  yes  |  |
 | templateVariables | HashMap<String,Any>? |  yes  |  |
 | templateId | String? |  yes  |  |
 | published | Boolean? |  yes  |  |
 | category | String? |  yes  |  |
 | createdAt | String? |  yes  |  |
 | updatedAt | String? |  yes  |  |
 | slug | String? |  yes  |  |
 | v | Int? |  yes  |  |

---


 
 
 #### [SystemSmsTemplates](#SystemSmsTemplates)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | urlShorten | [EnabledObj](#EnabledObj)? |  yes  |  |
 | id | String? |  yes  |  |
 | isSystem | Boolean? |  yes  |  |
 | isInternal | Boolean? |  yes  |  |
 | name | String? |  yes  |  |
 | description | String? |  yes  |  |
 | message | [SmsTemplateMessage](#SmsTemplateMessage)? |  yes  |  |
 | priority | String? |  yes  |  |
 | tags | ArrayList<String>? |  yes  |  |
 | templateVariables | HashMap<String,Any>? |  yes  |  |
 | templateId | String? |  yes  |  |
 | published | Boolean? |  yes  |  |
 | category | String? |  yes  |  |
 | createdAt | String? |  yes  |  |
 | updatedAt | String? |  yes  |  |
 | slug | String? |  yes  |  |
 | v | Int? |  yes  |  |

---


 
 
 #### [metaObj](#metaObj)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | type | String? |  yes  |  |
 | isSystem | Boolean? |  yes  |  |
 | template | String? |  yes  |  |

---


 
 
 #### [SmsTemplateReq](#SmsTemplateReq)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | name | String |  no  |  |
 | description | String? |  yes  |  |
 | priority | String? |  yes  |  |
 | templateId | String? |  yes  |  |
 | meta | [metaObj](#metaObj)? |  yes  |  |
 | templateVariables | HashMap<String,Any>? |  yes  |  |
 | published | Boolean? |  yes  |  |
 | message | [SmsTemplateMessage](#SmsTemplateMessage)? |  yes  |  |

---


 
 
 #### [Notification](#Notification)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | title | String? |  yes  |  |
 | body | String? |  yes  |  |
 | subtitle | String? |  yes  |  |
 | icon | String? |  yes  |  |
 | deeplink | String? |  yes  |  |
 | clickAction | String? |  yes  |  |

---


 
 
 #### [SystemNotificationUser](#SystemNotificationUser)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | type | String? |  yes  |  |
 | value | String? |  yes  |  |

---


 
 
 #### [SystemNotification](#SystemNotification)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | notification | [Notification](#Notification)? |  yes  |  |
 | user | [SystemNotificationUser](#SystemNotificationUser)? |  yes  |  |
 | settings | [SystemNotificationUser](#SystemNotificationUser)? |  yes  |  |
 | id | String? |  yes  |  |
 | group | String? |  yes  |  |
 | createdAt | String? |  yes  |  |

---


 
 
 #### [SystemNotifications](#SystemNotifications)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | items | ArrayList<[SystemNotification](#SystemNotification)>? |  yes  |  |
 | lastReadAnchor | Int? |  yes  |  |
 | page | [Page](#Page)? |  yes  |  |

---


 
 
 #### [Page](#Page)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | type | String |  no  |  |
 | size | Int? |  yes  |  |
 | current | Int? |  yes  |  |
 | hasNext | Boolean? |  yes  |  |
 | itemTotal | Int? |  yes  |  |
 | nextId | String? |  yes  |  |
 | hasPrevious | Boolean? |  yes  |  |

---


 
 
 #### [GenericError](#GenericError)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | message | [Message](#Message)? |  yes  |  |
 | sentry | String? |  yes  |  |

---


 
 
 #### [GenericDelete](#GenericDelete)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | message | String? |  yes  |  |
 | acknowledged | Boolean? |  yes  |  |
 | affected | Int? |  yes  |  |
 | operation | String? |  yes  |  |

---


 
 
 #### [Message](#Message)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | message | String? |  yes  |  |
 | success | Boolean? |  yes  |  |
 | info | String? |  yes  |  |
 | operation | String? |  yes  |  |

---


 
 
 #### [EnabledObj](#EnabledObj)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | enabled | Boolean? |  yes  |  |

---


 
 
 #### [OtpConfigurationExpiryDuration](#OtpConfigurationExpiryDuration)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | time | Double |  no  |  |
 | denomination | String |  no  |  |

---


 
 
 #### [OtpConfigurationExpiry](#OtpConfigurationExpiry)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | duration | [OtpConfigurationExpiryDuration](#OtpConfigurationExpiryDuration) |  no  |  |
 | type | String |  no  |  |

---


 
 
 #### [OtpConfiguration](#OtpConfiguration)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | otpLength | Int |  no  |  |
 | type | String |  no  |  |
 | expiry | [OtpConfigurationExpiry](#OtpConfigurationExpiry) |  no  |  |
 | applicationId | String? |  yes  |  |
 | companyId | String? |  yes  |  |

---



