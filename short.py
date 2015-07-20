"""A script to map 5base key to a url"""
import pickle


def add_to_store(store,url):

    last = list(store['last'])
    short_url = last
    pos = store['change']

    #this is not all possible permutation algorithm
    j = pos+1
    while True:

         #store.values() method will be terribly slow in large
         #database. Could be changed to one more seperate dict
         if ''.join(short_url) not in store.values():
            break
 
         if j == pos:
            pos += 1
            j = pos+1

         if j==5:
            j = 0

         if pos == 5:
            return "not possible anymore"
         temp = ord(short_url[j])
         if temp != 122:
            short_url[j] = chr(temp+1)

         else:
            j+=1

    #update the data.txt file
    store['change'] = pos
    store['last'] = ''.join(short_url)
    store[url] = ''.join(short_url)
    write(store)
    return store[url]

def write(store):
    with open('data.txt', 'wb') as f:
        pickle.dump(store, f) 

def shorten(url):
    #store the dict in the text file for later use
    #store is the dict which should store the exsisting URL
    
    with open('data.txt', 'rb') as f:
        store = pickle.loads(f.read())

    if url in store:
        return store[url]

    result = add_to_store(store,url)
    return result

if __name__ == '__main__':
    url = raw_input("Enter the URL to be shortened")
    print(shorten(url))
