# Epeuva cli

![master](https://github.com/DT42/epeuva-cli/workflows/main/badge.svg)
![develop](https://github.com/DT42/epeuva-cli/workflows/main/badge.svg?branch=develop)

## Installation (virtualenv)
```
$ git clone git@github.com:DT42/epeuva-cli.git
$ python3 -m venv env
$ source env/bin/activate
(env)$ cd epeuva-cli
(env)$ python3 setup.py install
```

---

### Prequisites

##### Set up Epeuva host

To use the Epeuva CLI, you need to have the access to an Epeuva (the End-to-End AI gateway) instance.

Currently, Epeuva has not been open-sourced yet, but it is planned to be (coming soon). 

##### Create config

The Epeuva CLI will load the config file `~/.epeuva-cli.conf`. 

If this config file is not present or not in the correct format, a prompt will be shown when running any Epeuva CLI command to ask if you want to generate a new config (to replace the old config if any)

```
$ epeuva
[Errno 2] Config file not found: '/home/user/.epeuva-cli.conf'

Would you like to generate/update the config? [y/N]:
```

Enter `y` and the CLI will ask for the Epeuva host url (API url, ex. `https://epeuva.ai/api/v1`), username and password. When you finished, you will see this line:

```
Config file created. Please run the CLI command again.
```

Now you can start using Epeuva CLI.

---


### Usage

##### Basics

Show help

```
$ epeuva --help
```

List all Apps

```
$ epeuva app list
```

Get single app info

```
$ epeuva app detail --id 1 show
```

List all base models

```
$ epeuva base list
```

List all labels of a base model

```
$ epeuva label list --base-id 1
```


##### API to upload training data

Upload images to target label

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

##### Check task status

Track task status

```
$ epeuva task detail --uuid <task-id> show
```

##### API to download trained model

Download original model

```
$  epeuva model detail --id 836 --app-id 1 download
```

Download converted model

```
$ epeuva model detail --id 836 --app-id 1 download --converted
```

