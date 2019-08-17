# presalytics_ooxml_automation.EffectTypesApi

All URIs are relative to *http://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_a_effect_types_get**](EffectTypesApi.md#o_a_effect_types_get) | **GET** /shared/EffectTypes | EffectTypes: List All Possible Types
[**o_a_effect_types_get_id**](EffectTypesApi.md#o_a_effect_types_get_id) | **GET** /shared/EffectTypes/{id} | EffectTypes: Get by Id


# **o_a_effect_types_get**
> list[SharedEffectTypes] o_a_effect_types_get()

EffectTypes: List All Possible Types

List Types: Use this method to retreive a list of possible options for the EffectTypes type. Use the Id from oneof the returned elements on to make changes to elements in the Shared object space.

### Example

```python
from __future__ import print_function
import time
import presalytics_ooxml_automation
from presalytics_ooxml_automation.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = presalytics_ooxml_automation.EffectTypesApi()

try:
    # EffectTypes: List All Possible Types
    api_response = api_instance.o_a_effect_types_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EffectTypesApi->o_a_effect_types_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SharedEffectTypes]**](SharedEffectTypes.md)

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

# **o_a_effect_types_get_id**
> SharedEffectTypes o_a_effect_types_get_id(id)

EffectTypes: Get by Id

Get by Id: Use this method to retrieve a EffectTypes object by its primary key (id)

### Example

```python
from __future__ import print_function
import time
import presalytics_ooxml_automation
from presalytics_ooxml_automation.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = presalytics_ooxml_automation.EffectTypesApi()
id = 56 # int | The primary key (Id) of the EffectTypes object

try:
    # EffectTypes: Get by Id
    api_response = api_instance.o_a_effect_types_get_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EffectTypesApi->o_a_effect_types_get_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The primary key (Id) of the EffectTypes object | 

### Return type

[**SharedEffectTypes**](SharedEffectTypes.md)

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

