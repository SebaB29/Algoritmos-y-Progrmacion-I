from ejercicio3 import fahrenheit_a_celsius

def main():
    for tf in range(0, 121, 10):
        tc = fahrenheit_a_celsius(tf)
        
        print(f'TF: {tf}  →   TC:{tc}')

main()