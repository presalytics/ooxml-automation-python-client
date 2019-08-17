# presalytics_ooxml_automation.TablesApi

All URIs are relative to *http://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_a_tables_details_id**](TablesApi.md#o_a_tables_details_id) | **GET** /Tables/Details/{Id} | Tables: Retrieve Object Tree
[**o_a_tables_get_id**](TablesApi.md#o_a_tables_get_id) | **GET** /Tables/{Id} | Tables: Get by Id


# **o_a_tables_details_id**
> TableTables o_a_tables_details_id(id)

Tables: Retrieve Object Tree

Returns a nested JSON object of all the Tables base object and all of its descendants that can edited via the corresoponding methods tied to this object.

### Example

```python
from __future__ import print_function
import time
import presalytics_ooxml_automation
from presalytics_ooxml_automation.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = presalytics_ooxml_automation.TablesApi()
id = 56 # int | 

try:
    # Tables: Retrieve Object Tree
    api_response = api_instance.o_a_tables_details_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TablesApi->o_a_tables_details_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**TableTables**](TableTables.md)

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

# **o_a_tables_get_id**
> TableTables o_a_tables_get_id(id)

Tables: Get by Id

Get by Id: Use this method to retrieve a Tables object by its primary key (id)

### Example

```python
from __future__ import print_function
import time
import presalytics_ooxml_automation
from presalytics_ooxml_automation.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = presalytics_ooxml_automation.TablesApi()
id = 56 # int | The primary key (Id) of the Tables object

try:
    # Tables: Get by Id
    api_response = api_instance.o_a_tables_get_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TablesApi->o_a_tables_get_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The primary key (Id) of the Tables object | 

### Return type

[**TableTables**](TableTables.md)

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

