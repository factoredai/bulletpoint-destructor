import pickle

def save_file_as_pickle(file, path: str) -> None:
    """Saves any type of file as pickle

    Parameters
    ----------
    file : Any
        The file to be saved
    path : str
        The path to save the file
    """

    with open(file=path, mode="wb") as f:
        pickle.dump(obj=file, file=f, protocol=pickle.HIGHEST_PROTOCOL)