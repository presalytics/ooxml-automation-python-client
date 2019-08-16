# presalytics_ooxml_automation.GradientStopsApi

All URIs are relative to *http://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gradient_stops_get_id**](GradientStopsApi.md#gradient_stops_get_id) | **GET** /shared/GradientStops/{id} | GradientStops: Get by Id
[**gradient_stops_put_id**](GradientStopsApi.md#gradient_stops_put_id) | **PUT** /shared/GradientStops/{id} | GradientStops: Modify Values


# **gradient_stops_get_id**
> SharedGradientStops gradient_stops_get_id(id)

GradientStops: Get by Id

Get by Id: Use this method to retrieve a GradientStops object by its primary key (id)

### Example

```python
from __future__ import print_function
import time
import presalytics_ooxml_automation
from presalytics_ooxml_automation.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = presalytics_ooxml_automation.GradientStopsApi()
id = 56 # int | The primary key (Id) of the GradientStops object

try:
    # GradientStops: Get by Id
    api_response = api_instance.gradient_stops_get_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GradientStopsApi->gradient_stops_get_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The primary key (Id) of the GradientStops object | 

### Return type

[**SharedGradientStops**](SharedGradientStops.md)

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

# **gradient_stops_put_id**
> gradient_stops_put_id(id, shared_gradient_stops=shared_gradient_stops)

GradientStops: Modify Values

PUT: Use this method for simple updates to GradientStops objects.   Please Note: Using this method sidesteps some data validation steps executed by base objects.  Please review the documentation and ECMA-376 prior to using this method. Per IETF 7231, all fields must be include in PUT requests, even though user and timestamp fields will be modified by the server.

### Example

```python
from __future__ import print_function
import time
import presalytics_ooxml_automation
from presalytics_ooxml_automation.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = presalytics_ooxml_automation.GradientStopsApi()
id = 56 # int | 
shared_gradient_stops = presalytics_ooxml_automation.SharedGradientStops() # SharedGradientStops |  (optional)

try:
    # GradientStops: Modify Values
    api_instance.gradient_stops_put_id(id, shared_gradient_stops=shared_gradient_stops)
except ApiException as e:
    print("Exception when calling GradientStopsApi->gradient_stops_put_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **shared_gradient_stops** | [**SharedGradientStops**](SharedGradientStops.md)|  | [optional] 

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

