# snapshotanlyzer-3000
Demo project to manage AWS EC2 Instance snapshots

# about

This project is a demo of using Boto3 to get AWS Instance snapshots.

## Configuring 

shotty uses the configuration created by AWS CLI, you must have a AWS account with programatically access and permisions to manage EC2

`aws configure --profile shotty`

## Running

pipenv run python shotty/shotty.py