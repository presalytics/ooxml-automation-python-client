# presalytics_ooxml_automation.FillMapApi

All URIs are relative to *http://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fill_map_get_id**](FillMapApi.md#fill_map_get_id) | **GET** /shared/FillMap/{id} | FillMap: Get by Id


# **fill_map_get_id**
> SharedFillMap fill_map_get_id(id)

FillMap: Get by Id

Get by Id: Use this method to retrieve a FillMap object by its primary key (id)

### Example

```python
from __future__ import print_function
import time
import presalytics_ooxml_automation
from presalytics_ooxml_automation.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = presalytics_ooxml_automation.FillMapApi()
id = 56 # int | The primary key (Id) of the FillMap object

try:
    # FillMap: Get by Id
    api_response = api_instance.fill_map_get_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FillMapApi->fill_map_get_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The primary key (Id) of the FillMap object | 

### Return type

[**SharedFillMap**](SharedFillMap.md)

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

