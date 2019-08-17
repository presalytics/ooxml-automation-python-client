# presalytics_ooxml_automation.DocumentsApi

All URIs are relative to *http://api.presalytics.io/ooxml-automation*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_a_documents_download_document_id**](DocumentsApi.md#o_a_documents_download_document_id) | **GET** /Documents/download/{DocumentId} | Link to download a user&#39;s document. Can only be accessed by the users who owns the document
[**o_a_documents_get_id**](DocumentsApi.md#o_a_documents_get_id) | **GET** /Documents/{id} | Get document information by document id
[**o_a_documents_post**](DocumentsApi.md#o_a_documents_post) | **POST** /Documents | Upload a file into the docAPI, returns a document ids


# **o_a_documents_download_document_id**
> o_a_documents_download_document_id(document_id)

Link to download a user's document. Can only be accessed by the users who owns the document

### Example

```python
from __future__ import print_function
import time
import presalytics_ooxml_automation
from presalytics_ooxml_automation.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = presalytics_ooxml_automation.DocumentsApi()
document_id = 56 # int | 

try:
    # Link to download a user's document. Can only be accessed by the users who owns the document
    api_instance.o_a_documents_download_document_id(document_id)
except ApiException as e:
    print("Exception when calling DocumentsApi->o_a_documents_download_document_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_a_documents_get_id**
> o_a_documents_get_id(id)

Get document information by document id

### Example

```python
from __future__ import print_function
import time
import presalytics_ooxml_automation
from presalytics_ooxml_automation.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = presalytics_ooxml_automation.DocumentsApi()
id = 56 # int | 

try:
    # Get document information by document id
    api_instance.o_a_documents_get_id(id)
except ApiException as e:
    print("Exception when calling DocumentsApi->o_a_documents_get_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_a_documents_post**
> o_a_documents_post()

Upload a file into the docAPI, returns a document ids

### Example

```python
from __future__ import print_function
import time
import presalytics_ooxml_automation
from presalytics_ooxml_automation.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = presalytics_ooxml_automation.DocumentsApi()

try:
    # Upload a file into the docAPI, returns a document ids
    api_instance.o_a_documents_post()
except ApiException as e:
    print("Exception when calling DocumentsApi->o_a_documents_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

