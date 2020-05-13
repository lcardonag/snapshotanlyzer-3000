import click
import boto3
session=boto3.Session(profile_name='shotty')
ec2=session.resource('ec2')

@click.command()

def list_instances():
    "List of EC2 Instances"
    for i in ec2.instances.all():
        print(', '.join((
            i.id,
            i.instance_type,
            i.placement['AvailabilityZone'],
            i.state['Name'],
            i.public_dns_name)))
    return

def stop_all_instances():
    "Stop All EC2 Instances"
    for i in ec2.instances.all():
        i.stop()
    return


if __name__ == "__main__":
    #stop_all_instances()
    list_instances()
    

    
    