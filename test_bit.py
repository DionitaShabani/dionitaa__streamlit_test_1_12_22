
import streamlit as st

st.title('**:blue[TEST]**      :computer:')



title = st.text_input('Add your text here 👇:')
st.write( title)

def convert_list(title):
    lst = list(title.split())  #the string is converted to a list
    return lst

prnt = convert_list(title) 
if st.button('Return list'):
    st.write(prnt, 'The string is converted to a list')                  #this button shows the list



def convert_upper(prnt): #this function converts all elements of list created above to uppercase.
    upper_list = [] 
    for i in prnt:
        upper_list.append(i.upper())
    return upper_list

prnt_upper = convert_upper(prnt)
if st.button('Upper'):
    st.write(prnt_upper, 'All elements of the list are converted to uppercase') #this prints the elements all in uppercase



def count(prnt):  #counts all elements of the list
    counter = 0
    for i in prnt:
        counter +=1
    return counter
prnt_count = count(prnt)
if st.button('print_count'):
    st.write('The total number of elements in the list above is:',prnt_count)
