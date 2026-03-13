# Code API


> **API Documentation** | Generated on 2026-03-13 13:54:30

---

# Code API Documentation

---

## 1. Overview

* **API Name:** Code API
* **Purpose / Business Value:** This API manages nurse/patient call lifecycle and facility resources. It allows creation of calls (with room/floor context), acknowledgement and attendance tracking (including timing metrics like response_time_seconds and attend_delay_seconds), listing of unacknowledged calls, management of rooms, receiving external webhooks, and listing hospitals. The implementation sends out webhooks/websocket notifications after call creation.
* **Base URL:** `None`
* **API Version:** v1
* **Supported Formats:** JSON
* **Detected Frameworks:** Django REST Framework
* **Total Endpoints:** 10
* **Last Updated:** 2026-03-13 13:54:30

### Key Features

* Create and manage patient/nurse calls (create_call, acknowledge_call, attend_call)
* Track call lifecycle timings (created_at, acknowledged_at, attended_at, response_time_seconds, attend_delay_seconds)
* List and filter calls (unacknowledged_calls) and resources (rooms, hospitals)
* Room management (create_room, list_rooms)
* Webhook receiver endpoint for external integrations (webhook_receiver)

### Endpoint Distribution

| Method | Count | Description |
|--------|-------|-------------|
| `GET` | 4 | Data retrieval |
| `POST` | 6 | Resource creation, resource updates |

---

## 2. Authentication & Authorization

* **Authentication Type:** Token
* **How to Obtain Credentials:** No authentication patterns (JWT/Token/OAuth) were detected in the provided code snippets. If authentication is required in other parts of the codebase, provide auth details separately.
* **How to Pass Credentials:** N/A

### Authentication Endpoints

* `POST /create_call` - Authentication
* `POST /acknowledge_call` - Authentication
* `POST /attend_call` - Authentication
* `POST /create_room` - Authentication
* `POST /webhook_receiver` - Authentication

**Example Query Parameter:**

```
?api_key=N/A
```

---

## 3. Common Headers

The following headers are commonly used across all endpoints:

| Header | Required | Description |
|:-------|:--------:|:------------|
| Authorization | Optional | Bearer token or other credential if API is configured to require auth (none detected in provided snippets). |
| Content-Type | Yes | Must be application/json for JSON request bodies. |
| Accept | Optional | application/json (response format expected) |

---

## 4. Error Handling

| Status Code | Meaning |
|:-----------:|:--------|
| 200 | Success |
| 201 | Resource created |
| 400 | Bad Request — validation failed (serializer.is_valid() failures) |
| 401 | Unauthorized (if auth is enabled) |
| 403 | Forbidden (if permissions enforced) |
| 404 | Not Found (get_object_or_404 triggered) |
| 500 | Internal Server Error |

**Error Response Format:**

```json
{
  "drf_validation": {
    "field_errors_example": {
      "room_no": [
        "This field is required."
      ]
    }
  },
  "detail_format": {
    "detail": "Human-readable error message (standard DRF error response)"
  },
  "custom": {
    "error": "Error message",
    "code": "ERROR_CODE"
  }
}
```

### Common Error Types

| Error Code | Description |
|:----------:|:------------|
| `VALIDATION_ERROR` | Input validation failed (serializer errors). |
| `NOT_FOUND` | Requested resource (e.g., Call, Room) does not exist. |
| `CALL_ALREADY_ACKNOWLEDGED` | Attempted to acknowledge a call that already has acknowledged_at set. Endpoint logic checks acknowledged_at before updating. |
| `CALL_ALREADY_ATTENDED` | Attempted to mark a call as attended when attended_at is already set. Endpoint logic checks attended_at before updating. |

---

## 5. Resource Endpoints

### Acknowledge_calls

#### POST – Create Resource

*Create operations using the POST method*

#### Acknowledge Call

**Method:** POST
**Endpoint:** `/acknowledge_call`

🔄 **Idempotent:** This operation is idempotent - multiple identical requests have the same effect as a single request.

🔔 **Webhook:** This endpoint receives webhook callbacks.

**Description:** Marks a Call record as acknowledged by setting acknowledged_at and computing response_time_seconds; used when a nurse (or other staff) confirms they have seen/responded to a call.

**Request Headers:**

| Header | Required | Value |
|:-------|:--------:|:------|
| Authorization | Yes | Token |

**Response**

**Status Code:** `200 OK`

```json
{
  "id (inferred)": 123,
  "created_at (inferred)": "2026-03-13T09:00:00Z",
  "acknowledged_at (inferred)": "2026-03-13T09:00:42Z",
  "response_time_seconds (inferred)": 42
}
```

