# presalytics_ooxml_automation.ColumnCollectionsApi

All URIs are relative to *http://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**column_collections_get_id**](ColumnCollectionsApi.md#column_collections_get_id) | **GET** /charts/ColumnCollections/{id} | ColumnCollections: Get by Id


# **column_collections_get_id**
> ChartColumnCollections column_collections_get_id(id)

ColumnCollections: Get by Id

Get by Id: Use this method to retrieve a ColumnCollections object by its primary key (id)

### Example

```python
from __future__ import print_function
import time
import presalytics_ooxml_automation
from presalytics_ooxml_automation.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = presalytics_ooxml_automation.ColumnCollectionsApi()
id = 56 # int | The primary key (Id) of the ColumnCollections object

try:
    # ColumnCollections: Get by Id
    api_response = api_instance.column_collections_get_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ColumnCollectionsApi->column_collections_get_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The primary key (Id) of the ColumnCollections object | 

### Return type

[**ChartColumnCollections**](ChartColumnCollections.md)

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

