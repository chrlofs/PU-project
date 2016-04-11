from vehicle import Vehicle


class Car(Vehicle):
    '''subclass of vehicle'''





if __name__ == "__main__":
    r = Vehicle('reversed')
    n = Car()
    print(r.get_data())
    print(n.get_data())
