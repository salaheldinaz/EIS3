import os
import requests
from time import sleep
from datetime import datetime
import argparse
import json
from web3 import Web3
from ens import ENS


def banner():
    print("███████╗██╗███████╗ \n"
          "██╔════╝██║██╔════╝ \n"
          "█████╗  ██║███████╗ \n"
          "██╔══╝  ██║╚════██║ \n"
          "███████╗██║███████║ \n"
          "╚══════╝╚═╝╚══════╝ ENS Info Scanner 3.0\n")


def get_eth_address(domain_):
    tries = 0
    while tries <= 3:
        # look up the hex representation of the address for a name
        try:
            eth_address = ns.address(domain_)
            if eth_address:
                print(f"ETH Address:", eth_address)
            else:
                print(f"ETH Address: Expired")

            return eth_address
        except Exception as e:
            print(f"Error get_eth_address for {domain}:\n {e}")
            tries += 1


def get_domain(eth_address_):
    # get the domain from the address
    tries = 0
    while tries <= 3:
        try:
            domain = ns.name(eth_address_)
            print(f"Domain:", domain)
            return domain
        except Exception as e:
            print(f"Error get_domain for {eth_address_}:\n {e}")


def get_controller(domain_):
    # get Domain Controller
    tries = 0
    while tries <= 3:
        try:
            domain_controller = ns.owner(domain_)
            print(f"Controller:", domain_controller)
            return domain_controller
        except Exception as e:
            print(f"Error get_controller for {domain_}:\n {e}")


def get_domain_namehash(domain_: str):
    # get domain name hash
    try:
        name_hash = ns.namehash(domain_)
        print("Name Hash:", w3.toHex(name_hash))
        return name_hash
    except Exception as e:
        print(f"Error get_domain_namehash for {domain_}:\n {e}")


def get_domain_labelhash(domain_: str):
    # get domain label hash
    try:
        domain_label = domain_.split(".")[0]
        label_hash = ns.labelhash(domain_label)
        print("Label Hash:", w3.toHex(label_hash))
        return label_hash
    except Exception as e:
        print(f"Error get_domain_labelhash for {domain_}:\n {e}")


def get_token_id(label_hash_):
    token_id = int(w3.toHex(label_hash_), 0)
    print("TokenID:", token_id)
    return token_id


def get_domain_resolver(domain_):
    # Get Resolver
    tries = 0
    while tries <= 3:
        try:
            dns_resolver = ns.resolver(domain_)
            ens_resolver_contract = dns_resolver.address
            print(f"Resolver:", ens_resolver_contract)

            abi_file = '[{"inputs":[{"internalType":"contract ENS","name":"_ens","type":"address"},{"internalType":"bytes32","name":"_baseNode","type":"bytes32"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"approved","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":false,"internalType":"bool","name":"approved","type":"bool"}],"name":"ApprovalForAll","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"controller","type":"address"}],"name":"ControllerAdded","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"controller","type":"address"}],"name":"ControllerRemoved","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"id","type":"uint256"},{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":false,"internalType":"uint256","name":"expires","type":"uint256"}],"name":"NameMigrated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"id","type":"uint256"},{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":false,"internalType":"uint256","name":"expires","type":"uint256"}],"name":"NameRegistered","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"id","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"expires","type":"uint256"}],"name":"NameRenewed","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Transfer","type":"event"},{"constant":true,"inputs":[],"name":"GRACE_PERIOD","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"controller","type":"address"}],"name":"addController","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"approve","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"available","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"baseNode","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"controllers","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"ens","outputs":[{"internalType":"contract ENS","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getApproved","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"operator","type":"address"}],"name":"isApprovedForAll","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"isOwner","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"nameExpires","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"ownerOf","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address","name":"owner","type":"address"}],"name":"reclaim","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"duration","type":"uint256"}],"name":"register","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"duration","type":"uint256"}],"name":"registerOnly","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"controller","type":"address"}],"name":"removeController","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint256","name":"duration","type":"uint256"}],"name":"renew","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"renounceOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"safeTransferFrom","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"safeTransferFrom","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"bool","name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"resolver","type":"address"}],"name":"setResolver","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes4","name":"interfaceID","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"transferFrom","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]'

            abi_file = [
                {
                    "constant": True,
                    "inputs": [
                        {
                            "internalType": "bytes32",
                            "name": "node",
                            "type": "bytes32"
                        },
                        {
                            "internalType": "string",
                            "name": "key",
                            "type": "string"
                        }
                    ],
                    "name": "text",
                    "outputs": [
                        {
                            "internalType": "string",
                            "name": "",
                            "type": "string"
                        }
                    ],
                    "payable": False,
                    "stateMutability": "view",
                    "type": "function"
                }
            ]

            contract_ = w3.eth.contract(address=ens_resolver_contract, abi=abi_file)
            return contract_, ens_resolver_contract
        except Exception as e:
            print(f"Error get_domain_resolver for {domain_}:\n {e}")


