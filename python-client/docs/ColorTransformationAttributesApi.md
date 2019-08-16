# presalytics_ooxml_automation.ColorTransformationAttributesApi

All URIs are relative to *http://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**color_transformation_attributes_get_id**](ColorTransformationAttributesApi.md#color_transformation_attributes_get_id) | **GET** /shared/ColorTransformationAttributes/{id} | ColorTransformationAttributes: Get by Id
[**color_transformation_attributes_put_id**](ColorTransformationAttributesApi.md#color_transformation_attributes_put_id) | **PUT** /shared/ColorTransformationAttributes/{id} | ColorTransformationAttributes: Modify Values


# **color_transformation_attributes_get_id**
> SharedColorTransformationAttributes color_transformation_attributes_get_id(id)

ColorTransformationAttributes: Get by Id

Get by Id: Use this method to retrieve a ColorTransformationAttributes object by its primary key (id)

### Example

```python
from __future__ import print_function
import time
import presalytics_ooxml_automation
from presalytics_ooxml_automation.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = presalytics_ooxml_automation.ColorTransformationAttributesApi()
id = 56 # int | The primary key (Id) of the ColorTransformationAttributes object

try:
    # ColorTransformationAttributes: Get by Id
    api_response = api_instance.color_transformation_attributes_get_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ColorTransformationAttributesApi->color_transformation_attributes_get_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The primary key (Id) of the ColorTransformationAttributes object | 

### Return type

[**SharedColorTransformationAttributes**](SharedColorTransformationAttributes.md)

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

# **color_transformation_attributes_put_id**
> color_transformation_attributes_put_id(id, shared_color_transformation_attributes=shared_color_transformation_attributes)

ColorTransformationAttributes: Modify Values

PUT: Use this method for simple updates to ColorTransformationAttributes objects.   Please Note: Using this method sidesteps some data validation steps executed by base objects.  Please review the documentation and ECMA-376 prior to using this method. Per IETF 7231, all fields must be include in PUT requests, even though user and timestamp fields will be modified by the server.

### Example

```python
from __future__ import print_function
import time
import presalytics_ooxml_automation
from presalytics_ooxml_automation.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = presalytics_ooxml_automation.ColorTransformationAttributesApi()
id = 56 # int | 
shared_color_transformation_attributes = presalytics_ooxml_automation.SharedColorTransformationAttributes() # SharedColorTransformationAttributes |  (optional)

try:
    # ColorTransformationAttributes: Modify Values
    api_instance.color_transformation_attributes_put_id(id, shared_color_transformation_attributes=shared_color_transformation_attributes)
except ApiException as e:
    print("Exception when calling ColorTransformationAttributesApi->color_transformation_attributes_put_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **shared_color_transformation_attributes** | [**SharedColorTransformationAttributes**](SharedColorTransformationAttributes.md)|  | [optional] 

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

