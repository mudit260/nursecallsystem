# Sample API


> **API Documentation** | Generated on 2026-03-02 14:31:25

---

# Sample API Documentation

---

## 1. Overview

* **API Name:** Sample API
* **Purpose / Business Value:** Provides a simple endpoint to create Call records and immediately dispatch notification payloads (webhook/websocket) containing call metadata such as call_id, room_no and floor_no. Intended for systems that need to register a new call and notify downstream listeners in real time.
* **Base URL:** `https://api.example.com`
* **API Version:** v1
* **Supported Formats:** JSON
* **Detected Frameworks:** Django REST Framework
* **Total Endpoints:** 10
* **Last Updated:** 2026-03-02 14:31:25

### Key Features

* Create call records via POST /create_call
* Input validation using Django REST Framework serializers
* Emits a webhook/websocket payload after a successful create

### Endpoint Distribution

| Method | Count | Description |
|--------|-------|-------------|
| `GET` | 4 | Data retrieval |
| `POST` | 6 | Resource creation, data retrieval |

---

## 2. Authentication & Authorization

* **Authentication Type:** Token
* **How to Obtain Credentials:** This codebase excerpt contains no authentication patterns. Endpoints appear to be unauthenticated in the provided code. If authentication is added, it would typically be configured in Django REST Framework settings (e.g., TokenAuthentication or JWT) and documented separately.
* **How to Pass Credentials:** N/A

### Authentication Endpoints

* `POST /create_call` - Authentication
* `POST /acknowledge_call` - Authentication
* `POST /attend_call` - Authentication
* `GET /unacknowledged_calls` - Authentication
* `POST /create_room` - Authentication

**Example Query Parameter:**

```
?api_key=N/A
```

---

## 3. Common Headers

The following headers are commonly used across all endpoints:

| Header | Required | Description |
|:-------|:--------:|:------------|
| Authorization | Optional | Not required by the provided endpoints. Present only if auth is later enabled. |
| Content-Type | Yes | Must be application/json for request bodies. |

---

## 4. Error Handling

| Status Code | Meaning |
|:-----------:|:--------|
| 201 | Created - call resource successfully created |
| 400 | Bad Request - input validation failed |
| 500 | Internal Server Error - unexpected error (e.g., webhook delivery failure) |

**Error Response Format:**

```json
{
  "status": 400,
  "message": "Short human-readable error message or field error map",
  "data": null
}
```

### Common Error Types

| Error Code | Description |
|:----------:|:------------|
| `VALIDATION_ERROR` | Input validation failed; serializer.errors will contain details keyed by field. |
| `WEBHOOK_ERROR` | Post-save webhook or websocket notification failed; the call was created but notification delivery errored. |

---

## 5. Resource Endpoints

### Acknowledge_calls

#### POST – Create Resource

*Create operations using the POST method*

#### Acknowledge Call

**Method:** POST
**Endpoint:** `/acknowledge_call`

🔔 **Webhook:** This endpoint receives webhook callbacks.

**Description:** Primary Purpose: Acknowledge a nurse call by marking the Call record's acknowledged_at timestamp and computing response_time_seconds; returns the serialized Call.

**Request Headers:**

| Header | Required | Value |
|:-------|:--------:|:------|
| Authorization | Yes | Token |

**Response**

**Status Code:** `200 OK`

```json
{
  "id": 123,
  "acknowledged_at": "2026-03-02T14:12:30Z",
  "response_time_seconds": 42
}
```

**Code Examples:**

**cURL:**
```bash
curl -X POST 'https://api.example.com/acknowledge_call' \
  -H 'Authorization: Token <token> YOUR_TOKEN'
```

**Python (requests):**
```python
import requests

url = 'https://api.example.com/acknowledge_call'
headers = {
    'Authorization': 'Token <token> YOUR_TOKEN',
}

response = requests.post(url, headers=headers)
print(response.json())
```

