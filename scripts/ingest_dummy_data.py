"""
This script requires the following packages:
    - python-icat
    - suds-community
"""

import argparse

import icat
import icat.query


def create(icat_entity):
    """
    Submits the input icat entity to the database.
    :param icat_entity:
    :return: The submitted entity or the already existing one
    """

    try:
        icat_entity.create()
    except icat.ICATObjectExistsError:
        icat_entity = icat_entity.client.searchMatching(icat_entity)
    return icat_entity


def upload_dummy_data(username, password, address, ids_address):
    print(f'Try to access: {address} with {username}')
    client = icat.client.Client(url=address, idsurl=ids_address)
    client.login('simple', {'username': username, 'password': password})

    # Create facility
    f_lils = client.new('facility')
    f_lils.name = 'LILS'
    f_lils.fullName = 'Lorem Ipsum Laser System'
    f_lils = create(f_lils)

    # Check
    print('Facilities:')
    print(client.search('select o from Facility o'))

    # Create investigation type
    investigation_type = client.new('investigationType', facility=f_lils, name='Internal')
    investigation_type = create(investigation_type)

    # Check
    print('Investigation types:')
    print(client.search('select o from InvestigationType o'))

    # Create investigations
    for inv in ['Inv A', 'Inv B', 'Inv C']:
        investigation = client.new(
            'investigation',
            facility=f_lils,
            type=investigation_type,
            name=inv, title=f'The {inv}',
            visitId='One'
        )
        create(investigation)


    # Check
    print('Investigations:')
    print(client.search('select o from Investigation o include o.type, o.facility'))

    # Create datasetType
    dataset_type = client.new('datasetType', facility=f_lils, name='Dummy data')
    dataset_type = create(dataset_type)

    # Check
    print('Dataset types:')
    print(client.search('select o from DatasetType o'))

    # Create datasets
    datafile_format = client.new('datafileFormat', name='Text', facility=f_lils, version='1.0.0')
    datafile_format = create(datafile_format)

    # Check
    print('Datafile formats:')
    print(client.search('select o from DatasetType o'))

    for inv in client.search('select inv from Investigation inv'):
        ds = client.new('dataset', investigation=inv, name=f'the data for {inv.name}', type=dataset_type)
        ds = create(ds)
        # add file
        data_file = client.new(
            'datafile',
            name='dummy.txt',
            dataset=ds,
            datafileFormat=datafile_format
        )
        client.putData('../resources/dummy.txt', data_file)

    # Check
    print('Datasets:')
    print(client.search('select o from Dataset o include o.type, o.investigation'))

    #Check
    print('Datafiles:')
    print(client.search('select o from Datafile o'))

    client.logout()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--username', type=str, default='root')
    parser.add_argument('--password', type=str, default='password')
    parser.add_argument('--address', type=str, default='http://localhost:8080')
    parser.add_argument('--ids_address', type=str, default='http://localhost:8080')

    args = parser.parse_args()
    upload_dummy_data(
        username=args.username,
        password=args.password,
        address=args.address,
        ids_address=args.ids_address
    )


if __name__ == '__main__':
    main()
