



##### [Back to Platform docs](./README.md)

## Orders Methods
Handles all platform order and shipment api(s)
* [getShipmentDetails](#getshipmentdetails)
* [getLaneConfig](#getlaneconfig)
* [getOrderShipmentDetails](#getordershipmentdetails)
* [getShipmentList](#getshipmentlist)
* [getShipmentToManifest](#getshipmenttomanifest)
* [getOrders](#getorders)
* [getMetricCount](#getmetriccount)
* [getfilters](#getfilters)
* [getApplicationShipments](#getapplicationshipments)
* [createShipmentReport](#createshipmentreport)
* [getReportsShipmentListing](#getreportsshipmentlisting)
* [upsertJioCode](#upsertjiocode)



## Methods with example and description


### getShipmentDetails





```python
try:
    result = await client.orders.getShipmentDetails(shipmentId=shipmentId, orderingCompanyId=orderingCompanyId, requestByExt=requestByExt)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| shipmentId | String | yes |  |   
| orderingCompanyId | String? | no |  |   
| requestByExt | String? | no |  |  





*Returned Response:*




[ShipmentInfoResponse](#ShipmentInfoResponse)

We are processing the report!




<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
  "success": true,
  "order": {
    "fynd_order_id": "FY62B13E2101810C19E4",
    "shipment_count": 1,
    "order_date": "2022-06-21T09:12:26+00:00"
  },
  "shipments": [
    {
      "shipment_id": "16557829457641286433",
      "payment_mode": "COD",
      "fulfilling_store": {
        "id": 1,
        "code": "HS-468a5",
        "fulfillment_channel": "pulse",
        "store_name": "Reliance Industries Ltd - Jio Market",
        "contact_person": "",
        "phone": "8268108880",
        "address": "high_street WEWORK, VIJAY DIAMONDS, ANDHERI MUMBAI MAHARASHTRA 400093",
        "city": "MUMBAI",
        "state": "MAHARASHTRA",
        "country": "INDIA",
        "pincode": 400093
      },
      "delivery_details": {
        "name": "Manish Prakash",
        "email": "Manish.Prakash@ril.com",
        "phone": "7787051611",
        "address": "home 479 sector3 bokaro Bokaro Jharkhand 827003",
        "city": "Bokaro",
        "state": "Jharkhand",
        "country": "India",
        "pincode": "827003",
        "state_code": 0
      },
      "billing_details": {
        "name": "Manish Prakash",
        "email": "Manish.Prakash@ril.com",
        "phone": "7787051611",
        "address": "home 479 sector3 bokaro Bokaro Jharkhand 827003",
        "city": "Bokaro",
        "state": "Jharkhand",
        "country": "India",
        "pincode": "827003",
        "state_code": 0
      },
      "dp_details": {
        "id": null,
        "name": null,
        "awb_no": null,
        "eway_bill_id": null,
        "track_url": null,
        "gst_tag": "sgst"
      },
      "journey_type": "forward",
      "order": {
        "fynd_order_id": "FY62B13E2101810C19E4",
        "affiliate_id": "000000000000000000000001",
        "ordering_channel": "FYND",
        "source": null,
        "tax_details": {
          "gstin": null
        },
        "order_date": "2022-06-21T09:12:26+00:00"
      },
      "gst_details": {
        "value_of_good": 475.24,
        "gst_fee": 23.76,
        "brand_calculated_amount": 499,
        "tax_collected_at_source": 0,
        "gstin_code": null
      },
      "shipment_quantity": 1,
      "bag_status_history": [
        {
          "status": "pending",
          "updated_at": "2022-06-21T09:12:26+00:00",
          "state_type": "operational",
          "app_display_name": "Pending",
          "display_name": "Pending",
          "forward": null
        },
        {
          "status": "placed",
          "updated_at": "2022-06-21T09:12:32+00:00",
          "state_type": "operational",
          "app_display_name": "Ordered",
          "display_name": "Placed",
          "forward": null
        },
        {
          "status": "bag_confirmed",
          "updated_at": "2022-06-21T09:39:13+00:00",
          "state_type": "operational",
          "app_display_name": "Ordered",
          "display_name": "Bag Confirmed",
          "forward": null
        },
        {
          "status": "dp_assigned",
          "updated_at": "2022-06-21T09:40:04+00:00",
          "state_type": "operational",
          "app_display_name": "DP Assigned",
          "display_name": "DP Assigned",
          "forward": null
        },
        {
          "status": "bag_picked",
          "updated_at": "2022-06-21T09:40:12+00:00",
          "state_type": "operational",
          "app_display_name": "Shipped",
          "display_name": "In Transit",
          "forward": null
        },
        {
          "status": "out_for_delivery",
          "updated_at": "2022-06-21T09:40:29+00:00",
          "state_type": "operational",
          "app_display_name": "Out For Delivery",
          "display_name": "Out For Delivery",
          "forward": null
        },
        {
          "status": "delivery_done",
          "updated_at": "2022-06-21T09:40:37+00:00",
          "state_type": "operational",
          "app_display_name": "Delivered",
          "display_name": "Delivery Done",
          "forward": null
        }
      ],
      "bags": [
        {
          "bag_id": 43880,
          "display_name": "Bag",
          "entity_type": "bag",
          "bag_configs": {
            "is_returnable": true,
            "can_be_cancelled": true,
            "enable_tracking": false,
            "is_customer_return_allowed": true,
            "allow_force_return": false,
            "is_active": false
          },
          "financial_breakup": [
            {
              "price_effective": 499,
              "discount": 0,
              "amount_paid": 549,
              "coupon_effective_discount": 0,
              "delivery_charge": 50,
              "fynd_credits": 0,
              "cod_charges": 0,
              "refund_credit": 0,
              "cashback": 0,
              "refund_amount": 549,
              "added_to_fynd_cash": false,
              "cashback_applied": 0,
              "gst_tax_percentage": 5,
              "value_of_good": 475.24,
              "price_marked": 499,
              "transfer_price": 0,
              "brand_calculated_amount": 499,
              "promotion_effective_discount": 0,
              "coupon_value": 0,
              "pm_price_split": {
                "COD": 549
              },
              "size": "5",
              "total_units": 1,
              "hsn_code": "62050000",
              "identifiers": {
                "sku_code": "CL-001L-L-PRPL-PINK-5"
              },
              "item_name": "Purple Flip Flops",
              "gst_fee": "23.76",
              "gst_tag": "IGST"
            }
          ],
          "current_status": "delivery_done",
          "item": {
            "name": "Purple Flip Flops",
            "brand": "Nike",
            "slug_key": "purple-flip-flops-ezmucvw4d3",
            "images": [
              "https://hdn-1.fynd.com/products/pictures/item/free/270x0/CL-001L-L-PRPL-PINK-6/Rvk5WbGg9Hx-1.jpg"
            ],
            "size": "5",
            "l1_category": "",
            "l3_category": "27"
          },
          "brand": {
            "modified_on": 1655707988,
            "logo": "https://hdn-1.jiomarketx0.de/x0/brands/pictures/square-logo/original/DbhIvd_tB-Logo.jpeg",
            "brand_name": "Nike",
            "company": null,
            "created_on": 1647793418,
            "id": 4
          },
          "gst_details": {
            "gstin_code": null,
            "gst_tag": "IGST",
            "hsn_code": "62050000",
            "value_of_good": 475.24,
            "gst_tax_percentage": 5,
            "is_default_hsn_code": true,
            "brand_calculated_amount": 499,
            "gst_fee": "23.76"
          },
          "article": {
            "uid": "6237fdfec0903e7ae543c201",
            "identifiers": {
              "sku_code": "CL-001L-L-PRPL-PINK-5"
            },
            "return_config": {
              "time": 30,
              "unit": "days",
              "returnable": true
            }
          },
          "quantity": 1
        }
      ],
      "delivery_slot": {
        "slot": "By 03:00 AM",
        "upper_bound": "2022-06-21T03:42:23+00:00",
        "lower_bound": "2022-06-21T03:42:23+00:00",
        "date": "2022-06-21T03:42:23+00:00",
        "type": "order_window"
      },
      "total_items": 1,
      "payment_methods": [
        {
          "slug": "COD",
          "payment_id": "COD",
          "payment_amt": 549,
          "payment_cart": null,
          "payment_desc": "COD",
          "bdcustomer_id": null,
          "order_inv_num": null,
          "mode_of_payment": "COD",
          "payment_gateway_logo": null,
          "transaction_ref_number": ""
        }
      ],
      "vertical": "GROCERIES",
      "payments": {
        "mode": "COD",
        "logo": "https://hdn-1.fynd.com/payment/Pos+Logo.png",
        "source": "Jio Partner Pay"
      },
      "priority_text": null,
      "status": {
        "created_at": 1655804437,
        "shipment_id": "16557829457641286433",
        "status": "delivery_done",
        "bag_list": [
          "43880"
        ],
        "id": 19980
      },
      "prices": {
        "amount_paid": 549,
        "refund_amount": 549,
        "price_marked": 499,
        "cod_charges": 0,
        "discount": 0,
        "cashback_applied": 0,
        "delivery_charge": 50,
        "fynd_credits": 0,
        "cashback": 0,
        "price_effective": 499,
        "refund_credit": 0,
        "value_of_good": 475.24,
        "pm_price_split": {
          "COD": 549
        },
        "brand_calculated_amount": 499,
        "coupon_effective_discount": 0,
        "tax_collected_at_source": 0,
        "promotion_effective_discount": 0
      },
      "picked_date": "",
      "tracking_list": [
        {
          "status": "Order Placed",
          "time": "2022-06-21T09:12:32+00:00",
          "is_passed": true,
          "is_current": false
        },
        {
          "status": "Order Confirmed",
          "time": "2022-06-21T09:39:13+00:00",
          "is_passed": true,
          "is_current": false
        },
        {
          "status": "Invoiced",
          "time": "2022-06-21T09:40:12+00:00",
          "is_passed": true,
          "is_current": false
        },
        {
          "status": "Delivery Partner Assigned",
          "time": "2022-06-21T09:40:12+00:00",
          "is_passed": true,
          "is_current": false
        },
        {
          "status": "Packed",
          "time": "2022-06-21T09:40:12+00:00",
          "is_passed": true,
          "is_current": false
        },
        {
          "status": "In Transit",
          "time": "2022-06-21T09:40:12+00:00",
          "is_passed": true,
          "is_current": false
        },
        {
          "status": "Out For Delivery",
          "time": "2022-06-21T09:40:29+00:00",
          "is_passed": true,
          "is_current": false
        },
        {
          "status": "Delivered",
          "time": "2022-06-21T09:40:37+00:00",
          "is_passed": true,
          "is_current": true
        }
      ],
      "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
      "platform_logo": "https://fynd-static.s3.amazonaws.com/mode_of_payment/fynd_logo.png",
      "packaging_type": "POLYB_DFLT_L"
    }
  ]
}
```
</details>









---


### getLaneConfig





```python
try:
    result = await client.orders.getLaneConfig(superLane=superLane, groupEntity=groupEntity, fromDate=fromDate, toDate=toDate, dpIds=dpIds, stores=stores, salesChannel=salesChannel, paymentMode=paymentMode, bagStatus=bagStatus)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| superLane | String? | no |  |   
| groupEntity | String? | no |  |   
| fromDate | String? | no |  |   
| toDate | String? | no |  |   
| dpIds | String? | no |  |   
| stores | String? | no |  |   
| salesChannel | String? | no |  |   
| paymentMode | String? | no |  |   
| bagStatus | String? | no |  |  





*Returned Response:*




[LaneConfigResponse](#LaneConfigResponse)

Response containing count of shipments of the given status




<details>
<summary><i>&nbsp; Example:</i></summary>

```json

```
</details>









---


### getOrderShipmentDetails





```python
try:
    result = await client.orders.getOrderShipmentDetails(orderId=orderId)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| orderId | String | yes |  |  





*Returned Response:*




[ShipmentDetailsResponse](#ShipmentDetailsResponse)

We are processing the report!




<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
  "success": true,
  "order": {
    "fynd_order_id": "FY62B13E2101810C19E4",
    "shipment_count": 1,
    "order_date": "2022-06-21T09:12:26+00:00"
  },
  "shipments": [
    {
      "shipment_id": "16557829457641286433",
      "payment_mode": "COD",
      "fulfilling_store": {
        "id": 1,
        "code": "HS-468a5",
        "fulfillment_channel": "pulse",
        "store_name": "Reliance Industries Ltd - Jio Market",
        "contact_person": "",
        "phone": "8268108880",
        "address": "high_street WEWORK, VIJAY DIAMONDS, ANDHERI MUMBAI MAHARASHTRA 400093",
        "city": "MUMBAI",
        "state": "MAHARASHTRA",
        "country": "INDIA",
        "pincode": 400093
      },
      "delivery_details": {
        "name": "Manish Prakash",
        "email": "Manish.Prakash@ril.com",
        "phone": "7787051611",
        "address": "home 479 sector3 bokaro Bokaro Jharkhand 827003",
        "city": "Bokaro",
        "state": "Jharkhand",
        "country": "India",
        "pincode": "827003",
        "state_code": 0
      },
      "billing_details": {
        "name": "Manish Prakash",
        "email": "Manish.Prakash@ril.com",
        "phone": "7787051611",
        "address": "home 479 sector3 bokaro Bokaro Jharkhand 827003",
        "city": "Bokaro",
        "state": "Jharkhand",
        "country": "India",
        "pincode": "827003",
        "state_code": 0
      },
      "dp_details": {
        "id": null,
        "name": null,
        "awb_no": null,
        "eway_bill_id": null,
        "track_url": null,
        "gst_tag": "sgst"
      },
      "journey_type": "forward",
      "order": {
        "fynd_order_id": "FY62B13E2101810C19E4",
        "affiliate_id": "000000000000000000000001",
        "ordering_channel": "FYND",
        "source": null,
        "tax_details": {
          "gstin": null
        },
        "order_date": "2022-06-21T09:12:26+00:00"
      },
      "gst_details": {
        "value_of_good": 475.24,
        "gst_fee": 23.76,
        "brand_calculated_amount": 499,
        "tax_collected_at_source": 0,
        "gstin_code": null
      },
      "shipment_quantity": 1,
      "bag_status_history": [
        {
          "status": "pending",
          "updated_at": "2022-06-21T09:12:26+00:00",
          "state_type": "operational",
          "app_display_name": "Pending",
          "display_name": "Pending",
          "forward": null
        },
        {
          "status": "placed",
          "updated_at": "2022-06-21T09:12:32+00:00",
          "state_type": "operational",
          "app_display_name": "Ordered",
          "display_name": "Placed",
          "forward": null
        },
        {
          "status": "bag_confirmed",
          "updated_at": "2022-06-21T09:39:13+00:00",
          "state_type": "operational",
          "app_display_name": "Ordered",
          "display_name": "Bag Confirmed",
          "forward": null
        },
        {
          "status": "dp_assigned",
          "updated_at": "2022-06-21T09:40:04+00:00",
          "state_type": "operational",
          "app_display_name": "DP Assigned",
          "display_name": "DP Assigned",
          "forward": null
        },
        {
          "status": "bag_picked",
          "updated_at": "2022-06-21T09:40:12+00:00",
          "state_type": "operational",
          "app_display_name": "Shipped",
          "display_name": "In Transit",
          "forward": null
        },
        {
          "status": "out_for_delivery",
          "updated_at": "2022-06-21T09:40:29+00:00",
          "state_type": "operational",
          "app_display_name": "Out For Delivery",
          "display_name": "Out For Delivery",
          "forward": null
        },
        {
          "status": "delivery_done",
          "updated_at": "2022-06-21T09:40:37+00:00",
          "state_type": "operational",
          "app_display_name": "Delivered",
          "display_name": "Delivery Done",
          "forward": null
        }
      ],
      "bags": [
        {
          "bag_id": 43880,
          "display_name": "Bag",
          "entity_type": "bag",
          "bag_configs": {
            "is_returnable": true,
            "can_be_cancelled": true,
            "enable_tracking": false,
            "is_customer_return_allowed": true,
            "allow_force_return": false,
            "is_active": false
          },
          "financial_breakup": [
            {
              "price_effective": 499,
              "discount": 0,
              "amount_paid": 549,
              "coupon_effective_discount": 0,
              "delivery_charge": 50,
              "fynd_credits": 0,
              "cod_charges": 0,
              "refund_credit": 0,
              "cashback": 0,
              "refund_amount": 549,
              "added_to_fynd_cash": false,
              "cashback_applied": 0,
              "gst_tax_percentage": 5,
              "value_of_good": 475.24,
              "price_marked": 499,
              "transfer_price": 0,
              "brand_calculated_amount": 499,
              "promotion_effective_discount": 0,
              "coupon_value": 0,
              "pm_price_split": {
                "COD": 549
              },
              "size": "5",
              "total_units": 1,
              "hsn_code": "62050000",
              "identifiers": {
                "sku_code": "CL-001L-L-PRPL-PINK-5"
              },
              "item_name": "Purple Flip Flops",
              "gst_fee": "23.76",
              "gst_tag": "IGST"
            }
          ],
          "current_status": "delivery_done",
          "item": {
            "name": "Purple Flip Flops",
            "brand": "Nike",
            "slug_key": "purple-flip-flops-ezmucvw4d3",
            "images": [
              "https://hdn-1.fynd.com/products/pictures/item/free/270x0/CL-001L-L-PRPL-PINK-6/Rvk5WbGg9Hx-1.jpg"
            ],
            "size": "5",
            "l1_category": "",
            "l3_category": "27"
          },
          "brand": {
            "modified_on": 1655707988,
            "logo": "https://hdn-1.jiomarketx0.de/x0/brands/pictures/square-logo/original/DbhIvd_tB-Logo.jpeg",
            "brand_name": "Nike",
            "company": null,
            "created_on": 1647793418,
            "id": 4
          },
          "gst_details": {
            "gstin_code": null,
            "gst_tag": "IGST",
            "hsn_code": "62050000",
            "value_of_good": 475.24,
            "gst_tax_percentage": 5,
            "is_default_hsn_code": true,
            "brand_calculated_amount": 499,
            "gst_fee": "23.76"
          },
          "article": {
            "uid": "6237fdfec0903e7ae543c201",
            "identifiers": {
              "sku_code": "CL-001L-L-PRPL-PINK-5"
            },
            "return_config": {
              "time": 30,
              "unit": "days",
              "returnable": true
            }
          },
          "quantity": 1
        }
      ],
      "delivery_slot": {
        "slot": "By 03:00 AM",
        "upper_bound": "2022-06-21T03:42:23+00:00",
        "lower_bound": "2022-06-21T03:42:23+00:00",
        "date": "2022-06-21T03:42:23+00:00",
        "type": "order_window"
      },
      "total_items": 1,
      "payment_methods": [
        {
          "slug": "COD",
          "payment_id": "COD",
          "payment_amt": 549,
          "payment_cart": null,
          "payment_desc": "COD",
          "bdcustomer_id": null,
          "order_inv_num": null,
          "mode_of_payment": "COD",
          "payment_gateway_logo": null,
          "transaction_ref_number": ""
        }
      ],
      "vertical": "GROCERIES",
      "payments": {
        "mode": "COD",
        "logo": "https://hdn-1.fynd.com/payment/Pos+Logo.png",
        "source": "Jio Partner Pay"
      },
      "priority_text": null,
      "status": {
        "created_at": 1655804437,
        "shipment_id": "16557829457641286433",
        "status": "delivery_done",
        "bag_list": [
          "43880"
        ],
        "id": 19980
      },
      "prices": {
        "amount_paid": 549,
        "refund_amount": 549,
        "price_marked": 499,
        "cod_charges": 0,
        "discount": 0,
        "cashback_applied": 0,
        "delivery_charge": 50,
        "fynd_credits": 0,
        "cashback": 0,
        "price_effective": 499,
        "refund_credit": 0,
        "value_of_good": 475.24,
        "pm_price_split": {
          "COD": 549
        },
        "brand_calculated_amount": 499,
        "coupon_effective_discount": 0,
        "tax_collected_at_source": 0,
        "promotion_effective_discount": 0
      },
      "picked_date": "",
      "tracking_list": [
        {
          "status": "Order Placed",
          "time": "2022-06-21T09:12:32+00:00",
          "is_passed": true,
          "is_current": false
        },
        {
          "status": "Order Confirmed",
          "time": "2022-06-21T09:39:13+00:00",
          "is_passed": true,
          "is_current": false
        },
        {
          "status": "Invoiced",
          "time": "2022-06-21T09:40:12+00:00",
          "is_passed": true,
          "is_current": false
        },
        {
          "status": "Delivery Partner Assigned",
          "time": "2022-06-21T09:40:12+00:00",
          "is_passed": true,
          "is_current": false
        },
        {
          "status": "Packed",
          "time": "2022-06-21T09:40:12+00:00",
          "is_passed": true,
          "is_current": false
        },
        {
          "status": "In Transit",
          "time": "2022-06-21T09:40:12+00:00",
          "is_passed": true,
          "is_current": false
        },
        {
          "status": "Out For Delivery",
          "time": "2022-06-21T09:40:29+00:00",
          "is_passed": true,
          "is_current": false
        },
        {
          "status": "Delivered",
          "time": "2022-06-21T09:40:37+00:00",
          "is_passed": true,
          "is_current": true
        }
      ],
      "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
      "platform_logo": "https://fynd-static.s3.amazonaws.com/mode_of_payment/fynd_logo.png",
      "packaging_type": "POLYB_DFLT_L"
    }
  ]
}
```
</details>









---


### getShipmentList





```python
try:
    result = await client.orders.getShipmentList(lane=lane, searchType=searchType, searchId=searchId, fromDate=fromDate, toDate=toDate, dpIds=dpIds, orderingCompanyId=orderingCompanyId, stores=stores, salesChannel=salesChannel, requestByExt=requestByExt, pageNo=pageNo, pageSize=pageSize, customerId=customerId, isPrioritySort=isPrioritySort)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| lane | String? | no |  |   
| searchType | String? | no |  |   
| searchId | String? | no |  |   
| fromDate | String? | no |  |   
| toDate | String? | no |  |   
| dpIds | String? | no |  |   
| orderingCompanyId | String? | no |  |   
| stores | String? | no |  |   
| salesChannel | String? | no |  |   
| requestByExt | String? | no |  |   
| pageNo | Int? | no |  |   
| pageSize | Int? | no |  |   
| customerId | String? | no |  |   
| isPrioritySort | Boolean? | no |  |  





*Returned Response:*




[ShipmentInternalPlatformViewResponse](#ShipmentInternalPlatformViewResponse)

We are processing the report!




<details>
<summary><i>&nbsp; Example:</i></summary>

```json

```
</details>









---


### getShipmentToManifest





```python
try:
    result = await client.orders.getShipmentToManifest(groupEntity=groupEntity, salesChannel=salesChannel, dpIds=dpIds)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| groupEntity | String | yes |  |   
| salesChannel | String? | no |  |   
| dpIds | String? | no |  |  





*Returned Response:*




[ManifestShipmentResponse](#ManifestShipmentResponse)

We are processing the report!




<details>
<summary><i>&nbsp; Example:</i></summary>

```json

```
</details>









---


### getOrders





```python
try:
    result = await client.orders.getOrders(lane=lane, searchType=searchType, searchValue=searchValue, fromDate=fromDate, toDate=toDate, dpIds=dpIds, stores=stores, salesChannel=salesChannel, pageNo=pageNo, pageSize=pageSize, isPrioritySort=isPrioritySort)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| lane | String? | no |  |   
| searchType | String? | no |  |   
| searchValue | String? | no |  |   
| fromDate | String? | no |  |   
| toDate | String? | no |  |   
| dpIds | String? | no |  |   
| stores | String? | no |  |   
| salesChannel | String? | no |  |   
| pageNo | Int? | no |  |   
| pageSize | Int? | no |  |   
| isPrioritySort | Boolean? | no |  |  





*Returned Response:*




[OrderListingResponse](#OrderListingResponse)

We are processing the report!




<details>
<summary><i>&nbsp; Example:</i></summary>

```json

```
</details>









---


### getMetricCount





```python
try:
    result = await client.orders.getMetricCount(fromDate=fromDate, toDate=toDate)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| fromDate | String? | no |  |   
| toDate | String? | no |  |  





*Returned Response:*




[MetricCountResponse](#MetricCountResponse)

Response containing count of shipments of the given metrics




<details>
<summary><i>&nbsp; Example:</i></summary>

```json

```
</details>









---


### getfilters





```python
try:
    result = await client.orders.getfilters(view=view)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| view | String | yes |  |  





*Returned Response:*




[FiltersResponse](#FiltersResponse)

List of filters




<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
  "delivery_partners": [
    {
      "text": "Ecomm",
      "value": 1,
      "name": "ecom_jio"
    },
    {
      "text": "Grab",
      "value": 12,
      "name": "grab_jio"
    },
    {
      "text": "Ecomm Express",
      "value": 13,
      "name": "ecom_express_3P"
    },
    {
      "text": "Delivery Express",
      "value": 14,
      "name": "delhivery_express_3P"
    },
    {
      "text": "Xpressbees Express",
      "value": 15,
      "name": "xpressbees_express_3P"
    },
    {
      "text": "Delhiver Express",
      "value": 19,
      "name": "delhivery_jio_surface"
    }
  ],
  "channels": [
    {
      "text": "JIOMARKET",
      "value": "0000000000000000000000045",
      "name": "JIOMARKET"
    },
    {
      "text": "JIOMART",
      "value": "5ea6821b3425bb07c82a2551",
      "name": "JIOMART"
    }
  ]
}
```
</details>









---


### getApplicationShipments





```python
try:
    result = await client.application("<APPLICATION_ID>").orders.getApplicationShipments(lane=lane, searchType=searchType, searchId=searchId, fromDate=fromDate, toDate=toDate, dpIds=dpIds, orderingCompanyId=orderingCompanyId, stores=stores, salesChannel=salesChannel, requestByExt=requestByExt, pageNo=pageNo, pageSize=pageSize, customerId=customerId, isPrioritySort=isPrioritySort)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| lane | String? | no |  |   
| searchType | String? | no |  |   
| searchId | String? | no |  |   
| fromDate | String? | no |  |   
| toDate | String? | no |  |   
| dpIds | String? | no |  |   
| orderingCompanyId | String? | no |  |   
| stores | String? | no |  |   
| salesChannel | String? | no |  |   
| requestByExt | String? | no |  |   
| pageNo | Int? | no |  |   
| pageSize | Int? | no |  |   
| customerId | String? | no |  |   
| isPrioritySort | Boolean? | no |  |  





*Returned Response:*




[ShipmentInternalPlatformViewResponse](#ShipmentInternalPlatformViewResponse)

We are processing the report!




<details>
<summary><i>&nbsp; Example:</i></summary>

```json

```
</details>









---


### createShipmentReport





```python
try:
    result = await client.orders.createShipmentReport(fromDate=fromDate, toDate=toDate)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| fromDate | String? | no |  |   
| toDate | String? | no |  |  





*Returned Response:*




[Success](#Success)

We have accepted report generation request.




<details>
<summary><i>&nbsp; Example:</i></summary>

```json

```
</details>









---


### getReportsShipmentListing





```python
try:
    result = await client.orders.getReportsShipmentListing(pageNo=pageNo, pageSize=pageSize)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- | 
| pageNo | Int? | no |  |   
| pageSize | Int? | no |  |  





*Returned Response:*




[OmsReports](#OmsReports)

We have are getting the info.




<details>
<summary><i>&nbsp; Example:</i></summary>

```json

```
</details>









---


### upsertJioCode





```python
try:
    result = await client.orders.upsertJioCode(body=body)
    # use result
except Exception as e:
    print(e)
```





| Argument  |  Type  | Required | Description |
| --------- | -----  | -------- | ----------- |
| body | [JioCodeUpsertPayload](#JioCodeUpsertPayload) | yes | Request body |




*Returned Response:*




[JioCodeUpsertResponse](#JioCodeUpsertResponse)

We are processing the report!




<details>
<summary><i>&nbsp; Example:</i></summary>

```json

```
</details>









---



### Schemas

 
 
 #### [UserDetailsData](#UserDetailsData)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | address | String |  no  |  |
 | email | String |  no  |  |
 | name | String |  no  |  |
 | phone | String |  no  |  |
 | state | String |  no  |  |
 | city | String |  no  |  |
 | pincode | String |  no  |  |
 | country | String |  no  |  |

---


 
 
 #### [FulfillingStore](#FulfillingStore)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | address | String |  no  |  |
 | storeName | String |  no  |  |
 | pincode | String |  no  |  |
 | contactPerson | String |  no  |  |
 | meta | HashMap<String,Any> |  no  |  |
 | code | String |  no  |  |
 | phone | String |  no  |  |
 | id | String |  no  |  |
 | city | String |  no  |  |
 | state | String |  no  |  |
 | country | String |  no  |  |
 | fulfillmentChannel | String |  no  |  |

---


 
 
 #### [GST](#GST)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | valueOfGood | Double |  no  |  |
 | taxCollectedAtSource | Double |  no  |  |
 | brandCalculatedAmount | Double |  no  |  |
 | gstFee | Double |  no  |  |
 | gstinCode | String |  no  |  |

---


 
 
 #### [TrackingList](#TrackingList)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | isPassed | Boolean? |  yes  |  |
 | status | String |  no  |  |
 | isCurrent | Boolean? |  yes  |  |
 | time | String? |  yes  |  |

---


 
 
 #### [OrderDetailsData](#OrderDetailsData)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | affiliateId | String? |  yes  |  |
 | fyndOrderId | String |  no  |  |
 | taxDetails | HashMap<String,Any>? |  yes  |  |
 | orderDate | String? |  yes  |  |
 | orderValue | String? |  yes  |  |
 | source | String? |  yes  |  |
 | codCharges | String? |  yes  |  |
 | orderingChannel | String? |  yes  |  |
 | orderingChannelLogo | HashMap<String,Any>? |  yes  |  |

---


 
 
 #### [OrderBrandName](#OrderBrandName)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | brandName | String |  no  |  |
 | logo | String |  no  |  |
 | modifiedOn | Int? |  yes  |  |
 | createdOn | Int |  no  |  |
 | company | String |  no  |  |
 | id | Int |  no  |  |

---


 
 
 #### [BagConfigs](#BagConfigs)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | isCustomerReturnAllowed | Boolean |  no  |  |
 | isActive | Boolean |  no  |  |
 | canBeCancelled | Boolean |  no  |  |
 | enableTracking | Boolean |  no  |  |
 | allowForceReturn | Boolean |  no  |  |
 | isReturnable | Boolean |  no  |  |

---


 
 
 #### [OrderBagArticle](#OrderBagArticle)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | returnConfig | HashMap<String,Any>? |  yes  |  |
 | identifiers | HashMap<String,Any>? |  yes  |  |
 | uid | String? |  yes  |  |

---


 
 
 #### [BagGST](#BagGST)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | gstTaxPercentage | Int? |  yes  |  |
 | valueOfGood | Int? |  yes  |  |
 | brandCalculatedAmount | Int? |  yes  |  |
 | gstTag | String? |  yes  |  |
 | gstFee | Int? |  yes  |  |
 | isDefaultHsnCode | Boolean? |  yes  |  |
 | gstinCode | String? |  yes  |  |
 | hsnCode | String? |  yes  |  |

---


 
 
 #### [FinancialBreakup](#FinancialBreakup)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | discount | Int |  no  |  |
 | transferPrice | Int |  no  |  |
 | totalUnits | Int |  no  |  |
 | addedToFyndCash | Boolean |  no  |  |
 | cashbackApplied | Int |  no  |  |
 | gstFee | String |  no  |  |
 | identifiers | HashMap<String,Any> |  no  |  |
 | couponEffectiveDiscount | Int |  no  |  |
 | couponValue | Int |  no  |  |
 | itemName | String |  no  |  |
 | priceMarked | Int |  no  |  |
 | deliveryCharge | Int |  no  |  |
 | gstTaxPercentage | Int |  no  |  |
 | pmPriceSplit | HashMap<String,Any> |  no  |  |
 | gstTag | String |  no  |  |
 | promotionEffectiveDiscount | Int |  no  |  |
 | codCharges | Int |  no  |  |
 | hsnCode | String |  no  |  |
 | amountPaid | Int |  no  |  |
 | refundCredit | Int |  no  |  |
 | size | String |  no  |  |
 | valueOfGood | Int |  no  |  |
 | brandCalculatedAmount | Int |  no  |  |
 | cashback | Int |  no  |  |
 | fyndCredits | Int |  no  |  |
 | priceEffective | Int |  no  |  |

---


 
 
 #### [OrderBagItem](#OrderBagItem)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | size | String |  no  |  |
 | image | ArrayList<String>? |  yes  |  |
 | brand | String |  no  |  |
 | name | String |  no  |  |
 | l1Category | ArrayList<String>? |  yes  |  |
 | slugKey | String |  no  |  |
 | l3Category | Int |  no  |  |

---


 
 
 #### [OrderBags](#OrderBags)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | displayName | String |  no  |  |
 | brand | [OrderBrandName](#OrderBrandName)? |  yes  |  |
 | bagConfigs | [BagConfigs](#BagConfigs)? |  yes  |  |
 | quantity | Int |  no  |  |
 | article | [OrderBagArticle](#OrderBagArticle)? |  yes  |  |
 | bagId | Int |  no  |  |
 | gstDetails | [BagGST](#BagGST)? |  yes  |  |
 | currentStatus | String |  no  |  |
 | entityType | String |  no  |  |
 | financialBreakup | ArrayList<[FinancialBreakup](#FinancialBreakup)>? |  yes  |  |
 | item | [OrderBagItem](#OrderBagItem)? |  yes  |  |

---


 
 
 #### [ShipmentStatusData](#ShipmentStatusData)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | createdAt | String? |  yes  |  |
 | status | String? |  yes  |  |
 | bagList | ArrayList<Int>? |  yes  |  |
 | id | Int? |  yes  |  |
 | shipmentId | String? |  yes  |  |

---


 
 
 #### [DPDetails](#DPDetails)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | name | String? |  yes  |  |
 | trackUrl | String? |  yes  |  |
 | gstTag | String? |  yes  |  |
 | ewayBillId | String? |  yes  |  |
 | awbNo | String? |  yes  |  |
 | id | String? |  yes  |  |
 | pincode | String? |  yes  |  |
 | country | String? |  yes  |  |

---


 
 
 #### [ShipmentPayments](#ShipmentPayments)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | source | String? |  yes  |  |
 | logo | String? |  yes  |  |
 | mode | String |  no  |  |

---


 
 
 #### [Prices](#Prices)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | amountPaid | Double |  no  |  |
 | deliveryCharge | Double |  no  |  |
 | refundCredit | Double |  no  |  |
 | amountPaidRoundoff | Double |  no  |  |
 | discount | Double |  no  |  |
 | valueOfGood | Double |  no  |  |
 | taxCollectedAtSource | Double |  no  |  |
 | refundAmount | Double |  no  |  |
 | cashback | Double |  no  |  |
 | cashbackApplied | Double |  no  |  |
 | couponValue | Double |  no  |  |
 | promotionEffectiveDiscount | Double |  no  |  |
 | codCharges | Double |  no  |  |
 | fyndCredits | Double |  no  |  |
 | priceEffective | Double |  no  |  |
 | priceMarked | Double |  no  |  |

---


 
 
 #### [BagStatusHistory](#BagStatusHistory)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | displayName | Boolean? |  yes  |  |
 | updatedAt | String? |  yes  |  |
 | status | String |  no  |  |
 | appDisplayName | Boolean? |  yes  |  |
 | stateType | Boolean? |  yes  |  |
 | forward | Boolean? |  yes  |  |

---


 
 
 #### [ShipmentInfoResponse](#ShipmentInfoResponse)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | pickedDate | String |  no  |  |
 | shipmentQuantity | Int |  no  |  |
 | totalItems | Int? |  yes  |  |
 | kiranaStoreId | String? |  yes  |  |
 | isNotFyndSource | Boolean |  no  |  |
 | payButton | String? |  yes  |  |
 | invoice | HashMap<String,Any> |  no  |  |
 | paymentMode | String |  no  |  |
 | priorityText | String? |  yes  |  |
 | affiliateShipmentId | String |  no  |  |
 | billingDetails | [UserDetailsData](#UserDetailsData)? |  yes  |  |
 | forwardOrderStatus | ArrayList<HashMap<String,Any>>? |  yes  |  |
 | company | HashMap<String,Any> |  no  |  |
 | items | ArrayList<HashMap<String,Any>> |  no  |  |
 | enableDpTracking | String |  no  |  |
 | fulfillingStore | [FulfillingStore](#FulfillingStore)? |  yes  |  |
 | packagingType | String |  no  |  |
 | coupon | HashMap<String,Any>? |  yes  |  |
 | escalation | HashMap<String,Any>? |  yes  |  |
 | userInfo | HashMap<String,Any>? |  yes  |  |
 | isPdsr | String? |  yes  |  |
 | gstDetails | [GST](#GST)? |  yes  |  |
 | deliveryDetails | [UserDetailsData](#UserDetailsData)? |  yes  |  |
 | isPackagingOrder | Boolean |  no  |  |
 | dueDate | String? |  yes  |  |
 | trackingList | ArrayList<[TrackingList](#TrackingList)>? |  yes  |  |
 | refundText | String? |  yes  |  |
 | beneficiaryDetails | Boolean? |  yes  |  |
 | enableTracking | Boolean? |  yes  |  |
 | creditNoteId | String |  no  |  |
 | forwardTrackingList | ArrayList<HashMap<String,Any>>? |  yes  |  |
 | orderStatus | HashMap<String,Any> |  no  |  |
 | currentShipmentStatus | HashMap<String,Any> |  no  |  |
 | isInvoiced | Boolean |  no  |  |
 | mid | String? |  yes  |  |
 | canCancel | Boolean? |  yes  |  |
 | order | [OrderDetailsData](#OrderDetailsData)? |  yes  |  |
 | platformLogo | Boolean |  no  |  |
 | orderCreatedTime | String? |  yes  |  |
 | refundDetails | HashMap<String,Any>? |  yes  |  |
 | replacementDetails | String? |  yes  |  |
 | bankData | HashMap<String,Any>? |  yes  |  |
 | securedDeliveryFlag | String? |  yes  |  |
 | bags | [OrderBags](#OrderBags)? |  yes  |  |
 | status | [ShipmentStatusData](#ShipmentStatusData)? |  yes  |  |
 | emailId | String |  no  |  |
 | orderingStore | HashMap<String,Any> |  no  |  |
 | deliveryStatus | ArrayList<HashMap<String,Any>> |  no  |  |
 | isFyndStore | String? |  yes  |  |
 | dpDetails | [DPDetails](#DPDetails)? |  yes  |  |
 | forwardShipmentStatus | ArrayList<HashMap<String,Any>>? |  yes  |  |
 | fyndstoreEmp | HashMap<String,Any> |  no  |  |
 | payments | [ShipmentPayments](#ShipmentPayments)? |  yes  |  |
 | goGreen | Boolean? |  yes  |  |
 | userId | String |  no  |  |
 | deliverySlot | HashMap<String,Any> |  no  |  |
 | vertical | String? |  yes  |  |
 | userAgent | String |  no  |  |
 | prices | [Prices](#Prices)? |  yes  |  |
 | isFyndCoupon | Boolean |  no  |  |
 | lockStatus | String |  no  |  |
 | orderType | String |  no  |  |
 | journeyType | String |  no  |  |
 | childNodes | ArrayList<String>? |  yes  |  |
 | canReturn | Boolean? |  yes  |  |
 | statusProgress | Int |  no  |  |
 | bagStatusHistory | ArrayList<[BagStatusHistory](#BagStatusHistory)>? |  yes  |  |
 | shipmentId | String |  no  |  |
 | canBreak | String |  no  |  |
 | trackingUrl | String |  no  |  |

---


 
 
 #### [Error](#Error)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | success | Boolean? |  yes  |  |
 | reason | String? |  yes  |  |

---


 
 
 #### [SubLane](#SubLane)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | text | String |  no  |  |
 | index | Int |  no  |  |
 | nextState | ArrayList<String>? |  yes  |  |
 | currentState | ArrayList<String>? |  yes  |  |
 | value | String |  no  |  |
 | totalShipments | Int |  no  |  |

---


 
 
 #### [SuperLane](#SuperLane)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | value | String |  no  |  |
 | options | ArrayList<[SubLane](#SubLane)>? |  yes  |  |
 | text | String |  no  |  |

---


 
 
 #### [LaneConfigResponse](#LaneConfigResponse)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | superLanes | ArrayList<[SuperLane](#SuperLane)>? |  yes  |  |

---


 
 
 #### [OrderDict](#OrderDict)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | orderDate | String |  no  |  |
 | fyndOrderId | String |  no  |  |
 | shipmentCount | Int |  no  |  |

---


 
 
 #### [Shipment](#Shipment)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | pickedDate | String |  no  |  |
 | shipmentQuantity | Int |  no  |  |
 | totalItems | Int? |  yes  |  |
 | paymentMode | String |  no  |  |
 | priorityText | String? |  yes  |  |
 | billingDetails | [UserDetailsData](#UserDetailsData)? |  yes  |  |
 | enableDpTracking | String |  no  |  |
 | fulfillingStore | [FulfillingStore](#FulfillingStore)? |  yes  |  |
 | packagingType | String |  no  |  |
 | gstDetails | [GST](#GST)? |  yes  |  |
 | deliveryDetails | [UserDetailsData](#UserDetailsData)? |  yes  |  |
 | trackingList | ArrayList<[TrackingList](#TrackingList)>? |  yes  |  |
 | order | [OrderDetailsData](#OrderDetailsData)? |  yes  |  |
 | platformLogo | String |  no  |  |
 | bags | [OrderBags](#OrderBags)? |  yes  |  |
 | status | [ShipmentStatusData](#ShipmentStatusData)? |  yes  |  |
 | dpDetails | [DPDetails](#DPDetails)? |  yes  |  |
 | payments | [ShipmentPayments](#ShipmentPayments)? |  yes  |  |
 | deliverySlot | HashMap<String,Any> |  no  |  |
 | vertical | String? |  yes  |  |
 | userAgent | String |  no  |  |
 | prices | [Prices](#Prices)? |  yes  |  |
 | journeyType | String |  no  |  |
 | bagStatusHistory | ArrayList<[BagStatusHistory](#BagStatusHistory)>? |  yes  |  |
 | shipmentId | String |  no  |  |

---


 
 
 #### [ShipmentDetailsResponse](#ShipmentDetailsResponse)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | success | Boolean |  no  |  |
 | order | [OrderDict](#OrderDict)? |  yes  |  |
 | shipments | ArrayList<[Shipment](#Shipment)>? |  yes  |  |

---


 
 
 #### [FilterInfoOption](#FilterInfoOption)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | value | String? |  yes  |  |
 | text | String |  no  |  |
 | name | String? |  yes  |  |

---


 
 
 #### [FiltersInfo](#FiltersInfo)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | type | String |  no  |  |
 | value | String |  no  |  |
 | options | ArrayList<[FilterInfoOption](#FilterInfoOption)>? |  yes  |  |
 | text | String |  no  |  |

---


 
 
 #### [ShipmentStatus](#ShipmentStatus)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | title | String |  no  |  |
 | opsStatus | String |  no  |  |
 | hexCode | String |  no  |  |
 | actualStatus | String |  no  |  |
 | status | String |  no  |  |

---


 
 
 #### [PaymentModeInfo](#PaymentModeInfo)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | type | String |  no  |  |
 | logo | String |  no  |  |

---


 
 
 #### [Item](#Item)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | size | String |  no  |  |
 | color | String? |  yes  |  |
 | image | ArrayList<String>? |  yes  |  |
 | name | String |  no  |  |
 | canCancel | Boolean |  no  |  |
 | l1Category | ArrayList<String>? |  yes  |  |
 | code | String |  no  |  |
 | canReturn | Boolean |  no  |  |
 | departmentId | Int |  no  |  |
 | id | Int |  no  |  |
 | l3CategoryName | String |  no  |  |
 | l3Category | Int |  no  |  |

---


 
 
 #### [BagUnit](#BagUnit)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | gst | [GST](#GST)? |  yes  |  |
 | bagId | Int |  no  |  |
 | prices | [Prices](#Prices)? |  yes  |  |
 | status | HashMap<String,Any> |  no  |  |
 | orderingChannel | String |  no  |  |
 | itemQuantity | Int |  no  |  |
 | shipmentId | String |  no  |  |
 | totalShipmentBags | Int |  no  |  |
 | item | [Item](#Item)? |  yes  |  |

---


 
 
 #### [UserDataInfo](#UserDataInfo)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | email | String |  no  |  |
 | mobile | String |  no  |  |
 | avisUserId | String |  no  |  |
 | firstName | String |  no  |  |
 | lastName | String |  no  |  |
 | isAnonymousUser | Boolean |  no  |  |
 | gender | String |  no  |  |
 | uid | Int |  no  |  |

---


 
 
 #### [ShipmentItemFulFillingStore](#ShipmentItemFulFillingStore)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | code | String |  no  |  |
 | id | String |  no  |  |

---


 
 
 #### [ShipmentItem](#ShipmentItem)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | createdAt | String |  no  |  |
 | shipmentStatus | [ShipmentStatus](#ShipmentStatus)? |  yes  |  |
 | shipmentCreatedAt | Int |  no  |  |
 | totalBagsCount | Int |  no  |  |
 | fulfillingCentre | String |  no  |  |
 | paymentModeInfo | [PaymentModeInfo](#PaymentModeInfo)? |  yes  |  |
 | sla | HashMap<String,Any>? |  yes  |  |
 | prices | [Prices](#Prices)? |  yes  |  |
 | bags | ArrayList<[BagUnit](#BagUnit)>? |  yes  |  |
 | application | HashMap<String,Any>? |  yes  |  |
 | id | String |  no  |  |
 | channel | HashMap<String,Any>? |  yes  |  |
 | totalShipmentsInOrder | Int |  no  |  |
 | user | [UserDataInfo](#UserDataInfo)? |  yes  |  |
 | fulfillingStore | [ShipmentItemFulFillingStore](#ShipmentItemFulFillingStore)? |  yes  |  |

---


 
 
 #### [ShipmentInternalPlatformViewResponse](#ShipmentInternalPlatformViewResponse)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | filters | ArrayList<[FiltersInfo](#FiltersInfo)>? |  yes  |  |
 | page | HashMap<String,Any>? |  yes  |  |
 | appliedFilters | HashMap<String,Any>? |  yes  |  |
 | items | ArrayList<[ShipmentItem](#ShipmentItem)>? |  yes  |  |

---


 
 
 #### [ShipmentPricesDataSet](#ShipmentPricesDataSet)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | amountPaid | Int? |  yes  |  |
 | deliveryCharge | Int? |  yes  |  |
 | refundCredit | Int? |  yes  |  |
 | discount | String? |  yes  |  |
 | valueOfGood | Int? |  yes  |  |
 | taxCollectedAtSource | Int? |  yes  |  |
 | brandCalculatedAmount | Int? |  yes  |  |
 | cashback | Int? |  yes  |  |
 | cashbackApplied | Int? |  yes  |  |
 | gstFee | Int? |  yes  |  |
 | codCharges | Int? |  yes  |  |
 | fyndCredits | Int? |  yes  |  |
 | couponEffectiveDiscount | Int? |  yes  |  |
 | priceEffective | Int? |  yes  |  |
 | priceMarked | Int? |  yes  |  |

---


 
 
 #### [Shipment1](#Shipment1)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | totalItems | String |  no  |  |
 | shipmentStatus | String |  no  |  |
 | rtdDone | String |  no  |  |
 | prices | [ShipmentPricesDataSet](#ShipmentPricesDataSet)? |  yes  |  |
 | shipmentId | String |  no  |  |
 | orderId | String |  no  |  |

---


 
 
 #### [ManifestShipmentResponse](#ManifestShipmentResponse)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | success | Boolean |  no  |  |
 | shipments | ArrayList<[Shipment1](#Shipment1)>? |  yes  |  |

---


 
 
 #### [ErrorSchemaDataSet](#ErrorSchemaDataSet)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | success | Boolean? |  yes  |  |
 | reason | String? |  yes  |  |

---


 
 
 #### [UserDataSet](#UserDataSet)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | mobile | Int |  no  |  |
 | email | String? |  yes  |  |
 | gender | String? |  yes  |  |
 | name | String |  no  |  |

---


 
 
 #### [ShipmentPricesDataInfo](#ShipmentPricesDataInfo)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | amountPaid | Int? |  yes  |  |
 | deliveryCharge | Int? |  yes  |  |
 | refundCredit | Int? |  yes  |  |
 | discount | Int? |  yes  |  |
 | valueOfGood | Int? |  yes  |  |
 | refundAmount | Int? |  yes  |  |
 | couponValue | String? |  yes  |  |
 | cashbackApplied | Int? |  yes  |  |
 | cashback | Int? |  yes  |  |
 | codCharges | Int? |  yes  |  |
 | fyndCredits | Int? |  yes  |  |
 | priceEffective | Int? |  yes  |  |
 | priceMarked | Int? |  yes  |  |

---


 
 
 #### [ShipmentDataSet](#ShipmentDataSet)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | deliveryCharge | Int? |  yes  |  |
 | refundCredit | Int? |  yes  |  |
 | totalItems | Int |  no  |  |
 | shipmentStatus | HashMap<String,Any> |  no  |  |
 | valueOfGood | Int? |  yes  |  |
 | taxCollectedAtSource | Int? |  yes  |  |
 | brandCalculatedAmount | Int? |  yes  |  |
 | cashback | Int? |  yes  |  |
 | cashbackApplied | Int? |  yes  |  |
 | prices | [ShipmentPricesDataInfo](#ShipmentPricesDataInfo)? |  yes  |  |
 | fyndCredits | Int? |  yes  |  |
 | totalBags | Int |  no  |  |
 | couponEffectiveDiscount | Int? |  yes  |  |
 | priceEffective | Int? |  yes  |  |
 | shipmentId | String |  no  |  |
 | shipmentImages | ArrayList<String>? |  yes  |  |

---


 
 
 #### [OrderDataSet](#OrderDataSet)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | userInfo | [UserDataSet](#UserDataSet)? |  yes  |  |
 | orderCreatedTime | String |  no  |  |
 | shipments | ArrayList<[ShipmentDataSet](#ShipmentDataSet)>? |  yes  |  |
 | orderId | String |  no  |  |

---


 
 
 #### [OrderListingResponse](#OrderListingResponse)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | success | Boolean |  no  |  |
 | orders | ArrayList<[OrderDataSet](#OrderDataSet)>? |  yes  |  |

---


 
 
 #### [OrderErrorSchemaDataSet](#OrderErrorSchemaDataSet)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | success | Boolean? |  yes  |  |
 | reason | String? |  yes  |  |

---


 
 
 #### [Options](#Options)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | value | Int? |  yes  |  |
 | text | String? |  yes  |  |

---


 
 
 #### [MetricsCount](#MetricsCount)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | value | Int |  no  |  |
 | options | ArrayList<[Options](#Options)>? |  yes  |  |
 | text | String |  no  |  |
 | key | String |  no  |  |

---


 
 
 #### [MetricCountResponse](#MetricCountResponse)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | items | ArrayList<[MetricsCount](#MetricsCount)>? |  yes  |  |

---


 
 
 #### [FiltersResponse](#FiltersResponse)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | deliveryPartners | ArrayList<[FiltersInfo](#FiltersInfo)>? |  yes  |  |
 | channels | ArrayList<[FiltersInfo](#FiltersInfo)>? |  yes  |  |

---


 
 
 #### [Success](#Success)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | success | Boolean? |  yes  |  |
 | message | String? |  yes  |  |

---


 
 
 #### [OmsReports](#OmsReports)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | displayName | String? |  yes  |  |
 | requestDetails | HashMap<String,Any>? |  yes  |  |
 | reportName | String? |  yes  |  |
 | status | String? |  yes  |  |
 | reportRequestedAt | String? |  yes  |  |
 | reportCreatedAt | String? |  yes  |  |
 | s3Key | String? |  yes  |  |
 | reportType | String? |  yes  |  |
 | reportId | String? |  yes  |  |

---


 
 
 #### [JioCodeUpsertDataSet](#JioCodeUpsertDataSet)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | articleId | String? |  yes  |  |
 | companyId | String? |  yes  |  |
 | jioCode | String? |  yes  |  |
 | itemId | String? |  yes  |  |

---


 
 
 #### [JioCodeUpsertPayload](#JioCodeUpsertPayload)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | data | ArrayList<[JioCodeUpsertDataSet](#JioCodeUpsertDataSet)>? |  yes  |  |

---


 
 
 #### [NestedErrorSchemaDataSet](#NestedErrorSchemaDataSet)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | type | String? |  yes  |  |
 | value | String? |  yes  |  |
 | message | String? |  yes  |  |

---


 
 
 #### [JioCodeUpsertResponse](#JioCodeUpsertResponse)

 | Properties | Type | Nullable | Description |
 | ---------- | ---- | -------- | ----------- |
 | data | ArrayList<HashMap<String,Any>>? |  yes  |  |
 | error | ArrayList<[NestedErrorSchemaDataSet](#NestedErrorSchemaDataSet)>? |  yes  |  |
 | identifier | String? |  yes  |  |
 | success | Boolean? |  yes  |  |
 | traceId | String? |  yes  |  |

---


