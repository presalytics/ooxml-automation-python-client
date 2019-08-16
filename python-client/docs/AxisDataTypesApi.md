# presalytics_ooxml_automation.AxisDataTypesApi

All URIs are relative to *http://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**axis_data_types_get**](AxisDataTypesApi.md#axis_data_types_get) | **GET** /charts/AxisDataTypes | AxisDataTypes: List All Possible Types
[**axis_data_types_get_id**](AxisDataTypesApi.md#axis_data_types_get_id) | **GET** /charts/AxisDataTypes/{id} | AxisDataTypes: Get by Id


# **axis_data_types_get**
> list[ChartAxisDataTypes] axis_data_types_get()

AxisDataTypes: List All Possible Types

List Types: Use this method to retreive a list of possible options for the AxisDataTypes type. Use the Id from oneof the returned elements on to make changes to elements in the Chart object space.

### Example

```python
from __future__ import print_function
import time
import presalytics_ooxml_automation
from presalytics_ooxml_automation.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = presalytics_ooxml_automation.AxisDataTypesApi()

try:
    # AxisDataTypes: List All Possible Types
    api_response = api_instance.axis_data_types_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AxisDataTypesApi->axis_data_types_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ChartAxisDataTypes]**](ChartAxisDataTypes.md)

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

# **axis_data_types_get_id**
> ChartAxisDataTypes axis_data_types_get_id(id)

AxisDataTypes: Get by Id

Get by Id: Use this method to retrieve a AxisDataTypes object by its primary key (id)

### Example

```python
from __future__ import print_function
import time
import presalytics_ooxml_automation
from presalytics_ooxml_automation.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = presalytics_ooxml_automation.AxisDataTypesApi()
id = 56 # int | The primary key (Id) of the AxisDataTypes object

try:
    # AxisDataTypes: Get by Id
    api_response = api_instance.axis_data_types_get_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AxisDataTypesApi->axis_data_types_get_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The primary key (Id) of the AxisDataTypes object | 

### Return type

[**ChartAxisDataTypes**](ChartAxisDataTypes.md)

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

