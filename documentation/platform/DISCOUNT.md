



##### [Back to Platform docs](./README.md)

## Discount Methods
Discount

Default
* [getDiscounts](#getdiscounts)
* [createDiscount](#creatediscount)
* [getDiscount](#getdiscount)
* [updateDiscount](#updatediscount)
* [upsertDiscountItems](#upsertdiscountitems)
* [validateDiscountFile](#validatediscountfile)
* [downloadDiscountFile](#downloaddiscountfile)
* [getValidationJob](#getvalidationjob)
* [cancelValidationJob](#cancelvalidationjob)
* [getDownloadJob](#getdownloadjob)
* [cancelDownloadJob](#canceldownloadjob)




## Methods with example and description



### getDiscounts
Fetch discount list.




```python
try:
    result = await platformClient.discount.getDiscounts(view=view, q=q, pageNo=pageNo, pageSize=pageSize, archived=archived, month=month, year=year, type=type, appIds=appIds)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| view | String? | no | listing or calender.  Default is listing. |   
| q | String? | no | The search query. This can be a partial or complete name of a discount. |   
| pageNo | Int? | no | page number. Default is 1. |   
| pageSize | Int? | no | page size. Default is 12. |   
| archived | Boolean? | no | archived. Default is false. |   
| month | Int? | no | month. Default is current month. |   
| year | Int? | no | year. Default is current year. |   
| type | String? | no | basic or custom. |   
| appIds | ArrayList<String>? | no | application ids. |  



Fetch discount list.

*Returned Response:*




[ListOrCalender](#ListOrCalender)

Success




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; success_basic</i></summary>

```json
{
  "value": {
    "items": [
      {
        "is_active": false,
        "app_ids": [
          "646f43ee3b7f8c2847e31fb0"
        ],
        "_id": "xxxxxxxxxxxx",
        "name": "Discount Basic",
        "job_type": "app",
        "discount_type": "percentage",
        "discount_level": "application",
        "company_id": 90,
        "validity": {
          "start": "2021-04-06T08:25:34.110Z",
          "end": "2021-04-22T18:30:00.000Z"
        },
        "value": 0,
        "created_by": {
          "username": "narutouzumaki",
          "user_id": "0"
        },
        "modified_by": {
          "username": "narutouzumaki",
          "user_id": "0"
        },
        "created_on": "2021-04-06T08:10:16.609Z",
        "modified_on": "2021-04-07T08:19:12.007Z",
        "brand_ids": [
          90
        ],
        "store_ids": [
          1001
        ]
      }
    ],
    "page": {
      "current": 1,
      "item_total": 1,
      "type": "number",
      "size": 1,
      "has_previous": true,
      "has_next": false
    }
  }
}
```
</details>

<details>
<summary><i>&nbsp; success_custom</i></summary>

```json
{
  "value": {
    "items": [
      {
        "is_active": false,
        "app_ids": [
          "646f43ee3b7f8c2847e31fb0"
        ],
        "_id": "xxxxxxxxxxxx",
        "name": "Discount",
        "job_type": "app|brand|product",
        "discount_type": "percentage",
        "discount_level": "application",
        "company_id": 90,
        "validity": {
          "start": "2021-04-06T08:25:34.110Z",
          "end": "2021-04-22T18:30:00.000Z"
        },
        "value": 0,
        "file_path": "https://xxx.xxx.xxx/file.xlsx",
        "created_by": {
          "username": "narutouzumaki",
          "user_id": "0"
        },
        "modified_by": {
          "username": "narutouzumaki",
          "user_id": "0"
        },
        "created_on": "2021-04-06T08:10:16.609Z",
        "modified_on": "2021-04-07T08:19:12.007Z",
        "brand_ids": [
          90
        ],
        "store_ids": [
          1001
        ]
      }
    ],
    "page": {
      "current": 1,
      "item_total": 1,
      "type": "number",
      "size": 1,
      "has_previous": true,
      "has_next": false
    }
  }
}
```
</details>

</details>









---


### createDiscount
Create Discount.




```python
try:
    result = await platformClient.discount.createDiscount(body=body)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- |
| body | [CreateUpdateDiscount](#CreateUpdateDiscount) | yes | Request body |


Create Discount.

*Returned Response:*




[DiscountJob](#DiscountJob)

Success




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; success_basic</i></summary>

```json
{
  "value": {
    "_id": "64a7c915c160922f34ba4f12",
    "name": "Contract Discount Name",
    "company_id": 90,
    "is_active": true,
    "app_ids": [
      "646f43ee3b7f8c2847e31fb0"
    ],
    "job_type": "app",
    "discount_type": "flat",
    "discount_level": "application",
    "value": 10,
    "brand_ids": [
      90
    ],
    "store_ids": [
      1001
    ],
    "discount_meta": {
      "timer": true,
      "hours": 20,
      "minutes": 35
    },
    "validity": {
      "start": "2090-04-07T08:19:12.007Z",
      "end": "2090-04-10T08:19:12.007Z"
    },
    "created_on": "2021-04-06T08:19:12.007Z",
    "modified_on": "2021-04-06T08:19:12.007Z",
    "created_by": {
      "username": "narutouzumaki",
      "user_id": "0"
    },
    "modified_by": {
      "username": "narutouzumaki",
      "user_id": "0"
    }
  }
}
```
</details>

<details>
<summary><i>&nbsp; success_custom</i></summary>

```json
{
  "value": {
    "_id": "64a7c915c160922f34ba4f12",
    "name": "Contract Discount Name",
    "company_id": 90,
    "is_active": true,
    "app_ids": [
      "646f43ee3b7f8c2847e31fb0"
    ],
    "job_type": "app",
    "discount_type": "flat",
    "discount_level": "application",
    "value": 10,
    "brand_ids": [
      90
    ],
    "store_ids": [
      1001
    ],
    "discount_meta": {
      "timer": true,
      "hours": 20,
      "minutes": 35
    },
    "validity": {
      "start": "2090-04-07T08:19:12.007Z",
      "end": "2090-04-10T08:19:12.007Z"
    },
    "created_on": "2021-04-06T08:19:12.007Z",
    "modified_on": "2021-04-06T08:19:12.007Z",
    "created_by": {
      "username": "narutouzumaki",
      "user_id": "0"
    },
    "modified_by": {
      "username": "narutouzumaki",
      "user_id": "0"
    }
  }
}
```
</details>

</details>









---


### getDiscount
Fetch discount.




```python
try:
    result = await platformClient.discount.getDiscount(id=id)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| id | String | yes | unique id. |  



Fetch discount.

*Returned Response:*




[DiscountJob](#DiscountJob)

Success




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; success_basic</i></summary>

```json
{
  "value": {
    "_id": "64a7c915c160922f34ba4f12",
    "name": "Discount Name",
    "company_id": 90,
    "is_active": true,
    "app_ids": [
      "646f43ee3b7f8c2847e31fb0"
    ],
    "job_type": "app",
    "discount_type": "flat",
    "discount_level": "application",
    "value": 10,
    "brand_ids": [
      90
    ],
    "store_ids": [
      1001
    ],
    "discount_meta": {
      "timer": true,
      "hours": 20,
      "minutes": 35
    },
    "validity": {
      "start": "2021-04-07T08:19:12.007Z",
      "end": "2021-04-10T08:19:12.007Z"
    },
    "created_on": "2021-04-06T08:19:12.007Z",
    "modified_on": "2021-04-06T08:19:12.007Z",
    "created_by": {
      "username": "narutouzumaki",
      "user_id": "0"
    },
    "modified_by": {
      "username": "narutouzumaki",
      "user_id": "0"
    }
  }
}
```
</details>

<details>
<summary><i>&nbsp; success_custom</i></summary>

```json
{
  "value": {
    "_id": "62c538dd6c0f710007ac6dbf",
    "name": "Discount Name",
    "company_id": 90,
    "is_active": true,
    "app_ids": [
      "646f43ee3b7f8c2847e31fb0"
    ],
    "job_type": "app|brand|product",
    "file_path": "https://xxx.xxx.xxx/file.xlsx",
    "discount_type": "flat",
    "discount_level": "application",
    "value": 10,
    "brand_ids": [
      90
    ],
    "store_ids": [
      1001
    ],
    "discount_meta": {
      "timer": true,
      "hours": 20,
      "minutes": 35
    },
    "validity": {
      "start": "2021-04-07T08:19:12.007Z",
      "end": "2021-04-10T08:19:12.007Z"
    },
    "created_on": "2021-04-06T08:19:12.007Z",
    "modified_on": "2021-04-06T08:19:12.007Z",
    "created_by": {
      "username": "narutouzumaki",
      "user_id": "0"
    },
    "modified_by": {
      "username": "narutouzumaki",
      "user_id": "0"
    }
  }
}
```
</details>

</details>









---


### updateDiscount
Update Discount.




```python
try:
    result = await platformClient.discount.updateDiscount(id=id, body=body)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| id | String | yes | id |  
| body | [CreateUpdateDiscount](#CreateUpdateDiscount) | yes | Request body |


Update Discount.

*Returned Response:*




[DiscountJob](#DiscountJob)

Success




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; success_basic</i></summary>

```json
{
  "value": {
    "_id": "64a7c915c160922f34ba4f12",
    "name": "Discount Name",
    "company_id": 90,
    "is_active": true,
    "app_ids": [
      "646f43ee3b7f8c2847e31fb0"
    ],
    "job_type": "app",
    "discount_type": "flat",
    "discount_level": "application",
    "value": 10,
    "brand_ids": [
      90
    ],
    "store_ids": [
      1001
    ],
    "discount_meta": {
      "timer": true,
      "hours": 20,
      "minutes": 35
    },
    "validity": {
      "start": "2021-04-07T08:19:12.007Z",
      "end": "2021-04-10T08:19:12.007Z"
    },
    "created_by": {
      "username": "narutouzumaki",
      "user_id": "0"
    },
    "modified_by": {
      "username": "narutouzumaki",
      "user_id": "0"
    }
  }
}
```
</details>

<details>
<summary><i>&nbsp; success_custom</i></summary>

```json
{
  "value": {
    "_id": "64a7c915c160922f34ba4f12",
    "name": "Discount Name",
    "company_id": 90,
    "is_active": true,
    "app_ids": [
      "646f43ee3b7f8c2847e31fb0"
    ],
    "job_type": "app",
    "discount_type": "flat",
    "discount_level": "application",
    "file_path": "https://xxx.xxx.xxx/file.xlsx",
    "value": 10,
    "brand_ids": [
      90
    ],
    "store_ids": [
      1001
    ],
    "discount_meta": {
      "timer": true,
      "hours": 20,
      "minutes": 35
    },
    "validity": {
      "start": "2021-04-07T08:19:12.007Z",
      "end": "2021-04-10T08:19:12.007Z"
    },
    "created_by": {
      "username": "narutouzumaki",
      "user_id": "0"
    },
    "modified_by": {
      "username": "narutouzumaki",
      "user_id": "0"
    }
  }
}
```
</details>

</details>









---


### upsertDiscountItems
Create custom discount from bulk.




```python
try:
    result = await platformClient.discount.upsertDiscountItems(id=id, body=body)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| id | String | yes | Job ID of the discount. |  
| body | [BulkDiscount](#BulkDiscount) | yes | Request body |


Create custom discounts through API.

*Returned Response:*




[HashMap<String,Any>](#HashMap<String,Any>)

Success




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; success_product</i></summary>

```json
{
  "value": {
    "success": true
  }
}
```
</details>

<details>
<summary><i>&nbsp; success_inventory</i></summary>

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


### validateDiscountFile
Validate File.




```python
try:
    result = await platformClient.discount.validateDiscountFile(discount=discount, body=body)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| discount | String? | no | discount |  
| body | [FileJobRequest](#FileJobRequest) | yes | Request body |


Validate File.

*Returned Response:*




[FileJobResponse](#FileJobResponse)

Success




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; success</i></summary>

```json
{
  "value": {
    "_id": "xxxxxxxxxxxx",
    "stage": "processing",
    "total": 10,
    "failed": 0,
    "company_id": 90,
    "file_path": "https://xxx.xxx.xxx/file.xlsx",
    "body": {
      "is_active": false,
      "app_ids": [
        "646f43ee3b7f8c2847e31fb0"
      ],
      "_id": "xxxxxxxxxxxx",
      "name": "Discount",
      "job_type": "app|brand|product",
      "discount_type": "percentage",
      "discount_level": "application",
      "company_id": 90,
      "file_path": "https://xxx.xxx.xxx/file.xlsx",
      "validity": {
        "start": "2090-04-06T08:25:34.110Z",
        "end": "2090-04-22T18:30:00.000Z"
      },
      "value": null,
      "created_by": {
        "username": "narutouzumaki",
        "user_id": "0"
      },
      "modified_by": {
        "username": "narutouzumaki",
        "user_id": "0"
      },
      "created_on": "2021-04-06T08:10:16.609Z",
      "modified_on": "2021-04-07T08:19:12.007Z",
      "brand_ids": [
        90
      ],
      "store_ids": [
        1001
      ]
    },
    "type": "download",
    "file_type": "product"
  }
}
```
</details>

</details>









---


### downloadDiscountFile
Validate File.




```python
try:
    result = await platformClient.discount.downloadDiscountFile(type=type, body=body)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| type | String | yes | type |  
| body | [DownloadFileJob](#DownloadFileJob) | yes | Request body |


Validate File.

*Returned Response:*




[FileJobResponse](#FileJobResponse)

Success




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; success</i></summary>

```json
{
  "value": {
    "_id": "xxxxxxxxxxxx",
    "stage": "processing",
    "total": 10,
    "failed": 0,
    "company_id": 90,
    "file_path": "https://xxx.xxx.xxx/file.xlsx",
    "body": {
      "is_active": false,
      "app_ids": [
        "646f43ee3b7f8c2847e31fb0"
      ],
      "_id": "xxxxxxxxxxxx",
      "name": "Discount",
      "job_type": "app",
      "discount_type": "percentage",
      "discount_level": "application",
      "company_id": 90,
      "file_path": "https://xxx.xxx.xxx/file.xlsx",
      "validity": {
        "start": "2021-04-06T08:25:34.110Z",
        "end": "2021-04-22T18:30:00.000Z"
      },
      "value": null,
      "created_by": {
        "username": "narutouzumaki",
        "user_id": "0"
      },
      "modified_by": {
        "username": "narutouzumaki",
        "user_id": "0"
      },
      "created_on": "2021-04-06T08:10:16.609Z",
      "modified_on": "2021-04-07T08:19:12.007Z",
      "brand_ids": [
        90
      ],
      "store_ids": [
        1001
      ]
    },
    "type": "download",
    "file_type": "product"
  }
}
```
</details>

</details>









---


### getValidationJob
Validate File Job.




```python
try:
    result = await platformClient.discount.getValidationJob(id=id)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| id | String | yes | id |  



Validate File Job.

*Returned Response:*




[FileJobResponse](#FileJobResponse)

Success




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; success</i></summary>

```json
{
  "value": {
    "_id": "6519669e7fc0cd03ce111ab9",
    "stage": "processing",
    "total": 10,
    "failed": 0,
    "company_id": 90,
    "file_path": "https://xxx.xxx.xxx/file.xlsx",
    "body": {
      "is_active": false,
      "app_ids": [
        "646f43ee3b7f8c2847e31fb0"
      ],
      "_id": "64a7c915c160922f34ba4f12",
      "name": "Discount",
      "job_type": "app",
      "discount_type": "percentage",
      "discount_level": "application",
      "company_id": 90,
      "file_path": "https://xxx.xxx.xxx/file.xlsx",
      "validity": {
        "start": "2021-04-06T08:25:34.110Z",
        "end": "2021-04-22T18:30:00.000Z"
      },
      "value": null,
      "created_by": {
        "username": "narutouzumaki",
        "user_id": "0"
      },
      "modified_by": {
        "username": "narutouzumaki",
        "user_id": "0"
      },
      "created_on": "2021-04-06T08:10:16.609Z",
      "modified_on": "2021-04-07T08:19:12.007Z",
      "brand_ids": [
        90
      ],
      "store_ids": [
        1001
      ]
    },
    "type": "download",
    "file_type": "product"
  }
}
```
</details>

</details>









---


### cancelValidationJob
Cancel Validation Job.




```python
try:
    result = await platformClient.discount.cancelValidationJob(id=id)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| id | String | yes | id |  



Cancel Validation Job.

*Returned Response:*




[CancelJobResponse](#CancelJobResponse)

Success




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; success</i></summary>

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


### getDownloadJob
Download File Job.




```python
try:
    result = await platformClient.discount.getDownloadJob(id=id)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| id | String | yes | id |  



Download File Job.

*Returned Response:*




[FileJobResponse](#FileJobResponse)

Success




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; success</i></summary>

```json
{
  "value": {
    "_id": "651b00ef29aedf98f98a8cbd",
    "stage": "processing",
    "total": 10,
    "failed": 0,
    "company_id": 90,
    "file_path": "https://xxx.xxx.xxx/file.xlsx",
    "body": {
      "is_active": false,
      "app_ids": [
        "646f43ee3b7f8c2847e31fb0"
      ],
      "_id": "64a7c915c160922f34ba4f12",
      "name": "Discount",
      "job_type": "app",
      "discount_type": "percentage",
      "discount_level": "application",
      "company_id": 90,
      "file_path": "https://xxx.xxx.xxx/file.xlsx",
      "validity": {
        "start": "2021-04-06T08:25:34.110Z",
        "end": "2021-04-22T18:30:00.000Z"
      },
      "value": null,
      "created_by": {
        "username": "narutouzumaki",
        "user_id": "0"
      },
      "modified_by": {
        "username": "narutouzumaki",
        "user_id": "0"
      },
      "created_on": "2021-04-06T08:10:16.609Z",
      "modified_on": "2021-04-07T08:19:12.007Z",
      "brand_ids": [
        90
      ],
      "store_ids": [
        1001
      ]
    },
    "type": "download",
    "file_type": "product"
  }
}
```
</details>

</details>









---


### cancelDownloadJob
Cancel Download Job.




```python
try:
    result = await platformClient.discount.cancelDownloadJob(id=id)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| id | String | yes | id |  



Cancel Download Job.

*Returned Response:*




[CancelJobResponse](#CancelJobResponse)

Success




<details>
<summary><i>&nbsp; Examples:</i></summary>


<details>
<summary><i>&nbsp; success</i></summary>

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




### Schemas

 
 
 #### [ValidityObject](#ValidityObject)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | start | String |  no  |  |
 | end | String |  no  |  |

---


 
 
 #### [CreateUpdateDiscount](#CreateUpdateDiscount)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | name | String |  no  |  |
 | companyId | Int |  no  |  |
 | isActive | Boolean |  no  |  |
 | appIds | ArrayList<String> |  no  |  |
 | extensionIds | ArrayList<String>? |  yes  |  |
 | jobType | String |  no  |  |
 | discountType | String |  no  |  |
 | discountLevel | String |  no  |  |
 | value | Int? |  yes  |  |
 | filePath | String? |  yes  |  |
 | brandIds | ArrayList<Int>? |  yes  |  |
 | storeIds | ArrayList<Int>? |  yes  |  |
 | zoneIds | ArrayList<String>? |  yes  |  |
 | validity | [ValidityObject](#ValidityObject) |  no  |  |
 | discountMeta | [DiscountMeta](#DiscountMeta)? |  yes  |  |

---


 
 
 #### [DiscountMeta](#DiscountMeta)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | timer | Boolean |  no  | Determines whether the discount countdown is visible or not. |
 | hours | Double? |  yes  | The time in hours before the discount ends when the countdown timer should start. |
 | minutes | Double? |  yes  | The time in minutes before the discount ends when the countdown timer should start. |

---


 
 
 #### [DiscountJob](#DiscountJob)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | id | String |  no  |  |
 | name | String |  no  |  |
 | companyId | Int |  no  |  |
 | isActive | Boolean |  no  |  |
 | appIds | ArrayList<String>? |  yes  |  |
 | jobType | String? |  yes  |  |
 | discountType | String? |  yes  |  |
 | discountLevel | String? |  yes  |  |
 | value | Int? |  yes  |  |
 | filePath | String? |  yes  |  |
 | brandIds | ArrayList<Int>? |  yes  |  |
 | storeIds | ArrayList<Int>? |  yes  |  |
 | zoneIds | ArrayList<String>? |  yes  |  |
 | discountMeta | [DiscountMeta](#DiscountMeta)? |  yes  |  |
 | validity | [ValidityObject](#ValidityObject) |  no  |  |
 | createdOn | String |  no  |  |
 | modifiedOn | String |  no  |  |
 | createdBy | [UserDetails](#UserDetails) |  no  |  |
 | modifiedBy | [UserDetails](#UserDetails) |  no  |  |
 | meta | HashMap<String,Any>? |  yes  |  |

---


 
 
 #### [FileJobBody](#FileJobBody)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | name | String? |  yes  |  |
 | companyId | Int? |  yes  |  |
 | isActive | Boolean? |  yes  |  |
 | appIds | ArrayList<String>? |  yes  |  |
 | jobType | String? |  yes  |  |
 | discountType | String? |  yes  |  |
 | discountLevel | String? |  yes  |  |
 | value | Int? |  yes  |  |
 | filePath | String? |  yes  |  |
 | brandIds | ArrayList<Int>? |  yes  |  |
 | storeIds | ArrayList<Int>? |  yes  |  |
 | extensionIds | ArrayList<String>? |  yes  |  |
 | zoneIds | ArrayList<String>? |  yes  |  |
 | discountMeta | [DiscountMeta](#DiscountMeta)? |  yes  |  |
 | validity | [ValidityObject](#ValidityObject)? |  yes  |  |
 | createdOn | String? |  yes  |  |
 | modifiedOn | String? |  yes  |  |
 | createdBy | [UserDetails](#UserDetails)? |  yes  |  |
 | modifiedBy | [UserDetails](#UserDetails)? |  yes  |  |
 | meta | HashMap<String,Any>? |  yes  |  |

---


 
 
 #### [ListOrCalender](#ListOrCalender)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | items | ArrayList<[DiscountJob](#DiscountJob)> |  no  |  |
 | page | [Page](#Page) |  no  |  |

---


 
 
 #### [DiscountItems](#DiscountItems)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | itemCode | String? |  yes  |  |
 | brandName | String? |  yes  |  |
 | sellerIdentifier | String? |  yes  |  |
 | discountType | String |  no  |  |
 | value | Double |  no  |  |
 | discountMeta | [DiscountMeta](#DiscountMeta)? |  yes  |  |

---


 
 
 #### [BulkDiscount](#BulkDiscount)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | companyId | Int |  no  |  |
 | items | ArrayList<[DiscountItems](#DiscountItems)> |  no  |  |

---


 
 
 #### [FileJobResponse](#FileJobResponse)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | stage | String |  no  |  |
 | total | Int |  no  |  |
 | failed | Int |  no  |  |
 | companyId | Int |  no  |  |
 | body | [FileJobBody](#FileJobBody)? |  yes  |  |
 | type | String |  no  |  |
 | fileType | String? |  yes  |  |
 | id | String |  no  | A unique identifier to distinguish and identify a job. |
 | filePath | String? |  yes  |  |
 | progress | Int? |  yes  |  |
 | extensionIds | ArrayList<String>? |  yes  |  |
 | zoneIds | ArrayList<String>? |  yes  |  |
 | createdOn | String? |  yes  |  |
 | modifiedOn | String? |  yes  |  |
 | createdBy | [UserDetails](#UserDetails)? |  yes  |  |

---


 
 
 #### [FileJobRequest](#FileJobRequest)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | name | String |  no  |  |
 | isActive | Boolean |  no  |  |
 | companyId | Int |  no  |  |
 | appIds | ArrayList<String>? |  yes  |  |
 | jobType | String? |  yes  |  |
 | discountType | String? |  yes  |  |
 | discountLevel | String? |  yes  |  |
 | filePath | String? |  yes  |  |
 | brandIds | ArrayList<Int>? |  yes  |  |
 | storeIds | ArrayList<Int>? |  yes  |  |
 | validity | [ValidityObject](#ValidityObject) |  no  |  |
 | meta | HashMap<String,Any>? |  yes  |  |

---


 
 
 #### [DownloadFileJob](#DownloadFileJob)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | brandIds | ArrayList<Int>? |  yes  |  |
 | storeIds | ArrayList<Int>? |  yes  |  |

---


 
 
 #### [CancelJobResponse](#CancelJobResponse)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | success | Boolean |  no  |  |

---


 
 
 #### [Page](#Page)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | itemTotal | Int? |  yes  |  |
 | nextId | String? |  yes  |  |
 | hasPrevious | Boolean? |  yes  |  |
 | hasNext | Boolean? |  yes  |  |
 | current | Int? |  yes  |  |
 | type | String |  no  |  |
 | size | Int? |  yes  |  |

---


 
 
 #### [UserDetails](#UserDetails)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | username | String |  no  |  |
 | userId | String |  no  |  |

---


 
 
 #### [BadRequestObject](#BadRequestObject)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | message | String |  no  |  |

---


 
 
 #### [BadRequestData](#BadRequestData)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | message | String? |  yes  |  |

---


 
 
 #### [BadRequestObjectGet](#BadRequestObjectGet)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | message | String? |  yes  |  |
 | error | String? |  yes  |  |
 | data | [BadRequestData](#BadRequestData)? |  yes  |  |

---



