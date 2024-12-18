#!/bin/bash

# Detect changes in the repository and output the list of changed folders
changed_folders=$(git diff --name-only HEAD~1 HEAD | grep '/' | cut -d '/' -f1 | sort | uniq)

# Start generating the CircleCI config file
cat <<EOL > .circleci/generated_config.yml
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
    parameters:
      folder:
        type: string
    steps:
      - checkout
      - run:
          name: Run operations for << parameters.folder >>
          command: |
            if [ -d "<< parameters.folder >>" ]; then
              echo "Running operations for << parameters.folder >>"
              # Add your folder-specific operations here
            else
              echo "Folder << parameters.folder >> does not exist."
            fi

workflows:
  version: 2
  detect_and_run:
    jobs:
      - run_operations:
          folder: << folder_name >>
EOL

# Loop through each changed folder and add a job to the workflow
for folder in $changed_folders; do
  sed -i "\$a\      - run_operations:\n          folder: $folder\n          requires:\n            - run_operations" .circleci/generated_config.yml
done