from collections import deque
def main():
    #add code here
    store = deque(maxlen=5)
    store.append("STA001")
    list = ["Rice","beans","plantain","eba"]
    store.extend(list)
    store.append("DES001")
    print(store)
    return store

if __name__ == "__main__":
    main()