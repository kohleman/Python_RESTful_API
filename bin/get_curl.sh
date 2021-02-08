#!/bin/bash
curl -X GET "http://localhost:5000/boardgames?sort_order=asc&sort_by=id&limit=100&offset=0"
