# Code API


> **API Documentation** | Generated on 2026-03-24 15:36:11

---

# Code API Documentation

---

## 1. Overview

* **API Name:** Code API
* **Purpose / Business Value:** The Code API facilitates the management of calls and rooms in a healthcare environment, allowing for the creation, acknowledgment, and attendance of calls, as well as the management of hospitals and rooms.
* **Base URL:** `None`
* **API Version:** v1
* **Supported Formats:** JSON
* **Detected Frameworks:** Django, Django REST Framework
* **Total Endpoints:** 21
* **Last Updated:** 2026-03-24 15:36:11

### Key Features

* Create and manage calls
* Acknowledge and attend calls
* Manage hospitals and rooms
* Webhook support for real-time updates

### Endpoint Distribution

| Method | Count | Description |
|--------|-------|-------------|
| `GET` | 9 | Data retrieval |
| `POST` | 12 | Resource creation, resource updates |

---

## 2. Authentication & Authorization

* **Authentication Type:** JWT Token
* **How to Obtain Credentials:** Users can obtain a JWT token by logging in through the authentication endpoint.
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
| Authorization | Yes | Auth token for accessing protected endpoints |
| Content-Type | Yes | Specifies the media type of the resource, typically application/json |

---

## 4. Error Handling

| Status Code | Meaning |
|:-----------:|:--------|
| 200 | Success |
| 400 | Bad Request - Input validation failed or incorrect data format. |
| 401 | Unauthorized - Authentication credentials are missing or invalid. |

**Error Response Format:**

```json
{
  "status": 400,
  "message": "Error message detailing the issue",
  "data": null
}
```

### Common Error Types

| Error Code | Description |
|:----------:|:------------|
| `VALIDATION_ERROR` | Input validation failed due to incorrect or missing data. |
| `NOT_FOUND` | Requested resource was not found. |

---

## 5. Resource Endpoints

### Acknowledge_calls

#### POST – Create Resource

*Create operations using the POST method*

#### Acknowledge Call

**Method:** POST
**Endpoint:** `/acknowledge_call`

🔔 **Webhook:** This endpoint receives webhook callbacks.

**Description:** The /acknowledge_call endpoint is designed to allow a nurse to acknowledge a specific call identified by its primary key (pk).

**Request Headers:**

| Header | Required | Value |
|:-------|:--------:|:------|
| Authorization | Yes | Token |

**Response**

**Status Code:** `200 OK`

```json
{
  "type": {
    "id": 1,
    "name": "Sample type"
  },
  "properties": "sample_properties"
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

### Admins

#### GET – Fetch Resource

*Retrieve operations using the GET method*

#### Admin.Site.Urls

**Method:** GET
**Endpoint:** `/admin`

🔄 **Idempotent:** This operation is idempotent - multiple identical requests have the same effect as a single request.

**Description:** The GET /admin endpoint serves as the administrative interface for managing the Django application.

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
    "name": "Example admin 1"
  },
  {
    "id": 2,
    "name": "Example admin 2"
  }
]
```

**Code Examples:**

**cURL:**
```bash
curl -X GET '/admin' \
  -H 'Authorization: Token <token> YOUR_TOKEN'
```

**Python (requests):**
```python
import requests

url = '/admin'
headers = {
    'Authorization': 'Token <token> YOUR_TOKEN',
}

response = requests.get(url, headers=headers)
print(response.json())
```

**JavaScript (fetch):**
```javascript
const url = '/admin';
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

*Source: `core/urls.py`*

### Attend_calls

#### POST – Create Resource

*Create operations using the POST method*

#### Attend Call

**Method:** POST
**Endpoint:** `/attend_call`

🔔 **Webhook:** This endpoint receives webhook callbacks.

**Description:** The /attend_call endpoint allows a nurse to mark a specific call as attended by its ID (pk).

**Request Headers:**

| Header | Required | Value |
|:-------|:--------:|:------|
| Authorization | Yes | Token |

**Response**

**Status Code:** `200 OK`

```json
{
  "type": {
    "id": 1,
    "name": "Sample type"
  },
  "properties": "sample_properties"
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

### Calls

#### GET – Fetch Resource

*Retrieve operations using the GET method*

#### Views.Unacknowledged Calls

**Method:** GET
**Endpoint:** `/calls/unacknowledged`

🔄 **Idempotent:** This operation is idempotent - multiple identical requests have the same effect as a single request.

**Description:** The GET /calls/unacknowledged endpoint retrieves a list of calls that have not yet been acknowledged.

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
    "name": "Example unacknowledged 1"
  },
  {
    "id": 2,
    "name": "Example unacknowledged 2"
  }
]
```

**Code Examples:**

**cURL:**
```bash
curl -X GET '/calls/unacknowledged' \
  -H 'Authorization: Token <token> YOUR_TOKEN'
