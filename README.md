
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

![Architecture Diagram](docs/architecture_v2.png)

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

| Region    | Culture                     |
|-----------|-----------------------------|
| USA       | Basketball court background |
| Argentina | Soccer field background     |

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
# Generated Creative Image Gallery

<table>
<tr>
<td><img src="outputs/creative_argentina_running_shoes1_16x9.png" width="260" style="border-radius:10px; box-shadow:0 3px 10px rgba(0,0,0,0.15);"></td>
<td><img src="outputs/creative_argentina_running_shoes1_1x1.png" width="260" style="border-radius:10px; box-shadow:0 3px 10px rgba(0,0,0,0.15);"></td>
<td><img src="outputs/creative_argentina_running_shoes1_9x16.png" width="260" style="border-radius:10px; box-shadow:0 3px 10px rgba(0,0,0,0.15);"></td>
</tr>

<tr>
<td><img src="outputs/creative_argentina_shoes1_16x9.png" width="260" style="border-radius:10px; box-shadow:0 3px 10px rgba(0,0,0,0.15);"></td>
<td><img src="outputs/creative_argentina_shoes1_1x1.png" width="260" style="border-radius:10px; box-shadow:0 3px 10px rgba(0,0,0,0.15);"></td>
<td><img src="outputs/creative_argentina_shoes1_9x16.png" width="260" style="border-radius:10px; box-shadow:0 3px 10px rgba(0,0,0,0.15);"></td>
</tr>

<tr>
<td><img src="outputs/creative_argentina_shoes2_16x9.png" width="260" style="border-radius:10px; box-shadow:0 3px 10px rgba(0,0,0,0.15);"></td>
<td><img src="outputs/creative_argentina_shoes2_1x1.png" width="260" style="border-radius:10px; box-shadow:0 3px 10px rgba(0,0,0,0.15);"></td>
<td><img src="outputs/creative_argentina_shoes2_9x16.png" width="260" style="border-radius:10px; box-shadow:0 3px 10px rgba(0,0,0,0.15);"></td>
</tr>

<tr>
<td><img src="outputs/creative_usa_running_shoes1_16x9.png" width="260" style="border-radius:10px; box-shadow:0 3px 10px rgba(0,0,0,0.15);"></td>
<td><img src="outputs/creative_usa_running_shoes1_1x1.png" width="260" style="border-radius:10px; box-shadow:0 3px 10px rgba(0,0,0,0.15);"></td>
<td><img src="outputs/creative_usa_running_shoes1_9x16.png" width="260" style="border-radius:10px; box-shadow:0 3px 10px rgba(0,0,0,0.15);"></td>
</tr>

<tr>
<td><img src="outputs/creative_usa_shoes1_16x9.png" width="260" style="border-radius:10px; box-shadow:0 3px 10px rgba(0,0,0,0.15);"></td>
<td><img src="outputs/creative_usa_shoes1_1x1.png" width="260" style="border-radius:10px; box-shadow:0 3px 10px rgba(0,0,0,0.15);"></td>
<td><img src="outputs/creative_usa_shoes1_9x16.png" width="260" style="border-radius:10px; box-shadow:0 3px 10px rgba(0,0,0,0.15);"></td>
</tr>

<tr>
<td><img src="outputs/creative_usa_shoes2_16x9.png" width="260" style="border-radius:10px; box-shadow:0 3px 10px rgba(0,0,0,0.15);"></td>
<td><img src="outputs/creative_usa_shoes2_1x1.png" width="260" style="border-radius:10px; box-shadow:0 3px 10px rgba(0,0,0,0.15);"></td>
<td><img src="outputs/creative_usa_shoes2_9x16.png" width="260" style="border-radius:10px; box-shadow:0 3px 10px rgba(0,0,0,0.15);"></td>
</tr>

</table>

---

# Generated Creative Video Gallery

<table>

<tr>
<td>
<video width="260" controls style="border-radius:10px; box-shadow:0 3px 10px rgba(0,0,0,0.15);">
  <source src="outputs/creative_argentina_shoes1_16x9_multi.mp4" type="video/mp4">
</video>
</td>
<td>
<video width="260" controls style="border-radius:10px; box-shadow:0 3px 10px rgba(0,0,0,0.15);">
  <source src="outputs/creative_argentina_shoes1_1x1_multi.mp4" type="video/mp4">
</video>
</td>
<td>
<video width="260" controls style="border-radius:10px; box-shadow:0 3px 10px rgba(0,0,0,0.15);">
  <source src="outputs/creative_argentina_shoes1_9x16_multi.mp4" type="video/mp4">
