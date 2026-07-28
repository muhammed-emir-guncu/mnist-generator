import joblib
from model.model import Genes,Digiter
import numpy as np
import matplotlib.pyplot as plt
import random

gen = joblib.load("model/mnist-creator.joblib")

def sayi():
    d="0123456789"
    l=random.randint(3,7)
    xs=str(random.choices(d,k=l))
    return xs

def main():
    imag=gen.gen(sayi())
    plt.imsave("assets/asset-1.png",imag)
    imag=gen.gen(sayi())
    plt.imsave("assets/asset-2.png",imag)
    imag=gen.gen(sayi())
    plt.imsave("assets/asset-3.png",imag)
    imag=gen.gen(sayi())
    plt.imsave("assets/asset-4.png",imag)
if __name__=="__main__":
    main()