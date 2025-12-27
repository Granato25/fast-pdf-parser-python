# ⚡ Ultra-Fast PDF to JSON Parser (with Bounding Boxes)

A minimal Python client for the  
👉 **[Ultra-Fast PDF to JSON API](https://rapidapi.com/nathanffm/api/ultra-fast-pdf-to-json-bounding-boxes)**

> Extracts text and exact bounding boxes from PDFs in milliseconds using Rust + PDFium.

## Why this exists

Most PDF tools are either:
- **slow** (Python-only libraries)
- **expensive** (per-page billing)
- **unpredictable** for large documents


## Why not PyMuPDF / pdfplumber / tika?

- **Maintenance**: Local libraries often break on malformed PDFs or require complex system dependencies (like Java/Tika).
- **Speed**: Pure Python implementations can be slow for large batch processing.
- **Complexity**: Extracting layout-perfect bounding boxes usually requires writing complex heuristics.

This client delegates the heavy lifting to a hosted Rust engine (requires an API key).

## Features

- ⚡ **Very fast**: Typical processing time ~10–20ms per document
- 🎯 **Layout-aware**: Exact X/Y coordinates for every text span
- 💰 **Flat pricing**: No per-page billing
- 🔒 **Privacy-first**: Files are processed in memory and discarded immediately

## Usage

```python
from client import parse_pdf

result = parse_pdf("invoice.pdf", api_key="YOUR_RAPIDAPI_KEY")
print(result)
```

## Input requirements

- Works with digital (text-based) PDFs
- **OCR is not supported** by design (for speed & determinism)

## Get an API Key

👉 **Free tier available on RapidAPI:**  
[https://rapidapi.com/nathanffm/api/ultra-fast-pdf-to-json-bounding-boxes](https://rapidapi.com/nathanffm/api/ultra-fast-pdf-to-json-bounding-boxes)
