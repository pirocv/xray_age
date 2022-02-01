from fastai.vision import *
import argparse

def main():
    parser=argparse.ArgumentParser(description='predict X-ray age from frontal CXR.')
    parser.add_argument('image', help='CXR image file path')
    args=parser.parse_args()
    image=args.image

    learn=load_learner(
        '.','every_model_age_senet154_v2_tl_26_ft_7_fp32.pkl'
    )
    out=learn.predict(open_image(image))[0]

    print(f"CXR age: {round(out.data[0])}")

if __name__ == '__main__':
    main()




