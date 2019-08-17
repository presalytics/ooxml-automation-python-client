# presalytics_ooxml_automation.IntensityApi

All URIs are relative to *http://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_a_intensity_get**](IntensityApi.md#o_a_intensity_get) | **GET** /themes/Intensity | Intensity: List All Possible Types
[**o_a_intensity_get_id**](IntensityApi.md#o_a_intensity_get_id) | **GET** /themes/Intensity/{id} | Intensity: Get by Id


# **o_a_intensity_get**
> list[ThemeIntensity] o_a_intensity_get()

Intensity: List All Possible Types

List Types: Use this method to retreive a list of possible options for the Intensity type. Use the Id from oneof the returned elements on to make changes to elements in the Themes object space.

### Example

```python
from __future__ import print_function
import time
import presalytics_ooxml_automation
from presalytics_ooxml_automation.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = presalytics_ooxml_automation.IntensityApi()

try:
    # Intensity: List All Possible Types
    api_response = api_instance.o_a_intensity_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntensityApi->o_a_intensity_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ThemeIntensity]**](ThemeIntensity.md)

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

# **o_a_intensity_get_id**
> ThemeIntensity o_a_intensity_get_id(id)

Intensity: Get by Id

Get by Id: Use this method to retrieve a Intensity object by its primary key (id)

### Example

```python
from __future__ import print_function
import time
import presalytics_ooxml_automation
from presalytics_ooxml_automation.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = presalytics_ooxml_automation.IntensityApi()
id = 56 # int | The primary key (Id) of the Intensity object

try:
    # Intensity: Get by Id
    api_response = api_instance.o_a_intensity_get_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntensityApi->o_a_intensity_get_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The primary key (Id) of the Intensity object | 

### Return type

[**ThemeIntensity**](ThemeIntensity.md)

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

