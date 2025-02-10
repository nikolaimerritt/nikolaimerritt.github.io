#! /bin/bash
set -eux
source ~/.env
script_dir=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

image_tag="$REPO/$PROJECT_NAME:$VERSION"
aws ecr get-login-password --region eu-west-2 | docker login --username AWS --password-stdin "$REPO"
docker pull "$image_tag"
docker run -p 8000:8000 -v "$script_dir/sqlite:/sqlite" "$image_tag"
