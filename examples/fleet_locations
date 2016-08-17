#!/usr/bin/python
"""
This script retrieves and prints the GPS locations for all vehicles in a group.

To use it, run:
./examples/fleet_locations --access_token <SAMSARA_API_TOKEN> --group_id <GROUP_ID>

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
    # Get GPS locations for vehicles in the group.
    response = client.get_fleet_locations(access_token,
                                          samsara.GroupParam(group_id))
    for vehicle in response.vehicles:
        print '\nvehicle ID: {}, name: {}, (lat, long): ({}, {}), time:{}'.\
            format(vehicle.id, vehicle.name, vehicle.latitude,
                   vehicle.longitude, vehicle.time)


if __name__ == "__main__":
    get_sensors()
