# presalytics_ooxml_automation.RowsApi

All URIs are relative to *http://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rows_get_id**](RowsApi.md#rows_get_id) | **GET** /tables/Rows/{id} | Rows: Get by Id
[**rows_get_id_0**](RowsApi.md#rows_get_id_0) | **GET** /charts/Rows/{id} | Rows: Get by Id


# **rows_get_id**
> TableRows rows_get_id(id)

Rows: Get by Id

Get by Id: Use this method to retrieve a Rows object by its primary key (id)

### Example

```python
from __future__ import print_function
import time
import presalytics_ooxml_automation
from presalytics_ooxml_automation.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = presalytics_ooxml_automation.RowsApi()
id = 56 # int | The primary key (Id) of the Rows object

try:
    # Rows: Get by Id
    api_response = api_instance.rows_get_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RowsApi->rows_get_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The primary key (Id) of the Rows object | 

### Return type

[**TableRows**](TableRows.md)

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

# **rows_get_id_0**
> ChartRows rows_get_id_0(id)

Rows: Get by Id

Get by Id: Use this method to retrieve a Rows object by its primary key (id)

### Example

```python
from __future__ import print_function
import time
import presalytics_ooxml_automation
from presalytics_ooxml_automation.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = presalytics_ooxml_automation.RowsApi()
id = 56 # int | The primary key (Id) of the Rows object

try:
    # Rows: Get by Id
    api_response = api_instance.rows_get_id_0(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RowsApi->rows_get_id_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The primary key (Id) of the Rows object | 

### Return type

[**ChartRows**](ChartRows.md)

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

