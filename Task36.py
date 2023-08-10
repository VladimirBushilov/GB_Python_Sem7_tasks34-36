def print_operation_table(operation, num_rows=6, num_columns=6):
    for column in range(1, num_columns+1):
        print(column, end='\t')
    print()
    
    for row in range(1, num_rows+1):
        for column in range(1, num_columns+1):
            value = operation(row, column)
    
            print(value, end='\t')
        print()

print_operation_table(lambda x, y: x * y)