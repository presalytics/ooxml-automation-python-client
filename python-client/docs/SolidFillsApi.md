# presalytics_ooxml_automation.SolidFillsApi

All URIs are relative to *http://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**solid_fills_get_id**](SolidFillsApi.md#solid_fills_get_id) | **GET** /shared/SolidFills/{id} | SolidFills: Get by Id
[**solid_fills_put_id**](SolidFillsApi.md#solid_fills_put_id) | **PUT** /shared/SolidFills/{id} | SolidFills: Modify Values


# **solid_fills_get_id**
> SharedSolidFills solid_fills_get_id(id)

SolidFills: Get by Id

Get by Id: Use this method to retrieve a SolidFills object by its primary key (id)

### Example

```python
from __future__ import print_function
import time
import presalytics_ooxml_automation
from presalytics_ooxml_automation.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = presalytics_ooxml_automation.SolidFillsApi()
id = 56 # int | The primary key (Id) of the SolidFills object

try:
    # SolidFills: Get by Id
    api_response = api_instance.solid_fills_get_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SolidFillsApi->solid_fills_get_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The primary key (Id) of the SolidFills object | 

### Return type

[**SharedSolidFills**](SharedSolidFills.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request.  Please check for valid Id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **solid_fills_put_id**
> solid_fills_put_id(id, shared_solid_fills=shared_solid_fills)

SolidFills: Modify Values

PUT: Use this method for simple updates to SolidFills objects.   Please Note: Using this method sidesteps some data validation steps executed by base objects.  Please review the documentation and ECMA-376 prior to using this method. Per IETF 7231, all fields must be include in PUT requests, even though user and timestamp fields will be modified by the server.

### Example

```python
from __future__ import print_function
import time
import presalytics_ooxml_automation
from presalytics_ooxml_automation.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = presalytics_ooxml_automation.SolidFillsApi()
id = 56 # int | 
shared_solid_fills = presalytics_ooxml_automation.SharedSolidFills() # SharedSolidFills |  (optional)

try:
    # SolidFills: Modify Values
    api_instance.solid_fills_put_id(id, shared_solid_fills=shared_solid_fills)
except ApiException as e:
    print("Exception when calling SolidFillsApi->solid_fills_put_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **shared_solid_fills** | [**SharedSolidFills**](SharedSolidFills.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**204** |  |  -  |
**400** | Bad request.  Please check for valid Id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

