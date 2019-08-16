# presalytics_ooxml_automation.SlidesApi

All URIs are relative to *http://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**slides_details_id**](SlidesApi.md#slides_details_id) | **GET** /Slides/Details/{Id} | Slides: Retrieve Object Tree
[**slides_get_id**](SlidesApi.md#slides_get_id) | **GET** /Slides/{Id} | Slides: Get by Id


# **slides_details_id**
> SlideSlides slides_details_id(id)

Slides: Retrieve Object Tree

Returns a nested JSON object of all the Slides base object and all of its descendants that can edited via the corresoponding methods tied to this object.

### Example

```python
from __future__ import print_function
import time
import presalytics_ooxml_automation
from presalytics_ooxml_automation.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = presalytics_ooxml_automation.SlidesApi()
id = 56 # int | 

try:
    # Slides: Retrieve Object Tree
    api_response = api_instance.slides_details_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlidesApi->slides_details_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**SlideSlides**](SlideSlides.md)

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

# **slides_get_id**
> SlideSlides slides_get_id(id)

Slides: Get by Id

Get by Id: Use this method to retrieve a Slides object by its primary key (id)

### Example

```python
from __future__ import print_function
import time
import presalytics_ooxml_automation
from presalytics_ooxml_automation.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = presalytics_ooxml_automation.SlidesApi()
id = 56 # int | The primary key (Id) of the Slides object

try:
    # Slides: Get by Id
    api_response = api_instance.slides_get_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SlidesApi->slides_get_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The primary key (Id) of the Slides object | 

### Return type

[**SlideSlides**](SlideSlides.md)

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

