# presalytics_ooxml_automation.RowColApi

All URIs are relative to *http://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**row_col_get**](RowColApi.md#row_col_get) | **GET** /charts/RowCol | RowCol: List All Possible Types
[**row_col_get_id**](RowColApi.md#row_col_get_id) | **GET** /charts/RowCol/{id} | RowCol: Get by Id


# **row_col_get**
> list[ChartRowCol] row_col_get()

RowCol: List All Possible Types

List Types: Use this method to retreive a list of possible options for the RowCol type. Use the Id from oneof the returned elements on to make changes to elements in the Chart object space.

### Example

```python
from __future__ import print_function
import time
import presalytics_ooxml_automation
from presalytics_ooxml_automation.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = presalytics_ooxml_automation.RowColApi()

try:
    # RowCol: List All Possible Types
    api_response = api_instance.row_col_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RowColApi->row_col_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ChartRowCol]**](ChartRowCol.md)

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

# **row_col_get_id**
> ChartRowCol row_col_get_id(id)

RowCol: Get by Id

Get by Id: Use this method to retrieve a RowCol object by its primary key (id)

### Example

```python
from __future__ import print_function
import time
import presalytics_ooxml_automation
from presalytics_ooxml_automation.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = presalytics_ooxml_automation.RowColApi()
id = 56 # int | The primary key (Id) of the RowCol object

try:
    # RowCol: Get by Id
    api_response = api_instance.row_col_get_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RowColApi->row_col_get_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The primary key (Id) of the RowCol object | 

### Return type

[**ChartRowCol**](ChartRowCol.md)

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

