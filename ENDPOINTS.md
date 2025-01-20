
---

# API Endpoints Documentation

This document provides an overview of the available endpoints in your API, categorized by app and resource type.

---

## Core App

| **Method** | **Endpoint**          | **Description**               |
|------------|-----------------------|-------------------------------|
| `GET`      | `/api/`               | API root                      |
| `POST`     | `/api/token/`         | Obtain JWT token              |
| `POST`     | `/api/token-refresh/` | Refresh JWT token             |
| `GET`      | `/api/home/`          | Home view                     |

---

## Players App

| **Method** | **Endpoint**           | **Description**                 |
|------------|------------------------|---------------------------------|
| `GET`      | `/api/players/`        | List all players                |
| `POST`     | `/api/players/`        | Create a new player             |
| `GET`      | `/api/players/{id}/`   | Retrieve a specific player      |
| `PUT`      | `/api/players/{id}/`   | Update a specific player        |
| `PATCH`    | `/api/players/{id}/`   | Partially update a specific player |
| `DELETE`   | `/api/players/{id}/`   | Delete a specific player        |

---

## Matches App

### Singles Matches

| **Method** | **Endpoint**                   | **Description**                 |
|------------|--------------------------------|---------------------------------|
| `GET`      | `/api/matches/singles/`        | List all singles matches        |
| `POST`     | `/api/matches/singles/`        | Create a new singles match      |
| `GET`      | `/api/matches/singles/{id}/`   | Retrieve a specific singles match |
| `PUT`      | `/api/matches/singles/{id}/`   | Update a specific singles match |
| `PATCH`    | `/api/matches/singles/{id}/`   | Partially update a specific singles match |
| `DELETE`   | `/api/matches/singles/{id}/`   | Delete a specific singles match |

### Doubles Matches

| **Method** | **Endpoint**                   | **Description**                 |
|------------|--------------------------------|---------------------------------|
| `GET`      | `/api/matches/doubles/`        | List all doubles matches        |
| `POST`     | `/api/matches/doubles/`        | Create a new doubles match      |
| `GET`      | `/api/matches/doubles/{id}/`   | Retrieve a specific doubles match |
| `PUT`      | `/api/matches/doubles/{id}/`   | Update a specific doubles match |
| `PATCH`    | `/api/matches/doubles/{id}/`   | Partially update a specific doubles match |
| `DELETE`   | `/api/matches/doubles/{id}/`   | Delete a specific doubles match |

---

## Seasons App

| **Method** | **Endpoint**          | **Description**                 |
|------------|-----------------------|---------------------------------|
| `GET`      | `/api/seasons/`       | List all seasons                |
| `POST`     | `/api/seasons/`       | Create a new season             |
| `GET`      | `/api/seasons/{id}/`  | Retrieve a specific season      |
| `PUT`      | `/api/seasons/{id}/`  | Update a specific season        |
| `PATCH`    | `/api/seasons/{id}/`  | Partially update a specific season |
| `DELETE`   | `/api/seasons/{id}/`  | Delete a specific season        |

---

## Notes

1. Replace `{id}` in the endpoints with the relevant resource ID.
2. Some endpoints require appropriate authentication and authorization.

--- 