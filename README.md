# 🎬 AI UGC Content Creation Template

> A complete workshop template for building AI-powered User-Generated Content (UGC) creation workflows using n8n, OpenAI, Google AI Studio, and Google Drive.

![Banner](assets/banner.png)

---

## 📖 Overview

This repository provides a **step-by-step LiveLab workshop** that teaches you how to build an automated AI content creation pipeline. By the end of the workshop, you'll have a fully functional n8n workflow that can:

- 🤖 Generate AI-powered content using OpenAI GPT models
- 🎨 Create images with AI image generation APIs
- 📁 Automatically organize and store content in Google Drive
- 🔄 Automate the entire UGC content creation process
- 🔐 Securely manage API credentials and authentication

---

## 🚀 Getting Started

### Prerequisites

Before starting the workshop, ensure you have:

- [ ] A Google account (for Google Drive & Google AI Studio)
- [ ] An OpenAI account (for GPT API access)
- [ ] An n8n instance (cloud or self-hosted)
- [ ] Basic understanding of APIs and automation workflows

### Quick Start

1. **Clone this repository:**
   ```bash
   git clone https://github.com/yourusername/ai-ugc-content-creation-template.git
   cd ai-ugc-content-creation-template
   ```

2. **Read the workshop:**
   Open [`workshops/live_lab.md`](workshops/live_lab.md) and follow along step-by-step.

3. **Obtain the workflow:**
   The UGC Content Creation workflow is available as a premium digital asset. Purchase access to receive the complete workflow package, which includes:
   - The n8n workflow JSON file
   - Setup instructions
   - Link to this workshop repository

4. **Import and configure:**
   Once you have the workflow, import it into your n8n instance and update the credentials as described in Module 5 of the workshop.

---

## 📁 Repository Structure

```
ai-ugc-content-creation-template/
│
├── README.md                          # You are here!
│
├── workshops/
│   └── live_lab.md                    # Complete step-by-step workshop guide
│
├── exports/
│   └── live_lab_export.json           # LiveLab template export (JSON)
│
├── workflow/
│   └── ugc_workflow.json              # Placeholder - workflow available as premium asset
│
├── screenshots/
│   ├── 01_gcp_oauth_client_web_app.png
│   ├── 02_openai_login_page.png
│   ├── ... (36 total screenshots)
│   └── 36_gcp_billing_overview_with_free_trial_credit.png
│
├── assets/
│   ├── logo.png                       # Project logo
│   ├── banner.png                     # README banner
│   └── diagram.png                    # Architecture diagram
│
├── docs/
│   ├── install_guide.md               # Detailed installation guide
│   ├── troubleshooting.md             # Common issues and solutions
│   └── faqs.md                        # Frequently asked questions
│
└── LICENSE                            # MIT License
```

---

## 📚 Documentation

| Document | Description |
|----------|-------------|
| [Live Lab Workshop](workshops/live_lab.md) | The main hands-on workshop guide |
| [Installation Guide](docs/install_guide.md) | Detailed setup instructions |
| [Troubleshooting](docs/troubleshooting.md) | Solutions to common issues |
| [FAQs](docs/faqs.md) | Frequently asked questions |

---

## 💰 Workflow Availability

The complete **"Automate UGC Content Creation with N8N and Sora 2"** workflow is available as a premium digital asset. The workflow package includes:

- ✅ Complete n8n workflow JSON file
- ✅ Setup and configuration guide  
- ✅ Link to this workshop repository

> **Note:** This public repository contains the **free workshop guide** that teaches you how to set up all the credentials and configure the workflow. The actual workflow file must be purchased separately.

---

## 🛠️ What You'll Build

This workshop guides you through creating an **end-to-end AI content creation pipeline** that includes:

### 1. **API Setup & Configuration**
- OpenAI API key creation and billing setup
- Google AI Studio API integration
- Google Cloud Platform OAuth configuration

### 2. **n8n Workflow Development**
- Creating automated workflows
- Setting up credential connections
- Building trigger-based automation

### 3. **Google Drive Integration**
- OAuth2 authentication
- Automated file management
- Content organization

### 4. **AI Content Generation**
- GPT-powered text generation
- Image creation and processing
- Content templating

---

## 🔐 Security Notes

⚠️ **Important Security Reminders:**

- Never commit real API keys to version control
- Use environment variables for sensitive credentials
- Replace all `YOUR_API_KEY_HERE` placeholders before use
- Rotate API keys regularly
- Review OAuth scopes for minimum required permissions

---

## 📸 Screenshots

The `screenshots/` folder contains visual guides for each step of the workshop:

- **01-10:** OpenAI & GCP OAuth setup
- **11-20:** n8n credential configuration
- **21-30:** Workflow building steps
- **31-36:** Google AI Studio & GCP billing

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- [n8n](https://n8n.io/) - Workflow automation platform
- [OpenAI](https://openai.com/) - AI models and APIs
- [Google Cloud Platform](https://cloud.google.com/) - Cloud services and APIs
- [Google AI Studio](https://aistudio.google.com/) - AI development tools

---

## 📬 Support

If you encounter any issues or have questions:

1. Check the [Troubleshooting Guide](docs/troubleshooting.md)
2. Review the [FAQs](docs/faqs.md)
3. Open an issue in this repository

---

<p align="center">
  Made with ❤️ for the AI Content Creator Community
</p>

