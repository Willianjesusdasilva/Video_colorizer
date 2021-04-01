import matplotlib.pyplot as plt
from Video_colorizer.colorizers import *
import numpy as np


def colorize_frame(img):
        #colorizer_eccv16 = eccv16(pretrained=True).eval()
        colorizer_siggraph17 = siggraph17(pretrained=True).eval()
        if(True):
                #colorizer_eccv16.cuda()
                colorizer_siggraph17.cuda()
        img = load_img(img)
        (tens_l_orig, tens_l_rs) = preprocess_img(img, HW=(256,256))
        if(True):
                tens_l_rs = tens_l_rs.cuda()

        img_bw = postprocess_tens(tens_l_orig, torch.cat((0*tens_l_orig,0*tens_l_orig),dim=1))
        #out_img_eccv16 = postprocess_tens(tens_l_orig, colorizer_eccv16(tens_l_rs).cpu())
        out_img_siggraph17 = postprocess_tens(tens_l_orig, colorizer_siggraph17(tens_l_rs).cpu())

        #return out_img_eccv16
        return out_img_siggraph17
