import json
import os
import numpy as np

def main():

    image_cid = "Qmc3PaGYADjfirAQqBmRvhy7FJrgqvYmAgwGfYv3hF5m8Q"
    animation_url_cid = "QmP41Gnw8pM28X6oBu3C7ydUoLkFXhQqaqjFeXPx1vpLs6"
    os.makedirs("/Users/chrisrussell/Cryptids/cryptid-generation/output/prereveal_metadata", exist_ok=True)           

    # print(file_name)
    for i in range(1, 7778):

        with open(f"/Users/chrisrussell/Cryptids/cryptid-generation/output/prereveal_metadata/{i}.json", "w") as o:

            metadata = {
                "name": f"Cryptid #{i}",
                "description": "Part fantasy, part science-fiction. Cryptids is a generative art collection of 7,777 fantastic mythical creatures. Created by @no__solo and @chrisrusselljr.",
                "image": f"ipfs://{image_cid}",
                "animation_url": f"ipfs://{animation_url_cid}",
                "attributes": []
                }

            json.dump(metadata, o, indent=4)


if __name__ == "__main__":
    main()

