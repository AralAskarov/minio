#!/bin/bash

if [ -z "$1" ]; then
  echo "Usage: $0 <BUCKET_NAME>"
  exit 1
fi

BUCKET_NAME="$1"
LOCAL_DIR="/home/aral/minio-$BUCKET_NAME"
LOG_DIR="/home/aral/minio-backup/logs"
LOG_FILE="$LOG_DIR/minio-$BUCKET_NAME-sync.log"

#bucket creating if doesnt exists
if ! rclone lsd minio: | grep -qw "$BUCKET_NAME"; then
  echo "Bucket '$BUCKET_NAME' does not exist. Creating bucket..."
  rclone mkdir minio:$BUCKET_NAME
  rclone lsd minio:
  if [ $? -ne 0 ]; then
    echo "Failed to create bucket '$BUCKET_NAME'. Exiting..."
    exit 1
  fi
  echo "Bucket '$BUCKET_NAME' created successfully."
else
  echo "Bucket '$BUCKET_NAME' already exists."
fi

#localdir creation if doesnt exist
if [ ! -d "$LOCAL_DIR" ]; then
    mkdir -p "$LOCAL_DIR"
    if [ $? -ne 0 ]; then
      echo "Failed to create local directory '$LOCAL_DIR'. Exiting..."
      exit 1
    fi
    echo "Local directory '$LOCAL_DIR' created successfully."
  fi

#log dir creation if doesnt exist
if [ ! -d "$LOG_DIR" ]; then
  echo "Log directory '$LOG_DIR' does not exist. Creating it..."
  mkdir -p "$LOG_DIR"
  if [ $? -ne 0 ]; then
    echo "Failed to create log directory '$LOG_DIR'. Exiting..."
    exit 1
  fi
  echo "Log directory '$LOG_DIR' created successfully."
fi

#log file if doesnt exist
if [ ! -f "$LOG_FILE" ]; then
  echo "Log file '$LOG_FILE' does not exist. Creating it..."
  touch "$LOG_FILE"
  if [ $? -ne 0 ]; then
    echo "Failed to create log file '$LOG_FILE'. Exiting..."
    exit 1
  fi
  echo "Log file '$LOG_FILE' created successfully."
fi


rclone -v sync minio:$BUCKET_NAME $LOCAL_DIR >> "$LOG_FILE" 2>&1
