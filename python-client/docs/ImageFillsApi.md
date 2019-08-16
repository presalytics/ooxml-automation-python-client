# presalytics_ooxml_automation.ImageFillsApi

All URIs are relative to *http://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**image_fills_get_id**](ImageFillsApi.md#image_fills_get_id) | **GET** /shared/ImageFills/{id} | ImageFills: Get by Id
[**image_fills_put_id**](ImageFillsApi.md#image_fills_put_id) | **PUT** /shared/ImageFills/{id} | ImageFills: Modify Values


# **image_fills_get_id**
> SharedImageFills image_fills_get_id(id)

ImageFills: Get by Id

Get by Id: Use this method to retrieve a ImageFills object by its primary key (id)

### Example

```python
from __future__ import print_function
import time
import presalytics_ooxml_automation
from presalytics_ooxml_automation.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = presalytics_ooxml_automation.ImageFillsApi()
id = 56 # int | The primary key (Id) of the ImageFills object

try:
    # ImageFills: Get by Id
    api_response = api_instance.image_fills_get_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageFillsApi->image_fills_get_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The primary key (Id) of the ImageFills object | 

### Return type

[**SharedImageFills**](SharedImageFills.md)

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

# **image_fills_put_id**
> image_fills_put_id(id, shared_image_fills=shared_image_fills)

ImageFills: Modify Values

PUT: Use this method for simple updates to ImageFills objects.   Please Note: Using this method sidesteps some data validation steps executed by base objects.  Please review the documentation and ECMA-376 prior to using this method. Per IETF 7231, all fields must be include in PUT requests, even though user and timestamp fields will be modified by the server.

### Example

```python
from __future__ import print_function
import time
import presalytics_ooxml_automation
from presalytics_ooxml_automation.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = presalytics_ooxml_automation.ImageFillsApi()
id = 56 # int | 
shared_image_fills = presalytics_ooxml_automation.SharedImageFills() # SharedImageFills |  (optional)

try:
    # ImageFills: Modify Values
    api_instance.image_fills_put_id(id, shared_image_fills=shared_image_fills)
except ApiException as e:
    print("Exception when calling ImageFillsApi->image_fills_put_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **shared_image_fills** | [**SharedImageFills**](SharedImageFills.md)|  | [optional] 

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

