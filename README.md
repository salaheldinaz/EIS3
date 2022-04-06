[![Awesome](https://awesome.re/badge-flat2.svg)](https://github.com/salaheldinaz/eis)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![Docker Image CI](https://github.com/salaheldinaz/eis3/actions/workflows/docker-image.yml/badge.svg)](https://github.com/salaheldinaz/eis3/actions/workflows/docker-image.yml)


<h1 align="center">ENS Info Scanner (EIS 3.0)</h1>

*<p align="center">Search for information about ens domain or eth address using ENS contracts in Ethereum chain, and ENS metadata api.</p>*

---

_Ethereum Name Service (ENS) is a distributed, extensible naming system based on the Ethereum blockchain._


### Prerequisite
- Python 3.7 or newer.
- Infura API key (free).  https://infura.io/

### Installation
```shell
pip install -r requirements.txt
```

---
### Usage

#### Single Domain Scan 
```shell
python main.py -d <domain.eth> -k <infura-api-key>
```
ex. `python main.py -d nick.eth -k 123456789abcdefg`

---
#### List of Domains Scan
```shell
python main.py -l <path-to-file> -k <infura-api-key>
```
ex. `python main.py -l list.txt -k 123456789abcdefg`

You can use:

`-s` to specify where to start in the list

`-e` to specify where to stop in the list

ex. `-s 100 -e 200` 

---

#### Ethereum Address Scan
```shell
python main.py -a <ethereum-address> -k <infura-api-key>
```
ex. `python main.py -a 0xb8c2c29ee19d8307cb7255e1cd9cbde883a267d5 -k 123456789abcdefg`

---

### Using Docker

##### Using the published image

```shell
docker run -it --rm -v `pwd`:/app/results/ salaheldinaz/eis3:latest -d nick.eth -k 123456789abcdefg
```
`pwd` This folder will be used to save the result.

---

##### Using a local docker image
1. Build
```shell
docker build -t "eis3:latest" . 
```

2. Run
```shell
docker run -it --rm -v `pwd`:/app/results/ eis3:latest -d nick.eth -k 123456789abcdefg
```
`pwd` This folder will be used to save the result.

---
### Output Example 
```shell
███████╗██╗███████╗
██╔════╝██║██╔════╝
█████╗  ██║███████╗
██╔══╝  ██║╚════██║
███████╗██║███████║
╚══════╝╚═╝╚══════╝ ENS Info Scanner 3.0

nick.eth =======
ETH Address: 0xb8c2C29ee19D8307cb7255e1Cd9CbDE883A267d5
Name Hash: 0x05a67c0ee82964c4f7394cdd47fee7f4d9503a23c09c38341779ea012afe6e00
Label Hash: 0x5d5727cb0fb76e4944eafb88ec9a3cf0b3c9025a4b2f947729137c5d7f84f68f
TokenID: 42219085255511335250589442208301538195142221433306354426240614732612795430543
Controller: 0xb8c2C29ee19D8307cb7255e1Cd9CbDE883A267d5
Registrant: 0xb8c2C29ee19D8307cb7255e1Cd9CbDE883A267d5
Resolver: 0x4976fb03C32e5B8cfe2b6cCB31c09Ba78EBaBa41
Metadata: {'is_normalized': True, 'name': 'nick.eth', 'description': 'nick.eth, an ENS name.', 'attributes': [{'trait_type': 'Created Date', 'display_type': 'date', 'value': None}, {'trait_type': 'Length', 'display_type': 'number', 'value': 4}, {'trait_type': 'Registration Date', 'display_type': 'date', 'value': 1580803395000}, {'trait_type': 'Expiration Date', 'display_type': 'date', 'value': 1698131707000}], 'name_length': 4, 'url': 'https://app.ens.domains/name/nick.eth', 'version': 0, 'background_image': 'https://metadata.ens.domains/mainnet/avatar/nick.eth', 'image_url': 'https://metadata.ens.domains/mainnet/0x57f1887a8BF19b14fC0dF6Fd9B2acc9Af147eA85/0x5d5727cb0fb76e4944eafb88ec9a3cf0b3c9025a4b2f947729137c5d7f84f68f/image'}
Registration Date: Feb 04,2020, 08:03:15
Expiration Date: Oct 24,2023, 07:15:07
snapshot: ipns://storage.snapshot.page/registry/0xb8c2C29ee19D8307cb7255e1Cd9CbDE883A267d5/nick.eth
email: arachnid@notdot.net
url: https://ens.domains/
avatar: eip155:1/erc1155:0x495f947276749ce646f68ac8c248420045cb7b5e/8112316025873927737505937898915153732580103913704334048512380490797008551937
com.discord: nickjohnson#0001
com.github: arachnid
com.twitter: nicksdjohnson
eth.ens.delegate: https://discuss.ens.domains/t/ens-dao-delegate-applications/815/716
[{'nick.eth': {'address': '0xb8c2C29ee19D8307cb7255e1Cd9CbDE883A267d5', 'controller': '0xb8c2C29ee19D8307cb7255e1Cd9CbDE883A267d5', 'registrant': '0xb8c2C29ee19D8307cb7255e1Cd9CbDE883A267d5', 'token_id': 42219085255511335250589442208301538195142221433306354426240614732612795430543, 'register_data': 'Feb 04,2020, 08:03:15', 'expiration_data': 'Oct 24,2023, 07:15:07', 'resolver': '0x4976fb03C32e5B8cfe2b6cCB31c09Ba78EBaBa41', 'txt_records': [{'snapshot': 'ipns://storage.snapshot.page/registry/0xb8c2C29ee19D8307cb7255e1Cd9CbDE883A267d5/nick.eth'}, {'email': 'arachnid@notdot.net'}, {'url': 'https://ens.domains/'}, {'avatar': 'eip155:1/erc1155:0x495f947276749ce646f68ac8c248420045cb7b5e/8112316025873927737505937898915153732580103913704334048512380490797008551937'}, {'com.discord': 'nickjohnson#0001'}, {'com.github': 'arachnid'}, {'com.twitter': 'nicksdjohnson'}, {'eth.ens.delegate': 'https://discuss.ens.domains/t/ens-dao-delegate-applications/815/716'}], 'metadata': {'is_normalized': True, 'name': 'nick.eth', 'description': 'nick.eth, an ENS name.', 'attributes': [{'trait_type': 'Created Date', 'display_type': 'date', 'value': None}, {'trait_type': 'Length', 'display_type': 'number', 'value': 4}, {'trait_type': 'Registration Date', 'display_type': 'date', 'value': 1580803395000}, {'trait_type': 'Expiration Date', 'display_type': 'date', 'value': 1698131707000}], 'name_length': 4, 'url': 'https://app.ens.domains/name/nick.eth', 'version': 0, 'background_image': 'https://metadata.ens.domains/mainnet/avatar/nick.eth', 'image_url': 'https://metadata.ens.domains/mainnet/0x57f1887a8BF19b14fC0dF6Fd9B2acc9Af147eA85/0x5d5727cb0fb76e4944eafb88ec9a3cf0b3c9025a4b2f947729137c5d7f84f68f/image'}}}]
```

---

Authors

[![Michael James](https://img.shields.io/twitter/follow/ginsberg5150?style=social&logo=twitter)](https://twitter.com/ginsberg5150)
     [![Salaheldinaz](https://img.shields.io/twitter/follow/salaheldinaz?style=social&logo=twitter)](https://twitter.com/salaheldinaz)