</video>
</td>
</tr>

<tr>
<td>
<video width="260" controls style="border-radius:10px; box-shadow:0 3px 10px rgba(0,0,0,0.15);">
  <source src="outputs/creative_argentina_shoes2_16x9_multi.mp4" type="video/mp4">
</video>
</td>
<td>
<video width="260" controls style="border-radius:10px; box-shadow:0 3px 10px rgba(0,0,0,0.15);">
  <source src="outputs/creative_argentina_shoes2_1x1_multi.mp4" type="video/mp4">
</video>
</td>
<td>
<video width="260" controls style="border-radius:10px; box-shadow:0 3px 10px rgba(0,0,0,0.15);">
  <source src="outputs/creative_argentina_shoes2_9x16_multi.mp4" type="video/mp4">
</video>
</td>
</tr>

<tr>
<td>
<video width="260" controls style="border-radius:10px; box-shadow:0 3px 10px rgba(0,0,0,0.15);">
  <source src="outputs/creative_usa_shoes1_16x9_multi.mp4" type="video/mp4">
</video>
</td>
<td>
<video width="260" controls style="border-radius:10px; box-shadow:0 3px 10px rgba(0,0,0,0.15);">
  <source src="outputs/creative_usa_shoes1_1x1_multi.mp4" type="video/mp4">
</video>
</td>
<td>
<video width="260" controls style="border-radius:10px; box-shadow:0 3px 10px rgba(0,0,0,0.15);">
  <source src="outputs/creative_usa_shoes1_9x16_multi.mp4" type="video/mp4">
</video>
</td>
</tr>

<tr>
<td>
<video width="260" controls style="border-radius:10px; box-shadow:0 3px 10px rgba(0,0,0,0.15);">
  <source src="outputs/creative_usa_shoes2_16x9_multi.mp4" type="video/mp4">
</video>
</td>
<td>
<video width="260" controls style="border-radius:10px; box-shadow:0 3px 10px rgba(0,0,0,0.15);">
  <source src="outputs/creative_usa_shoes2_1x1_multi.mp4" type="video/mp4">
</video>
</td>
<td>
<video width="260" controls style="border-radius:10px; box-shadow:0 3px 10px rgba(0,0,0,0.15);">
  <source src="outputs/creative_usa_shoes2_9x16_multi.mp4" type="video/mp4">
</video>
</td>
</tr>

</table>

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

# Video Creative Generation

* Extend the pipeline to generate **short video creatives (3–10 seconds)** from static images
* Add motion effects such as **zoom (Ken Burns), pan, fade, and parallax**
* Export videos optimized for **TikTok, Instagram Reels, and YouTube Shorts**

---

# Audio & Music Integration

* Support adding **background music and sound effects** from an `assets/audio/` folder
* Enable **audio mixing** (music + effects + voice)
* Automatically trim and sync audio with video duration

---

# Text-to-Speech (TTS) for Localization

* Generate **region-specific voiceovers** using open-source TTS models (e.g., Coqui TTS)
* Add **localized chants or slogans** as audio overlays
* Support **multilingual voice generation** for global campaigns

---

# Multi-Scene Video Storytelling

* Generate multi-scene creatives:

  * Intro (brand/logo)
  * Product highlight
  * CTA ending
* Add smooth **transitions between scenes**

---

# Social Media Optimization

* Automatically tailor creatives for:

  * **9:16 (Reels/TikTok)**
  * **1:1 (Instagram posts)**
  * **16:9 (YouTube ads)**
* Optimize layout, pacing, and text placement per platform

---

# Beat-Synced Motion (Advanced)

* Analyze background music (e.g., using `librosa`)
* Sync motion effects and transitions with **music beats**

---

# AI-Powered Creative Optimization

* Rank creatives based on predicted engagement
* Use ML models to estimate **CTR and conversion performance**
* Automatically select best-performing variants

---

# Captions & Accessibility

* Auto-generate **subtitles and captions**
* Improve accessibility and engagement

---

# Scalable Video Generation

* Introduce:

  * async processing workers
  * GPU-based rendering pipelines
  * cloud storage (S3/CDN)
* Enable large-scale parallel creative generation

---

# Advanced GenAI Enhancements

* Integrate **video generation models** (AnimateDiff, Stable Video Diffusion)
* Improve **prompt engineering** for higher-quality outputs
* Add **brand-aware and style-consistent generation**

---

# A/B Testing & Feedback Loop

* Generate multiple creative variations automatically
* Evaluate performance metrics
* Continuously improve generation quality using feedback