```

**Python (requests):**
```python
import requests

url = '/calls/unacknowledged'
headers = {
    'Authorization': 'Token <token> YOUR_TOKEN',
}

response = requests.get(url, headers=headers)
print(response.json())
```

**JavaScript (fetch):**
```javascript
const url = '/calls/unacknowledged';
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

*Source: `calls/urls.py`*


---

#### Views.Call Events

**Method:** GET
**Endpoint:** `/calls/events`

🔄 **Idempotent:** This operation is idempotent - multiple identical requests have the same effect as a single request.

🔔 **Webhook:** This endpoint receives webhook callbacks.

**Description:** The GET /calls/events endpoint retrieves a list of call events, which can be used to monitor and manage call activities within the application.

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
    "name": "Example events 1"
  },
  {
    "id": 2,
    "name": "Example events 2"
  }
]
```

**Code Examples:**

**cURL:**
```bash
curl -X GET '/calls/events' \
  -H 'Authorization: Token <token> YOUR_TOKEN'
```

**Python (requests):**
```python
import requests

url = '/calls/events'
headers = {
    'Authorization': 'Token <token> YOUR_TOKEN',
}

response = requests.get(url, headers=headers)
print(response.json())
```

**JavaScript (fetch):**
```javascript
const url = '/calls/events';
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

*Source: `calls/urls.py`*

#### POST – Create Resource

*Create operations using the POST method*

#### Views.Create Call

**Method:** POST
**Endpoint:** `/call`

**Description:** The POST /call endpoint is designed to create a new call within the system, primarily used in scenarios where a user needs to initiate a communication session, such as a medical consultation or emergency response.

**Request Headers:**

| Header | Required | Value |
|:-------|:--------:|:------|
| Authorization | Yes | Token |

**Response**

**Status Code:** `200 OK`

```json
{
  "type": {
    "id": 1,
    "name": "Sample type"
  },
  "properties": "sample_properties"
}
```

**Code Examples:**

**cURL:**
```bash
curl -X POST '/call' \
  -H 'Authorization: Token <token> YOUR_TOKEN'
```

**Python (requests):**
```python
import requests

url = '/call'
headers = {
    'Authorization': 'Token <token> YOUR_TOKEN',
}

response = requests.post(url, headers=headers)
print(response.json())
```

**JavaScript (fetch):**
```javascript
const url = '/call';
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

*Source: `calls/urls.py`*


---

#### Views.Acknowledge Call

**Method:** POST
**Endpoint:** `/call/<int:pk>/ack`

**Description:** The POST /call/<int:pk>/ack endpoint is designed to acknowledge a specific call identified by its primary key (pk).

**Request Headers:**

| Header | Required | Value |
|:-------|:--------:|:------|
| Authorization | Yes | Token |

**Response**

**Status Code:** `200 OK`

```json
{
  "type": {
    "id": 1,
    "name": "Sample type"
  },
  "properties": "sample_properties"
}
```

**Code Examples:**

**cURL:**
```bash
curl -X POST '/call/<int:pk>/ack' \
  -H 'Authorization: Token <token> YOUR_TOKEN'
```

**Python (requests):**
```python
import requests

url = '/call/<int:pk>/ack'
headers = {
    'Authorization': 'Token <token> YOUR_TOKEN',
}

response = requests.post(url, headers=headers)
print(response.json())
```

**JavaScript (fetch):**
```javascript
const url = '/call/<int:pk>/ack';
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

*Source: `calls/urls.py`*


---

#### Views.Attend Call

