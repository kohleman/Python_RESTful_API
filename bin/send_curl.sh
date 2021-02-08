#!/bin/bash

curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"id":"1","name":"Risiko", "designer": "Albert Lamorisse", "playing_time": "60 Min", "rating": 7.5}' \
  http://localhost:5000/boardgames

curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"id":"2","name":"Nauticus", "designer": "Wolfgang Kramer", "playing_time": "30 Min", "rating": 9.5}' \
  http://localhost:5000/boardgames
