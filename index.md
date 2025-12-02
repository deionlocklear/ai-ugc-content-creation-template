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
- ☁️ **Google Cloud Platform** - For OAuth authentication and Google Drive API
- 🧠 **Google AI Studio** - For additional AI capabilities
- 🔄 **n8n** - For workflow automation
- 📁 **Google Drive** - For content storage and organization

### Workshop Structure

This workshop is divided into clear modules:

**Modules 1-4: Credential Setup** (Complete these first)
- **Module 1:** Get your OpenAI API key
- **Module 2:** Get Google Cloud OAuth Client ID & Secret, enable Google Drive API
- **Module 3:** Get your Google AI Studio API key
- **Module 4:** Add all credentials to n8n

**Module 5: Workflow Import** (After credentials are ready)
- Import the pre-built workflow into n8n
- Update workflow nodes to use your credentials

**Module 6: Testing & Deployment**
- Test your workflow
- Deploy to production

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


---

## Module 1: OpenAI Setup

**Goal:** Obtain your OpenAI API key for AI content generation.

**What you'll get:** OpenAI API key (starts with `sk-proj-...`)

---

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

**Goal:** Get OAuth Client ID and Secret for Google Drive integration, and enable the Google Drive API.

**What you'll get:** 
- OAuth Client ID
- OAuth Client Secret
- Google Drive API enabled

---

### 2.1 Creating OAuth Credentials

For Google Drive integration, you'll need OAuth 2.0 credentials.

