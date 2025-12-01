#!/usr/bin/env python3
"""
Screenshot Obfuscation Script
Redacts sensitive information from workshop screenshots
"""

from PIL import Image, ImageDraw, ImageFilter
import os

SCREENSHOTS_DIR = os.path.join(os.path.dirname(__file__), '..', 'screenshots')

# Redaction color (dark gray bar)
REDACT_COLOR = (40, 40, 40)
# Alternative: blur instead of solid color
USE_BLUR = False
BLUR_RADIUS = 30

def redact_area(img, box, use_blur=USE_BLUR):
    """Redact an area of the image with a solid color or blur"""
    draw = ImageDraw.Draw(img)
    x1, y1, x2, y2 = box
    
    if use_blur:
        # Crop, blur, and paste back
        region = img.crop(box)
        blurred = region.filter(ImageFilter.GaussianBlur(BLUR_RADIUS))
        img.paste(blurred, box)
    else:
        # Draw solid rectangle
        draw.rectangle(box, fill=REDACT_COLOR)
    
    return img

def add_placeholder_text(img, box, text="[REDACTED]"):
    """Add placeholder text over redacted area"""
    draw = ImageDraw.Draw(img)
    x1, y1, x2, y2 = box
    # Center text in box
    text_x = x1 + (x2 - x1) // 2 - len(text) * 3
    text_y = y1 + (y2 - y1) // 2 - 6
    draw.text((text_x, text_y), text, fill=(150, 150, 150))
    return img

def process_screenshot(filename, redactions):
    """Process a single screenshot with multiple redactions"""
    filepath = os.path.join(SCREENSHOTS_DIR, filename)
    
    if not os.path.exists(filepath):
        print(f"  ⚠️  File not found: {filename}")
        return False
    
    try:
        img = Image.open(filepath)
        original_size = img.size
        print(f"  📐 Size: {original_size[0]}x{original_size[1]}")
        
        for redaction in redactions:
            box = redaction['box']
            label = redaction.get('label', 'sensitive data')
            placeholder = redaction.get('placeholder', '[REDACTED]')
            
            # Validate box coordinates
            if box[2] > original_size[0] or box[3] > original_size[1]:
                print(f"  ⚠️  Box {box} exceeds image size, adjusting...")
                box = (
                    min(box[0], original_size[0]),
                    min(box[1], original_size[1]),
                    min(box[2], original_size[0]),
                    min(box[3], original_size[1])
                )
            
            img = redact_area(img, box)
            img = add_placeholder_text(img, box, placeholder)
            print(f"  ✓ Redacted: {label}")
        
        # Save the modified image
        img.save(filepath)
        print(f"  💾 Saved: {filename}")
        return True
        
    except Exception as e:
        print(f"  ❌ Error processing {filename}: {e}")
        return False

