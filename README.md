# Epeuva cli

## Installation
```
$ git clone git@github.com:DT42/epeuva-cli.git
$ cd epeuva-cli
$ python3 setup.py install
```

---


### Usage

##### Basics

Show help

```
$ epeuva --help
```



Show Apps

```
$ epeuva app list
```



Get single app info

```
$ epeuva app detail --id 1 show
```



Get base model list

```
$ epeuva base list
```



Get label list

```
$ epeuva label list --base-id 1
```


##### API to upload training data and labels



Upload image to target label

```
$ epeuva label detail --id 3 upload_images *.jpg
```



##### API to trigger training pipeline on Epeuva



Retrain model

```
$ epeuva job retrain --model-name cli-test-00 \
    --label-list label.txt \
    --app-id 1 \
    --note "Hello world"
```



##### API to convert model for a specific hardware



Convert model

```
$ epeuva job convert --model-name cli-test-00 --model-id 836 --platform snpe --app-id 1
```



Track task status

```
$ epeuva task detail --uuid <task-id> show
```



##### API to download trained model and deploy



Download original model

```
$  epeuva model detail --id 836 --app-id 1 download
```



Download converted model

```
$ epeuva model detail --id 836 --app-id 1 download --converted
```

