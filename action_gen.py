import joblib
from model.model import Genes,Digiter
import numpy as np
import matplotlib.pyplot as plt

gen = joblib.load("model/mnist-creator.joblib")
def main():
    imag=gen.gen("123")
    plt.imsave("asset.png",imag)
if __name__=="__main__":
    main()