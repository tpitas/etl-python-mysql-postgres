class Transform:
    """ 
    - Retrieve some records from the top of the extracted dataset.
    - Retrieve some records from the end of the extracted dataset.
    - Rename one or more columns.
    - Remove one or more unnecessary columns.
    - Transform the data itself.
    """
    def head(self, dataset, step): # Return the top records from the dataset
        pass

    def tail(self): # Return the last records from the dataset
        pass

    def rename_attribute(self): # Rename one column in the dataset
        pass

    def remove_attribute(self): # Remove a column from the dataset
        pass

    def rename_attributes(self): # Rename a list of columns in the dataset
        pass

    def remove_attributes(self): # Remove a list of columns in the dataset
        pass

    def transform(self):
        pass