def get_registrant(domain_):
    primary_name = domain_.split('.')[-2]
    # Get Smart contract of BaseRegistrarImplementation.sol
    address_str = '0x57f1887a8BF19b14fC0dF6Fd9B2acc9Af147eA85'
    address_chksum = w3.toChecksumAddress(address_str)
    abi = [
        {
            "constant": True,
            "inputs": [
                {
                    "internalType": "uint256",
                    "name": "tokenId",
                    "type": "uint256"
                }
            ],
            "name": "ownerOf",
            "outputs": [
                {
                    "internalType": "address",
                    "name": "",
                    "type": "address"
                }
            ],
            "payable": False,
            "stateMutability": "view",
            "type": "function"
        },
    ]

    contract_instance = w3.eth.contract(address=address_chksum, abi=abi)
    registrant = contract_instance.functions.ownerOf(Web3.toInt(Web3.keccak(text=primary_name))).call()
    print("Registrant:", registrant)
    return registrant


def get_txt_records(contract_, name_hash_, domain_):
    # get top txt record
    # https://etherscan.io/address/0x4976fb03c32e5b8cfe2b6ccb31c09ba78ebaba41

    tries = 0
    while tries <= 3:
        try:
            txt_records = []
            txt_labels = ["snapshot", "email", "url", "avatar", "description", "notice", "keywords", "display",
                          "com.discord", "com.github", "com.reddit", "com.twitter", "org.telegram", "com.peepeth",
                          "io.keybase", "com.linkedin", "eth.ens.delegate", "mail", "location", "phone"]

            for txt_label in txt_labels:
                txt_record_value = contract_.functions.text(name_hash_, txt_label).call()

                if txt_record_value:
                    print(f"{txt_label}: {txt_record_value}")
                    txt_records.append({txt_label: txt_record_value})
            return txt_records
        except Exception as e:
            print(f"Error get_txt_records for {domain_}:\n {e}")


def get_domain_info(domain_, address_=None):
    tries = 0
    while tries <= 3:
        try:
            domain_info = {}
            if not address_:
                eth_address = get_eth_address(domain_=domain)
            else:
                eth_address = address_

            name_hash = get_domain_namehash(domain_=domain)
            label_hash = get_domain_labelhash(domain_=domain)
            token_id = get_token_id(label_hash_=label_hash)

            domain_controller = get_controller(domain_=domain_)
            domain_registrant = get_registrant(domain_)
            contract, resolver_address = get_domain_resolver(domain_=domain_)
            domain_metadata, register_date, expiration_date = get_domain_metadata(domain_=domain, token_id_=token_id)
            txt_records = get_txt_records(contract_=contract, name_hash_=name_hash, domain_=domain_)

            domain_info.update({
                domain_: {
                    "address": eth_address,
                    "controller": domain_controller,
                    "registrant": domain_registrant,
                    "token_id": token_id,
                    "register_data": register_date,
                    "expiration_data": expiration_date,
                    "resolver": resolver_address,
                    "txt_records": txt_records,
                    "metadata": domain_metadata
                }
            })

            return domain_info
        except Exception as e:
            print(f"Error get_domain_info for {domain_}:\n {e}")


