<h1 align="center">
    <p>Steel-Defect-Detection</p>
</h1>

<p align="center">
    <a href="" alt="License">
        <img src="https://img.shields.io/badge/license-MIT-blue" />
    </a>
    <a href="" alt="Python Version">
        <img src="https://img.shields.io/badge/python-3.6%2C3.7%2C3.8-blue?logo=python" />
    </a>
</p> 

<h1 align="center">
    <a href="https://imgbb.com/"><img src="https://i.ibb.co/KxPjZjW/ezgif-com-gif-maker.gif" alt="ezgif-com-gif-maker" border="0"></a>
</h1>

## 📝 Description
- In this project, I have used the **Inceptionv3** and **Inception v4** model with transfer learning for steel defect detection.
- You can check out the deployed web application on http://steeldefect.herokuapp.com/ which runs the lightweight v3 model (**Testing image:** https://res.cloudinary.com/dnz9tlf5t/image/upload/v1645286147/hvknl7w2le3tbss6pjkx.jpg).

## ⏳ Dataset
- For the training, I have used the dataset of the Kaggle competition hosted by Severstal.
- You can check out the competition by below-mentioned link: https://www.kaggle.com/c/severstal-steel-defect-detection/data

## :desktop_computer: Download Pre-trained Model
I have uploaded the whole model on github with git lfs and you just have to run below command :-
```bash
$  git lfs pull --include=models/inceptionv3.h5
$  git lfs pull --include=models/inceptionv4.h5
```

## :gear: Setup
There are two requirements files for the specific web-application deployment and one for the Model training Notebook.
 
1. Install the dependencies for the web application:-
```bash
$ pip install -r requirements.txt

```
2. Install the dependencies for the training notebook:-
```bash
$ pip install -r notebook-requirements.txt

```

