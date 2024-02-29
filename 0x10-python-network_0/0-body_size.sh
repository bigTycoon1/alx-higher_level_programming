#!/bin/bash
# sends a request to that URL, and displays size of the response body
curl -sI "$1" | grep -i Content-Length | cut -d " " -f2
