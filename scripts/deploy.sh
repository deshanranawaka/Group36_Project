#!/bin/bash

REMOTE_USER="ubuntu"
REMOTE_IP="192.168.5.177"
REMOTE_DIR="~/reddit_analysis_project"

echo "Deploying source code to the cluster at $REMOTE_IP..."

# Create the destination directory on the cluster
ssh $REMOTE_USER@$REMOTE_IP "mkdir -p $REMOTE_DIR"

# Copy the src directory
rsync -avz --progress ./src $REMOTE_USER@$REMOTE_IP:$REMOTE_DIR/

echo "Deployment finished. Your code is now available at $REMOTE_IP:$REMOTE_DIR/src"