**JavaScript (fetch):**
```javascript
const url = 'https://api.example.com/acknowledge_call';
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

🔄 **Idempotent:** This operation is idempotent - multiple identical requests have the same effect as a single request.

🔔 **Webhook:** This endpoint receives webhook callbacks.

**Description:** Primary purpose: mark a Call record as attended by setting its attended_at timestamp and computing attend_delay_seconds, then return the serialized Call.

**Request Headers:**

| Header | Required | Value |
|:-------|:--------:|:------|
| Authorization | Yes | Token |

**Response**

**Status Code:** `200 OK`

```json
{
  "id": 456,
  "created_at": "2026-03-02T10:00:00Z",
  "acknowledged_at": "2026-03-02T10:05:00Z",
  "attended_at": "2026-03-02T10:06:30Z",
  "attend_delay_seconds": 90
}
```

**Code Examples:**

**cURL:**
```bash
curl -X POST 'https://api.example.com/attend_call' \
  -H 'Authorization: Token <token> YOUR_TOKEN'
```

**Python (requests):**
```python
import requests

url = 'https://api.example.com/attend_call'
headers = {
    'Authorization': 'Token <token> YOUR_TOKEN',
}

response = requests.post(url, headers=headers)
print(response.json())
```

**JavaScript (fetch):**
```javascript
const url = 'https://api.example.com/attend_call';
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

**Description:** Returns all call events, optionally filtered by hospital, floor_no, or room_no, and is intended for listing call events used by dashboards, reporting, or monitoring.

**Request Headers:**

| Header | Required | Value |
|:-------|:--------:|:------|
| Authorization | Yes | Token |

**Response**

**Status Code:** `200 OK`

```json
{
  "inferred_call_events": [
    {
      "hospital_name": "Central Hospital (inferred)",
      "floor_no": 2,
      "room_no": "210A (inferred)"
    }
  ]
}
```

**Code Examples:**

**cURL:**
```bash
curl -X GET 'https://api.example.com/call_events' \
  -H 'Authorization: Token <token> YOUR_TOKEN'
```

**Python (requests):**
```python
import requests

url = 'https://api.example.com/call_events'
headers = {
    'Authorization': 'Token <token> YOUR_TOKEN',
}

response = requests.get(url, headers=headers)
print(response.json())
```

**JavaScript (fetch):**
```javascript
const url = 'https://api.example.com/call_events';
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

**Description:** Creates a new Call record and returns the created resource.

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
  "floor_no": "1",
  "hospital_name": "General Hospital",
  "city": "Metropolis",
  "call_from": "nurse_station",
  "created_at": "2026-03-02T14:30:00Z"
}
```

**Code Examples:**

**cURL:**
```bash
curl -X POST 'https://api.example.com/create_call' \
  -H 'Authorization: Token <token> YOUR_TOKEN'
```

**Python (requests):**
```python
import requests

url = 'https://api.example.com/create_call'
headers = {
    'Authorization': 'Token <token> YOUR_TOKEN',
}

response = requests.post(url, headers=headers)
print(response.json())
```

**JavaScript (fetch):**
```javascript
const url = 'https://api.example.com/create_call';
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

**Description:** Creates a new hospital record using the HospitalSerializer and returns the created hospital representation with HTTP 201 on success or HTTP 400 if validation fails.

**Request Headers:**

| Header | Required | Value |
|:-------|:--------:|:------|
| Authorization | Yes | Token |

**Response**

**Status Code:** `200 OK`

```json
{
  "id": 123,
  "name": "Central City Hospital",
  "_inferred_fields": [
    "id",
    "name"
  ]
}
```

**Code Examples:**

**cURL:**
```bash
curl -X POST 'https://api.example.com/create_hospital' \
  -H 'Authorization: Token <token> YOUR_TOKEN'
```

**Python (requests):**
```python
import requests

url = 'https://api.example.com/create_hospital'
headers = {
    'Authorization': 'Token <token> YOUR_TOKEN',
}

response = requests.post(url, headers=headers)
print(response.json())
```

**JavaScript (fetch):**
```javascript
const url = 'https://api.example.com/create_hospital';
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

