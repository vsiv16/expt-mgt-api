import pickle

def get_filename(args):
    # download and get the name of the file we are storing
    return

def serialise(filename):
    # open the file for reading
    with open(filename, 'rb') as file:
        # read the contents of the file
        file_contents = file.read()

    # serialize the data using pickle
    serialized_file = pickle.dumps(file_contents)

    # open a new file for writing
    with open('serialized_file.pickle', 'wb') as new_file:
        # write the serialized data to the new file
        new_file.write(serialized_file)

    # print a message indicating that the file has been serialized
    print('The file has been serialized.')

def deserialise(pickle_file, filename):
    # open the serialized file for reading
    with open(pickle_file, 'rb') as file:
        # read the serialized data from the file
        serialized_file = file.read()

    # deserialize the data using pickle
    deserialized_file_contents = pickle.loads(serialized_file)

    with open(filename, 'rb') as file:
        file.write(deserialized_file_contents)

    # print a message indicating that the file has been deserialized
    print('The file has been deserialized.')

