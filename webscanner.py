import shodan

# set up an instance of the Shodan object
api = shodan.Shodan('233v2eeS3IBoah74rWCyvECSDUcHublw')

# define the target query
#query = input('Weblink:\t')

#try:
    # perform the search and get the results
#    results = api.search(query)

    # iterate over the results and print the IP addresses
#    for result in results['matches']:
#        print(result['ip_str'])

#except shodan.APIError as e:
#    print('Error: {}'.format(e))

try:
        # Search Shodan
        results = api.search('apache')

        # Show the results
        print('Results found: {}'.format(results['total']))
        for result in results['matches']:
                print('IP: {}'.format(result['ip_str']))
                print(result['data'])
                print('')
except shodan.APIError as e:
        print('Error: {}'.format(e))