# Define redactions for each screenshot
# Box format: (x1, y1, x2, y2) - top-left to bottom-right
# Images are ~3000x1700 resolution
REDACTIONS = {
    # Screenshot 07: OpenAI Save your key modal - API key visible (3014x1698)
    "07_openai_save_api_key_modal.png": [
        {
            "box": (1080, 820, 1720, 880),  # API key in modal (highlighted green)
            "label": "OpenAI API Key",
            "placeholder": "sk-proj-YOUR_API_KEY_HERE"
        },
        {
            "box": (2200, 560, 2340, 600),  # "Bizee Bee" username in table
            "label": "Username (Bizee Bee)",
            "placeholder": "[USER]"
        }
    ],
    
    # Screenshot 08: OpenAI API keys list (3022x1710)
    "08_openai_api_keys_list.png": [
        {
            "box": (1240, 560, 1410, 600),  # Partial API key "sk-...aqEA"
            "label": "Partial API Key",
            "placeholder": "sk-...****"
        },
        {
            "box": (2200, 560, 2340, 600),  # "Bizee Bee" username
            "label": "Username",
            "placeholder": "[USER]"
        }
    ],
    
    # Screenshot 10: n8n Overview - username at bottom left (3024x1650)
    "10_n8n_overview_workflows_list.png": [
        {
            "box": (30, 1560, 230, 1610),  # "Deion Locklear" username
            "label": "Username",
            "placeholder": "[USER]"
        }
    ],
    
    # Screenshot 12: n8n Google Drive OAuth form (similar size)
    "12_n8n_google_drive_oauth2_connection_form.png": [
        {
            "box": (30, 1560, 230, 1610),  # "Deion Locklear" username
            "label": "Username",
            "placeholder": "[USER]"
        }
    ],
    
    # Screenshot 14: n8n OpenAI credential form
    "14_n8n_openai_credential_connection_form.png": [
        {
            "box": (30, 1560, 230, 1610),  # "Deion Locklear" username
            "label": "Username",
            "placeholder": "[USER]"
        }
    ],
    
    # Screenshot 16: n8n Header Auth form
    "16_n8n_header_auth_credential_connection_form.png": [
        {
            "box": (30, 1560, 230, 1610),  # "Deion Locklear" username
            "label": "Username",
            "placeholder": "[USER]"
        }
    ],
    
    # Screenshot 20: Google AI Studio API Keys (3024x1630)
    "20_google_ai_studio_api_keys_list.png": [
        {
            "box": (600, 460, 870, 500),  # Partial API key "...63WE"
            "label": "Gemini API Key",
            "placeholder": "...****"
        },
        {
            "box": (1080, 500, 1410, 540),  # Project ID "gen-lang-client-0868045849"
            "label": "Project ID",
            "placeholder": "gen-lang-client-XXXXXXXXXX"
        }
    ],
    
    # Screenshot 21: GCP Console Welcome (2916x1566)
    "21_n8n_screen_01.png": [
        {
            "box": (660, 595, 870, 635),  # Project number "685701800314"
            "label": "Project Number",
            "placeholder": "XXXXXXXXXXXX"
        },
        {
            "box": (1115, 595, 1480, 635),  # Project ID "gen-lang-client-0679080284"
            "label": "Project ID",
            "placeholder": "gen-lang-client-XXXXXXXXXX"
        }
    ],
    
    # Screenshot 27: GCP OAuth client created modal (2992x1624)
    "27_n8n_screen_07.png": [
        {
            "box": (1430, 540, 1930, 660),  # Client ID (multi-line)
            "label": "OAuth Client ID",
            "placeholder": "YOUR_CLIENT_ID_HERE"
        },
        {
            "box": (1430, 980, 1930, 1060),  # Client Secret
            "label": "OAuth Client Secret",
            "placeholder": "YOUR_CLIENT_SECRET_HERE"
        }
    ],
    
    # Screenshot 30: GCP Client ID details (3010x1636)
    "30_n8n_screen_10.png": [
        {
            "box": (560, 100, 1720, 145),  # Client ID in breadcrumb
            "label": "Client ID (breadcrumb)",
            "placeholder": "[CLIENT_ID_REDACTED]"
        },
        {
            "box": (2190, 350, 2880, 460),  # Client ID in panel (multi-line)
            "label": "Client ID (panel)",
            "placeholder": "YOUR_CLIENT_ID_HERE"
        },
        {
            "box": (2190, 1380, 2350, 1420),  # Partial client secret "****Aztt"
            "label": "Client Secret",
            "placeholder": "****"
        }
    ],
    
    # Screenshot 31: Google AI Studio create new API key
    "31_google_ai_studio_create_new_api_key.png": [
        {
            "box": (570, 460, 870, 500),  # Partial API key in background
            "label": "Background API Key",
            "placeholder": "...****"
        },
        {
            "box": (1060, 500, 1410, 540),  # Project ID in background
            "label": "Background Project ID",
            "placeholder": "gen-lang-client-XXXXXXXXXX"
        }
    ],
}

def main():
    print("🔐 Screenshot Obfuscation Script")
    print("=" * 50)
    print(f"📁 Screenshots directory: {SCREENSHOTS_DIR}")
    print()
    
    success_count = 0
    total_count = len(REDACTIONS)
    
    for filename, redactions in REDACTIONS.items():
        print(f"\n📸 Processing: {filename}")
        if process_screenshot(filename, redactions):
            success_count += 1
    
    print("\n" + "=" * 50)
    print(f"✅ Completed: {success_count}/{total_count} screenshots processed")
    
    if success_count < total_count:
        print("⚠️  Some screenshots could not be processed. Check the output above.")

if __name__ == "__main__":
    main()

