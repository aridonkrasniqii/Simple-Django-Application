try:
    file = open('file.txt', 'a')
    # You can raise an Exception and it will be catch in catch block
    # if file.name == 'file.txt':
    #     raise Exception

except FileNotFoundError as ex:
    print(ex)
except Exception as ex:
    print(ex)
else:
    # Else block will be executed if the try clause  doesn't throw Exception
    try:
        print(file.read())
        file.close()
    except Exception as ex:
        print(f"{file.name} is " + str(ex))
finally:
    # If we are working with a database
    # In this finally block you can close the database connection
    print('Executing Finally... ')