**Code Examples:**

**cURL:**
```bash
curl -X POST '/acknowledge_call' \
  -H 'Authorization: Token <token> YOUR_TOKEN'
```

**Python (requests):**
```python
import requests

url = '/acknowledge_call'
headers = {
    'Authorization': 'Token <token> YOUR_TOKEN',
}

response = requests.post(url, headers=headers)
print(response.json())
```

**JavaScript (fetch):**
```javascript
const url = '/acknowledge_call';
const options = {
  method: 'POST',
  headers: {
    'Authorization': 'Token <token> YOUR_TOKEN',
  }
};

fetch(url, options)
  .then(response => response.json())
  .then(data => console.log(data));
```

---

*Source: `calls/views.py`*

### Attend_calls

#### POST – Create Resource

*Create operations using the POST method*

#### Attend Call

**Method:** POST
**Endpoint:** `/attend_call`

🔔 **Webhook:** This endpoint receives webhook callbacks.

**Description:** Marks a specific call as attended by setting attended_at (and calculating attend_delay_seconds) and returns the call representation.

**Request Headers:**

| Header | Required | Value |
|:-------|:--------:|:------|
| Authorization | Yes | Token |

**Response**

**Status Code:** `200 OK`

```json
{
  "id": 123,
  "attended_at": "2024-03-01T14:22:35Z",
  "attend_delay_seconds": 42
}
```

**Code Examples:**

**cURL:**
```bash
curl -X POST '/attend_call' \
  -H 'Authorization: Token <token> YOUR_TOKEN'
```

**Python (requests):**
```python
import requests

url = '/attend_call'
headers = {
    'Authorization': 'Token <token> YOUR_TOKEN',
}

response = requests.post(url, headers=headers)
print(response.json())
```

**JavaScript (fetch):**
```javascript
const url = '/attend_call';
const options = {
  method: 'POST',
  headers: {
    'Authorization': 'Token <token> YOUR_TOKEN',
  }
};

fetch(url, options)
  .then(response => response.json())
  .then(data => console.log(data));
```

---

*Source: `calls/views.py`*

### Call_events

#### GET – Fetch Resource

*Retrieve operations using the GET method*

#### Call Events

**Method:** GET
**Endpoint:** `/call_events`

🔄 **Idempotent:** This operation is idempotent - multiple identical requests have the same effect as a single request.

🔔 **Webhook:** This endpoint receives webhook callbacks.

**Description:** Returns all call events with optional filtering by hospital, floor_no, or room_no.
Query params (optional):
  - hospital: string
  - floor_no: int
  - room_no: string

**Request Headers:**

| Header | Required | Value |
|:-------|:--------:|:------|
| Authorization | Yes | Token |

**Response**

**Status Code:** `200 OK`

```json
[
  {
    "id": 1,
    "name": "Example call_events 1"
  },
  {
    "id": 2,
    "name": "Example call_events 2"
  }
]
```

**Code Examples:**

**cURL:**
```bash
curl -X GET '/call_events' \
  -H 'Authorization: Token <token> YOUR_TOKEN'
```

**Python (requests):**
```python
import requests

url = '/call_events'
headers = {
    'Authorization': 'Token <token> YOUR_TOKEN',
}

response = requests.get(url, headers=headers)
print(response.json())
```

**JavaScript (fetch):**
```javascript
const url = '/call_events';
const options = {
  method: 'GET',
  headers: {
    'Authorization': 'Token <token> YOUR_TOKEN',
  }
};

fetch(url, options)
  .then(response => response.json())
  .then(data => console.log(data));
```

---

*Source: `calls/views.py`*

### Create_calls

#### POST – Create Resource

*Create operations using the POST method*

#### Create Call

**Method:** POST
**Endpoint:** `/create_call`

🔔 **Webhook:** This endpoint receives webhook callbacks.

**Description:** Creates a new Call record from the provided data, persists it, and triggers outbound notifications (a webhook and a websocket event).

**Request Headers:**

| Header | Required | Value |
|:-------|:--------:|:------|
| Authorization | Yes | Token |

**Response**

**Status Code:** `200 OK`

```json
{
  "id": 123,
  "room_no": "101",
  "floor_no": 1,
  "hospital_name": "Central Hospital",
  "city": "Metropolis",
  "call_from": "nurse_station",
  "created_at": "2026-03-13T14:22:00Z"
}
```

**Code Examples:**

**cURL:**
```bash
curl -X POST '/create_call' \
  -H 'Authorization: Token <token> YOUR_TOKEN'
```

