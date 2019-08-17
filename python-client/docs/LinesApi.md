# presalytics_ooxml_automation.LinesApi

All URIs are relative to *http://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_a_lines_get_id**](LinesApi.md#o_a_lines_get_id) | **GET** /shared/Lines/{id} | Lines: Get by Id
[**o_a_lines_put_id**](LinesApi.md#o_a_lines_put_id) | **PUT** /shared/Lines/{id} | Lines: Modify Values


# **o_a_lines_get_id**
> SharedLines o_a_lines_get_id(id)

Lines: Get by Id

Get by Id: Use this method to retrieve a Lines object by its primary key (id)

### Example

```python
from __future__ import print_function
import time
import presalytics_ooxml_automation
from presalytics_ooxml_automation.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = presalytics_ooxml_automation.LinesApi()
id = 56 # int | The primary key (Id) of the Lines object

try:
    # Lines: Get by Id
    api_response = api_instance.o_a_lines_get_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinesApi->o_a_lines_get_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The primary key (Id) of the Lines object | 

### Return type

[**SharedLines**](SharedLines.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request.  Please check for valid Id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_a_lines_put_id**
> o_a_lines_put_id(id, shared_lines=shared_lines)

Lines: Modify Values

PUT: Use this method for simple updates to Lines objects.   Please Note: Using this method sidesteps some data validation steps executed by base objects.  Please review the documentation and ECMA-376 prior to using this method. Per IETF 7231, all fields must be include in PUT requests, even though user and timestamp fields will be modified by the server.

### Example

```python
from __future__ import print_function
import time
import presalytics_ooxml_automation
from presalytics_ooxml_automation.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = presalytics_ooxml_automation.LinesApi()
id = 56 # int | 
shared_lines = presalytics_ooxml_automation.SharedLines() # SharedLines |  (optional)

try:
    # Lines: Modify Values
    api_instance.o_a_lines_put_id(id, shared_lines=shared_lines)
except ApiException as e:
    print("Exception when calling LinesApi->o_a_lines_put_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **shared_lines** | [**SharedLines**](SharedLines.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**204** |  |  -  |
**400** | Bad request.  Please check for valid Id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

