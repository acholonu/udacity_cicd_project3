#!/bin/bash
aws s3 rm --recursive s3://udapeople-$2
aws cloudformation --profile $1 delete-stack --stack-name "uda-frontend-stack-$2"
aws cloudformation --profile $1 delete-stack --stack-name "uda-backend-stack-$2"
aws cloudformation --profile $1 delete-stack --stack-name uda-prometheus-server-stack

# To run this script: > ./cleanup.sh profile-name workflowid