# presalytics_ooxml_automation.RowCollectionsApi

All URIs are relative to *http://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_a_row_collections_get_id**](RowCollectionsApi.md#o_a_row_collections_get_id) | **GET** /charts/RowCollections/{id} | RowCollections: Get by Id


# **o_a_row_collections_get_id**
> ChartRowCollections o_a_row_collections_get_id(id)

RowCollections: Get by Id

Get by Id: Use this method to retrieve a RowCollections object by its primary key (id)

### Example

```python
from __future__ import print_function
import time
import presalytics_ooxml_automation
from presalytics_ooxml_automation.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = presalytics_ooxml_automation.RowCollectionsApi()
id = 56 # int | The primary key (Id) of the RowCollections object

try:
    # RowCollections: Get by Id
    api_response = api_instance.o_a_row_collections_get_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RowCollectionsApi->o_a_row_collections_get_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The primary key (Id) of the RowCollections object | 

### Return type

[**ChartRowCollections**](ChartRowCollections.md)

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

