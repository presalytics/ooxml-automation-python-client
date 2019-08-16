# presalytics_ooxml_automation.FillsApi

All URIs are relative to *http://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fills_get_id**](FillsApi.md#fills_get_id) | **GET** /themes/Fills/{id} | Fills: Get by Id


# **fills_get_id**
> ThemeFills fills_get_id(id)

Fills: Get by Id

Get by Id: Use this method to retrieve a Fills object by its primary key (id)

### Example

```python
from __future__ import print_function
import time
import presalytics_ooxml_automation
from presalytics_ooxml_automation.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = presalytics_ooxml_automation.FillsApi()
id = 56 # int | The primary key (Id) of the Fills object

try:
    # Fills: Get by Id
    api_response = api_instance.fills_get_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FillsApi->fills_get_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The primary key (Id) of the Fills object | 

### Return type

[**ThemeFills**](ThemeFills.md)

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