**Method:** POST
**Endpoint:** `/call/<int:pk>/attend`

**Description:** The POST /call/<int:pk>/attend endpoint is designed to allow users to attend a specific call identified by its primary key (pk).

**Request Headers:**

| Header | Required | Value |
|:-------|:--------:|:------|
| Authorization | Yes | Token |

**Response**

**Status Code:** `200 OK`

```json
{
  "type": {
    "id": 1,
    "name": "Sample type"
  },
  "properties": "sample_properties"
}
```

**Code Examples:**

**cURL:**
```bash
curl -X POST '/call/<int:pk>/attend' \
  -H 'Authorization: Token <token> YOUR_TOKEN'
```

**Python (requests):**
```python
import requests

url = '/call/<int:pk>/attend'
headers = {
    'Authorization': 'Token <token> YOUR_TOKEN',
}

response = requests.post(url, headers=headers)
print(response.json())
```

**JavaScript (fetch):**
```javascript
const url = '/call/<int:pk>/attend';
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

*Source: `calls/urls.py`*

### Create_calls

#### POST – Create Resource

*Create operations using the POST method*

#### Create Call

**Method:** POST
**Endpoint:** `/create_call`

🔔 **Webhook:** This endpoint receives webhook callbacks.

**Description:** The /create_call endpoint is designed to facilitate the creation of a new call record within the system.

**Request Headers:**

| Header | Required | Value |
|:-------|:--------:|:------|
| Authorization | Yes | Token |

**Response**

**Status Code:** `200 OK`

```json
{
  "type": {
    "id": 1,
    "name": "Sample type"
  },
  "properties": "sample_properties"
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

**Description:** The POST /create_hospital endpoint is designed to create a new hospital record in the system.

**Request Headers:**

| Header | Required | Value |
|:-------|:--------:|:------|
| Authorization | Yes | Token |

**Response**

**Status Code:** `200 OK`

```json
{
  "type": {
    "id": 1,
    "name": "Sample type"
  },
  "properties": "sample_properties"
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

**Description:** The /create_room endpoint is designed to facilitate the creation of a new room within a specified hospital and floor.

**Request Headers:**

| Header | Required | Value |
|:-------|:--------:|:------|
| Authorization | Yes | Token |

**Response**

**Status Code:** `200 OK`

```json
{
  "type": "object"
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

### Hospitals

#### GET – Fetch Resource

*Retrieve operations using the GET method*

#### Views.List Hospitals

**Method:** GET
**Endpoint:** `/hospitals`

🔄 **Idempotent:** This operation is idempotent - multiple identical requests have the same effect as a single request.

**Description:** The GET /hospitals endpoint retrieves a list of hospitals from the system, serving as a crucial resource for users needing information about available healthcare facilities.

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
curl -X GET '/hospitals' \
  -H 'Authorization: Token <token> YOUR_TOKEN'
```

**Python (requests):**
```python
import requests

url = '/hospitals'
headers = {
    'Authorization': 'Token <token> YOUR_TOKEN',
}

response = requests.get(url, headers=headers)
print(response.json())
```

**JavaScript (fetch):**
```javascript
const url = '/hospitals';
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

*Source: `calls/urls.py`*

#### POST – Create Resource

*Create operations using the POST method*

#### Views.Create Hospital

**Method:** POST
**Endpoint:** `/hospitals/create`

**Description:** The POST /hospitals/create endpoint is designed to facilitate the creation of new hospital records within the system.

**Request Headers:**

| Header | Required | Value |
|:-------|:--------:|:------|
| Authorization | Yes | Token |

**Response**

**Status Code:** `200 OK`

```json
{
  "type": "object"
}
```

**Code Examples:**

**cURL:**
```bash
curl -X POST '/hospitals/create' \
  -H 'Authorization: Token <token> YOUR_TOKEN'
```

**Python (requests):**
```python
import requests

url = '/hospitals/create'
headers = {
    'Authorization': 'Token <token> YOUR_TOKEN',
}

response = requests.post(url, headers=headers)
print(response.json())
```

**JavaScript (fetch):**
```javascript
const url = '/hospitals/create';
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

*Source: `calls/urls.py`*

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

**Description:** The /list_rooms endpoint retrieves a list of all rooms in the system, ordered by their room number.

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

### Rooms

#### GET – Fetch Resource

*Retrieve operations using the GET method*

#### Views.List Rooms

**Method:** GET
**Endpoint:** `/rooms`

🔄 **Idempotent:** This operation is idempotent - multiple identical requests have the same effect as a single request.

**Description:** The GET /rooms endpoint retrieves a list of rooms available in the system.

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
curl -X GET '/rooms' \
  -H 'Authorization: Token <token> YOUR_TOKEN'
```

**Python (requests):**
```python
import requests

url = '/rooms'
headers = {
    'Authorization': 'Token <token> YOUR_TOKEN',
}

response = requests.get(url, headers=headers)
print(response.json())
```

**JavaScript (fetch):**
```javascript
const url = '/rooms';
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

*Source: `calls/urls.py`*

#### POST – Create Resource

*Create operations using the POST method*

#### Views.Create Room

**Method:** POST
**Endpoint:** `/rooms/create`

🔔 **Webhook:** This endpoint receives webhook callbacks.

**Description:** The POST /rooms/create endpoint is designed to facilitate the creation of new rooms within the application.

**Request Headers:**

| Header | Required | Value |
|:-------|:--------:|:------|
| Authorization | Yes | Token |

**Response**

**Status Code:** `200 OK`

```json
{
  "type": {
    "id": 1,
    "name": "Sample type"
  },
  "properties": "sample_properties"
}
```

**Code Examples:**

**cURL:**
```bash
curl -X POST '/rooms/create' \
  -H 'Authorization: Token <token> YOUR_TOKEN'
```

**Python (requests):**
```python
import requests

url = '/rooms/create'
headers = {
    'Authorization': 'Token <token> YOUR_TOKEN',
}

response = requests.post(url, headers=headers)
print(response.json())
```

**JavaScript (fetch):**
```javascript
const url = '/rooms/create';
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

*Source: `calls/urls.py`*

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

**Description:** The /webhook_receiver endpoint is designed to receive webhook notifications from various services, allowing the application to process real-time updates or events.

**Request Headers:**

| Header | Required | Value |
|:-------|:--------:|:------|
| Authorization | Yes | Token |

**Response**

**Status Code:** `200 OK`

```json
{
  "type": {
    "id": 1,
    "name": "Sample type"
  },
  "properties": "sample_properties"
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

### Webhooks

#### POST – Create Resource

*Create operations using the POST method*

#### Views.Webhook Receiver

**Method:** POST
**Endpoint:** `/webhook`

🔔 **Webhook:** This endpoint receives webhook callbacks.

**Description:** The POST /webhook endpoint is designed to receive webhook notifications from external services, allowing the application to process events in real-time.

**Request Headers:**

| Header | Required | Value |
|:-------|:--------:|:------|
| Authorization | Yes | Token |

**Response**

**Status Code:** `200 OK`

```json
{
  "type": "object",
  "properties": {}
}
```

**Code Examples:**

**cURL:**
```bash
curl -X POST '/webhook' \
  -H 'Authorization: Token <token> YOUR_TOKEN'
```

**Python (requests):**
```python
import requests

url = '/webhook'
headers = {
    'Authorization': 'Token <token> YOUR_TOKEN',
}

response = requests.post(url, headers=headers)
print(response.json())
```

**JavaScript (fetch):**
```javascript
const url = '/webhook';
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

*Source: `calls/urls.py`*


---

## 6. Rate Limiting

**Rate Limiting:** Enabled

* **User:** 100/minute

### Rate Limit Headers

| Header | Description |
|--------|-------------|
| `X-RateLimit-Limit` | Total number of requests allowed per minute |
| `X-RateLimit-Remaining` | Number of requests remaining in the current rate limit window |
| `X-RateLimit-Reset` | Time when the rate limit will reset |

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
| 1.0.0 | 2026-03-24 | Initial release with Call endpoints, Calls endpoints, Rooms endpoints |

---

## API Documentation Best Practices

* Use nouns instead of verbs in URLs
* Return correct HTTP status codes
* Keep response formats consistent
* Always include example requests and responses
* Clearly document validation rules and edge cases
