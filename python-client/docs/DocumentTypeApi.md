# presalytics_ooxml_automation.DocumentTypeApi

All URIs are relative to *http://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_a_document_type_get**](DocumentTypeApi.md#o_a_document_type_get) | **GET** /documents/DocumentType | DocumentType: List All Possible Types
[**o_a_document_type_get_id**](DocumentTypeApi.md#o_a_document_type_get_id) | **GET** /documents/DocumentType/{id} | DocumentType: Get by Id


# **o_a_document_type_get**
> list[DocumentType] o_a_document_type_get()

DocumentType: List All Possible Types

List Types: Use this method to retreive a list of possible options for the DocumentType type. Use the Id from oneof the returned elements on to make changes to elements in the Documents object space.

### Example

```python
from __future__ import print_function
import time
import presalytics_ooxml_automation
from presalytics_ooxml_automation.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = presalytics_ooxml_automation.DocumentTypeApi()

try:
    # DocumentType: List All Possible Types
    api_response = api_instance.o_a_document_type_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentTypeApi->o_a_document_type_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[DocumentType]**](DocumentType.md)

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

# **o_a_document_type_get_id**
> DocumentType o_a_document_type_get_id(id)

DocumentType: Get by Id

Get by Id: Use this method to retrieve a DocumentType object by its primary key (id)

### Example

```python
from __future__ import print_function
import time
import presalytics_ooxml_automation
from presalytics_ooxml_automation.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = presalytics_ooxml_automation.DocumentTypeApi()
id = 56 # int | The primary key (Id) of the DocumentType object

try:
    # DocumentType: Get by Id
    api_response = api_instance.o_a_document_type_get_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentTypeApi->o_a_document_type_get_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The primary key (Id) of the DocumentType object | 

### Return type

[**DocumentType**](DocumentType.md)

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

