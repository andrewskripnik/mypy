#!/bin/bash

# Detect changes in the repository and output the list of changed folders
changed_folders=$(git diff --name-only HEAD~1 HEAD | grep '/' | cut -d '/' -f1 | sort | uniq)

# Start generating the CircleCI config file
cat <<EOL > .circleci/config_template.yml
version: 2.1

executors:
  python:
    docker:
      - image: cimg/python:3.13
  base:
    docker:
      - image: cimg/base:2024.12

jobs:
  run_operations:
    executor: python
    resource_class: small
    parameters:
      folder:
        type: string
    steps:
      - checkout
      - run:
          name: Run operations for $FOLDER
          command: |
            if [ -d "$FOLDER" ]; then
              echo "Running operations for $FOLDER"
              # Add your folder-specific operations here
            else
              echo "Folder $FOLDER does not exist."
            fi

workflows:
  detect_and_run:
    jobs:
EOL

# Initialize the config file
cp .circleci/config_template.yml .circleci/generated_config.yml

# Append jobs to the config file
for dir in $changed_dirs; do
  export FOLDER=$dir
  envsubst < .circleci/config_template.yml >> .circleci/generated_config.yml
  cat <<EOL >> .circleci/generated_config.yml
      - run_operations:
          folder: $FOLDER
EOL
done

# Clean up temporary file
rm .circleci/config_template.yml
