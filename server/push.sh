#! /bin/bash
set -eu
version="0.0.1"
script_dir=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
repo="672675261983.dkr.ecr.eu-west-2.amazonaws.com"
image_tag="$repo:$version"

aws ecr get-login-password --region eu-west-2 | docker login --username AWS --password-stdin $repo
docker build -t sheldon-ring .
docker tag sheldon-ring:latest "$image_tag" 
docker push "$image_tag"