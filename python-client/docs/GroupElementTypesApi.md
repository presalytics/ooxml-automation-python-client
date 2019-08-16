# presalytics_ooxml_automation.GroupElementTypesApi

All URIs are relative to *http://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**group_element_types_get**](GroupElementTypesApi.md#group_element_types_get) | **GET** /slides/GroupElementTypes | GroupElementTypes: List All Possible Types
[**group_element_types_get_id**](GroupElementTypesApi.md#group_element_types_get_id) | **GET** /slides/GroupElementTypes/{id} | GroupElementTypes: Get by Id


# **group_element_types_get**
> list[SlideGroupElementTypes] group_element_types_get()

GroupElementTypes: List All Possible Types

List Types: Use this method to retreive a list of possible options for the GroupElementTypes type. Use the Id from oneof the returned elements on to make changes to elements in the Slides object space.

### Example

```python
from __future__ import print_function
import time
import presalytics_ooxml_automation
from presalytics_ooxml_automation.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = presalytics_ooxml_automation.GroupElementTypesApi()

try:
    # GroupElementTypes: List All Possible Types
    api_response = api_instance.group_element_types_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupElementTypesApi->group_element_types_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SlideGroupElementTypes]**](SlideGroupElementTypes.md)

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

# **group_element_types_get_id**
> SlideGroupElementTypes group_element_types_get_id(id)

GroupElementTypes: Get by Id

Get by Id: Use this method to retrieve a GroupElementTypes object by its primary key (id)

### Example

```python
from __future__ import print_function
import time
import presalytics_ooxml_automation
from presalytics_ooxml_automation.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = presalytics_ooxml_automation.GroupElementTypesApi()
id = 56 # int | The primary key (Id) of the GroupElementTypes object

try:
    # GroupElementTypes: Get by Id
    api_response = api_instance.group_element_types_get_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupElementTypesApi->group_element_types_get_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The primary key (Id) of the GroupElementTypes object | 

### Return type

[**SlideGroupElementTypes**](SlideGroupElementTypes.md)

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

