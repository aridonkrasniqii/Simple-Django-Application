from design import Connect

with Connect('aridon_server') as server:
    print('Installing python')
    print('Installing and updating more tools')


print('This is after __exit__')