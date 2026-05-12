# 🕊️ FAIR
## Filter And Image Removal

<p align="center">

AI Quality Assurance Infrastructure for Automotive Insurance Intelligence

</p>

---

## Overview

FAIR is the visual integrity infrastructure of the MARSAIL ecosystem.

The system performs deterministic mathematical validation and semantic AI verification before downstream underwriting and claim assessment inference.

FAIR is designed to prevent:

- Blurry submissions
- Over-exposed images
- Under-exposed images
- Non-vehicle content
- Fraudulent screenshots
- Super zoom-in structural corruption

from contaminating production AI pipelines.

---

## MARSAIL Laboratory

**MARSAIL**  
Motor AI Recognition Solution AI Laboratory

Developer:
**Teerapong Panboonyuen (Kao)**

---

# System Architecture

```text
Input Image
    ↓
Mathematical Quality Validation
    ↓
Semantic Automotive Verification
    ↓
Super Zoom Detection
    ↓
FAIR Decision Engine
    ↓
PASS / REJECT
```

---

# Mathematical Foundation

## Blur Detection

```math
\mathcal{L}(I)
=
\frac{1}{N}
\sum_{i=1}^{N}
(\nabla^2 I_i - \mu)^2
```

## Global FAIR Decision

```math
FAIR(I)
=
Q(I)
\land
S(I)
\land
Z(I)
```

---

# Mock API Deployment

## Build Docker

```bash
docker build -t fair-api .
```

## Run Container

```bash
docker run -p 8000:8000 fair-api
```

---

# API Endpoint

## POST

```http
POST /fair/analyze
```

---

# Example Usage

```bash
python test_fair_api.py
```

---

# Example PASS Response

```json
{
  "FAIR_STATUS": "PASS",
  "IMAGE_TAG": "FrontRightCorner+zoom-out",
  "QUALITY_DECISION": "PASS"
}
```

---

# Example REJECT Response

```json
{
  "FAIR_STATUS": "REJECT",
  "REASONS_SHORT": [
    "NOT_CAR_IMAGE"
  ]
}
```

---

# Citation

```bibtex
@article{panboonyuen2026fair,
  title={FAIR: Filter And Image Removal},
  author={Panboonyuen, Teerapong},
  year={2026},
  institution={MARSAIL -- Motor AI Recognition Solution AI Laboratory}
}
```

---

# Philosophy

FAIR is not merely a model.

FAIR is infrastructure.

The system establishes reliable visual evidence governance for AI underwriting ecosystems requiring explainability, robustness, and production-grade reliability.

---

# License

Private Research Infrastructure License  
MARSAIL Laboratory © 2026