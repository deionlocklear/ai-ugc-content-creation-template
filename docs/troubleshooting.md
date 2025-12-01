# Troubleshooting Guide

> Solutions to common issues encountered during the AI UGC Content Creation LiveLab.

---

## Table of Contents

1. [OpenAI Issues](#openai-issues)
2. [Google OAuth Issues](#google-oauth-issues)
3. [n8n Issues](#n8n-issues)
4. [Google Drive Issues](#google-drive-issues)
5. [API & Rate Limiting](#api--rate-limiting)
6. [GCP Billing Issues](#gcp-billing-issues)
7. [Workflow Issues](#workflow-issues)
8. [Image Generation Issues](#image-generation-issues)
9. [Error Code Reference](#error-code-reference)
10. [Getting Additional Help](#getting-additional-help)

---

## OpenAI Issues

### Issue: OpenAI API Key Not Working

**Symptoms:**
- 401 Unauthorized error
- "Invalid API key" message
- API calls returning authentication errors

**Solutions:**

1. **Verify the API key is copied correctly**
   - Check for extra spaces at the beginning or end
   - Ensure no characters were missed during copy/paste
   
2. **Check if the key has been revoked**
   - Go to [OpenAI API Keys](https://platform.openai.com/api-keys)
   - Verify your key is listed and active
   
3. **Ensure billing is set up**
   - Free trial credits may have expired
   - Go to Billing and add a payment method
   
4. **Create a new API key**
   - If all else fails, generate a fresh key
   - Remember to update all your integrations

---

## Google OAuth Issues

### Issue: Google OAuth Connection Failed

**Symptoms:**
- "Access denied" error
- Redirect loop during authentication
- "Error 400: redirect_uri_mismatch"

**Solutions:**

1. **Verify OAuth consent screen is configured**
   - Go to GCP Console > APIs & Services > OAuth consent screen
   - Ensure all required fields are filled
   - Add your email to test users if in testing mode
   
2. **Check redirect URIs match exactly**
   - The callback URL must match precisely
   - For n8n: `https://your-n8n-instance.com/rest/oauth2-credential/callback`
   - Check for trailing slashes
   
3. **Ensure required scopes are added**
   - Add Google Drive scopes
   - Add any other required API scopes
   
4. **Try re-authenticating**
   - Disconnect the credential in n8n
   - Clear browser cookies for Google
   - Re-authorize the connection

---

## n8n Issues

### Issue: n8n Credential Connection Failed

**Symptoms:**
- "Could not connect" error
- Timeout errors
- Credential test fails

**Solutions:**

1. **Verify credentials are entered correctly**
   - Double-check all field values
   - Ensure no hidden characters
   
2. **Check for typos**
   - Client ID and Secret are case-sensitive
   - API keys must be exact
   
3. **Ensure the API is enabled in GCP**
   - Go to GCP Console > APIs & Services > Library
   - Enable Google Drive API
   - Enable any other required APIs
   
4. **Check n8n instance connectivity**
   - Ensure n8n can reach external APIs
   - Check firewall settings
   - Verify SSL certificates

---

## Google Drive Issues

### Issue: Google Drive Upload Failed

**Symptoms:**
- "Insufficient permissions" error
- "File not found" error
- Upload hangs indefinitely

**Solutions:**

1. **Re-authenticate Google Drive credentials**
   - Delete existing credential
   - Create new credential with fresh OAuth
   
2. **Check folder permissions**
   - Ensure your Google account has write access
   - Verify the folder isn't read-only
   
3. **Verify the target folder exists**
   - Check the folder ID is correct
   - Ensure the folder hasn't been deleted
   
4. **Ensure Drive API is enabled**
   - Go to GCP Console > APIs & Services
   - Enable Google Drive API if not already

---

## API & Rate Limiting

### Issue: Rate Limiting Errors

**Symptoms:**
- 429 Too Many Requests
- "Rate limit exceeded" message
- Temporary blocks

**Solutions:**

1. **Add delays between API calls**
   - Use n8n's Wait node
   - Add 1-2 second delays between requests
   
2. **Implement exponential backoff**
   - Start with short delays
   - Increase delay on each retry
   
3. **Upgrade to higher API tier**
   - Contact API provider for higher limits
   - Consider enterprise plans
   
4. **Distribute requests over time**
   - Spread batch operations
   - Use scheduled workflows

---

## GCP Billing Issues

### Issue: GCP Billing Not Set Up

**Symptoms:**
- "Billing account required" message
- API calls blocked
- Services unavailable

**Solutions:**

1. **Navigate to GCP Billing**
   - Go to GCP Console > Billing
   - Click "Manage billing accounts"
   
2. **Create a billing account**
   - Click "Create account"
   - Enter payment information
   - Complete verification
   
3. **Link billing to your project**
   - Go to your project settings
   - Link the billing account
   
4. **Wait for propagation**
   - Billing changes can take a few minutes
   - Try again after 5-10 minutes

---

## Workflow Issues

### Issue: Workflow Not Triggering

**Symptoms:**
- Workflow doesn't start
- No execution history
- Trigger seems inactive

**Solutions:**

1. **Check trigger configuration**
   - Verify trigger node settings
   - Test webhook URLs if applicable
   
2. **Verify workflow is active**
   - Toggle the workflow on
   - Check the active status
   
3. **Test with manual trigger first**
   - Add a manual trigger node
   - Execute manually to test
   
4. **Check for disabled nodes**
   - Ensure no nodes are disabled
   - Look for error indicators

---

## Image Generation Issues

### Issue: Image Generation Failed

**Symptoms:**
- Empty image response
- "Content policy violation" error
- Timeout during generation

**Solutions:**

1. **Review prompt for policy violations**
   - Check OpenAI's content policy
   - Remove potentially problematic content
   
2. **Try a different prompt**
   - Simplify the prompt
   - Use more generic descriptions
   
3. **Check image generation credits**
   - Verify you have available credits
   - Check billing status
   
4. **Verify API endpoint is correct**
   - Use the correct DALL-E endpoint
   - Check API version

---

## Error Code Reference

| Code | Meaning | Action |
|------|---------|--------|
| 400 | Bad Request | Check request format and parameters |
| 401 | Unauthorized | Verify API key or credentials |
| 403 | Forbidden | Check permissions and access rights |
| 404 | Not Found | Verify endpoint URL and resource IDs |
| 429 | Rate Limited | Add delays and implement backoff |
| 500 | Server Error | Wait and retry later |
| 502 | Bad Gateway | Check service status, retry |
| 503 | Service Unavailable | Check service status page |
| 504 | Gateway Timeout | Increase timeout, retry |

---

## Getting Additional Help

If you're still experiencing issues after trying the solutions above:

### 1. Check Official Documentation

- **OpenAI:** [platform.openai.com/docs](https://platform.openai.com/docs)
- **n8n:** [docs.n8n.io](https://docs.n8n.io)
- **Google Cloud:** [cloud.google.com/docs](https://cloud.google.com/docs)
- **Google AI Studio:** [ai.google.dev/docs](https://ai.google.dev/docs)

### 2. Community Resources

- n8n Community Forum
- OpenAI Developer Forum
- Stack Overflow

### 3. Open an Issue

If you believe you've found a bug or have a feature request:

1. Check existing issues first
2. Provide detailed reproduction steps
3. Include error messages and logs
4. Specify your environment details

### 4. Contact Support

For urgent production issues, contact the respective platform support:

- OpenAI: [help.openai.com](https://help.openai.com)
- n8n: [n8n.io/contact](https://n8n.io/contact)
- Google Cloud: [cloud.google.com/support](https://cloud.google.com/support)

---

## Preventive Measures

To avoid common issues:

1. **Regularly rotate API keys** - Don't use the same key indefinitely
2. **Monitor usage** - Set up alerts for unusual activity
3. **Keep backups** - Export workflows regularly
4. **Test in staging** - Don't deploy untested changes to production
5. **Document changes** - Keep a log of modifications

---

<p align="center">
  <strong>Still stuck? Don't hesitate to ask for help!</strong>
</p>

