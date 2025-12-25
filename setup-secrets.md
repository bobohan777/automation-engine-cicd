# GitHub Secrets Setup Guide

This guide explains how to set up the required GitHub secrets for the CI/CD pipeline.

## Required Secrets

### 1. Docker Hub Credentials

#### DOCKER_USERNAME
- **Value:** Your Docker Hub username
- **Example:** `your-dockerhub-username`

#### DOCKER_PASSWORD
- **Value:** Docker Hub access token (not password)
- **How to create:**
  1. Login to Docker Hub
  2. Go to Account Settings → Security
  3. Click "New Access Token"
  4. Name: `github-actions-automation-engine`
  5. Permissions: Read, Write, Delete
  6. Copy the generated token

## Setting Up Secrets

### Step 1: Navigate to Repository Settings
```
1. Go to your GitHub repository
2. Click "Settings" tab
3. In left sidebar, click "Secrets and variables"
4. Click "Actions"
```

### Step 2: Add Repository Secrets
```
1. Click "New repository secret"
2. Name: DOCKER_USERNAME
3. Secret: your-dockerhub-username
4. Click "Add secret"

5. Click "New repository secret" again
6. Name: DOCKER_PASSWORD
7. Secret: your-docker-hub-access-token
8. Click "Add secret"
```

### Step 3: Verify Secrets
```
After adding secrets, you should see:
✅ DOCKER_USERNAME
✅ DOCKER_PASSWORD
```

## Security Best Practices

### Access Token Permissions
- **Minimum required:** Read, Write
- **Recommended:** Read, Write, Delete (for cleanup)
- **Never use:** Full account access

### Token Rotation
- Rotate tokens every 90 days
- Update GitHub secrets when rotating
- Monitor token usage in Docker Hub

### Repository Access
- Limit repository access to necessary collaborators
- Use branch protection rules
- Require PR reviews for main branch

## Troubleshooting

### Common Issues

#### "Invalid credentials" error
```bash
# Check if secrets are set correctly
# Verify Docker Hub token has correct permissions
# Ensure token hasn't expired
```

#### "Repository not found" error
```bash
# Verify DOCKER_USERNAME matches Docker Hub username exactly
# Check if repository exists in Docker Hub
# Ensure token has write permissions
```

#### Pipeline fails at Docker push
```bash
# Verify both DOCKER_USERNAME and DOCKER_PASSWORD are set
# Check Docker Hub service status
# Verify token permissions include Write access
```

## Testing Setup

### Manual Test
```bash
# Test Docker Hub login locally
echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin

# If successful, your credentials work
# If failed, check username/token
```

### Pipeline Test
```bash
# Create a test commit to trigger pipeline
git commit --allow-empty -m "Test CI/CD pipeline"
git push origin main

# Watch GitHub Actions tab for results
```

## Next Steps

After setting up secrets:

1. ✅ Fork this repository
2. ✅ Set up Docker Hub credentials
3. ✅ Add GitHub secrets
4. ✅ Update deployment.yaml with your Docker Hub username
5. ✅ Create a test commit
6. ✅ Watch the green checkmarks appear!

## Support

If you encounter issues:
- Check GitHub Actions logs for detailed error messages
- Verify Docker Hub token permissions
- Ensure repository settings allow Actions to run
- Review branch protection rules

---

**Security Note:** Never commit credentials to code. Always use GitHub secrets for sensitive information.