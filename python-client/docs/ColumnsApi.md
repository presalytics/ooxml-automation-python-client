# presalytics_ooxml_automation.ColumnsApi

All URIs are relative to *http://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_a_columns_get_id**](ColumnsApi.md#o_a_columns_get_id) | **GET** /tables/Columns/{id} | Columns: Get by Id
[**o_a_columns_get_id_0**](ColumnsApi.md#o_a_columns_get_id_0) | **GET** /charts/Columns/{id} | Columns: Get by Id


# **o_a_columns_get_id**
> TableColumns o_a_columns_get_id(id)

Columns: Get by Id

Get by Id: Use this method to retrieve a Columns object by its primary key (id)

### Example

```python
from __future__ import print_function
import time
import presalytics_ooxml_automation
from presalytics_ooxml_automation.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = presalytics_ooxml_automation.ColumnsApi()
id = 56 # int | The primary key (Id) of the Columns object

try:
    # Columns: Get by Id
    api_response = api_instance.o_a_columns_get_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ColumnsApi->o_a_columns_get_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The primary key (Id) of the Columns object | 

### Return type

[**TableColumns**](TableColumns.md)

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

# **o_a_columns_get_id_0**
> ChartColumns o_a_columns_get_id_0(id)

Columns: Get by Id

Get by Id: Use this method to retrieve a Columns object by its primary key (id)

### Example

```python
from __future__ import print_function
import time
import presalytics_ooxml_automation
from presalytics_ooxml_automation.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = presalytics_ooxml_automation.ColumnsApi()
id = 56 # int | The primary key (Id) of the Columns object

try:
    # Columns: Get by Id
    api_response = api_instance.o_a_columns_get_id_0(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ColumnsApi->o_a_columns_get_id_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The primary key (Id) of the Columns object | 

### Return type

[**ChartColumns**](ChartColumns.md)

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

