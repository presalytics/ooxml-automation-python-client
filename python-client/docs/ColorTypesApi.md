# presalytics_ooxml_automation.ColorTypesApi

All URIs are relative to *http://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**color_types_get**](ColorTypesApi.md#color_types_get) | **GET** /shared/ColorTypes | ColorTypes: List All Possible Types
[**color_types_get_id**](ColorTypesApi.md#color_types_get_id) | **GET** /shared/ColorTypes/{id} | ColorTypes: Get by Id


# **color_types_get**
> list[SharedColorTypes] color_types_get()

ColorTypes: List All Possible Types

List Types: Use this method to retreive a list of possible options for the ColorTypes type. Use the Id from oneof the returned elements on to make changes to elements in the Shared object space.

### Example

```python
from __future__ import print_function
import time
import presalytics_ooxml_automation
from presalytics_ooxml_automation.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = presalytics_ooxml_automation.ColorTypesApi()

try:
    # ColorTypes: List All Possible Types
    api_response = api_instance.color_types_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ColorTypesApi->color_types_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SharedColorTypes]**](SharedColorTypes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **color_types_get_id**
> SharedColorTypes color_types_get_id(id)

ColorTypes: Get by Id

Get by Id: Use this method to retrieve a ColorTypes object by its primary key (id)

### Example

```python
from __future__ import print_function
import time
import presalytics_ooxml_automation
from presalytics_ooxml_automation.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = presalytics_ooxml_automation.ColorTypesApi()
id = 56 # int | The primary key (Id) of the ColorTypes object

try:
    # ColorTypes: Get by Id
    api_response = api_instance.color_types_get_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ColorTypesApi->color_types_get_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The primary key (Id) of the ColorTypes object | 

### Return type

[**SharedColorTypes**](SharedColorTypes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

