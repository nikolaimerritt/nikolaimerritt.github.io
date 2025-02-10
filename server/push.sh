#! /bin/bash
set -eu
export AWS_PROFILE="default"
script_dir=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
version="$(cat "$script_dir/VERSION" | tr -d "\n")"
repo="672675261983.dkr.ecr.eu-west-2.amazonaws.com"
project_name="sheldon-ring"
image_tag="$repo/$project_name:$version"

aws ecr get-login-password --region eu-west-2 | docker login --username AWS --password-stdin "$repo"
docker build -t sheldon-ring "$script_dir"
docker tag sheldon-ring:latest "$image_tag" 
docker push "$image_tag"