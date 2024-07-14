from Extract import * 
class Transform:
    """ 
    - Retrieve some records from the top of the extracted dataset.
    - Retrieve some records from the end of the extracted dataset.
    - Rename one or more columns.
    - Remove one or more unnecessary columns.
    - Transform the data itself.
    """
    def head(self, dataset, step): # Return the top records from the dataset
        if not dataset:
           raise Exception("The Dataset cannot be empty")
        if step < 1:
           raise Exception("The step value cannot be positive")
        return dataset[0:step] 

    def tail(self, dataset, step): # Return the last records from the dataset
        if not dataset:
            raise Exception("The dataset cannot be empty")
        if step < 1:
            raise Exception("The step value must be positive")
        return dataset[len(dataset) - step:len(dataset)]
   
    def rename_attribute(self, dataset, attribute, new_attribute): # Rename one column in the dataset
        if not dataset:
            raise Exception("The dataset cannot be empty")
        if not attribute:
            raise Exception("The attribute key must be a valid key")
        new_dataset = []
        for row in dataset:
            if attribute in row.keys():
                val = row[attribute]
                new_row = row.copy()
                del new_row[attribute]
                new_row[new_attribute] = val
                new_dataset.append(new_row)
            else:
                raise Exception("The operation is not possible because the column " + str(column_name)\
                    + " does not exist in the dataset")
        return new_dataset

    def remove_attribute(self, dataset, attribute): # Remove a column from the dataset
        for row in dataset:
            new_row = row
            if attribute in new_row.keys():
                del new_row[attribute]
                new_dataset.append(new_row)
        return new_dataset

    def rename_attributes(self, dataset, attributes, new_attributes): # Rename a list of columns in the dataset
        if not attributes or not new_attributes:
            raise Exception("The attributes cannot be empty")
        if len(attributes) != len(new_attributes):
            raise Exception("The number of new column names must match the number of existing column names")
        for row in dataset:
            new_row = row 
            for item in range(0, len(attributes)):
                attribute = attributes[item]
                new_attribute = new_attributes[item]
                if attribute in new_row.keys():
                    val = row[attribute]
                    del new_row[attribute]
                    new_row[new_attribute] = val
                else:
                    raise Exception("Operation is not possible because the key " + str(key)+ \
                        "does not exist in one of the rows in the dataset")
            new_dataset.append(new_row)
        return new_dataset

    def remove_attributes(self, dataset, attributes): # Remove a list of columns in the dataset
        if not dataset:
            raise Exception("Dataset cannot be empty")
        if not attributes:
            raise Exception("The list of attributes cannot be empty")
        for row in dataset:
            new_row = row
            for attribute in attributes:
                if attribute in new_row.keys():
                    del new_row[attribute]
            new_dataset.append(new_row)
        return new_dataset

    def transform(self, dataset, attribute, new_attribute, transform_function, *args):
        if not dataset:
            raise Exception("The dataset cannot be empty")
        if not attribute or not new_attribute:
            raise Exception("The input attribute cannot be empty")
        if not transform_function:
            raise Exception("The transform_function cannot be None")
        new_dataset = [] # Output 
        for row in dataset:  # Iterate through the input data   
            trf = transform_function(row[attribute], *args) # Apply transformation function on column
            ze = row.copy()
            ze.update({new_attribute:trf}) # Create a new column in the dataset 
            new_dataset.append(ze) 
        return new_dataset

    def open_price(value, *args):
        return float(value)

#### Extract
ex = Extract()
dataset = ex.from_csv(file_path="<------->/stocks.csv") # To be replaced by file path
print(f"\nOriginal dataset:")
print(dataset[0])

#### Transform
tr = Transform()
new_dataset = tr.transform(dataset = dataset, attribute = "Open", \
    new_attribute = "open_price", transform_function = open_price)

print(f"\nTransformed dataset:")
print(new_dataset[0])

