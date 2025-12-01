# 🎬 AI UGC Content Creation LiveLab

> A comprehensive hands-on workshop for building AI-powered content creation workflows.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Module 1: OpenAI Setup](#module-1-openai-setup)
4. [Module 2: Google Cloud Platform OAuth Configuration](#module-2-google-cloud-platform-oauth-configuration)
5. [Module 3: Google AI Studio Setup](#module-3-google-ai-studio-setup)
6. [Module 4: n8n Workflow Platform](#module-4-n8n-workflow-platform)
7. [Module 5: Building the UGC Workflow](#module-5-building-the-ugc-workflow)
8. [Module 6: Testing & Deployment](#module-6-testing--deployment)
9. [Troubleshooting Appendix](#troubleshooting-appendix)

---

## Introduction

Welcome to the **AI UGC Content Creation LiveLab**! This workshop will guide you through building a complete automated content creation pipeline using:

- 🤖 **OpenAI** - For AI-powered text and image generation
- ☁️ **Google Cloud Platform** - For OAuth authentication
- 🧠 **Google AI Studio** - For additional AI capabilities
- 🔄 **n8n** - For workflow automation
- 📁 **Google Drive** - For content storage and organization

By the end of this workshop, you'll have a fully functional system that can automatically generate, process, and organize AI-created content.

---

## Prerequisites

Before starting this workshop, ensure you have:

### Accounts Required
- [ ] Google Account (Gmail)
- [ ] OpenAI Account
- [ ] n8n Account (cloud or self-hosted instance)

### Technical Requirements
- [ ] Modern web browser (Chrome, Firefox, Edge)
- [ ] Stable internet connection
- [ ] Basic understanding of APIs

### Time Estimate
- **Total Workshop Duration:** 2-3 hours
- **Recommended Breaks:** Every 45 minutes

---

## Module 1: OpenAI Setup

### 1.1 Creating Your OpenAI Account

1. Navigate to [platform.openai.com](https://platform.openai.com)

   ![OpenAI Login Page](../screenshots/02_openai_login_page.png)

2. Click **Sign Up** or **Log In** if you already have an account

3. Complete the registration process

### 1.2 Exploring the Platform

Once logged in, you'll see the OpenAI Platform dashboard.

![OpenAI Platform Models Overview](../screenshots/03_openai_platform_models_overview.png)

Take a moment to explore:
- **Models** - Available AI models
- **Usage** - API usage statistics
- **Billing** - Payment and credits

### 1.3 Understanding Billing

![OpenAI Billing Overview](../screenshots/04_openai_billing_overview_free_trial.png)

OpenAI provides:
- Free trial credits for new accounts
- Pay-as-you-go pricing
- Usage limits and caps

### 1.4 Creating Your API Key

This is a critical step - your API key is how your applications authenticate with OpenAI.

1. Return to the dashboard

   ![OpenAI Platform Dashboard](../screenshots/05_openai_platform_dashboard_return.png)

2. Navigate to **API Keys** section

3. Click **Create new secret key**

   ![OpenAI Create API Key](../screenshots/06_openai_quickstart_create_api_key.png)

4. **IMPORTANT:** Save your API key immediately!

   ![OpenAI Save API Key Modal](../screenshots/07_openai_save_api_key_modal.png)

   ⚠️ **Warning:** You will only see this key once. Copy it to a secure location.

5. Your key will appear in the API Keys list

   ![OpenAI API Keys List](../screenshots/08_openai_api_keys_list.png)

### 1.5 Setting Up Billing

To use the API beyond free credits:

1. Go to **Billing** settings

   ![OpenAI Billing Add Payment](../screenshots/09_openai_billing_add_payment_details.png)

2. Add your payment method
3. Set up usage limits (recommended)

---

## Module 2: Google Cloud Platform OAuth Configuration

### 2.1 Creating OAuth Credentials

For Google Drive integration, you'll need OAuth 2.0 credentials.

1. Go to [Google Cloud Console](https://console.cloud.google.com)
2. Create a new project or select an existing one
3. Navigate to **APIs & Services** > **Credentials**
4. Click **Create Credentials** > **OAuth client ID**
5. Select **Web application**

   ![GCP OAuth Client Web App](../screenshots/01_gcp_oauth_client_web_app.png)

### 2.2 Configuring OAuth Consent Screen

Before creating OAuth credentials, configure the consent screen:

1. Go to **OAuth consent screen**
2. Select **External** user type
3. Fill in required fields:
   - App name
   - User support email
   - Developer contact information
4. Add scopes for Google Drive

### 2.3 Setting Authorized Redirect URIs

For n8n integration, add the callback URL:

```
https://your-n8n-instance.com/rest/oauth2-credential/callback
```

Replace `your-n8n-instance.com` with your actual n8n URL.

---

## Module 3: Google AI Studio Setup

### 3.1 Accessing Google AI Studio

1. Navigate to [Google AI Studio](https://aistudio.google.com)

   ![Google AI Studio Landing Page](../screenshots/17_google_ai_studio_landing_page.png)

2. Sign in with your Google account

3. Accept the welcome modal

   ![Google AI Studio Welcome Modal](../screenshots/18_google_ai_studio_welcome_modal.png)

### 3.2 Dashboard Overview

![Google AI Studio Home Dashboard](../screenshots/19_google_ai_studio_home_dashboard.png)

The dashboard provides access to:
- Model playground
- API key management
- Project settings

### 3.3 Creating an API Key

1. Navigate to **API Keys**

   ![Google AI Studio API Keys List](../screenshots/20_google_ai_studio_api_keys_list.png)

2. Click **Create API Key**

   ![Google AI Studio Create New API Key](../screenshots/31_google_ai_studio_create_new_api_key.png)

3. Select or create a project

### 3.4 GCP Billing Setup (If Required)

If your project requires billing:

1. You may see a billing requirement message

   ![GCP Project Has No Billing Account](../screenshots/32_gcp_project_has_no_billing_account.png)

2. Set up a billing account

   ![GCP Set Billing Account](../screenshots/33_gcp_set_billing_account_for_project.png)

3. View existing billing accounts

   ![GCP Billing Account Management](../screenshots/34_gcp_billing_account_management_list.png)

4. Create a new billing account if needed

   ![GCP Create New Billing Account](../screenshots/35_gcp_create_new_billing_account_form.png)

5. Confirm your billing setup with free trial credit

   ![GCP Billing Overview with Free Trial](../screenshots/36_gcp_billing_overview_with_free_trial_credit.png)

---

## Module 4: n8n Workflow Platform

### 4.1 Accessing n8n

1. Log into your n8n instance
2. View your workflows

   ![n8n Overview Workflows List](../screenshots/10_n8n_overview_workflows_list.png)

### 4.2 Setting Up Google Drive Credentials

1. Go to **Credentials** in n8n
2. Click **Add Credential**
3. Search for **Google Drive**

   ![n8n Add Credential Google Drive Search](../screenshots/11_n8n_add_credential_google_drive_search.png)

4. Configure OAuth2 connection

   ![n8n Google Drive OAuth2 Connection Form](../screenshots/12_n8n_google_drive_oauth2_connection_form.png)

5. Enter your credentials:
   - Client ID: `YOUR_CLIENT_ID_HERE`
   - Client Secret: `YOUR_CLIENT_SECRET_HERE`

### 4.3 Setting Up OpenAI Credentials

1. Add a new credential
2. Search for **OpenAI**

   ![n8n Add Credential OpenAI Search](../screenshots/13_n8n_add_credential_openai_search.png)

3. Configure the connection

   ![n8n OpenAI Credential Connection Form](../screenshots/14_n8n_openai_credential_connection_form.png)

4. Enter your API key: `YOUR_API_KEY_HERE`

### 4.4 Setting Up Header Auth Credentials

For custom API integrations:

1. Search for **Header Auth**

   ![n8n Add Credential Header Auth Search](../screenshots/15_n8n_add_credential_header_auth_search.png)

2. Configure the header authentication

   ![n8n Header Auth Credential Connection Form](../screenshots/16_n8n_header_auth_credential_connection_form.png)

---

## Module 5: Building the UGC Workflow

### 5.1 Workflow Overview

The UGC workflow consists of several interconnected nodes:

1. **Trigger** - Initiates the workflow
2. **AI Text Generation** - Creates content using OpenAI
3. **AI Image Generation** - Creates visuals
4. **Google Drive Upload** - Stores the content
5. **Notification** - Confirms completion

### 5.2 Step-by-Step Workflow Building

![n8n Workflow Building Step 1](../screenshots/21_n8n_screen_01.png)

![n8n Workflow Building Step 2](../screenshots/22_n8n_screen_02.png)

![n8n Workflow Building Step 3](../screenshots/23_n8n_screen_03.png)

![n8n Workflow Building Step 4](../screenshots/24_n8n_screen_04.png)

![n8n Workflow Building Step 5](../screenshots/25_n8n_screen_05.png)

![n8n Workflow Building Step 6](../screenshots/26_n8n_screen_06.png)

![n8n Workflow Building Step 7](../screenshots/27_n8n_screen_07.png)

![n8n Workflow Building Step 8](../screenshots/28_n8n_screen_08.png)

![n8n Workflow Building Step 9](../screenshots/29_n8n_screen_09.png)

![n8n Workflow Building Step 10](../screenshots/30_n8n_screen_10.png)

### 5.3 Workflow Configuration

```json
{
  "name": "UGC Content Creator",
  "nodes": [
    {
      "name": "Trigger",
      "type": "n8n-nodes-base.manualTrigger"
    },
    {
      "name": "OpenAI",
      "type": "n8n-nodes-base.openAi",
      "credentials": {
        "openAiApi": "YOUR_API_KEY_HERE"
      }
    },
    {
      "name": "Google Drive",
      "type": "n8n-nodes-base.googleDrive",
      "credentials": {
        "googleDriveOAuth2Api": "YOUR_CLIENT_ID_HERE"
      }
    }
  ]
}
```

---

## Module 6: Testing & Deployment

### 6.1 Testing Your Workflow

1. Click **Execute Workflow** in n8n
2. Monitor the execution
3. Check for errors in each node
4. Verify content in Google Drive

### 6.2 Deployment Checklist

- [ ] All credentials are valid and connected
- [ ] API keys are not expired
- [ ] Billing is set up for all services
- [ ] Error handling is configured
- [ ] Notifications are working

### 6.3 Production Considerations

- Set up monitoring and alerts
- Configure retry logic for failed API calls
- Implement rate limiting
- Back up your workflow regularly

---

## Troubleshooting Appendix

### Common Issues and Solutions

#### Issue 1: OpenAI API Key Not Working

**Symptoms:**
- 401 Unauthorized error
- "Invalid API key" message

**Solutions:**
1. Verify the API key is copied correctly (no extra spaces)
2. Check if the key has been revoked
3. Ensure billing is set up on your OpenAI account
4. Create a new API key if necessary

#### Issue 2: Google OAuth Connection Failed

**Symptoms:**
- "Access denied" error
- Redirect loop

**Solutions:**
1. Verify OAuth consent screen is configured
2. Check redirect URIs match exactly
3. Ensure required scopes are added
4. Try re-authenticating

#### Issue 3: n8n Credential Connection Failed

**Symptoms:**
- "Could not connect" error
- Timeout errors

**Solutions:**
1. Verify credentials are entered correctly
2. Check for typos in Client ID/Secret
3. Ensure the API is enabled in GCP
4. Check n8n instance can reach external APIs

#### Issue 4: Google Drive Upload Failed

**Symptoms:**
- "Insufficient permissions" error
- "File not found" error

**Solutions:**
1. Re-authenticate Google Drive credentials
2. Check folder permissions
3. Verify the target folder exists
4. Ensure Drive API is enabled

#### Issue 5: Rate Limiting Errors

**Symptoms:**
- 429 Too Many Requests
- "Rate limit exceeded" message

**Solutions:**
1. Add delays between API calls
2. Implement exponential backoff
3. Upgrade to higher API tier
4. Distribute requests over time

#### Issue 6: GCP Billing Not Set Up

**Symptoms:**
- "Billing account required" message
- API calls blocked

**Solutions:**
1. Go to GCP Console > Billing
2. Create or link a billing account
3. Enable billing for your project
4. Wait a few minutes for propagation

#### Issue 7: Workflow Not Triggering

**Symptoms:**
- Workflow doesn't start
- No execution history

**Solutions:**
1. Check trigger configuration
2. Verify workflow is active
3. Test with manual trigger first
4. Check for disabled nodes

#### Issue 8: Image Generation Failed

**Symptoms:**
- Empty image response
- "Content policy violation" error

**Solutions:**
1. Review prompt for policy violations
2. Try a different prompt
3. Check image generation credits
4. Verify API endpoint is correct

### Error Code Reference

| Code | Meaning | Action |
|------|---------|--------|
| 401 | Unauthorized | Check API key |
| 403 | Forbidden | Check permissions |
| 404 | Not Found | Verify endpoint URL |
| 429 | Rate Limited | Add delays |
| 500 | Server Error | Retry later |
| 503 | Service Unavailable | Check service status |

### Getting Additional Help

If you're still experiencing issues:

1. Check the [FAQs](../docs/faqs.md)
2. Review the [Installation Guide](../docs/install_guide.md)
3. Open an issue in the repository
4. Consult the official documentation:
   - [OpenAI Docs](https://platform.openai.com/docs)
   - [n8n Docs](https://docs.n8n.io)
   - [Google Cloud Docs](https://cloud.google.com/docs)

---

## Conclusion

Congratulations! 🎉 You've completed the AI UGC Content Creation LiveLab.

You now have:
- ✅ OpenAI API integration
- ✅ Google Cloud OAuth configuration
- ✅ Google AI Studio access
- ✅ A working n8n workflow
- ✅ Automated content creation pipeline

### Next Steps

1. Customize the workflow for your use case
2. Add more AI models and capabilities
3. Set up scheduled triggers
4. Build a content library in Google Drive
5. Share your creations!

---

<p align="center">
  <strong>Happy Creating! 🚀</strong>
</p>

