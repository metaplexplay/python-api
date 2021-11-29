# from https://github.com/diman-io/solana-encrypt-keypair
import argparse
import base58

def native_json(keypair_array):
    return str(keypair_array).replace(" ", "")


def keypair_array(hex_priv, hex_publ):
    return [int(b) for b in bytearray.fromhex(hex_priv + hex_publ)]

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "PRIVATE_KEY",
        help="privake key from fantom wallet",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    
    b58_priv_b58_publ = args.PRIVATE_KEY

    priv_publ = base58.b58decode(b58_priv_b58_publ)
    hex_priv = priv_publ[:32].hex()
    hex_publ = priv_publ[32:].hex()
    
    print(native_json(keypair_array(hex_priv, hex_publ)))


if __name__ == "__main__":
    main()