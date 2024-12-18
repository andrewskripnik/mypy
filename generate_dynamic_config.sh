#!/bin/bash

# If no directories are provided, exit gracefully
if [ -z "$changed_dirs" ]; then
  echo "[generate_dynamic_config.sh] No directories with .py files provided. Stopping build."
  circleci-agent step halt
fi

# Detect changes in the repository and output the list of changed folders
changed_folders=$(git diff --name-only HEAD~1 HEAD | grep '/' | cut -d '/' -f1 | sort | uniq)

# Initialize the config file
cp .circleci/config_template.yml .circleci/generated_config.yml

# Append jobs to the config file
echo "Changed dirs: "
echo $changed_folders

for dir in $changed_folders; do
  echo $dir
  export FOLDER=$dir
  envsubst < .circleci/config_template.yml >> .circleci/generated_config.yml
  cat <<EOL >> .circleci/generated_config.yml
      - run_operations:
          folder: $FOLDER
EOL
done

# Clean up temporary file
rm .circleci/config_template.yml
