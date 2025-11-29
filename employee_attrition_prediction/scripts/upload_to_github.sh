#!/bin/bash

# GitHub Upload Script
# Pushes the Employee Attrition project to GitHub

echo "🚀 GitHub Upload Script"
echo ""

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "❌ Not a git repository. Run from project root."
    exit 1
fi

# Check if remote already exists
if git remote | grep -q origin; then
    echo "ℹ️  Remote 'origin' already exists:"
    git remote -v
    echo ""
    read -p "Do you want to replace it? (y/n): " replace
    if [ "$replace" = "y" ]; then
        echo "📝 Enter your GitHub repository URL:"
        read repo_url
        git remote remove origin
        git remote add origin "$repo_url"
    fi
else
    echo "📝 Enter your GitHub repository URL (e.g., https://github.com/username/repo.git):"
    read repo_url
    
    if [ -z "$repo_url" ]; then
        echo "❌ No URL provided. Exiting."
        exit 1
    fi
    
    git remote add origin "$repo_url"
    echo "✅ Remote added"
fi

echo ""
echo "📤 Pushing to GitHub..."

# Push to main/master branch
git branch -M main
git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Successfully pushed to GitHub!"
    echo "🌐 View your repository:"
    git remote get-url origin
else
    echo ""
    echo "❌ Push failed. Common issues:"
    echo "   1. Repository doesn't exist on GitHub - create it first"
    echo "   2. Authentication failed - set up SSH keys or personal access token"
    echo "   3. Permission denied - check repository access"
fi
