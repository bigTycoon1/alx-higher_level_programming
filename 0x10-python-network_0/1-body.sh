#!/bin/bash
# sends a GET reqst to URL and display response body
curl -sfL "$1" -X GET
