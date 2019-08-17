# presalytics_ooxml_automation.GradientFillsApi

All URIs are relative to *http://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_a_gradient_fills_get_id**](GradientFillsApi.md#o_a_gradient_fills_get_id) | **GET** /shared/GradientFills/{id} | GradientFills: Get by Id
[**o_a_gradient_fills_put_id**](GradientFillsApi.md#o_a_gradient_fills_put_id) | **PUT** /shared/GradientFills/{id} | GradientFills: Modify Values


# **o_a_gradient_fills_get_id**
> SharedGradientFills o_a_gradient_fills_get_id(id)

GradientFills: Get by Id

Get by Id: Use this method to retrieve a GradientFills object by its primary key (id)

### Example

```python
from __future__ import print_function
import time
import presalytics_ooxml_automation
from presalytics_ooxml_automation.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = presalytics_ooxml_automation.GradientFillsApi()
id = 56 # int | The primary key (Id) of the GradientFills object

try:
    # GradientFills: Get by Id
    api_response = api_instance.o_a_gradient_fills_get_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GradientFillsApi->o_a_gradient_fills_get_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The primary key (Id) of the GradientFills object | 

### Return type

[**SharedGradientFills**](SharedGradientFills.md)

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

# **o_a_gradient_fills_put_id**
> o_a_gradient_fills_put_id(id, shared_gradient_fills=shared_gradient_fills)

GradientFills: Modify Values

PUT: Use this method for simple updates to GradientFills objects.   Please Note: Using this method sidesteps some data validation steps executed by base objects.  Please review the documentation and ECMA-376 prior to using this method. Per IETF 7231, all fields must be include in PUT requests, even though user and timestamp fields will be modified by the server.

### Example

```python
from __future__ import print_function
import time
import presalytics_ooxml_automation
from presalytics_ooxml_automation.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = presalytics_ooxml_automation.GradientFillsApi()
id = 56 # int | 
shared_gradient_fills = presalytics_ooxml_automation.SharedGradientFills() # SharedGradientFills |  (optional)

try:
    # GradientFills: Modify Values
    api_instance.o_a_gradient_fills_put_id(id, shared_gradient_fills=shared_gradient_fills)
except ApiException as e:
    print("Exception when calling GradientFillsApi->o_a_gradient_fills_put_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **shared_gradient_fills** | [**SharedGradientFills**](SharedGradientFills.md)|  | [optional] 

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

