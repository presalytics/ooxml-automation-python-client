# presalytics_ooxml_automation.DashTypesApi

All URIs are relative to *http://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_a_dash_types_get**](DashTypesApi.md#o_a_dash_types_get) | **GET** /shared/DashTypes | DashTypes: List All Possible Types
[**o_a_dash_types_get_id**](DashTypesApi.md#o_a_dash_types_get_id) | **GET** /shared/DashTypes/{id} | DashTypes: Get by Id


# **o_a_dash_types_get**
> list[SharedDashTypes] o_a_dash_types_get()

DashTypes: List All Possible Types

List Types: Use this method to retreive a list of possible options for the DashTypes type. Use the Id from oneof the returned elements on to make changes to elements in the Shared object space.

### Example

```python
from __future__ import print_function
import time
import presalytics_ooxml_automation
from presalytics_ooxml_automation.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = presalytics_ooxml_automation.DashTypesApi()

try:
    # DashTypes: List All Possible Types
    api_response = api_instance.o_a_dash_types_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashTypesApi->o_a_dash_types_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SharedDashTypes]**](SharedDashTypes.md)

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

# **o_a_dash_types_get_id**
> SharedDashTypes o_a_dash_types_get_id(id)

DashTypes: Get by Id

Get by Id: Use this method to retrieve a DashTypes object by its primary key (id)

### Example

```python
from __future__ import print_function
import time
import presalytics_ooxml_automation
from presalytics_ooxml_automation.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = presalytics_ooxml_automation.DashTypesApi()
id = 56 # int | The primary key (Id) of the DashTypes object

try:
    # DashTypes: Get by Id
    api_response = api_instance.o_a_dash_types_get_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashTypesApi->o_a_dash_types_get_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The primary key (Id) of the DashTypes object | 

### Return type

[**SharedDashTypes**](SharedDashTypes.md)

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

