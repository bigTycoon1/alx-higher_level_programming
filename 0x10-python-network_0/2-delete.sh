#!/bin/bash
# sends a DELETE reqst, and passed the first args
curl -s "$1" -X DELETE
