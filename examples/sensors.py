#!/usr/bin/python
"""
This script retrieves all the sensors for a group and prints their ID, Name, Mac Address.

To use it, run:
./examples/sensors --access_token <SAMSARA_API_TOKEN> --group_id <GROUP_ID>

passing in your Samsara API access token and the group ID you want to access.

"""
import click

import samsara
from samsara.apis import SamsaraClient


@click.command()
@click.option('--access_token', type=str, required=True)
@click.option('--group_id', type=int, required=True)
def get_sensors(access_token, group_id):
    # Create an instance of the SamsaraClient.
    client = SamsaraClient()
    # Get the sensors for the group.
    response = client.get_sensors(access_token,
                                  samsara.GroupParam(group_id))
    for sensor in response.sensors:
        print '\nsensor ID: {}, name: {}, macAddress: {}'.format(sensor.id,
                                                                 sensor.name,
                                                                 sensor.mac_address)


if __name__ == "__main__":
    get_sensors()
