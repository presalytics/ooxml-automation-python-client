# presalytics_ooxml_automation.FillTypesApi

All URIs are relative to *http://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fill_types_get**](FillTypesApi.md#fill_types_get) | **GET** /shared/FillTypes | FillTypes: List All Possible Types
[**fill_types_get_id**](FillTypesApi.md#fill_types_get_id) | **GET** /shared/FillTypes/{id} | FillTypes: Get by Id


# **fill_types_get**
> list[SharedFillTypes] fill_types_get()

FillTypes: List All Possible Types

List Types: Use this method to retreive a list of possible options for the FillTypes type. Use the Id from oneof the returned elements on to make changes to elements in the Shared object space.

### Example

```python
from __future__ import print_function
import time
import presalytics_ooxml_automation
from presalytics_ooxml_automation.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = presalytics_ooxml_automation.FillTypesApi()

try:
    # FillTypes: List All Possible Types
    api_response = api_instance.fill_types_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FillTypesApi->fill_types_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SharedFillTypes]**](SharedFillTypes.md)

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

# **fill_types_get_id**
> SharedFillTypes fill_types_get_id(id)

FillTypes: Get by Id

Get by Id: Use this method to retrieve a FillTypes object by its primary key (id)

### Example

```python
from __future__ import print_function
import time
import presalytics_ooxml_automation
from presalytics_ooxml_automation.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = presalytics_ooxml_automation.FillTypesApi()
id = 56 # int | The primary key (Id) of the FillTypes object

try:
    # FillTypes: Get by Id
    api_response = api_instance.fill_types_get_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FillTypesApi->fill_types_get_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The primary key (Id) of the FillTypes object | 

### Return type

[**SharedFillTypes**](SharedFillTypes.md)

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

