from src.phonebook import Phonebook

phonebook = Phonebook()


print(phonebook.add('Gildo4', "84988974488"))
print(phonebook.add('Gildo5', "84988974488"))
print(phonebook.add('Gildo3', "84988974488"))
#print(phonebook.lookup('Gildo'))
print(phonebook.get_phonebook_sorted())
print(phonebook.get_phonebook_reverse())
print(phonebook.entries)
print(phonebook.delete("Gildo5"))
print((phonebook.entries))