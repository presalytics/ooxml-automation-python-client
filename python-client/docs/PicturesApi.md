# presalytics_ooxml_automation.PicturesApi

All URIs are relative to *http://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_a_pictures_get_id**](PicturesApi.md#o_a_pictures_get_id) | **GET** /shared/Pictures/{id} | Pictures: Get by Id
[**o_a_pictures_put_id**](PicturesApi.md#o_a_pictures_put_id) | **PUT** /shared/Pictures/{id} | Pictures: Modify Values


# **o_a_pictures_get_id**
> SharedPictures o_a_pictures_get_id(id)

Pictures: Get by Id

Get by Id: Use this method to retrieve a Pictures object by its primary key (id)

### Example

```python
from __future__ import print_function
import time
import presalytics_ooxml_automation
from presalytics_ooxml_automation.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = presalytics_ooxml_automation.PicturesApi()
id = 56 # int | The primary key (Id) of the Pictures object

try:
    # Pictures: Get by Id
    api_response = api_instance.o_a_pictures_get_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PicturesApi->o_a_pictures_get_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The primary key (Id) of the Pictures object | 

### Return type

[**SharedPictures**](SharedPictures.md)

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

# **o_a_pictures_put_id**
> o_a_pictures_put_id(id, shared_pictures=shared_pictures)

Pictures: Modify Values

PUT: Use this method for simple updates to Pictures objects.   Please Note: Using this method sidesteps some data validation steps executed by base objects.  Please review the documentation and ECMA-376 prior to using this method. Per IETF 7231, all fields must be include in PUT requests, even though user and timestamp fields will be modified by the server.

### Example

```python
from __future__ import print_function
import time
import presalytics_ooxml_automation
from presalytics_ooxml_automation.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = presalytics_ooxml_automation.PicturesApi()
id = 56 # int | 
shared_pictures = presalytics_ooxml_automation.SharedPictures() # SharedPictures |  (optional)

try:
    # Pictures: Modify Values
    api_instance.o_a_pictures_put_id(id, shared_pictures=shared_pictures)
except ApiException as e:
    print("Exception when calling PicturesApi->o_a_pictures_put_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **shared_pictures** | [**SharedPictures**](SharedPictures.md)|  | [optional] 

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

