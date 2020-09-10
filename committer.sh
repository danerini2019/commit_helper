#!/bin/sh -e
commit_message="$1"
git add
git commit -am "$commit_message"
git push