# presalytics_ooxml_automation.BackgroundFillsApi

All URIs are relative to *http://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**background_fills_get_id**](BackgroundFillsApi.md#background_fills_get_id) | **GET** /themes/BackgroundFills/{id} | BackgroundFills: Get by Id


# **background_fills_get_id**
> ThemeBackgroundFills background_fills_get_id(id)

BackgroundFills: Get by Id

Get by Id: Use this method to retrieve a BackgroundFills object by its primary key (id)

### Example

```python
from __future__ import print_function
import time
import presalytics_ooxml_automation
from presalytics_ooxml_automation.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = presalytics_ooxml_automation.BackgroundFillsApi()
id = 56 # int | The primary key (Id) of the BackgroundFills object

try:
    # BackgroundFills: Get by Id
    api_response = api_instance.background_fills_get_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BackgroundFillsApi->background_fills_get_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The primary key (Id) of the BackgroundFills object | 

### Return type

[**ThemeBackgroundFills**](ThemeBackgroundFills.md)

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

