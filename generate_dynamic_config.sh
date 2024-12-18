#!/bin/bash

# List of changed directories containing .py files (passed as a parameter)
changed_folders=$1

# If no directories are provided, exit gracefully
if [ -z "$changed_folders" ]; then
  echo "No directories with .py files provided. Stopping build."
  circleci-agent step halt
fi

# Initialize the config file
cp .circleci/config_template.yml .circleci/generated_config.yml

# Append jobs to the config file
echo ""
echo "Append jobs to the config file"
echo ""
for dir in $changed_folders; do
  echo $dir
  export FOLDER=$dir
  envsubst < .circleci/config_template.yml >> .circleci/generated_config.yml
  cat <<EOL >> .circleci/generated_config.yml
      - run_operations:
          folder: $FOLDER
EOL
done
echo "End appending"

# Clean up temporary file
rm .circleci/config_template.yml
