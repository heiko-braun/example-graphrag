import pickle

def save_object(name, obj):
    with open(f"output/{name}.pickle", "wb") as outfile:
        # "wb" argument opens the file in binary mode
        pickle.dump(obj, outfile)

def load_object(name):
    try:
        with open(f"output/{name}.pickle", "rb") as infile:
            print(f"Load '{name}' from file ...")
            return pickle.load(infile)        
    except FileNotFoundError:
        print(f"'{name}' does not exist ...")
        return None        