**Python (requests):**
```python
import requests

url = '/create_call'
headers = {
    'Authorization': 'Token <token> YOUR_TOKEN',
}

response = requests.post(url, headers=headers)
print(response.json())
```

**JavaScript (fetch):**
```javascript
const url = '/create_call';
const options = {
  method: 'POST',
  headers: {
    'Authorization': 'Token <token> YOUR_TOKEN',
  }
};

fetch(url, options)
  .then(response => response.json())
  .then(data => console.log(data));
```

---

*Source: `calls/views.py`*

### Create_hospitals

#### POST – Create Resource

*Create operations using the POST method*

#### Create Hospital

**Method:** POST
**Endpoint:** `/create_hospital`

**Description:** Creates a new Hospital record using the HospitalSerializer and returns the created hospital representation with HTTP 201 on success.

**Request Headers:**

| Header | Required | Value |
|:-------|:--------:|:------|
| Authorization | Yes | Token |

**Response**

**Status Code:** `200 OK`

```json
{
  "id (inferred)": 1,
  "name (inferred)": "Central City Hospital",
  "address (inferred)": "123 Main St, Suite 100",
  "phone (inferred)": "+1-555-0100"
}
```

**Code Examples:**

**cURL:**
```bash
curl -X POST '/create_hospital' \
  -H 'Authorization: Token <token> YOUR_TOKEN'
```

**Python (requests):**
```python
import requests

url = '/create_hospital'
headers = {
    'Authorization': 'Token <token> YOUR_TOKEN',
}

response = requests.post(url, headers=headers)
print(response.json())
```

**JavaScript (fetch):**
```javascript
const url = '/create_hospital';
const options = {
  method: 'POST',
  headers: {
    'Authorization': 'Token <token> YOUR_TOKEN',
  }
};

fetch(url, options)
  .then(response => response.json())
  .then(data => console.log(data));
```

---

*Source: `calls/views.py`*

### Create_rooms

#### POST – Create Resource

*Create operations using the POST method*

#### Create Room

**Method:** POST
**Endpoint:** `/create_room`

**Description:** Creates a new room record associated with a hospital and floor.

**Request Headers:**

| Header | Required | Value |
|:-------|:--------:|:------|
| Authorization | Yes | Token |

**Response**

**Status Code:** `200 OK`

```json
{
  "room_no": "101",
  "floor_no": 3,
  "hospital": 1
}
```

**Code Examples:**

**cURL:**
```bash
curl -X POST '/create_room' \
  -H 'Authorization: Token <token> YOUR_TOKEN'
```

**Python (requests):**
```python
import requests

url = '/create_room'
headers = {
    'Authorization': 'Token <token> YOUR_TOKEN',
}

response = requests.post(url, headers=headers)
print(response.json())
```

**JavaScript (fetch):**
```javascript
const url = '/create_room';
const options = {
  method: 'POST',
  headers: {
    'Authorization': 'Token <token> YOUR_TOKEN',
  }
};

fetch(url, options)
  .then(response => response.json())
  .then(data => console.log(data));
```

---

*Source: `calls/views.py`*

### List_hospitals

#### GET – Fetch Resource

*Retrieve operations using the GET method*

#### List Hospitals

**Method:** GET
**Endpoint:** `/list_hospitals`

🔄 **Idempotent:** This operation is idempotent - multiple identical requests have the same effect as a single request.

**Description:** Primary Purpose: Returns a list of hospitals available in the system as a simple GET endpoint; intended for clients that need to display or select hospitals.

**Request Headers:**

| Header | Required | Value |
|:-------|:--------:|:------|
| Authorization | Yes | Token |

**Response**

**Status Code:** `200 OK`

```json
{
  "type": "object",
  "properties": {
    "count": {
      "type": "integer",
      "example": 4
    },
    "next": {
      "type": "string",
      "example": null
    },
    "previous": {
      "type": "string",
      "example": null
    },
    "results": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {}
      }
    }
  }
}
```

**Code Examples:**

**cURL:**
```bash
curl -X GET '/list_hospitals' \
  -H 'Authorization: Token <token> YOUR_TOKEN'
```

**Python (requests):**
```python
import requests

url = '/list_hospitals'
headers = {
    'Authorization': 'Token <token> YOUR_TOKEN',
}

response = requests.get(url, headers=headers)
print(response.json())
```

**JavaScript (fetch):**
```javascript
const url = '/list_hospitals';
const options = {
  method: 'GET',
  headers: {
    'Authorization': 'Token <token> YOUR_TOKEN',
  }
};

fetch(url, options)
  .then(response => response.json())
  .then(data => console.log(data));
```

---

*Source: `calls/views.py`*

