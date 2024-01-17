# Pagination in REST API Design

## Introduction

Pagination is a crucial aspect of designing RESTful APIs that deal with large datasets. Properly implementing pagination ensures efficient data retrieval, improves performance, and enhances the overall user experience. This README guide will walk you through implementing pagination in your REST API, covering simple page and page_size parameters, HATEOAS, and deletion-resilient pagination.

## Table of Contents

1. [Simple Pagination with page and page_size Parameters](#simple-pagination)
2. [Pagination with HATEOAS](#pagination-with-hateoas)
3. [Deletion-Resilient Pagination](#deletion-resilient-pagination)

## Simple Pagination with page and page_size Parameters <a name="simple-pagination"></a>

### Overview

Implementing pagination with simple page and page_size parameters is a common approach. Clients can request specific pages of data with a defined page size, allowing them to navigate through the dataset efficiently.

### Usage

Endpoint: `/api/resource`

Parameters:
- `page` (optional): The page number to retrieve (default: 1).
- `page_size` (optional): The number of items per page (default: a reasonable default value).

Example Request:
```http
GET /api/resource?page=2&page_size=10
```

Example Response:
```json
{
  "data": [...],  // Paginated data
  "meta": {
    "page": 2,
    "page_size": 10,
    "total_items": 100,
    "total_pages": 10
  }
}
```

# Pagination with HATEOAS <a name="pagination-with-hateoas"></a>
## Overview
HATEOAS provides hypermedia links within API responses, allowing clients to discover and navigate through related resources. Including pagination links in your API responses enables clients to traverse the dataset seamlessly.

## Usage
Endpoint: `/api/resource`

Example Response:
```json
{
  "data": [...],  // Paginated data
  "links": {
    "self": "/api/resource?page=2&page_size=10",
    "first": "/api/resource?page=1&page_size=10",
    "prev": "/api/resource?page=1&page_size=10",
    "next": "/api/resource?page=3&page_size=10",
    "last": "/api/resource?page=10&page_size=10"
  },
  "meta": {
    "page": 2,
    "page_size": 10,
    "total_items": 100,
    "total_pages": 10
  }
}
```

# Deletion-Resilient Pagination <a name="deletion-resilient-pagination"></a>
## Overview
Deletion-resilient pagination ensures a consistent user experience even when items are deleted during pagination. This is achieved by using a unique identifier for pagination and handling deletions gracefully.

## Implementation
1. `Use Cursor-Based Pagination:` Instead of relying on page numbers, use a unique identifier (e.g., item's ID) as a cursor to paginate.

2. `Handle Deletions Gracefully:` If an item in the current page is deleted, adjust the pagination accordingly to prevent skipping or duplicating items.

Example Response:
```json
{
  "data": [...],  // Paginated data
  "meta": {
    "cursor": "unique_identifier_of_last_item",
    "page_size": 10,
    "has_more": true
  }
}
```
# Conclusion
By following the best practices outlined in this guide, you can implement efficient and user-friendly pagination in your REST API, providing a seamless experience for clients interacting with large datasets.
