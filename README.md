# image_denoiser
This project is for removing noise from scans of technical documents.

### List of supported formats

currently [all formats supported by the PILLOW library](https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html) in version 9.0.0 should be supported. some of the weird ones with exotic (e.g. with many bits per channel) probably aren't and you will find this out if PIL gives you spicy errors

### requirements
please run `pipreqs`

### usage

```
python src/denoiser.py
```
provided the image `test_pic.jpeg` is in your `inputs/` folder.<br>
this will create a cleaned output you'll be able to find at `outputs/test_pic_denoised.jpeg`
