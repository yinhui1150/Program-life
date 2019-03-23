#永久存储
import pickle

my_list = [123, 3.14, ['another list']]
pickle_file = open('E:\\python\\pickle.pkl', 'wb')
pickle.dump(my_list, pickle_file)
pickle_file.close()

pickle_file = open('E:\\python\\pickle.pkl', 'rb')
mylist2 = pickle.load(pickle_file)
print(mylist2)
pickle_file.close()
