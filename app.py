import joblib
from model.model import Genes,Digiter
import numpy as np
import matplotlib.pyplot as plt
import sys
import io
from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse



import __main__
__main__.Digiter = Digiter
__main__.Genes = Genes

if '__mp_main__' in sys.modules:
    sys.modules['__mp_main__'].Digiter = Digiter
    sys.modules['__mp_main__'].Genes = Genes
# -----------------------


app = FastAPI(
    title="MNIST Generative KDE Service",
    description="PCA + KDE kullanarak çoklu rakam sentezleyen üretken API servisi.",
    version="1.0.0"
)

digit_service = joblib.load("model/mnist-creator.joblib")

@app.get("/")
def read_root():
    return {
        "status": "online",
        "message": "MNIST Generative API'ye hoş geldiniz. /generate/3087 şeklinde istek atabilirsiniz."
    }

@app.get("/generate/{number}", summary="Rakam Görseli Üret")
async def generate_digits(number: str):
    if not number.isdigit():
        raise HTTPException(
            status_code=400, 
            detail="Lütfen sadece rakamlardan oluşan bir girdi girin (örn: 3087)."
        )
    
    try:
        img_np = digit_service.gen_cut(number)
        
        img = io.BytesIO()
        
        plt.imsave(img, img_np, cmap='gray', format='png')
        
        img.seek(0)
        return StreamingResponse(img, media_type="image/PNG")
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Görsel üretilirken sunucu hatası oluştu: {str(e)}")