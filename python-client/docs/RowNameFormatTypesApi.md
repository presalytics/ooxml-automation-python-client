# presalytics_ooxml_automation.RowNameFormatTypesApi

All URIs are relative to *http://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**row_name_format_types_get**](RowNameFormatTypesApi.md#row_name_format_types_get) | **GET** /charts/RowNameFormatTypes | RowNameFormatTypes: List All Possible Types
[**row_name_format_types_get_id**](RowNameFormatTypesApi.md#row_name_format_types_get_id) | **GET** /charts/RowNameFormatTypes/{id} | RowNameFormatTypes: Get by Id


# **row_name_format_types_get**
> list[ChartRowNameFormatTypes] row_name_format_types_get()

RowNameFormatTypes: List All Possible Types

List Types: Use this method to retreive a list of possible options for the RowNameFormatTypes type. Use the Id from oneof the returned elements on to make changes to elements in the Chart object space.

### Example

```python
from __future__ import print_function
import time
import presalytics_ooxml_automation
from presalytics_ooxml_automation.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = presalytics_ooxml_automation.RowNameFormatTypesApi()

try:
    # RowNameFormatTypes: List All Possible Types
    api_response = api_instance.row_name_format_types_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RowNameFormatTypesApi->row_name_format_types_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ChartRowNameFormatTypes]**](ChartRowNameFormatTypes.md)

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

# **row_name_format_types_get_id**
> ChartRowNameFormatTypes row_name_format_types_get_id(id)

RowNameFormatTypes: Get by Id

Get by Id: Use this method to retrieve a RowNameFormatTypes object by its primary key (id)

### Example

```python
from __future__ import print_function
import time
import presalytics_ooxml_automation
from presalytics_ooxml_automation.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = presalytics_ooxml_automation.RowNameFormatTypesApi()
id = 56 # int | The primary key (Id) of the RowNameFormatTypes object

try:
    # RowNameFormatTypes: Get by Id
    api_response = api_instance.row_name_format_types_get_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RowNameFormatTypesApi->row_name_format_types_get_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The primary key (Id) of the RowNameFormatTypes object | 

### Return type

[**ChartRowNameFormatTypes**](ChartRowNameFormatTypes.md)

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

