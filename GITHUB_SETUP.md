# WebtroopsScreen Draw - GitHub Repository Structure

This repository contains a professional screen drawing tool that allows you to draw directly on your screen.

## GitHub Repository Setup Instructions

1. Create a new repository on GitHub named "WebTroopScreenDraw"

2. Initialize the repository with these files:
   - README.md
   - LICENSE
   - .gitignore

3. Clone the repository to your local machine and push the code:

```
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YourUsername/WebTroopScreenDraw.git
git push -u origin main
```

4. Create releases by:
   - Building the installer using build_installer.py
   - Going to the GitHub repository
   - Click on "Releases" > "Create a new release"
   - Tag version: v1.0.0
   - Title: WebtroopsScreen Draw v1.0.0
   - Description: Initial release of WebtroopsScreen Draw
   - Attach the installer file from the dist folder
   - Publish release

## Important GitHub Pages

Consider setting up GitHub Pages to create a landing page for your application:

1. Go to repository Settings > Pages
2. Select main branch and root folder
3. Save and wait for deployment
4. Customize the page with more details about your application

## Workflow for Updates

1. Make changes to the code
2. Update version numbers in:
   - setup.py
   - build_installer.py
3. Run build_installer.py to create a new installer
4. Commit and push changes to GitHub
5. Create a new release with the new installer

## GitHub Actions (Optional)

You can set up GitHub Actions to automatically build the installer when you push to the main branch.
Create a .github/workflows/build.yml file with the necessary configuration.
