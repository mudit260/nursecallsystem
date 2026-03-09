# Code API


> **API Documentation** | Generated on 2026-03-09 11:38:39

---

# Code API Documentation

---

## 1. Overview

* **API Name:** Code API
* **Purpose / Business Value:** Manage and track nurse/patient calls and related resources (rooms, hospitals). Provides endpoints to create calls, acknowledge and attend to calls, list unacknowledged calls, manage rooms and hospitals, and receive webhook notifications for call events.
* **Base URL:** `None`
* **API Version:** v1
* **Supported Formats:** JSON
* **Detected Frameworks:** Django REST Framework
* **Total Endpoints:** 10
* **Last Updated:** 2026-03-09 11:38:39

### Key Features

* Call lifecycle management (create, acknowledge, attend)
* Unacknowledged call listing for dashboards/triage
* Room and hospital creation and listing
* Webhook receiver endpoint for external integrations/notifications
* Server-side validation using Django REST Framework serializers

### Endpoint Distribution

| Method | Count | Description |
|--------|-------|-------------|
| `GET` | 4 | Data retrieval |
| `POST` | 6 | Resource creation, data retrieval |

---

## 2. Authentication & Authorization

* **Authentication Type:** Token
* **How to Obtain Credentials:** No authentication patterns were detected in the provided code snippets. Endpoints appear to be implemented without auth checks. If authentication is required in your deployment, add DRF authentication classes (Token/JWT) and update this section accordingly.
* **How to Pass Credentials:** None

### Authentication Endpoints

* `POST /create_call` - Authentication
* `POST /acknowledge_call` - Authentication
* `POST /attend_call` - Authentication
* `POST /create_room` - Authentication
* `GET /list_rooms` - Authentication

**Example Query Parameter:**

```
?api_key=None
```

---

## 3. Common Headers

The following headers are commonly used across all endpoints:

| Header | Required | Description |
|:-------|:--------:|:------------|
| Authorization | Optional | Optional auth token header if your deployment adds auth (e.g., 'Authorization: Bearer <token>'). Not required in the provided code. |
| Content-Type | Yes | Must be 'application/json' for endpoints that accept a JSON body (POST endpoints such as /create_call, /create_room, /create_hospital). |
| Accept | Optional | Clients should accept 'application/json'. |

---

## 4. Error Handling

| Status Code | Meaning |
|:-----------:|:--------|
| 201 | Created (resource successfully created, e.g., POST /create_call) |
| 200 | Success |
| 400 | Bad Request (validation errors from serializers) |
| 404 | Not Found (e.g. call/room/hospital not found; get_object_or_404 used) |
| 500 | Internal Server Error |

**Error Response Format:**

```json
{
  "status": 400,
  "message": "Human readable error message (e.g. 'This field is required.')",
  "data": null
}
```

### Common Error Types

| Error Code | Description |
|:----------:|:------------|
| `VALIDATION_ERROR` | Input validation failed (serializer.is_valid() returned False). Response includes field-level errors. |
| `NOT_FOUND` | Requested resource does not exist (raised via get_object_or_404). |
| `ALREADY_ACKNOWLEDGED` | Attempted to acknowledge a call that already has an acknowledged_at timestamp. |
| `ALREADY_ATTENDED` | Attempted to mark a call as attended that already has an attended_at timestamp. |

---

## 5. Resource Endpoints

### Acknowledge_calls

#### POST – Create Resource

*Create operations using the POST method*

#### Acknowledge Call

**Method:** POST
**Endpoint:** `/acknowledge_call`

🔔 **Webhook:** This endpoint receives webhook callbacks.

**Description:** Primary Purpose: Acknowledge an existing Call record so the system records when a nurse (or other staff) accepted the call; it sets acknowledged_at, computes response_time_seconds, persists the Call, and emits a websocket notification and a webhook.

**Request Headers:**

| Header | Required | Value |
|:-------|:--------:|:------|
| Authorization | Yes | Token |

**Response**

**Status Code:** `200 OK`

```json
{
  "id": 123,
  "created_at": "2026-03-09T10:15:00Z",
  "acknowledged_at": "2026-03-09T10:17:30Z",
  "response_time_seconds": 150
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

🔄 **Idempotent:** This operation is idempotent - multiple identical requests have the same effect as a single request.

🔔 **Webhook:** This endpoint receives webhook callbacks.

**Description:** Marks a Call record as attended by setting its attended_at timestamp and calculating attend_delay_seconds, then returns the serialized Call.

**Request Headers:**

| Header | Required | Value |
|:-------|:--------:|:------|
| Authorization | Yes | Token |

**Response**

**Status Code:** `200 OK`

```json
{
  "id": 42,
  "attended_at": "2026-03-09T12:34:56Z",
  "attend_delay_seconds": 120
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

**Description:** Creates a new call record (e.

**Request Headers:**

| Header | Required | Value |
|:-------|:--------:|:------|
| Authorization | Yes | Token |

**Response**

**Status Code:** `200 OK`

```json
{
  "call_id": 12345,
  "room_no": "101",
  "floor_no": 2,
  "hospital_name": "General Hospital",
  "city": "Springfield",
  "call_from": "nurse_station",
  "created_at": "2025-03-09T12:34:56Z"
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

**Description:** Creates a new hospital record from the JSON body and returns the created hospital representation; it is intended for clients that need to add hospital entities to the system.

**Request Headers:**

| Header | Required | Value |
|:-------|:--------:|:------|
| Authorization | Yes | Token |

**Response**

**Status Code:** `200 OK`

```json
{
  "id (inferred)": 42,
  "name (inferred)": "City General Hospital",
  "address (inferred)": "123 Main St, Springfield",
  "phone (inferred)": "+1-555-0100",
  "email (inferred)": "contact@cityhospital.example",
  "capacity (inferred)": 250
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

**Description:** Creates a Room record linking a room number to a specific hospital and floor.

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

**Description:** Returns a list of all Room records ordered by room_no.

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

**Description:** Primary Purpose: Accepts incoming webhook notifications and acknowledges receipt.

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

* **Strategy:** None (no API versioning detected in provided code)

---

## 7. Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-03-09 | Initial release with Create Call endpoints, Acknowledge Call endpoints, Attend Call endpoints |

---

## API Documentation Best Practices

* Use nouns instead of verbs in URLs
* Return correct HTTP status codes
* Keep response formats consistent
* Always include example requests and responses
* Clearly document validation rules and edge cases
