row_1=['☺️','☺️','☺️']
row_2=['☺️','☺️','☺️']
row_3=['☺️','☺️','☺️']
matrix=[row_1,row_2,row_3]
print(f"{row_1}\n{row_2}\n{row_3}")
position=input("enter a position: ")
#23
row_number=int(position[0])
column_number=int(position[1])
row_selected=matrix[row_number-1]
row_selected[column_number-1]='X'
print(f"{row_1}\n{row_2}\n{row_3}")