def get_domain_metadata(domain_, token_id_):
    domain_metadata = {}
    register_date = None
    expiration_date = None
    # https://etherscan.io/accounts/label/ens
    ens_contract_address = "0x57f1887a8BF19b14fC0dF6Fd9B2acc9Af147eA85"

    try:
        api_url = f"https://metadata.ens.domains/mainnet/{ens_contract_address}/{token_id_}/"
        response = requests.get(url=api_url)
        if response.status_code == 200:
            domain_metadata = response.json()
            print(f"Metadata:", domain_metadata)
            register_timestamp = domain_metadata["attributes"][2]["value"] / 1000
            register_date = datetime.utcfromtimestamp(register_timestamp).strftime("%b %d,%Y, %H:%M:%S")
            print(f"Registration Date: {register_date}")

            expiration_timestamp = domain_metadata["attributes"][3]["value"] / 1000
            expiration_date = datetime.utcfromtimestamp(expiration_timestamp).strftime("%b %d,%Y, %H:%M:%S")
            print(f"Expiration Date: {expiration_date}")
        else:
            domain_metadata = response.json()
            print(f"No metadata found for {domain_}:", domain_metadata)

    except Exception as e:
        print(f"Error get_domain_metadata for {domain_}:\n {e}")

    return domain_metadata, register_date, expiration_date


if __name__ == "__main__":
    banner()
    parser = argparse.ArgumentParser(description="Search for information about ens domain or eth address using ENS "
                                                 "contracts in Ethereum chain, and ENS metadata api.")
    parser.add_argument("-k", "--key", type=str, help="Input infura project id", required=True)
    run_type = parser.add_mutually_exclusive_group(required=True)
    run_type.add_argument("-l", "--list", type=argparse.FileType('r'), help="Enter list file path ")
    run_type.add_argument("-d", "--domain", type=str, help="Enter Domain vitalik.eth")
    run_type.add_argument("-a", "--address", type=str,
                          help="Enter ETH Address 0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045")
    parser.add_argument("-s", "--start", type=int, default=1, help="Where to start in the domains list.")
    parser.add_argument("-e", "--end", type=int, default=-1, help="Where to stop in the domains list.")

    args = parser.parse_args()
    domains_data = []
    rpc_url = f"https://mainnet.infura.io/v3/{args.key}"
    w3 = None
    try:
        w3 = Web3(Web3.HTTPProvider(rpc_url))
    except Exception as e:
        print(f"Error 1 connecting to infura rpc:\n {e}")
        exit()

    # Check result folder
    if not os.path.exists('results'):
        os.makedirs("results")

    if w3.isConnected():
        ns = ENS.fromWeb3(w3)

        if args.domain:
            domain = args.domain
            print(f"\n{domain} =======")
            domain_data = get_domain_info(domain_=domain)
            domains_data.append(domain_data)

        elif args.address:
            address_str = args.address
            try:
                address_chksum = w3.toChecksumAddress(address_str)

                if w3.isAddress(address_chksum) and w3.isChecksumAddress(address_chksum):
                    print(f"\n{address_chksum} =======")
                    domain = get_domain(eth_address_=address_chksum)
                    if domain:
                        domain_data = get_domain_info(domain_=domain, address_=address_chksum)
                        domains_data.append(domain_data)
                    else:
                        print(f"{address_chksum} address is not an eth domain.")
                else:
                    print(f"{address_chksum} address is not correct.")

            except Exception:
                print(f"{address_str} address is not correct.")

        elif args.list:
            domains_file = args.list
            start_no = args.start
            end_no = args.end
            print(f"Scanning from {start_no}:{end_no}...")

            list_of_domains = [line.strip() for line in domains_file.readlines()]
            target_list = list_of_domains[start_no - 1:end_no]
            print("Targets list", target_list)
            count_ = 1

            for domain in target_list:
                print(f"\n{count_} | {domain} =======")
                try:
                    domain_data = get_domain_info(domain_=domain)

                    if domain_data:
                        domains_data.append(domain_data)
                    count_ += 1
                    sleep(0.5)

                except KeyboardInterrupt:
                    print(f"Hello user you have pressed ctrl-c button...\n")
                    break
                except Exception as e:
                    print(f"Error {domain}:\n {e}")

        with open(f"./results/{datetime.now().timestamp()}.json", "w") as result_file:
            print(domains_data)
            if domains_data:
                print("Saving data to file...")
                json.dump(domains_data, result_file, indent=4)
    else:
        print("Error 2 connecting to infura rpc.")
