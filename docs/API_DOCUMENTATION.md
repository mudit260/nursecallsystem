# Code API


> **API Documentation** | Generated on 2026-03-19 11:04:44

---

# Code API Documentation

---

## 1. Overview

* **API Name:** Code API
* **Purpose / Business Value:** The Code API provides functionalities for managing calls and rooms in a healthcare setting, allowing users to create, acknowledge, attend calls, and manage hospital information.
* **Base URL:** `None`
* **API Version:** v1
* **Supported Formats:** JSON
* **Detected Frameworks:** Django REST Framework
* **Total Endpoints:** 10
* **Last Updated:** 2026-03-19 11:04:44

### Key Features

* Create and manage calls
* Acknowledge and attend calls
* Manage hospital and room information
* Webhook integration for real-time updates

### Endpoint Distribution

| Method | Count | Description |
|--------|-------|-------------|
| `GET` | 4 | Data retrieval |
| `POST` | 6 | Resource creation |

---

## 2. Authentication & Authorization

* **Authentication Type:** JWT Token
* **How to Obtain Credentials:** Users must authenticate via the login endpoint to receive a JWT token.
* **How to Pass Credentials:** Header

### Authentication Endpoints

* `POST /auth/login` - User login to obtain JWT token

**Example Header:**

```
Authorization: Bearer <token>
```

---

## 3. Common Headers

The following headers are commonly used across all endpoints:

| Header | Required | Description |
|:-------|:--------:|:------------|
| Authorization | Yes | Auth token used for authentication |
| Content-Type | Yes | application/json |

---

## 4. Error Handling

| Status Code | Meaning |
|:-----------:|:--------|
| 200 | Success |
| 400 | Bad Request |
| 401 | Unauthorized |
| 404 | Not Found |

**Error Response Format:**

```json
{
  "status": 400,
  "message": "Error message",
  "data": null
}
```

### Common Error Types

| Error Code | Description |
|:----------:|:------------|
| `VALIDATION_ERROR` | Input validation failed |
| `NOT_FOUND` | Requested resource not found |

---

## 5. Resource Endpoints

### Acknowledge_calls

#### POST – Create Resource

*Create operations using the POST method*

#### Acknowledge Call

**Method:** POST
**Endpoint:** `/acknowledge_call`

🔔 **Webhook:** This endpoint receives webhook callbacks.

**Description:** The /acknowledge_call endpoint is designed to allow a nurse to acknowledge a call identified by its unique ID (pk).

**Request Headers:**

| Header | Required | Value |
|:-------|:--------:|:------|
| Authorization | Yes | Token |

**Response**

**Status Code:** `200 OK`

```json
{
  "id": 1,
  "acknowledged_at": "2023-10-01T12:00:00Z",
  "response_time_seconds": 30
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

**Description:** The /attend_call endpoint allows a nurse to mark a specific call as attended by providing the call's unique identifier (ID).

**Request Headers:**

| Header | Required | Value |
|:-------|:--------:|:------|
| Authorization | Yes | Token |

**Response**

**Status Code:** `200 OK`

```json
{
  "id": 123,
  "attended_at": "2023-10-01T12:00:00Z",
  "attend_delay_seconds": 30
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

**Description:** The POST /create_call endpoint is designed to create a new call record in the system.

**Request Headers:**

| Header | Required | Value |
|:-------|:--------:|:------|
| Authorization | Yes | Token |

**Response**

**Status Code:** `200 OK`

```json
{
  "call_id": 1,
  "room_no": "101",
  "floor_no": "1",
  "hospital_name": "General Hospital",
  "city": "Metropolis",
  "call_from": "Patient",
  "created_at": "2023-10-01T12:00:00Z",
  "status": "New call received"
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

**Description:** The POST /create_hospital endpoint is designed to facilitate the creation of new hospital records in the system.

**Request Headers:**

| Header | Required | Value |
|:-------|:--------:|:------|
| Authorization | Yes | Token |

**Response**

**Status Code:** `200 OK`

```json
{
  "id": 1,
  "name": "General Hospital",
  "location": "123 Main St, Anytown, USA",
  "capacity": 200
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

**Description:** The /create_room endpoint is designed to create a new room within a specified hospital and floor.

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

**Description:** The /list_hospitals endpoint retrieves a list of hospitals available in the system.

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

🔔 **Webhook:** This endpoint receives webhook callbacks.

**Description:** The /list_rooms endpoint retrieves a list of all available rooms in the system, ordered by their room number.

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

**Description:** The POST /webhook_receiver endpoint is designed to receive webhook notifications from various services.

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

## 6. Rate Limiting

**Rate Limiting:** Enabled

* **User:** 100/minute

### Rate Limit Headers

| Header | Description |
|--------|-------------|
| `X-RateLimit-Limit` | Total allowed requests per minute |
| `X-RateLimit-Remaining` | Requests remaining in the current window |

### Retry Strategy

When rate limited (429 status), wait for the time specified in `Retry-After` header.

---

## 7. Versioning Strategy

* **Strategy:** URL-based
* **Current Version:** v1

### Available Versions

* `v1`

---

## 8. Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-03-19 | Initial release with Create Call endpoints, Acknowledge Call endpoints, Attend Call endpoints |

---

## API Documentation Best Practices

* Use nouns instead of verbs in URLs
* Return correct HTTP status codes
* Keep response formats consistent
* Always include example requests and responses
* Clearly document validation rules and edge cases
