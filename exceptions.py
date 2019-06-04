try:
    f = open('curruptfile.txt')
    if f.name == 'currupt_file.txt':
        raise Exception
except IOError as e:
    print('First!')
except Exception as e:
    print('Manually raised exception')
else:  # If try succeeds
    print(f.read())
    f.close()
finally:  # runs no matter what happpens #Release resources like close db handler etc
    print("Executing Finally...")