**Description:** Creates a new room tied to a specific hospital and floor.

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
curl -X POST 'https://api.example.com/create_room' \
  -H 'Authorization: Token <token> YOUR_TOKEN'
```

**Python (requests):**
```python
import requests

url = 'https://api.example.com/create_room'
headers = {
    'Authorization': 'Token <token> YOUR_TOKEN',
}

response = requests.post(url, headers=headers)
print(response.json())
```

**JavaScript (fetch):**
```javascript
const url = 'https://api.example.com/create_room';
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

**Description:** Returns a simple list of available hospitals.

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
curl -X GET 'https://api.example.com/list_hospitals' \
  -H 'Authorization: Token <token> YOUR_TOKEN'
```

**Python (requests):**
```python
import requests

url = 'https://api.example.com/list_hospitals'
headers = {
    'Authorization': 'Token <token> YOUR_TOKEN',
}

response = requests.get(url, headers=headers)
print(response.json())
```

**JavaScript (fetch):**
```javascript
const url = 'https://api.example.com/list_hospitals';
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

**Description:** Returns a list of all Room records (serialized with RoomSerializer) ordered by room_no.

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
curl -X GET 'https://api.example.com/list_rooms' \
  -H 'Authorization: Token <token> YOUR_TOKEN'
```

**Python (requests):**
```python
import requests

url = 'https://api.example.com/list_rooms'
headers = {
    'Authorization': 'Token <token> YOUR_TOKEN',
}

response = requests.get(url, headers=headers)
print(response.json())
```

**JavaScript (fetch):**
```javascript
const url = 'https://api.example.com/list_rooms';
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

🔔 **Webhook:** This endpoint receives webhook callbacks.

**Description:** Returns a list of call records that have not yet been acknowledged (acknowledged_at is null), ordered by creation time.

**Request Headers:**

| Header | Required | Value |
|:-------|:--------:|:------|
| Authorization | Yes | Token |

**Response**

**Status Code:** `200 OK`

```json
{
  "calls": [
    {
      "id (inferred)": 123,
      "created_at (inferred)": "2026-02-28T09:15:00Z",
      "acknowledged_at (inferred)": null
    },
    {
      "id (inferred)": 124,
      "created_at (inferred)": "2026-02-28T09:20:30Z",
      "acknowledged_at (inferred)": null
    }
  ]
}
```

**Code Examples:**

**cURL:**
```bash
curl -X GET 'https://api.example.com/unacknowledged_calls' \
  -H 'Authorization: Token <token> YOUR_TOKEN'
```

**Python (requests):**
```python
import requests

url = 'https://api.example.com/unacknowledged_calls'
headers = {
    'Authorization': 'Token <token> YOUR_TOKEN',
}

response = requests.get(url, headers=headers)
print(response.json())
```

**JavaScript (fetch):**
```javascript
const url = 'https://api.example.com/unacknowledged_calls';
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

**Description:** Primary Purpose: This endpoint receives webhook notifications (HTTP POST) from this or external services, logs the incoming payload, and acknowledges receipt with a 200 OK and a brief JSON confirmation.

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
curl -X POST 'https://api.example.com/webhook_receiver' \
  -H 'Authorization: Token <token> YOUR_TOKEN'
```

**Python (requests):**
```python
import requests

url = 'https://api.example.com/webhook_receiver'
headers = {
    'Authorization': 'Token <token> YOUR_TOKEN',
}

response = requests.post(url, headers=headers)
print(response.json())
```

**JavaScript (fetch):**
```javascript
const url = 'https://api.example.com/webhook_receiver';
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

## 6. Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-03-02 | Initial release with Create Call endpoints, Acknowledge Call endpoints, Attend Call endpoints |

---

## API Documentation Best Practices

* Use nouns instead of verbs in URLs
* Return correct HTTP status codes
* Keep response formats consistent
* Always include example requests and responses
* Clearly document validation rules and edge cases