### List_rooms

#### GET – Fetch Resource

*Retrieve operations using the GET method*

#### List Rooms

**Method:** GET
**Endpoint:** `/list_rooms`

🔄 **Idempotent:** This operation is idempotent - multiple identical requests have the same effect as a single request.

**Request Headers:**

| Header | Required | Value |
|:-------|:--------:|:------|
| Authorization | Yes | Token |

**Response**

**Status Code:** `200 OK`

```json
{
  "type": "object",
  "properties": {
    "count": {
      "type": "integer",
      "example": 4
    },
    "next": {
      "type": "string",
      "example": null
    },
    "previous": {
      "type": "string",
      "example": null
    },
    "results": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {}
      }
    }
  }
}
```

**Code Examples:**

**cURL:**
```bash
curl -X GET '/list_rooms' \
  -H 'Authorization: Token <token> YOUR_TOKEN'
```

**Python (requests):**
```python
import requests

url = '/list_rooms'
headers = {
    'Authorization': 'Token <token> YOUR_TOKEN',
}

response = requests.get(url, headers=headers)
print(response.json())
```

**JavaScript (fetch):**
```javascript
const url = '/list_rooms';
const options = {
  method: 'GET',
  headers: {
    'Authorization': 'Token <token> YOUR_TOKEN',
  }
};

fetch(url, options)
  .then(response => response.json())
  .then(data => console.log(data));
```

---

*Source: `calls/views.py`*

### Unacknowledged_calls

#### GET – Fetch Resource

*Retrieve operations using the GET method*

#### Unacknowledged Calls

**Method:** GET
**Endpoint:** `/unacknowledged_calls`

🔄 **Idempotent:** This operation is idempotent - multiple identical requests have the same effect as a single request.

**Request Headers:**

| Header | Required | Value |
|:-------|:--------:|:------|
| Authorization | Yes | Token |

**Response**

**Status Code:** `200 OK`

```json
[
  {
    "id": 1,
    "name": "Example unacknowledged_calls 1"
  },
  {
    "id": 2,
    "name": "Example unacknowledged_calls 2"
  }
]
```

**Code Examples:**

**cURL:**
```bash
curl -X GET '/unacknowledged_calls' \
  -H 'Authorization: Token <token> YOUR_TOKEN'
```

**Python (requests):**
```python
import requests

url = '/unacknowledged_calls'
headers = {
    'Authorization': 'Token <token> YOUR_TOKEN',
}

response = requests.get(url, headers=headers)
print(response.json())
```

**JavaScript (fetch):**
```javascript
const url = '/unacknowledged_calls';
const options = {
  method: 'GET',
  headers: {
    'Authorization': 'Token <token> YOUR_TOKEN',
  }
};

fetch(url, options)
  .then(response => response.json())
  .then(data => console.log(data));
```

---

*Source: `calls/views.py`*

### Webhook_receivers

#### POST – Create Resource

*Create operations using the POST method*

#### Webhook Receiver

**Method:** POST
**Endpoint:** `/webhook_receiver`

🔔 **Webhook:** This endpoint receives webhook callbacks.

**Description:** Primary Purpose: This endpoint receives webhook notifications (an arbitrary JSON payload) and acknowledges receipt by returning a simple status.

**Request Headers:**

| Header | Required | Value |
|:-------|:--------:|:------|
| Authorization | Yes | Token |

**Response**

**Status Code:** `200 OK`

```json
{
  "id": 1,
  "message": "Created successfully"
}
```

**Code Examples:**

**cURL:**
```bash
curl -X POST '/webhook_receiver' \
  -H 'Authorization: Token <token> YOUR_TOKEN'
```

**Python (requests):**
```python
import requests

url = '/webhook_receiver'
headers = {
    'Authorization': 'Token <token> YOUR_TOKEN',
}

response = requests.post(url, headers=headers)
print(response.json())
```

**JavaScript (fetch):**
```javascript
const url = '/webhook_receiver';
const options = {
  method: 'POST',
  headers: {
    'Authorization': 'Token <token> YOUR_TOKEN',
  }
};

fetch(url, options)
  .then(response => response.json())
  .then(data => console.log(data));
```

---

*Source: `calls/views.py`*


---

## 6. Versioning Strategy

* **Strategy:** None detected

---

## 7. Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-03-13 | Initial release with Create Call endpoints, Acknowledge Call endpoints, Attend Call endpoints |

---

## API Documentation Best Practices

* Use nouns instead of verbs in URLs
* Return correct HTTP status codes
* Keep response formats consistent
* Always include example requests and responses
* Clearly document validation rules and edge cases