1. Go to [Google Cloud Console](https://console.cloud.google.com)
2. Create a new project or select an existing one

   ![GCP Console Welcome](../screenshots/21_n8n_screen_01.png)

3. Navigate to **APIs & Services** > **Library** or search for "Google Auth Platform"

   ![GCP Search for Google Auth Platform](../screenshots/22_n8n_screen_02.png)

4. Click on **Google Auth Platform** from the search results
5. Navigate to **APIs & Services** > **Credentials** (or use the Google Auth Platform sidebar)
6. Click **Create Credentials** > **OAuth client ID**
7. Select **Web application**

   ![GCP OAuth Client Web App](../screenshots/01_gcp_oauth_client_web_app.png)

### 2.2 Configuring OAuth Consent Screen

Before creating OAuth credentials, you must configure the OAuth consent screen. If you haven't set this up yet, you'll see a message indicating it's not configured:

![GCP OAuth Overview Not Configured](../screenshots/23_n8n_screen_03.png)

1. Click **Get started** or navigate to **OAuth consent screen** from the Google Auth Platform sidebar
2. Select **External** user type (for most use cases)
3. Fill in the **App Information** step:
   - **App name** - Choose a name for your application
   - **User support email** - Your email address

   ![GCP OAuth Consent Screen App Information](../screenshots/24_n8n_screen_04.png)

4. Complete the remaining steps:
   - **Audience** - Select who can use your app
   - **Contact Information** - Add developer contact details
5. Add scopes for Google Drive (if not already added):
   - Look for scopes like `https://www.googleapis.com/auth/drive` or `https://www.googleapis.com/auth/drive.file`
6. Complete the consent screen setup

### 2.3 Enabling Google Drive API

Before you can use Google Drive with n8n, you must enable the Google Drive API in your GCP project:

1. In the Google Cloud Console, use the search bar at the top to search for **"Google Drive API"**

   ![GCP Search for Google Drive API](../screenshots/37_gcp_search_google_drive_api.png)

2. Click on **Google Drive API** from the search results (it will appear in the "Top results" or "Marketplace" section)

3. You'll be taken to the Google Drive API product details page. Click the blue **Enable** button to activate the API for your project

   ![GCP Google Drive API Product Details](../screenshots/38_gcp_google_drive_api_product_details.png)

4. After enabling, you'll be redirected to the API/Service Details page where you can verify the API is enabled

   ![GCP Google Drive API Enabled](../screenshots/39_gcp_google_drive_api_enabled.png)

   ✅ **Verification:** You should see **Status: Enabled** on this page, confirming the API is active for your project.

   ⚠️ **Note:** If you don't see the Enable button on the product details page, the API may already be enabled. You can verify this in the **APIs & Services** > **Enabled APIs** section.

### 2.4 Setting Authorized Redirect URIs

After creating your OAuth client, you'll see a confirmation modal with your Client ID and Client Secret:

![GCP OAuth Client Created](../screenshots/27_n8n_screen_07.png)

**Important:** Save your Client ID and Client Secret immediately! You'll need these in Module 4.

Now, configure the authorized redirect URIs:

1. Navigate to your OAuth client details page (you can access this from the **Clients** tab in Google Auth Platform)
2. Scroll to the **Authorized redirect URIs** section
3. Click **+ Add URI**
4. Add the callback URL for n8n:

   ![GCP OAuth Client Details with Redirect URIs](../screenshots/30_n8n_screen_10.png)

**For n8n Cloud users:** Use `https://oauth.n8n.cloud/oauth2/callback`

**For self-hosted n8n:** Use your n8n instance URL followed by `/rest/oauth2-credential/callback`

5. Click **Save** to apply the changes

> ⚠️ **Note:** It may take 5 minutes to a few hours for settings to take effect.

---

## Module 3: Google AI Studio Setup

**Goal:** Obtain your Google AI Studio API key for Gemini API access.

**What you'll get:** Google AI Studio API key

---

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

   ⚠️ **Important Note:** To move into Tier 1 (beyond free tier limits), you may need to add a credit card to your Google Cloud billing account. The free trial provides $300 in credits, but some services require a payment method on file to access Tier 1 quotas.

---

## Module 4: n8n Workflow Platform

**Goal:** Add all your credentials to n8n so the workflow can authenticate with external services.

**What you'll create:**
- Google Drive OAuth2 credential in n8n
- OpenAI API credential in n8n
- Header Auth credential for Google AI Studio in n8n

---

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

### 4.4 Setting Up Header Auth Credentials (For Google AI Studio)

For Google AI Studio API integration, you'll need to set up Header Auth credentials:

1. In n8n, go to **Credentials** and click **Add Credential**
2. Search for **Header Auth**

   ![n8n Add Credential Header Auth Search](../screenshots/15_n8n_add_credential_header_auth_search.png)

3. Configure the header authentication:
   - **Name:** `x-goog-api-key`
   - **Value:** Your Google AI Studio API key (from Module 3.3)

   ![n8n Header Auth Credential Connection Form](../screenshots/16_n8n_header_auth_credential_connection_form.png)

4. Click **Save** to store the credential

### 4.5 Credential Summary

By the end of Module 4, you should have created the following credentials in n8n:

- ✅ **Google Drive OAuth2** - Using Client ID and Client Secret from Module 2
- ✅ **OpenAI API** - Using API key from Module 1.4
- ✅ **Header Auth (x-goog-api-key)** - Using Google AI Studio API key from Module 3.3

Make sure all credentials are saved and test each one to ensure they're working correctly before proceeding to Module 5.

---

## Module 5: Importing and Configuring the UGC Workflow

Now that you have all your credentials set up in n8n, it's time to import the pre-built workflow and connect it to your credentials.

### 5.1 Understanding the Workflow

The **"Automate UGC Content Creation with N8N and Sora 2"** workflow automates the creation of User-Generated Content (UGC) videos. Here's what it does:

**Workflow Overview:**
1. **Form Trigger** - Collects a product image and product name from users
2. **Persona Generation** - Uses OpenAI to analyze the product and generate an ideal customer persona
3. **Script Generation** - Uses Google AI Studio (Gemini) to create 3 authentic UGC video scripts based on the persona
4. **Video Creation** - Generates 3 videos using OpenAI's Sora 2 model:
   - Creates a first frame image using Gemini
   - Generates 12-second videos with Sora 2
   - Polls for video completion
   - Downloads completed videos
5. **Storage** - Uploads all generated videos to Google Drive

**Key Components:**
- **Input:** Product image (file) + Product name (text)
- **AI Services Used:** OpenAI (GPT-4o, Sora 2), Google AI Studio (Gemini 2.5)
- **Output:** 3 UGC videos uploaded to Google Drive

### 5.2 Obtaining the Workflow

The UGC Content Creation workflow is available as a premium digital asset and is **not included** in this public repository.

**To obtain the workflow:**

1. Purchase access to the workflow through the designated platform
2. Download the workflow package (ZIP file)
3. Extract the contents, which include:
   - `ugc_workflow.json` - The complete n8n workflow file
   - `README.md` - Setup and usage instructions
   - `workshop_link.md` - Link to this GitHub workshop repository

4. Open `ugc_workflow.json` in a text editor
5. Copy the entire JSON contents (or use the file directly)

   > **Note:** The workflow file contains all nodes, connections, and configurations. You'll need to update the credentials after importing.

### 5.3 Importing the Workflow into n8n

1. Log into your n8n instance
2. Click **Workflows** in the left sidebar (or use the **Overview** page)

   ![n8n Overview Workflows List](../screenshots/10_n8n_overview_workflows_list.png)

3. Click the **Import** button (usually in the top right, or use the dropdown menu from the "Create Workflow" button)
4. Choose one of these options:
   - **Paste JSON:** Paste the workflow JSON directly
   - **Upload File:** Upload the `ugc_workflow.json` file
5. Click **Import** to add the workflow to n8n
6. The workflow will appear in your workflows list

### 5.4 Updating Workflow Nodes with Your Credentials

After importing, you need to update each node to use the credentials you created in Modules 1-4. The workflow contains several node types that require credential configuration:

#### 5.4.1 Update OpenAI Nodes

The workflow uses OpenAI for persona generation, script extraction, and Sora 2 video generation. Update these nodes:

**OpenAI LangChain Nodes:**
- **"Generate Ideal Persona"** - Analyzes product image and creates customer persona
- **"Extract Prompts"** - Extracts and formats video script prompts

**HTTP Request Nodes (OpenAI API):**
- **"Generate Video With SORA"** - Creates videos using Sora 2
- **"Get Video Creation Status"** - Checks video generation status
- **"Download Video"** - Downloads completed videos

**Steps to Update:**
1. Click on each OpenAI node in the workflow
2. In the node configuration panel, find the **Credential** dropdown
3. Select your **OpenAI credential** (created in Module 4.3)

   > 💡 **Reference:** The credential selection interface will look similar to the OpenAI credential form you saw in Module 4.3. The dropdown will show all your saved OpenAI credentials.

   ![n8n OpenAI Credential Connection Form](../screenshots/14_n8n_openai_credential_connection_form.png)

4. For HTTP Request nodes using OpenAI API, look for **Authentication** → **Predefined Credential Type** → **OpenAI API**
5. Repeat for all OpenAI-related nodes in the workflow

#### 5.4.2 Update Google Drive Nodes

The workflow uses Google Drive to store generated videos:

**Google Drive Node:**
- **"upload_video"** - Uploads completed videos to Google Drive

**Steps to Update:**
1. Click on the **"upload_video"** node in the workflow
2. In the node configuration panel, find the **Credential** dropdown
3. Select your **Google Drive OAuth2 credential** (created in Module 4.2)

   > 💡 **Reference:** The credential selection interface will look similar to the Google Drive credential form you saw in Module 4.2.

   ![n8n Google Drive OAuth2 Connection Form](../screenshots/12_n8n_google_drive_oauth2_connection_form.png)

4. Complete the OAuth flow if prompted (this authorizes n8n to access your Google Drive)
   - You may be redirected to Google to authorize access
   - Click **Allow** to grant permissions
5. **Optional:** Update the folder path in the node configuration if you want videos saved to a specific Google Drive folder

#### 5.4.3 Update Google AI Studio (Gemini) Nodes

The workflow uses Google AI Studio (Gemini) for script generation and first frame image creation:

**HTTP Request Nodes (Gemini API):**
- **"generate_ad_prompts"** - Generates 3 UGC video scripts using Gemini 2.5 Pro
- **"Generate First Frame Image"** - Creates first frame image using Gemini 2.5 Flash Image Preview

**Steps to Update:**
1. Click on each HTTP Request node that calls Gemini API (look for URLs containing `generativelanguage.googleapis.com`)
2. In the node configuration, find the **Authentication** section
3. Select **Generic Credential Type** → **HTTP Header Auth**
4. Choose your **Header Auth credential** with `x-goog-api-key` (created in Module 4.4)

   > 💡 **Reference:** The credential selection interface will look similar to the Header Auth credential form you saw in Module 4.4.

   ![n8n Header Auth Credential Connection Form](../screenshots/16_n8n_header_auth_credential_connection_form.png)

5. Verify the header name is set to `x-goog-api-key` in the node configuration
6. Repeat for both Gemini API nodes:
   - `generate_ad_prompts` (Gemini 2.5 Pro)
   - `Generate First Frame Image` (Gemini 2.5 Flash Image Preview)

### 5.5 Verifying Node Connections

After updating all credentials, verify the workflow is properly configured:

1. **Check Credentials:**
   - ✅ All OpenAI nodes have your OpenAI credential selected
   - ✅ Google Drive node has your Google Drive OAuth2 credential selected
   - ✅ Both Gemini HTTP Request nodes have your Header Auth credential selected

2. **Verify Node Connections:**
   - ✅ Node connections (the lines between nodes) are intact
   - ✅ No red error indicators are present on any nodes
   - ✅ All required parameters are filled in

3. **Key Nodes to Verify:**
   - **Form Trigger** - Should be active and ready to receive submissions
   - **OpenAI Nodes** - Verify model selection (GPT-4o, GPT-5-mini, Sora 2)
   - **Gemini HTTP Request Nodes** - Check URLs point to correct Gemini endpoints
   - **Google Drive Node** - Confirm folder path is set (or will use default)
   - **Video Generation Nodes** - Ensure Sora 2 API endpoints are correct

4. **Optional Configuration:**
   - Update the Google Drive folder path in the `upload_video` node if you want videos saved to a specific location
   - Review the form trigger settings if you want to customize the input fields
   - Check video generation parameters (duration, size) if you want to modify defaults

### 5.6 Workflow Execution Flow

Understanding the workflow execution will help you troubleshoot if needed:

**Execution Flow:**
1. **Form Submission** → User submits product image + name via form trigger
2. **Image Processing** → Product image converted to base64 format
3. **Persona Generation** → OpenAI analyzes product and generates ideal customer persona
4. **Script Generation** → Gemini creates 3 authentic UGC video scripts
5. **Script Extraction** → OpenAI formats scripts into structured prompts
6. **Video Loop** (runs 3 times, once per script):
   - **First Frame** → Gemini generates first frame image
   - **Resize** → Image resized to video format (720x1280)
   - **Video Generation** → Sora 2 creates 12-second video
   - **Status Check** → Polls for video completion (with 15-second delays)
   - **Download** → Downloads completed video
   - **Upload** → Saves video to Google Drive

**Expected Output:**
- 3 UGC videos (12 seconds each, 720x1280 resolution)
- Videos saved to Google Drive with names like "UGC Video #1", "UGC Video #2", "UGC Video #3"

> 💡 **Tip:** The workflow includes retry logic and error handling. If a video generation fails, the workflow will retry automatically. Check the execution logs in n8n if you encounter issues.

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