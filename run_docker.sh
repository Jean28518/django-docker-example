#!/bin/bash

# Build image and add a descriptive tag
docker build --tag=demochecklist .

# Run docker container
docker run -d -p 8000:80 --restart=unless-stopped --volume="/home/$USER/.db/:/app/demochecklist/db" --name='demochecklist' 'demochecklist'