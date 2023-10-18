#!/bin/bash

#Desenvolvido por: Bee Solutions
#Autor: Fernando Almondes
#Data: 07/07/2023

URL="http://localhost:4000/api/message"
PHONE="$1"
TITULO="$2"
MESSAGE="$TITULO$3"

curl --location --request POST "$URL" \
     --header 'Content-Type: application/json' \
     --data-raw "{
        \"number\": \"${PHONE}\",
        \"message\": \"${MESSAGE}\"
     }"