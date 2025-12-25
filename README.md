# telegram-reaction-bot

This repository runs a Telegram bot that automatically adds reactions to channel posts.

Quick start (recommended flow):
1. Add repository secrets (Settings → Secrets → Actions):
   - TELEGRAM_BOT_TOKEN: your bot token
   - (optional) KOYEB_TOKEN: your Koyeb API token
   - (optional) KOYEB_SERVICE_ID: the Koyeb service id to trigger deployments

2. Push to main. GitHub Actions will build and push a Docker image to GitHub Container Registry.
3. If you provide KOYEB_TOKEN and KOYEB_SERVICE_ID the workflow will trigger a deployment update on Koyeb.

Koyeb notes:
- To keep the bot running 24/7 without interruption, use a paid plan or ensure your app does not scale-to-zero.
- Alternatively, you can deploy the built image from ghcr.io to Koyeb using the Koyeb dashboard and enable automatic redeploy on new image.

Running locally:
- Set TELEGRAM_BOT_TOKEN in your environment and run:
  ```
  python bot2.py
  ```
