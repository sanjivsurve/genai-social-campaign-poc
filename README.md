```markdown
# GenAI Social Campaign Automation (POC)

This project demonstrates a **Generative AI powered system that automatically generates social media advertising creatives** based on a campaign brief.

The system automates:

- Campaign creative generation
- Brand compliance checks
- Localization for different regions
- Cultural adaptation (sports themes, chants, etc.)
- Multi-aspect-ratio social media creatives

If product assets are missing, the system automatically generates them using a **local Stable Diffusion XL (SDXL) model**.

---

# Table of Contents

- [Architecture](#architecture)
- [Key Features](#key-features)
- [Repository Structure](#repository-structure)
- [Campaign JSON Structure](#campaign-json-structure)
- [Product Asset Logic](#product-asset-logic)
- [GenAI Product Generation](#genai-product-generation)
- [Installation](#installation)
- [Running the Campaign Generator](#running-the-campaign-generator)
- [Output](#output)
- [Limitations](#limitations)
- [Future Enhancements](#future-enhancements)

---

# Architecture

The architecture of the system is shown below.

![Architecture Diagram](https://raw.githubusercontent.com/sanjivsurve/genai-social-campaign-poc/main/docs/architecture_v2.png)

The pipeline flows from:

```

Campaign Input
↓
Asset Discovery
↓
GenAI Product Generation (if assets missing)
↓
Creative Composition
↓
Compliance Checks
↓
Final Social Media Outputs

```

---

# Key Features

## Campaign Automation

- Generates social campaign creatives automatically from JSON input
- Supports multiple regions and localized messaging

---

## Multi-Aspect Ratio Creative Generation

Outputs creatives for common social media formats:

| Aspect Ratio | Platform Examples |
|---------------|------------------|
| **1:1** | Instagram / Facebook Posts |
| **9:16** | Reels / TikTok / Stories |
| **16:9** | YouTube / Landscape Ads |

---

## Brand Compliance

Includes checks for:

- Brand color usage
- Logo presence
- Prohibited words

---

## Cultural Adaptation

Region-specific creative variations.

Example:

| Region | Culture |
|------|------|
| USA | Basketball court background |
| Argentina | Soccer field background |

---

## Automatic Product Generation (GenAI)

If product images are not found locally:

- Uses **Stable Diffusion XL**
- Generates photorealistic product images
- Removes background
- Saves to the product asset folder

Model used:

```

stabilityai/stable-diffusion-xl-base-1.0

```

---

# Repository Structure

```

genai-social-campaign-poc/
│
├── src/
│   ├── main.py
│   ├── campaign_engine.py
│   ├── overlay_engine.py
│   ├── image_generator.py
│   ├── asset_manager.py
│   ├── compliance.py
│   ├── localization.py
│   └── genai_product_generator.py
│
├── assets/
│   ├── logo/
│   │   └── logo.png
│   │
│   └── products/
│       └── running_shoes1.png
│
├── outputs/
│   └── generated creatives
│
├── docs/
│   └── architecture.png
│
├── campaign_brief_example.json
├── requirements.txt
├── README.md
└── .gitignore

````

---

# Campaign JSON Structure

Campaign creatives are generated based on a **campaign brief JSON file**.

Example:

```json
{
  "product": "running_shoes",

  "brand_colors": {
    "primary": "#FFD54F",
    "secondary": "#FFF8E1"
  },

  "regions": [
    {
      "name": "usa",
      "campaign_message": "Own the court with unstoppable style",
      "cta": "Shop Now",
      "culture": {
        "sport": "basketball",
        "chant": "Let's Go!"
      }
    },
    {
      "name": "argentina",
      "campaign_message": "Domina la cancha con estilo imparable",
      "cta": "Compra Ahora",
      "culture": {
        "sport": "soccer",
        "chant": "Vamos!"
      }
    }
  ]
}
````

---

## Fields

| Field            | Description                               |
| ---------------- | ----------------------------------------- |
| product          | Product name used to match product images |
| brand_colors     | Colors used in creative design            |
| regions          | Regional campaign configurations          |
| campaign_message | Text displayed on creatives               |
| cta              | Call-to-action button text                |
| culture          | Influences background visuals             |

---

# Product Asset Logic

The system looks for product images inside:

```
assets/products/
```

Matching logic:

```
filename starts with product name
```

Example:

```
product = running_shoes
```

Valid assets:

```
running_shoes1.png
running_shoes_pro.png
running_shoes_red.png
```

---

# GenAI Product Generation

If no matching product assets exist:

1. The system triggers **local Stable Diffusion generation**
2. Generates a **photorealistic product image**
3. Removes background
4. Saves image automatically

Example output:

```
assets/products/running_shoes1.png
```

This generated asset is then used in the campaign pipeline.

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/sanjivsurve/genai-social-campaign-poc.git
cd genai-social-campaign-poc
```

---

## 2. Create Python Virtual Environment

```bash
python -m venv venv
```

Activate:

### Windows

```
venv\Scripts\activate
```

### Linux / Mac

```
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Example `requirements.txt`:

```
torch
diffusers
transformers
accelerate
safetensors
pillow
numpy
```

---

# Running the Campaign Generator

Execute the campaign generator using:

```
python src/main.py campaign_brief_example.json
```

---

# Output

Generated creatives will be saved under:

```
outputs/
```

Example:

```
creative_usa_running_shoes1_1x1.png
creative_usa_running_shoes1_9x16.png
creative_usa_running_shoes1_16x9.png

creative_argentina_running_shoes1_1x1.png
creative_argentina_running_shoes1_9x16.png
creative_argentina_running_shoes1_16x9.png
```

---

# Example Generated Creatives

The system automatically produces:

* branded visuals
* localized messaging
* culturally relevant backgrounds
* consistent brand design

---

# Limitations

This POC is designed for demonstration purposes.

Current limitations:

* Background removal is basic
* GenAI generation may take time on CPU
* Prompt engineering can be improved for product quality
* Brand compliance rules are simplified

---

# Future Enhancements

Possible improvements:

* Vector database for brand assets
* LLM prompt optimization
* Creative ranking model
* Multi-product campaigns
* Async campaign generation workers
* Automatic A/B testing
* Cloud GPU inference
