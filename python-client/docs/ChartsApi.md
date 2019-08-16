# presalytics_ooxml_automation.ChartsApi

All URIs are relative to *http://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**charts_details_id**](ChartsApi.md#charts_details_id) | **GET** /Charts/Details/{Id} | Charts: Retrieve Object Tree
[**charts_get_id**](ChartsApi.md#charts_get_id) | **GET** /Charts/{Id} | Charts: Get by Id


# **charts_details_id**
> ChartCharts charts_details_id(id)

Charts: Retrieve Object Tree

Returns a nested JSON object of all the Charts base object and all of its descendants that can edited via the corresoponding methods tied to this object.

### Example

```python
from __future__ import print_function
import time
import presalytics_ooxml_automation
from presalytics_ooxml_automation.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = presalytics_ooxml_automation.ChartsApi()
id = 56 # int | 

try:
    # Charts: Retrieve Object Tree
    api_response = api_instance.charts_details_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChartsApi->charts_details_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ChartCharts**](ChartCharts.md)

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

# **charts_get_id**
> ChartCharts charts_get_id(id)

Charts: Get by Id

Get by Id: Use this method to retrieve a Charts object by its primary key (id)

### Example

```python
from __future__ import print_function
import time
import presalytics_ooxml_automation
from presalytics_ooxml_automation.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = presalytics_ooxml_automation.ChartsApi()
id = 56 # int | The primary key (Id) of the Charts object

try:
    # Charts: Get by Id
    api_response = api_instance.charts_get_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChartsApi->charts_get_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The primary key (Id) of the Charts object | 

### Return type

[**ChartCharts**](ChartCharts.md)

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

