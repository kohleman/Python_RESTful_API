#!/bin/bash

curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"id":"1","name":"Risiko"}' \
  http://localhost:5000/boardgames
