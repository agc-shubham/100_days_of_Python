# Send Email using smtplib
## If you are getting the error Connection unexpectedly closed, it might be due to a number of things.
1. Make sure you've got the correct smtp address for your email provider:
    * Gmail: smtp.gmail.com
    * Hotmail: smtp.live.com
    * Outlook: outlook.office365.com
    * Yahoo: smtp.mail.yahoo.com
    * If you use another email provider, just Google for your email provider e.g. "Gmail SMTP address"
2. Make sure you've enabled less secure apps if you are sending from a Gmail account.
3. Try to go through the Gmail Captcha here while logged in to the Gmail account: https://accounts.google.com/DisplayUnlockCaptcha
4. Add a port number by changing your code to this: `smtplib.SMTP("smtp.gmail.com", port=587)`