class kafeteria:
    def __init__(self, kafes=0, gala=0, zaxari=0, nero=0):
        
    def status(self):
        
        
    
    def __add__(self, other):
        
        
    
    def __call__(self, kafes, gala, zaxari, nero):
        
        
    def __eq__(self, other):
        

    def __mul__(self, number):
        
        



kaf1 = kafeteria(100, 50, 200, 1000)
kaf2 = kafeteria(10, 20, 30, 40)


print("kaf1 status:")
kaf1.status()
print("kaf2 status:")
kaf2.status()


kaf3 = kaf1 + kaf2
print("\nkaf3 status (kaf1 + kaf2):")
kaf3.status()


kaf1(200, 100, 400, 2000)
print("\nkaf1 status μετά την ενημέρωση:")
kaf1.status()


print("\nkaf1 == kaf2:", kaf1 == kaf2)


kaf4 = kaf1 * 2
print("\nkaf4 status (kaf1 * 2):")
kaf4.status()
